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

    # Categorical data
    le = preprocessing.LabelEncoder()

    # Sex
    data['Sex'].replace({'male': 0, 'female': 1}, inplace=True)

    # Embarked
    data['Embarked'].replace({'male': 0, 'female': 1}, inplace=True)

    return data


def fit_and_predict(input_model):
    """The following code makes faster to evaluate a model
     automating the fit and accuracy process"""
    input_model.fit(X_train, y_train)
    prediction = input_model.predict(X_val)
    return accuracy_score(y_val, prediction)


clean_train = clean_data(train)
clean_test = clean_data(test)

# clean_train.info()
# clean_test.info()

# Set X and y
X = pd.get_dummies(train.drop('Survived', axis=1))
y = train['Survived']


# Split model train test data
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

is_performance = True

if is_performance:
    model = GradientBoostingClassifier()
    print(f'Model: {model}')
    print(f'ACC: {fit_and_predict(model)}')

    # Create CSV file
    predict = model.predict(pd.get_dummies(clean_test))
    output = pd.DataFrame({'PassengerId': clean_test['PassengerId'], 'Survived': predict})
    output.to_csv('my_submission.csv', index=False)
    print("Done")


else:
    # Try some models
    model1 = LogisticRegression(solver='liblinear', random_state=42)
    model2 = GradientBoostingClassifier()
    model3 = RandomForestClassifier()
    model4 = SGDClassifier()
    model5 = SVC()

    models = [model1, model2, model3, model4, model5]
    i = 1
    for model in models:
        print(f'Model{i}: {model}')
        print(f'ACC: {fit_and_predict(model)}')




