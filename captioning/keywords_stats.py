import os
import numpy as np
import cPickle as pickle
import itertools
from collections import Counter
base_dir = '/media/researchshare/linjie/data/captioning/'
list_path = 'train_list_all.txt'
with open(list_path,'r') as f:
	image_list = [line.strip().split()[0] for line in f]
image_n = len(image_list)
#key in keywords_all_list is image name without suffix '.jpg'
keys_list = [x.split('/')[-1][:-4] for x in image_list]
keyw_path = base_dir + 'keywords_all_list'
keywords = pickle.load(open(keyw_path,'rb'))
#collect keywords of images in image_list 
keywords_train = [keywords[key] for key in keys_list if key in keywords]
print 'There are %d images with keywords in the training set' % len(keywords_train)
all_keywords = list(itertools.chain(* keywords_train))
keywords_c = Counter(all_keywords)
top_n = 20000
keywords_top = keywords_c.most_common(top_n)
with open('keywords_all_freq.txt','w') as f:
	for pair in keywords_top:
		#save word and appearance time to file, filter all non-ascii characters
		f.write('%s %d\n' %(pair[0].encode('ascii','ignore'), pair[1]))
	

