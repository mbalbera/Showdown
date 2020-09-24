# PlayerCard.py

"""This module contains the aspects of batter and pitcher Showdown Cards.
Attributes include point value, position, control (pitchers only), on-base (batters only), and outcome ranges.
Outcome ranges for pitchers include Out(PU), Out(SO), Out(GB), Out(FB), BB, 1B, 2B, and HR.
Outcome ranges for pitchers include Out(SO), Out(GB), Out(FB), BB, 1B, 1B+ 2B, 3B and HR.

"""

class PlayerCard: # nothing should ever be of class PlayerCard, & all cards should use the PitcherCard or BatterCard subtypes; as such, there is no initializer
    # GETTERS AND SETTERS
    
    def getPointValue(self):
        return self._PointValue
    
    def getPosition(self):
        return self._Position
    
    def getSpeed(self):
        return self._Speed
    
    def setCurrentPosition(self,position):
        positions = ["C","1B","2B","3B","SS","LF","RF","CF","P","DH"]
        assert position.upper() in positions
        #TODO: check that the batterCard can play the position to which he is passed
        # figure out what error this throws if not, so the try/except block in setLineup() under class Lineup can work correctly
        self._CurrentPosition = position
    
    def getCurrentPosition(self):
        return self._CurrentPosition
    
    def setName(self,first,last):
        self._nameFirst = first
        self._nameLast = last
    
    def getName(self):
        return self._nameFirst+" "+self._nameLast
    
    def getLastName(self):
        return self._nameLast
    
class PitcherCard(PlayerCard):
    # GETTERS AND SETTERS

    def getControl(self):
        return self._Control
    
    def getPitcherOutcomes(self):
        return self._PitcherOutcomes
    
    def getIP(self):
        return self._IP
    
    def getInningsPitched(self):
        return self._outsRecorded/3
    
    def setInningsPitched(self,numberOutsRecorded):
        self._outsRecorded = numberOutsRecorded
    
    #__INITIALIZER__
    # Awards to be added later
    def __init__(self,nameFirst,nameLast,PointValue,Position,Control,IP,OutPU,OutSO,OutGB,OutFB,BB,single,double,homerun):
        assert isinstance(nameFirst, str)
        assert isinstance(nameLast, str)
        assert Position.title() == "Starter" or Position.title() == "Reliever" or Position.title() == "Closer"
        assert isinstance(Control, int)
        assert Control >= 0
        assert Control <= 6
        assert isinstance(IP,int)
        assert IP >= 1
        assert IP <= 9
        # the input values are the size of each range
        # TODO: add error messages to each assertion
        assert isinstance(OutPU, int) and OutPU >= 0
        assert isinstance(OutSO, int) and OutSO >= 0
        assert isinstance(OutGB, int) and OutGB >= 0
        assert isinstance(OutFB, int) and OutFB >= 0
        assert isinstance(BB, int) and BB >= 0
        assert isinstance(single, int) and single >= 0
        assert isinstance(double, int) and double >= 0
        assert isinstance(homerun, int) and homerun >= 0
        
        self.setName(nameFirst,nameLast)
        self._PointValue = PointValue
        self._Position = Position
        self._Control = Control
        self._IP = IP
        self._Speed = 10
        self._outsRecorded = 0
        
        self._PitcherOutcomes = (OutPU,OutSO,OutGB,OutFB,BB,single,double,homerun)
        
    
class BatterCard(PlayerCard):
    # GETTERS AND SETTERS

    def getOnBase(self):
        return self._OnBase
    
    def getBatterOutcomes(self):
        return self._BatterOutcomes
    
    #__INITIALIZER__
    # Awards to be added later
    # Secondary position to be added later
    def __init__(self,nameFirst,nameLast,PointValue,Position,OnBase,Speed,OutSO,OutGB,OutFB,BB,single,single_plus,double,triple,homerun,Fielding = -1):
        #TODO: add error messages to each assertion
        assert isinstance(nameFirst, str)
        assert isinstance(nameLast, str)
        # the below line currently allows Position to be only 'LF', which I'll accept for now to mean LF/RF.
        assert Position == "C" or Position == "1B" or Position == "2B" or Position == "3B" or Position == "SS" or Position == "LF/RF" or Position == "CF" or Position == "OF" or Position == "IF" or Position == "2B/SS" or Position == "2B/3B" or Position == "-" or Position == "LFRF" or Position == "DH" or Position == "LF", "Position was passed "+str(Position)+", which caused a fail."
        assert isinstance(Fielding, int)
        assert Fielding >= -1
        assert Fielding <= 12
        assert isinstance(Speed,int)
        assert Speed >= 8
        assert Speed <= 28
        assert isinstance(OutSO, int) and OutSO >= 0
        assert isinstance(OutGB, int) and OutGB >= 0
        assert isinstance(OutFB, int) and OutFB >= 0
        assert isinstance(BB, int) and BB >= 0
        assert isinstance(single, int) and single >= 0
        assert isinstance(single_plus, int) and single_plus >= 0
        assert isinstance(double, int) and double >= 0
        assert isinstance(triple, int) and triple >= 0
        assert isinstance(homerun, int) and homerun >= 0
        
        self.setName(nameFirst,nameLast)
        self._PointValue = PointValue
        self._Position = Position
        self._Fielding = Fielding
        self._OnBase = OnBase
        self._Speed = Speed
        
        self._BatterOutcomes = (OutSO,OutGB,OutFB,BB,single,single_plus,double,triple,homerun)
        
        self._CurrentPosition = None
