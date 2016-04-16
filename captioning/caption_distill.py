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
	
def caption_distill(cap):
	#preprocessing
	cap = cap.translate(None,'"')
	cap = cap.replace(':','.')
	cap = cap.replace(' - ',' . ') 
	#try stanford NER
	t1=time.time()
	tokens = nltk.word_tokenize(cap)#StanfordTokenizer().tokenize(cap)#
	t2=time.time()
	tags = st.tag(tokens)
	t3=time.time()
	#correct date tags
	for i,pair in enumerate(tags):
		if re.match(r'(\d+-\d+-\d+)',pair[0]) is not None:
			tags[i] = (pair[0],'DATE')
	t4=time.time()
	#distill string according to tags
	del_tag = [False] * len(tokens)
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
	t5=time.time()
	print 'time of all stages: %f %f %f %f' % (t2-t1, t3-t2, t4-t3, t5-t4)
	cap_filt = ' '.join(tokens_filt)
	#print cap_filt
	sentences = cap_filt.split('.')
	sent_longest = max(sentences, key=len)
	return sent_longest.lower()

if __name__ == '__main__':


	sl_ids = [8,14,15,32,39,44,50,60,69,76,78,79,82,92,93,90,88,87,97]
	#n = len(sl_id)
	cap_path = 'captions_all.txt'
	sav_path = 'captions_distill.txt'
	with open(cap_path,'r') as f:
		captions = [line.strip() for line in f]
	#cap_sl = [captions[i-1] for i in sl_ids]
	with open(sav_path,'w') as f:
		for i,cap in enumerate(captions):
			if (i % 1000)==0:
				print('%d captions processed' % i)
			cap_new = caption_distill(cap)
			#print cap_new
			f.write(cap_new+'\n')

