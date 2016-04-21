import glob
import os
import shutil
vid_dir ='/home/a-jianchaoyang/trunk/story-analysis/our_story/media-downloads/'
sav_dir = '/media/researchshare/linjie/data/snapchat/video/'
fds = os.listdir(vid_dir)
sample_n = 30
for fd in fds:
	video_names = glob.glob(vid_dir+fd+'/*.mp4')
	for path in video_names[:sample_n]:
		shutil.copy(path, sav_dir)

