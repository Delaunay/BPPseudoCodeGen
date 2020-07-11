
from codegen.ue4_stub import *

from Script.AkAudio import PostAkEvent
from Script.Engine import Lerp
from Script.Engine import FClamp
from Game.FactoryGame.Interface.UI.Audio.FuseLever.Play_UI_PowerLossLever_Click_Down import Play_UI_PowerLossLever_Click_Down
from Script.Engine import Delay
from Script.Engine import Pawn
from Script.Engine import LatentActionInfo
from Game.FactoryGame.Interface.UI.InGame.-Shared.Widget_Fusebox import ExecuteUbergraph_Widget_Fusebox
from Script.Engine import Ease
from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import EqualEqual_FloatFloat
from Game.FactoryGame.Interface.UI.InGame.-Shared.Widget_Fusebox import ExecuteUbergraph_Widget_Fusebox.K2Node_ComponentBoundEvent_Value
from Script.UMG import SetRenderScale
from Script.UMG import PlayAnimation
from Script.Engine import GreaterEqual_FloatFloat
from Script.Engine import GetWorldDeltaSeconds
from Script.UMG import StopAnimation
from Script.UMG import SetValue
from Game.FactoryGame.Interface.UI.Audio.FuseLever.Play_UI_PowerLossLever_Lock import Play_UI_PowerLossLever_Lock
from Game.FactoryGame.Interface.UI.Audio.FuseLever.Play_UI_PowerLossLever_Fail import Play_UI_PowerLossLever_Fail
from Game.FactoryGame.Interface.UI.InGame.-Shared.Widget_Fusebox import ExecuteUbergraph_Widget_Fusebox.K2Node_Event_InDeltaTime
from Game.FactoryGame.Interface.UI.InGame.-Shared.Widget_Fusebox import ExecuteUbergraph_Widget_Fusebox.K2Node_Event_MyGeometry
from Script.Engine import Default__GameplayStatics
from Script.UMG import WidgetAnimation
from Script.AkAudio import Default__AkGameplayStatics
from Script.UMG import UserWidget
from Script.UMG import GetOwningPlayerPawn
from Game.FactoryGame.Interface.UI.Audio.FuseLever.Play_UI_PowerLossLever_Click_Up import Play_UI_PowerLossLever_Click_Up
from Script.UMG import UMGSequencePlayer
from Script.CoreUObject import Vector2D
from Script.AkAudio import AkComponent
from Script.UMG import GetValue

class Widget_Fusebox(UserWidget):
    SpawnAnim: Ptr[WidgetAnimation]
    IdleAnim: Ptr[WidgetAnimation]
    ShakeAnim: Ptr[WidgetAnimation]
    ResetFuse: FMulticastScriptDelegate
    IsFuseReset: bool
    T: float
    TempValue: float
    LerpActive: bool
    mCurrentLeverValue: float
    mLastLeverValue: float
    NewVar_0: float
    
    def Get_HandleShadow_Value_0(self):
        ReturnValue: float = self.HandleSlider.GetValue()
        ReturnValue_0: float = Ease(0, 1, ReturnValue, 5, 2, 2)
        ReturnValue_1: float = ReturnValue_0 - 0.5
        ReturnValue_2: float = ReturnValue_1 * 2
        ReturnValue_3: Vector2D = Vector2D(1, ReturnValue_2)
        self.BarsShadow.SetRenderScale(ReturnValue_3)
        ReturnValue = self.HandleSlider.GetValue()
        ReturnValue_0 = Ease(0, 1, ReturnValue, 5, 2, 2)
        ReturnValue_4: float = ReturnValue_0
    

    def GetHandleSliderClickabe(self):
        if not self.IsFuseReset:
            goto('L39')
        ReturnValue = 3
        goto('L59')
        # Label 39
        ReturnValue = 0
    

    def BndEvt__Button_0_K2Node_ComponentBoundEvent_0_OnButtonClickedEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_Fusebox(412)
    

    def Tick(self):
        ExecuteUbergraph_Widget_Fusebox.K2Node_Event_MyGeometry = MyGeometry #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_Fusebox.K2Node_Event_InDeltaTime = InDeltaTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_Fusebox(432)
    

    def BndEvt__Slider_0_K2Node_ComponentBoundEvent_1_OnFloatValueChangedEvent__DelegateSignature(self, Value: float):
        ExecuteUbergraph_Widget_Fusebox.K2Node_ComponentBoundEvent_Value = Value #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_Fusebox(1884)
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_Fusebox(2647)
    

    def ResetFusebox(self):
        self.ExecuteUbergraph_Widget_Fusebox(2739)
    

    def BndEvt__HandleSlider_K2Node_ComponentBoundEvent_2_OnMouseCaptureEndEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_Fusebox(2755)
    

    def BndEvt__HandleSlider_K2Node_ComponentBoundEvent_3_OnControllerCaptureEndEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_Fusebox(2882)
    

    def RestFuseWithAnimation(self):
        self.ExecuteUbergraph_Widget_Fusebox(3190)
    

    def ExecuteUbergraph_Widget_Fusebox(self):
        goto(ComputedJump("EntryPoint"))
        self.ResetFuse.ProcessMulticastDelegate()
        self.ResetFusebox()
        ReturnValue1: Ptr[Pawn] = self.GetOwningPlayerPawn()
        ReturnValue1_0: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_UI_PowerLossLever_Fail, ReturnValue1, True)
        goto(ExecutionFlow.Pop())
        # Label 130
        ReturnValue: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.SpawnAnim, 0, 1, 0, 1)
        self.HandleSlider.SetValue(1)
        ReturnValue2: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.IdleAnim, 0, 0, 0, 1)
        self.OffLight.SetVisibility(0)
        self.OnLight.SetVisibility(2)
        self.ResetFuseScreen.SetVisibility(0)
        self.FuseOkScreen.SetVisibility(2)
        goto(ExecutionFlow.Pop())
        self.ResetFuse.ProcessMulticastDelegate()
        goto(ExecutionFlow.Pop())
        ReturnValue_0: float = self.HandleSlider.GetValue()
        ReturnValue1_1: float = FClamp(ReturnValue_0, 0.5, 1)
        ReturnValue_1: float = ReturnValue1_1 - 0.5
        ReturnValue1_2: float = ReturnValue_1 * 2
        ReturnValue1_3: Vector2D = Vector2D(1, ReturnValue1_2)
        self.BarsBottom.SetRenderScale(ReturnValue1_3)
        ReturnValue_0 = self.HandleSlider.GetValue()
        ReturnValue_2: float = FClamp(ReturnValue_0, 0, 0.5)
        ReturnValue_3: float = ReturnValue_2 * 2
        ReturnValue1_4: float = 1 - ReturnValue_3
        ReturnValue_4: Vector2D = Vector2D(1, ReturnValue1_4)
        self.BarsTop.SetRenderScale(ReturnValue_4)
        if not self.LerpActive:
           goto(ExecutionFlow.Pop())
        ReturnValue1_5: float = self.HandleSlider.GetValue()
        ReturnValue_5: bool = ReturnValue1_5 <= 0.6000000238418579
        if not ReturnValue_5:
            goto('L1483')
        ReturnValue1_6: float = Default__GameplayStatics.GetWorldDeltaSeconds(self)
        ReturnValue1_7: float = ReturnValue1_6 / 0.20000000298023224
        ReturnValue1_8: float = ReturnValue1_7 + self.T
        self.T = ReturnValue1_8
        ReturnValue1_9: float = Lerp(self.TempValue, 0, self.T)
        self.HandleSlider.SetValue(ReturnValue1_9)
        ReturnValue4: float = self.HandleSlider.GetValue()
        ReturnValue_6: bool = ReturnValue4 <= 0
        if not ReturnValue_6:
           goto(ExecutionFlow.Pop())
        self.LerpActive = False
        self.HandleSlider.SetValue(0)
        self.RestFuseWithAnimation()
        goto(ExecutionFlow.Pop())
        # Label 1483
        ReturnValue_7: float = Default__GameplayStatics.GetWorldDeltaSeconds(self)
        ReturnValue_8: float = ReturnValue_7 / 0.5
        ReturnValue_9: float = ReturnValue_8 + self.T
        self.T = ReturnValue_9
        ReturnValue_10: float = Lerp(self.TempValue, 1, self.T)
        self.HandleSlider.SetValue(ReturnValue_10)
        ReturnValue3: float = self.HandleSlider.GetValue()
        ReturnValue_11: bool = GreaterEqual_FloatFloat(ReturnValue3, 1)
        if not ReturnValue_11:
           goto(ExecutionFlow.Pop())
        self.LerpActive = False
        self.HandleSlider.SetValue(1)
        goto(ExecutionFlow.Pop())
        if not self.IsFuseReset:
            goto('L1936')
        self.HandleSlider.SetValue(0)
        goto(ExecutionFlow.Pop())
        # Label 1936
        ExecutionFlow.Push("L2219")
        self.mCurrentLeverValue = Value
        ReturnValue1_10: bool = GreaterEqual_FloatFloat(self.mCurrentLeverValue, self.mLastLeverValue)
        if not ReturnValue1_10:
            goto('L2448')
        ReturnValue2_0: float = self.mLastLeverValue + 0.05000000074505806
        ReturnValue2_1: bool = GreaterEqual_FloatFloat(self.mCurrentLeverValue, ReturnValue2_0)
        if not ReturnValue2_1:
           goto(ExecutionFlow.Pop())
        self.mLastLeverValue = self.mCurrentLeverValue
        ReturnValue2_2: Ptr[Pawn] = self.GetOwningPlayerPawn()
        ReturnValue3_0: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_UI_PowerLossLever_Click_Up, ReturnValue2_2, True)
        goto(ExecutionFlow.Pop())
        # Label 2219
        ReturnValue_12: float = Ease(0, 1, Value, 6, 5, 2)
        self.HandleSlider.SetValue(ReturnValue_12)
        ReturnValue_12 = Ease(0, 1, Value, 6, 5, 2)
        ReturnValue_13: bool = EqualEqual_FloatFloat(ReturnValue_12, 0)
        if not ReturnValue_13:
           goto(ExecutionFlow.Pop())
        self.IsFuseReset = True
        self.RestFuseWithAnimation()
        goto(ExecutionFlow.Pop())
        # Label 2448
        ReturnValue2_3: float = self.mLastLeverValue - 0.05000000074505806
        ReturnValue1_11: bool = self.mCurrentLeverValue <= ReturnValue2_3
        if not ReturnValue1_11:
           goto(ExecutionFlow.Pop())
        self.mLastLeverValue = self.mCurrentLeverValue
        ReturnValue2_2 = self.GetOwningPlayerPawn()
        ReturnValue2_4: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_UI_PowerLossLever_Click_Down, ReturnValue2_2, True)
        goto(ExecutionFlow.Pop())
        self.ResetFusebox()
        goto(ExecutionFlow.Pop())
        # Label 2662
        Default__KismetSystemLibrary.Delay(self, 1, LatentActionInfo(Linkage = 15, UUID = -979767424, ExecutionFunction = "ExecuteUbergraph_Widget_Fusebox", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        self.IsFuseReset = False
        goto('L130')
        # Label 2755
        if not self.IsFuseReset:
            goto('L2770')
        goto(ExecutionFlow.Pop())
        # Label 2770
        self.T = 0
        ReturnValue2_5: float = self.HandleSlider.GetValue()
        self.TempValue = ReturnValue2_5
        self.LerpActive = True
        goto(ExecutionFlow.Pop())
        goto('L2755')
        # Label 2887
        ReturnValue1_12: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.ShakeAnim, 0, 1, 0, 1)
        ReturnValue_14: Ptr[Pawn] = self.GetOwningPlayerPawn()
        ReturnValue_15: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_UI_PowerLossLever_Lock, ReturnValue_14, True)
        self.StopAnimation(self.IdleAnim)
        self.OnLight.SetVisibility(0)
        self.OffLight.SetVisibility(2)
        self.ResetFuseScreen.SetVisibility(2)
        self.FuseOkScreen.SetVisibility(0)
        goto('L2662')
        goto('L2887')
    

    def ResetFuse__DelegateSignature(self):
        pass
    
