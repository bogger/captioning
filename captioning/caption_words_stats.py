import os

caption_dir = '/media/researchshare/linjie/data/dreamstime/captions/'
files = os.listdir(caption_dir)
word_dict={}
for i, fname in enumerate(files):
	if (i+1) % 10000 == 0:
		print '%d files processed' % (i+1)
	with open (caption_dir+fname,'r') as f:
		cap = f.read()
		#remove the trailing characters
		#cap = cap[:-2]
		cap = cap.lower()
		#cap is comprised of ASCII chars
		cap = cap.translate(None,'\',.!?&()[]:;\t0123456789@#-~')
		#cap.translate(' ','@#-~')
		words = cap.split()
		for w in words:
			word_dict[w] = 1 if w not in word_dict else word_dict[w]+1
#del word_dict['']
#sorting
import operator
sorted_words = sorted(word_dict.items(), key=operator.itemgetter(1),reverse=True)
word_n = len(sorted_words)
show_n = 10000
print '%d words in total' % word_n
with open('word_freq.txt','w') as f:
	for pair in sorted_words[:show_n]:
		f.write('%s %d\n' % (pair[0], pair[1]))

