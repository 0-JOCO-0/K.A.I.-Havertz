# -*- coding: utf-8 -*-
"""
Created on Sun Aug  8 23:35:55 2021

@author: jcohen3
"""

def Points(Player, string):
    for x in ['bonus','clean_sheets','goals_conceded','minutes',
              'saves','assists','goals_scored','red_cards','yellow_cards',
              'penalties_missed','penalties_saved']:
        exec(f"global {x}; {x} = getattr(Player,x+string,0)")
    Position=Player.Position
    if minutes==0:
        return 0
    elif minutes<60:
        mps=1
    else:
        mps=2
    if Position=='GK':
        return (bonus+mps+(4*clean_sheets)+(saves//3)+(5*penalties_saved)
                -(yellow_cards)-(2*red_cards)-(goals_conceded//2))
    elif Position=='DEF':
        return (bonus+mps+(4*clean_sheets)+(3*assists)+(6*goals_scored)
                -(yellow_cards)-(2*red_cards)-(goals_conceded//2))
    elif Position=='MID':
        return (bonus+mps+(clean_sheets)+(3*assists)+(5*goals_scored)
                -(yellow_cards)-(2*red_cards))
    elif Position=='FWD':
        return (bonus+mps+(3*assists)+(4*goals_scored)
                -(yellow_cards)-(2*red_cards))
    else:
        print('Invalid Player Position')