import tensorflow as tf
import sys
import re
import numpy as np
import matplotlib.pyplot as plt
import os
#print(sys.argv)
#print(sys.argv[0])
train_path ='/home/prudhvi/Desktop/pascal_data/TUDarmstadt/PNGImages/';
class_=os.listdir(train_path);  # collect the data folder names

names=[];

for i in range(0,len(class_)):
    n=os.listdir(train_path+'/'+class_[i])
    n.sort()                               # collect file names in each class
    names.append(n)

data=[];
num=0;


for i in range(0,len(class_)):
    for j in range(0,len(names[i])):
      a=plt.imread(train_path+'/'+class_[i]+'/'+names[i][j])  # get data matrix
      data.append(a)
      num=num+1


data=np.array(data);
#np.save('test.npy', data)

#d = np.load('test3.npy')

train_xy_path ='/home/prudhvi/Desktop/pascal_data/TUDarmstadt/Annotations/';
class1=os.listdir(train_xy_path);

labels_xy=[];

for i in range(0,len(class1)):
 dir=os.listdir(train_xy_path+'/'+class1[i])
 dir.sort()
 for i1 in range(0,len(dir)):
  f=open(train_xy_path+'/'+class1[i]+'/'+dir[i1],'r').read() #(Xmin, Ymin) - (Xmax, Ymax) : (205, 218) - (17, 105)
  f2=np.array((f.splitlines()))
  x=re.findall('\d+',f2[14])[1:5]
  labels_xy.append(x)


np.save('test.npy', data)
np.save('test_label_xy.npy', labels_xy)

d = np.load('test.npy')