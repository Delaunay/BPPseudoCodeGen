
from codegen.ue4_stub import *

from Script.FactoryGame import GetMaxNumConnections
from Script.Engine import Delay
from Script.Engine import K2_SetTimerDelegate
from Game.FactoryGame.Buildable.Factory.-Shared.Widget_PoleConnections import ExecuteUbergraph_Widget_PoleConnections.K2Node_Event_IsDesignTime
from Script.Engine import GetComponentByClass
from Script.UMG import SetPadding
from Script.Slate import ETextJustify
from Script.UMG import OverlaySlot
from Script.Engine import GreaterEqual_IntInt
from Script.UMG import GetChildrenCount
from Script.UMG import Default__WidgetLayoutLibrary
from Script.UMG import SetJustification
from Script.UMG import PanelSlot
from Script.FactoryGame import GetNumConnections
from Script.UMG import SlotAsOverlaySlot
from Script.UMG import AddChild
from Script.Engine import Not_PreBool
from Script.Engine import LatentActionInfo
from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import PlayerController
from Script.UMG import GetChildAt
from Script.Engine import FormatArgumentData
from Script.UMG import PlayAnimation
from Script.UMG import ESlateVisibility
from Game.FactoryGame.Buildable.Factory.-Shared.Widget_PoleConnections import ExecuteUbergraph_Widget_PoleConnections
from Script.Engine import TimerHandle
from Script.UMG import StopAnimation
from Script.Engine import IsValid
from Script.UMG import Default__WidgetBlueprintLibrary
from Script.UMG import SetColorAndOpacity
from Script.Engine import EqualEqual_IntInt
from Script.Engine import Default__KismetTextLibrary
from Script.UMG import Widget
from Script.FactoryGame import FGPowerConnectionComponent
from Script.Engine import Format
from Script.UMG import WidgetAnimation
from Script.UMG import UserWidget
from Game.FactoryGame.Interface.UI.HUDHelpers.HUDHelpers import Default__HUDHelpers
from Script.FactoryGame import FGBuildablePowerPole
from Script.UMG import UMGSequencePlayer
from Script.UMG import Create
from Script.UMG import IsAnimationPlaying
from Script.SlateCore import SlateColor
from Game.FactoryGame.Buildable.Factory.-Shared.Widget_PoleConnections_Dot import Widget_PoleConnections_Dot
from Script.Engine import K2_ClearAndInvalidateTimerHandle
from Script.Engine import PrintString
from Script.CoreUObject import LinearColor

class Widget_PoleConnections(UserWidget):
    FullAnim: Ptr[WidgetAnimation]
    SpawnAnim: Ptr[WidgetAnimation]
    PowerPoleDataModel: Ptr[FGBuildablePowerPole]
    mMaxConnections: int32
    mCurrentConnections: int32
    UpdateTimer: TimerHandle
    mLastCurrentConnections: int32
    mUseBackground: bool = True
    
    def SetStyle(self, UseBackground: bool):
        self.mUseBackground = UseBackground
        Variable2: uint8 = 3
        # Label 39
        Variable3: uint8 = 1
        Variable2_0: bool = self.mUseBackground
        
        switch = {
            False: Variable3,
            True: Variable2
        }
        self.mBoxBackground.SetVisibility(switch.get(Variable2_0, None))
        Margin.Left = 20
        Margin.Top = 10
        Margin.Right = 20
        Margin.Bottom = 10
        Margin1.Left = 0
        Margin1.Top = 0
        Margin1.Right = 0
        Margin1.Bottom = 0
        Variable1: bool = self.mUseBackground
        ReturnValue: Ptr[OverlaySlot] = Default__WidgetLayoutLibrary.SlotAsOverlaySlot(self.mInfoContainer)
        
        switch_0 = {
            False: Margin1,
            True: Margin
        }
        ReturnValue.SetPadding(switch_0.get(Variable1, None))
        Variable: uint8 = 1
        Variable1_0: uint8 = 0
        Variable_0: bool = self.mUseBackground
        
        switch_1 = {
            False: Variable1_0,
            True: Variable
        }
        self.mConnectionText.SetJustification(switch_1.get(Variable_0, None))
    

    def GetColorAndOpacity_0(self):
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(self.PowerPoleDataModel)
        if not ReturnValue:
            goto('L506')
        ReturnValue_0: Ptr[FGPowerConnectionComponent] = self.PowerPoleDataModel.GetComponentByClass(FGPowerConnectionComponent)
        ReturnValue1: bool = Default__KismetSystemLibrary.IsValid(ReturnValue_0)
        if not ReturnValue1:
            goto('L506')
        ReturnValue_0 = self.PowerPoleDataModel.GetComponentByClass(FGPowerConnectionComponent)
        ReturnValue_1: int32 = ReturnValue_0.GetMaxNumConnections()
        ReturnValue_2: int32 = ReturnValue_0.GetNumConnections()
        ReturnValue_3: bool = GreaterEqual_IntInt(ReturnValue_2, ReturnValue_1)
        if not ReturnValue_3:
            goto('L506')
        SlateColor1.SpecifiedColor = LinearColor(R = 0.7835379838943481, G = 0.2917709946632385, B = 0.05951099842786789, A = 1)
        SlateColor1.ColorUseRule = 0
        ReturnValue_4: SlateColor = SlateColor1
        goto('L623')
        # Label 506
        SlateColor.SpecifiedColor = LinearColor(R = 1, G = 1, B = 1, A = 1)
        SlateColor.ColorUseRule = 0
        ReturnValue_4 = SlateColor
    

    def GetText_0(self):
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(self.PowerPoleDataModel)
        if not ReturnValue:
            goto('L879')
        ReturnValue_0: Ptr[FGPowerConnectionComponent] = self.PowerPoleDataModel.GetComponentByClass(FGPowerConnectionComponent)
        ReturnValue1: bool = Default__KismetSystemLibrary.IsValid(ReturnValue_0)
        if not ReturnValue1:
            goto('L879')
        ReturnValue_0 = self.PowerPoleDataModel.GetComponentByClass(FGPowerConnectionComponent)
        ReturnValue_1: int32 = ReturnValue_0.GetMaxNumConnections()
        ReturnValue_2: int32 = ReturnValue_0.GetNumConnections()
        FormatArgumentData.ArgumentName = "Max"
        FormatArgumentData.ArgumentValueType = 0
        FormatArgumentData.ArgumentValue = 
        FormatArgumentData.ArgumentValueInt = ReturnValue_1
        FormatArgumentData.ArgumentValueFloat = 0
        FormatArgumentData.ArgumentValueGender = 0
        FormatArgumentData1.ArgumentName = "Free"
        FormatArgumentData1.ArgumentValueType = 0
        FormatArgumentData1.ArgumentValue = 
        FormatArgumentData1.ArgumentValueInt = ReturnValue_2
        FormatArgumentData1.ArgumentValueFloat = 0
        FormatArgumentData1.ArgumentValueGender = 0
        Array: List[FormatArgumentData] = [FormatArgumentData1, FormatArgumentData]
        ReturnValue_3: FText = Default__KismetTextLibrary.Format("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 787, 'Value': '{Free}/{Max}'}", Array)
        ReturnValue_4: FText = ReturnValue_3
        goto('L940')
        # Label 879
        ReturnValue_4 = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 899, 'Value': 'N/A'}"
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_PoleConnections(1903)
    

    def UpdateConnections(self):
        self.ExecuteUbergraph_Widget_PoleConnections(1908)
    

    def Destruct(self):
        self.ExecuteUbergraph_Widget_PoleConnections(2392)
    

    def PreConstruct(self):
        ExecuteUbergraph_Widget_PoleConnections.K2Node_Event_IsDesignTime = IsDesignTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_PoleConnections(15)
    

    def ExecuteUbergraph_Widget_PoleConnections(self):
        goto(ComputedJump("EntryPoint"))
        self.SetStyle(self.mUseBackground)
        goto(ExecutionFlow.Pop())
        # Label 39
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(self.PowerPoleDataModel)
        if not ReturnValue:
            goto('L771')
        ReturnValue_0: Ptr[FGPowerConnectionComponent] = self.PowerPoleDataModel.GetComponentByClass(FGPowerConnectionComponent)
        ReturnValue1: bool = Default__KismetSystemLibrary.IsValid(ReturnValue_0)
        if not ReturnValue1:
            goto('L771')
        ReturnValue_0 = self.PowerPoleDataModel.GetComponentByClass(FGPowerConnectionComponent)
        ReturnValue_1: int32 = ReturnValue_0.GetNumConnections()
        self.mCurrentConnections = ReturnValue_1
        ReturnValue_0 = self.PowerPoleDataModel.GetComponentByClass(FGPowerConnectionComponent)
        ReturnValue_2: int32 = ReturnValue_0.GetMaxNumConnections()
        self.mMaxConnections = ReturnValue_2
        self.mDotConatiner.ClearChildren()
        Variable: int32 = 0
        # Label 535
        ReturnValue_3: int32 = self.mMaxConnections - 1
        ReturnValue_4: bool = Variable <= ReturnValue_3
        if not ReturnValue_4:
            goto('L848')
        ExecutionFlow.Push("L1038")
        ReturnValue_5: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_6: Ptr[Widget_PoleConnections_Dot] = Default__WidgetBlueprintLibrary.Create(self, Widget_PoleConnections_Dot, ReturnValue_5)
        ReturnValue_7: Ptr[PanelSlot] = self.mDotConatiner.AddChild(ReturnValue_6)
        goto(ExecutionFlow.Pop())
        # Label 771
        Default__KismetSystemLibrary.Delay(self, 0.10000000149011612, LatentActionInfo(Linkage = 39, UUID = -430492542, ExecutionFunction = "ExecuteUbergraph_Widget_PoleConnections", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        # Label 848
        self.UpdateConnections()
        if not self.mUseBackground:
            goto('L922')
        ReturnValue_8: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.SpawnAnim, 0, 1, 0, 1)
        # Label 922
        OutputDelegate.BindUFunction(self, UpdateConnections)
        ReturnValue_9: TimerHandle = Default__KismetSystemLibrary.K2_SetTimerDelegate(OutputDelegate, 0.10000000149011612, True)
        self.UpdateTimer = ReturnValue_9
        goto(ExecutionFlow.Pop())
        # Label 1038
        ReturnValue_10: int32 = Variable + 1
        Variable = ReturnValue_10
        goto('L535')
        # Label 1112
        ExecutionFlow.Push("L1459")
        ReturnValue_11: Ptr[Widget] = self.mDotConatiner.GetChildAt(Variable1)
        Dot: Ptr[Widget_PoleConnections_Dot] = Cast[Widget_PoleConnections_Dot](ReturnValue_11)
        bSuccess: bool = Dot
        if not bSuccess:
           goto(ExecutionFlow.Pop())
        ReturnValue_12: bool = Variable1 <= self.mCurrentConnections
        if not ReturnValue_12:
            goto('L1392')
        
        Orange = None
        OrangeText = None
        Default__HUDHelpers.GetFactoryGameOrange(self, Ref[Orange], Ref[OrangeText])
        Dot.SetColorAndOpacity(Orange)
        goto(ExecutionFlow.Pop())
        # Label 1392
        Dot.SetColorAndOpacity(LinearColor(R = 1, G = 1, B = 1, A = 1))
        goto(ExecutionFlow.Pop())
        # Label 1459
        ReturnValue1_0: int32 = Variable1 + 1
        Variable1: int32 = ReturnValue1_0
        # Label 1528
        ReturnValue_13: int32 = self.mDotConatiner.GetChildrenCount()
        ReturnValue1_1: bool = Variable1 <= ReturnValue_13
        if not ReturnValue1_1:
            goto('L1635')
        goto('L1112')
        # Label 1635
        ReturnValue_14: bool = EqualEqual_IntInt(self.mCurrentConnections, self.mMaxConnections)
        if not ReturnValue_14:
            goto('L1883')
        ReturnValue_15: bool = self.IsAnimationPlaying(self.FullAnim)
        ReturnValue_16: bool = Not_PreBool(ReturnValue_15)
        if not ReturnValue_16:
           goto(ExecutionFlow.Pop())
        Default__KismetSystemLibrary.PrintString(self, "Hello", True, True, LinearColor(R = 0, G = 0.6600000262260437, B = 1, A = 1), 2)
        ReturnValue1_2: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.FullAnim, 0, 0, 0, 1)
        goto(ExecutionFlow.Pop())
        # Label 1883
        self.StopAnimation(self.FullAnim)
        goto(ExecutionFlow.Pop())
        goto('L39')
        ReturnValue2: bool = Default__KismetSystemLibrary.IsValid(self.PowerPoleDataModel)
        if not ReturnValue2:
           goto(ExecutionFlow.Pop())
        ReturnValue1_3: Ptr[FGPowerConnectionComponent] = self.PowerPoleDataModel.GetComponentByClass(FGPowerConnectionComponent)
        ReturnValue3: bool = Default__KismetSystemLibrary.IsValid(ReturnValue1_3)
        if not ReturnValue3:
           goto(ExecutionFlow.Pop())
        ReturnValue1_3 = self.PowerPoleDataModel.GetComponentByClass(FGPowerConnectionComponent)
        ReturnValue1_4: int32 = ReturnValue1_3.GetNumConnections()
        self.mCurrentConnections = ReturnValue1_4
        ReturnValue1_3 = self.PowerPoleDataModel.GetComponentByClass(FGPowerConnectionComponent)
        ReturnValue1_5: int32 = ReturnValue1_3.GetMaxNumConnections()
        self.mMaxConnections = ReturnValue1_5
        self.mLastCurrentConnections = self.mCurrentConnections
        Variable1 = 0
        goto('L1528')
        
        Default__KismetSystemLibrary.K2_ClearAndInvalidateTimerHandle(self, Ref[self.UpdateTimer])
        goto(ExecutionFlow.Pop())
    
