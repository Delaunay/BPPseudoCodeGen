
from codegen.ue4_stub import *

from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import PlayerController
from Script.UMG import UMGSequencePlayer
from Script.UMG import PlayAnimation
from Script.UMG import Create
from Script.Engine import Delay
from Game.FactoryGame.Interface.UI.InGame.Cursor.Widget_DefaultCursor import Widget_DefaultCursor
from Game.FactoryGame.Interface.UI.InGame.Cursor.Widget_HandSlamCursorHard import ExecuteUbergraph_Widget_HandSlamCursorHard
from Script.UMG import WidgetAnimation
from Script.UMG import Default__WidgetBlueprintLibrary
from Script.Engine import LatentActionInfo
from Script.UMG import UserWidget
from Script.Engine import SetMouseCursorWidget

class Widget_HandSlamCursorHard(UserWidget):
    Idle: Ptr[WidgetAnimation]
    
    def Construct(self):
        self.ExecuteUbergraph_Widget_HandSlamCursorHard(136)
    

    def ExecuteUbergraph_Widget_HandSlamCursorHard(self):
        goto(ComputedJump("EntryPoint"))
        ReturnValue: Ptr[Widget_DefaultCursor] = Default__WidgetBlueprintLibrary.Create(self, Widget_DefaultCursor, None)
        ReturnValue_0: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_0.SetMouseCursorWidget(1, ReturnValue)
        goto(ExecutionFlow.Pop())
        ReturnValue_1: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.Idle, 0, 1, 0, 1)
        Default__KismetSystemLibrary.Delay(self, 1.100000023841858, LatentActionInfo(Linkage = 15, UUID = -66809512, ExecutionFunction = "ExecuteUbergraph_Widget_HandSlamCursorHard", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
    
