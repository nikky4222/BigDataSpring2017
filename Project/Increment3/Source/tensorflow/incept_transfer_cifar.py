
import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np
import time
from datetime import timedelta
import os
import scipy.misc as sci
import hickle as hk
import pickle as p
# Functions and classes for loading and using the Inception inception.


# We use Pretty Tensor to define the new classifier.
import prettytensor as pt
#tf.__version__  '1.0.0'
#pt.__version__ '0.7.4'

#data set path
data_path='/home/prudhvi/Desktop/source/inception/data/cifar.p'
model_path='/inception'
x=p.load( open( data_path, "rb" ) )
test_images=x['test_d']    #len(test_images) 10000
test_labels=x['test_l']    #len(test_labels) 10000


train_images=x['train_d']   #len(train_images) 50000
train_labels=x['train_l']   #len(train_labels) 50000

#model_data_url='http://download.tensorflow.org/models/inception_v3_2016_08_28.tar.gz'

#////////////////////////////////////////////////////////////////////////////////

JPEG_DATA_TENSOR_NAME = 'DecodeJpeg/contents:0'
tensor_name_input_image = "DecodeJpeg:0"
RESIZED_INPUT_TENSOR_NAME = 'ResizeBilinear:0'
BOTTLENECK_TENSOR_NAME = 'pool_3/_reshape:0'

#/////////////////////////////////////////////////////////////////////////////////

MODEL_INPUT_WIDTH = 299
MODEL_INPUT_HEIGHT = 299
MODEL_INPUT_DEPTH = 3

BOTTLENECK_TENSOR_SIZE = 2048

path = "/home/prudhvi/Desktop/source/inception/inception/classify_image_graph_def.pb"
#//////////////////////////////creating a inception ///////////////////////////////////
def resh_299(data):
    im_reshape = np.reshape(data, (32, 32, 3))
    im_resize = sci.imresize(im_reshape, (299, 299, 3))
    return im_resize




sess=tf.Session()

#graph = tf.get_default_graph()

f= tf.gfile.FastGFile(path, 'rb')

graph_def = tf.GraphDef()

graph_def.ParseFromString(f.read())

bottleneck_tensor, jpeg_data_tensor, resized_input_tensor = (
    tf.import_graph_def(graph_def, name='', return_elements=[
        BOTTLENECK_TENSOR_NAME, JPEG_DATA_TENSOR_NAME,
        RESIZED_INPUT_TENSOR_NAME]))


#A frozen graph can be loaded using tf.import_graph_def(). In this case, the weights are (typically) embedded in the graph, so you don't need to load a separate checkpoint.
#transfer_layer = graph.get_tensor_by_name(tensor_name_transfer_layer)



transfer_values_data=np.zeros((1,2048))

for i in range(50000):
 transfer_values = sess.run(bottleneck_tensor, feed_dict={tensor_name_input_image:resh_299(train_images[i])})
 print(i)
 transfer_values_data=np.vstack((transfer_values_data,transfer_values))
transfer_values_data1=transfer_values_data[-0,:]
np.save('transfer_data.npy', transfer_values_data)
np.save('transfer_labels.npy',train_labels)
#transfer_data={"transfer_x":transfer_values_data}
#p.dump( transfer_data, open( "/home/prudhvi/Desktop/source/inception/data/transferdata_cifar.p", "wb" ) )









