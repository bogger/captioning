import os
#import matplotlib as plt
base_dir = '/media/researchshare/linjie/data/snapchat/breaking_news_cluster/'
sav_path = 'cluster_im_list.txt'
fds = os.listdir(base_dir)
f = open(sav_path,'w')
for fd in fds:
	im_dir = base_dir+fd
	im_list = os.listdir(im_dir)
	for name in im_list:
		f.write('%s/%s\n' % (im_dir,name))
f.close()

