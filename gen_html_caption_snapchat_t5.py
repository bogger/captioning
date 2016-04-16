import random
import os
import json
import cPickle
def gen_html(argv):
	sav_path = '/media/researchshare/linjie/data/snapchat/'
	image_dir ='story_images_sl/'
	#json_path_pre = '/home/a-linjieyang/work/caffe/caffe_s2vt/retrieval_cache/val/all_ims/lrcn_vgg_iter_100000/beam1/generation_result.json'
	iter_n = 100000
	beam_size = 20
	model = 'lrcn2_finetune_vgg'
	data = 'dreamstime'
	filename = 'caption_samples_t5_%s_word_prob' % (data)
	json_path = '/home/a-linjieyang/work/caffe/caffe_s2vt/retrieval_cache/snapchat/all_ims/%s_iter_%d/beam%d/generation_result_t5.json' % (model,iter_n,beam_size)
	#id_path = 'selected_ids'
	#sl_ids = cPickle.load(open(id_path,'rb'))
	#captions = json.load(open(json_path_pre))
	captions_all = json.load(open(json_path))
	#random.seed(100)
	sl_n=len(captions_all)
	cap_per_im = 5
	page = open('%s%s.html' % (sav_path,filename),'w')
	page.write('<hr><h2>caption samples training with %s and test with snapchat iter %d beam size %d</h2>' % (data, iter_n,beam_size))
	for i in xrange(sl_n):
		cap_info = captions_all[i]
		print cap_info
		im_path = cap_info['image_path'] 
		im_path = '/'.join(im_path.split('/')[6:])	
		#sl_ids.append(full_path)
		captions = cap_info['captions']
		cap_n = len(captions)
	#render head
		
		page.write('<div style=\'border: 2px solid; width:166px; height:500px; display:inline-table\'>')
		page.write('<image width="190" height = "288" src=\'%s\'></video><br> <hr>' % (im_path))
		for cap in captions:
			page.write('<label>%s</label> <br>' % cap)
		page.write('</div>')
		
	page.write('<hr>')
	page.close()
	#with open(id_path,'wb') as f:
	#	cPickle.dump(sl_ids, f)
	
if __name__ == '__main__':
	import sys
	gen_html(sys.argv)
