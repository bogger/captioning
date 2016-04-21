import glob
import os
import shutil
import magic
vid_dir ='/media/researchshare/jianchao/trunk/story-analysis/our_story/media-downloads/'
sav_dir = '/media/researchshare/linjie/data/snapchat/story_images/'
fds = os.listdir(vid_dir)
sample_n = 5
for fd in fds:
	video_names = glob.glob(vid_dir+fd+'/*.jpg')
	for path in video_names[:sample_n]:
		if magic.from_file(path, mime=True) == 'image/jpeg':
			shutil.copy(path, sav_dir)

