
from codegen.ue4_stub import *

from Game.FactoryGame.Interface.UI.InGame.-Shared.Widget_PulsingNamedSlot import ExecuteUbergraph_Widget_PulsingNamedSlot
from Script.Engine import Default__KismetSystemLibrary
from Script.UMG import UMGSequencePlayer
from Script.Engine import Delay
from Script.UMG import PlayAnimation
from Script.UMG import SetContentColorAndOpacity
from Script.UMG import StopAnimation
from Script.UMG import WidgetAnimation
from Script.Engine import LatentActionInfo
from Script.UMG import UserWidget
from Script.CoreUObject import LinearColor

class Widget_PulsingNamedSlot(UserWidget):
    IdleAnimation: Ptr[WidgetAnimation]
    IsAnimating: bool
    
    def mPlayPulseAnim(self):
        self.ExecuteUbergraph_Widget_PulsingNamedSlot(165)
    

    def mStopPulseAnim(self):
        self.ExecuteUbergraph_Widget_PulsingNamedSlot(170)
    

    def ExecuteUbergraph_Widget_PulsingNamedSlot(self):
        goto(ComputedJump("EntryPoint"))
        # Label 15
        Default__KismetSystemLibrary.Delay(self, 1, LatentActionInfo(Linkage = 92, UUID = 1080282334, ExecutionFunction = "ExecuteUbergraph_Widget_PulsingNamedSlot", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        if not self.IsAnimating:
            goto('L107')
        goto(ExecutionFlow.Pop())
        # Label 107
        ReturnValue: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.IdleAnimation, 0, 0, 0, 1)
        self.IsAnimating = True
        goto(ExecutionFlow.Pop())
        goto('L15')
        self.StopAnimation(self.IdleAnimation)
        self.Border_0.SetContentColorAndOpacity(LinearColor(R = 1, G = 1, B = 1, A = 0))
        self.IsAnimating = False
        goto(ExecutionFlow.Pop())
    
