import os
base_dir ='/media/researchshare/linjie/data/captioning/'
sub_dirs = ['captions','captions2','captions3']
fout = open('real_image_list_all.txt','w')
real_files = 0
target_words=['abstract', 'vector', 'illustration', 'design', 'designs', 'sign', 'signs', 'concept', 'cartoon', 'icon', 'icons', 'logo', 'logos', 'badge', 'badges', 'symbol', 'symbols', 'seamless']
	
#caption_dir = '/media/researchshare/linjie/data/dreamstime/captions/'
for sub_dir in sub_dirs:
	caption_dir = base_dir + sub_dir
	files = os.listdir(caption_dir)
	#word_dict={}
	for i, fname in enumerate(files):
		if (i+1) % 10000 == 0:
			print '%d files processed' % (i+1)
		filepath = caption_dir + '/' +fname
		filepath_p = sub_dir + '/' + fname
		with open (filepath, 'r') as f:
			cap = f.read()
			#remove the trailing characters
			#cap = cap[:-2]
			cap = cap.lower()
			#cap is comprised of ASCII chars
			cap = cap.translate(None,'\',.!?&()[]:;\t0123456789@#-~')
			#cap.translate(' ','@#-~')
			words = cap.split()
			#is_abs = False
			
			if len(set(target_words) & set(words)) == 0:
				real_files += 1
				fout.write('%s\n' % filepath_p)

fout.close()
print '%s real images in total' % real_files

