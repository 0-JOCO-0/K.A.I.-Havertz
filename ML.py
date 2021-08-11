# -*- coding: utf-8 -*-
"""
Created on Sun Aug  8 23:35:58 2021

@author: jcohen3
"""

import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import OneHotEncoder

class ML:
    def __init__(self, df):
        self.df = df
        self.OneHotEncode()
        
    def CreateModel(self, target, targets):
        self.Split(target, targets)
        self.Learn()
        self.df = self.safe_df
        self.Importances()
        return self.rf
        
    def OneHotEncode(self):
        #print(self.df.shape)
        self.df = pd.get_dummies(self.df)
        #print(self.df.shape)
        #OneHotEncoder().fit(self.df)
        #print(self.df.shape)
        self.safe_df = self.df.copy()
        
    def Split(self, target, targets):
        self.labels = np.array(self.df['target_'+target])
        for x in targets:
            self.df = self.df.drop('target_'+x, axis = 1)
        self.df_list = list(self.df.columns)
        self.df = np.array(self.df)

    def Learn(self):
        self.rf = RandomForestRegressor(n_estimators = 1000, random_state = 42)
        self.rf.fit(self.df, self.labels)

    def Importances(self):
        # Get numerical feature importances
        importances = list(self.rf.feature_importances_)
        # List of tuples with variable and importance
        feature_importances = [(feature, round(importance, 2)) for feature, importance in zip(self.df_list, importances)]
        # Sort the feature importances by most important first
        feature_importances = sorted(feature_importances, key = lambda x: x[1], reverse = True)
        feature_importances = feature_importances[:5]
        # Print out the feature and importances 
        [print('Variable: {:5} Importance: {}'.format(*pair)) for pair in feature_importances];