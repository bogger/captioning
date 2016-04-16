import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
cap_path = 'captions_all.txt'
with open(cap_path,'r') as f:
	caps = [line.strip() for line in f]
cap_n = len(caps)
cap_lens = np.zeros((cap_n,1),dtype = np.int32)
for i,cap in enumerate(caps):
	cap_lens[i] = len(cap)
#print cap_lens[-1]
idx = np.argsort(cap_lens,axis = 0)
#idx = list(reversed(idx))
#print caps.shape
print idx[0]
#print idx[-1]
for i in xrange(5):
	print caps[idx[i]]
	print cap_lens[idx[i]]
#	print idx[-i-1]
#	print -i-1
print 'min length of caption is %d, max length is %d' % (cap_lens.min(),cap_lens.max())
print 'there are %d empty caption' % np.sum(cap_lens==1)
#cap_lens_f = np.select([x<500,x>=500],[x,500])
cap_lens_f = cap_lens[cap_lens<500]
n, bins, patches = plt.hist(cap_lens_f, 30, alpha=0.75)
plt.title(r'captions length distribution of dreamstime data')
plt.grid(True)
plt.show()
plt.savefig('cap_len_dist.png')


