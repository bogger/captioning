import os
import cPickle
base_dir = '/media/researchshare/linjie/data/'
keyw_path = base_dir + 'captioning/keywords_all_list'
keywords = cPickle.load(open(keyw_path,'rb'))
output_path = base_dir + 'captioning/keywords_all.txt'
with open(output_path,'w') as f:
	for k,v in keywords.iteritems():
		keyw_str = ' '.join(v)
		keyw_str = keyw_str.encode('ascii',errors='ignore')
		f.write(keyw_str+'\n')

