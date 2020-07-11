
from codegen.ue4_stub import *

from Game.FactoryGame.Character.Player.BP_RemoteCallObject import BP_RemoteCallObject
from Game.FactoryGame.Buildable.-Shared.Widgets.BPW_Train_DockingStation_Fluid import ExecuteUbergraph_BPW_Train_DockingStation_Fluid.K2Node_Event_MyGeometry
from Script.FactoryGame import GetInflowRate
from Script.FactoryGame import FGPlayerController
from Script.FactoryGame import FGCharacterPlayer
from Script.FactoryGame import BreakInventoryStack
from Script.Engine import Pawn
from Script.FactoryGame import FGBuildable
from Script.FactoryGame import Default__FGInventoryLibrary
from Game.FactoryGame.Buildable.-Shared.Widgets.BPW_Train_DockingStation_Fluid import ExecuteUbergraph_BPW_Train_DockingStation_Fluid.K2Node_Event_InDeltaTime
from Script.Engine import Not_PreBool
from Game.FactoryGame.Buildable.-Shared.Widgets.BPW_Train_DockingStation_Fluid import ExecuteUbergraph_BPW_Train_DockingStation_Fluid
from Script.Engine import HasAuthority
from Script.Engine import Default__KismetSystemLibrary
from Game.FactoryGame.Buildable.-Shared.Widgets.BPW_Train_DockingStation_Fluid import ExecuteUbergraph_BPW_Train_DockingStation_Fluid.K2Node_CustomEvent_replicationDetailActorOwner
from Script.Engine import PlayerController
from Script.FactoryGame import GetAmountConvertedByForm
from Script.Engine import K2_GetPawn
from Script.FactoryGame import GetOutflowRate
from Script.FactoryGame import GetInventory
from Game.FactoryGame.Interface.UI.InGame.Widget_UseableBase import Construct
from Script.FactoryGame import FGInventoryComponent
from Game.FactoryGame.Buildable.-Shared.Widgets.BPW_Train_DockingStation_Fluid import ExecuteUbergraph_BPW_Train_DockingStation_Fluid.K2Node_ComponentBoundEvent_FlushNetwork
from Script.UMG import Tick
from Game.FactoryGame.Interface.UI.InGame.Widget_UseableBase import Widget_UseableBase
from Script.Engine import PrintString
from Script.FactoryGame import Init
from Script.FactoryGame import GetScaledFluidStackSize
from Script.FactoryGame import FGBuildableTrainPlatformCargo
from Script.FactoryGame import GetRemoteCallObjectOfClass
from Script.FactoryGame import GetStackFromIndex
from Script.FactoryGame import FGItemDescriptor
from Game.FactoryGame.Buildable.-Shared.Widgets.BPW_Train_DockingStation_Fluid import ExecuteUbergraph_BPW_Train_DockingStation_Fluid.K2Node_ComponentBoundEvent_DrainDuration
from Game.FactoryGame.Character.Player.BP_PlayerController import BP_PlayerController
from Script.FactoryGame import BreakInventoryItem
from Script.FactoryGame import RemoveAllFromIndex
from Script.CoreUObject import LinearColor

class BPW_Train_DockingStation_Fluid(Widget_UseableBase):
    mTrainPlatformCargo: Ptr[FGBuildableTrainPlatformCargo]
    mCurrentFluidClass: TSubclassOf[FGItemDescriptor]
    mFlushing: bool
    mMaxStackSize: float
    mLatestFluidAmount: float
    mUseMouse = True
    mCaptureInput = True
    mRestoreFocusWhenLost = True
    mDesiredHorizontalAlignment = 2
    mDesiredVerticalAlignment = 2
    mCustomTickRate = 0.10000000149011612
    mCallCustomTickOnConstruct = True
    bIsFocusable = True
    bHasScriptImplementedTick = True
    
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
        self.ExecuteUbergraph_BPW_Train_DockingStation_Fluid(1702)
    

    def Construct(self):
        self.ExecuteUbergraph_BPW_Train_DockingStation_Fluid(43)
    

    def GrabAllFromStorage(self):
        self.ExecuteUbergraph_BPW_Train_DockingStation_Fluid(894)
    

    def DumpAllInStorage(self):
        self.ExecuteUbergraph_BPW_Train_DockingStation_Fluid(899)
    

    def BndEvt__Widget_SwitchButton_K2Node_ComponentBoundEvent_1_OnClicked__DelegateSignature(self):
        self.ExecuteUbergraph_BPW_Train_DockingStation_Fluid(904)
    

    def Tick(self):
        ExecuteUbergraph_BPW_Train_DockingStation_Fluid.K2Node_Event_MyGeometry = MyGeometry #  PERSISTENT_FRAME(
        ExecuteUbergraph_BPW_Train_DockingStation_Fluid.K2Node_Event_InDeltaTime = InDeltaTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BPW_Train_DockingStation_Fluid(909)
    

    def BndEvt__Widget_Window_DarkMode_K2Node_ComponentBoundEvent_2_OnClose__DelegateSignature(self):
        self.ExecuteUbergraph_BPW_Train_DockingStation_Fluid(1677)
    

    def OnReplicationDetailActorReplicated(self, replicationDetailActorOwner: Ptr[Actor]):
        ExecuteUbergraph_BPW_Train_DockingStation_Fluid.K2Node_CustomEvent_replicationDetailActorOwner = replicationDetailActorOwner #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BPW_Train_DockingStation_Fluid(1697)
    

    def BndEvt__BPW_PipeModule_K2Node_ComponentBoundEvent_4_OnFlush__DelegateSignature(self, FlushNetwork: bool, DrainDuration: float):
        ExecuteUbergraph_BPW_Train_DockingStation_Fluid.K2Node_ComponentBoundEvent_FlushNetwork = FlushNetwork #  PERSISTENT_FRAME(
        ExecuteUbergraph_BPW_Train_DockingStation_Fluid.K2Node_ComponentBoundEvent_DrainDuration = DrainDuration #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BPW_Train_DockingStation_Fluid(1791)
    

    def BndEvt__BPW_PipeModule_K2Node_ComponentBoundEvent_0_OnDrainCompleted__DelegateSignature(self):
        self.ExecuteUbergraph_BPW_Train_DockingStation_Fluid(1807)
    

    def ExecuteUbergraph_BPW_Train_DockingStation_Fluid(self):
        # Label 10
        self.OnEscapePressed()
        # End
        self.Construct()
        self.SetHeaderText()
        Cargo: Ptr[FGBuildableTrainPlatformCargo] = Cast[FGBuildableTrainPlatformCargo](self.mInteractObject)
        bSuccess: bool = Cargo
        if not bSuccess:
            goto('L1899')
        # Label 146
        self.mTrainPlatformCargo = Cargo
        self.GetLoadingModeButton()
        ReturnValue: int32 = self.mTrainPlatformCargo.GetScaledFluidStackSize()
        ReturnValue1: float = Default__FGInventoryLibrary.GetAmountConvertedByForm(ReturnValue, 2)
        self.mMaxStackSize = ReturnValue1
        # End
        # Label 322
        ReturnValue_0: Ptr[FGInventoryComponent] = self.mTrainPlatformCargo.GetInventory()
        self.GrabAllFromInventory(ReturnValue_0)
        # End
        # Label 392
        ReturnValue1_0: Ptr[FGInventoryComponent] = self.mTrainPlatformCargo.GetInventory()
        self.DumpAllToInventory(ReturnValue1_0)
        # End
        # Label 462
        ReturnValue_1: bool = self.mTrainPlatformCargo.HasAuthority()
        if not ReturnValue_1:
            goto('L523')
        # End
        # Label 523
        OutputDelegate.BindUFunction(self, OnReplicationDetailActorReplicated)
        self.mTrainPlatformCargo.OnReplicationDetailActorCreatedEvent.AddUnique(OutputDelegate)
        # End
        # Label 592
        ReturnValue_2: Ptr[PlayerController] = self.GetOwningPlayer()
        Controller: Ptr[BP_PlayerController] = Cast[BP_PlayerController](ReturnValue_2)
        bSuccess1: bool = Controller
        if not bSuccess1:
            goto('L1899')
        ReturnValue_3: bool = self.mTrainPlatformCargo.GetIsInLoadMode()
        ReturnValue_4: Ptr[BP_RemoteCallObject] = Controller.GetRemoteCallObjectOfClass(BP_RemoteCallObject)
        ReturnValue_5: bool = Not_PreBool(ReturnValue_3)
        ReturnValue_4.Server_SetLoadModeOnTrainCargoPlatform(self.mTrainPlatformCargo, ReturnValue_5)
        self.GetLoadingModeButton()
        # End
        goto('L322')
        goto('L392')
        goto('L592')
        self.Tick(MyGeometry, InDeltaTime)
        self.GetLoadingModeButton()
        ReturnValue1_1: bool = Not_PreBool(self.mFlushing)
        if not ReturnValue1_1:
            goto('L1603')
        ReturnValue2: Ptr[FGInventoryComponent] = self.mTrainPlatformCargo.GetInventory()
        
        stack = None
        ReturnValue_6: bool = ReturnValue2.GetStackFromIndex(0, Ref[stack])
        
        stack = None
        numItems = None
        item = None
        Default__FGInventoryLibrary.BreakInventoryStack(Ref[stack], Ref[numItems], Ref[item])
        
        item = None
        itemClass = None
        itemState = None
        Default__FGInventoryLibrary.BreakInventoryItem(Ref[item], Ref[itemClass], Ref[itemState])
        self.mCurrentFluidClass = itemClass
        
        stack = None
        numItems = None
        item = None
        Default__FGInventoryLibrary.BreakInventoryStack(Ref[stack], Ref[numItems], Ref[item])
        ReturnValue_7: float = Default__FGInventoryLibrary.GetAmountConvertedByForm(numItems, 2)
        self.mLatestFluidAmount = ReturnValue_7
        ReturnValue_8: float = self.mTrainPlatformCargo.GetInflowRate()
        ReturnValue_9: float = self.mTrainPlatformCargo.GetOutflowRate()
        self.BPW_PipeModule.UpdateValues(self.mLatestFluidAmount, self.mMaxStackSize, ReturnValue_8, ReturnValue_9, 0)
        self.BPW_PipeModule.SetFluidType(self.mCurrentFluidClass)
        # End
        # Label 1603
        self.BPW_PipeModule.UpdateValues(self.mLatestFluidAmount, self.mMaxStackSize, 0, 0, 0)
        # End
        goto('L10')
        # Label 1682
        self.Init()
        goto('L462')
        # End
        goto('L1682')
        # Label 1707
        ReturnValue3: Ptr[FGInventoryComponent] = self.mTrainPlatformCargo.GetInventory()
        ReturnValue3.RemoveAllFromIndex(0)
        # End
        self.mFlushing = True
        goto('L1707')
        self.mFlushing = False
        Default__KismetSystemLibrary.PrintString(self, "Hello", True, True, LinearColor(R = 0, G = 0.6600000262260437, B = 1, A = 1), 2)
    
