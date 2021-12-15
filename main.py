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
# train.info()
#
# print('------------------------------------')
# print('Percentage of NA per property sorted')
# print('------------------------------------')
# p = (train.isna().sum()/len(train)*100).sort_values(ascending=False)
# print(p)
# print('----------------------------------------------------')
# print('Unique values for duplications and other useful info')
# print('----------------------------------------------------')
# u = train.nunique().sort_values()
# print(u)

def clean_data(data):
    # Drop not useful data
    data.drop(['Cabin', 'Name', 'Ticket'], axis=1, inplace=True)

    # Fill null of 'Age'
    data['Age'] = data.groupby(['Pclass', 'Sex'])['Age'].transform(lambda x: x.fillna(x.median()))

    # FARE Data missing in test
    data['Fare'] = data.groupby(['Pclass', 'Sex'])['Age'].transform(lambda x: x.fillna(x.median()))

    # Fill null of 'Embarked'
    data.dropna(axis=0, subset=['Embarked'], inplace=True)



