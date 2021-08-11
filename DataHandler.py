# -*- coding: utf-8 -*-
"""
Created on Sun Aug  8 23:35:57 2021

@author: jcohen3
"""
    # Pandas is used for data manipulation
import pandas as pd

#class DataHandler:

"""# Read in data and display first 5 rows
features = pd.read_csv("Fantasy-Premier-League\\data\\2020-21\\gws\\merged_gw.csv")
print(features.head(5))
c=0
for x in features.iterrows():
    print(x[1][1])
    c=c+1
print(c)"""

class DataHandler:
    def __init__(self, FileName):
        ###find way to import and iterate only once
        self.file = pd.read_csv(FileName)
        self.Positions = ['GK','DEF','MID','FWD']
        self.PlayerDict = {x:{} for x in self.Positions}
        self.PlayerNames = []
        self.CreatePlayerDict()
    
    def CreatePlayerDict(self):
        for Player in self.file.iterrows():
            PlayerPosition = Player[1][1]
            if PlayerPosition not in self.Positions:
                continue
            PlayerName = Player[1][0]
            GW = Player[1][-1]
            if PlayerName not in self.PlayerDict[PlayerPosition]:
                self.PlayerDict[PlayerPosition][PlayerName] = {}
                self.PlayerNames.append(PlayerName)
            self.PlayerDict[PlayerPosition][PlayerName][GW] = Player[1]
    
    def CreatePlayers(self, CurrentGW):
        for PlayerName in self.PlayerNames:
            setattr(self, PlayerName, Player(PlayerName, self.PlayerDict, CurrentGW))
            
    
    def CreateDF(self, Positions, Attributes):
        DF = []
        for position in Positions:
            for PlayerName in self.PlayerDict[position]:
                PlayerAttributes = []
                for attribute in Attributes:
                    try:
                        PlayerAttributes.append(getattr(self, PlayerName).attribute)
                    except:
                        continue
                    
                