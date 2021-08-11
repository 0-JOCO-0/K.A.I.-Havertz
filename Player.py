# -*- coding: utf-8 -*-
"""
Created on Sun Aug  8 23:34:43 2021

@author: jcohen3
"""

class Player:
    def __init__(self, PlayerName, PlayerDict, CurrentGW):
        self.Position = PlayerDict[PlayerName][CurrentGW][1]
        self.Team = PlayerDict[PlayerName][CurrentGW][2]
        self.Targets()
        self.GWs()

    
    def Targets(self, TargetDict):
        for target in TargetDict[self.Position]:
            setattr(self, 'target_'+target, PlayerDict[PlayerName][CurrentGW][1])
            ###Make pd.SERIES not lists!!
    def GWs(self, range):
        for 