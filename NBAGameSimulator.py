# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 13:02:06 2018

@author: Ken
"""

import pandas as pd 
import random as rnd
import numpy as np 
import matplotlib.pyplot as plt


class Team:
    """Team creates an object that can be passed into the simulation. Takes a Team Name (String)
    points (list), and opp_points (List) """
    
    def __init__(self, TeamName,points, opp_points):
        self.TeamName = TeamName
        self.points = points
        self.opp_points = opp_points
    
    #Returns avg of points
    def pointsavg(self):
        return np.mean(self.points)
    
    #Returns standard deviation of points
    def pointsstd(self):
        return np.std(self.points)
    #returns avg of opponent points
    def opp_pointsavg(self):
        return np.mean(self.opp_points)
    #returns standard deviation of opponent points 
    def opp_pointsstd(self):
        return np.std(self.opp_points)

class MatchupSimulator:
    def __init__(self, Team1,Team2):
        self.Team1 = Team1
        self.Team2 = Team2
        self.results = []
        
    def gameSim(self):
        T1 = (rnd.gauss(self.Team1.pointsavg(),self.Team1.pointsstd())+ rnd.gauss(self.Team2.opp_pointsavg(),self.Team2.opp_pointsstd()))/2
        T2 = (rnd.gauss(self.Team2.pointsavg(),self.Team2.pointsstd())+ rnd.gauss(self.Team1.opp_pointsavg(),self.Team1.opp_pointsstd()))/2
        if int(round(T1)) > int(round(T2)):
            return 1
        elif int(round(T1)) < int(round(T2)):
            return -1
        else: return 0
        
    def gamesSim(self,number_simulations):
        gamesout = []
        team1win = 0
        team2win = 0
        tie = 0
        for i in range(number_simulations):
            gm = self.gameSim()
            gamesout.append(gm)
            if gm == 1:
                team1win +=1 
            elif gm == -1:
                team2win +=1
            else: tie +=1 
        print(self.Team1.TeamName + ' Win ', team1win/(team1win+team2win+tie),'%')
        print(self.Team2.TeamName + ' Win ', team2win/(team1win+team2win+tie),'%')
        print('Tie ', tie/(team1win+team2win+tie), '%')
        self.results = gamesout

    
