
from codegen.ue4_stub import *

from Script.Engine import K2_IsTimerActiveHandle
from Script.AkAudio import PostAkEvent
from Script.FactoryGame import GetFloatCurveValue
from Script.Engine import Lerp
from Script.Engine import FClamp
from Script.Engine import K2_SetTimerDelegate
from Script.Engine import Delay
from Game.FactoryGame.Buildable.Factory.Pipeline.UI.BPW_FlushHandle import ExecuteUbergraph_BPW_FlushHandle
from Script.Engine import Not_PreBool
from Game.FactoryGame.Buildable.Factory.Pipeline.UI.Curve_FlushHandle import Curve_FlushHandle
from Script.Engine import LatentActionInfo
from Script.Engine import Ease
from Script.Engine import Default__KismetSystemLibrary
from Script.AkAudio import SetSwitch
from Game.FactoryGame.Interface.UI.Audio.Play_UI_Pipeline_Handle import Play_UI_Pipeline_Handle
from Script.Engine import PlayerController
from Script.Engine import Array_Find
from Script.Engine import EqualEqual_FloatFloat
from Script.Engine import Default__KismetArrayLibrary
from Script.FactoryGame import GetItemName
from Script.Engine import TimerHandle
from Game.FactoryGame.Interface.UI.Audio.Play_UI_Pipeline_Flush import Play_UI_Pipeline_Flush
from Script.Engine import GreaterEqual_FloatFloat
from Script.UMG import SetValue
from Game.FactoryGame.Interface.UI.Audio.Play_UI_Pipeline_FlushSwitch import Play_UI_Pipeline_FlushSwitch
from Script.UMG import SetRenderAngle
from Script.Engine import RichCurve
from Script.Engine import RuntimeFloatCurve
from Script.FactoryGame import Default__FGSkySphere
from Script.AkAudio import Default__AkGameplayStatics
from Game.FactoryGame.Buildable.Factory.Pipeline.UI.BPW_FlushHandle import ExecuteUbergraph_BPW_FlushHandle.K2Node_ComponentBoundEvent_Value
from Script.UMG import UserWidget
from Script.FactoryGame import Default__FGItemDescriptor
from Script.FactoryGame import FGItemDescriptor
from Script.Engine import Abs
from Script.AkAudio import AkComponent
from Script.Engine import IsValidClass
from Script.Engine import K2_ClearAndInvalidateTimerHandle

class BPW_FlushHandle(UserWidget):
    mMinAngle: float
    mMaxAngle: float = 90
    mCurrentValue: float
    mLerpStart: float
    mLerpEnd: float
    mLerpT: float
    mLerpDuration: float = 0.20000000298023224
    mLerpUpdate: float = 0.009999999776482582
    mLerpTimer: TimerHandle
    OnFlush: FMulticastScriptDelegate
    mFullFlush: bool
    mThreshold: float = 0.800000011920929
    mInteractable: bool = True
    mHasMouseCapture: bool
    OnFlushCompleted: FMulticastScriptDelegate
    mFlushDuration: float = 0.75
    mFlushSpeed: float = 1
    mOldValue: float
    mFlushLerp: bool
    mFluidLerpDuration: float
    mFluidLerpTimer: TimerHandle
    mFluidLerpT: float
    OnFluidLerp: FMulticastScriptDelegate
    mFluidFillingUp: bool
    OnFluidFilledUp: FMulticastScriptDelegate
    mFluidDescriptor: TSubclassOf[FGItemDescriptor]
    mFluidDrainDuration: float = 6
    mWWiseNameConverter: List[FText] = ['NSLOCTEXT("", "6CA8BF5D4E20C2554CAE2D95DD3069F9", "Crude Oil")', 'NSLOCTEXT("", "195E9F44440EC34C2C30189D8747C252", "Fuel")', 'NSLOCTEXT("", "3708C00F4631BCEB92EF33BAEB54049B", "Heavy Oil Residue")', 'NSLOCTEXT("", "8658AC8A4F3946D61694229DF7579106", "Water")', 'NSLOCTEXT("", "2468D41B451AC81F3A5245891302192B", "N/A")']
    OnDrainCompleted: FMulticastScriptDelegate
    
    def StartFluidLerp(self, Duration: float):
        self.mFluidLerpDuration = Duration
        
        Default__KismetSystemLibrary.K2_ClearAndInvalidateTimerHandle(self, Ref[self.mFluidLerpTimer])
        self.mFluidLerpT = 0
        self.mFluidFillingUp = False
        OutputDelegate.BindUFunction(self, LerpFluid)
        ReturnValue: TimerHandle = Default__KismetSystemLibrary.K2_SetTimerDelegate(OutputDelegate, self.mLerpUpdate, True)
        self.mFluidLerpTimer = ReturnValue
    

    def PlayHandleNoise(self, Speed: float):
        FastSpeed = 0
        MediumSpeed = 0.03999999910593033
        SlowSpeed = 0.02500000037252903
        ReturnValue1: bool = Speed > SlowSpeed
        if not ReturnValue1:
            goto('L354')
        ReturnValue: bool = Speed > MediumSpeed
        if not ReturnValue:
            goto('L535')
        ReturnValue1_0: Ptr[PlayerController] = self.GetOwningPlayer()
        Default__AkGameplayStatics.SetSwitch("Pipeline_FlushHandle", "fast", ReturnValue1_0)
        ReturnValue1_0 = self.GetOwningPlayer()
        ReturnValue1_1: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_UI_Pipeline_Handle, ReturnValue1_0, True)
        # End
        # Label 354
        ReturnValue2: Ptr[PlayerController] = self.GetOwningPlayer()
        Default__AkGameplayStatics.SetSwitch("Pipeline_FlushHandle", "Slow", ReturnValue2)
        ReturnValue2 = self.GetOwningPlayer()
        ReturnValue2_0: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_UI_Pipeline_Handle, ReturnValue2, True)
        # End
        # Label 535
        ReturnValue_0: Ptr[PlayerController] = self.GetOwningPlayer()
        Default__AkGameplayStatics.SetSwitch("Pipeline_FlushHandle", "Medium", ReturnValue_0)
        ReturnValue_0 = self.GetOwningPlayer()
        ReturnValue_1: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_UI_Pipeline_Handle, ReturnValue_0, True)
    

    def StartLerp(self, EndValue: float, FullFlush: bool):
        self.mLerpEnd = EndValue
        self.mFullFlush = FullFlush
        self.mLerpStart = self.mCurrentValue
        
        Default__KismetSystemLibrary.K2_ClearAndInvalidateTimerHandle(self, Ref[self.mLerpTimer])
        self.mLerpT = 0
        OutputDelegate.BindUFunction(self, LerpHandle)
        ReturnValue: TimerHandle = Default__KismetSystemLibrary.K2_SetTimerDelegate(OutputDelegate, self.mLerpUpdate, True)
        self.mLerpTimer = ReturnValue
    

    def RotateHandle(self, amount: float):
        FlushHandleCurve = RuntimeFloatCurve(EditorCurveData = RichCurve(Keys = List[StructProperty /Script/Engine.RichCurve:Keys.Keys]([]), PreInfinityExtrap = 4, PostInfinityExtrap = 4, DefaultValue = 3.4028234663852886e+38), ExternalCurve = Curve_FlushHandle)
        ReturnValue: float = Ease(0, 1, amount, 7, 2, 2)
        Variable: bool = self.mFullFlush
        
        ReturnValue_0: float = Default__FGSkySphere.GetFloatCurveValue(amount, Ref[FlushHandleCurve])
        ReturnValue_1: float = self.mMaxAngle * -1
        
        switch = {
            False: ReturnValue_0,
            True: ReturnValue
        }
        ReturnValue_2: float = Lerp(self.mMinAngle, ReturnValue_1, switch.get(Variable, None))
        self.mHandleBottom.SetRenderAngle(ReturnValue_2)
        self.mHandleHighlight.SetRenderAngle(ReturnValue_2)
        self.mHandleTop.SetRenderAngle(ReturnValue_2)
        self.mHandleShadow.SetRenderAngle(ReturnValue_2)
    

    def BndEvt__Slider_28_K2Node_ComponentBoundEvent_0_OnFloatValueChangedEvent__DelegateSignature(self, Value: float):
        ExecuteUbergraph_BPW_FlushHandle.K2Node_ComponentBoundEvent_Value = Value #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BPW_FlushHandle(1484)
    

    def BndEvt__Slider_28_K2Node_ComponentBoundEvent_1_OnMouseCaptureEndEvent__DelegateSignature(self):
        self.ExecuteUbergraph_BPW_FlushHandle(1516)
    

    def LerpHandle(self):
        self.ExecuteUbergraph_BPW_FlushHandle(1738)
    

    def BndEvt__mSlider_K2Node_ComponentBoundEvent_2_OnMouseCaptureBeginEvent__DelegateSignature(self):
        self.ExecuteUbergraph_BPW_FlushHandle(2339)
    

    def ResetFlush(self):
        self.ExecuteUbergraph_BPW_FlushHandle(2374)
    

    def LerpFluid(self):
        self.ExecuteUbergraph_BPW_FlushHandle(2397)
    

    def ExecuteUbergraph_BPW_FlushHandle(self):
        goto(ComputedJump("EntryPoint"))
        self.StartLerp(0, True)
        self.OnFlushCompleted.ProcessMulticastDelegate()
        goto(ExecutionFlow.Pop())
        # Label 55
        self.OnFlush.ProcessMulticastDelegate(self.mFluidDrainDuration)
        self.mInteractable = False
        self.StartFluidLerp(self.mFluidDrainDuration)
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_0: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_UI_Pipeline_FlushSwitch, ReturnValue, True)
        ReturnValue_1: bool = Default__KismetSystemLibrary.IsValidClass(self.mFluidDescriptor)
        if not ReturnValue_1:
           goto(ExecutionFlow.Pop())
        ReturnValue_2: FText = Default__FGItemDescriptor.GetItemName(self.mFluidDescriptor)
        Variable: FName = "No_Fluid"
        Variable1: FName = "Water"
        Variable2: FName = "Heavy_Oil_Residue"
        Variable3: FName = "Fuel"
        Variable4: FName = "Crude_Oil"
        ReturnValue1: Ptr[PlayerController] = self.GetOwningPlayer()
        
        ReturnValue_3: int32 = Default__KismetArrayLibrary.Array_Find(Ref[self.mWWiseNameConverter], Ref[ReturnValue_2])
        Variable_0: int32 = ReturnValue_3
        
        switch = {
            0: Variable4,
            1: Variable3,
            2: Variable2,
            3: Variable1,
            4: Variable
        }
        Default__AkGameplayStatics.SetSwitch("Pipeline_Flush_Type", switch.get(Variable_0, None), ReturnValue1)
        ReturnValue1 = self.GetOwningPlayer()
        ReturnValue1_0: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_UI_Pipeline_Flush, ReturnValue1, True)
        goto(ExecutionFlow.Pop())
        # Label 851
        ExecutionFlow.Push("L871")
        if not Variable_1:
            goto('L945')
        goto(ExecutionFlow.Pop())
        # Label 871
        if not Variable_1:
            goto('L886')
        goto(ExecutionFlow.Pop())
        # Label 886
        Variable_1: bool = True
        self.StartLerp(1, False)
        self.mCurrentValue = 1
        goto('L55')
        # Label 945
        Variable_1 = True
        if not False:
           goto(ExecutionFlow.Pop())
        Variable_1 = True
        goto(ExecutionFlow.Pop())
        # Label 970
        ExecutionFlow.Push("L1076")
        ReturnValue2: bool = self.mCurrentValue > 0.30000001192092896
        if not ReturnValue2:
            goto('L1038')
        if not Variable2_0:
            goto('L1438')
        goto(ExecutionFlow.Pop())
        # Label 1038
        Variable2_0: bool = False
        if not Variable3_0:
            goto('L1064')
        goto(ExecutionFlow.Pop())
        # Label 1064
        Variable3_0: bool = True
        goto(ExecutionFlow.Pop())
        # Label 1076
        ReturnValue_4: float = FClamp(Value, 0, 1)
        self.mCurrentValue = ReturnValue_4
        ReturnValue_5: float = self.mCurrentValue - self.mOldValue
        ReturnValue_6: float = Abs(ReturnValue_5)
        ReturnValue_7: float = 0.30000001192092896 * ReturnValue_6 + 1 - 0.30000001192092896 * self.mFlushSpeed
        self.mFlushSpeed = ReturnValue_7
        self.mFullFlush = False
        self.RotateHandle(self.mCurrentValue)
        ReturnValue1_1: bool = self.mCurrentValue > self.mThreshold
        if not ReturnValue1_1:
           goto(ExecutionFlow.Pop())
        goto('L851')
        # Label 1438
        Variable2_0 = True
        Variable3_0 = False
        self.PlayHandleNoise(self.mFlushSpeed)
        goto(ExecutionFlow.Pop())
        self.mOldValue = self.mCurrentValue
        goto('L970')
        self.mHasMouseCapture = False
        self.mSlider.SetValue(0)
        ReturnValue_8: bool = self.mCurrentValue > self.mThreshold
        if not ReturnValue_8:
            goto('L1717')
        ReturnValue_9: bool = Default__KismetSystemLibrary.K2_IsTimerActiveHandle(self, self.mLerpTimer)
        ReturnValue_10: bool = Not_PreBool(ReturnValue_9)
        self.mInteractable = ReturnValue_10
        goto(ExecutionFlow.Pop())
        # Label 1717
        self.StartLerp(0, False)
        goto(ExecutionFlow.Pop())
        Variable_2: float = 0.5
        Variable_3: bool = self.mFullFlush
        
        switch_0 = {
            False: self.mLerpDuration,
            True: Variable_2
        }
        ReturnValue_11: float = self.mLerpUpdate / switch_0.get(Variable_3, None)
        ReturnValue_12: float = ReturnValue_11 + self.mLerpT
        self.mLerpT = ReturnValue_12
        ReturnValue_13: float = Lerp(self.mLerpStart, self.mLerpEnd, self.mLerpT)
        self.RotateHandle(ReturnValue_13)
        ReturnValue_14: bool = GreaterEqual_FloatFloat(self.mLerpT, 1)
        if not ReturnValue_14:
           goto(ExecutionFlow.Pop())
        ReturnValue_15: bool = EqualEqual_FloatFloat(self.mLerpEnd, 0)
        if not ReturnValue_15:
            goto('L2258')
        
        Default__KismetSystemLibrary.K2_ClearAndInvalidateTimerHandle(self, Ref[self.mLerpTimer])
        self.ResetFlush()
        ReturnValue1_2: bool = Not_PreBool(self.mHasMouseCapture)
        ReturnValue_16: bool = self.mFullFlush and ReturnValue1_2
        if not ReturnValue_16:
           goto(ExecutionFlow.Pop())
        self.mInteractable = True
        goto(ExecutionFlow.Pop())
        # Label 2258
        Default__KismetSystemLibrary.Delay(self, self.mFlushDuration, LatentActionInfo(Linkage = 15, UUID = -2056763286, ExecutionFunction = "ExecuteUbergraph_BPW_FlushHandle", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        self.mHasMouseCapture = True
        self.mFlushSpeed = 0
        goto(ExecutionFlow.Pop())
        Variable_1 = False
        Variable_1 = True
        goto(ExecutionFlow.Pop())
        ReturnValue1_3: float = self.mLerpUpdate / self.mFluidLerpDuration
        ReturnValue1_4: float = self.mFluidLerpT + ReturnValue1_3
        self.mFluidLerpT = ReturnValue1_4
        Variable1_0: bool = self.mFluidFillingUp
        ReturnValue2_0: float = 1 - self.mFluidLerpT
        
        switch_1 = {
            False: self.mFluidLerpT,
            True: ReturnValue2_0
        }
        ReturnValue1_5: float = FClamp(switch_1.get(Variable1_0, None), 0, 1)
        self.OnFluidLerp.ProcessMulticastDelegate(ReturnValue1_5)
        ReturnValue1_6: bool = GreaterEqual_FloatFloat(self.mFluidLerpT, 1)
        if not ReturnValue1_6:
           goto(ExecutionFlow.Pop())
        if not self.mFluidFillingUp:
            goto('L2816')
        
        Default__KismetSystemLibrary.K2_ClearAndInvalidateTimerHandle(self, Ref[self.mFluidLerpTimer])
        self.OnFluidFilledUp.ProcessMulticastDelegate()
        goto(ExecutionFlow.Pop())
        # Label 2816
        self.mFluidLerpT = 0
        self.mFluidFillingUp = True
        self.OnDrainCompleted.ProcessMulticastDelegate()
        goto(ExecutionFlow.Pop())
    

    def OnDrainCompleted__DelegateSignature(self):
        pass
    

    def OnFluidFilledUp__DelegateSignature(self):
        pass
    

    def OnFluidLerp__DelegateSignature(self, Alpha: float):
        pass
    

    def OnFlushCompleted__DelegateSignature(self):
        pass
    

    def OnFlush__DelegateSignature(self, DrainDuration: float):
        pass
    
