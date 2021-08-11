# -*- coding: utf-8 -*-
"""
Created on Sun Aug  8 23:35:57 2021

@author: jcohen3
"""
    # Pandas is used for data manipulation
import pandas as pd
from Player import Player

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
    def __init__(self, FileName, CurrentGW, TargetDict, Range, Attributes):
        ###find way to import and iterate only once
        self.file = pd.read_csv(FileName)
        self.Positions = ['GK','DEF','MID','FWD']
        self.PlayerDict = {x:{} for x in self.Positions}
        self.PlayerNames = []
        self.CreatePlayerDict(CurrentGW, TargetDict, Range, Attributes)
    
    def CreatePlayerDict(self, CurrentGW, TargetDict, Range, Attributes):
        for Player in self.file.iterrows():
            PlayerPosition = Player[1][1]
            if PlayerPosition not in self.Positions:
                continue
            PlayerName = Player[1][0]
            GW = int(Player[1][-1])
            if PlayerName not in self.PlayerDict[PlayerPosition]:
                self.PlayerDict[PlayerPosition][PlayerName] = {}
                self.PlayerNames.append(PlayerName)
            self.PlayerDict[PlayerPosition][PlayerName][GW] = Player[1]
    
    def CreatePlayers(self, CurrentGW, TargetDict, Range, Attributes):
        for position in self.Positions:
            for PlayerName in list(self.PlayerDict[position].keys()):
                try:
                    setattr(self, PlayerName,Player(PlayerName,
                                                self.PlayerDict[position],
                                                CurrentGW,
                                                Range,
                                                TargetDict,
                                                Attributes))
                except:
                    continue
    
    def CreateDF(self, Positions, Attributes, Range, TargetDict):
        DF = []
        index = []
        for position in Positions:
            columns = ['GW_'+str(x)+'_'+y for y in Attributes for x in Range] +[
            'target_'+target for target in TargetDict[position]] + [
                'Position', 'Team']
            for PlayerName in self.PlayerDict[position]:
                PlayerAttributes = []
                for x in Range:
                    for y in Attributes:
                        try:
                            PlayerAttributes.append(getattr(
                                getattr(self, PlayerName),
                                'GW_'+str(x)+'_'+y))
                        except:
                            continue
                if len(PlayerAttributes) != (len(Range)*len(Attributes)):
                    continue
                for target in TargetDict[position]:
                    PlayerAttributes.append(getattr(
                        getattr(self, PlayerName),
                        'target_'+target))
                PlayerAttributes.append(getattr(self, PlayerName).Position)
                PlayerAttributes.append(getattr(self, PlayerName).Team)
                DF.append(PlayerAttributes)
                index.append(PlayerName)
        df = pd.DataFrame(DF, index=index, columns=columns)
        return df
        
                    
                