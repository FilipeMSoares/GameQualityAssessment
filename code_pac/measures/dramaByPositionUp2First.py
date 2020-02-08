# -*- coding: utf-8 -*-
'''
Created on 24/05/2015

@author: mangeli
'''
from __future__ import division
from GameQualityAssessment.code_pac.measures import MeasureTemplate, MeasureType
import math

class DramaByPositionUp2First(MeasureTemplate):
    '''Evaluate drama in a game by measuring the position distance
     from the game winner to the eventual first place in each round'''
    
    
    
    def __init__(self, *args, **kwargs):
        super(DramaByPositionUp2First, self).__init__(*args, **kwargs)
        self._measureType = MeasureType(code=1, description='Drama by position', version=2) #for retro compatibility
        
    def _evaluateMeasure(self):
        dist = 0
        count = 0
        for gameRound in self._game.getGameStruct():
            '''first gameRound hasn't results'''
            if not self._game.getGameStruct().index(gameRound) <= self._ignored -1:
                '''ordered gameRound results'''
                totalScores = gameRound[1]
                
                '''winner isn't gameRound best totalScore'''
                if not self._winner == totalScores[0].playerCode:
                    count +=1
                    for t in totalScores:
                        if t.playerCode == self._winner:
                            dist += math.sqrt(totalScores.index(t) / len(totalScores))
                            break
        self._measureValue = dist / count if count > 0 else 0 
