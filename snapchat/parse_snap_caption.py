import os
import json
import nltk
from nltk.tokenize import TweetTokenizer
import itertools
import subprocess
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
meta_file = 'meta-caption.json'
metadata = json.load(open(meta_file))
print type(metadata)
print metadata[0]
print len(metadata)
snap_dir = '/media/researchshare/jianchao/data/media-downloads/2015-12-15-2015-12-22'
#caption statistics
all_captions = []
all_length = []
all_files = []
tknzer = TweetTokenizer(strip_handles=True, reduce_len=True)
for item in metadata:
	tokens = tknzer.tokenize(item['overlay_text'].lower())
	if len(tokens) <= 20:
		all_files.append(item['id'])
		all_captions.append(tokens)
		all_length.append(len(tokens))
#word_freq = nltk.FreqDist(itertools.chain(*all_captions))
#print "Found %d unique word tokens" % len(word_freq.items())
#vocab_freq = word_freq.most_common(5000)
#vocab = [x[0] for x in vocab_freq]
#with open('caption_vocab.txt','w') as f:
#	for x in vocab_freq:
#		f.write('%s %d\n' % (x[0],x[1]))
#plt.hist(all_length)
#plt.savefig('hist.png')
all_file_captions = zip(all_files,all_captions)
#all_files --> extract images
sav_dir = '/media/researchshare/linjie/data/snapchat/video_frame/'
file_captions = {}
for vid_id,cap in all_file_captions:
	fd = vid_id.split('~')[0]
	vid_path = '%s/%s/%s.mp4' % (snap_dir, fd, vid_id)
	if not os.path.exists(vid_path):
		print '%s not exists' % vid_path
		exit()
	sav_path = '%s/%s.jpg' % (sav_dir, vid_id)
	try:
		duration = subprocess.check_output(["ffprobe", "-i", vid_path,"-show_entries",
		"format=duration","-v","quiet"])
	except subprocess.CalledProcessError as e:
		print "%s unreadable" % vid_path
		continue
	#valid videos with caption
	file_captions[vid_id] = cap
	t = float(duration.split('\n')[1][9:])
	print t
	#print duration
	#t = time.strptime(duration,'%H:%M:%S')
	mid_t = t/2 
	os.system("ffmpeg -ss %f -i %s -t 1 %s" % (mid_t, vid_path, sav_path))
with open('snapchat_video_captions.json','w') as f:
	json.dump(file_captions, f)
