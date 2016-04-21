import random
import os
import json
import cPickle
def gen_html(argv):
	sav_path = '/media/researchshare/linjie/data/MS_COCO/'
	image_dir ='images/val2014'
	#json_path_pre = '/home/a-linjieyang/work/caffe/caffe_s2vt/retrieval_cache/val/all_ims/lrcn_vgg_iter_100000/beam1/generation_result.json'
	iter_n = 200000
	beam_size = 5
	filename = 'dt_beam%d' % beam_size
	json_path = '/home/a-linjieyang/work/caffe/caffe_s2vt/retrieval_cache/val/100_ims/lrcn_vgg_iter_%d/beam%d/generation_result.json' % (iter_n,beam_size)
	id_path = 'selected_ids'
	sl_ids = cPickle.load(open(id_path,'rb'))
	#captions = json.load(open(json_path_pre))
	captions_new = json.load(open(json_path))
	#random.seed(100)
	sl_n=100
	item_each_line = 6
	page = open('%s%s.html' % (sav_path,filename),'w')
	page.write('<hr><h2>caption samples training with dreamstime and test with coco iter %d</h2>' % iter_n)
	#print len(captions)
	#captions_sl = random.sample(captions, sl_n)
	#with open('selected_ids2.txt','w') as f:
	#	for cap in captions_sl:
	#		f.write('%d\n' % cap['image_id'])
	#exit()
	#id_set = set([cap['image_id'] for cap in captions_sl])
	#id_set_new = set([cap['image_id'] for cap in captions_new])
	#print id_set == id_set_new
	#print len(id_set)
	#print len(id_set_new)
	#cap_dict = {}
	#cap_dict_new = {}
	#for i,cap in enumerate(captions_sl):
	#	cap_dict[cap['image_id']] = i
	#for i,cap in enumerate(captions_new):
	#	cap_dict_new[cap_dict[cap['image_id']]] = i
	#sl_ids = []#[captions_sl[i]['image_id'] for i in xrange(sl_n)]
	for i in xrange(sl_n):
		cap_info = captions_new[i]
		im_path = '%s/COCO_val2014_%012d.jpg' % (image_dir, cap_info['image_id']) 
		full_path = sav_path + im_path
		#sl_ids.append(full_path)
		caption = cap_info['caption'][:-1]
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
