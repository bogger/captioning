import random
import os
import shutil
import json
import cPickle
def gen_html(argv):
	sav_path = '/media/researchshare/linjie/data/MS_COCO/'
	image_dir ='images/val2014'
	image_sav_dir = 'images_sl'
	
	#json_path_pre = '/home/a-linjieyang/work/caffe/caffe_s2vt/retrieval_cache/val/all_ims/lrcn_vgg_iter_100000/beam1/generation_result.json'
	iter_n = 40000
	#filename = 'coco'
	beam_size = 5
	filename = 'coco_beam%d' % beam_size
	json_path = '/home/a-linjieyang/work/caffe/caffe_s2vt/retrieval_cache/val/100_ims/lrcn_finetune_vgg_iter_%d/beam%d/generation_result.json' % (iter_n,beam_size)
	#id_path = 'selected_ids'
	#sl_ids = cPickle.load(open(id_path,'rb'))
	#captions = json.load(open(json_path_pre))
	captions_new = json.load(open(json_path))
	#random.seed(100)
	sl_n=100
	item_each_line = 6
	page = open('%s%s.html' % (sav_path,filename),'w')
	page.write('<hr><h2>caption samples training with coco and test with coco beam size %d</h2>' % beam_size)
	if not os.path.exists(sav_path+image_sav_dir):
		os.mkdir(sav_path+image_sav_dir)
	for i in xrange(sl_n):
		cap_info = captions_new[i]
		im_sav_path = '%s/COCO_val2014_%012d.jpg' % (image_sav_dir, cap_info['image_id']) 
		im_path = '%s/COCO_val2014_%012d.jpg' % (image_dir, cap_info['image_id'])
		shutil.copyfile(sav_path+im_path, sav_path+im_sav_path)
		#sl_ids.append(full_path)
		caption = cap_info['caption']
	#render head
		
		page.write('<div style=\'border: 2px solid; width:166px; height:360px; display:inline-table\'>')
		page.write('<image width="190" height = "288" src=\'%s\'></video><br> <hr><label>%s</label></div>' % (im_sav_path, caption))
		
		
	page.write('<hr>')
	page.close()
	#with open(id_path,'wb') as f:
	#	cPickle.dump(sl_ids, f)
	
if __name__ == '__main__':
	import sys
	gen_html(sys.argv)
