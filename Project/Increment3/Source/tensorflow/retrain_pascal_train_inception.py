import numpy as np
import tensorflow as tf
import scipy.misc as sci

data = np.load('data/data.npy')
labels_b =np.load ('data/labels_xy_new.npy')

path='/home/prudhvi/Desktop/inc 3/inception/inception/classify_image_graph_def.pb';

JPEG_DATA_TENSOR_NAME = 'DecodeJpeg/contents:0'
tensor_name_input_image = "DecodeJpeg:0"
RESIZED_INPUT_TENSOR_NAME = 'ResizeBilinear:0'
BOTTLENECK_TENSOR_NAME = 'pool_3/_reshape:0'


MODEL_INPUT_WIDTH = 299
MODEL_INPUT_HEIGHT = 299
MODEL_INPUT_DEPTH = 3

BOTTLENECK_TENSOR_SIZE = 2048

CLASSES=3;

ittarate=500;

fc1=350
fc2=75
fc3=4


input_tensor = tf.placeholder(tf.float32,[None, BOTTLENECK_TENSOR_SIZE],name='1')

label_tensor = tf.placeholder(tf.float32, [None, 4],name='output_transfer')





weights={
'wc1': tf.Variable(tf.random_normal([BOTTLENECK_TENSOR_SIZE,fc1]),name='weight1'),
'wc2': tf.Variable(tf.random_normal([fc1,fc2]),name='weight2'),
'wc3': tf.Variable(tf.random_normal([fc2,fc3]),name='weight2'),}


tf.summary.histogram('weights1', weights['wc1'])
tf.summary.histogram('weights2', weights['wc2'])

bias={
    'bc1': tf.Variable(tf.random_normal([fc1]),name='bias1'),
    'bc2': tf.Variable(tf.random_normal([fc2]),name='bias2'),
'bc3': tf.Variable(tf.random_normal([fc3]),name='bias2'), }


def resh_299(data):
    im_resize = sci.imresize(data, (299, 299, 3))
    return im_resize



#graph = tf.get_default_graph()
f= tf.gfile.FastGFile(path, 'rb')
graph_def = tf.GraphDef()
graph_def.ParseFromString(f.read())


bottleneck_tensor, jpeg_data_tensor, resized_input_tensor = (
    tf.import_graph_def(graph_def, name='', return_elements=[
        BOTTLENECK_TENSOR_NAME, JPEG_DATA_TENSOR_NAME,
        RESIZED_INPUT_TENSOR_NAME]))

transfer_pascal=np.zeros([1,2048])

with tf.Session() as sess:
 for i in range(0,len(data)):
  transfer_values = sess.run(bottleneck_tensor, feed_dict={tensor_name_input_image:resh_299(data[i])})
  print(i)
  transfer_pascal=np.vstack((transfer_pascal,transfer_values))
transfer_pascal_1 = transfer_pascal[1:, :]

np.save('trasfer_pascel.npy', transfer_pascal_1)







transfer_pascal_1=np.float32(np.load('trasfer_pascel.npy'))




#dense = tf.layers.dense(inputs=input_tensor, units=fc1, activation=tf.nn.relu)
#dense1 = tf.layers.dense(inputs=dense, units=fc2, activation=tf.nn.relu)
#dense2 = tf.layers.dense(inputs=dense, units=fc3, activation=tf.nn.relu)
#loss=tf.nn.l2_loss(label_tensor-dense2)


dense = tf.nn.sigmoid(tf.add(tf.matmul(input_tensor,weights['wc1']),bias['bc1']))

dense1 = tf.nn.relu(tf.add((tf.matmul(dense, weights['wc2'])),bias['bc2']))

dense2=tf.nn.relu(tf.add(tf.matmul(dense1, weights['wc3']),bias['bc3']))

loss=tf.nn.l2_loss(label_tensor-dense2)
train_op = tf.train.GradientDescentOptimizer(1).minimize(loss)


tf.summary.histogram('loss', loss)
merged = tf.summary.merge_all()



#sess=tf.Session()
with tf.Session() as sess:
 trainwriter = tf.summary.FileWriter('data/logs', sess.graph)
 sess.run(tf.global_variables_initializer())
 for i1 in range(0,100):
    summary,gradient,loss_=sess.run([merged,train_op,loss],feed_dict={input_tensor: transfer_pascal_1,label_tensor:labels_b})
    trainwriter.add_summary(summary, i1)
    print(i1)
    print('test loss %g', loss_)
    #print('gradient loss %g', gradient)







