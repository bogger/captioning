import os
import magic
base_dir = '/media/researchshare/linjie/data/captioning/'
sub_dir_proj = {'captions':'images','captions2':'images2','captions3':'images3'}


list_in = 'real_image_list_all.txt'
list_out = 'real_valid_image_list_all.txt'
fout = open(list_out,'w')
with open(list_in,'r') as f:
	for line in f:
		items = line.strip().split('/')#example: captions/dagbfads.txt
			
		im_path_p =  sub_dir_proj[items[0]] + '/' + items[1][:-4] + '.jpg'
		im_path = base_dir + im_path_p	
		#a magic way to check file corruption
		if magic.from_file(im_path, mime=True) == 'image/jpeg':
			fout.write('%s\n' % im_path_p)
fout.close()
