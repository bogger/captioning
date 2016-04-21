import base64
import json
import os
import urllib2
import time
import multiprocessing

### TODO: REPLACE WITH YOUR COOKIE STRING
cookie_string = '~AJKiYcFAoHCnu4d428dsu9Rka5VBaEFci_BCRJSfzk059hGLf6-hdH2qhySHR6-95r2qn7EaMWmx3Q88p-p1IdnRH-ajhaFD4Zvzz9lZ-WUrYHxEdK7Q8EsIN6AOYLjDFReHmGEB-grrga1DVZR23lXC-WM0-9qCh1fx0wbBxUL9zVPwEN8Rt-5cBKROdoR8xKgBA1aXue7Z6n7h3RUwp-0plkAAQjup35qanCCz0BKtm4yvwar1W_n31hF589ge56jySLyxIs4-pmMTGgEI0fy-1BucYx--gdAzpigcvN_be9Fb3BPV7Y_Zy9dudUpcOdFpZ17d1pKOQg05rbIAn4ot9guT7EYwe_M7teZkQtv4xgKyqOot0pcG14RGKFZ_eUMOAyXoiOtBTqwyCeNSRlaPy_T7LcqWXRKgKGtLHv_BMOi1QRSO_MjFNlccL1BWM5aodlt-IrF4RxIajStT-ShodjvsmIeOdjlsoxwU2fbGSM7oAqENyFXKnLZXJeLFKf30DuMCtLNa25EWSABNXWRRrrLPCN8_BwNKuvOnFGAGHG-o-Qf_nG9tfaeNJFfiVHO7Z8PDzcTuMwYRY-y-WMP70vpkYBdY7VUyz3K29dclhtz_Z7ESU_zqj8DX67K6WWsHBs7VYtOsWMFK4ZWYkC_Z4Ack2tswW3BgWU3SKqkEaN56TOg_dc8OktWpsFAsCyU1OXfPp_iQC821ockcGKfrjYQwn4mcCBLDdv7lRFZUSu06y55Kogbf8lNEt29ZPg5S35fQd9jxpLz2uwft6489H50DYd2XOMqeCjnbrhCcLZWlKLmGXDEXTB8K2DznEjGncnzmP0Fe7S4necRkxx0b1V6whhIS5uIG6pie1QWRfVtdmmVff_CvU_qvQAXePgcWGk_p77VMpB3unixuFOJK1nbBMz9mh3LvS3jOiTX4xqKScZOQ3vc'
### TODO: REPLACE WITH YOUR INPUT/OUTPUT DIRECTORIES
data_base = '/media/researchshare/linjie/data/MS_COCO/'
in_dir = data_base+'images_sl/'
out_dir = data_base+'snapeye_keywords/'

# init variables
backend_address = 'https://snap-eye.appspot.com'
cookie_string = 'SACSID=' + cookie_string

def extract_feature(inputs):
  """ 
  Returns a tuple of (Status, result), where result is 
  a dictionary converted from the returned json message.
  """
  (media_name, media_name_out) = inputs
  print media_name + '\t' + media_name_out
  start = time.clock()

  # check if file exists
  if os.path.isfile(media_name_out):
    print "File already exists!"
    return

  query = dict()
  query['media_name'] = media_name
  ext_name = os.path.splitext(media_name)[-1]
  if ext_name == '.jpg':
    query['media_type'] = 'IMAGE_JPG'
  elif ext_name == '.mp4':
    query['media_type'] = 'VIDEO_MP4' 
  else:
    print "File type not supported: " + ext_name
    return 

  with open(media_name) as media_file:
    query['media_string'] = base64.b64encode(media_file.read())
  json_query = json.dumps(query)
  try:
    opener = urllib2.build_opener()
    opener.addheaders.append(('Cookie', cookie_string))
    result_message = opener.open(os.path.join(backend_address, 'ps'), json_query)
  except urllib2.HTTPError as url_error:
    print "Error opening the url: " + url_error.reason
    return 
  results = json.load(result_message)
  tags = results['results'][0]['tags']

  end = time.clock()
  print "Time elapsed: " + str(end - start)

  fout = open(media_name_out, 'w')
  fout.write("\n".join([str(x) for x in tags]))
  fout.close()


if __name__ == "__main__":

  # generate pool array
  pool_arr = []

  file_list = os.listdir(in_dir)
  for f_idx, f in enumerate(file_list):
    media_name = in_dir + f
    media_name_out = out_dir + os.path.splitext(f)[0] + '.txt'
    pool_arr.append((media_name, media_name_out))

  # set up pool
  pool = multiprocessing.Pool()
  pool.map(extract_feature, pool_arr)
  pool.close()
  pool.join()

  print "done!"
