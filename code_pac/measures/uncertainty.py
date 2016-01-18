'''
Created on 30/11/2015

@author: mangeli
'''
from __future__ import division
from code_pac.measures import MeasureTemplate, MeasureType
from code_pac.model import GenericGame

import math, sys


class Uncertainty(MeasureTemplate):
    '''
    evaluates the game Uncertainty by measure the distance between the
    discrete uniform distribution of the probabilities of players win
    the game and the actual probability distribution vis a vis the normalized
    score relation
    '''


    def __init__(self, *args, **kwargs):
        super(Uncertainty, self).__init__(*args, **kwargs)
        self._measureType = MeasureType(code=3, description='Uncertainty', version=3) #for retro compatibility

    def _evaluateMeasure(self):
        nPlayers = len(self._game.getPlayers())
        nTurns = self._game.getNumberRounds() - self._ignored #first gameRound hasn't results
        
        if nPlayers == 0 or nTurns == 0:
            self._measureValue = 0 #preventing possible garbage in dataset
        else:
            players = self._game.getPlayers() #list of players
            nPlayers = len(players)
            #winner = self.getWinner()
                        
            auxMatchUncertainty = 0
            
            for gameRound in self._game.getGameStruct():
                inPlayers = []
                turnScores={}
                totalRoundScore = 0
                auxTurnUncertainty = 0
                '''first gameRound hasn't results'''
                if self._game.getGameStruct().index(gameRound) > self._ignored - 1: #starting from 0
                    #building round players list and top score in the turn
                    for roundItem in gameRound[1]:
                        inPlayers.append(roundItem.playerCode)
                        turnScores[roundItem.playerCode] = max(0, roundItem.totalScore - self._minScore)
                        totalRoundScore += max(0, roundItem.totalScore - self._minScore)
                            
                    for player in players:
                        if player in inPlayers:
                            proPlayer = (turnScores[player]/totalRoundScore) #probability of the player win the match
                        else:
                            proPlayer = 0
                        auxTurnUncertainty += math.pow((math.sqrt(proPlayer) - math.sqrt(1/nPlayers)),2)
                        
                    
                    auxMatchUncertainty += math.sqrt(auxTurnUncertainty / 2)
            
            
                
            self._measureValue = 1 - (auxMatchUncertainty / nTurns)
            
       

if __name__ == '__main__':
    import code_pac.brasileiro.model as brasileiroModel
    import code_pac.model as model
    import code_pac.measures as measures
    
    from code_pac import dataBaseAdapter
    import code_pac.desafio.model as desafioModel
    
    #set the test type (brasileiro = 1, desafio = 2)
    testType = 1
    
    #set desafioGame data
    tournamentCode = 123
    seriesCode = 264
    groupCode = 10880
    
    
    if testType == 1:
        games = brasileiroModel.Game.retrieveList()
        for game in games:
            print game.year
            print measures.Uncertainty(game=model.BrasileiroGame(game), ignored=0).getMeasureValue()
            print '==================='
    elif testType == 2:
        conn = dataBaseAdapter.getConnection()
        tournament = desafioModel.Tournament.retrieve(tournamentCode, conn)
        series = desafioModel.Series.retrieve(tournament, seriesCode, conn)
        game = desafioModel.Game(series, groupCode)
        print tournament.refYear
        print measures.Uncertainty(game=model.DesafioGame(game), ignored=1, minScore=50).getMeasureValue()
        print '================'
    
