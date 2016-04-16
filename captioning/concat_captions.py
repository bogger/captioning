import os
import json
sav_name = 'captions_all.txt'
list_name = 'real_valid_image_list_all.txt'
sub_dir_dict = {'images':'captions','images2':'captions2','images3':'captions3'}
cap_dir = '/media/researchshare/linjie/data/captioning/'
#fout = open(sav_name,'w')
image_captions = {}
with open(list_name,'r') as f:
	for line in f:
		im_name = line.strip()
		items = im_name.split('/')
		cap_name = sub_dir_dict[items[0]]+'/'+items[1][:-4]+'.txt'
		with open(cap_dir+cap_name,'r') as f2:
		
			image_captions[im_name] = f2.read().strip()
			print image_captions[im_name]
#fout.close()
with open('captions_all.json','w') as fout:
	json.dump(image_captions,fout)
