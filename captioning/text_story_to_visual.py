import os
import sys
import numpy as np
from sklearn.neighbors import NearestNeighbors
sys.path.append('/home/a-linjieyang/work/skip-thoughts/')
import skipthoughts
import time
import json
base_dir =  '/home/a-linjieyang/work/video_caption/dreamstime/'
feat_path = base_dir + 'captions_distill.npz'
cap_path = base_dir + 'captions_distill.txt'
imfile_path = base_dir + 'images_distill.txt'
print 'start loading dictionary...'
t1= time.time()
with np.load(feat_path) as feat:
	dict_features = feat['arr_0']
t2 = time.time()
print 'finished. %f seconds elapsed' % (t2 - t1) 
feat_n = len(dict_features)
print feat_n
captions = []
imfiles = []

with open(cap_path,'r') as f, open(imfile_path,'r') as fi:
	for line in f:
		sent = line.strip()
		im_path = fi.readline().strip()
		if len(sent)>0:
			captions.append(sent)
			imfiles.append(im_path)
captions = captions[:feat_n]
imfiles = imfiles[:feat_n]
if len(captions)!= feat_n or len(imfiles) != feat_n:
	print 'captions length %d, imfiles length %d' % (len(captions),len(imfiles))
	exit()

par_path = '/home/a-linjieyang/work/skip-thoughts/training/story_to_visual_sl.txt'
pars = []
with open(par_path,'r') as f:
	par = []
	for line in f:
		sent = line.strip()
		if len(sent) > 0:
			par.append(sent)
		else:
			pars.append(par)
			par = []
skip_model = skipthoughts.load_model()
nbrs = NearestNeighbors(n_neighbors=1, algorithm='ball_tree').fit(dict_features)
save_path = '/home/a-linjieyang/work/video_caption/dreamstime/story/'
stories = []
for i,par in enumerate(pars):
	ret_list = []
	for sent in par:
		#remove the last punctuation
		print sent
		sent_feat = skipthoughts.encode(skip_model, [sent[:-1].lower()])
		dist, ind = nbrs.kneighbors(sent_feat)
		ret_item = {}
		print ind[0]
		ret_item['caption'] = captions[ind[0]]
		ret_item['image_path'] = imfiles[ind[0]]
		ret_item['sentence'] = sent
		ret_list.append(ret_item)
	stories.append(ret_list)
#save results
with open(save_path+'books_par.json','w') as f:
	json.dump(stories, f)

		
	
