# ShowdownTeam.py

"""This module contains all aspects of teams in a Showdown game.
Attributes (members) of a team are all of type PlayerCard & include:
a lineup, starting pitching staff, relief pitching staff, and bench.
A valid team includes the following 20 PlayerCard members:
A lineup of 9 cards, one who plays each position (including DH)
A starting pitching staff of 4 cards
A relief corps of 1-4 cards & a bench of 3-6 cards, totaling 7 cards between the two

One starting pitcher is designated as the active starting pitcher using a boolean value.
"""

import PlayerCard
import pyperclip
import PlayerCardCreator

# A lineup is a list of 9 batters who each are assigned one position.
# Batting order is stored as a string of PlayerCards
# Each PlayerCard is stored separately in its position
class Lineup(list):
    
    # GETTERS AND SETTERS
    
    def getBattingOrder(self):
        return self._BattingOrder
    
    def getCatcherArm(self): # doesn't work as of now, still figuring out how the lineup knows who is playing where, but concept is correct
        return self.catcher.Fielding
    
    def getInfieldArm(self): # doesn't work as of now, still figuring out how the lineup knows who is playing where, but concept is correct
        return sum(self.firstbase.Fielding,self.secondbase.Fielding,self.thirdbase.Fielding,self.shortstop.Fielding)
    
    def getOutfieldArm(): # doesn't work as of now, still figuring out how the lineup knows who is playing where, but concept is correct
        return sum(self.leftfield.Fielding,self.centerfield.Fielding,self.rightfield.Fielding)
    
    def setPitcher(self,thePitcher):
        assert isinstance(thePitcher,PlayerCard.PitcherCard) or thePitcher == None
        
        if self._Pitcher == None:
            self._Pitcher = thePitcher
        else: # self.getPitcher() != None:
            assert isinstance(thePitcher,PlayerCard.PitcherCard)
            # remove self.getPitcher() from possible new pitchers
            self._Pitcher = thePitcher
        
    def getPitcher(self):
        return self._Pitcher
        
    def getBatter(self,spot):
        assert isinstance(spot, int)
        assert spot >= 1
        assert spot <= 9
        return self.getBattingOrder()[spot-1] # so that batter's number in order follows 1-9 convention while call to list is indexed correctly, e.g. starting with 0
        
    def setLineup(self): #critical, as this is the only function called in the initializer
        gameDict = PlayerCardCreator.doTheThing() # dictionary of possible cards
        
        # for temporary debugging purposes
        theLineup = [gameDict['Edgar Renteria2004'],gameDict['Juan Pierre2001'],gameDict['Luis Gonzalez2002'],gameDict['Mark Grace2004'],gameDict['Vinny Castilla2002'],gameDict['Eric Young2004'],gameDict['Carl Crawford2003'],gameDict['Toby Hall2003'],gameDict['Harold Baines2000']]
        for player in theLineup:
            # quick check
            print (player.getName())
        self.setPitcher(gameDict['Tom Seaver2004'])
        # quick check
        print (self.getPitcher().getName())
        
        '''theLineup = []
        availablePositions = ["C","1B","2B","3B","SS","LF","CF","RF","DH","P"] # at the moment, no pitcher is set whether or not there is a DH
        i = 1
        while i < 10:
            # First thing's first: set the pitcher.  Should happen one time and one time only.
            if i == 1 and self.getPitcher() == None:
                selectedPitcherName = input("Please select a starting pitcher. ").title()
                try: selectedPitcher = gameDict[selectedPitcherName]
                except KeyError:
                    print("You've entered a player who is not in the list of valid players.  Please try again!")
                    continue # if this block hits, restart loop at current i without incrementing
                self.setPitcher(selectedPitcher)
                pitcherBat = input("Will your pitcher be hitting today? ")
                if pitcherBat == True or pitcherBat.upper() == "YES":
                    availablePositions.remove("DH")
                    print("The DH has been removed. Please remember to place this pitcher in the batting order.")
                    #TODO: when pitcher is placed at bat, check that it is indeed this pitcher
                    # will build this functionality later
            # Set the batter
            selectedBatterName = input("Please place a batter in the "+str(i)+" spot. ").title() # ask "which batter would you like to place in the "+i+" spot in the lineup?"
            try: selectedBatter = gameDict[selectedBatterName]
            except KeyError:
                print("You've entered a player who is not in the list of valid players.  Please try again!")
                continue # if this block hits, restart loop at current i without incrementing
            selectedBatterPosition = input("Please select a position for this player. ")
            selectedBatterPosition = selectedBatterPosition.upper() # prevents unwarranted errors
            # the below two segments work individually, but should be done at once in order to avoid removing the position from the availablePositions list or placing the batter in the lineup unless both conditions are satisfied
            
            #TODO: make this into its own "assign position" function, as this will have to be redone when making subs

            if isinstance(selectedBatter,PlayerCard.PlayerCard):
                try: selectedBatter.setCurrentPosition(selectedBatterPosition) # if both the if statement and the try statement pass, assign batter to this position
                # this may not need to assign the batter a position (to save memory) - may only need to check that he is playing there.  Leaving here for now.
                except ValueError:
                    print("You've assigned this batter to a position he can't legally play.  Please try again!")
                    continue # if this block hits, restart loop at current i without incrementing
                try: # if both the if statement, the above try statement, and this try statement pass, do both things
                    availablePositions.remove(selectedBatterPosition) # if both the if statement, the above try statement, and this try statement pass, remove selected position from availablePositions
                except ValueError: # print statement on following line is self-explanatory
                    print("You've either already placed someone in that position, or the position you've selected is invalid.  Please try again!")
                    continue # if this block hits, restart loop at current i without incrementing
                # so the batter knows what position he is playing and checks to see whether this is valid
                
                theLineup.append(selectedBatter) # if all of the if statement and the two try statements pass, place batter in lineup                
                
                # make it so the lineup knows what position the batter is playing for the purposes of calculating fielding
                #TODO: implement me
                
            else:
                print("The batter you've selected is not a valid PlayerCard.")
                continue # if passed an invalid PlayerCard, restart loop at current i without incrementing
            i += 1
            '''
        self._BattingOrder = theLineup
    
    #__INITIALIZER__
    # I belive doing as such solves the problem of how to always check that the lineup has exactly one player playing each position and ability to understand who is playing where (ie to calculate fielding as needed)

    def __init__(self): # initializing as empty, appending done subsequently
        self._Pitcher = None
        self.setLineup() # this function handles lineup setting

class ShowdownTeam: # not strictly necessary for basic operation but will be eventually
    
    # GETTERS AND SETTERS
      
    #__INITIALIZER__
    def __init__(self,lineup,rotation,bullpen,bench):
        assert isinstance(lineup,Lineup)
        assert len(lineup) == 9
        assert isinstance(rotation,list)
        assert len(rotation) == 4
        assert isinstance(bullpen,list)
        assert len(bullpen) >= 1 and len(bullpen) <= 4
        assert isinstance(bench,list)
        assert len(bench) >= 3 and len(bench) <= 6
        assert len(bullpen) + len(bench) == 7
                    
        for b in rotation:
            assert isinstance(b,PitcherCard)
            assert b.getPosition() == "Starter"
            
        for c in bullpen:
            assert isinstance(c,PitcherCard)
            assert c.getPosition() == "Reliever" or c.getPosition() == "Closer"
            
        for d in bench:
            assert isinstance(d,BatterCard)