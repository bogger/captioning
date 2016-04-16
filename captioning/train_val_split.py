import os
import random
base_dir = '/media/researchshare/linjie/data/captioning'
list_in = 'images_distill_all.txt'
list_train = 'train_list_all.txt'
list_val = 'val_list_all.txt'
list_cap_train = 'train_list_cap_all.txt'
list_cap_val = 'val_list_cap_all.txt'
list_cap_in = 'captions_distill_all.txt'
#fc=open(list_cap_in,'r')
cap_list=[]
file_list=[]
with open(list_in,'r') as fin:
	for line in fin:#line includes the \n at the end of line
		file_list.append(line)
with open(list_cap_in,'r') as fin:
	for line in fin:
		cap_list.append(line)
file_cap = zip(file_list, cap_list)
random.seed(1234)
random.shuffle(file_cap)
train_n = 4500000
test_n = len(file_cap) - train_n
f = open(list_train,'w') 
fc = open(list_cap_train,'w')
ft = open(list_val,'w')
fct = open(list_cap_val,'w')
for i in xrange(train_n):
	f.write('%s/%s 0\n' % (base_dir, file_cap[i][0][:-1]))
	fc.write(file_cap[i][1])
for i in xrange(train_n, len(file_cap)):
	ft.write('%s/%s 0\n' % (base_dir, file_cap[i][0][:-1]))
	fct.write(file_cap[i][1])
f.close()
fc.close()
ft.close()
fct.close()

