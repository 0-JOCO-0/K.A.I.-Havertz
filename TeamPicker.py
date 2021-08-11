# -*- coding: utf-8 -*-
"""
Created on Sun Aug  8 23:37:11 2021

@author: jcohen3
"""

from DataHandler import DataHandler
from ML import ML

class TeamPicker():
    def __init__(self, FileName, TargetDict, Attributes, CurrentGW, Range):
        print('Initialising...')
        self.Data = DataHandler(FileName, CurrentGW-1, TargetDict, Range, Attributes)
        print('Player Dictionary created.')
        self.Data.CreatePlayers(CurrentGW-1, TargetDict, Range, Attributes)
        print('Players created.')
        for position in self.Data.Positions:
            #CREATE ATTRIBUTES and TargetDict
            df = self.Data.CreateDF([position], Attributes, Range, TargetDict)
            print(position + ' Dataframe created.')
            setattr(self, position+'ml', ML(df))
            print(position + ' ML established.')
            for target in TargetDict[position]:
                print(target)
                setattr(self, position+'_rf_'+target, getattr(self, position+'ml').CreateModel(target, TargetDict[position]))
            print(position+' randoom forests established.')
        print('Finished Initialising.')
    
    #It would be sexy to add xP to everyone as an attribute in init...
    #rf.predict(test_features)
    #Currently we have a predictor for CurrentWeek but we want to apply it to CurrentWeek+1
    
    #def Pick():
    
  #  def Points():
    
   # def SingleTransfer():