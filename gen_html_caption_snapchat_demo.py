import random
import os
import json
import cPickle
import csv
def gen_html(argv):
	sav_path = '/media/researchshare/linjie/data/snapchat/'
	image_dir ='story_images_sl/'
	#json_path_pre = '/home/a-linjieyang/work/caffe/caffe_s2vt/retrieval_cache/val/all_ims/lrcn_vgg_iter_100000/beam1/generation_result.json'
	iter_n = 100000
	beam_size = 5
	model = 'lrcn2_finetune_vgg'
	data = 'dreamstime'
	filename = 'image_captioning_demo'
	json_path = '/home/a-linjieyang/work/caffe/caffe_s2vt/retrieval_cache/snapchat/all_ims/%s_iter_%d/beam%d/generation_result.json' % (model,iter_n,beam_size)
	#id_path = 'selected_ids'
	#sl_ids = cPickle.load(open(id_path,'rb'))
	#captions = json.load(open(json_path_pre))
	captions = json.load(open(json_path))
	#random.seed(100)
	csv_path = 'caption_quality.csv'
	row_from = 1
	pos_col = 4
	neg_col = 5
	item_line = 6
	with open(csv_path,'rU') as f:
		reader = csv.reader(f)
		rows = [row for row in reader]
		pos_list = [int(r[pos_col]) for r in rows[row_from:] if len(r[pos_col])>0]
		neg_list = [int(r[neg_col]) for r in rows[row_from:] if len(r[neg_col])>0]
		print pos_list
		print neg_list
	
	
	
	page = open('%s%s.html' % (sav_path,filename),'w')
	page.write('<hr><h2>Automatic image captioning on snapchat images</h2>') 
	page.write('<hr><h3> correct samples </h3>')
	for n,i in enumerate(pos_list):
		if n % item_line == 0:
			page.write('<br>')
		cap_info = captions[i]
		im_path = cap_info['image_path'] 
		im_path = '/'.join(im_path.split('/')[6:])	
		#sl_ids.append(full_path)
		caption = cap_info['caption']
	#render head
		
		page.write('<div style=\'border: 2px solid; width:166px; height:360px; display:inline-table\'>')
		page.write('<image width="190" height = "288" src=\'%s\'></video><br> <hr><label>%s</label></div>' % (im_path, caption))
		
		
	page.write('<hr><h3> incorrect samples </h3>')
	for n,i in enumerate(neg_list):
		if n % item_line == 0:
			page.write('<br>')
	
		cap_info = captions[i]
		im_path = cap_info['image_path'] 
		im_path = '/'.join(im_path.split('/')[6:])	
		#sl_ids.append(full_path)
		caption = cap_info['caption']
	#render head
		
		page.write('<div style=\'border: 2px solid; width:166px; height:360px; display:inline-table\'>')
		page.write('<image width="190" height = "288" src=\'%s\'></video><br> <hr><label>%s</label></div>' % (im_path, caption))
	
	page.write('<hr>')
	page.close()
	#with open(id_path,'wb') as f:
	#	cPickle.dump(sl_ids, f)
	
if __name__ == '__main__':
	import sys
	gen_html(sys.argv)
