
from codegen.ue4_stub import *

from Script.Engine import Texture2D
from Script.FactoryGame import GetActiveSchematic
from Script.Engine import K2_SetTimerDelegate
from Script.FactoryGame import GetOngoingResearchTimeLeft
from Script.Engine import FromSeconds
from Game.FactoryGame.Interface.UI.InGame.ActorDetails.Widget_ActorDetails_Parent import Widget_ActorDetails_Parent
from Script.FactoryGame import GetCost
from Script.UMG import PanelSlot
from Script.UMG import AddChild
from Game.FactoryGame.Interface.UI.InGame.ActorDetails.Widget_ActorDetails_Hub import ExecuteUbergraph_Widget_ActorDetails_Hub
from Script.CoreUObject import Timespan
from Script.Engine import Default__KismetSystemLibrary
from Script.FactoryGame import Default__FGResearchManager
from Script.Engine import PlayerController
from Script.FactoryGame import Get
from Script.Engine import Default__KismetArrayLibrary
from Script.Engine import GameStateBase
from Script.Engine import FormatArgumentData
from Script.Engine import TimerHandle
from Game.FactoryGame.Interface.UI.InGame.Widget_CostSlotWrapper import Widget_CostSlotWrapper
from Script.FactoryGame import IsAnyResearchBeingConducted
from Script.Engine import Conv_IntToText
from Script.UMG import Default__WidgetBlueprintLibrary
from Script.Engine import Default__KismetTextLibrary
from Script.FactoryGame import GetSmallIcon
from Script.Engine import Default__GameplayStatics
from Script.FactoryGame import FGGameState
from Script.Engine import BreakTimespan
from Script.FactoryGame import GetPaidOffCostFor
from Script.Engine import Format
from Script.FactoryGame import FGResearchManager
from Script.FactoryGame import GetTimeUntilShipReturn
from Script.FactoryGame import FGBuildableTradingPost
from Script.FactoryGame import FGSchematic
from Script.Engine import K2_ClearAndInvalidateTimerHandle
from Script.FactoryGame import IsShipAtTradingPost
from Script.FactoryGame import FGSchematicManager
from Script.UMG import Create
from Script.FactoryGame import Default__FGSchematic
from Script.Engine import GetGameState
from Script.FactoryGame import Default__FGItemDescriptor
from Game.FactoryGame.Interface.UI.InGame.ActorDetails.Widget_ActorDetails_Parent import Construct
from Script.FactoryGame import ItemAmount
from Script.Engine import IsValidClass
from Script.FactoryGame import Default__FGSchematicManager
from Script.FactoryGame import GetSchematicDisplayName
from Script.FactoryGame import GetResearchBeingConducted

class Widget_ActorDetails_Hub(Widget_ActorDetails_Parent):
    mSchematicManager: Ptr[FGSchematicManager]
    mTradingPost: Ptr[FGBuildableTradingPost]
    UpdateInfoTimer: TimerHandle
    MamInfoTimer: TimerHandle
    
    def FromSecondsToText(self, Seconds: float):
        ReturnValue: Timespan = FromSeconds(Seconds)
        
        Days = None
        Hours = None
        Minutes = None
        Seconds_0 = None
        Milliseconds = None
        BreakTimespan(ReturnValue, Ref[Days], Ref[Hours], Ref[Minutes], Ref[Seconds_0], Ref[Milliseconds])
        ReturnValue_0: int32 = Days * 24
        ReturnValue_1: FText = Default__KismetTextLibrary.Conv_IntToText(Seconds_0, False, True, 2, 324)
        ReturnValue_2: int32 = ReturnValue_0 + Hours
        FormatArgumentData.ArgumentName = "sec"
        FormatArgumentData.ArgumentValueType = 4
        FormatArgumentData.ArgumentValue = ReturnValue_1
        FormatArgumentData.ArgumentValueInt = 0
        FormatArgumentData.ArgumentValueFloat = 0
        FormatArgumentData.ArgumentValueGender = 0
        ReturnValue1: int32 = ReturnValue_2 * 60
        ReturnValue1_0: int32 = ReturnValue1 + Minutes
        ReturnValue1_1: FText = Default__KismetTextLibrary.Conv_IntToText(ReturnValue1_0, False, True, 2, 324)
        FormatArgumentData1.ArgumentName = "min"
        FormatArgumentData1.ArgumentValueType = 4
        FormatArgumentData1.ArgumentValue = ReturnValue1_1
        FormatArgumentData1.ArgumentValueInt = 0
        FormatArgumentData1.ArgumentValueFloat = 0
        FormatArgumentData1.ArgumentValueGender = 0
        Array: List[FormatArgumentData] = [FormatArgumentData1, FormatArgumentData]
        # Label 828
        ReturnValue_3: FText = Default__KismetTextLibrary.Format("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 879, 'Value': '{min}:{sec}'}", Array)
        Result = ReturnValue_3
    

    def UpdateInfo(self):
        ExecutionFlow.Push("L1907")
        Variable1: FText = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 25, 'Value': 'Pod will return in:'}"
        ReturnValue: bool = self.mSchematicManager.IsShipAtTradingPost()
        Variable2: FText = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 144, 'Value': 'Current Milestone:'}"
        Variable2_0: bool = ReturnValue
        
        switch = {
            False: Variable1,
            True: Variable2
        }
        self.mMilstoneLabel.SetText(switch.get(Variable2_0, None))
        Variable: FText = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 328, 'Value': 'No Milestone Selected'}"
        ReturnValue_0: TSubclassOf[FGSchematic] = self.mSchematicManager.GetActiveSchematic()
        ReturnValue_1: bool = Default__KismetSystemLibrary.IsValidClass(ReturnValue_0)
        ReturnValue_2: float = self.mSchematicManager.GetTimeUntilShipReturn()
        Variable1_0: bool = ReturnValue_1
        
        Result = None
        self.FromSecondsToText(ReturnValue_2, Ref[Result])
        ReturnValue_3: FText = Default__FGSchematic.GetSchematicDisplayName(ReturnValue_0)
        ReturnValue1: bool = self.mSchematicManager.IsShipAtTradingPost()
        Variable_0: bool = ReturnValue1
        
        switch_0 = {
            False: Variable,
            True: ReturnValue_3
        }
        
        switch_1 = {
            False: Result,
            True: switch_0.get(Variable1_0, None)
        }
        self.mMilestoneName.SetText(switch_1.get(Variable_0, None))
        ReturnValue_0 = self.mSchematicManager.GetActiveSchematic()
        ReturnValue_1 = Default__KismetSystemLibrary.IsValidClass(ReturnValue_0)
        ReturnValue1 = self.mSchematicManager.IsShipAtTradingPost()
        ReturnValue_4: bool = ReturnValue_1 and ReturnValue1
        if not ReturnValue_4:
           goto(ExecutionFlow.Pop())
        Variable_1: int32 = 0
        Variable_2: int32 = 0
        # Label 1063
        ReturnValue2: TSubclassOf[FGSchematic] = self.mSchematicManager.GetActiveSchematic()
        ReturnValue_5: List[ItemAmount] = Default__FGSchematic.GetCost(ReturnValue2)
        
        ReturnValue_6: int32 = len(ReturnValue_5)
        ReturnValue_7: bool = Variable_1 <= ReturnValue_6
        if not ReturnValue_7:
           goto(ExecutionFlow.Pop())
        Variable_2 = Variable_1
        ExecutionFlow.Push("L1833")
        ReturnValue_8: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_9: Ptr[Widget_CostSlotWrapper] = Default__WidgetBlueprintLibrary.Create(self, Widget_CostSlotWrapper, ReturnValue_8)
        ReturnValue1_0: TSubclassOf[FGSchematic] = self.mSchematicManager.GetActiveSchematic()
        ReturnValue_10: List[ItemAmount] = self.mSchematicManager.GetPaidOffCostFor(ReturnValue1_0)
        
        Item = None
        Item = ReturnValue_10[Variable_2]
        ReturnValue2 = self.mSchematicManager.GetActiveSchematic()
        ReturnValue_5 = Default__FGSchematic.GetCost(ReturnValue2)
        
        Item1 = None
        Item1 = ReturnValue_5[Variable_2]
        ReturnValue_9.Setup CostIcon(None, Item1, None, 0, Item.amount, False, False, False)
        ReturnValue_11: Ptr[PanelSlot] = self.mCostSlotContainer.AddChild(ReturnValue_9)
        goto(ExecutionFlow.Pop())
        # Label 1833
        ReturnValue_12: int32 = Variable_1 + 1
        Variable_1 = ReturnValue_12
        goto('L1063')
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_ActorDetails_Hub(1689)
    

    def UpdateInfoEvent(self):
        self.ExecuteUbergraph_Widget_ActorDetails_Hub(711)
    

    def UpdateMAMInfo(self):
        self.ExecuteUbergraph_Widget_ActorDetails_Hub(1521)
    

    def ExecuteUbergraph_Widget_ActorDetails_Hub(self):
        # Label 10
        self.UpdateInfo()
        ReturnValue: bool = self.mSchematicManager.IsShipAtTradingPost()
        if not ReturnValue:
            goto('L351')
        # Label 80
        ReturnValue1: Ptr[FGResearchManager] = Default__FGResearchManager.Get(self)
        ReturnValue_0: bool = ReturnValue1.IsAnyResearchBeingConducted()
        if not ReturnValue_0:
            goto('L471')
        self.mMamInfo.SetVisibility(3)
        self.UpdateMAMInfo()
        OutputDelegate1.BindUFunction(self, UpdateMAMInfo)
        ReturnValue1_0: TimerHandle = Default__KismetSystemLibrary.K2_SetTimerDelegate(OutputDelegate1, 0.5, True)
        self.MamInfoTimer = ReturnValue1_0
        # End
        # Label 351
        OutputDelegate.BindUFunction(self, UpdateInfoEvent)
        ReturnValue_1: TimerHandle = Default__KismetSystemLibrary.K2_SetTimerDelegate(OutputDelegate, 0.20000000298023224, True)
        self.UpdateInfoTimer = ReturnValue_1
        goto('L80')
        # Label 471
        self.mMamInfo.SetVisibility(1)
        # End
        # Label 514
        ReturnValue_2: Ptr[GameStateBase] = Default__GameplayStatics.GetGameState(self)
        State: Ptr[FGGameState] = Cast[FGGameState](ReturnValue_2)
        bSuccess: bool = State
        if not bSuccess:
            goto('L1694')
        ReturnValue_3: Ptr[FGSchematicManager] = Default__FGSchematicManager.Get(State)
        self.mSchematicManager = ReturnValue_3
        goto('L10')
        self.UpdateInfo()
        ReturnValue1_1: bool = self.mSchematicManager.IsShipAtTradingPost()
        if not ReturnValue1_1:
            goto('L1694')
        
        Default__KismetSystemLibrary.K2_ClearAndInvalidateTimerHandle(self, Ref[self.UpdateInfoTimer])
        # End
        # Label 828
        ReturnValue2: Ptr[FGResearchManager] = Default__FGResearchManager.Get(self)
        ReturnValue_4: TSubclassOf[FGSchematic] = ReturnValue2.GetResearchBeingConducted()
        ReturnValue_5: FText = Default__FGSchematic.GetSchematicDisplayName(ReturnValue_4)
        self.mMamResearchName.SetText(ReturnValue_5)
        ReturnValue_6: Ptr[Texture2D] = Default__FGItemDescriptor.GetSmallIcon(None)
        self.mMamIcon.SetBrushFromTexture(ReturnValue_6, False)
        ReturnValue3: Ptr[FGResearchManager] = Default__FGResearchManager.Get(self)
        ReturnValue1_2: bool = ReturnValue3.IsAnyResearchBeingConducted()
        if not ReturnValue1_2:
            goto('L1210')
        # End
        
        # Label 1210
        Default__KismetSystemLibrary.K2_ClearAndInvalidateTimerHandle(self, Ref[self.MamInfoTimer])
        self.mMamInfo.SetVisibility(1)
        # End
        # Label 1295
        ReturnValue2 = Default__FGResearchManager.Get(self)
        ReturnValue_4 = ReturnValue2.GetResearchBeingConducted()
        ReturnValue_7: float = ReturnValue2.GetOngoingResearchTimeLeft(ReturnValue_4)
        
        Result = None
        self.FromSecondsToText(ReturnValue_7, Ref[Result])
        self.mMamTimeLeft.SetText(Result)
        goto('L828')
        goto('L1295')
        # Label 1526
        Post: Ptr[FGBuildableTradingPost] = Cast[FGBuildableTradingPost](self.mActor)
        bSuccess1: bool = Post
        if not bSuccess1:
            goto('L1694')
        self.mTradingPost = Post
        goto('L514')
        # Label 1629
        self.Construct()
        self.Widget_ActorDetails_Container.SetShowPointer(self.ShowPointer)
        goto('L1526')
        goto('L1629')
    
