
from codegen.ue4_stub import *

from Game.FactoryGame.Interface.UI.InGame.-Shared.Widget_Lever import ExecuteUbergraph_Widget_Lever.K2Node_Event_IsDesignTime
from Script.AkAudio import PostAkEvent
from Script.Engine import NotEqual_BoolBool
from Script.Engine import FClamp
from Script.Engine import K2_SetTimerDelegate
from Game.FactoryGame.Interface.UI.InGame.-Shared.Widget_Lever import ExecuteUbergraph_Widget_Lever
from Script.Engine import Conv_IntToFloat
from Game.FactoryGame.Interface.UI.InGame.-Shared.Widget_Lever import ExecuteUbergraph_Widget_Lever.K2Node_ComponentBoundEvent_Value
from Game.FactoryGame.Buildable.Factory.SpaceElevator.Audio.Play_SpaceElevator_Lever_Pull import Play_SpaceElevator_Lever_Pull
from Script.Engine import Ease
from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import PlayerController
from Script.UMG import SetRenderScale
from Script.UMG import PlayAnimation
from Script.UMG import SetRenderTranslation
from Script.Engine import TimerHandle
from Script.Engine import IsValid
from Script.UMG import SetValue
from Script.UMG import SetColorAndOpacity
from Script.Engine import CurveFloat
from Script.AkAudio import AkAudioEvent
from Script.UMG import WidgetAnimation
from Script.AkAudio import Default__AkGameplayStatics
from Script.UMG import UserWidget
from Script.Engine import NearlyEqual_FloatFloat
from Script.UMG import UMGSequencePlayer
from Script.Engine import Abs
from Script.CoreUObject import Vector2D
from Script.Engine import Clamp
from Script.AkAudio import AkComponent
from Script.Engine import K2_ClearAndInvalidateTimerHandle
from Script.Engine import GetFloatValue
from Script.UMG import GetValue

class Widget_Lever(UserWidget):
    PushButtonAnim: Ptr[WidgetAnimation]
    ShowButtonAnim: Ptr[WidgetAnimation]
    CurrentSelectionIndex: int32
    mLeverCurve: Ptr[CurveFloat] = Namespace(AssetPath='/Game/FactoryGame/Buildable/-Shared/Curves/LinearCurve.LinearCurve')
    mSelections: int32 = 2
    SelectionNormalizedSize: float
    OnNewSelection: FMulticastScriptDelegate
    LatestSelectionIndex: int32
    mLockBetweenSelections: bool
    LerpHandle: TimerHandle
    LerpT: float
    mLerpDelta: float = 0.01600000075995922
    LerpDuration: float = 0.10000000149011612
    LerpStartValue: float
    mMaxSelectionIndex: int32 = -1
    mMinSelectionIndex: int32 = -1
    ShowButton: bool
    mShakeAnim: Ptr[WidgetAnimation]
    mShakeAnimTarget: Ptr[UserWidget]
    mUseCutomSounds: bool
    mCustomAKSound: Ptr[AkAudioEvent]
    mAutoSelectSelection: bool
    mSliderLocked: bool
    
    def LeverShake(self, MaxOrMinSelectionIndex: int32):
        ReturnValue: bool = self.CurrentSelectionIndex != MaxOrMinSelectionIndex
        if not ReturnValue:
            goto('L66')
        self.OnShake()
    

    def OnShake(self):
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(self.mShakeAnim)
        if not ReturnValue:
            goto('L133')
        ReturnValue_0: Ptr[UMGSequencePlayer] = self.mShakeAnimTarget.PlayAnimation(self.mShakeAnim, 0, 1, 0, 1)
    

    def SetShowButton(self, ShowButton: bool):
        ReturnValue: bool = NotEqual_BoolBool(ShowButton, self.ShowButton)
        if not ReturnValue:
            goto('L182')
        self.ShowButton = ShowButton
        if not self.ShowButton:
            goto('L136')
        ReturnValue1: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.ShowButtonAnim, 0, 1, 0, 1)
        # End
        # Label 136
        ReturnValue_0: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.ShowButtonAnim, 0, 1, 1, 1)
    

    def StartLerp(self):
        
        Default__KismetSystemLibrary.K2_ClearAndInvalidateTimerHandle(self, Ref[self.LerpHandle])
        self.LerpT = 0
        ReturnValue: float = self.LeverHandle.GetValue()
        self.LerpStartValue = ReturnValue
        OutputDelegate.BindUFunction(self, LerpLever)
        ReturnValue_0: TimerHandle = Default__KismetSystemLibrary.K2_SetTimerDelegate(OutputDelegate, self.mLerpDelta, True)
        self.LerpHandle = ReturnValue_0
    

    def GetCurrentSelectionPosOnSlider(self):
        ReturnValue: float = self.CurrentSelectionIndex * self.SelectionNormalizedSize
        ReturnValue_0: float = 1 - ReturnValue
        ReturnValue_1: float = ReturnValue_0
    

    def GetCalculatedCurve(self, CurveFloat: Ptr[CurveFloat], InTime: float):
        LocalCurveFloat = CurveFloat
        LocalInTime = InTime
        ReturnValue: float = self.LeverHandle.GetValue()
        ReturnValue1: float = self.GetCurrentSelectionPosOnSlider()
        ReturnValue_0: bool = ReturnValue > ReturnValue1
        if not ReturnValue_0:
            goto('L761')
        ReturnValue_1: float = self.GetCurrentSelectionPosOnSlider()
        ReturnValue_2: float = 1 - ReturnValue_1
        ReturnValue_3: int32 = self.mSelections - 1
        ReturnValue1_0: int32 = self.mSelections - 1
        ReturnValue_4: float = Conv_IntToFloat(ReturnValue_3)
        ReturnValue3: float = self.GetCurrentSelectionPosOnSlider()
        ReturnValue2: float = 1 - ReturnValue3
        ReturnValue3_0: float = LocalInTime - ReturnValue2
        ReturnValue_5: float = ReturnValue1_0 * ReturnValue3_0
        ReturnValue_6: float = Abs(ReturnValue_5)
        ReturnValue_7: float = LocalCurveFloat.GetFloatValue(ReturnValue_6)
        ReturnValue_8: float = ReturnValue_7 / ReturnValue_4
        ReturnValue4: float = ReturnValue_2 - ReturnValue_8
        ReturnValue_9: float = ReturnValue4
        goto('L1337')
        # Label 761
        ReturnValue2_0: float = self.GetCurrentSelectionPosOnSlider()
        ReturnValue1_1: float = 1 - ReturnValue2_0
        ReturnValue_3 = self.mSelections - 1
        ReturnValue1_0 = self.mSelections - 1
        ReturnValue_4 = Conv_IntToFloat(ReturnValue_3)
        ReturnValue3 = self.GetCurrentSelectionPosOnSlider()
        ReturnValue2 = 1 - ReturnValue3
        ReturnValue3_0 = LocalInTime - ReturnValue2
        ReturnValue_5 = ReturnValue1_0 * ReturnValue3_0
        ReturnValue_6 = Abs(ReturnValue_5)
        ReturnValue_7 = LocalCurveFloat.GetFloatValue(ReturnValue_6)
        ReturnValue_8 = ReturnValue_7 / ReturnValue_4
        ReturnValue_10: float = ReturnValue_8 + ReturnValue1_1
        ReturnValue_9 = ReturnValue_10
    

    def GetSliderMinClamp(self):
        ReturnValue: bool = self.CurrentSelectionIndex > self.mMinSelectionIndex
        if not ReturnValue:
            goto('L172')
        ReturnValue_0: int32 = self.CurrentSelectionIndex - 1
        ReturnValue1: float = ReturnValue_0 * self.SelectionNormalizedSize
        ReturnValue_1: float = ReturnValue1
        goto('L245')
        # Label 172
        ReturnValue_2: float = self.mMinSelectionIndex * self.SelectionNormalizedSize
        ReturnValue_1 = ReturnValue_2
    

    def GetSliderMaxClamp(self):
        ReturnValue: bool = self.CurrentSelectionIndex <= self.mMaxSelectionIndex
        if not ReturnValue:
            goto('L172')
        ReturnValue_0: int32 = self.CurrentSelectionIndex + 1
        ReturnValue1: float = ReturnValue_0 * self.SelectionNormalizedSize
        ReturnValue_1: float = ReturnValue1
        goto('L245')
        # Label 172
        ReturnValue_2: float = self.mMaxSelectionIndex * self.SelectionNormalizedSize
        ReturnValue_1 = ReturnValue_2
    

    def SetHandle(self, Value: float):
        SlideValue = Value
        ReturnValue: float = FClamp(SlideValue, 0.5, 1)
        ReturnValue3: float = ReturnValue - 0.5
        ReturnValue1: float = ReturnValue3 * 2
        ReturnValue2: Vector2D = Vector2D(1, ReturnValue1)
        # Label 200
        self.LeverArmBottom.SetRenderScale(ReturnValue2)
        ReturnValue = FClamp(SlideValue, 0.5, 1)
        ReturnValue3 = ReturnValue - 0.5
        ReturnValue1 = ReturnValue3 * 2
        LinearColor.R = 1
        LinearColor.G = 1
        LinearColor.B = 1
        LinearColor.A = ReturnValue1
        self.LeverArmBottom.SetColorAndOpacity(LinearColor)
        ReturnValue2_0: float = 1 - SlideValue
        ReturnValue1_0: float = FClamp(ReturnValue2_0, 0.5, 1)
        ReturnValue4: float = ReturnValue1_0 - 0.5
        ReturnValue2_1: float = ReturnValue4 * 2
        ReturnValue1_1: Vector2D = Vector2D(1, ReturnValue2_1)
        self.LeverArmTop.SetRenderScale(ReturnValue1_1)
        ReturnValue2_0 = 1 - SlideValue
        ReturnValue1_0 = FClamp(ReturnValue2_0, 0.5, 1)
        ReturnValue4 = ReturnValue1_0 - 0.5
        ReturnValue2_1 = ReturnValue4 * 2
        LinearColor1.R = 1
        LinearColor1.G = 1
        LinearColor1.B = 1
        LinearColor1.A = ReturnValue2_1
        self.LeverArmTop.SetColorAndOpacity(LinearColor1)
        ReturnValue1_2: float = Ease(0, 1, SlideValue, 5, 1.5, 2)
        self.LeverShadow.SetValue(ReturnValue1_2)
        ReturnValue_0: float = Ease(0, 1, SlideValue, 5, 1, 2)
        self.LeverPlatfrormShadow.SetValue(ReturnValue_0)
        ReturnValue_1: float = 1 - SlideValue
        ReturnValue1_3: float = ReturnValue_1 - 0.5
        ReturnValue_2: float = ReturnValue1_3 * self.ButtonContainer.HeightOverride
        ReturnValue_3: Vector2D = Vector2D(1, ReturnValue_2)
        self.ButtonMover.SetRenderTranslation(ReturnValue_3)
    

    def PreConstruct(self):
        ExecuteUbergraph_Widget_Lever.K2Node_Event_IsDesignTime = IsDesignTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_Lever(1025)
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_Lever(1273)
    

    def BndEvt__LeverHandle_K2Node_ComponentBoundEvent_0_OnFloatValueChangedEvent__DelegateSignature(self, Value: float):
        ExecuteUbergraph_Widget_Lever.K2Node_ComponentBoundEvent_Value = Value #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_Lever(1441)
    

    def BndEvt__LeverHandle_K2Node_ComponentBoundEvent_3_OnMouseCaptureEndEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_Lever(2696)
    

    def BndEvt__LeverHandle_K2Node_ComponentBoundEvent_4_OnControllerCaptureEndEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_Lever(3519)
    

    def LerpLever(self):
        self.ExecuteUbergraph_Widget_Lever(3913)
    

    def BndEvt__LeverHandle_K2Node_ComponentBoundEvent_5_OnMouseCaptureBeginEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_Lever(4391)
    

    def BndEvt__LeverHandle_K2Node_ComponentBoundEvent_6_OnControllerCaptureBeginEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_Lever(4448)
    

    def ExecuteUbergraph_Widget_Lever(self):
        goto(ComputedJump("EntryPoint"))
        # Label 15
        ReturnValue1: bool = self.CurrentSelectionIndex != self.LatestSelectionIndex
        if not ReturnValue1:
           goto(ExecutionFlow.Pop())
        self.mSliderLocked = True
        self.StartLerp()
        goto(ExecutionFlow.Pop())
        # Label 89
        ExecutionFlow.Push("L15")
        ReturnValue: bool = Value <= 0.5
        if not ReturnValue:
            goto('L162')
        ExecutionFlow.Push("L185")
        if not Variable1:
            goto('L297')
        goto(ExecutionFlow.Pop())
        # Label 162
        Variable1: bool = False
        Variable1 = True
        goto(ExecutionFlow.Pop())
        # Label 185
        if not Variable1:
            goto('L200')
        goto(ExecutionFlow.Pop())
        # Label 200
        Variable1 = True
        # Label 211
        ReturnValue1_0: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue1_1: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_SpaceElevator_Lever_Pull, ReturnValue1_0, True)
        goto(ExecutionFlow.Pop())
        # Label 297
        Variable1 = True
        if not False:
           goto(ExecutionFlow.Pop())
        Variable1 = True
        goto(ExecutionFlow.Pop())
        # Label 322
        ExecutionFlow.Push("L15")
        ReturnValue1_2: bool = Value <= 0.9900000095367432
        if not ReturnValue1_2:
            goto('L451')
        ExecutionFlow.Push("L420")
        if not Variable:
            goto('L395')
        goto(ExecutionFlow.Pop())
        # Label 395
        Variable: bool = True
        if not False:
           goto(ExecutionFlow.Pop())
        Variable_0: bool = True
        goto(ExecutionFlow.Pop())
        # Label 420
        if not Variable_0:
            goto('L435')
        goto(ExecutionFlow.Pop())
        # Label 435
        Variable_0 = True
        goto('L211')
        # Label 451
        Variable_0 = False
        Variable = True
        goto(ExecutionFlow.Pop())
        # Label 474
        ReturnValue_0: float = self.GetSliderMinClamp()
        ReturnValue1_3: float = self.SelectionNormalizedSize / 2
        ReturnValue_1: float = self.LeverHandle.GetValue()
        ReturnValue_2: float = 1 - ReturnValue_1
        ReturnValue_3: bool = NearlyEqual_FloatFloat(ReturnValue_2, ReturnValue_0, ReturnValue1_3)
        if not ReturnValue_3:
            goto('L322')
        self.LeverShake(self.mMinSelectionIndex)
        ReturnValue1_4: int32 = self.CurrentSelectionIndex - 1
        ReturnValue1_5: int32 = Clamp(ReturnValue1_4, self.mMinSelectionIndex, self.mMaxSelectionIndex)
        self.CurrentSelectionIndex = ReturnValue1_5
        goto('L89')
        # Label 853
        ReturnValue_4: int32 = self.CurrentSelectionIndex + 1
        ReturnValue_5: int32 = Clamp(ReturnValue_4, self.mMinSelectionIndex, self.mMaxSelectionIndex)
        self.CurrentSelectionIndex = ReturnValue_5
        goto('L15')
        # Label 982
        self.LeverShake(self.mMaxSelectionIndex)
        goto('L853')
        # Label 1010
        self.StartLerp()
        goto(ExecutionFlow.Pop())
        ReturnValue_6: bool = self.mSelections <= 2
        if not ReturnValue_6:
           goto(ExecutionFlow.Pop())
        self.mSelections = 2
        ReturnValue2: bool = self.mMinSelectionIndex <= 0
        if not ReturnValue2:
           goto(ExecutionFlow.Pop())
        self.mMinSelectionIndex = 0
        ReturnValue1_6: bool = self.mMaxSelectionIndex <= 0
        if not ReturnValue1_6:
           goto(ExecutionFlow.Pop())
        ReturnValue3: int32 = self.mSelections - 1
        self.mMaxSelectionIndex = ReturnValue3
        goto(ExecutionFlow.Pop())
        self.SetHandle(1)
        ReturnValue2_0: int32 = self.mSelections - 1
        ReturnValue_7: float = Conv_IntToFloat(ReturnValue2_0)
        ReturnValue2_1: float = 1 / ReturnValue_7
        self.SelectionNormalizedSize = ReturnValue2_1
        goto(ExecutionFlow.Pop())
        if not self.mSliderLocked:
            goto('L1696')
        ReturnValue_8: float = self.CurrentSelectionIndex * self.SelectionNormalizedSize
        ReturnValue5: float = 1 - ReturnValue_8
        self.LeverHandle.SetValue(ReturnValue5)
        ReturnValue_8 = self.CurrentSelectionIndex * self.SelectionNormalizedSize
        ReturnValue5 = 1 - ReturnValue_8
        self.SetHandle(ReturnValue5)
        goto(ExecutionFlow.Pop())
        # Label 1696
        ReturnValue_9: float = FClamp(Value, 0, 1)
        ReturnValue1_7: float = 1 - ReturnValue_9
        ReturnValue1_8: float = self.GetSliderMaxClamp()
        ReturnValue2_2: float = self.GetSliderMinClamp()
        ReturnValue1_9: float = FClamp(ReturnValue1_7, ReturnValue2_2, ReturnValue1_8)
        ReturnValue_10: float = self.GetCalculatedCurve(self.mLeverCurve, ReturnValue1_9)
        ReturnValue3_0: float = 1 - ReturnValue_10
        ReturnValue2_3: float = FClamp(ReturnValue3_0, 0, 1)
        self.LeverHandle.SetValue(ReturnValue2_3)
        ReturnValue_9 = FClamp(Value, 0, 1)
        ReturnValue1_7 = 1 - ReturnValue_9
        ReturnValue1_8 = self.GetSliderMaxClamp()
        ReturnValue2_2 = self.GetSliderMinClamp()
        ReturnValue1_9 = FClamp(ReturnValue1_7, ReturnValue2_2, ReturnValue1_8)
        ReturnValue_10 = self.GetCalculatedCurve(self.mLeverCurve, ReturnValue1_9)
        ReturnValue3_0 = 1 - ReturnValue_10
        ReturnValue2_3 = FClamp(ReturnValue3_0, 0, 1)
        self.SetHandle(ReturnValue2_3)
        if not self.mAutoSelectSelection:
           goto(ExecutionFlow.Pop())
        ReturnValue_11: float = self.SelectionNormalizedSize / 2
        ReturnValue_12: float = self.GetSliderMaxClamp()
        ReturnValue1_10: float = self.LeverHandle.GetValue()
        ReturnValue2_4: float = 1 - ReturnValue1_10
        ReturnValue1_11: bool = NearlyEqual_FloatFloat(ReturnValue2_4, ReturnValue_12, ReturnValue_11)
        if not ReturnValue1_11:
            goto('L474')
        goto('L982')
        # Label 2696
        if not self.ShowButton:
            goto('L2756')
        ReturnValue1_12: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.PushButtonAnim, 0, 1, 1, 1)
        # Label 2756
        ReturnValue3_1: float = self.SelectionNormalizedSize / 2
        ReturnValue2_5: float = self.GetSliderMaxClamp()
        ReturnValue3_2: float = self.LeverHandle.GetValue()
        ReturnValue6: float = 1 - ReturnValue3_2
        ReturnValue3_3: bool = NearlyEqual_FloatFloat(ReturnValue6, ReturnValue2_5, ReturnValue3_1)
        if not ReturnValue3_3:
            goto('L3135')
        self.LeverShake(self.mMaxSelectionIndex)
        ReturnValue1_13: int32 = self.CurrentSelectionIndex + 1
        ReturnValue2_6: int32 = Clamp(ReturnValue1_13, self.mMinSelectionIndex, self.mMaxSelectionIndex)
        self.CurrentSelectionIndex = ReturnValue2_6
        goto('L1010')
        # Label 3135
        ReturnValue1_14: float = self.GetSliderMinClamp()
        ReturnValue2_7: float = self.LeverHandle.GetValue()
        ReturnValue4: float = 1 - ReturnValue2_7
        ReturnValue5_0: float = self.SelectionNormalizedSize / 2
        ReturnValue2_8: bool = NearlyEqual_FloatFloat(ReturnValue4, ReturnValue1_14, ReturnValue5_0)
        if not ReturnValue2_8:
            goto('L3514')
        self.LeverShake(self.mMinSelectionIndex)
        ReturnValue_13: int32 = self.CurrentSelectionIndex - 1
        ReturnValue3_4: int32 = Clamp(ReturnValue_13, self.mMinSelectionIndex, self.mMaxSelectionIndex)
        self.CurrentSelectionIndex = ReturnValue3_4
        goto('L1010')
        # Label 3514
        goto('L1010')
        goto('L2696')
        # Label 3524
        ReturnValue_14: float = self.GetCurrentSelectionPosOnSlider()
        self.SetHandle(ReturnValue_14)
        goto(ExecutionFlow.Pop())
        # Label 3580
        ReturnValue_14 = self.GetCurrentSelectionPosOnSlider()
        self.LeverHandle.SetValue(ReturnValue_14)
        goto('L3524')
        # Label 3658
        self.OnNewSelection.ProcessMulticastDelegate(self.CurrentSelectionIndex)
        goto(ExecutionFlow.Pop())
        # Label 3687
        self.LatestSelectionIndex = self.CurrentSelectionIndex
        
        Default__KismetSystemLibrary.K2_ClearAndInvalidateTimerHandle(self, Ref[self.LerpHandle])
        if not self.mUseCutomSounds:
            goto('L3658')
        ReturnValue_15: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_16: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(self.mCustomAKSound, ReturnValue_15, True)
        goto('L3658')
        # Label 3860
        ReturnValue_17: bool = self.CurrentSelectionIndex != self.LatestSelectionIndex
        if not ReturnValue_17:
           goto(ExecutionFlow.Pop())
        goto('L3687')
        ReturnValue2_9: bool = self.LerpT <= 1
        if not ReturnValue2_9:
            goto('L3860')
        ReturnValue4_0: float = self.mLerpDelta / self.LerpDuration
        ReturnValue_18: float = ReturnValue4_0 + self.LerpT
        self.LerpT = ReturnValue_18
        ReturnValue1_15: float = self.GetCurrentSelectionPosOnSlider()
        ReturnValue_19: float = Ease(self.LerpStartValue, ReturnValue1_15, self.LerpT, 5, 3, 2)
        self.LeverHandle.SetValue(ReturnValue_19)
        ReturnValue1_15 = self.GetCurrentSelectionPosOnSlider()
        ReturnValue_19 = Ease(self.LerpStartValue, ReturnValue1_15, self.LerpT, 5, 3, 2)
        self.SetHandle(ReturnValue_19)
        ReturnValue3_5: bool = self.LerpT <= 1
        if not ReturnValue3_5:
            goto('L3580')
        goto(ExecutionFlow.Pop())
        # Label 4391
        if not self.ShowButton:
           goto(ExecutionFlow.Pop())
        ReturnValue_20: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.PushButtonAnim, 0, 1, 0, 1)
        goto(ExecutionFlow.Pop())
        goto('L4391')
    

    def OnNewSelection__DelegateSignature(self, SelectionIndex: int32):
        pass
    
