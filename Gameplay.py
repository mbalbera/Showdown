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
import pyperclip
import PlayerCardCreator

class Gameplay:
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
        self._InningTopBottom = TorB
        print("It's the "+self.getInningTopBottom().lower()+" of inning number "+str(self.getInningNumber()))
        
    def getInningNumber(self):
        return self._InningNumber
    
    def setInningNumber(self,number):
        assert isinstance(number,int)
        self._InningNumber = number
    
    def getOuts(self):
        return self._numberOuts
    
    def setOuts(self,value):
        assert value <= 2
        self._numberOuts = value
    
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
    
    def getAwayPitcher(self):
        return self._AwayPitcher
    
    def getTeamPitcher(self,team):
        assert isinstance(team,ShowdownTeam.Lineup)
        return team.getPitcher()
    
    '''def getHomeBatter(self):
        return self._HomeBatter
    
    def getAwayBatter(self):
        return self._AwayBatter'''
   
    def getActiveBatter(self):
        if self.getInningTopBottom().upper() == "TOP":
            return self.awayLineup.getBatter(self.awayBatterNumber) 
        else:
            return self.homeLineup.getBatter(self.homeBatterNumber)
        
    def getActivePitcher(self):
        if self.getInningTopBottom().upper() == "TOP":
            return self.homeLineup.getPitcher()
        else:
            return self.awayLineup.getPitcher()
    
    #output is of type ShowdownTeam
    def getHomeTeam(self):
        return self._HomeTeam
    
    #output is of type ShowdownTeam
    def getAwayTeam(self):
        return self._AwayTeam
    
    
    #outputs for the three below getters are of type PlayerCard, or are None
    def getFirstBase(self):
        return self._FirstBase
    
    def getSecondBase(self):
        return self._SecondBase
    
    def getThirdBase(self):
        return self._ThirdBase
    
    #inputs for the three below getters are of type PlayerCard
    def setFirstBase(self,player):
        assert isinstance(player, PlayerCard.PlayerCard) or player == None
        self._FirstBase = player 
    
    def setSecondBase(self,player):
        assert isinstance(player, PlayerCard.PlayerCard) or player == None
        self._SecondBase = player
        
    def setThirdBase(self,player):
        assert isinstance(player, PlayerCard.PlayerCard) or player == None
        self._ThirdBase = player
        
    def dieRoll(self):
        return random.randint(1,20)
    
    def attemptDoublePlay(self,runner):
        speed = runner.getSpeed()
        if self.getInningTopBottom() == "TOP":
            arm = self.homeLineup.getInfieldArm()
        else:
            arm = self.awayLineup.getInfieldArm()
        roll = self.dieRoll()
        if arm + roll > speed:
            self.tootblan(runner)
    
    # this is the main function that handles every aspect of each play - pitch, swing, advancing runners, choosing to take extra bases, turning double plays... etc.  This is going to be a doozy.
    
    def atBat(self):
        thePitcher = self.getActivePitcher()
        theBatter = self.getActiveBatter()
        thePitch = self.dieRoll()
        print("The pitch is a "+str(thePitch)+"!")
        OutcomesList = None
        ResultList = None
        atBatResult = None
        if thePitcher.getControl() + thePitch > theBatter.getOnBase():
            print ("Pitcher's advantage!")
            OutcomesList = thePitcher.getPitcherOutcomes()
            ResultList = self.PitcherOutcomes

        else:
            print ("Batter's advantage!")
            OutcomesList = theBatter.getBatterOutcomes()
            ResultList = self.BatterOutcomes
        
        # this is not working exactly correctly    
        outcomeSum = 0
        theSwing = self.dieRoll()
        print("The swing is a "+str(theSwing)+"!")
        loopCounter = 0
        # sum up the OutcomesList until you exceed the die roll
        while outcomeSum < theSwing:
            outcomeSum += OutcomesList[loopCounter] # add the next outcome
            if outcomeSum >= theSwing: # correct result identified
                atBatResult = ResultList[loopCounter] 
                # or should I return here and then set the returned value to something, for the sake of separating functions?
                # at the moment I am not, because the following (commented) tasks need to be handled before the next batter comes up.
                # although that function doesn't actually call the next batter to the plate...
            loopCounter += 1
            
        print ("the result is a "+atBatResult)
        
        #atBatResult section - this is where the fun begins...
        
        if atBatResult == "Out(PU)" or atBatResult == "Out(SO)":
            self.batterOut()
        elif atBatResult == "Out(GB)":
            if self.getFirstBase != None:
                if self.getSecondBase != None:
                    if self.getThirdBase != None:
                        #TODO: get out the man on third
                        
                        #does this code simply live in self.attemptDoublePlay()?  Possibly.
                        whichBase = input("Which base would you like to throw to - third, second, or first? ").upper()
                        possibleBases = ["FIRST","SECOND","THIRD","1ST","2ND","3RD","1","2","3"]
                        while whichBase not in possibleBases:
                            whichBase = input("Which base would you like to throw to - third, second, or first? Please select a valid option. ").upper()
                        #TODO: self.attemptDoublePlay(whichBase)
            self.batterOut()
            # if "Out(GB)" and self.getFirstBase != None then self.attemptDoublePlay()
            # if "Out(GB)" and self.getFirstBase == None and self.getSecondBase or self.getThirdBase != None then self.advanceRunnersIfFastEnough()
        elif atBatResult == "Out(FB)":
            self.batterOut()
            # if "Out(FB)" and (self.getSecondBase != None or self.getThirdBase() != None) then self.attemptTagUp(), first line of which is input("Do you want to attempt to tag up [from 2nd/3rd]?")
        elif atBatResult == "BB":
            self.scoreRun(self.getThirdBase())
            self.setThirdBase(self.getSecondBase())
            self.setSecondBase(self.getFirstBase())
            self.setFirstBase(theBatter)
            self.nextBatter()
        elif atBatResult == "single":
            self.scoreRun(self.getThirdBase())
            self.setThirdBase(self.getSecondBase())
            self.setSecondBase(self.getFirstBase())
            self.setFirstBase(theBatter)
            self.nextBatter()
        elif atBatResult == "single_plus": # if second base is empty after runners have advanced, advance the original batter to second base
            self.scoreRun(self.getThirdBase())
            self.setThirdBase(self.getSecondBase())
            self.setSecondBase(self.getFirstBase())
            if self.getSecondBase() == None:
                self.setSecondBase(theBatter)
            else:
                self.setFirstBase(theBatter)
            self.nextBatter()
        elif atBatResult == "double":
            self.scoreRun(self.getThirdBase())
            self.scoreRun(self.getSecondBase())
            self.setThirdBase(self.getFirstBase())
            self.setSecondBase(theBatter)
            self.nextBatter()
        # if "single","single_plus","double" then self.attemptTagUp() and (self.getSecondBase != None or self.getThirdBase() != None), as per above
        elif atBatResult == "triple":
            self.scoreRun(self.getThirdBase())
            self.scoreRun(self.getSecondBase())
            self.scoreRun(self.getFirstBase())
            self.setThirdBase(theBatter)
            self.nextBatter()
        elif atBatResult == "homerun":
            self.scoreRun(self.getThirdBase())
            self.scoreRun(self.getSecondBase())
            self.scoreRun(self.getFirstBase())
            self.scoreRun(theBatter)
            self.nextBatter()
        
        # on to the next batter, once every possible outcome is calculated!
        # if not (self.getFirstBase() == None and self.getSecondBase() == None and self.getThirdBase() == None and self.getOuts() == 0):
        #    self.nextBatter()
    
    def incrementInning(self): 
        #possibly: check here if game should end
        if self.getInningTopBottom() == "BOTTOM":
            self.setInningNumber(self.getInningNumber()+1)
            self.setInningTopBottom("TOP")
        else:
            self.setInningTopBottom("BOTTOM")
        self.setOuts(0)
        self.setFirstBase(None)
        self.setSecondBase(None)
        self.setThirdBase(None)
        
    def nextBatter(self): # ALERT: this one may be getting called once too many, or at the wrong time
        if self.getInningTopBottom() == "TOP":
            if self.awayBatterNumber == 9:
                self.awayBatterNumber = 1
            else:
                self.awayBatterNumber += 1
        if self.getInningTopBottom() == "BOTTOM":
            if self.homeBatterNumber == 9:
                self.homeBatterNumber = 1
            else:
                self.homeBatterNumber += 1
    
    def playerOut(self):
        self.getActivePitcher().setInningsPitched(self.getActivePitcher().getInningsPitched()*3+1) # add one out to pitcher's count
        if self._numberOuts == 2:
            self.incrementInning()
        else:
            self._numberOuts += 1
    
    def batterOut(self):
        self.nextBatter()
        self.playerOut()
    
    # def tootblan(self,player):
    # pass the player who was thrown out
    # self.playerOut()
            
    def scoreRun(self,player):
        if player != None:
            if self.getInningTopBottom() == "TOP":
                self.setAwayScore(self.getAwayScore()+1)
            else:
                self.setHomeScore(self.getHomeScore()+1)
        
    
    # __INITIALIZER__
    def __init__(self):#,HomeTeam,AwayTeam): #saved for later
        #self._HomeTeam = HomeTeam # not necessary as of now, will be in the future to ensure only full, legal teams are used
        #self._AwayTeam = AwayTeam # not necessary as of now, will be in the future to ensure only full, legal teams are used
        numInnings = input("Please select how many innings will be played. ") # number of innings to play
        try: self.numberInnings = int(numInnings)
        except:
            print("Please select a positive integer number of innings to play.")
            numInnings = input("Please select how many innings will be played. ") # number of innings to play
            self.numberInnings = int(numInnings)
        assert isinstance (self.numberInnings, int) and self.numberInnings >= 1 # if fail here, program crashes, try again
        # homeLineup = homeTeam.getBattingOrder()
        self.homeLineup = ShowdownTeam.Lineup()
        self.awayLineup = ShowdownTeam.Lineup()
        # awayLineup = awayTeam.getBattingOrder()
        self.PitcherOutcomes = ["Out(PU)","Out(SO)","Out(GB)","Out(FB)","BB","single","double","homerun"]
        self.BatterOutcomes = ["Out(SO)","Out(GB)","Out(FB)","BB","single","single_plus","double","triple","homerun"]
        self.setInningNumber(1)
        self.setInningTopBottom('TOP')
        self.setHomeScore(0)
        self.setAwayScore(0)
        self._numberOuts = 0 # use setter?
        self.awayBatterNumber = 1
        self.homeBatterNumber = 1
        self.setFirstBase(None)
        self.setSecondBase(None)
        self.setThirdBase(None)
        
        activeGame = True

        while activeGame:
            # before the pitch
            # log active state
            print(self.getInningTopBottom()+" "+str(self.getInningNumber()))
            print(str(self.getAwayScore())+" - "+str(self.getHomeScore()))
            print("Pitcher: "+self.getActivePitcher().getName())
            print("Batter: "+self.getActiveBatter().getName())
            print ("O: "+str(self.getOuts()*"x"))
            if self.getFirstBase() == None:
                print ("1B:")
            else: print ("1B: "+self.getFirstBase().getLastName())
            if self.getSecondBase() == None:
                print ("2B:")
            else: print ("2B: "+self.getSecondBase().getLastName())
            if self.getThirdBase() == None:
                print ("3B:")
            else: print ("3B: "+self.getThirdBase().getLastName())
            # pitcher options
            pQuestion = None
            while (pQuestion != 'pitch' and pQuestion != 'change pitchers'):
                print (pQuestion)
                pQuestion = input("What do you want to do - 'pitch' or 'change pitchers'? ").lower()
                # if pQuestion == 'change pitchers':
                  # self.pitchingChange(newPitcher, team)
            
            # batter options - similar to pitchers', above
            '''if self.getFirstBase() != None:
                self.stealBase(self.getFirstBase(),'second')
            
            if self.getSecondBase() != None:
                self.stealBase(self.getThirdBase(),'third')
            '''
            # call atBat() to handle the pitch, swing, outcome, and all associated changes, including inning increment, and finally bring up the next batter
            self.atBat()

            #end game turn activeGame = FALSE when...
            # home team wins
            if self.getInningNumber() >= self.numberInnings and self.getOuts() == 3 and self.getInningTopBottom() == "TOP" and self.getHomeScore() > self.getAwayScore():
                activeGame = FALSE
                return ("The home team defeated the away team by a score of "+str(self.getHomeScore())+" to "+str(self.getAwayScore())+" in "+str(self.inning)+" innings.")
            # away team wins
            # self.getOuts() == 3 isn't hitting here
            if self.getInningNumber() >= self.numberInnings and self.getOuts() == 3 and self.getInningTopBottom() == "BOTTOM" and self.getHomeScore() < self.getAwayScore():
                activeGame = FALSE                
                return ("The away team defeated the home team by a score of "+str(self.getAwayScore())+" to "+str(self.getHomeScore())+" in "+str(self.inning)+" innings.")

# temporary fix to make sure there is a list of cards
# gameDict = PlayerCardCreator.doTheThing()
    
newGame = Gameplay()
''' start! This calls the initializer.  What should happen now:

1. The players are prompted to input how many innings they will play.
2. The home team is prompted to add its lineup (see ShowdownTeam.py for details).
3. The away team is prompted to add its lineup.
4. The scoreboard is set to 0-0 in the top of the 1st inning with 0 outs.
5. The first batter is set to be due up next for each team.

'''
        