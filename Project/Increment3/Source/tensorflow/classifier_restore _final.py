import tensorflow as tf
import numpy as np



saver = tf.train.import_meta_graph("/home/prudhvi/Desktop/inc_3/data/logs/model.meta")
sess = tf.Session()
saver.restore(sess, "/home/prudhvi/Desktop/inc_3/data/logs/model")

train= np.load('/home/prudhvi/Desktop/inc_3/inception/transfer_data.npy')


result = sess.run("Softmax:0", feed_dict={"input_transfer:0":np.reshape(train[1],(1,2048))})

