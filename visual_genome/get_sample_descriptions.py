import os
import json
import cv2
import numpy as np
base_dir = '/media/researchshare/linjie/data/visual-genome/'
im_dir = base_dir + 'images/'
json_path = base_dir + 'region_descriptions.json'
descriptions = json.load(open(json_path))
n = len(descriptions)
sample_id = 2342728
for desc in descriptions:
	if desc['id'] == sample_id:
		res=[desc]
		break
save_path = base_dir + 'sample_region_descriptions.json'
with open(save_path,'w') as f:
	json.dump(res, f)
meta_path = base_dir + 'image_data.json'
meta_data = json.load(open(meta_path))
for desc in meta_data:
	if desc['id']== sample_id:
		res=[desc]
		break
save_path = base_dir + 'sample_image_data.json'
with open(save_path,'w') as f:
	json.dump(res, f)
