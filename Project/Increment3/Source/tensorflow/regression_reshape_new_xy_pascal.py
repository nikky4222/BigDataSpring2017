import re
import numpy as np
import matplotlib.pyplot as plt
import os
#import tensorflow as tf
#import resizeimage as pri



train_path ='/home/prudhvi/Desktop/pascal_data/TUDarmstadt/PNGImages/';
train_xy_path ='/home/prudhvi/Desktop/pascal_data/TUDarmstadt/Annotations/';


data_reshape_x=299
data_reshape_y=299

class_=os.listdir(train_path)   # collect the data folder names
class1=os.listdir(train_xy_path); # collect the label data folder names

names=[];

for i in range(0,len(class_)):
    n = os.listdir(train_path + '/' + class_[i])
    n.sort()  # collect file names in each class
    names.append(n)

data=[];
num=0;










for i in range(0,len(class_)):
    for j in range(0,len(names[i])):
      a=plt.imread(train_path+'/'+class_[i]+'/'+names[i][j])  # get data matrix
      data.append(a)
      num=num+1


data=np.array(data);


#################################################################################data



labels_xy=[];

for i in range(0,len(class1)):
 dir=os.listdir(train_xy_path+'/'+class1[i])
 dir.sort()
 for i1 in range(0,len(dir)):
  f=open(train_xy_path+'/'+class1[i]+'/'+dir[i1],'r').read() #(Xmin, Ymin) - (Xmax, Ymax) : (205, 218) - (17, 105)
  f2=np.array((f.splitlines()))
  for i2 in f2:
   if "Bounding box for object 1" in i2:
     x=re.findall('\d+',i2)[1:5]
     labels_xy.append(x)
     labels_xy=np.array(labels_xy)
####################################################################################labels for Bounding box for object 1



def reshape(data,label_xy,data_reshape_x,data_reshape_y):
    a=[]
    for i in range(0,len(labels_xy)):
        label_1=label_xy[i]
        shape_=data[i].shape
        print(shape_[0],shape_[1],'to ',data_reshape_x,data_reshape_y)
        x_=data_reshape_x/shape_[0];
        y_=  data_reshape_y/shape_[1] ;
        lab = [int(label_1[0])*x_,int(label_1[1])*y_,int(label_1[2])*x_,int(label_1[3])*y_]
        a.append(lab)

    return (a)


labels_xy_new = reshape(data, labels_xy, data_reshape_x, data_reshape_y)

np.save('data', data)
np.save('labels_xy_new',labels_xy_new)



#x=tf.image.resize_images(data[i],(299,299))
#sess=tf.Session()