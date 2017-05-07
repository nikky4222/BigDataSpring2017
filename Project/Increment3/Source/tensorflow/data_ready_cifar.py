import numpy as np
import pickle as p
#data set from https://www.cs.toronto.edu/~kriz/cifar-10-python.tar.gz

data_path = "/home/prudhvi/Desktop/source/inception/data/CIFAR-10/"

def data_prep_cifar10 (i,data_path):
    data_path_=data_path+i
    fo = open(data_path_, 'rb')
    fo.seek(0)
    dict_ = (p.load(fo, encoding='bytes'))
    l = np.array(dict_[b'labels'])
    d = np.array(dict_[b'data'])
    fo.close()
    return d,l
d1,l1=data_prep_cifar10('data_batch_1',data_path)
d2,l2=data_prep_cifar10('data_batch_2',data_path)
d3,l3=data_prep_cifar10('data_batch_3',data_path)
d4,l4=data_prep_cifar10('data_batch_4',data_path)
d5,l5=data_prep_cifar10('data_batch_5',data_path)

train_label = np.concatenate((l1,l2,l3,l4,l5))
train_data=np.concatenate((d1,d2,d3,d4,d5))

test_data,test_labels=data_prep_cifar10('test_batch',data_path)

data={"train_l":train_label ,"train_d":train_data,"test_l":test_labels,"test_d":test_labels}
p.dump( data, open( "/home/prudhvi/Desktop/source/inception/data/cifar.p", "wb" ) )


x=p.load( open( "cifar.p", "rb" ))