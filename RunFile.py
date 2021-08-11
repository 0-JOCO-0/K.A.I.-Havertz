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
              'DEF':['bonus','assists','clean_sheets	','goals_conceded','goals_scored','minutes'],
              'MID':['bonus','assists','clean_sheets	','goals_scored','minutes'],
              'FWD':['bonus','assists','goals_scored','minutes']}
Attributes = ['xP','assists','bonus','bps','clean_sheets	',
              'creativity','element'	, 'fixture','goals_conceded'	,
              'goals_scored', 'ict_index',	'influence',
              'koff_time','minutes', 'opponent_team','own_goals',
              'penalties_missed','penalties_saved',
              'red_cards','round	','saves','selected','team_a_score',
              'team_h_score','threat','total_points','transfers_balance',
              'transfers_in','transfers_out','value','was_home',	
              'yellow_cards',	'GW'
]

#%%
test = TeamPicker(FileName, TargetDict, Attributes)

#%%
P = [x for x in [y for y in range(5)]]
print(P)