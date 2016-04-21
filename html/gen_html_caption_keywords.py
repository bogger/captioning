import random
import os
import shutil
import json
import cPickle
import csv
def gen_html(argv):
	sav_path = '/media/researchshare/linjie/data/MS_COCO/'
	keyw_dir = 'snapeye_keywords'
	image_dir ='images_sl'
	csv_path = 'caption_stats.csv'
	row_from = 3
	pos_col = 4
	neg_col = 5
	with open(csv_path,'rU') as f:
		reader = csv.reader(f)
		rows = [row for row in reader]
		pos_list = [int(r[pos_col]) for r in rows[row_from:] if len(r[pos_col])>0]
		neg_list = [int(r[neg_col]) for r in rows[row_from:] if len(r[neg_col])>0]
		print pos_list
		print neg_list
	
	full_list = pos_list+neg_list
	#exit()
	#image_sav_dir = 'images_sl'
	
	#json_path_pre = '/home/a-linjieyang/work/caffe/caffe_s2vt/retrieval_cache/val/all_ims/lrcn_vgg_iter_100000/beam1/generation_result.json'
	iter_n = 40000
	#filename = 'coco'
	beam_size = 5
	data = 'coco'
	test_data = 'coco'
	filename = 'caption_keywords_%s' % test_data
	json_path = '/home/a-linjieyang/work/caffe/caffe_s2vt/retrieval_cache/val/100_ims/lrcn_finetune_vgg_iter_%d/beam%d/generation_result.json' % (iter_n,beam_size)
	#id_path = 'selected_ids'
	#sl_ids = cPickle.load(open(id_path,'rb'))
	#captions = json.load(open(json_path_pre))
	captions_new = json.load(open(json_path))
	#random.seed(100)
	sl_n=len(full_list)
	item_each_line = 6
	page = open('%s%s.html' % (sav_path,filename),'w')
	page.write('<hr><h2>captions and keywords (captions training with %s and test with %s)</h2>' % (data, test_data)) 
	#if not os.path.exists(sav_path+image_sav_dir):
	#	os.mkdir(sav_path+image_sav_dir)
	for i in full_list:
		cap_info = captions_new[i]
		im_sav_path = '%s/COCO_val2014_%012d.jpg' % (image_dir, cap_info['image_id']) 
		keyw_path = '%s%s/COCO_val2014_%012d.txt' % (sav_path,keyw_dir,cap_info['image_id'])
		with open(keyw_path,'r') as f:
			keywords = [line.strip() for line in f]
		#im_path = '%s/COCO_val2014_%012d.jpg' % (image_dir, cap_info['image_id'])
		#shutil.copyfile(sav_path+im_path, sav_path+im_sav_path)
		#sl_ids.append(full_path)
		caption = cap_info['caption']
	#render head
		
		page.write('<div style=\'border: 2px solid; width:190px; height:570px; display:inline-table\'>')
		page.write('<image width="220" height = "300" src=\'%s\'></image><br> <hr><label>%s</label><hr> <label>%s</label> </div>' % (im_sav_path, caption, '<br>'.join(keywords)))
		
		
	page.write('<hr>')
	page.close()
	#with open(id_path,'wb') as f:
	#	cPickle.dump(sl_ids, f)
	
if __name__ == '__main__':
	import sys
	gen_html(sys.argv)
