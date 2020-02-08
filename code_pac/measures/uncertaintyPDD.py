'''
Created on 30/11/2015
ge
@author: mangeli
'''
from __future__ import division
from GameQualityAssessment.code_pac.measures import MeasureTemplate, MeasureType
from GameQualityAssessment.code_pac.model import GenericGame
from GameQualityAssessment.code_pac.measures import probWinning

import math, sys


class UncertaintyPDD(MeasureTemplate):
    '''
    evaluates the game Uncertainty by measure the distance between the
    discrete uniform distribution of the probabilities of players win
    the game and the actual probability distribution vis a vis the normalized
    score relation
    '''


    def __init__(self, *args, **kwargs):
        if kwargs.get('scoreLimit') == None:
            self._probPlayer = probWinning.probA
        else:
            self._probPlayer = probWinning.probB
            self._scoreLimit = kwargs.get('scoreLimit')
            
        super(UncertaintyPDD, self).__init__(*args, **kwargs)
        self._measureType = MeasureType(code=5, description='Uncertainty by PDD', version=3) #for retro compatibility
        #some games have a limit in the score increasing per turn
        

    def _evaluateMeasure(self):
        nPlayers = len(self._game.getPlayers())
        self._nTurns = self._game.getNumberRounds() - self._ignored #first gameRound hasn't results
        
        if nPlayers == 0 or self._nTurns == 0:
            self._measureValue = 0 #preventing possible garbage in dataset
        else:
            players = self._game.getPlayers() #list of players
            nPlayers = len(players)
            
                        
            matchUncertainty = 0
            
            
            for gameRound in self._game.getGameStruct():
                inPlayers = []
                turnScores={}
                turnUncertainty = 0
                self._turnNumber = self._game.getGameStruct().index(gameRound) + 1
                
                '''first gameRound hasn't results, last gameRound is discarded'''
                if self._turnNumber > self._ignored \
                    and self._turnNumber < self._game.getNumberRounds(): #starting from 0, stoping before the last
                    '''for debug'''
                    #testProb = 0
                    #print '---------------', self._turnNumber
                    #building round players list and top score in the turn
                    for roundItem in gameRound[1]:
                        inPlayers.append(roundItem.playerCode)
                        turnScores[roundItem.playerCode] = max(0, roundItem.totalScore - self._minScore)
                        turnUncertaintyPart = 0
                            
                    for player in players:
                        if player in inPlayers:
                            proPlayer = self._probPlayer(player, turnScores, self) #(turnScores[player]/totalRoundScore) #probability of the player win the match
                        else:
                            proPlayer = 0
                        turnUncertaintyPart += math.pow((math.sqrt(proPlayer) - 1/math.sqrt(nPlayers)),2) / (2 - (2/math.sqrt(nPlayers))) 
                        '''for debug'''
                        #testProb += proPlayer
                        #print player, turnScores.get(player), proPlayer
                    
                    turnUncertainty = 1 - math.sqrt(turnUncertaintyPart)
                    matchUncertainty += turnUncertainty
                    #print turnUncertainty, testProb
                            
            self._measureValue = matchUncertainty / (self._nTurns - 1)
