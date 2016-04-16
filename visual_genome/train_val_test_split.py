import os
import random
import numpy as np
import json
image_path = '/media/researchshare/linjie/data/visual-genome/images/'
region_path= '/media/researchshare/linjie/data/visual-genome/region_descriptions.json'
image_regions = json.load(open(region_path))
valid_im_ids = []
for item in image_regions:
	if 50 >= len(item['regions']) >= 20:
		valid_im_ids.append(item['id'])

#image_list = os.listdir(image_path)
random.seed(10)
random.shuffle(valid_im_ids)
tot_n = len(valid_im_ids)
val_n = 5000
test_n = 5000
train_n = tot_n - val_n - test_n
with open('train_ids.txt','w') as f:
	for i in xrange(train_n):
		f.write(str(valid_im_ids[i])+'\n')
with open('val_ids.txt','w') as f:
	for i in xrange(train_n, train_n + val_n):
		f.write(str(valid_im_ids[i])+'\n')
with open('test_ids.txt','w') as f:
	for i in xrange(train_n +val_n, tot_n):
		f.write(str(valid_im_ids[i])+'\n')
