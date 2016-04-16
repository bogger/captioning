#import cv2 
#import skvideo.io
import glob
import os
from subprocess import call
#import os.listdir
video_dir = '/media/researchshare/linjie/data/UCF-101/'
im_dir = '/media/researchshare/linjie/data/UCF-101_images/'
fds = os.listdir(video_dir)
for fd in fds:
	video_names = glob.glob(video_dir+fd+'/*.avi')
	print video_names[0]
	for path in video_names:
		#vc = skvideo.io.VideoCapture(path)

		#c=1

		#if vc.isOpened():
			#rval , frame = vc.read()
		fd_name = im_dir+fd+'/'+path.split('/')[-1][0:-4]
		if not os.path.exists(fd_name):
			os.makedirs(fd_name)
		cmd = 'ffmpeg -i %s -r 24 %s/%%06d.jpg' % (path, fd_name)
		print cmd
		os.system(cmd)
		#while (True):
			#	rval, frame = vc.read()
				#if (type(frame) == type(None)):
				#if not rval:
				#	break
				#cv2.imwrite(fd_name + '/' + str(c) + '.jpg',frame)
				#print str(c) + '.jpg'
				#c = c + 1
				#cv2.waitKey(1)
		    #print "read the first frame, rval is " + str(rval)
		#else:
		#	rval = False
		#	print "cannot open video"


		    
		#vc.release()
