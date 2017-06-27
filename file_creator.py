# imports
import matplotlib
matplotlib.use('Agg')
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time

import matplotlib.image as mpimg
import sys
clear = lambda: os.system('cls')

path = "/home/ppedapen/stl"
print(os.getcwd())
os.chdir(path)
print(os.getcwd())

# functions to access the data
# image shape
HEIGHT = 96
WIDTH = 96
DEPTH = 3

# size of a single image in bytes
SIZE = HEIGHT * WIDTH * DEPTH
def read_labels(path_to_labels):
    """
    :param path_to_labels: path to the binary file containing labels from the STL-10 dataset
    :return: an array containing the labels
    """
    with open(path_to_labels, 'rb') as f:
        labels = np.fromfile(f, dtype=np.uint8)
        return labels

def read_all_images(path_to_data):
    with open(path_to_data, 'rb') as f:
        # read whole file in uint8 chunks
        everything = np.fromfile(f, dtype=np.uint8)
        images = np.reshape(everything, (-1, 3, 96, 96))
        images = np.transpose(images, (0, 3, 2, 1))
        return images
def read_single_image(image_file):
    """
    CAREFUL! - this method uses a file as input instead of the path - so the
    position of the reader will be remembered outside of context of this method.
    :param image_file: the open file containing the images
    :return: a single image
    """
    image = np.fromfile(image_file, dtype=np.uint8, count=SIZE)
    image = np.reshape(image, (3, 96, 96))
    image = np.transpose(image, (2, 1, 0))
    return image

def plot_image(image):
    """
    :param image: the image to be plotted in a 3-D matrix format
    :return: None
    """
    plt.axis('off')
    plt.imshow(image)
    plt.show()

#  train data load

train_x= read_all_images('train_X.bin')
train_y =  read_labels('train_y.bin')
test_x = read_all_images('test_X.bin')
test_y = read_labels('test_y.bin')


def save_images_train(i):
    image = train_x[i]
    lable_target = train_y[i]
    save_path = os.getcwd()+'/data/train'
    save_path_target = save_path + '/'+str(lable_target)
    if os.path.exists(save_path_target):
        try:
            plt.axis('off')
            plt.imshow(image)
            plt.savefig(save_path_target+'/'+str(i),bbox_inches='tight') # give file name
        except OSError as error:
            pass
    else:
        try:
            os.makedirs(save_path_target)
            plt.axis('off')
            plt.imshow(image)
            plt.savefig(save_path_target+'/'+str(i),bbox_inches='tight') # give file name
        except OSError as error:
            time.sleep(2)
            plt.axis('off')
            plt.imshow(image)
            plt.savefig(save_path_target+'/'+str(i),bbox_inches='tight') # give file name
    return 0

def save_images_valid(i):
    image = test_x[i]
    lable_target = test_y[i]
    save_path = os.getcwd()+'/data/valid'
    save_path_target = save_path + '/'+str(lable_target)
    if os.path.exists(save_path_target):
        try:
            plt.axis('off')
            plt.imshow(image)
            plt.savefig(save_path_target+'/'+str(i),bbox_inches='tight') # give file name
        except OSError as error:
            pass
    else:
        try:
            os.makedirs(save_path_target)
            plt.axis('off')
            plt.imshow(image)
            plt.savefig(save_path_target+'/'+str(i),bbox_inches='tight') # give file name
        except OSError as error:
            time.sleep(2)
            plt.axis('off')
            plt.imshow(image)
            plt.savefig(save_path_target+'/'+str(i),bbox_inches='tight') # give file name
    return 0



from multiprocessing import Pool
if __name__ == '__main__':
    input_to_pool = list(range(0,len(train_x)))
    print("pools train started")
    process = Pool(10)
    #process.map(save_images_train,input_to_pool)
    print("pool test started")
    input_to_pool = list(range(0,len(test_x)))
    process.map(save_images_valid,input_to_pool)

