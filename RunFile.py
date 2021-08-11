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
              'kickoff_time','minutes', 'opponent_team','own_goals',
              'penalties_missed','penalties_saved',
              'red_cards','round','saves','selected','team_a_score',
              'team_h_score','threat','total_points','transfers_balance',
              'transfers_in','transfers_out','value','was_home',	
              'yellow_cards',	'GW'
]

CurrentGW=10
Range=[CurrentGW-1]
#%%
test = TeamPicker(FileName, TargetDict, Attributes, CurrentGW, Range)

#%%
print(getattr(test.Data, 'Aaron Connolly').Value)
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