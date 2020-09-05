# -*- coding: utf-8 -*-
"""AmCentr_NN_app_01.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/159OJxS-b4xzfqYiB9pXwGJbvZ9byFpNm
"""

import os
from werkzeug.utils import secure_filename
import numpy as np # linear algebra
import pandas as pd
import torch
import torchvision
from torchvision import transforms
from tqdm import tqdm
import shutil 
import matplotlib.pyplot as plt
import time
import copy
from PIL import Image

#connect to google drive where dataset is model h5
from google.colab import drive
drive.mount ('/content/gdrive', force_remount = True)

!ls /content/gdrive/'My Drive'/dataset0011/

class ImageFolderWithPaths(torchvision.datasets.ImageFolder):
    def __getitem__(self, index):
        original_tuple = super(ImageFolderWithPaths, self).__getitem__(index)
        path = self.imgs[index][0]
        tuple_with_path = (original_tuple + (path,))
        return tuple_with_path

ALLOWED_EXTENSIONS=set(['jpg', 'jpeg'])

def allowed_file(filename):
    return '.' in filename and filename.lower().rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

model = torch.load("../content/gdrive/My Drive/dataset0011/model_0011_01.h5")

UPLOAD_FOLDER = '../content/gdrive/My Drive/dataset0011/'
data_root = '../content/gdrive/My Drive/dataset0011/'
test_dir = '../content/gdrive/My Drive/dataset0011/'

def get_prediction():
     
    val_transforms = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ])  
    test_dataset = ImageFolderWithPaths(test_dir, val_transforms)
    #test_dataset = torchvision.datasets.ImageFolder(test_dir, val_transforms)

    test_dataloader = torch.utils.data.DataLoader(
        test_dataset, batch_size=2, shuffle=False, num_workers=0)
    model.eval()

    test_predictions = []
    test_img_paths = []
    for inputs, labels, paths in tqdm(test_dataloader):
        #inputs = inputs.to(device)
        #labels = labels.to(device)
        with torch.set_grad_enabled(False):
            preds = model(inputs)
        test_predictions.append(
            torch.nn.functional.softmax(preds, dim=1)[:,1].data.cpu().numpy())
        test_img_paths.extend(paths)
    
    test_predictions = np.concatenate(test_predictions)

    inputs, labels, paths = next(iter(test_dataloader))
    submission_df = pd.DataFrame.from_dict({'id': test_img_paths, 'label': test_predictions})
    submission_df['label'] = submission_df['label'].map(lambda pred: 'People' if pred > 0.5 else 'NoPeople')
    submission_df['id'] = submission_df['id'].str.replace('../content/gdrive/My Drive/dataset0011/', '')
    submission_df['id'] = submission_df['id'].str.replace('.jpg', '')    
    return submission_df

res = get_prediction()
print(res)

!pip freeze  > requirements.txt

!ls

from google.colab import files

files.download('requirements.txt')
