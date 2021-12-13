# -*- coding: utf-8 -*-
"""
Created on Sun Aug  8 23:37:36 2021

@author: jcohen3
"""

from Points import Points
from DataHandler import DataHandler
from TeamPicker import TeamPicker
from knapsack import knapSack


#%%
FileName = "C:\\Users\\josep\\OneDrive\\Documents\\K.A.I. Havertz\\K.A.I.-Havertz\\merged_gw.csv"

##Add Pen;aties/Cards?
TargetDict = {'GK':['bonus','clean_sheets','goals_conceded','minutes','saves'],
              'DEF':['bonus','assists','clean_sheets','goals_conceded','goals_scored','minutes'],
              'MID':['bonus','assists','clean_sheets','goals_scored','minutes'],
              'FWD':['bonus','assists','goals_scored','minutes']}
Attributes = ['xP','assists','bonus','bps','clean_sheets',
              'creativity','element'	, 'fixture','goals_conceded'	,
              'goals_scored', 'ict_index',	'influence',
              'minutes', 'opponent_team','own_goals',
              'penalties_missed','penalties_saved',
              'red_cards','round','saves','selected','team_a_score',
              'team_h_score','threat','total_points','transfers_balance',
              'transfers_in','transfers_out','value','was_home',	
              'yellow_cards',	'GW'
]

#'kickoff_time'

CurrentGW=17
Range=[CurrentGW-2]
#%%
test = TeamPicker(FileName, TargetDict, Attributes, CurrentGW, Range)

#%%
"""Options = test.BadInit(test.Data.PlayerList)
for y in Options:
        for x in y:
                print(x.PlayerName)
                print(x.xP)

squad = Options[0][:2]+Options[1][:5]+Options[2][:5]+Options[3][:3]
print(len(squad))
Picker = test.Pick(squad)
print("No transfers:")
print('First team:')
for x in Picker[0]:
        print(x.PlayerName)
print('Bench:')
for x in Picker[1]:
        print(x.PlayerName)
captain = test.LineupPoints(Picker[0])
print('Expected Points: ', captain[0])
print('Captain: ', captain[1].PlayerName)
print('Vice-Captain: ', captain[2].PlayerName)

"""
List = test.Data.PlayerList
print(len(List))
#for x in List:
 #       print(x.PlayerName, x.Value, x.xP)



Current_team = ['Aaron Ramsdale', 'Edouard Mendy',
                'Max Kilman', 'Reece James', 'Gabriel Magalhães', 'Matthew Lowton', 'Andrew Robertson',
                'Conor Gallagher', 'Raphael Dias Belloli', 'Demarai Gray', 'Mohamed Salah', 'Declan Rice',
                'Adam Armstrong', 'Emmanuel Dennis', 'Cristiano Ronaldo dos Santos Aveiro']
SQUAD=[]
print("yeeeeeeeee")
teams=[]
"""for x in List:
        if x.Team not in teams:
                teams.append(x.Team)
        if x.Team == 'Burnley':
                print(x.PlayerName)
print(teams)
print(len(teams))"""
print("******************************")
print("No subs:")
for y in Current_team:
            for x in List:
                if x.PlayerName == y:
                    SQUAD.append(x)
Picker = test.Pick(SQUAD)
print('First team:')
for x in Picker[0]:
        print(x.PlayerName)
print('Bench:')
for x in Picker[1]:
        print(x.PlayerName)
captain = test.LineupPoints(Picker[0])
print('Expected Points: ', captain[0])
print('Captain: ', captain[1].PlayerName)
print('Vice-Captain: ', captain[2].PlayerName)
print("******************************")
print("One sub:")
sub =test.dream_subs(Current_team, test.Data.PlayerList)
Picker = test.Pick(sub)
print('First team:')
for x in Picker[0]:
        print(x.PlayerName)
print('Bench:')
for x in Picker[1]:
        print(x.PlayerName)
captain = test.LineupPoints(Picker[0])
print('Expected Points: ', captain[0])
print('Captain: ', captain[1].PlayerName)
print('Vice-Captain: ', captain[2].PlayerName)
print("******************************")
print("Two subs:")
new = [Player.PlayerName for Player in sub]

next = test.dream_subs(new, test.Data.PlayerList)

Picker = test.Pick(next)
print('First team:')
for x in Picker[0]:
        print(x.PlayerName)
print('Bench:')
for x in Picker[1]:
        print(x.PlayerName)
captain = test.LineupPoints(Picker[0])
print('Expected Points: ', captain[0])
print('Captain: ', captain[1].PlayerName)
print('Vice-Captain: ', captain[2].PlayerName)
print("*****************************")
print("Three subs:")
new = [Player.PlayerName for Player in next]
new = test.dream_subs(new, test.Data.PlayerList)

Picker = test.Pick(new)
print('First team:')
for x in Picker[0]:
        print(x.PlayerName)
print('Bench:')
for x in Picker[1]:
        print(x.PlayerName)
captain = test.LineupPoints(Picker[0])
print('Expected Points: ', captain[0])
print('Captain: ', captain[1].PlayerName)
print('Vice-Captain: ', captain[2].PlayerName)
print("*****************************")
print("Four subs:")
new = [Player.PlayerName for Player in new]
new = test.dream_subs(new, test.Data.PlayerList)

Picker = test.Pick(new)
print('First team:')
for x in Picker[0]:
        print(x.PlayerName)
print('Bench:')
for x in Picker[1]:
        print(x.PlayerName)
captain = test.LineupPoints(Picker[0])
print('Expected Points: ', captain[0])
print('Captain: ', captain[1].PlayerName)
print('Vice-Captain: ', captain[2].PlayerName)


# Driver code
val = [x.xP for x in List]
wt = [int(10*x.Value) for x in List]
W = 1000
n = len(val)
# This code is contributed by Suyash Saxena
print(knapSack(W, wt, val, n))
