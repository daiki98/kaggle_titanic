# imports
import numpy as np
import pandas as pd
import os
import seaborn as sns
from sklearn.metrics import accuracy_score
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score

from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import SGDClassifier
from sklearn.svm import SVC

# load dataset
train_path = 'dataset/train.csv'
test_path = 'dataset/test.csv'

train = pd.read_csv(train_path)
test = pd.read_csv(test_path)

# Some info about the data
train.info()

print('------------------------------------')
print('Percentage of NA per property sorted')
print('------------------------------------')
p = (train.isna().sum()/len(train)*100).sort_values(ascending=False)
print(p)
print('----------------------------------------------------')
print('Unique values for duplications and other useful info')
print('----------------------------------------------------')
u = train.nunique().sort_values()
print(u)


