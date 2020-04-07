import h5py

import numpy as np
import os
import pandas as pd
import shutil
import torch
from sklearn.model_selection import train_test_split
import csv

base_dir = '/home/cougarnet.uh.edu/szare836/Downloads/COVID-19'
dest_path = base_dir + '/CT_DATA'
base_covid_img_dir = base_dir + '/CT_COVID'
base_noncovid_img_dir = base_dir + '/CT_NonCOVID'

try:
    os.stat(dest_path)
except:
    os.mkdir(dest_path)

def data_seperation(file_name, source_path, destination_path, mode, class_name):
    with open(file_name, newline='') as f:
        reader = csv.reader(f)
        data = list(reader)

    destination_path = destination_path + '/' + mode
    try:
        os.stat(destination_path)
    except:
        os.mkdir(destination_path)

    for i in range(len(data)):
        for file in os.listdir(source_path):
            if file == data[i][0]:
                try:
                    os.stat(destination_path + '/' + class_name)
                except:
                    os.mkdir(destination_path+ '/' + class_name)
                shutil.copy(source_path + '/' + data[i][0], destination_path + '/' + class_name)

data_seperation(file_name='NonCOVID_test.csv', source_path='/home/cougarnet.uh.edu/szare836/Downloads/COVID-19/CT_NonCOVID', destination_path= dest_path, mode='Test', class_name='NonCOVID')
data_seperation(file_name='NonCOVID_train.csv', source_path='/home/cougarnet.uh.edu/szare836/Downloads/COVID-19/CT_NonCOVID', destination_path= dest_path, mode='Train', class_name='NonCOVID')
data_seperation(file_name='NonCOVID_val.csv', source_path='/home/cougarnet.uh.edu/szare836/Downloads/COVID-19/CT_NonCOVID', destination_path= dest_path, mode='Val', class_name='NonCOVID')
data_seperation(file_name='COVID_test.csv', source_path='/home/cougarnet.uh.edu/szare836/Downloads/COVID-19/CT_COVID', destination_path= dest_path, mode='Test', class_name='COVID')
data_seperation(file_name='COVID_train.csv', source_path='/home/cougarnet.uh.edu/szare836/Downloads/COVID-19/CT_COVID', destination_path= dest_path, mode='Train', class_name='COVID')
data_seperation(file_name='COVID_val.csv', source_path='/home/cougarnet.uh.edu/szare836/Downloads/COVID-19/CT_COVID', destination_path= dest_path, mode='Val', class_name='COVID')




"""np.savez_compressed('COVID_train', x=x_train, y=y_train)
np.savez_compressed('COVID_train', x=x_test, y=y_test)"""