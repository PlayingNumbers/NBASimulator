# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 13:21:25 2018

@author: Ken
"""

from NBAGameSimulator import *
import numpy as np

gsw = Team('GSW',[90,100,110,120],[85,90,100,110])
cle = Team('CLE',[90,99,108,117],[85,90,100,110])

msim = MatchupSimulator(gsw,cle)

msim.gamesSim(1000)