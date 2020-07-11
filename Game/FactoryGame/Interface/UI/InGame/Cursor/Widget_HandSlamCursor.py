
from codegen.ue4_stub import *

from Script.UMG import UMGSequencePlayer
from Script.UMG import PlayAnimation
from Script.UMG import WidgetAnimation
from Game.FactoryGame.Interface.UI.InGame.Cursor.Widget_HandSlamCursor import ExecuteUbergraph_Widget_HandSlamCursor
from Script.UMG import UserWidget

class Widget_HandSlamCursor(UserWidget):
    Idle: Ptr[WidgetAnimation]
    
    def Construct(self):
        self.ExecuteUbergraph_Widget_HandSlamCursor(61)
    

    def ExecuteUbergraph_Widget_HandSlamCursor(self):
        # Label 10
        ReturnValue: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.Idle, 0, 0, 0, 1)
        # End
        goto('L10')
    
