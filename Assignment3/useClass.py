# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 20:49:09 2020

@author: Josh
"""
import math
from knn import * # Import your knn class
from sklearn.impute import SimpleImputer

def euclidean_dist(x1, x2):
    # .... compute euclidean distance between vectors x1 and x2
    sqrSum = 0
    
    for i in range(len(x1)):
        sqrSum += math.pow(x1[i] - x2[i], 2)
        
    return math.sqrt(sqrSum)
    
# Read data and split, first into X and y and then into training and test.
data = pd.read_csv('./churn_data.csv')
data.head()
    
from sklearn.preprocessing import LabelEncoder #use a label encoder to fix the fact that float != str
for column in data.columns:
    if data[column].dtype == type(object):
        le = LabelEncoder()
        data[column] = le.fit_transform(data[column])

data_x = data[list(data[1:])]
data_y = data['Churn'] #guessing here, but do need data_x and y as per example

x_train, x_test, y_train, y_test = train_test_split(data_x, data_y, test_size = 0.3, random_state = 4)
  
k = KNN()
k.fit(x_train, y_train, x_test, y_test)

"""  
knn = KNN(3, euclidean) # Create a 3-NN algorithm with Euclidean distance
knn.test()
knn.fit(x_train, y_train)
y_hat = knn.predict(x_test)


euclidean_dist(1,2);
"""