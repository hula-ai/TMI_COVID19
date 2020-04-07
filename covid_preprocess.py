import h5py

import numpy as np
import os
import pandas as pd
import shutil
import torch
from sklearn.model_selection import train_test_split

base_dir = '/home/cougarnet.uh.edu/szare836/Downloads'
destination_path = base_dir + '/All_Images'
base_covid_img_dir = base_dir + '/CT_COVID'
base_noncovid_img_dir = base_dir + '/CT_NonCOVID'

try:
    os.stat(destination_path)
except:
    os.mkdir(destination_path)

img_name1 = []
img_name2 = []
for filename in os.listdir(base_covid_img_dir):
    #path = destination_path + '/' + filename
    img_name1.append(filename)
    shutil.copy(base_covid_img_dir + '/' + filename, destination_path)

a = len(img_name1)
label1 = torch.ones(a)

for filename in os.listdir(base_noncovid_img_dir):
    #path = destination_path + '/' + filename
    img_name2.append(filename)
    shutil.copy(base_noncovid_img_dir + '/' + filename, destination_path)

a = len(img_name2)
label2 = torch.zeros(a)

PATH = np.append(img_name2, img_name1, axis=0)
labels = np.append(label2, label1)

"""x_train, x_test, y_train, y_test = train_test_split(PATH, labels, test_size=0.2, random_state=2018)

np.savez_compressed('COVID_train', x=x_train, y=y_train)
np.savez_compressed('COVID_train', x=x_test, y=y_test)"""

np.savez_compressed('COVID_Dataset', x=PATH, y=labels)