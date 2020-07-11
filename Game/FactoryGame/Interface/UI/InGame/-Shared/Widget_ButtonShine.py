
from codegen.ue4_stub import *

from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import SetScalarParameterValue
from Script.UMG import UMGSequencePlayer
from Script.UMG import PlayAnimation
from Script.Engine import K2_SetTimerDelegate
from Script.Engine import TimerHandle
from Script.UMG import StopAnimation
from Script.UMG import WidgetAnimation
from Script.Engine import MaterialInstanceDynamic
from Script.UMG import GetDynamicMaterial
from Game.FactoryGame.Interface.UI.InGame.-Shared.Widget_ButtonShine import ExecuteUbergraph_Widget_ButtonShine
from Script.Engine import K2_ClearAndInvalidateTimerHandle
from Script.UMG import UserWidget

class Widget_ButtonShine(UserWidget):
    ShineAnim: Ptr[WidgetAnimation]
    HoverTimerHandle: TimerHandle
    mShineOnHover: bool = True
    
    def Construct(self):
        self.ExecuteUbergraph_Widget_ButtonShine(441)
    

    def HoverCheck(self):
        self.ExecuteUbergraph_Widget_ButtonShine(446)
    

    def Destruct(self):
        self.ExecuteUbergraph_Widget_ButtonShine(451)
    

    def PlayShineAnim(self):
        self.ExecuteUbergraph_Widget_ButtonShine(498)
    

    def ExecuteUbergraph_Widget_ButtonShine(self):
        # Label 10
        if not self.mShineOnHover:
            goto('L544')
        OutputDelegate.BindUFunction(self, HoverCheck)
        ReturnValue: TimerHandle = Default__KismetSystemLibrary.K2_SetTimerDelegate(OutputDelegate, 0.10000000149011612, True)
        self.HoverTimerHandle = ReturnValue
        # End
        # Label 144
        Variable: bool = False
        ReturnValue_0: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.ShineAnim, 0, 1, 0, 1)
        # End
        # Label 206
        if not Variable:
            goto('L225')
        # End
        # Label 225
        Variable = True
        self.StopAnimation(self.ShineAnim)
        ReturnValue_1: Ptr[MaterialInstanceDynamic] = self.Shine.GetDynamicMaterial()
        ReturnValue_1.SetScalarParameterValue("Progress", 0)
        # End
        # Label 352
        ReturnValue_2: bool = self.IsHovered()
        if not ReturnValue_2:
            goto('L409')
        if not Variable1:
            goto('L425')
        # End
        # Label 409
        Variable1: bool = False
        goto('L206')
        # Label 425
        Variable1 = True
        goto('L144')
        goto('L10')
        goto('L352')
        
        Default__KismetSystemLibrary.K2_ClearAndInvalidateTimerHandle(self, Ref[self.HoverTimerHandle])
        # End
        ReturnValue1: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.ShineAnim, 0, 1, 0, 1)
    
