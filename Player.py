# -*- coding: utf-8 -*-
"""
Created on Sun Aug  8 23:34:43 2021

@author: jcohen3
"""

class Player:
    def __init__(self, PlayerName, PlayerDict, CurrentGW, Range, TargetDict, Attributes):
        self.PlayerName = PlayerName
        self.Position = PlayerDict[PlayerName][CurrentGW]['position']
        self.Team = PlayerDict[PlayerName][CurrentGW]['team']
        self.Value = PlayerDict[PlayerName][CurrentGW]['value']/10
        #self.Value = PlayerDict[PlayerName][CurrentGW+1]['value']/10
        #Ultimately self.Value might come from different file!
        self.Targets(TargetDict, PlayerName, PlayerDict, CurrentGW)
        self.GWs(Range+[CurrentGW], PlayerName, PlayerDict, Attributes)

    
    def Targets(self, TargetDict, PlayerName, PlayerDict, CurrentGW):
        for target in TargetDict[self.Position]:
            setattr(self, 'target_'+target, PlayerDict[PlayerName][CurrentGW][target])
            
    def GWs(self, Range, PlayerName, PlayerDict, Attributes):
        for x in Range:
            for y in Attributes:
                setattr(self, 'GW_'+str(x)+'_'+y, PlayerDict[PlayerName][x][y])