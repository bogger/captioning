from itertools import islice
import os
import cPickle
path = '/media/researchshare/linjie/data/captioning/keywords_all'
keywords_dict = cPickle.load(open(path))
keywords_dict_sp =dict([(k,v.split(', ')) for k,v in keywords_dict.iteritems()])
#for k,v in keywords_dict_sp.iteritems():
#	print k,v
with open(path+'_list','wb') as f:
	cPickle.dump(keywords_dict_sp,f,protocol=cPickle.HIGHEST_PROTOCOL)
