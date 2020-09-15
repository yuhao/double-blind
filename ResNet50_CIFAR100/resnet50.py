"""
Taken from https://github.com/Ecohnoch/tensorflow-cifar100/blob/master/model/resnet50.py
Then made modifications to adapt it to fit with the other scripts and their file structure.
"""

import tensorflow as tf 
from tensorflow.keras import Input
from tensorflow.keras.layers import Conv2D, BatchNormalization, PReLU, ReLU, Add, InputLayer, Dense, GlobalAveragePooling2D#, Softmax
from tensorflow.keras.initializers import GlorotNormal, Zeros
#import numpy as np 

def conv2d(input_tensor, filters, kernel_size, strides, act=None, padding='same', w_init=None, b_init=None, name=None):
    return Conv2D(filters=filters, kernel_size=kernel_size, strides=strides, activation=act, padding=padding, kernel_initializer=w_init, bias_initializer=b_init, name=name)(input_tensor)

def bn(input_tensor, is_train, name=None):
    x = BatchNormalization(name=name)(inputs=input_tensor,training=is_train)
    return  ReLU()(x)

def prelu(input_tensor):
	return PReLU()(input_tensor)

def identity_block2d(input_tensor, kernel_size, filters, stage, block, is_training, reuse, kernel_initializer=None):
    filters1, filters2, filters3 = filters

    conv_name_1 = 'conv' + str(stage) + '_' + str(block) + '_1x1_reduce'
    bn_name_1   = 'bn'   + str(stage) + '_' + str(block) + '_1x1_reduce'

    x = conv2d(input_tensor, filters1, kernel_size=1, strides=(1,1), padding='same', w_init=kernel_initializer, name=conv_name_1)
    x = bn(x, is_train=is_training, name=bn_name_1)

    conv_name_2 = 'conv' + str(stage) + '_' + str(block) + '_3x3'
    bn_name_2   = 'bn'   + str(stage) + '_' + str(block) + '_3x3'
    x = conv2d(x, filters2, kernel_size=kernel_size, strides=(1,1), padding='same', w_init=kernel_initializer, name=conv_name_2)
    x = bn(x, is_train=is_training, name=bn_name_2)

    conv_name_3 = 'conv' + str(stage) + '_' + str(block) + '_1x1_increase'
    bn_name_3   = 'bn'   + str(stage) + '_' + str(block) + '_1x1_increase'
    x = conv2d(x, filters3, kernel_size=1, strides=(1,1), padding='same', w_init=kernel_initializer, name=conv_name_3)
    x = bn(x, is_train=is_training, name=bn_name_3)
	
    #x = tl.layers.ElementwiseLayer([x, input_tensor], combine_fn=tf.add, act=tf.nn.relu, name=str(stage)+str(block)+'elementwise')
    x = Add(name=(str(stage)+str(block)+'elementwise'))([x, input_tensor])
    return ReLU()(x)


def conv_block_2d(input_tensor, kernel_size, filters, stage, block, is_training, reuse, strides=(2, 2), kernel_initializer=None):
    filters1, filters2, filters3 = filters

    conv_name_1 = 'conv' + str(stage) + '_' + str(block) + '_1x1_reduce'
    bn_name_1   = 'bn'   + str(stage) + '_' + str(block) + '_1x1_reduce'
    x = conv2d(input_tensor, filters1, kernel_size=1, strides=strides, padding='same', w_init=kernel_initializer, name=conv_name_1)
    x = bn(x, is_train=is_training, name=bn_name_1)

    conv_name_2 = 'conv' + str(stage) + '_' + str(block) + '_3x3'
    bn_name_2   = 'bn'   + str(stage) + '_' + str(block) + '_3x3'
    x = conv2d(x, filters2, kernel_size=kernel_size, strides=(1,1), padding='same', w_init=kernel_initializer, name=conv_name_2)
    x = bn(x, is_train=is_training, name=bn_name_2)

    conv_name_3 = 'conv' + str(stage) + '_' + str(block) + '_1x1_increase'
    bn_name_3   = 'bn'   + str(stage) + '_' + str(block) + '_1x1_increase'
    x = conv2d(x, filters3, kernel_size=1, strides=(1,1), padding='same', w_init=kernel_initializer, name=conv_name_3)
    x = bn(x, is_train=is_training, name=bn_name_3)

    conv_name_4 = 'conv' + str(stage) + '_' + str(block) + '_1x1_shortcut'
    bn_name_4   = 'bn'   + str(stage) + '_' + str(block) + '_1x1_shortcut'
    shortcut = conv2d(input_tensor, filters3, kernel_size=1, strides=strides, padding='same', w_init=kernel_initializer, name=conv_name_4)
    shortcut = bn(shortcut, is_train=is_training, name=bn_name_4)
    #x = tl.layers.ElementwiseLayer([x, shortcut], combine_fn=tf.add, act=tf.nn.relu, name=str(stage)+str(block)+'elementwise')
    x = Add(name=(str(stage)+str(block)+'elementwise'))([x, shortcut])
    return ReLU()(x)

def get_resnet(input_tensor, block, is_training, reuse, kernel_initializer=None):
    #3, 4, 16, 3
    with tf.compat.v1.variable_scope('scope', reuse=reuse):
        #x = InputLayer(name='inputs')(input_tensor)
        x = input_tensor
        x = conv2d(x, 64, (3,3), strides=(1,1), padding='same', w_init=kernel_initializer, name='face_conv1_1/3x3_s1')
        x = bn(x, is_train=is_training, name='face_bn1_1/3x3_s1')

        x = conv_block_2d(x, 3, [64, 64, 256], stage=2, block='face_1a', is_training=is_training, reuse=reuse, strides=(1,1), kernel_initializer=kernel_initializer)
        for first_block in range(block[0] - 1):
            x = identity_block2d(x, 3, [64, 64, 256], stage='1b_{}'.format(first_block), block='face_{}'.format(first_block), is_training=is_training, reuse=reuse, kernel_initializer=kernel_initializer)

        x = conv_block_2d(x, 3, [128, 128, 512], stage=3, block='face_2a', is_training=is_training, reuse=reuse, kernel_initializer=kernel_initializer)
        for second_block in range(block[1] - 1):
            x = identity_block2d(x, 3, [128, 128, 512], stage='2b_{}'.format(second_block), block='face_{}'.format(second_block), is_training=is_training, reuse=reuse, kernel_initializer=kernel_initializer)

        x = conv_block_2d(x, 3, [256, 256, 1024], stage=4, block='face_3a' , is_training=is_training, reuse=reuse, kernel_initializer=kernel_initializer)
        for third_block in range(block[2] - 1):
            x = identity_block2d(x, 3, [256, 256, 1024], stage='3b_{}'.format(third_block), block='face_{}'.format(third_block), is_training=is_training, reuse=reuse, kernel_initializer=kernel_initializer)
		
        x = conv_block_2d(x, 3, [512, 512, 2048], stage=5, block='face_4a', is_training=is_training, reuse=reuse, kernel_initializer=kernel_initializer)
        for fourth_block in range(block[3] - 1):
            x = identity_block2d(x, 3, [512, 512, 2048], stage='4b_{}'.format(fourth_block), block='face_{}'.format(fourth_block), is_training=is_training, reuse=reuse, kernel_initializer=kernel_initializer)
		
        #pooling_output = tf.layers.max_pooling2d(x4, (7,7), strides=(1,1), name='mpool2')
        #print('before gap: ', x)
        pooling_output = GlobalAveragePooling2D(name='gap')(x)
        fc_output = Dense(units=100, activation="softmax", kernel_initializer=GlorotNormal(), bias_initializer=Zeros(), name='face_fc1')(pooling_output)
        return fc_output

def resnet50(input_tensor, is_training, reuse, kernel_initializer=None):
    return get_resnet(input_tensor, [3,4,6,3], is_training, reuse, kernel_initializer)

#def resnet110(input_tensor, is_training, reuse, kernel_initializer=None):
#	return get_resnet(input_tensor, [3,4,23,3], is_training, reuse, kernel_initializer)

#def resnet152(input_tensor, is_training, reuse, kernel_initializer=None):
#	return get_resnet(input_tensor, [3,8,36,3], is_training, reuse, kernel_initializer)


def resnet50_model():
    #x = tf.placeholder(tf.float32, [None, 32, 32, 3])
    x = Input(shape=(32,32,3))
    y = resnet50(x, is_training=True, reuse=False)
    model = tf.keras.Model(inputs=x, outputs=y)
    return model


