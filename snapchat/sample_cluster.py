import os
import glob
import shutil
import json
import matplotlib.image as plt
base_dir = '/media/researchshare/kevin/breaking_news/intermediate-breaking-news-cluster/clusters/'
json_dir = base_dir + '../clusters_json/'
sav_dir = '/media/researchshare/linjie/data/snapchat/breaking_news_cluster/'
#only copy jpg images from base_dir
fds = os.listdir(base_dir)

im_range = range(100,200)
for fd in fds:
	im_list = glob.glob(base_dir+fd+'/*.jpg')
	print len(im_list)
	valid_list = []
	for im in im_list:
		try:
			
			plt.imread(im)
		except IOError as e:
			print e.message
			continue
		valid_list.append(im)

	if len(valid_list) in im_range:
		if not os.path.exists(sav_dir+fd):
			os.makedirs(sav_dir+fd)
		for im in valid_list:
			im_name = im.split('/')[-1]
			shutil.copy(im,sav_dir+fd+'/'+im_name)
	
