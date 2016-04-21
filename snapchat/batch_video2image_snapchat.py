import cv2
#import skvideo.io
import glob
import os
#import os.listdir
video_dir = '/media/researchshare/linjie/data/snapchat/video/'
im_dir = '/media/researchshare/linjie/data/snapchat/images/'
video_names = glob.glob(video_dir+'*.mp4')
print video_names[0]
for path in video_names:
	vc = cv2.VideoCapture(path)

	c=1

	if vc.isOpened():
		#rval , frame = vc.read()
		fd_name = im_dir+path.split('/')[-1][0:-4]
		if not os.path.exists(fd_name):
			os.mkdir(fd_name)
		while (True):
			rval, frame = vc.read()
			#if (type(frame) == type(None)):
			if not rval:
				break
			cv2.imwrite('%s/%06d.jpg' % (fd_name, c),frame)
			#print str(c) + '.jpg'
			c = c + 1
			#cv2.waitKey(1)
	    #print "read the first frame, rval is " + str(rval)
	else:
		rval = False
		print "cannot open video"


	    
	vc.release()
