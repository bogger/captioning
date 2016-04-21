import random
import os
import json
import cPickle
def gen_html(argv):
	sav_path = '/media/researchshare/linjie/data/snapchat/'
	image_dir ='breaking_news_cluster/'
	story_dir = 'story/'
	cluster_names = os.listdir(sav_path+image_dir)
	filename = 'story_samples'
	
	for i,name in enumerate(cluster_names):
		#read story information
		story = []
		with open(sav_path+story_dir+name+'.story','r') as f:
			for line in f:
				story.append(line.strip())
		sl_im_list = os.listdir(sav_path+story_dir+name)
		assert(len(sl_im_list) == len(story))
		#read cluster images
		cluster_images = os.listdir(sav_path+image_dir+name)
		page = open('%s%s_%d.html' % (sav_path,filename, i+1),'w')
		 

		page.write('<hr><h3> story %d </h3>' % (i+1))
		for im_id, cap in enumerate(story):
			page.write('<div style=\'border: 2px solid; width:166px; height:360px; display:inline-table\'>')
	
			page.write('<image width="190" height = "288" src=\'%s\'></image><br> <hr><label>%s</label></div>' % (story_dir+name+'/'+str(im_id)+'.jpg', cap))
		page.write('<hr><h3> source images of story %d </h3>' % (i+1))
		for im_name in cluster_images:
			page.write('<div style=\'border: 2px solid; width:166px; height:270px; display:inline-table\'>')
	
			page.write('<image width="190" height = "288" src=\'%s\'></image><br> </div>' % (image_dir+name+'/'+im_name))

	
		
		
		page.write('<hr>')
		page.close()
	#with open(id_path,'wb') as f:
	#	cPickle.dump(sl_ids, f)
	
if __name__ == '__main__':
	import sys
	gen_html(sys.argv)
