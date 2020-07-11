
from codegen.ue4_stub import *

from Game.FactoryGame.Character.Player.BP_RemoteCallObject import BP_RemoteCallObject
from Script.AkAudio import PostAkEvent
from Script.FactoryGame import FGPlayerController
from Script.FactoryGame import FGCharacterPlayer
from Script.Engine import Pawn
from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import PlayerController
from Script.Engine import K2_GetPawn
from Game.FactoryGame.Buildable.-Shared.Widgets.Widget_Storage import ExecuteUbergraph_Widget_Storage
from Game.FactoryGame.Buildable.-Shared.Widgets.Widget_Storage import ExecuteUbergraph_Widget_Storage.K2Node_CustomEvent_replicationDetailActorOwner
from Script.FactoryGame import GetInventory
from Game.FactoryGame.Interface.UI.InGame.Widget_UseableBase import Construct
from Script.FactoryGame import FGInventoryComponent
from Script.Engine import IsValid
from Game.FactoryGame.Interface.UI.Audio.ItemTransfer.Play_UI_GrabAllDumpAll import Play_UI_GrabAllDumpAll
from Game.FactoryGame.Interface.UI.InGame.Widget_UseableBase import Widget_UseableBase
from Script.FactoryGame import Init
from Script.AkAudio import Default__AkGameplayStatics
from Script.UMG import ScrollToStart
from Script.FactoryGame import GetRemoteCallObjectOfClass
from Script.UMG import GetOwningPlayerPawn
from Script.FactoryGame import FGBuildableStorage
from Game.FactoryGame.Interface.UI.InGame.Widget_UseableBase import Destruct
from Script.FactoryGame import GetStorageInventory
from Script.AkAudio import AkComponent

class Widget_Storage(Widget_UseableBase):
    mStorageActor: Ptr[FGBuildableStorage]
    mInventoryComponent: Ptr[FGInventoryComponent]
    mShouldOpenInventory = True
    mUseKeyboard = True
    mUseMouse = True
    mCaptureInput = True
    mRestoreFocusWhenLost = True
    mInputToPassThrough = ['Use']
    mDesiredHorizontalAlignment = 2
    mDesiredVerticalAlignment = 2
    mUseGamepadCursor = True
    mCallCustomTickOnConstruct = True
    
    def SetInventoryComp(self, InventoryComp: Ptr[FGInventoryComponent]):
        self.mInventoryComponent = InventoryComp
        self.mInventory.Init(self.mInventoryComponent)
        self.InitInventoryWidgetCallbacks(self.mInventory)
    

    def OnSortClicked(self):
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        Controller: Ptr[FGPlayerController] = Cast[FGPlayerController](ReturnValue)
        bSuccess: bool = Controller
        if not bSuccess:
            goto('L253')
        ReturnValue_0: Ptr[BP_RemoteCallObject] = Controller.GetRemoteCallObjectOfClass(BP_RemoteCallObject)
        ReturnValue_0.Server_SortInventory(self.mInventoryComponent)
        self.Widget_Scrollbox.mScrollBox.ScrollToStart()
    

    def OnDumpAllClicked(self):
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
        ReturnValue_1.Server_GrabAllItemsFromInventory(ReturnValue_2, self.mInventoryComponent, None)
    

    def OnGrabAllClicked(self):
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
        ReturnValue_1.Server_GrabAllItemsFromInventory(self.mInventoryComponent, ReturnValue_2, None)
    

    def BindStorageButtons(self):
        OutputDelegate1.BindUFunction(self, DumpAllInStorage)
        self.mDumpAllButton.mButton.OnClicked.AddUnique(OutputDelegate1)
        OutputDelegate.BindUFunction(self, GrabAllFromStorage)
        self.mGrabAllButton.mButton.OnClicked.AddUnique(OutputDelegate)
    

    def DropInventorySlotStack(self):
        
        Result = None
        self.DropInventoryStackOnInventoryWidget(InventorySlot, self.mInventory, Ref[Result])
        WasStackMoved = Result
    

    def Cleanup(self):
        self.mGrabAllButton.mButton.OnClicked.Clear()
        self.Widget_Window_DarkMode.OnClose.Clear()
    

    def Init(self):
        self.ExecuteUbergraph_Widget_Storage(10)
    

    def Destruct(self):
        self.ExecuteUbergraph_Widget_Storage(541)
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_Storage(570)
    

    def DumpAllInStorage(self):
        self.ExecuteUbergraph_Widget_Storage(663)
    

    def GrabAllFromStorage(self):
        self.ExecuteUbergraph_Widget_Storage(763)
    

    def BndEvt__mSortButton_K2Node_ComponentBoundEvent_0_OnClicked__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_Storage(782)
    

    def OnInventoryComponentReplicated(self, replicationDetailActorOwner: Ptr[Actor]):
        ExecuteUbergraph_Widget_Storage.K2Node_CustomEvent_replicationDetailActorOwner = replicationDetailActorOwner #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_Storage(801)
    

    def ExecuteUbergraph_Widget_Storage(self):
        self.Init()
        Storage: Ptr[FGBuildableStorage] = Cast[FGBuildableStorage](self.mInteractObject)
        bSuccess1: bool = Storage
        if not bSuccess1:
            goto('L295')
        self.mStorageActor = Storage
        ReturnValue1: Ptr[FGInventoryComponent] = self.mStorageActor.GetStorageInventory()
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(ReturnValue1)
        if not ReturnValue:
            goto('L402')
        ReturnValue1 = self.mStorageActor.GetStorageInventory()
        self.SetInventoryComp(ReturnValue1)
        # End
        # Label 295
        Component: Ptr[FGInventoryComponent] = Cast[FGInventoryComponent](self.mInteractObject)
        bSuccess: bool = Component
        if not bSuccess:
            goto('L806')
        self.SetInventoryComp(Component)
        # End
        # Label 402
        OutputDelegate1.BindUFunction(self, OnInventoryComponentReplicated)
        self.mStorageActor.OnReplicationDetailActorCreatedEvent.AddUnique(OutputDelegate1)
        # End
        # Label 471
        ReturnValue_0: Ptr[FGInventoryComponent] = self.mStorageActor.GetStorageInventory()
        self.SetInventoryComp(ReturnValue_0)
        # End
        self.Destruct()
        self.Cleanup()
        # End
        self.Construct()
        OutputDelegate.BindUFunction(self, OnEscapePressed)
        self.Widget_Window_DarkMode.OnClose.AddUnique(OutputDelegate)
        self.BindStorageButtons()
        # End
        self.OnDumpAllClicked()
        # Label 677
        ReturnValue_1: Ptr[Pawn] = self.GetOwningPlayerPawn()
        ReturnValue_2: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_UI_GrabAllDumpAll, ReturnValue_1, True)
        # End
        self.OnGrabAllClicked()
        goto('L677')
        self.OnSortClicked()
        # End
        goto('L471')
    
