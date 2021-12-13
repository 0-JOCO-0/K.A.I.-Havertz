# -*- coding: utf-8 -*-
"""
Created on Sun Aug  8 23:37:11 2021

@author: jcohen3
"""

from DataHandler import DataHandler
from ML import ML
from Points import Points

class TeamPicker(ML):
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
                #print(target)
                setattr(self, position+'_rf_'+target, getattr(self, position+'ml').CreateModel(target, TargetDict[position]))
            print(position+' randoom forests established.')
            self.df = self.Data.CreateDF([position], Attributes, [CurrentGW-1], None)
            self.OneHotEncode()
            for target in TargetDict[position]:
                prediction_df = self.df.copy()
                names = list(prediction_df.index)
                prediction_list = getattr(self, position+'_rf_'+target).predict(prediction_df)
                for i in (range(len(names))):
                    setattr(getattr(self.Data,names[i]),target+'_prediction', prediction_list[i])
            for PlayerName in names:
                Player = getattr(self.Data, PlayerName)
                xPoints = Points(Player, '_prediction')
                Player.xP = xPoints
                
        print('Finished Initialising.')
    
    #It would be sexy to add xP to everyone as an attribute in init...
    #rf.predict(test_features)
    #Currently we have a predictor for CurrentWeek but we want to apply it to CurrentWeek+1
    
    def Pick(self, squad):
        GkXp = [Player.xP for Player in squad if Player.Position=='GK']
        DefXp = [Player.xP for Player in squad if Player.Position=='DEF']
        MidXp = [Player.xP for Player in squad if Player.Position=='MID']
        FwdXp = [Player.xP for Player in squad if Player.Position=='FWD']
        Gk = [Player for Player in squad if Player.Position=='GK']
        Def = [Player for Player in squad if Player.Position=='DEF']
        Mid = [Player for Player in squad if Player.Position=='MID']
        Fwd = [Player for Player in squad if Player.Position=='FWD']
        
        """for x in [GkXp,DefXp,MidXp,FwdXp,Gk,Def,Mid,Fwd]:
            print(len(x))"""
        
        lineup=[]
        lineup.append(self.topPlayer(Gk,GkXp))
        lineup.append(self.topPlayer(Fwd,FwdXp))
        for x in range(3):
           lineup.append(self.topPlayer(Def,DefXp))
           lineup.append(self.topPlayer(Mid,MidXp))
        Outfield = Def+Mid+Fwd
        OutfieldXp = DefXp+MidXp+FwdXp
        for x in range(3):
            lineup.append(self.topPlayer(Outfield,OutfieldXp))
        
        subs=[]
        subs.append(self.topPlayer(Gk,GkXp))
        for x in range(3):
            subs.append(self.topPlayer(Outfield,OutfieldXp))
        return [lineup,subs]

        
    def topPlayer(self, Players, XPs):
        index = XPs.index(max(XPs))
        Player = Players[index]
        XPs.remove(XPs[index])
        Players.remove(Players[index])
        return(Player)
        
    def LineupPoints(self, Lineup):
        Captain = None
        CaptainXp = 0

        Score = 0
        ViceCaptain = None
        for Player in Lineup:
            if Player.xP > CaptainXp:
                ViceCaptain = Captain
                Captain = Player
                CaptainXp = Player.xP
            Score = Score+Player.xP
        Score = Score + CaptainXp
        if not ViceCaptain:
            CaptainXp=0
            for Player in Lineup[1:]:
                if Player.xP > CaptainXp:
                    ViceCaptain = Player
                    CaptainXp = Player.xP
        return [Score, Captain, ViceCaptain]
    
    def BadInit(self, squad, length=10):
        GkXp = [Player.xP for Player in squad if Player.Position=='GK']
        DefXp = [Player.xP for Player in squad if Player.Position=='DEF']
        MidXp = [Player.xP for Player in squad if Player.Position=='MID']
        FwdXp = [Player.xP for Player in squad if Player.Position=='FWD']
        Gk = [Player for Player in squad if Player.Position=='GK']
        Def = [Player for Player in squad if Player.Position=='DEF']
        Mid = [Player for Player in squad if Player.Position=='MID']
        Fwd = [Player for Player in squad if Player.Position=='FWD']
        
        Gks=[]
        Defs=[]
        Mids=[]
        Fwds=[]
        for x in range(length):
            Gks.append(self.topPlayer(Gk,GkXp))
            Defs.append(self.topPlayer(Def,DefXp))
            Mids.append(self.topPlayer(Mid,MidXp))
            Fwds.append(self.topPlayer(Fwd,FwdXp))
        return[Gks,Defs,Mids,Fwds]

    def dream_subs(self, current_team, options):
        squad =[]
        potentials = options.copy()
        for y in current_team:
            for x in potentials:
                if x.PlayerName == y:
                    squad.append(x)
                    potentials.remove(x)
        Tops=self.BadInit(potentials, length=1)
        print(len(squad))
        current = self.LineupPoints(squad)[0]
        best = self.LineupPoints(squad)[0]
        trial = squad.copy()
        positions = ['GK','DEF','MID','FWD']
        for x in range(4):
            candidates = [Player for Player in squad if Player.Position==positions[x]]
            for y in candidates:
                trial.remove(y)
                trial.append(Tops[x][0])
                Score = self.LineupPoints(trial)[0]
                if Score>best:
                    new_squad=trial.copy()
                    best=Score
                    playerIn = Tops[x][0]
                    playerOut = y
                trial = squad.copy()
        print("Bring in ",playerIn.PlayerName)
        print("Take out ",playerOut.PlayerName)
        print("Improvement = ", best-current)
        return new_squad
                




        
    

    """def Knapsack(self, money):
        squad = self.Data.PlayerList
        Gk = [Player for Player in squad if Player.Position=='GK']
        Def = [Player for Player in squad if Player.Position=='DEF']
        Mid = [Player for Player in squad if Player.Position=='MID']
        Fwd = [Player for Player in squad if Player.Position=='FWD']
        #bruteforce
        for x in range(len(Gk))
        trial = []
        for i in len(Gk):
            for j in Gk[:i]:
                trial.append(Gk[i],Gk[j])
"""
   # def DreamTeam(self):
    #    self.AllNames = list(Data.PlayerDict.
    
    #def isSquadValid:
    
  #  def Points():
    
   # def SingleTransfer():