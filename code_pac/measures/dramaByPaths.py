# -*- coding: utf-8 -*-
'''
Created on 24/05/2015

@author: mangeli
'''
from __future__ import division
from GameQualityAssessment.code_pac.measures import MeasureTemplate, MeasureType
import math

class DramaByPaths(MeasureTemplate):
    '''Evaluate drama in a game by measuring the position distance
     from the game winner to the eventual first place in each round'''
    
    
    
    def __init__(self, *args, **kwargs):
        super(DramaByPaths, self).__init__(*args, **kwargs)
        self._measureType = MeasureType(code=2, description='Drama by paths', version=2) #for retro compatibility
        
    def _evaluateMeasure(self):
        weakCount = 0
        distSum = 0
        pNumber = len(self._game.getPlayers())
        winner = self.getWinner()
        nTurn = self._game.getNumberRounds() - self._ignored #first gameRound hasn't results
        
        for gameRound in self._game.getGameStruct():
            '''first gameRound hasn't results'''
            if self._game.getGameStruct().index(gameRound) > self._ignored - 1: #starting from 0
                '''ordered gameRound results'''
                totalScores = gameRound[1]
                '''distance to MDP'''
                diff = abs(self._playerPosition(winner, gameRound) - self._maxDrama(self._game.getGameStruct().index(gameRound)))
                distSum += diff / ((pNumber - 1) * (nTurn - 1))
                '''winner isn't gameRound best totalScore'''
                if not self._winner == totalScores[0].playerCode:
                    weakCount +=1
                   
        self._measureValue = (weakCount / (nTurn - 1)) *(1- (distSum))
        
        
    def _maxDrama(self, m):
        x1 = 1 #primeira rodada 
        y1 = len(self._game.getPlayers()) #na última posição
        x2 = self._game.getNumberRounds() - self._ignored #última rodada
        y2 = 1 #primeira posição
        return math.ceil(  (y2-y1)*(m-x1)/(x2-x1) + y1 )
    
    def _playerPosition(self, pCode, gameRound):
        index = 1
        pos = 0
        for result in gameRound[1]:
            if result.playerCode == pCode:
                pos = index
            index += 1
        if pos == 0:
            raise Exception('Winner is not in gameRound')
        return pos