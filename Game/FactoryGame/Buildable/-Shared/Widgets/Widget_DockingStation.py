
from codegen.ue4_stub import *

from Game.FactoryGame.Character.Player.BP_RemoteCallObject import BP_RemoteCallObject
from Script.FactoryGame import FGPlayerController
from Script.FactoryGame import FGCharacterPlayer
from Script.Engine import Pawn
from Script.FactoryGame import FGBuildable
from Script.Engine import Not_PreBool
from Script.Engine import HasAuthority
from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import PlayerController
from Script.Engine import Default__KismetArrayLibrary
from Script.Engine import K2_GetPawn
from Script.FactoryGame import GetInventory
from Game.FactoryGame.Interface.UI.InGame.Widget_UseableBase import Construct
from Game.FactoryGame.Buildable.-Shared.Widgets.Widget_DockingStation import ExecuteUbergraph_Widget_DockingStation.K2Node_CustomEvent_ReplicationDetailOwner
from Script.FactoryGame import FGInventoryComponent
from Game.FactoryGame.Buildable.-Shared.Widgets.Widget_DockingStation import ExecuteUbergraph_Widget_DockingStation
from Script.Engine import IsValid
from Game.FactoryGame.Buildable.-Shared.Widgets.Widget_DockingStation import ExecuteUbergraph_Widget_DockingStation.K2Node_Event_InDeltaTime
from Script.UMG import Tick
from Game.FactoryGame.Interface.UI.InGame.Widget_UseableBase import Widget_UseableBase
from Script.FactoryGame import Init
from Script.Engine import Conv_BoolToString
from Game.FactoryGame.Buildable.-Shared.Widgets.Widget_DockingStation import ExecuteUbergraph_Widget_DockingStation.K2Node_Event_MyGeometry
from Script.Engine import Default__KismetStringLibrary
from Script.UMG import ScrollToStart
from Script.FactoryGame import FGBuildableDockingStation
from Script.FactoryGame import GetRemoteCallObjectOfClass
from Script.FactoryGame import GetFuelInventory
from Game.FactoryGame.Character.Player.BP_PlayerController import BP_PlayerController
from Script.Engine import Concat_StrStr
from Script.Engine import PrintString
from Script.CoreUObject import LinearColor

class Widget_DockingStation(Widget_UseableBase):
    mDockingStation: Ptr[FGBuildableDockingStation]
    mShouldOpenInventory = True
    mUseMouse = True
    mRestoreFocusWhenLost = True
    mDesiredHorizontalAlignment = 2
    mDesiredVerticalAlignment = 2
    mCallCustomTickOnConstruct = True
    bIsFocusable = True
    bHasScriptImplementedTick = True
    
    def DropInventorySlotStack(self):
        ExecutionFlow.Push("L183")
        ExecutionFlow.Push("L98")
        
        Result = None
        self.mFuelInventory.DropOntoInventorySlot(InventorySlot, Ref[Result])
        LocalResult = Result
        if not LocalResult:
            goto('L122')
        goto(ExecutionFlow.Pop())
        # Label 98
        WasStackMoved = LocalResult
        # End
        
        Result = None
        # Label 122
        self.DropInventoryStackOnInventoryWidget(InventorySlot, self.mInventory, Ref[Result])
        LocalResult = Result
        goto(ExecutionFlow.Pop())
    

    def SetHeaderText(self):
        AsFGBuildable: Ptr[FGBuildable] = Cast[FGBuildable](self.mInteractObject)
        bSuccess: bool = AsFGBuildable
        if not bSuccess:
            goto('L146')
        self.Widget_Window_DarkMode.SetTitle(AsFGBuildable.mDisplayName)
    

    def GetLoadingModeButton(self):
        ReturnValue: bool = self.mDockingStation.GetIsInLoadMode()
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
        self.ExecuteUbergraph_Widget_DockingStation(892)
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_DockingStation(1032)
    

    def GrabAllFromStorage(self):
        self.ExecuteUbergraph_Widget_DockingStation(2258)
    

    def DumpAllInStorage(self):
        self.ExecuteUbergraph_Widget_DockingStation(2263)
    

    def BndEvt__Widget_SwitchButton_K2Node_ComponentBoundEvent_1_OnClicked__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_DockingStation(2268)
    

    def Tick(self):
        ExecuteUbergraph_Widget_DockingStation.K2Node_Event_MyGeometry = MyGeometry #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_DockingStation.K2Node_Event_InDeltaTime = InDeltaTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_DockingStation(2273)
    

    def BndEvt__Widget_Window_DarkMode_K2Node_ComponentBoundEvent_2_OnClose__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_DockingStation(2316)
    

    def BndEvt__mSortButton_K2Node_ComponentBoundEvent_0_OnClicked__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_DockingStation(2321)
    

    def OnReplicationDetailActorReplicated(self, ReplicationDetailOwner: Ptr[Actor]):
        ExecuteUbergraph_Widget_DockingStation.K2Node_CustomEvent_ReplicationDetailOwner = ReplicationDetailOwner #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_DockingStation(2613)
    

    def ExecuteUbergraph_Widget_DockingStation(self):
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
        # Label 424
        ReturnValue_2: Ptr[FGInventoryComponent] = self.mDockingStation.GetInventory()
        ReturnValue_3: bool = Default__KismetSystemLibrary.IsValid(ReturnValue_2)
        if not ReturnValue_3:
           goto(ExecutionFlow.Pop())
        ReturnValue_2 = self.mDockingStation.GetInventory()
        self.mInventory.Init(ReturnValue_2)
        ReturnValue_4: Ptr[FGInventoryComponent] = self.mDockingStation.GetFuelInventory()
        ReturnValue1: bool = Default__KismetSystemLibrary.IsValid(ReturnValue_4)
        if not ReturnValue1:
           goto(ExecutionFlow.Pop())
        ReturnValue_4 = self.mDockingStation.GetFuelInventory()
        self.mFuelInventory.mCachedInventoryComponent = ReturnValue_4
        OutputDelegate2.BindUFunction(self, OnInventorySlotStackMove)
        self.mFuelInventory.OnMoveStack.AddUnique(OutputDelegate2)
        Variable = 0
        goto('L396')
        self.Init()
        ReturnValue_5: bool = self.mDockingStation.HasAuthority()
        if not ReturnValue_5:
            goto('L963')
        goto('L424')
        # Label 963
        OutputDelegate4.BindUFunction(self, OnReplicationDetailActorReplicated)
        self.mDockingStation.OnReplicationDetailActorCreatedEvent.AddUnique(OutputDelegate4)
        goto('L424')
        self.Construct()
        self.SetHeaderText()
        Station: Ptr[FGBuildableDockingStation] = Cast[FGBuildableDockingStation](self.mInteractObject)
        bSuccess: bool = Station
        self.mDockingStation = Station
        OutputDelegate.BindUFunction(self, GrabAllFromStorage)
        self.mGrabAllButton.mButton.OnClicked.AddUnique(OutputDelegate)
        OutputDelegate1.BindUFunction(self, DumpAllInStorage)
        self.mDumpAllButton.mButton.OnClicked.AddUnique(OutputDelegate1)
        self.GetLoadingModeButton()
        goto(ExecutionFlow.Pop())
        # Label 1327
        self.OnEscapePressed()
        goto(ExecutionFlow.Pop())
        # Label 1356
        ReturnValue1_0: Ptr[FGInventoryComponent] = self.mDockingStation.GetInventory()
        self.GrabAllFromInventory(ReturnValue1_0)
        goto(ExecutionFlow.Pop())
        # Label 1422
        ReturnValue2: Ptr[FGInventoryComponent] = self.mDockingStation.GetInventory()
        self.DumpAllToInventory(ReturnValue2)
        goto(ExecutionFlow.Pop())
        # Label 1488
        ReturnValue_6: Ptr[PlayerController] = self.GetOwningPlayer()
        Controller: Ptr[BP_PlayerController] = Cast[BP_PlayerController](ReturnValue_6)
        bSuccess1: bool = Controller
        if not bSuccess1:
           goto(ExecutionFlow.Pop())
        ReturnValue_7: Ptr[BP_RemoteCallObject] = Controller.GetRemoteCallObjectOfClass(BP_RemoteCallObject)
        ReturnValue_8: bool = self.mDockingStation.GetIsInLoadMode()
        ReturnValue_9: bool = Not_PreBool(ReturnValue_8)
        ReturnValue_7.Server_SetLoadModeOnDockingStation(self.mDockingStation, ReturnValue_9)
        self.GetLoadingModeButton()
        ReturnValue_8 = self.mDockingStation.GetIsInLoadMode()
        ReturnValue_10: FString = Default__KismetStringLibrary.Conv_BoolToString(ReturnValue_8)
        ReturnValue_9 = Not_PreBool(ReturnValue_8)
        ReturnValue_11: FString = Default__KismetStringLibrary.Concat_StrStr("load", ReturnValue_10)
        ReturnValue1_1: FString = Default__KismetStringLibrary.Conv_BoolToString(ReturnValue_9)
        ReturnValue1_2: FString = Default__KismetStringLibrary.Concat_StrStr(ReturnValue_11, "unload")
        ReturnValue2_0: FString = Default__KismetStringLibrary.Concat_StrStr(ReturnValue1_2, ReturnValue1_1)
        Default__KismetSystemLibrary.PrintString(self, ReturnValue2_0, True, True, LinearColor(R = 0, G = 0.6600000262260437, B = 1, A = 1), 2)
        goto(ExecutionFlow.Pop())
        goto('L1356')
        goto('L1422')
        goto('L1488')
        self.Tick(MyGeometry, InDeltaTime)
        self.GetLoadingModeButton()
        goto(ExecutionFlow.Pop())
        goto('L1327')
        ReturnValue1_3: Ptr[PlayerController] = self.GetOwningPlayer()
        Controller_0: Ptr[FGPlayerController] = Cast[FGPlayerController](ReturnValue1_3)
        bSuccess2: bool = Controller_0
        if not bSuccess2:
           goto(ExecutionFlow.Pop())
        ReturnValue3: Ptr[FGInventoryComponent] = self.mDockingStation.GetInventory()
        ReturnValue1_4: Ptr[BP_RemoteCallObject] = Controller_0.GetRemoteCallObjectOfClass(BP_RemoteCallObject)
        ReturnValue1_4.Server_SortInventory(ReturnValue3)
        self.Widget_Scrollbox.mScrollBox.ScrollToStart()
        goto(ExecutionFlow.Pop())
        goto('L424')
    
