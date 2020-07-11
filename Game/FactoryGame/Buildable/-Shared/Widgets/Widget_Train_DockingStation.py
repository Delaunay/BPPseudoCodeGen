
from codegen.ue4_stub import *

from Game.FactoryGame.Character.Player.BP_RemoteCallObject import BP_RemoteCallObject
from Script.FactoryGame import FGPlayerController
from Script.FactoryGame import FGCharacterPlayer
from Script.Engine import Pawn
from Script.FactoryGame import FGBuildable
from Script.Engine import Not_PreBool
from Script.Engine import HasAuthority
from Script.Engine import PlayerController
from Script.Engine import Default__KismetArrayLibrary
from Script.Engine import K2_GetPawn
from Script.FactoryGame import GetInventory
from Game.FactoryGame.Interface.UI.InGame.Widget_UseableBase import Construct
from Script.FactoryGame import FGInventoryComponent
from Game.FactoryGame.Buildable.-Shared.Widgets.Widget_Train_DockingStation import ExecuteUbergraph_Widget_Train_DockingStation.K2Node_Event_MyGeometry
from Script.UMG import Tick
from Game.FactoryGame.Interface.UI.InGame.Widget_UseableBase import Widget_UseableBase
from Script.FactoryGame import Init
from Game.FactoryGame.Buildable.-Shared.Widgets.Widget_Train_DockingStation import ExecuteUbergraph_Widget_Train_DockingStation
from Game.FactoryGame.Buildable.-Shared.Widgets.Widget_Train_DockingStation import ExecuteUbergraph_Widget_Train_DockingStation.K2Node_Event_InDeltaTime
from Game.FactoryGame.Buildable.-Shared.Widgets.Widget_Train_DockingStation import ExecuteUbergraph_Widget_Train_DockingStation.K2Node_CustomEvent_replicationDetailActorOwner
from Script.FactoryGame import FGBuildableTrainPlatformCargo
from Script.FactoryGame import GetRemoteCallObjectOfClass
from Script.UMG import ScrollToStart
from Game.FactoryGame.Character.Player.BP_PlayerController import BP_PlayerController

class Widget_Train_DockingStation(Widget_UseableBase):
    mTrainPlatformCargo: Ptr[FGBuildableTrainPlatformCargo]
    mShouldOpenInventory = True
    mUseMouse = True
    mRestoreFocusWhenLost = True
    mDesiredHorizontalAlignment = 2
    mDesiredVerticalAlignment = 2
    mCallCustomTickOnConstruct = True
    bIsFocusable = True
    bHasScriptImplementedTick = True
    
    def DropInventorySlotStack(self):
        
        Result = None
        self.DropInventoryStackOnInventoryWidget(InventorySlot, self.mInventory, Ref[Result])
        WasStackMoved = Result
    

    def SetHeaderText(self):
        AsFGBuildable: Ptr[FGBuildable] = Cast[FGBuildable](self.mInteractObject)
        bSuccess: bool = AsFGBuildable
        if not bSuccess:
            goto('L146')
        self.Widget_Window_DarkMode.SetTitle(AsFGBuildable.mDisplayName)
    

    def GetLoadingModeButton(self):
        ReturnValue: bool = self.mTrainPlatformCargo.GetIsInLoadMode()
        self.Widget_SwitchButton.SetButtonBrush(ReturnValue)
    

    def DumpAllToInventory(self, SourceComponent: Ptr[FGInventoryComponent]):
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        Controller: Ptr[FGPlayerController] = Cast[FGPlayerController](ReturnValue)
        bSuccess: bool = Controller
        if not bSuccess:
            goto('L372')
        ReturnValue_0: Ptr[Pawn] = Controller.K2_GetPawn()
        Player: Ptr[FGCharacterPlayer] = Cast[FGCharacterPlayer](ReturnValue_0)
        bSuccess1: bool = Player
        if not bSuccess1:
            goto('L372')
        ReturnValue_1: Ptr[BP_RemoteCallObject] = Controller.GetRemoteCallObjectOfClass(BP_RemoteCallObject)
        ReturnValue_2: Ptr[FGInventoryComponent] = Player.GetInventory()
        ReturnValue_1.Server_GrabAllItemsFromInventory(ReturnValue_2, SourceComponent, None)
    

    def GrabAllFromInventory(self, SourceComponent: Ptr[FGInventoryComponent]):
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        Controller: Ptr[FGPlayerController] = Cast[FGPlayerController](ReturnValue)
        bSuccess: bool = Controller
        if not bSuccess:
            goto('L372')
        ReturnValue_0: Ptr[Pawn] = Controller.K2_GetPawn()
        Player: Ptr[FGCharacterPlayer] = Cast[FGCharacterPlayer](ReturnValue_0)
        bSuccess1: bool = Player
        if not bSuccess1:
            goto('L372')
        ReturnValue_1: Ptr[BP_RemoteCallObject] = Controller.GetRemoteCallObjectOfClass(BP_RemoteCallObject)
        ReturnValue_2: Ptr[FGInventoryComponent] = Player.GetInventory()
        ReturnValue_1.Server_GrabAllItemsFromInventory(SourceComponent, ReturnValue_2, None)
    

    def Init(self):
        self.ExecuteUbergraph_Widget_Train_DockingStation(424)
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_Train_DockingStation(674)
    

    def GrabAllFromStorage(self):
        self.ExecuteUbergraph_Widget_Train_DockingStation(1434)
    

    def DumpAllInStorage(self):
        self.ExecuteUbergraph_Widget_Train_DockingStation(1439)
    

    def BndEvt__Widget_SwitchButton_K2Node_ComponentBoundEvent_1_OnClicked__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_Train_DockingStation(1444)
    

    def Tick(self):
        ExecuteUbergraph_Widget_Train_DockingStation.K2Node_Event_MyGeometry = MyGeometry #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_Train_DockingStation.K2Node_Event_InDeltaTime = InDeltaTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_Train_DockingStation(1449)
    

    def BndEvt__Widget_Window_DarkMode_K2Node_ComponentBoundEvent_2_OnClose__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_Train_DockingStation(1492)
    

    def BndEvt__mSortButton_K2Node_ComponentBoundEvent_0_OnClicked__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_Train_DockingStation(1497)
    

    def OnReplicationDetailActorReplicated(self, replicationDetailActorOwner: Ptr[Actor]):
        ExecuteUbergraph_Widget_Train_DockingStation.K2Node_CustomEvent_replicationDetailActorOwner = replicationDetailActorOwner #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_Train_DockingStation(1789)
    

    def ExecuteUbergraph_Widget_Train_DockingStation(self):
        goto(ComputedJump("EntryPoint"))
        # Label 15
        ExecutionFlow.Push("L166")
        OutputDelegate3.BindUFunction(self, OnInventorySlotStackMove)
        
        self.mInventory.mInventorySlots = None
        Item = None
        Item = self.mInventory.mInventorySlots[Variable]
        Item.OnMoveStack.AddUnique(OutputDelegate3)
        goto(ExecutionFlow.Pop())
        # Label 166
        ReturnValue: int32 = Variable + 1
        Variable: int32 = ReturnValue
        
        self.mInventory.mInventorySlots = None
        # Label 235
        ReturnValue_0: int32 = len(self.mInventory.mInventorySlots)
        ReturnValue_1: bool = Variable <= ReturnValue_0
        if not ReturnValue_1:
           goto(ExecutionFlow.Pop())
        Variable = Variable
        goto('L15')
        # Label 396
        Variable = 0
        goto('L235')
        self.Init()
        ReturnValue_2: bool = self.mTrainPlatformCargo.HasAuthority()
        if not ReturnValue_2:
            goto('L605')
        # Label 490
        ReturnValue2: Ptr[FGInventoryComponent] = self.mTrainPlatformCargo.GetInventory()
        self.mInventory.Init(ReturnValue2)
        Variable = 0
        goto('L396')
        # Label 605
        OutputDelegate.BindUFunction(self, OnReplicationDetailActorReplicated)
        self.mTrainPlatformCargo.OnReplicationDetailActorCreatedEvent.AddUnique(OutputDelegate)
        goto('L490')
        self.Construct()
        self.SetHeaderText()
        Cargo: Ptr[FGBuildableTrainPlatformCargo] = Cast[FGBuildableTrainPlatformCargo](self.mInteractObject)
        bSuccess: bool = Cargo
        if not bSuccess:
           goto(ExecutionFlow.Pop())
        self.mTrainPlatformCargo = Cargo
        OutputDelegate1.BindUFunction(self, GrabAllFromStorage)
        self.mGrabAllButton.mButton.OnClicked.AddUnique(OutputDelegate1)
        OutputDelegate2.BindUFunction(self, DumpAllInStorage)
        self.mDumpAllButton.mButton.OnClicked.AddUnique(OutputDelegate2)
        self.GetLoadingModeButton()
        goto(ExecutionFlow.Pop())
        # Label 979
        self.OnEscapePressed()
        goto(ExecutionFlow.Pop())
        # Label 1008
        ReturnValue_3: Ptr[FGInventoryComponent] = self.mTrainPlatformCargo.GetInventory()
        self.GrabAllFromInventory(ReturnValue_3)
        goto(ExecutionFlow.Pop())
        # Label 1074
        ReturnValue1: Ptr[FGInventoryComponent] = self.mTrainPlatformCargo.GetInventory()
        self.DumpAllToInventory(ReturnValue1)
        goto(ExecutionFlow.Pop())
        # Label 1140
        ReturnValue_4: Ptr[PlayerController] = self.GetOwningPlayer()
        Controller: Ptr[BP_PlayerController] = Cast[BP_PlayerController](ReturnValue_4)
        bSuccess1: bool = Controller
        if not bSuccess1:
           goto(ExecutionFlow.Pop())
        ReturnValue_5: bool = self.mTrainPlatformCargo.GetIsInLoadMode()
        ReturnValue_6: Ptr[BP_RemoteCallObject] = Controller.GetRemoteCallObjectOfClass(BP_RemoteCallObject)
        ReturnValue_7: bool = Not_PreBool(ReturnValue_5)
        ReturnValue_6.Server_SetLoadModeOnTrainCargoPlatform(self.mTrainPlatformCargo, ReturnValue_7)
        self.GetLoadingModeButton()
        goto(ExecutionFlow.Pop())
        goto('L1008')
        goto('L1074')
        goto('L1140')
        self.Tick(MyGeometry, InDeltaTime)
        self.GetLoadingModeButton()
        goto(ExecutionFlow.Pop())
        goto('L979')
        ReturnValue1_0: Ptr[PlayerController] = self.GetOwningPlayer()
        Controller_0: Ptr[FGPlayerController] = Cast[FGPlayerController](ReturnValue1_0)
        bSuccess2: bool = Controller_0
        if not bSuccess2:
           goto(ExecutionFlow.Pop())
        ReturnValue3: Ptr[FGInventoryComponent] = self.mTrainPlatformCargo.GetInventory()
        ReturnValue1_1: Ptr[BP_RemoteCallObject] = Controller_0.GetRemoteCallObjectOfClass(BP_RemoteCallObject)
        ReturnValue1_1.Server_SortInventory(ReturnValue3)
        self.Widget_Scrollbox.mScrollBox.ScrollToStart()
        goto(ExecutionFlow.Pop())
        goto('L490')
    
