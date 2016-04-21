#import cv2
#import skvideo.io
import glob
import os
from subprocess import call
#import os.listdir
video_dir = '/media/researchshare/linjie/data/snapchat/video/'
im_dir = '/media/researchshare/linjie/data/snapchat/images/'
video_names = glob.glob(video_dir+'*.mp4')
print video_names[0]
for path in video_names:
	#vc = cv2.VideoCapture(path)

	#c=1

	#if vc.isOpened():
		#rval , frame = vc.read()
	fd_name = im_dir+path.split('/')[-1][0:-4]
	if not os.path.exists(fd_name):
		os.mkdir(fd_name)
	
	cmd = 'ffmpeg -i %s -r 24 %s/%%06d.jpg' % (path, fd_name)
	print cmd
	os.system(cmd)
	    
	#vc.release()
