# -*- coding: utf-8 -*-
"""
Created on Sun Aug  8 23:37:11 2021

@author: jcohen3
"""

from DataHandler import DataHandler

class TeamPicker():
    def __init__(self, FileName, TargetDict, Attributes):
        print('Initialising...')
        Data = DataHandler(FileName, CurrentGW)
        print('Player Dictionary created.')
        Data.CreatePlayers()
        print('Players created.')
        for position in Data.Positions:
            #CREATE ATTRIBUTES and TargetDict
            df = Data.CreateDF(position, Attributes)
            print(position + 'Dataframe created.')
            setattr(self, position+'ml', ML(df))
            print(position + 'ML established.')
            for target in TargetDict[position]:
                setattr(self, position+'_rf_'+target, getattr(self, position+'ml').CreateModel(target))
            print(position+' randoom forests established.')
        print('Finished Initialising.')