# -*- coding: utf-8 -*-
"""
Created on Sun Aug  8 23:37:36 2021

@author: jcohen3
"""

from Points import Points
from DataHandler import DataHandler
from TeamPicker import TeamPicker


#%%
FileName = "Fantasy-Premier-League\\data\\2020-21\\gws\\merged_gw.csv"

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

CurrentGW=39
Range=[CurrentGW-2]
#%%
test = TeamPicker(FileName, TargetDict, Attributes, CurrentGW, Range)

#%%
Options = test.BadInit(test.Data.PlayerList)
Gks = [x.PlayerName for x in Options[0]]
Defs = [x.PlayerName for x in Options[1]]
Mids = [x.PlayerName for x in Options[2]]
Fwds = [x.PlayerName for x in Options[3]]

print(Gks)
print(Defs)
print(Mids)
print(Fwds)
Team = [Options[0][2],getattr(test.Data, 'Rúnar Alex Rúnarsson'),
        Options[1][2],Options[1][3], Options[1][4], Options[1][6],getattr(test.Data,'Daniel Amartey'),
        Options[2][1],Options[2][3],Options[2][4],Options[2][5],Options[2][7],
        getattr(test.Data,'Michael Obafemi'),Options[3][1], Options[3][3]
        ]
print([x.PlayerName for x in Team])
print([x.xP for x in Team])
print([x.xP for x in Options[3]])
#%%
#Picked = (test.Pick(test.Data.PlayerList))
Picked = test.Pick(Team)
Lineup = [x.PlayerName for x in Picked[0]]
Bench = [x.PlayerName for x in Picked[1]]

print(Lineup)
print(Bench)
Pts = (test.LineupPoints([x for x in Picked[0]]))
print(Pts[2].PlayerName)
print(Pts[1].PlayerName)
print(Pts[0])

#%%
print(len(test.Data.PlayerList))
#%%
def Curse():
    for x in ['bonus','clean_sheets','goals_conceded','minutes',
              'saves','assists','goals_scored','red_cards','yellow_cards',
              'penalties_missed','penalties_saved']:
        exec(f"global {x}; {x}=x")
    print(bonus)
    #exec(f"{x}")
Curse()
print(bonus)
app = 'bon'
exec("print(app)")
#%%
xPs=[1,4,6,3,2]
print([(xPs.index(max(xPs)))])
print([2*x for x in range(6) if x+1 in [1,3,5]])
#%%
n=pd.read_csv(FileName, index_col = 'name')
print(n['goals_scored'])
for x in n.iterrows():
    for a in ((x[1].index).tolist()):
        print(a)
#%%
columns = ['GW_'+str(x)+'_'+ y for y in Attributes for x in Range] + [
        'Team', 'Position']
print(columns)
#%%
"""['Bernd Leno', 'Jamie Vardy', 'Vladimir Coufal', 'Sadio Mané', 'Fabian Schär', 'Pablo Fornals', 'Rúben Santos Gato Alves Dias', 'Mohamed Salah', 'Nicolas Pépé', 'Juan Mata', 'Timo Werner']
['Rúnar Alex Rúnarsson', 'Mason Holgate', 'Daniel Amartey', 'Michael Obafemi']
Jamie Vardy
Sadio Mané
117.447"""