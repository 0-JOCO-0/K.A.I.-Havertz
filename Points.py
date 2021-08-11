# -*- coding: utf-8 -*-
"""
Created on Sun Aug  8 23:35:55 2021

@author: jcohen3
"""

def Points(position, bonus=0,clean_sheets=0,goals_conceded=0,minutes=0,saves=0,
           assists=0,goals_scored=0,red_cards=0,yellow_cards=0,penalties_missed=0,
           penalties_saved=0):
    if minutes==0:
        return 0
    elif minutes<60:
        mps=1
    else:
        mps=2
    if position=='GK':
        return (bonus+mps+(4*clean_sheets)+(saves//3)+(5*peanties_saved)
                -(yellow_cards)-(2*red_cards)-(goals_conceded//2))
    elif position=='DEF':
        return (bonus+mps+(4*clean_sheets)+(3*assists)+(6*goals_scored)
                -(yellow_cards)-(2*red_cards)-(goals_conceded//2))
    elif position=='MID':
        return (bonus+mps+(clean_sheets)+(3*assists)+(5*goals_scored)
                -(yellow_cards)-(2*red_cards))
    elif position=='FWD':
        return (bonus+mps+(3*assists)+(4*goals_scored)
                -(yellow_cards)-(2*red_cards))