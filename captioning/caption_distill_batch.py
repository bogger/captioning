import re
import os
import sys
import json
import nltk
import time
from nltk.tokenize import StanfordTokenizer 
from nltk.tag import StanfordNERTagger#try nltk binding for stanford NER
filtered_items={'LOCATION':0,'ORGANIZATION':1,'PERSON':2,'DATE':3,'TIME':4}
mask_strings=['','something','someone','','']
filtered_pred = ['in','on','at','during','until','from','to',',','of']
st = StanfordNERTagger('english.muc.7class.distsim.crf.ser.gz')
	
def caption_distill(caps):
	#preprocessing
	cap_n = len(caps)
	for i in xrange(cap_n):
		caps[i] = caps[i].translate(None,'"')
		caps[i] = caps[i].replace(':','.')
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
	#correct date tags
	for i in xrange(cap_n):
		for j,pair in enumerate(tags_sents[i]):
			if re.match(r'(\d+-\d+-\d+)',pair[0]) is not None:
				tags_sents[i][j] = (pair[0],'DATE')
	print tags_sents
	t4=time.time()
	#distill string according to tags
	caps_res=[]
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
					tokens[i] = mask_strings[item_id]
		tokens_filt = [t for i,t in enumerate(tokens) if del_tag[i] == False]
		cap_filt = ' '.join(tokens_filt)
		print cap_filt
		sentences = cap_filt.split('.')
		sent_longest = max(sentences, key=len)
		caps_res.append(sent_longest.strip())
	
	t5=time.time()
	print 'time of all stages: %f %f %f %f' % (t2-t1, t3-t2, t4-t3, t5-t4)
	
	return caps_res

if __name__ == '__main__':


	sl_ids = [8,14,15,32,39,44,50,60,69,76,78,79,82,92,93,90,88,87,97]
	#n = len(sl_id)
	cap_path = 'captions_all.txt'
	sav_path = 'captions_distill.txt'
	with open(cap_path,'r') as f:
		captions = [line.strip() for line in f]
	captions = [captions[i-1] for i in sl_ids]
	batch_size = 10000
	cap_n = len(captions)

	with open(sav_path,'w') as f:
		for i in xrange(0, cap_n, batch_size):
			#for i,cap in enumerate(captions):
			print('%d captions processed' % i)
		
			cap_batch = captions[i:min(i+batch_size, cap_n)]
			caps_new = caption_distill(cap_batch)
			#print cap_new
			for cap in caps_new:
				f.write(cap+'\n')

