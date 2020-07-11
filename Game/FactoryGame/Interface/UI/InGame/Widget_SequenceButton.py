
from codegen.ue4_stub import *

from Game.FactoryGame.Interface.UI.InGame.Widget_Button import Widget_Button
from Script.LevelSequence import LevelSequence

class Widget_SequenceButton(Widget_Button):
    mSequence: Ptr[LevelSequence]
    
