import os
im_dir = '/media/researchshare/linjie/data/snapchat/story_images_sl/'
im_list = os.listdir(im_dir)
sav_path = 'test_im_list_cap.txt'
with open(sav_path,'w') as f:
	for name in im_list:
		f.write('%s%s\n' % (im_dir,name))


