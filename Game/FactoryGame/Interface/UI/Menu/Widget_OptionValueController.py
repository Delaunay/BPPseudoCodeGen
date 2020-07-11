
from codegen.ue4_stub import *

from Game.FactoryGame.Interface.UI.Menu.Widget_OptionValueController import ExecuteUbergraph_Widget_OptionValueController
from Script.FactoryGame import FGOptionsValueController
from Script.CoreUObject import LinearColor

class Widget_OptionValueController(FGOptionsValueController):
    mHoveredColor: LinearColor = Namespace(A=1, B=1, G=1, R=1)
    mUnhoveredColor: LinearColor = Namespace(A=1, B=0.9890260100364685, G=0.9890260100364685, R=1)
    mDarkColor: LinearColor = Namespace(A=1, B=0.13563300669193268, G=0.13286800682544708, R=0.13286800682544708)
    
    def Construct(self):
        self.ExecuteUbergraph_Widget_OptionValueController(29)
    

    def ExecuteUbergraph_Widget_OptionValueController(self):
        # Label 10
        self.OnRowUnhovered()
        # End
        goto('L10')
    
