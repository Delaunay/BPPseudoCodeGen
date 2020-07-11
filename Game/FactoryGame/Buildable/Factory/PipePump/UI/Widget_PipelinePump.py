
from codegen.ue4_stub import *

from Script.Engine import SetTextPropertyByName
from Script.Engine import K2_IsTimerActiveHandle
from Script.Engine import Conv_TextToString
from Script.Engine import K2_SetTimerDelegate
from Game.FactoryGame.Buildable.Factory.PipePump.UI.Widget_PipelinePump import ExecuteUbergraph_Widget_PipelinePump.K2Node_ComponentBoundEvent_Value1
from Script.Engine import Not_PreBool
from Script.Engine import Default__KismetSystemLibrary
from Script.FactoryGame import SetFlowLimit
from Script.Engine import PlayerController
from Script.FactoryGame import GetIndicatorHeadLift
from Script.FactoryGame import GetDesignHeadLift
from Script.UMG import ESlateVisibility
from Script.FactoryGame import FGBuildablePipelinePump
from Script.Engine import Conv_FloatToText
from Script.Engine import TimerHandle
from Script.Engine import IsValid
from Game.FactoryGame.Interface.UI.InGame.Widget_Tooltip import Widget_Tooltip
from Script.UMG import Default__WidgetBlueprintLibrary
from Script.Engine import Default__KismetTextLibrary
from Game.FactoryGame.Buildable.Factory.PipePump.UI.Widget_PipelinePump import ExecuteUbergraph_Widget_PipelinePump.K2Node_ComponentBoundEvent_state
from Script.Engine import Conv_StringToText
from Script.FactoryGame import GetIndicatorFlow
from Script.Engine import BooleanOR
from Script.FactoryGame import GetMaxHeadLift
from Game.FactoryGame.Buildable.Factory.PipePump.UI.Widget_PipelinePump import ExecuteUbergraph_Widget_PipelinePump.K2Node_Event_UpdateTime
from Script.UMG import Widget
from Game.FactoryGame.Interface.UI.InGame.Widget_UseableBase import Widget_UseableBase
from Script.FactoryGame import Init
from Script.Engine import SelectString
from Script.Engine import Default__KismetStringLibrary
from Game.FactoryGame.Buildable.Factory.PipePump.UI.Widget_PipelinePump import ExecuteUbergraph_Widget_PipelinePump.K2Node_ComponentBoundEvent_Value
from Script.FactoryGame import SetMaxHeadLift
from Script.FactoryGame import GetFlowLimit
from Script.Engine import NearlyEqual_FloatFloat
from Script.UMG import Create
from Script.Engine import Abs
from Game.FactoryGame.Buildable.Factory.PipePump.UI.Widget_PipelinePump import ExecuteUbergraph_Widget_PipelinePump
from Script.Engine import K2_ClearAndInvalidateTimerHandle
from Script.Engine import Concat_StrStr

class Widget_PipelinePump(Widget_UseableBase):
    mFactory: Ptr[FGBuildablePipelinePump]
    mMaxRate: float = 10
    mMaxPressure: float = 50
    mHeadLiftWarning: bool
    mHeadLiftWarningTimer: TimerHandle
    mUseKeyboard = True
    mUseMouse = True
    mRestoreFocusWhenLost = True
    mInputToPassThrough = ['Use']
    mDesiredHorizontalAlignment = 2
    mDesiredVerticalAlignment = 2
    mCustomTickRate = 0.019999999552965164
    mCallCustomTickOnConstruct = True
    
    def GetHeadliftTooltip(self):
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_0: Ptr[Widget_Tooltip] = Default__WidgetBlueprintLibrary.Create(self, Widget_Tooltip, ReturnValue)
        Variable1: Const[FText] = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 105, 'Value': 'Displays how much higher up this pump is pushing the fluid.'}"
        
        Default__KismetSystemLibrary.SetTextPropertyByName(ReturnValue_0, "mDescriptionText", Ref[Variable1])
        Variable: Const[FText] = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 285, 'Value': 'Head Lift'}"
        
        Default__KismetSystemLibrary.SetTextPropertyByName(ReturnValue_0, "mTitleText", Ref[Variable])
        ReturnValue_1: Ptr[Widget] = ReturnValue_0
    

    def ActivateHeadLiftWarning(self):
        self.mHeadLiftWarning = True
        self.UpdateWarning()
    

    def UpdateWarning(self):
        Variable2: uint8 = 0
        Variable3: uint8 = 2
        ReturnValue1: bool = self.mFactory.HasPower()
        ReturnValue1_0: bool = Not_PreBool(ReturnValue1)
        Variable2_0: bool = ReturnValue1_0
        
        switch = {
            False: Variable3,
            True: Variable2
        }
        self.mFlowWarning.SetVisibility(switch.get(Variable2_0, None))
        Variable: uint8 = 0
        Variable1: uint8 = 2
        ReturnValue: bool = self.mFactory.HasPower()
        ReturnValue_0: bool = Not_PreBool(ReturnValue)
        ReturnValue_1: bool = BooleanOR(self.mHeadLiftWarning, ReturnValue_0)
        Variable1_0: bool = ReturnValue_1
        
        switch_0 = {
            False: Variable1,
            True: Variable
        }
        self.mHeadWarning.SetVisibility(switch_0.get(Variable1_0, None))
        Variable_0: FText = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 504, 'Value': 'HEADLIFT IS EXCEEDING RECOMMENDED LEVEL'}"
        Variable1_1: FText = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 601, 'Value': 'NO POWER'}"
        Variable_1: bool = self.mHeadLiftWarning
        
        switch_1 = {
            False: Variable1_1,
            True: Variable_0
        }
        self.mHeadWarning.SetText(switch_1.get(Variable_1, None))
    

    def SetStaticInfo(self):
        ReturnValue: float = self.mFactory.GetFlowLimit()
        ReturnValue_0: float = ReturnValue * 60
        ReturnValue1: FText = Default__KismetTextLibrary.Conv_FloatToText(ReturnValue_0, 0, False, True, 1, 324, 0, 0)
        self.mMaxFlowRateText.SetText(ReturnValue1)
        ReturnValue1_0: float = self.mFactory.GetDesignHeadLift()
        ReturnValue_1: FText = Default__KismetTextLibrary.Conv_FloatToText(ReturnValue1_0, 0, False, True, 1, 324, 0, 0)
        self.mRecMaxHeadLiftText.SetText(ReturnValue_1)
        ReturnValue_2: float = self.mFactory.GetMaxHeadLift()
        ReturnValue_3: float = self.mFactory.GetDesignHeadLift()
        ReturnValue_4: float = ReturnValue_3 / ReturnValue_2
        self.mHeadLiftGauge.SetDividerPosition(ReturnValue_4)
    

    def UpdateStats(self):
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(self.mFactory)
        if not ReturnValue:
            goto('L1279')
        ReturnValue_0: float = self.mFactory.GetFlowLimit()
        ReturnValue1: float = self.mFactory.GetIndicatorFlow()
        ReturnValue1_0: float = ReturnValue1 / ReturnValue_0
        self.mFlowRateGauge.UpdateGaugeValue(ReturnValue1_0)
        ReturnValue_1: float = self.mFactory.GetMaxHeadLift()
        ReturnValue2: float = self.mFactory.GetIndicatorHeadLift()
        ReturnValue_2: float = ReturnValue2 / ReturnValue_1
        self.mHeadLiftGauge.UpdateGaugeValue(ReturnValue_2)
        ReturnValue_3: float = self.mFactory.GetIndicatorFlow()
        ReturnValue_4: float = ReturnValue_3 * 60
        ReturnValue1_1: FText = Default__KismetTextLibrary.Conv_FloatToText(ReturnValue_4, 0, False, True, 1, 324, 0, 0)
        self.mFlowRateText.SetText(ReturnValue1_1)
        ReturnValue_5: float = self.mFactory.GetIndicatorHeadLift()
        ReturnValue_6: FText = Default__KismetTextLibrary.Conv_FloatToText(ReturnValue_5, 0, False, True, 1, 324, 1, 1)
        self.mHeadLiftText.SetText(ReturnValue_6)
        ReturnValue_7: float = self.mFactory.GetDesignHeadLift()
        ReturnValue1_2: float = self.mFactory.GetIndicatorHeadLift()
        ReturnValue_8: bool = ReturnValue1_2 > ReturnValue_7
        if not ReturnValue_8:
            goto('L1212')
        ReturnValue_9: bool = Default__KismetSystemLibrary.K2_IsTimerActiveHandle(self, self.mHeadLiftWarningTimer)
        ReturnValue_10: bool = Not_PreBool(ReturnValue_9)
        if not ReturnValue_10:
            goto('L1279')
        OutputDelegate.BindUFunction(self, ActivateHeadLiftWarning)
        ReturnValue_11: TimerHandle = Default__KismetSystemLibrary.K2_SetTimerDelegate(OutputDelegate, 2, False)
        self.mHeadLiftWarningTimer = ReturnValue_11
        # End
        
        # Label 1212
        Default__KismetSystemLibrary.K2_ClearAndInvalidateTimerHandle(self, Ref[self.mHeadLiftWarningTimer])
        self.mHeadLiftWarning = False
        self.UpdateWarning()
    

    def GetFlowText(self):
        ReturnValue: float = self.mFactory.GetIndicatorFlow()
        ReturnValue_0: float = ReturnValue * 60
        ReturnValue_1: float = Abs(ReturnValue_0)
        ReturnValue_2: FText = Default__KismetTextLibrary.Conv_FloatToText(ReturnValue_1, 0, False, True, 1, 324, 1, 1)
        
        ReturnValue_3: FString = Default__KismetTextLibrary.Conv_TextToString(Ref[ReturnValue_2])
        ReturnValue_4: FString = Default__KismetStringLibrary.Concat_StrStr(ReturnValue_3, " m³/min")
        ReturnValue_5: FText = Default__KismetTextLibrary.Conv_StringToText(ReturnValue_4)
        ReturnValue_6: FText = ReturnValue_5
    

    def GetBackPressureText(self):
        ReturnValue: float = self.mFactory.GetIndicatorHeadLift()
        ReturnValue_0: FText = Default__KismetTextLibrary.Conv_FloatToText(ReturnValue, 0, False, True, 1, 324, 1, 1)
        
        ReturnValue_1: FString = Default__KismetTextLibrary.Conv_TextToString(Ref[ReturnValue_0])
        ReturnValue_2: FString = Default__KismetStringLibrary.Concat_StrStr(ReturnValue_1, " m")
        ReturnValue_3: FText = Default__KismetTextLibrary.Conv_StringToText(ReturnValue_2)
        ReturnValue_4: FText = ReturnValue_3
    

    def GetPressureText(self):
        ReturnValue: float = self.mFactory.GetIndicatorHeadLift()
        ReturnValue_0: FText = Default__KismetTextLibrary.Conv_FloatToText(ReturnValue, 0, False, True, 1, 324, 1, 1)
        
        ReturnValue_1: FString = Default__KismetTextLibrary.Conv_TextToString(Ref[ReturnValue_0])
        ReturnValue_2: FString = Default__KismetStringLibrary.Concat_StrStr(ReturnValue_1, " m")
        ReturnValue_3: FText = Default__KismetTextLibrary.Conv_StringToText(ReturnValue_2)
        ReturnValue_4: FText = ReturnValue_3
    

    def GetFlowLimitText(self):
        ReturnValue: float = self.mFactory.GetFlowLimit()
        ReturnValue_0: float = ReturnValue * 60
        ReturnValue_1: FText = Default__KismetTextLibrary.Conv_FloatToText(ReturnValue_0, 0, False, True, 1, 324, 1, 1)
        ReturnValue_2: bool = NearlyEqual_FloatFloat(ReturnValue_0, 0, 9.999999974752427e-07)
        
        ReturnValue_3: FString = Default__KismetTextLibrary.Conv_TextToString(Ref[ReturnValue_1])
        ReturnValue_4: FString = Default__KismetStringLibrary.Concat_StrStr(ReturnValue_3, " m³/min")
        ReturnValue_5: FString = SelectString("∞", ReturnValue_4, ReturnValue_2)
        ReturnValue_6: FText = Default__KismetTextLibrary.Conv_StringToText(ReturnValue_5)
        ReturnValue_7: FText = ReturnValue_6
    

    def Init(self):
        self.ExecuteUbergraph_Widget_PipelinePump(29)
    

    def BndEvt__Widget_Window_DarkMode_K2Node_ComponentBoundEvent_0_OnClose__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_PipelinePump(223)
    

    def BndEvt__mRateSlider_K2Node_ComponentBoundEvent_1_OnFloatValueChangedEvent__DelegateSignature(self, Value: float):
        ExecuteUbergraph_Widget_PipelinePump.K2Node_ComponentBoundEvent_Value1 = Value #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_PipelinePump(242)
    

    def BndEvt__mPressureSlider_K2Node_ComponentBoundEvent_2_OnFloatValueChangedEvent__DelegateSignature(self, Value: float):
        ExecuteUbergraph_Widget_PipelinePump.K2Node_ComponentBoundEvent_Value = Value #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_PipelinePump(334)
    

    def OnCustomTick(self):
        ExecuteUbergraph_Widget_PipelinePump.K2Node_Event_UpdateTime = UpdateTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_PipelinePump(477)
    

    def BndEvt__mFactory_K2Node_ComponentBoundEvent_3_BuildingStateChanged__DelegateSignature(self, State: bool):
        ExecuteUbergraph_Widget_PipelinePump.K2Node_ComponentBoundEvent_state = State #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_PipelinePump(496)
    

    def ExecuteUbergraph_Widget_PipelinePump(self):
        # Label 10
        self.UpdateWarning()
        # End
        self.Init()
        Pump: Ptr[FGBuildablePipelinePump] = Cast[FGBuildablePipelinePump](self.mInteractObject)
        bSuccess: bool = Pump
        if not bSuccess:
            goto('L510')
        self.mFactory = Pump
        self.Widget_Window_DarkMode.SetTitle(self.mFactory.mDisplayName)
        self.SetStaticInfo()
        goto('L10')
        self.OnEscapePressed()
        # End
        ReturnValue: float = Value1 * self.mMaxRate
        self.mFactory.SetFlowLimit(ReturnValue)
        # End
        ReturnValue1: float = Value * self.mMaxPressure
        ReturnValue_0: float = ReturnValue1 + 2
        self.mFactory.SetMaxHeadLift(ReturnValue1, ReturnValue_0)
        # End
        self.UpdateStats()
        # End
        self.UpdateWarning()
    
