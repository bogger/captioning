import os
import itertools
import numpy as np
import cPickle
from collections import Counter
from sklearn.neighbors import NearestNeighbors
src_tag = 'val'
base_dir = '/media/researchshare/linjie/data/'
target_path = base_dir + 'snapchat/features/vgg.bin'
src_path = base_dir + 'dreamstime/features/vgg_'+src_tag+'.bin'
target = cPickle.load(open(target_path,'rb'))
src = cPickle.load(open(src_path,'rb'))
#sample src for quick debugging
#src = src[:1000][:]
keyw_path = base_dir + 'dreamstime/keywords_dreamstime_list'
keywords = cPickle.load(open(keyw_path,'rb'))
list_path = '%s_list.txt' % src_tag
with open(list_path,'r') as f:
	image_list = [line.strip('\n') for line in f]
image_n = len(image_list)
feature_n = src.shape[0]
print image_n
print feature_n
tg_list_path = '../snapchat/test_list.txt'
with open(tg_list_path,'r') as f:
	tg_im_list = [line.strip() for line in f]
tg_im_n = len(tg_im_list)
tg_feat_n = target.shape[0]
print tg_im_n
print tg_feat_n


nn=10
nbrs = NearestNeighbors(n_neighbors=nn, algorithm='ball_tree').fit(src)
distances, indices = nbrs.kneighbors(target)
print indices.shape
target_n = target.shape[0]
keyword_top = 8
top_words = []
for i in xrange(target_n):
	#print image_list[indices[i][0]]
	keywords_c =list(itertools.chain(* [keywords[image_list[indices[i][x]][:-6].split('/')[-1]] \
	for x in xrange(nn)]))
	keywords_count = Counter(keywords_c)
	most_c = keywords_count.most_common(keyword_top)
	top_words.append([item[0] for item in most_c])

sav_file = '../snapchat/keywords_res.txt'
#print tg_im_list[0]
#print ' '.join(top_words[0])
with open(sav_file,'w') as f:
	for i in xrange(target_n):
		f.write('%s %s\n' % (tg_im_list[i][:-2],' '.join(top_words[i])))

