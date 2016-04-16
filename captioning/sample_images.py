import os
import random
import shutil
im_dir ='/media/researchshare/linjie/data/dreamstime/images/'
sav_dir = '/media/researchshare/linjie/data/dreamstime/sample_images/'
sample_n = 5000
image_list = []
with open('real_image_list.txt','r') as f:
	for line in f:
		image_list.append(line[:-5]+'.jpg')

#image_list = os.listdir(im_dir)
image_n = len(image_list)
s = random.sample(image_list,sample_n)
for fname in s:
	shutil.copy(im_dir+fname,sav_dir)

