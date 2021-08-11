# -*- coding: utf-8 -*-
"""
Created on Sun Aug  8 23:35:58 2021

@author: jcohen3
"""

import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor

class ML:
    def __init__(self, df):
        self.df = df
        self.OneHotEncode()
        
    def CreateModel(self, target):
        self.Split(target)
        self.Learn()
        self.df = self.safe_df
        return self.rf
        
    def OneHotEncode(self):
        self.df = pd.get_dummies(self.df)
        self.safe_df = self.df.copy()
        
    def Split(self, target):
        self.labels = np.array(features[target])
        self.df = self.df.drop(target, axis = 1)
        self.df_list = list(self.df.columns)
        self.df = np.array(self.df)

    def Learn(self):
        self.rf = RandomForestRegressor(n_estimators = 1000, random_state = 42)
        self.rf.fit(self.df, self.labels)
