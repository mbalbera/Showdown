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

# A lineup is a list of 9 batters who each are assigned one position.
# Batting order is stored as a string of PlayerCards
# Each PlayerCard is stored separately in its position
class Lineup(list):
    
    # GETTERS AND SETTERS
    
    def getBattingOrder(self):
        return self._BattingOrder()
    
    def getCatcherArm(self): # doesn't work as of now, still figuring out how the lineup knows who is playing where, but concept is correct
        return self.catcher.Fielding
    
    def getInfieldArm(self): # doesn't work as of now, still figuring out how the lineup knows who is playing where, but concept is correct
        return sum(self.firstbase.Fielding,self.secondbase.Fielding,self.thirdbase.Fielding,self.shortstop.Fielding)
    
    def getOutfieldArm(): # doesn't work as of now, still figuring out how the lineup knows who is playing where, but concept is correct
        return sum(self.leftfield.Fielding,self.centerfield.Fielding,self.rightfield.Fielding)
    
    def setPitcher(self,thePitcher):
        assert isinstance(thePitcher,PitcherCard)
        self._Pitcher = thePitcher
        
    def getBatter(self,spot):
        assert isinstance(spot, integer)
        assert spot >= 1
        assert spot <= 9
        return self.getLineup()[spot]
        
    def setLineup(homeOrAway,self): #critical, as this is the only function called in the initializer
        assert homeOrAway.upper() == "HOME" or homeOrAway.upper() == "AWAY"
        theLineup = []
        availablePositions = ["C","1B","2B","3B","SS","LF","CF","RF","DH","P"] # at the moment, no pitcher is set whether or not there is a DH
        i = 1
        while i < 10:
            selectedBatter = input() # ask "which batter would you like to place in the "+i+" spot in the lineup?"
            selectedBatterPosition = input()
            # the below two segments work individually, but should be done at once in order to avoid removing the position from the availablePositions list or placing the batter in the lineup unless both conditions are satisfied
            
            #TODO: make this into its own "assign position" function, as this will have to be redone when making subs
            if isinstance(selectedBatter,PlayerCard):
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
                
                theLineup[i] = selectedBatter # if all of the if statement and the two try statements pass, place batter in lineup                
                
                # make it so the lineup knows what position the batter is playing for the purposes of calculating fielding
                #TODO: implement me
                
            else:
                print("The batter you've selected is not a valid PlayerCard.")
                continue # if passed an invalid PlayerCard, restart loop at current i without incrementing
            i += 1
            # set the pitcher
            # add ability to deal with an extra pitcher if there is no pitcher in lineup
        self._BattingOrder = theLineup
    
    #__INITIALIZER__
    # I belive doing as such solves the problem of how to always check that the lineup has exactly one player playing each position and ability to understand who is playing where (ie to calculate fielding as needed)

    def __init__(self): # initializing as empty, appending done subsequently
        self.setLineup() # this function handles lineup setting
        # save me for later in case decide to use this initializer type. (self,batter1,batter1pos,batter2,batter2pos,batter3,batter3pos,batter4,batter4pos,batter5,batter5pos,batter6,batter6pos,batter7,batter7pos,batter8,batter8pos,batter9,batter9pos,pitcher1=none): # optional pitcher argument if DH used
        #TODO: this initializer is extra.  replace this with a loop.
        ''' This is a better way to select and create teams
        This has been moved to self.setLineup()
        
        
        theLineup = [] # do a home and away
        availablePositions = ["C","1B","2B","3B","SS","LF","CF","RF","DH","P"]
        i = 1
        while i < 10:
            selectedBatter = input() # ask "which batter would you like to place in the "+i+" spot in the lineup?"
            selectedBatterPosition = input()
            # the below two segments work individually, but should be done at once in order to avoid removing the position from the availablePositions list or placing the batter in the lineup unless both conditions are satisfied
            
            if isinstance(selectedBatter,PlayerCard):
                try: # if both the if statement and the try statement pass, do both things
                    availablePositions.remove(selectedBatterPosition) # if both the if statement and the try statement pass, remove selected position from availablePositions
                except ValueError: # print statement on following line is self-explanatory
                    print("You've either already placed someone in that position, or the position you've selected is invalid.  Please try again!")
                    continue # if this block hits, restart loop at current i without incrementing
                theLineup[i] = selectedBatter # if both the if statement and the try statement pass, place batter in lineup
                selectedBatter.setCurrentPosition(selectedBatterPosition) # if both the if statement and the try statement pass, set batter's position
            else:
                print("The batter you've selected is not a valid PlayerCard.")
                continue # if passed an invalid PlayerCard, restart loop at current i without incrementing
            i += 1
        '''    
        
        # The above loop structure is cleaner AND a better UX!  Huge win!
        
        '''assert isinstance (batter1, PlayerCard), 'The first batter is not a card in your deck.'
        assert isinstance (batter2, PlayerCard)
        assert isinstance (batter3, PlayerCard)
        assert isinstance (batter4, PlayerCard)
        assert isinstance (batter5, PlayerCard)
        assert isinstance (batter6, PlayerCard)
        assert isinstance (batter7, PlayerCard)
        assert isinstance (batter8, PlayerCard)
        assert isinstance (batter9, PlayerCard)''' # did this better below
        
        # this block might better at thoroughly checking that each batter is indeed a batter, but I think is unnecessary as the above while loop is almost as foolproof and way easier
        '''self._BattingOrder = [batter1,batter2,batter3,batter4,batter5,batter6,batter7,batter8,batter9]
        for eachHitter in range(0,9):
            assert isinstance (self.getBattingOrder()[eachHitter],PlayerCard), ('The batter in position '+str(eachHitter)+'is not a card in your deck.')
            battersPosition = self.getBattingOrder()[eachHitter].getCurrentPosition() #TODO: assign positions in lineup
            if battersPosition == "C":
                count_C += 1
            elif battersPosition == "1B":
                count_1B += 1
            elif battersPosition == "2B":
                count_2B += 1
            elif battersPosition == "3B":
                count_3B += 1
            elif battersPosition == "SS":
                count_SS += 1
            elif battersPosition == "LF":
                count_LF += 1
            elif battersPosition == "CF":
                count_CF += 1
            elif battersPosition == "RF":
                count_RF += 1
            elif battersPosition == "P":
                count_P_DH += 1
                count_P += 1
                self.setPitcher(self.getBattingOrder()[eachHitter])
            elif battersPosition == "DH":
                count_P_DH += 1
            
        
        assert max(count_C,count_1B,count_2B,count_3B,count_SS,count_SS,count_LF,count_CF,count_RF,count_P_DH) == 1 and min(count_C,count_1B,count_2B,count_3B,count_SS,count_SS,count_LF,count_CF,count_RF,count_P_DH) == 1 # exactly one player at each position
        '''

class ShowdownTeam(object): # not strictly necessary for basic operation but will be eventually
    
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