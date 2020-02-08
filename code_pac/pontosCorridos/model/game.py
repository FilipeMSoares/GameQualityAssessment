'''
Created on 05/07/2015

@author: mangeli
'''
from collections import namedtuple
import os
import configparser
import json
from GameQualityAssessment.code_pac.configReader import ConfigReader

class Game:
    def __init__(self, country, year, gameRounds=None):
        self.country = country
        self.year = year
        if gameRounds == None:
            self.gameRounds = Game.__getGameRoundsByCountryAndYear(country,year)
        else:
            self.gameRounds = gameRounds
            
    
    @classmethod
    def getChampionshipName(cls,country):
        if country == 'brasileiro':
            return "Brasileirão Serie A"
        elif country == 'espanhol':
            return "Primera División da Liga de Fútbol Profesional"
        elif country == 'ingles':
            return "Premier League"
        elif country == 'italiano':
            return "Lega Nazionale Professionisti - Serie A"
        elif country == 'alemao':
            return "Futball Bundesliga"
        elif country == 'portugal':
            return "Primeira Liga"
        else:
            raise Exception("Country "+country+" is not archived")
    
    @classmethod
    def __getGameFilesByCountry(cls,country):
        configreader = ConfigReader()

        if country == 'brasileiro':
            list_of_games = configreader.listBrasileiroGames()
        elif country == 'espanhol':
            list_of_games = configreader.listLaLigaGames()
        elif country == 'ingles':
            list_of_games = configreader.listPremierLeagueGames()
        elif country == 'italiano':
            list_of_games = configreader.listLegaNazionaleGames()
        elif country == 'alemao':
            list_of_games = configreader.listBunsligaGames()
        elif country == 'portugal':
            list_of_games = configreader.listPrimeiraLigaGames()
        else:
            raise Exception("Country "+country+" is not archived")
        return list_of_games

    @classmethod
    def __getGameRoundsByCountryAndYear(cls,country, year):
        list_of_games = Game.__getGameFilesByCountry(country)

        foundGameFile = None
        for gameFile in list_of_games:
            if year in gameFile:
                foundGameFile = gameFile
        if foundGameFile == None:
            raise Exception("Year "+year+" is not archived")
        f = open(gameFile, 'r')
        j = json.load(f) #a list of rounds
        preGame =[]
        year = gameFile[-4:]
        for r in j:
            gameRound = []
            for p in r:
                gameRound.append(p)
            preGame.append(gameRound)
        return preGame

    @classmethod
    def retrieveList(cls,country):
        gameFiles = None
        try:
            gameFiles = Game.__getGameFilesByCountry(country)
        except:
            gameFiles = ConfigReader().listPontosCorridosGames()
        games = []
        for gameFile in gameFiles:
            f = open(gameFile, 'r')
            j = json.load(f) #a list of rounds
            pathArray = gameFile.split(os.sep)
            preGame =[]
            year = pathArray[-1][-4:]
            if (pathArray[-2] == "raw_data"):
                country = pathArray[-3]
            else:
                country = pathArray[-2]
            for r in j:
                gameRound = []
                for p in r:
                    gameRound.append(p)
                preGame.append(gameRound)
            games.append(cls(country, year, preGame))
        return sorted(games, key=lambda g: (g.country,g.year))


if __name__ == '__main__':
    lista = Game.retrieveList('brasileiro')
    print (lista)