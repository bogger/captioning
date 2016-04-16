import os
import json
import cv2
import numpy as np
base_dir = '/media/researchshare/linjie/data/visual-genome/'
im_dir = base_dir + 'images/'
json_path = base_dir + 'region_descriptions.json'
descriptions = json.load(open(json_path))
n = len(descriptions)
print 'total image number %d' % n
for item in descriptions:
	im_id = item['id']
	im_name = '%d.jpg' % im_id
	im = cv2.imread(im_dir+im_name)
	im_shape = im.shape
	print im_shape
	#print item
	for obj in item['regions']:
		print obj
		w = obj['width']
		h = obj['height']
		x = obj['x']
		y = obj['y']
		x1 = x 
		x2 = x1 + w
		y1 = y 
		y2 = y1 + h
		im_new = np.copy(im)
		cv2.rectangle(im_new, (x1, y1), (x2, y2), (255,0,0), 2)
		cv2.imwrite('regions/%s_%d.jpg' % (obj['phrase'],obj['id']),im_new)
	break

