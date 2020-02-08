# -*- coding: utf-8 -*-
'''
Created on 24/05/2015

@author: mangeli
'''
from __future__ import division
from GameQualityAssessment.code_pac.measures import MeasureTemplate, MeasureType
import math


class DramaByPointsUp2First(MeasureTemplate):
    '''Evaluate drama in a game by measuring the points distance
     from the game winner to the eventual first place in each round'''
    
    
    
    def __init__(self, *args, **kwargs):
        super(DramaByPointsUp2First, self).__init__(*args, **kwargs)
        self._measureType = MeasureType(0, "Drama by points", 3) #for retro compatibility
        
    def _evaluateMeasure(self):
        dist = 0
        count = 0
        for gameRound in self._game.getGameStruct():
            '''first gameRound hasn't results'''
            if not self._game.getGameStruct().index(gameRound) <= self._ignored - 1:
                '''ordered gameRound results'''
                totalScores = gameRound[1]
                
                if self._normScores:
                    bestScore = self._game.getGameStruct()[self._game.getNumberRounds() - 1][1][0].totalScore
                else:
                    bestScore = totalScores[0][2]
                
                '''winner isn't gameRound best totalScore'''
                if not self._winner == totalScores[0][0]:
                    count += 1 
                    for t in totalScores:
                        if t[0] == self._winner:
                            dist += math.sqrt((totalScores[0][2] - t[2]) / bestScore)
                            break
        self._measureValue = dist / count if count > 0 else 0
