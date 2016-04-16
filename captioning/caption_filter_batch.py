import re
import os
import sys
import json
import nltk
import time
import numpy as np
from nltk.tokenize import StanfordTokenizer 
from nltk.tag import StanfordNERTagger#try nltk binding for stanford NER
filtered_items={'LOCATION':0,'ORGANIZATION':1,'PERSON':2,'DATE':3,'TIME':4}
mask_strings=['somewhere','something','someone','','']
filtered_pred = ['in','on','at','during','until','from','to',',','of']
st = StanfordNERTagger('english.muc.7class.distsim.crf.ser.gz')
	
def caption_distill(caps,imgs):
	#preprocessing
	cap_n = len(caps)
	for i in xrange(cap_n):
		caps[i] = caps[i].translate(None,'"\n')
		caps[i] = caps[i].replace(':','.')
		#caps[i] = caps[i].replace('\n','')
		caps[i] = caps[i].replace(' - ',' . ') 
		caps[i] = re.sub(r'\([^)]*\)','',caps[i])
	#try stanford NER
	t1=time.time()
	tokens_sents = [nltk.word_tokenize(cap) for cap in caps]#StanfordTokenizer().tokenize(cap)#
	t2=time.time()
	tags_sents = st.tag_sents(tokens_sents)
	if len(tags_sents)!=cap_n:
		print 'tags size %d not equal to caption size %d' % (len(tags_sents),cap_n)
	t3=time.time()
	#correct date tags: mm-dd-yy
	#correct date tags: in the {spring}
	for i in xrange(cap_n):
		for j,pair in enumerate(tags_sents[i]):
			if re.match(r'(\d+-\d+-\d+)',pair[0]) is not None:
				tags_sents[i][j] = (pair[0],'DATE')
			if (pair[1]=='DATE' or pair[1]=="TIME") and j>0 and tags_sents[i][j-1][0].lower()=='the':
				tags_sents[i][j] = (pair[0], 'O')
	t4=time.time()
	#distill string according to tags
	caps_res=[]
	imgs_res=[]
	cap_del=[False] * cap_n
	for j in xrange(cap_n):
		tags = tags_sents[j]
		tokens = tokens_sents[j]
		del_tag = [False] * len(tags)
		for i,pair in enumerate(tags):
			if pair[1] in filtered_items:
				item_id = filtered_items[pair[1]]
				if mask_strings[item_id]=='':
					del_tag[i] = True
					if i>0 and tokens[i-1] in filtered_pred:
						del_tag[i-1] = True
				elif i<len(tokens)-1 and tags[i+1][1]==pair[1]:
					del_tag[i] = True
				else:
					cap_del[j] = True
					break
					#tokens[i] = mask_strings[item_id]
		if not cap_del[j]:
			tokens_filt = [t for i,t in enumerate(tokens) if del_tag[i] == False]
			cap_filt = ' '.join(tokens_filt)
			#print cap_filt
			sentences = cap_filt.split('.')
			sent_longest = max(sentences, key=len)
			caps_res.append(sent_longest.strip())
			imgs_res.append(imgs[j])
	t5=time.time()
	print 'time of all stages: %f %f %f %f' % (t2-t1, t3-t2, t4-t3, t5-t4)
	print 'remained captions: %d' % len(caps_res)	
	return caps_res, imgs_res

if __name__ == '__main__':


	sl_ids = [8,14,15,32,39,44,50,60,69,76,78,79,82,92,93,90,88,87,97]
	#n = len(sl_id)
	cap_path = 'captions_all.json'
	#img_path = 'real_valid_image_list_all.txt'
	sav_path = 'captions_distill_all.txt'
	sav_im_path = 'images_distill_all.txt'
	with open(cap_path,'r') as f:
		captions_dict = json.load(f)
		#captions = [line.strip() for line in f]
	#with open(img_path,'r') as f:
	#	images = [line.strip() for line in f]
	
	#captions = [captions[i-1] for i in sl_ids]
	#assert(len(captions)==len(images))
	batch_size = 10000
		
	captions = [v.encode('ascii','ignore') for k,v in captions_dict.iteritems()]
	images = [k for k,v in captions_dict.iteritems()]
	cap_n = len(captions)

	with open(sav_path,'w') as f, open(sav_im_path,'w') as f2:
		for i in xrange(0, cap_n, batch_size):
			#for i,cap in enumerate(captions):
			print('%d captions processed' % i)
		
			cap_batch = captions[i:min(i+batch_size, cap_n)]
			img_batch = images[i:min(i+batch_size, cap_n)]
			caps_new, imgs_new = caption_distill(cap_batch, img_batch)
			
			#print cap_new
			for cap in caps_new:
				f.write(cap+'\n')
			for img in imgs_new:
				f2.write(img+'\n')

