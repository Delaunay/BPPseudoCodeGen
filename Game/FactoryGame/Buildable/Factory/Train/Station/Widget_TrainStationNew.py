
from codegen.ue4_stub import *

from Script.Engine import SetTextPropertyByName
from Script.Engine import GetEmptyText
from Script.Engine import Conv_TextToString
from Script.FactoryGame import GetPowerCircuit
from Script.Engine import Delay
from Script.Engine import SetObjectPropertyByName
from Script.UMG import GetChildrenCount
from Game.FactoryGame.Buildable.Factory.Train.Station.Widget_TrainStationNew import ExecuteUbergraph_Widget_TrainStationNew.K2Node_CustomEvent_button
from Script.UMG import PanelSlot
from Script.UMG import AddChild
from Script.FactoryGame import FGPowerInfoComponent
from Script.FactoryGame import FGPowerCircuit
from Script.Engine import Not_PreBool
from Script.Engine import LatentActionInfo
from Script.Engine import Default__KismetSystemLibrary
from Script.FactoryGame import Get
from Script.UMG import GetChildAt
from Script.Engine import PlayerController
from Script.Engine import Default__KismetArrayLibrary
from Script.UMG import ESlateVisibility
from Script.FactoryGame import GetTrains
from Script.UMG import SetText
from Game.FactoryGame.Buildable.Factory.Train.Station.Widget_TrainStationNew import ExecuteUbergraph_Widget_TrainStationNew.K2Node_ComponentBoundEvent_Text
from Game.FactoryGame.Interface.UI.InGame.Widget_UseableBase import Construct
from Game.FactoryGame.Buildable.Factory.Train.Station.Widget_TrainStationNew import ExecuteUbergraph_Widget_TrainStationNew
from Script.Engine import Len
from Script.Engine import IsValid
from Game.FactoryGame.Buildable.Factory.Train.Station.Widget_TrainStationNew import ExecuteUbergraph_Widget_TrainStationNew.K2Node_ComponentBoundEvent_CommitMethod
from Script.UMG import Default__WidgetBlueprintLibrary
from Script.Engine import Default__KismetTextLibrary
from Script.Engine import Conv_StringToText
from Script.FactoryGame import GetTrainName
from Script.FactoryGame import FGRailroadSubsystem
from Game.FactoryGame.Buildable.Factory.Train.Station.Widget_TrainStationNew import ExecuteUbergraph_Widget_TrainStationNew.K2Node_ComponentBoundEvent_Text1
from Script.UMG import Widget
from Script.CoreUObject import LinearColor
from Script.FactoryGame import Default__FGRailroadSubsystem
from Game.FactoryGame.Interface.UI.InGame.Widget_UseableBase import Widget_UseableBase
from Script.Engine import Default__KismetStringLibrary
from Game.FactoryGame.Buildable.Vehicle.Train.Locomotive.UI.Widget_Locomotive_Menu import Widget_Locomotive_Menu
from Script.Engine import Conv_IntToString
from Script.Engine import NotEqual_ByteByte
from Script.Engine import RandomInteger
from Game.FactoryGame.Buildable.Factory.Train.Station.Widget_TrainStationNew import ExecuteUbergraph_Widget_TrainStationNew.K2Node_CustomEvent_state
from Script.FactoryGame import GetPowerInfo
from Script.FactoryGame import GetStationIdentifier
from Script.Engine import EqualEqual_TextText
from Script.FactoryGame import GetTrackGraphID
from Game.FactoryGame.Buildable.Factory.Train.Station.Widget_TrainButton import Widget_TrainButton
from Script.UMG import HasAnyChildren
from Script.UMG import Create
from Script.FactoryGame import GetStationName
from Script.FactoryGame import FGTrain
from Script.FactoryGame import FGBuildableRailroadStation
from Script.Engine import PrintString
from Script.FactoryGame import FGTrainStationIdentifier
from Script.SlateCore import ETextCommit
from Script.Engine import GetSubstring
from Script.Engine import NotEqual_StriStri

class Widget_TrainStationNew(Widget_UseableBase):
    RailroadStation: Ptr[FGBuildableRailroadStation]
    mInfoTextMessages: List[FText] = ['NSLOCTEXT("", "08F621E84D9B3EE89C9807B6A21C563C", "Please mind the gap between the train and the platform.")', 'NSLOCTEXT("", "D163D589438F0BF16025CEB2F0017995", "Don\\\'t leave any unattended crates on the platform.")', 'NSLOCTEXT("", "3D02AE6A464DAB1CB91A0D94213A74DA", "Have an efficient day!")', 'NSLOCTEXT("", "C82A6F36422C3CBCEF5751895A7E290E", "FICSIT and its affiliates are not responsible for any delays caused by any reason, including but not limited to; hog attacks, biomass on track, oncoming trains, collisions, nuclear meltdowns or general situational derailment.")', 'NSLOCTEXT("", "A114B98A4FD9DA291B189597F1EC4130", "Be sure to have your FICSIT badge ready at all times.")']
    mActiveTrainButton: Ptr[Widget_TrainButton]
    mInvalidTrainStationNames: List[FString] = ['wwwwwwwwwwwwwwwwwwwwww']
    mStationNameText: FText
    mInputMethod: uint8
    mUseMouse = True
    mRestoreFocusWhenLost = True
    mDesiredHorizontalAlignment = 2
    mDesiredVerticalAlignment = 2
    mCallCustomTickOnConstruct = True
    
    def CheckStationNameLengthAndValidity(self):
        ExecutionFlow.Push("L535")
        Variable: int32 = 0
        Variable_0: int32 = 0
        
        # Label 51
        ReturnValue: int32 = len(self.mInvalidTrainStationNames)
        ReturnValue_0: bool = Variable <= ReturnValue
        if not ReturnValue_0:
           goto(ExecutionFlow.Pop())
        Variable_0 = Variable
        ExecutionFlow.Push("L461")
        
        ReturnValue_1: FString = Default__KismetTextLibrary.Conv_TextToString(Ref[self.mStationNameText])
        
        Item = None
        Item = self.mInvalidTrainStationNames[Variable_0]
        ReturnValue_2: FString = Default__KismetStringLibrary.GetSubstring(ReturnValue_1, 0, 22)
        ReturnValue_3: bool = Default__KismetStringLibrary.NotEqual_StriStri(ReturnValue_2, Item)
        StationNameIsValid = ReturnValue_3
        # End
        # Label 461
        ReturnValue_4: int32 = Variable + 1
        Variable = ReturnValue_4
        goto('L51')
    

    def SetRandomInfoMessage(self):
        
        ReturnValue: int32 = len(self.mInfoTextMessages)
        ReturnValue_0: int32 = RandomInteger(ReturnValue)
        self.mInfoMessage.SetText(self.mInfoTextMessages[ReturnValue_0])
    

    def UpdatePowerStatus(self):
        ExecutionFlow.Push("L982")
        Variable: uint8 = 1
        Variable1: uint8 = 3
        ReturnValue2: bool = self.RailroadStation.HasPower()
        Variable_0: bool = ReturnValue2
        
        switch = {
            False: Variable1,
            True: Variable
        }
        self.mNoPowerWarning.SetVisibility(switch.get(Variable_0, None))
        Variable_1: int32 = 0
        # Label 222
        ReturnValue: int32 = self.mTrainList.GetChildrenCount()
        ReturnValue_0: bool = Variable_1 <= ReturnValue
        if not ReturnValue_0:
            goto('L646')
        ExecutionFlow.Push("L908")
        ReturnValue1: Ptr[Widget] = self.mTrainList.GetChildAt(Variable_1)
        Button: Ptr[Widget_TrainButton] = Cast[Widget_TrainButton](ReturnValue1)
        bSuccess1: bool = Button
        if not bSuccess1:
           goto(ExecutionFlow.Pop())
        ReturnValue1_0: bool = self.RailroadStation.HasPower()
        ReturnValue_1: bool = Not_PreBool(ReturnValue1_0)
        Button.Widget_TrainWarning.ShouldForceWarning(ReturnValue_1, "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 598, 'Value': 'No Power'}")
        goto(ExecutionFlow.Pop())
        # Label 646
        ReturnValue_2: bool = self.mLocomotiveMenuContainer.HasAnyChildren()
        if not ReturnValue_2:
           goto(ExecutionFlow.Pop())
        ReturnValue_3: Ptr[Widget] = self.mLocomotiveMenuContainer.GetChildAt(0)
        Menu: Ptr[Widget_Locomotive_Menu] = Cast[Widget_Locomotive_Menu](ReturnValue_3)
        bSuccess: bool = Menu
        if not bSuccess:
           goto(ExecutionFlow.Pop())
        ReturnValue_4: bool = self.RailroadStation.HasPower()
        Menu.mFakeHasPower = ReturnValue_4
        goto(ExecutionFlow.Pop())
        # Label 908
        ReturnValue_5: int32 = Variable_1 + 1
        Variable_1 = ReturnValue_5
        goto('L222')
    

    def ShowLocomotiveMenu(self, mTrain: Ptr[FGTrain]):
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_0: Ptr[Widget_Locomotive_Menu] = Default__WidgetBlueprintLibrary.Create(self, Widget_Locomotive_Menu, ReturnValue)
        Default__KismetSystemLibrary.SetObjectPropertyByName(ReturnValue_0, "mTrain", mTrain)
        ReturnValue_1: bool = self.RailroadStation.HasPower()
        ReturnValue_0.mFakeHasPower = ReturnValue_1
        ReturnValue_2: Ptr[PanelSlot] = self.mLocomotiveMenuContainer.AddChild(ReturnValue_0)
        self.mTrainStationWindow.SetVisibility(3)
        self.mLocomotiveMenuContainer.SetVisibility(0)
        OutputDelegate1.BindUFunction(self, OnLocomotiveMenuClosed)
        ReturnValue_0.OnClose.AddUnique(OutputDelegate1)
        OutputDelegate.BindUFunction(self, OnTrainNameChanged)
        ReturnValue_0.OnTrainNameChanged.AddUnique(OutputDelegate)
    

    def GenerateTrainList(self):
        ExecutionFlow.Push("L1385")
        ReturnValue: Ptr[FGTrainStationIdentifier] = self.RailroadStation.GetStationIdentifier()
        ReturnValue_0: int32 = ReturnValue.GetTrackGraphID()
        ReturnValue1: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_1: Ptr[FGRailroadSubsystem] = Default__FGRailroadSubsystem.Get(ReturnValue1)
        trains: List[Ptr[FGTrain]] = []
        
        ReturnValue_1.GetTrains(ReturnValue_0, Ref[trains])
        Variable: int32 = 0
        Variable_0: int32 = 0
        
        # Label 279
        ReturnValue_2: int32 = len(trains)
        ReturnValue_3: bool = Variable <= ReturnValue_2
        if not ReturnValue_3:
            goto('L1118')
        Variable_0 = Variable
        ExecutionFlow.Push("L1311")
        
        Item = None
        Item = trains[Variable_0]
        localFGTrain = Item
        ReturnValue_4: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_5: Ptr[Widget_TrainButton] = Default__WidgetBlueprintLibrary.Create(self, Widget_TrainButton, ReturnValue_4)
        Default__KismetSystemLibrary.SetObjectPropertyByName(ReturnValue_5, "mTrainObject", localFGTrain)
        Variable_1: FText = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 668, 'Value': 'Locomotive'}"
        ReturnValue_6: FText = localFGTrain.GetTrainName()
        ReturnValue_7: FText = Default__KismetTextLibrary.GetEmptyText()
        
        ReturnValue_8: bool = Default__KismetTextLibrary.EqualEqual_TextText(Ref[ReturnValue_6], Ref[ReturnValue_7])
        Variable_2: bool = ReturnValue_8
        
        switch = {
            False: ReturnValue_6,
            True: Variable_1
        }
        
        switch.get(Variable_2, None) = None
        Default__KismetSystemLibrary.SetTextPropertyByName(ReturnValue_5, "mTitle", Ref[switch.get(Variable_2, None)])
        ReturnValue_9: Ptr[PanelSlot] = self.mTrainList.AddChild(ReturnValue_5)
        OutputDelegate.BindUFunction(self, OnTrainButtonClicked)
        ReturnValue_5.OnClicked.AddUnique(OutputDelegate)
        goto(ExecutionFlow.Pop())
        # Label 1118
        ReturnValue_10: int32 = self.mTrainList.GetChildrenCount()
        ReturnValue_11: FString = Default__KismetStringLibrary.Conv_IntToString(ReturnValue_10)
        Default__KismetSystemLibrary.PrintString(self, ReturnValue_11, True, True, LinearColor(R = 0, G = 0.6600000262260437, B = 1, A = 1), 2)
        goto(ExecutionFlow.Pop())
        # Label 1311
        ReturnValue_12: int32 = Variable + 1
        Variable = ReturnValue_12
        goto('L279')
    

    def GetStationName(self):
        Variable: FText = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 20, 'Value': 'INVALID IDENTIFIER'}"
        ReturnValue: Ptr[FGTrainStationIdentifier] = self.RailroadStation.GetStationIdentifier()
        ReturnValue_0: bool = Default__KismetSystemLibrary.IsValid(ReturnValue)
        ReturnValue_1: FText = ReturnValue.GetStationName()
        Variable_0: bool = ReturnValue_0
        
        switch = {
            False: Variable,
            True: ReturnValue_1
        }
        Name = switch.get(Variable_0, None)
    

    def SetStationName(self, Name: FText):
        
        RCO = None
        self.GetDefaultRCO(Ref[RCO])
        ReturnValue: Ptr[FGTrainStationIdentifier] = self.RailroadStation.GetStationIdentifier()
        RCO.Server_SetTrainStationName(ReturnValue, Name)
    

    def OnGetPowerCircuit(self):
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(self.RailroadStation)
        # Label 51
        if not ReturnValue:
            goto('L173')
        ReturnValue_0: Ptr[FGPowerInfoComponent] = self.RailroadStation.GetPowerInfo()
        ReturnValue_1: Ptr[FGPowerCircuit] = ReturnValue_0.GetPowerCircuit()
        ReturnValue_2: Ptr[FGPowerCircuit] = ReturnValue_1
        goto('L184')
        # Label 173
        ReturnValue_2 = None
    

    def BndEvt__mStationNameInput_K2Node_ComponentBoundEvent_0_OnEditableTextCommittedEvent__DelegateSignature(self, text: Const[Ref[FText]], CommitMethod: uint8):
        ExecuteUbergraph_Widget_TrainStationNew.K2Node_ComponentBoundEvent_Text1 = text #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_TrainStationNew.K2Node_ComponentBoundEvent_CommitMethod = CommitMethod #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_TrainStationNew(391)
    

    def OnTrainButtonClicked(self, Button: Ptr[Widget_TrainButton]):
        ExecuteUbergraph_Widget_TrainStationNew.K2Node_CustomEvent_button = Button #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_TrainStationNew(758)
    

    def OnLocomotiveMenuClosed(self):
        self.ExecuteUbergraph_Widget_TrainStationNew(823)
    

    def OnTrainNameChanged(self):
        self.ExecuteUbergraph_Widget_TrainStationNew(911)
    

    def OnPowerChanged(self, State: bool):
        ExecuteUbergraph_Widget_TrainStationNew.K2Node_CustomEvent_state = State #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_TrainStationNew(1029)
    

    def BndEvt__mStationNameInput_K2Node_ComponentBoundEvent_1_OnEditableTextChangedEvent__DelegateSignature(self, text: Const[Ref[FText]]):
        ExecuteUbergraph_Widget_TrainStationNew.K2Node_ComponentBoundEvent_Text = text #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_TrainStationNew(1044)
    

    def AutoScrollInfoMessage(self):
        self.ExecuteUbergraph_Widget_TrainStationNew(1645)
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_TrainStationNew(1736)
    

    def ExecuteUbergraph_Widget_TrainStationNew(self):
        goto(ComputedJump("EntryPoint"))
        self.Widget_AutoScrollingContainer.StartAutoScroll()
        # Label 51
        goto(ExecutionFlow.Pop())
        # Label 52
        self.Construct()
        OutputDelegate.BindUFunction(self, OnEscapePressed)
        self.mTrainStationWindow.OnClose.AddUnique(OutputDelegate)
        Station: Ptr[FGBuildableRailroadStation] = Cast[FGBuildableRailroadStation](self.mInteractObject)
        bSuccess: bool = Station
        if not bSuccess:
           goto(ExecutionFlow.Pop())
        self.RailroadStation = Station
        OutputDelegate1.BindUFunction(self, OnPowerChanged)
        self.RailroadStation.mOnHasPowerChanged.AddUnique(OutputDelegate1)
        self.GenerateTrainList()
        self.UpdatePowerStatus()
        self.AutoScrollInfoMessage()
        
        Name1 = None
        self.GetStationName(Ref[Name1])
        self.mStationNameInput.SetText(Name1)
        goto(ExecutionFlow.Pop())
        self.mInputMethod = CommitMethod
        self.mStationNameText = Text1
        
        StationNameIsValid = None
        self.CheckStationNameLengthAndValidity(Ref[StationNameIsValid])
        if not StationNameIsValid:
            goto('L618')
        CmpSuccess: bool = NotEqual_ByteByte(self.mInputMethod, 0)
        if not CmpSuccess:
            goto('L669')
        CmpSuccess = NotEqual_ByteByte(self.mInputMethod, 1)
        if not CmpSuccess:
            goto('L734')
        CmpSuccess = NotEqual_ByteByte(self.mInputMethod, 2)
        if not CmpSuccess:
            goto('L669')
        goto(ExecutionFlow.Pop())
        # Label 618
        self.SetStationName()
        self.mStationNameInput.SetText()
        goto(ExecutionFlow.Pop())
        
        Name = None
        # Label 669
        self.GetStationName(Ref[Name])
        self.mStationNameInput.SetText(Name)
        goto(ExecutionFlow.Pop())
        # Label 734
        self.SetStationName(self.mStationNameText)
        goto(ExecutionFlow.Pop())
        self.mActiveTrainButton = button
        self.ShowLocomotiveMenu(self.mActiveTrainButton.mTrainObject)
        goto(ExecutionFlow.Pop())
        self.mTrainStationWindow.SetVisibility(0)
        self.mLocomotiveMenuContainer.SetVisibility(1)
        self.mActiveTrainButton = None
        goto(ExecutionFlow.Pop())
        ReturnValue: FText = self.mActiveTrainButton.mTrainObject.GetTrainName()
        self.mActiveTrainButton.SetTitle(ReturnValue)
        goto(ExecutionFlow.Pop())
        self.UpdatePowerStatus()
        goto(ExecutionFlow.Pop())
        
        Text = None
        ReturnValue_0: FString = Default__KismetTextLibrary.Conv_TextToString(Ref[Text])
        ReturnValue_1: int32 = Default__KismetStringLibrary.Len(ReturnValue_0)
        ReturnValue_2: bool = ReturnValue_1 > 22
        if not ReturnValue_2:
           goto(ExecutionFlow.Pop())
        
        Text = None
        ReturnValue1: FString = Default__KismetTextLibrary.Conv_TextToString(Ref[Text])
        ReturnValue_3: FString = Default__KismetStringLibrary.GetSubstring(ReturnValue1, 0, 22)
        ReturnValue_4: FText = Default__KismetTextLibrary.Conv_StringToText(ReturnValue_3)
        self.mStationNameInput.SetText(ReturnValue_4)
        
        Text = None
        ReturnValue1 = Default__KismetTextLibrary.Conv_TextToString(Ref[Text])
        ReturnValue_3 = Default__KismetStringLibrary.GetSubstring(ReturnValue1, 0, 22)
        ReturnValue_4 = Default__KismetTextLibrary.Conv_StringToText(ReturnValue_3)
        self.SetStationName(ReturnValue_4)
        goto(ExecutionFlow.Pop())
        self.SetRandomInfoMessage()
        Default__KismetSystemLibrary.Delay(self, 0.10000000149011612, LatentActionInfo(Linkage = 15, UUID = 961414655, ExecutionFunction = "ExecuteUbergraph_Widget_TrainStationNew", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        goto('L52')
    
