
from codegen.ue4_stub import *

from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import LatentActionInfo
from Game.FactoryGame.Interface.UI.Menu.MainMenu.Widget_CoffeeSplash import ExecuteUbergraph_Widget_CoffeeSplash
from Script.UMG import UMGSequencePlayer
from Script.UMG import PlayAnimation
from Script.UMG import Unhandled
from Script.Engine import Delay
from Script.UMG import IsAnimationPlaying
from Script.UMG import BindToAnimationFinished
from Script.UMG import WidgetAnimation
from Script.UMG import Default__WidgetBlueprintLibrary
from Script.UMG import UnbindAllFromAnimationFinished
from Script.UMG import EventReply
from Script.UMG import UserWidget

class Widget_CoffeeSplash(UserWidget):
    SpawnAnim: Ptr[WidgetAnimation]
    FadeOut: Ptr[WidgetAnimation]
    
    def OnKeyDown(self):
        self.HideSplash()
        ReturnValue: EventReply = Default__WidgetBlueprintLibrary.Unhandled()
        ReturnValue_0: EventReply = ReturnValue
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_CoffeeSplash(153)
    

    def BndEvt__mButton_K2Node_ComponentBoundEvent_0_OnButtonClickedEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_CoffeeSplash(158)
    

    def HideSplash(self):
        self.ExecuteUbergraph_Widget_CoffeeSplash(271)
    

    def Cleanup(self):
        self.ExecuteUbergraph_Widget_CoffeeSplash(354)
    

    def ExecuteUbergraph_Widget_CoffeeSplash(self):
        goto(ComputedJump("EntryPoint"))
        self.HideSplash()
        goto(ExecutionFlow.Pop())
        # Label 30
        ReturnValue: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.SpawnAnim, 0, 1, 0, 1)
        Default__KismetSystemLibrary.Delay(self, 2, LatentActionInfo(Linkage = 15, UUID = 1454444351, ExecutionFunction = "ExecuteUbergraph_Widget_CoffeeSplash", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        goto('L30')
        self.HideSplash()
        goto(ExecutionFlow.Pop())
        # Label 173
        ReturnValue1: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.FadeOut, 0, 1, 0, 1)
        OutputDelegate.BindUFunction(self, Cleanup)
        self.BindToAnimationFinished(self.FadeOut, OutputDelegate)
        goto(ExecutionFlow.Pop())
        ReturnValue_0: bool = self.IsAnimationPlaying(self.FadeOut)
        if not ReturnValue_0:
            goto('L173')
        goto(ExecutionFlow.Pop())
        # Label 315
        self.RemoveFromParent()
        goto(ExecutionFlow.Pop())
        # Label 330
        self.UnbindAllFromAnimationFinished(self.FadeOut)
        goto('L315')
        goto('L330')
    
