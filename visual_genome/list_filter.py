import os
base_dir = '/media/researchshare/linjie/data/visual-genome/densecap_splits/'
split_name = 'train'
filename = '%s.txt' % split_name
sav_name = '%s_filt.txt' % split_name
fout = open(base_dir + sav_name,'w')
with open(base_dir + filename) as f:
	for line in f:
		test_id = line.strip()[:-4]
		if test_id.isdigit():
			fout.write('%s\n' % test_id)

