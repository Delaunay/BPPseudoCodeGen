
from codegen.ue4_stub import *

from Script.Engine import SetTextPropertyByName
from Script.FactoryGame import GetTimeTable
from Game.FactoryGame.Buildable.Vehicle.Train.Locomotive.UI.Widget_Train_TimeTable import ExecuteUbergraph_Widget_Train_TimeTable.K2Node_CustomEvent_RuleWidget
from Script.Engine import K2_SetTimerDelegate
from Script.Engine import SetObjectPropertyByName
from Game.FactoryGame.Buildable.Vehicle.Train.Locomotive.UI.Widget_Train_TimeTable import ExecuteUbergraph_Widget_Train_TimeTable.K2Node_CustomEvent_Train
from Script.UMG import GetChildIndex
from Script.Engine import GreaterEqual_IntInt
from Script.UMG import GetChildrenCount
from Script.UMG import PanelSlot
from Script.UMG import AddChild
from Script.FactoryGame import GetStops
from Script.Engine import SetBytePropertyByName
from Game.FactoryGame.Buildable.Vehicle.Train.Locomotive.UI.Widget_Train_TimeTable import ExecuteUbergraph_Widget_Train_TimeTable.K2Node_CustomEvent_Index
from Script.Engine import Not_PreBool
from Game.FactoryGame.Buildable.Vehicle.Train.Locomotive.UI.Widget_Train_TimeTable import ExecuteUbergraph_Widget_Train_TimeTable.K2Node_CustomEvent_ListButton
from Script.Engine import Default__KismetSystemLibrary
from Script.FactoryGame import Get
from Script.Engine import PlayerController
from Script.UMG import GetChildAt
from Script.Engine import Array_Find
from Script.Engine import Default__KismetArrayLibrary
from Script.UMG import HasChild
from Script.UMG import ESlateVisibility
from Script.Engine import TimerHandle
from Script.Engine import IsValid
from Game.FactoryGame.Buildable.Vehicle.Train.Locomotive.UI.Widget_Train_TimeTable import ExecuteUbergraph_Widget_Train_TimeTable.K2Node_CustomEvent_RuleWidget3
from Script.UMG import Default__WidgetBlueprintLibrary
from Script.UMG import Destruct
from Script.Engine import EqualEqual_IntInt
from Game.FactoryGame.Buildable.Vehicle.Train.Locomotive.UI.Widget_Train_TimeTable import ExecuteUbergraph_Widget_Train_TimeTable.K2Node_CustomEvent_RuleWidget1
from Script.FactoryGame import GetTrainStations
from Script.FactoryGame import FGRailroadSubsystem
from Game.FactoryGame.Buildable.Vehicle.Train.Locomotive.UI.Widget_Train_TimeTable_Rule import Widget_Train_TimeTable_Rule
from Script.FactoryGame import GetCurrentStop
from Script.UMG import Widget
from Script.FactoryGame import Default__FGRailroadSubsystem
from Game.FactoryGame.Interface.UI.InGame.-Shared.Widget_ListButton import Widget_ListButton
from Script.Engine import EqualEqual_ObjectObject
from Game.FactoryGame.Buildable.Vehicle.Train.Locomotive.UI.Widget_Train_TimeTable import ExecuteUbergraph_Widget_Train_TimeTable
from Game.FactoryGame.Buildable.Vehicle.Train.Locomotive.UI.Widget_Train_TimeTable_AvilableStations import Widget_Train_TimeTable_AvilableStations
from Game.FactoryGame.Interface.UI.Assets.Map.MapCompass_Circle_Border import MapCompass_Circle_Border
from Script.UMG import UserWidget
from Game.FactoryGame.Interface.UI.HUDHelpers.BPHUDHelpers import Default__BPHUDHelpers
from Script.Engine import NotEqual_ObjectObject
from Script.FactoryGame import GetTrackGraphID
from Script.FactoryGame import GetStationName
from Script.UMG import Create
from Script.FactoryGame import TimeTableStop
from Script.FactoryGame import FGRailroadTimeTable
from Script.FactoryGame import FGTrain
from Script.FactoryGame import NewTimeTable
from Script.Engine import Array_Clear
from Script.Engine import K2_ClearAndInvalidateTimerHandle
from Script.FactoryGame import FGTrainStationIdentifier
from Game.FactoryGame.Buildable.Vehicle.Train.Locomotive.UI.Widget_Train_TimeTable import ExecuteUbergraph_Widget_Train_TimeTable.K2Node_CustomEvent_RuleWidget2

class Widget_Train_TimeTable(UserWidget):
    mTrainStations: List[Ptr[FGTrainStationIdentifier]]
    mTrain: Ptr[FGTrain]
    mTimeTable: Ptr[FGRailroadTimeTable]
    mAvailableStationsWidget: Ptr[Widget_Train_TimeTable_AvilableStations]
    SelectedRule: Ptr[Widget_Train_TimeTable_Rule]
    mAvailableStationsSelectedIndex: int32
    mNewStops: List[TimeTableStop]
    mCurrentStopRule: Ptr[Widget_Train_TimeTable_Rule]
    mCheckCurrentStopTimer: TimerHandle
    
    def SetCurrentStop(self, RuleWidget: Ptr[Widget_Train_TimeTable_Rule]):
        ReturnValue: bool = self.Widget_Splitter_OutputList.mOutputContainer.HasChild(RuleWidget)
        if not ReturnValue:
            goto('L301')
        ReturnValue_0: Ptr[PlayerController] = self.GetOwningPlayer()
        
        RCO = None
        Default__BPHUDHelpers.GetDefaultRCO(ReturnValue_0, self, Ref[RCO])
        ReturnValue_1: int32 = self.Widget_Splitter_OutputList.mOutputContainer.GetChildIndex(RuleWidget)
        RCO.Server_SetTimeTableCurrentStop(self.mTimeTable, ReturnValue_1)
    

    def ShowApplyChangesPrompt(self):
        self.mApplyChangesPrompt.SetVisibility(0)
    

    def CloseAvailableStationsWidget(self):
        self.mAvailableStationsWidget.SetIsVisible(False)
        self.SelectedRule.SetIsSelected(False)
        self.SelectedRule = None
        self.mAvailableStationsSelectedIndex = -1
    

    def MoveRule(self, RuleWidget: Ptr[Widget_Train_TimeTable_Rule], MoveDown: bool):
        LocalRuleIndex = 0
        LocalRule = RuleWidget
        LocalMoveDown = MoveDown
        LocalStation = LocalRule.mStation
        ReturnValue: int32 = self.Widget_Splitter_OutputList.mOutputContainer.GetChildIndex(LocalRule)
        LocalRuleIndex = ReturnValue
        ReturnValue_0: int32 = LocalRuleIndex - 1
        ReturnValue_1: int32 = LocalRuleIndex + 1
        Variable1: bool = LocalMoveDown
        
        switch = {
            False: ReturnValue_0,
            True: ReturnValue_1
        }
        LocalTargetIndex = switch.get(Variable1, None)
        Variable: bool = LocalMoveDown
        ReturnValue_2: int32 = self.Widget_Splitter_OutputList.mOutputContainer.GetChildrenCount()
        ReturnValue_3: bool = LocalRuleIndex <= ReturnValue_2
        ReturnValue_4: bool = GreaterEqual_IntInt(LocalRuleIndex, 0)
        
        switch_0 = {
            False: ReturnValue_3,
            True: ReturnValue_4
        }
        if not switch_0.get(Variable, None):
            goto('L960')
        # Label 605
        ReturnValue_5: Ptr[Widget] = self.Widget_Splitter_OutputList.mOutputContainer.GetChildAt(LocalTargetIndex)
        Rule: Ptr[Widget_Train_TimeTable_Rule] = Cast[Widget_Train_TimeTable_Rule](ReturnValue_5)
        bSuccess: bool = Rule
        if not bSuccess:
            goto('L960')
        LocalTargetRule = Rule
        LocalRule.UpdateRule(LocalTargetRule.mStation)
        LocalTargetRule.UpdateRule(LocalStation)
        LocalTargetRule.PlayNewNameAnim()
        LocalRule.PlayNewNameAnim()
    

    def SetSelectedRule(self, SelectedRule: Ptr[Widget_Train_TimeTable_Rule]):
        ExecutionFlow.Push("L478")
        self.SelectedRule = SelectedRule
        Variable: int32 = 0
        # Label 47
        ReturnValue: int32 = self.Widget_Splitter_OutputList.mOutputContainer.GetChildrenCount()
        ReturnValue_0: bool = Variable <= ReturnValue
        if not ReturnValue_0:
           goto(ExecutionFlow.Pop())
        ExecutionFlow.Push("L404")
        ReturnValue_1: Ptr[Widget] = self.Widget_Splitter_OutputList.mOutputContainer.GetChildAt(Variable)
        Rule: Ptr[Widget_Train_TimeTable_Rule] = Cast[Widget_Train_TimeTable_Rule](ReturnValue_1)
        bSuccess: bool = Rule
        if not bSuccess:
           goto(ExecutionFlow.Pop())
        ReturnValue_2: bool = EqualEqual_ObjectObject(Rule, self.SelectedRule)
        Rule.SetIsSelected(ReturnValue_2)
        goto(ExecutionFlow.Pop())
        # Label 404
        ReturnValue_3: int32 = Variable + 1
        Variable = ReturnValue_3
        goto('L47')
    

    def AddRule(self, mStation: Const[Ref[Ptr[FGTrainStationIdentifier]]]):
        ReturnValue3: int32 = self.Widget_Splitter_OutputList.mOutputContainer.GetChildrenCount()
        ReturnValue: bool = EqualEqual_IntInt(ReturnValue3, 1)
        if not ReturnValue:
            goto('L306')
        ReturnValue1: Ptr[Widget] = self.Widget_Splitter_OutputList.mOutputContainer.GetChildAt(0)
        Rule1: Ptr[Widget_Train_TimeTable_Rule] = Cast[Widget_Train_TimeTable_Rule](ReturnValue1)
        # Label 225
        bSuccess1: bool = Rule1
        if not bSuccess1:
            goto('L306')
        Rule1.SetOrderButtonsVisibility(False, True)
        # Label 306
        ReturnValue_0: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_1: Ptr[Widget_Train_TimeTable_Rule] = Default__WidgetBlueprintLibrary.Create(self, Widget_Train_TimeTable_Rule, ReturnValue_0)
        Default__KismetSystemLibrary.SetObjectPropertyByName(ReturnValue_1, "mStation", mStation)
        ReturnValue_2: Ptr[PanelSlot] = self.Widget_Splitter_OutputList.mOutputContainer.AddChild(ReturnValue_1)
        OutputDelegate4.BindUFunction(self, OnRuleClicked)
        ReturnValue_1.OnClicked.AddUnique(OutputDelegate4)
        OutputDelegate3.BindUFunction(self, OnRuleDeleted)
        ReturnValue_1.OnDeleted.AddUnique(OutputDelegate3)
        OutputDelegate2.BindUFunction(self, OnRuleMoveUp)
        ReturnValue_1.OnMoveUpClicked.AddUnique(OutputDelegate2)
        OutputDelegate1.BindUFunction(self, OnRuleMoveDown)
        ReturnValue_1.OnMoveDownClicked.AddUnique(OutputDelegate1)
        OutputDelegate.BindUFunction(self, SetCurrentStop)
        ReturnValue_1.OnSetCurrentStopClicked.AddUnique(OutputDelegate)
        ReturnValue2: int32 = self.Widget_Splitter_OutputList.mOutputContainer.GetChildrenCount()
        ReturnValue_3: bool = ReturnValue2 <= 1
        if not ReturnValue_3:
            goto('L1010')
        ReturnValue_1.SetOrderButtonsVisibility(False, False)
        # End
        # Label 1010
        ReturnValue1_0: int32 = self.Widget_Splitter_OutputList.mOutputContainer.GetChildrenCount()
        ReturnValue_4: int32 = ReturnValue1_0 - 2
        ReturnValue_5: Ptr[Widget] = self.Widget_Splitter_OutputList.mOutputContainer.GetChildAt(ReturnValue_4)
        Rule: Ptr[Widget_Train_TimeTable_Rule] = Cast[Widget_Train_TimeTable_Rule](ReturnValue_5)
        bSuccess: bool = Rule
        if not bSuccess:
            goto('L1466')
        ReturnValue_6: int32 = self.Widget_Splitter_OutputList.mOutputContainer.GetChildrenCount()
        ReturnValue_7: bool = ReturnValue_6 > 2
        Rule.SetOrderButtonsVisibility(ReturnValue_7, True)
        ReturnValue_1.SetOrderButtonsVisibility(True, False)
    

    def UpdateStopsOnServer(self):
        self.GenerateNewStopArray()
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(self.mTimeTable)
        if not ReturnValue:
            goto('L217')
        # Label 79
        ReturnValue_0: Ptr[PlayerController] = self.GetOwningPlayer()
        
        RCO = None
        Default__BPHUDHelpers.GetDefaultRCO(ReturnValue_0, self, Ref[RCO])
        
        RCO.Server_SetTimeTableStops(self.mTimeTable, Ref[self.mNewStops])
        # End
        # Label 217
        ReturnValue_1: Ptr[FGRailroadTimeTable] = self.mTrain.NewTimeTable()
        self.mTimeTable = ReturnValue_1
        goto('L79')
    

    def GenerateNewStopArray(self):
        ExecutionFlow.Push("L567")
        
        Default__KismetArrayLibrary.Array_Clear(Ref[self.mNewStops])
        Variable: int32 = 0
        # Label 69
        ReturnValue: int32 = self.Widget_Splitter_OutputList.mOutputContainer.GetChildrenCount()
        ReturnValue_0: bool = Variable <= ReturnValue
        if not ReturnValue_0:
           goto(ExecutionFlow.Pop())
        ExecutionFlow.Push("L493")
        ReturnValue_1: Ptr[Widget] = self.Widget_Splitter_OutputList.mOutputContainer.GetChildAt(Variable)
        Rule: Ptr[Widget_Train_TimeTable_Rule] = Cast[Widget_Train_TimeTable_Rule](ReturnValue_1)
        bSuccess: bool = Rule
        if not bSuccess:
           goto(ExecutionFlow.Pop())
        TimeTableStop.Station = Rule.mStation
        TimeTableStop.Duration = 1
        
        TimeTableStop = None
        ReturnValue_2: int32 = self.mNewStops.append(TimeTableStop)
        goto(ExecutionFlow.Pop())
        # Label 493
        ReturnValue_3: int32 = Variable + 1
        Variable = ReturnValue_3
        goto('L69')
    

    def PopulateAvailableStations(self):
        ExecutionFlow.Push("L1177")
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(self.mAvailableStationsWidget)
        if not ReturnValue:
           goto(ExecutionFlow.Pop())
        self.mAvailableStationsWidget.mList.ClearChildren()
        self.mAvailableStationsWidget.SetIsVisible(True)
        self.UpdateTrainStations()
        Variable: int32 = 0
        Variable_0: int32 = 0
        
        # Label 221
        ReturnValue_0: int32 = len(self.mTrainStations)
        ReturnValue_1: bool = Variable <= ReturnValue_0
        if not ReturnValue_1:
           goto(ExecutionFlow.Pop())
        Variable_0 = Variable
        ExecutionFlow.Push("L1103")
        ReturnValue_2: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_3: Ptr[Widget_ListButton] = Default__WidgetBlueprintLibrary.Create(self, Widget_ListButton, ReturnValue_2)
        Default__KismetSystemLibrary.SetObjectPropertyByName(ReturnValue_3, "mIcon", MapCompass_Circle_Border)
        
        Item = None
        Item = self.mTrainStations[Variable_0]
        # Label 567
        ReturnValue_4: FText = Item.GetStationName()
        
        Default__KismetSystemLibrary.SetTextPropertyByName(ReturnValue_3, "mTitle", Ref[ReturnValue_4])
        Variable_1: uint8 = 2
        
        Item = None
        Item = self.mTrainStations[Variable_0]
        ReturnValue_5: bool = EqualEqual_ObjectObject(Item, self.SelectedRule.mStation)
        Variable_2: bool = ReturnValue_5
        Variable1: uint8 = 3
        
        switch = {
            False: Variable_1,
            True: Variable1
        }
        Default__KismetSystemLibrary.SetBytePropertyByName(ReturnValue_3, "iconVisibility", switch.get(Variable_2, None))
        ReturnValue_6: Ptr[PanelSlot] = self.mAvailableStationsWidget.mList.AddChild(ReturnValue_3)
        OutputDelegate.BindUFunction(self, UpdateAvailableStationsSelectedIndex)
        ReturnValue_3.OnClicked.AddUnique(OutputDelegate)
        goto(ExecutionFlow.Pop())
        # Label 1103
        ReturnValue_7: int32 = Variable + 1
        Variable = ReturnValue_7
        goto('L221')
    

    def PopulateTimeTable(self):
        ExecutionFlow.Push("L530")
        ReturnValue: Ptr[FGRailroadTimeTable] = self.mTrain.GetTimeTable()
        # Label 47
        ReturnValue_0: bool = Default__KismetSystemLibrary.IsValid(ReturnValue)
        if not ReturnValue_0:
           goto(ExecutionFlow.Pop())
        self.mTimeTable = ReturnValue
        stops: List[TimeTableStop] = []
        
        self.mTimeTable.GetStops(Ref[stops])
        Variable: int32 = 0
        Variable_0: int32 = 0
        
        # Label 225
        ReturnValue_1: int32 = len(stops)
        ReturnValue_2: bool = Variable <= ReturnValue_1
        if not ReturnValue_2:
           goto(ExecutionFlow.Pop())
        Variable_0 = Variable
        ExecutionFlow.Push("L456")
        
        Item = None
        Item = stops[Variable_0]
        
        Item.Station = None
        self.AddRule(Ref[Item.Station])
        goto(ExecutionFlow.Pop())
        # Label 456
        ReturnValue_3: int32 = Variable + 1
        Variable = ReturnValue_3
        goto('L225')
    

    def UpdateTrainStations(self):
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_0: int32 = self.mTrain.GetTrackGraphID()
        ReturnValue_1: Ptr[FGRailroadSubsystem] = Default__FGRailroadSubsystem.Get(ReturnValue)
        stations: List[Ptr[FGTrainStationIdentifier]] = []
        
        ReturnValue_1.GetTrainStations(ReturnValue_0, Ref[stations])
        self.mTrainStations = stations
    

    def Init(self, Train: Ptr[FGTrain]):
        ExecuteUbergraph_Widget_Train_TimeTable.K2Node_CustomEvent_Train = Train #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_Train_TimeTable(828)
    

    def BndEvt__Widget_Splitter_OutputList_K2Node_ComponentBoundEvent_0_OnAddClicked__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_Train_TimeTable(852)
    

    def OnRuleClicked(self, RuleWidget: Ptr[Widget_Train_TimeTable_Rule]):
        ExecuteUbergraph_Widget_Train_TimeTable.K2Node_CustomEvent_RuleWidget3 = RuleWidget #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_Train_TimeTable(949)
    

    def UpdateStation(self):
        self.ExecuteUbergraph_Widget_Train_TimeTable(1075)
    

    def UpdateAvailableStationsSelectedIndex(self, index: int32, ListButton: Ptr[Widget_ListButton]):
        ExecuteUbergraph_Widget_Train_TimeTable.K2Node_CustomEvent_Index = index #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_Train_TimeTable.K2Node_CustomEvent_ListButton = ListButton #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_Train_TimeTable(1462)
    

    def OnRuleDeleted(self, RuleWidget: Ptr[Widget_Train_TimeTable_Rule]):
        ExecuteUbergraph_Widget_Train_TimeTable.K2Node_CustomEvent_RuleWidget2 = RuleWidget #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_Train_TimeTable(1508)
    

    def Destruct(self):
        self.ExecuteUbergraph_Widget_Train_TimeTable(1930)
    

    def OnRuleMoveUp(self, RuleWidget: Ptr[Widget_Train_TimeTable_Rule]):
        ExecuteUbergraph_Widget_Train_TimeTable.K2Node_CustomEvent_RuleWidget1 = RuleWidget #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_Train_TimeTable(1945)
    

    def OnRuleMoveDown(self, RuleWidget: Ptr[Widget_Train_TimeTable_Rule]):
        ExecuteUbergraph_Widget_Train_TimeTable.K2Node_CustomEvent_RuleWidget = RuleWidget #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_Train_TimeTable(2067)
    

    def CheckCurrentStop(self):
        self.ExecuteUbergraph_Widget_Train_TimeTable(2189)
    

    def ExecuteUbergraph_Widget_Train_TimeTable(self):
        # Label 10
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(self.mTimeTable)
        if not ReturnValue:
            goto('L2194')
        ReturnValue_0: int32 = self.mTimeTable.GetCurrentStop()
        ReturnValue1: int32 = self.Widget_Splitter_OutputList.mOutputContainer.GetChildrenCount()
        ReturnValue_1: bool = ReturnValue_0 <= ReturnValue1
        if not ReturnValue_1:
            goto('L2194')
        ReturnValue_0 = self.mTimeTable.GetCurrentStop()
        ReturnValue_2: Ptr[Widget] = self.Widget_Splitter_OutputList.mOutputContainer.GetChildAt(ReturnValue_0)
        Rule: Ptr[Widget_Train_TimeTable_Rule] = Cast[Widget_Train_TimeTable_Rule](ReturnValue_2)
        bSuccess: bool = Rule
        if not bSuccess:
            goto('L2194')
        ReturnValue_3: bool = NotEqual_ObjectObject(Rule, self.mCurrentStopRule)
        if not ReturnValue_3:
            goto('L2194')
        ReturnValue1_0: bool = Default__KismetSystemLibrary.IsValid(self.mCurrentStopRule)
        if not ReturnValue1_0:
            goto('L605')
        self.mCurrentStopRule.SetIsNextStop(False)
        # Label 605
        self.mCurrentStopRule = Rule
        self.mCurrentStopRule.SetIsNextStop(True)
        # End
        # Label 666
        self.UpdateTrainStations()
        self.PopulateTimeTable()
        self.CheckCurrentStop()
        OutputDelegate.BindUFunction(self, CheckCurrentStop)
        ReturnValue_4: TimerHandle = Default__KismetSystemLibrary.K2_SetTimerDelegate(OutputDelegate, 1, True)
        self.mCheckCurrentStopTimer = ReturnValue_4
        # End
        self.mTrain = Train
        goto('L666')
        
        Item = None
        Item = self.mTrainStations[0]
        
        Item = None
        self.AddRule(Ref[Item])
        self.ShowApplyChangesPrompt()
        # End
        ReturnValue_5: bool = Not_PreBool(RuleWidget3.mIsSelected)
        if not ReturnValue_5:
            goto('L1056')
        self.SetSelectedRule(RuleWidget3)
        self.PopulateAvailableStations()
        # End
        # Label 1056
        self.CloseAvailableStationsWidget()
        # End
        ReturnValue_6: bool = self.mAvailableStationsSelectedIndex > -1
        
        self.SelectedRule.mStation = None
        ReturnValue_7: int32 = Default__KismetArrayLibrary.Array_Find(Ref[self.mTrainStations], Ref[self.SelectedRule.mStation])
        ReturnValue_8: bool = ReturnValue_7 != self.mAvailableStationsSelectedIndex
        ReturnValue_9: bool = ReturnValue_6 and ReturnValue_8
        if not ReturnValue_9:
            goto('L1443')
        
        Item1 = None
        Item1 = self.mTrainStations[self.mAvailableStationsSelectedIndex]
        self.SelectedRule.UpdateRule(Item1)
        self.SelectedRule.PlayNewNameAnim()
        self.ShowApplyChangesPrompt()
        # Label 1443
        self.CloseAvailableStationsWidget()
        # End
        self.mAvailableStationsSelectedIndex = Index
        self.UpdateStation()
        # End
        RuleWidget2.RemoveFromParent()
        self.ShowApplyChangesPrompt()
        ReturnValue_10: int32 = self.Widget_Splitter_OutputList.mOutputContainer.GetChildrenCount()
        ReturnValue_11: bool = EqualEqual_IntInt(ReturnValue_10, 1)
        if not ReturnValue_11:
            goto('L2194')
        ReturnValue1_1: Ptr[Widget] = self.Widget_Splitter_OutputList.mOutputContainer.GetChildAt(0)
        Rule1: Ptr[Widget_Train_TimeTable_Rule] = Cast[Widget_Train_TimeTable_Rule](ReturnValue1_1)
        bSuccess1: bool = Rule1
        if not bSuccess1:
            goto('L2194')
        Rule1.SetOrderButtonsVisibility(False, False)
        # End
        # Label 1869
        self.UpdateStopsOnServer()
        
        Default__KismetSystemLibrary.K2_ClearAndInvalidateTimerHandle(self, Ref[self.mCheckCurrentStopTimer])
        # End
        self.Destruct()
        goto('L1869')
        self.MoveRule(RuleWidget1, False)
        self.ShowApplyChangesPrompt()
        ReturnValue2: bool = Default__KismetSystemLibrary.IsValid(self.SelectedRule)
        if not ReturnValue2:
            goto('L2194')
        self.CloseAvailableStationsWidget()
        # End
        self.MoveRule(RuleWidget, True)
        self.ShowApplyChangesPrompt()
        ReturnValue3: bool = Default__KismetSystemLibrary.IsValid(self.SelectedRule)
        if not ReturnValue3:
            goto('L2194')
        self.CloseAvailableStationsWidget()
        # End
        goto('L10')
    
