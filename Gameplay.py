# Gameplay.py

"""Controller module for Showdown card game.

This module contains the subcontroller to play a single game of Showdown.
Instances reflect a single game.  To play a new game, make a new instance of Gameplay.

This subcontroller manages the following and all associated die rolls:
inning number and top/bottom, the score, the current pitcher and batter, at-bats, pitches, swings,
which cards are on which bases & are thus allowed to take which actions, and the aforementioned actions.

"""

import random
import ShowdownTeam
import PlayerCard

class Gameplay(object):
    # GETTERS AND SETTERS
    
    def getInningNumber(self):
        return self._InningNumber
    
    def setInningNumber(self,value):
        assert isinstance(value,int)
        assert value > 0
        self._InningNumber = value
    
    #output is of type InningType
    def getInningTopBottom(self):
        return self._InningTopBottom
    
    def setInningTopBottom(self,TorB):
        TorB = TorB.upper()
        assert TorB == "TOP" or TorB == "BOTTOM"
        self._InningNumber = TorB
    
    def getOuts(self):
        return self._Outs
    
    def getHomeScore(self):
        return self._HomeScore
    
    def getAwayScore(self):
        return self._AwayScore

    def setHomeScore(self,score):
        self._HomeScore = score
        
    def setAwayScore(self,score):
        self._AwayScore = score
    
    #do the next four getter functions go here or in a team
    def getHomePitcher(self):
        return self._HomePitcher
    
    def getHomeBatter(self):
        return self._HomeBatter
    
    def getAwayPitcher(self):
        return self._AwayPitcher
    
    def getAwayBatter(self):
        return self._AwayBatter
   
    def getActiveBatter(self):
        if self.getInningTopBottom().upper() is "TOP":
            return self.getAwayBatter()
        else:
            return self.getHomeBatter()
        
    def getActivePitcher(self):
        if self.getInningTopBottom().upper() is "TOP":
            return self.getHomePitcher()
        else:
            return self.getAwayPitcher()
    
    #output is of type ShowdownTeam
    def getHomeTeam(self):
        return self._HomeTeam
    
    #output is of type ShowdownTeam
    def getAwayTeam(self):
        return self._AwayTeam
    
    '''
    #outputs for the three below getters are of type PlayerCard
    def getFirstBase(self):
        return self._FirstBase
    
    def getSecondBase(self):
        return self._SecondBase
    
    def getThirdBase(self):
        return self._ThirdBase
    
    #inputs for the three below getters are of type PlayerCard
    def setFirstBase(self,player):
        assert player is PlayerCard
        self._FirstBase = player 
    
    def setSecondBase(self):
        assert player is PlayerCard
        self._SecondBase = player
        
    def setThirdBase(self):
        assert player is PlayerCard
        self._ThirdBase = player
        
    def dieRoll(self):
        return random.randint(1,21)
    '''
    PitcherOutcomes = ["Out(PU)","Out(SO)","Out(GB)","Out(FB)","BB","single","double","homerun"]
    BatterOutcomes = ["Out(SO)","Out(GB)","Out(FB)","BB","single","single_plus","double","triple","homerun"]
    
    def atBat(self):
        thePitcher = self.getActivePitcher()
        theBatter = self.getActiveBatter()
        thePitch = self.dieRoll()
        OutcomesList = none
        Result = none
        if thePitcher.getControl() + thePitch > theBatter.getOnBase():
            print "Pitcher's advantage!"
            OutcomesList = thePitcher.getPitcherOutcomes()
            Result = PitcherOutcomes

        else:
            print "Batter's advantage!"
            OutcomesList = theBatter.getBatterOutcomes()
            Result = BatterOutcomes
            
        outcomeSum = 0
        theSwing = self.dieRoll()
        loopCounter = 0
        # sum up the OutcomesList until you exceed the die roll
        while outcomeSum < theSwing:
            outcomeSum += OutcomesList[loopCounter] # add the next outcome
            if outcomeSum <= theSwing: # correct result identified
                return Result[loopCounter] # return the appropriate result TODO: test me
            loopCounter += 1
            
    # __INITIALIZER__
    def __init__(self):#,HomeTeam,AwayTeam): #saved for later
        #self._HomeTeam = HomeTeam # not necessary as of now, will be in the future to ensure only full, legal teams are used
        #self._AwayTeam = AwayTeam # not necessary as of now, will be in the future to ensure only full, legal teams are usedactiveGame = TRUE
        homeLineup = Lineup('home')
        awayLineup = Lineup('away')
        self.setInningNumber(1)
        self.setInningTopBottom('Top')
        self.setHomeScore(0)
        self.setAwayScore(0)
        self._ActivePitcher = self.getActivePitcher()
        self._ActiveBatter = self.getActiveBatter()
        
        activeGame = TRUE            

        #while activeGame:
            #check inning
            #call atBat(), which yields a result
            #do the outcomes
            #on to the next batter
            #on to the next half-inning or full inning
            #continue
            #end game turn activeGame = FALSE when...
    
    
newGame = Gameplay(home,away) # start!
        