import os
im_dir = '/media/researchshare/linjie/data/snapchat/story_images/'
im_list = os.listdir(im_dir)
sav_name = 'test_list.txt'
fout = open(sav_name,'w')
for im_name in im_list:
	fout.write('%s%s 0\n' % (im_dir,im_name))
fout.close()
