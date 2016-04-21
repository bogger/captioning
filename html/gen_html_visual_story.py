import random
import os
import json
import cPickle
def gen_html(argv):
	sav_path = '/media/researchshare/linjie/data/dreamstime/'
	res_path = '/home/a-linjieyang/work/video_caption/dreamstime/story/books_par.json'
	stories = json.load(open(res_path))
	stories = stories[1:]
	
	filename = 'text_to_visual_story_samples'
	page = open('%s%s.html' % (sav_path,filename),'w')
		 

	for i,story in enumerate(stories):
		#read story information
		page.write('<hr><h2> story %d </h2>' % (i+1))
		page.write('<hr>')
		for item in story:
			page.write('<h3>%s</h3><br>' % item['sentence'])
		page.write('<hr>')
		for item in story:
			#get the relative path
			im_path = '/'.join(item['image_path'].split('/')[6:])
			cap = item['caption']
			sent = item['sentence']
			page.write('<div style=\'border: 2px solid; width:166px; height:360px; display:inline-table\'>')
	
			page.write('<image width="190" height = "288" src=\'%s\'></image><br> <hr><label><i>caption:</i> %s</label><br><label> <i>original sentence: </i>%s</label></div>' % (im_path, cap, sent))
	
	page.write('<hr>')
	page.close()

if __name__ == '__main__':
	import sys
	gen_html(sys.argv)
