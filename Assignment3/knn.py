# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 20:54:16 2020

@author: Josh
"""

import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn import neighbors
from sklearn.model_selection import train_test_split
from data_util import *

class KNN:
    
    def fit(self,x_train, y_train, x_test, y_test):    
        # Get some different values of k to try
        ks = [1,3,5,7,9,11,13,15,17,19,21]
        
        # For each value k, build a model and see how well it performed.
        for k in ks:
            print('------------ EVALUATING MODEL: k =' + str(k) + ' -----------------')
            mod = neighbors.KNeighborsClassifier(n_neighbors=k)
            mod.fit(x_train, y_train)
            
            # Make predictions on the current model
            preds = mod.predict(x_test)
            
            # Look at the error metrics and evaluate.
            print_binary_classif_error_report(y_test, preds) #function from data_util
            
    def predict(self):
        print("weee")

        