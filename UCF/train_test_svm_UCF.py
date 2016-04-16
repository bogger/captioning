import os
import numpy as np
import cPickle
from sklearn.svm import LinearSVC 
feat_dir = '/media/researchshare/linjie/data/UCF-101_features/'
models=('c3d','googlenet')
feat_len =(4096,1024)
#read training and testing labels
train_list = 'ucfTrainTestlist/trainlist01.txt'
class_list = 'ucfTrainTestlist/classInd.txt'
test_list = 'ucfTrainTestlist/testlist01.txt'
train_labels = []
test_labels = []
with open(train_list,'r') as f:
	for line in f:
		content = line.split()
		train_labels.append(int(content[1])-1)
class_idx = {}
class_names = []
with open(class_list,'r') as f:
	for line in f:
		content = line.split()
		class_idx[content[1]] = int(content[0])-1
		class_names.append(content[1])
with open(test_list,'r') as f:
	for line in f:
		test_labels.append(class_idx[line.split('/')[0]])
#C_list = [0.5,1.0,2.0]
class_n = len(class_idx)
class_acc = np.zeros((class_n,2),dtype=np.float32)
conf_matrix = np.zeros((class_n,class_n,2),dtype = np.float32)
for model_id in xrange(2):
	model = models[model_id]
	feat_n = feat_len[model_id]
	with open('%s%s_pooled_train' % (feat_dir,model),'rb') as fb:
		train_feats = cPickle.load(fb)
	with open('%s%s_pooled_test' % (feat_dir,model),'rb') as fb:
		test_feats = cPickle.load(fb)
	#normalize
	train_feats = train_feats/np.std(train_feats)
	print np.std(train_feats)
	#for c in C_list:
	svm = LinearSVC(C=1)
	svm.fit(train_feats,train_labels)
	pred_labels = svm.predict(test_feats)
	joint_labels = zip(pred_labels,test_labels)
	for i in xrange(class_n):
		class_sp = map(lambda a,b: a==i or b==i, test_labels, pred_labels).count(True)
		correct_sp = joint_labels.count((i,i))
		class_acc[i,model_id] = float(correct_sp) / class_sp
	for i in xrange(len(pred_labels)):
		conf_matrix[test_labels[i],pred_labels[i],model_id] += 1
	#for i in xrange(class_n):
	conf_matrix[:,:,model_id] = conf_matrix[:,:,model_id] / \
	np.sum(conf_matrix[:,:,model_id],axis=1)
class_acc_diff = class_acc[:,0] - class_acc[:,1]
idx = np.argsort(class_acc_diff)
idx = list(reversed(idx))
for i in xrange(class_n):
	conf_matrix[i,i,1] = 0
conf_max = np.argmax(conf_matrix[:,:,1],axis=1)
with open('class_ac_diff.txt','w') as f:
	for i in xrange(class_n):
		f.write('%.04f %s %s\n' % (class_acc_diff[idx[i]], \
		class_names[idx[i]], class_names[conf_max[idx[i]]]))
	#print "the accuracy of %s is %f with C %f" % (model, ac, c)

	
