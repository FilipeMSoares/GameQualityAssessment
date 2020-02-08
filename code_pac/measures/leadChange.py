'''
Created on 04/01/2016

@author: mangeli
'''
from __future__ import division
from GameQualityAssessment.code_pac.measures import MeasureTemplate, MeasureType
import math
from math import sqrt

class LeadChange(MeasureTemplate):
    '''Evaluate the leadChange aesthetic criterion in a match'''
    
    def __init__(self, *args, **kwargs):
        super(LeadChange, self).__init__(*args, **kwargs)
        self._measureType = MeasureType(code=3, description='Lead Change', version=4) #for retro compatibility
        
    def _evaluateMeasure(self):
        gameRoundCount = self._game.getNumberRounds() - self._ignored #in case first gameRound hasn't results
        playersCount = len(self._game.getPlayers())
        matchLeaders = []
        changesCount = 0
        currentLeader = None
        roundCounter = 0
        
        if gameRoundCount == 0 or playersCount == 0:
            mValue = 0
        else:
            for gameRound in self._game.getGameStruct():
                '''first gameRound hasn't results'''
                if self._game.getGameStruct().index(gameRound) > self._ignored - 1: #starting from 0
                    roundScores = gameRound[1] # List of (playerCode, roundScore, totalScore)
                    roundLeader = roundScores[0].playerCode # ordered gameRound results
                    #new leader
                    if not currentLeader == roundLeader:
                        currentLeader = roundLeader
                        if not roundLeader in matchLeaders:
                            matchLeaders.append(roundLeader)
                        if roundCounter > 0:
                            changesCount += 1
                    roundCounter += 1
            try:
                fac1 = changesCount / (gameRoundCount - 1)                
            except:
                fac1 = 0
            
            try:
                fac2 = (len(matchLeaders) - 1) / (playersCount - 1)
            except:
                fac2 = 0
            #print 'changes= ', changesCount
            #print 'rounds= ', gameRoundCount
            #print 'leaders= ', len(matchLeaders)
            #print 'players= ', playersCount
            #print fac1, '  ', fac2
            mValue = (sqrt(fac1) + sqrt(fac2))/2
        self._measureValue = mValue
        