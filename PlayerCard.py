# PlayerCard.py

"""This module contains the aspects of batter and pitcher Showdown Cards.
Attributes include point value, position, control (pitchers only), on-base (batters only), and outcome ranges.
Outcome ranges for pitchers include Out(PU), Out(SO), Out(GB), Out(FB), BB, 1B, 2B, and HR.
Outcome ranges for pitchers include Out(SO), Out(GB), Out(FB), BB, 1B, 1B+ 2B, 3B and HR.

"""

class PlayerCard(object):
    # GETTERS AND SETTERS
    
    def getPointValue(self):
        return self._PointValue
    
    def getPosition(self):
        return self._Position
    
    def getSpeed(self):
        return self._Speed
    
    def setCurrentPosition(self,position):
        positions = ["C","1B","2B","3B","SS","LF","RF","CF","P","DH"]
        assert position in positions
        #TODO: check that the batterCard can play the position to which he is passed
        # figure out what error this throws if not, so the try/except block in setLineup() under class Lineup can work correctly
        self._CurrentPosition = position
    
    def getCurrentPosition(self):
        return self._CurrentPosition
    
    class PitcherCard(PlayerCard):
        # GETTERS AND SETTERS
    
        def getControl(self):
            return self._Control
        
        def getPitcherOutcomes(self):
            return self._PitcherOutcomes
        
        #__INITIALIZER__
        # Awards to be added later
        def __init__(self,nameFirst,nameLast,PointValue,Position,Control,IP,OutPU,OutSO,OutGB,OutFB,BB,single,double,homerun):
            assert isinstance(nameFirst, string)
            assert isinstance(nameLast, string)
            assert Position == "Starter" or Position == "Reliever" or Position == "Closer"
            assert isinstance(Control, integer)
            assert Control >= 0
            assert Control <= 6
            assert isinstance(IP,integer)
            assert IP >= 1
            assert IP <= 9
            # the input values are the size of each range
            # TODO: add error messages to each assertion
            assert isinstance(OutPU, integer) and OutPU >= 0
            assert isinstance(OutSO, integer) and OutSO >= 0
            assert isinstance(OutGB, integer) and OutGB >= 0
            assert isinstance(OutFB, integer) and OutFB >= 0
            assert isinstance(BB, integer) and BB >= 0
            assert isinstance(single, integer) and single >= 0
            assert isinstance(double, integer) and double >= 0
            assert isinstance(homerun, integer) and homerun >= 0
            
            self._PointValue = PointValue
            self._Position = Position
            self._Control = Control
            self._Speed = 10
            
            self._PitcherOutcomes = tuple(OutPU,OutSO,OutGB,OutFB,BB,single,double,homerun) # change to nature of outcomes (now additive) will require this to change
            
        
    class BatterCard(PlayerCard):
        # GETTERS AND SETTERS
    
        def getOnBase(self):
            return self._OnBase
        
        def getBatterOutcomes(self):
            return self._BatterOutcomes
        
        #__INITIALIZER__
        # Awards to be added later
        # Secondary position to be added later
        def __init__(self,nameFirst,nameLast,PointValue,Position,Fielding,OnBase,Speed,OutSO,OutGB,OutFB,BB,single,single_plus,double,triple,homerun):
            #TODO: add error messages to each assertion
            assert isinstance(nameFirst, string)
            assert isinstance(nameLast, string)
            assert Position == "C" or Position == "1B" or Position == "2B" or Position == "3B" or Position == "SS" or Position == "LF/RF" or Position == "CF" or Position == "OF" or Position == "IF" or Position == "2B/SS" or Position == "2B/3B" or Position == "-"
            assert isinstance(Control, integer)
            assert Control >= 0
            assert Control <= 6
            assert isinstance(Fielding, integer)
            assert Fielding >= -1
            assert Fielding <= 12
            assert isinstance(Speed,integer)
            assert Speed >= 8
            assert Speed <= 28
            assert isinstance(OutSO, integer) and OutSO >= 0
            assert isinstance(OutGB, integer) and OutGB >= 0
            assert isinstance(OutFB, integer) and OutFB >= 0
            assert isinstance(BB, integer) and BB >= 0
            assert isinstance(single, integer) and single >= 0
            assert isinstance(single_plus, integer) and single_plus >= 0
            assert isinstance(double, integer) and double >= 0
            assert isinstance(triple, integer) and triple >= 0
            assert isinstance(homerun, integer) and homerun >= 0
            
            self._PointValue = PointValue
            self._Position = Position
            self._Fielding = Fielding
            self._OnBase = OnBase
            self._Speed = Speed
            
            self._BatterOutcomes = tuple(OutSO,OutGB,OutFB,BB,single,single_plus,double,triple,homerun)
            
            self._CurrentPosition = None
