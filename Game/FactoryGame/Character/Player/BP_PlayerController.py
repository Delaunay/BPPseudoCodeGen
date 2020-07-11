
from codegen.ue4_stub import *

from Script.Engine import FinishSpawningActor
from Game.FactoryGame.Character.Player.BP_PlayerController import ExecuteUbergraph_BP_PlayerController.K2Node_InputActionEvent_Key2
from Script.FactoryGame import FGCharacterPlayer
from Script.Engine import GetTransform
from Script.CoreUObject import Rotator
from Script.FactoryGame import OnMenuEnterDone
from Script.UMG import AddChild
from Script.Engine import Default__KismetSystemLibrary
from Script.FactoryGame import FGAudioMessage
from Script.FactoryGame import GetDisabledInputGate
from Script.Engine import IsValid
from Script.FactoryGame import HasEnoughSpaceForStacks
from Game.FactoryGame.Interface.UI.InGame.Widget_PhotoMode import Widget_PhotoMode
from Game.FactoryGame.Character.Player.BP_PlayerController import ExecuteUbergraph_BP_PlayerController
from Script.FactoryGame import FGPopupWidget
from Script.FactoryGame import ShowRespawnUI
from Game.FactoryGame.Interface.UI.HUDHelpers.HUDHelpers import Default__HUDHelpers
from Script.FactoryGame import GetIsPhotoMode
from Script.FactoryGame import ToggleHiResPhotoMode
from Script.UMG import Create
from Script.FactoryGame import InventoryItem
from Script.FactoryGame import GetScreenshotPath
from Game.FactoryGame.Equipment.-Shared.Audio.Play_Camera_SnapShot import Play_Camera_SnapShot
from Game.FactoryGame.Character.Player.BP_PlayerController import ExecuteUbergraph_BP_PlayerController.K2Node_InputActionEvent_Key11
from Script.FactoryGame import Default__FGUnlockSubsystem
from Script.CoreUObject import LinearColor
from Game.FactoryGame.Character.Player.BP_PlayerController import ExecuteUbergraph_BP_PlayerController.K2Node_Event_DeltaSeconds
from Script.FactoryGame import MakeInventoryStack
from Script.FactoryGame import FGPlayerController
from Script.Engine import Pawn
from Script.Engine import GreaterEqual_IntInt
from Script.FactoryGame import IsRagdolled
from Game.FactoryGame.Character.Player.BP_PlayerController import ExecuteUbergraph_BP_PlayerController.K2Node_InputActionEvent_Key3
from Script.Engine import HUD
from Script.UMG import SetInputMode_GameOnly
from Game.FactoryGame.Character.Player.BP_PlayerController import ExecuteUbergraph_BP_PlayerController.K2Node_InputActionEvent_Key13
from Script.Engine import SelectFloat
from Script.Engine import Default__KismetArrayLibrary
from Script.Engine import IsLocalPlayerController
from Script.FactoryGame import GetInventory
from Script.FactoryGame import DisabledInputGate
from Game.FactoryGame.Character.Player.BP_PlayerController import ExecuteUbergraph_BP_PlayerController.K2Node_InputActionEvent_Key1
from Script.FactoryGame import FGInventoryComponent
from Script.Engine import GetHUD
from Script.FactoryGame import GetPopup
from Game.FactoryGame.Character.Player.BP_PlayerController import ExecuteUbergraph_BP_PlayerController.K2Node_InputActionEvent_Key7
from Game.FactoryGame.Resource.Equipment.PortableMiner.BP_ItemDescriptorPortableMiner import BP_ItemDescriptorPortableMiner
from Game.FactoryGame.Character.Player.BP_PlayerController import ExecuteUbergraph_BP_PlayerController.K2Node_InputActionEvent_Key14
from Game.FactoryGame.Character.Player.BP_PlayerController import ExecuteUbergraph_BP_PlayerController.K2Node_InputActionEvent_Key4
from Script.FactoryGame import FGInteractWidget
from Script.FactoryGame import PopupData
from Script.AkAudio import Default__AkGameplayStatics
from Game.FactoryGame.Interface.UI.HUDHelpers.BPHUDHelpers import Default__BPHUDHelpers
from Script.FactoryGame import GetInventoryStacks
from Script.Engine import MakeTransform
from Script.Engine import IsPackagedForDistribution
from Script.FactoryGame import EnablePhotoMode
from Game.FactoryGame.Character.Player.BP_PlayerController import ExecuteUbergraph_BP_PlayerController.K2Node_InputActionEvent_Key6
from Script.FactoryGame import GetStorageInventory
from Script.UMG import AddToViewport
from Script.AkAudio import AkComponent
from Script.FactoryGame import GetHiResPhotoModeEnabled
from Script.Engine import PrintString
from Script.FactoryGame import GetDismantleInventoryReturns
from Script.Engine import GetInputAnalogStickState
from Game.FactoryGame.Character.Player.BP_PlayerController import ExecuteUbergraph_BP_PlayerController.K2Node_Event_inGolfCart
from Script.AkAudio import PostAkEvent
from Script.Engine import Delay
from Script.FactoryGame import CancelPressed
from Game.FactoryGame.Resource.Equipment.GolfCart.Desc_GolfCart import Desc_GolfCart
from Script.FactoryGame import Default__FGInventoryLibrary
from Script.FactoryGame import HasEnoughSpaceForStack
from Script.Engine import BreakTransform
from Script.UMG import PanelSlot
from Script.Engine import LatentActionInfo
from Game.FactoryGame.Character.Player.BP_PlayerController import ExecuteUbergraph_BP_PlayerController.K2Node_InputActionEvent_Key5
from Script.FactoryGame import Get
from Script.UMG import PlayAnimation
from Script.UMG import Default__WidgetBlueprintLibrary
from Script.Engine import Default__GameplayStatics
from Script.FactoryGame import Resize
from Script.Engine import BreakRotator
from Script.FactoryGame import GetGameUI
from Game.FactoryGame.Character.Player.BP_PlayerController import ExecuteUbergraph_BP_PlayerController.K2Node_InputActionEvent_Key8
from Script.FactoryGame import GetInteractWidgetStack
from Game.FactoryGame.Character.Player.BP_PlayerController import ExecuteUbergraph_BP_PlayerController.K2Node_InputActionEvent_Key
from Game.FactoryGame.Character.Player.BP_PlayerController import ExecuteUbergraph_BP_PlayerController.K2Node_InputActionEvent_Key10
from Script.FactoryGame import FGGameUI
from Game.FactoryGame.Interface.UI.Menu.PauseMenu.BP_PauseWidget import BP_PauseWidget
from Script.Engine import MakeRotator
from Game.FactoryGame.Character.Player.BP_PlayerController import ExecuteUbergraph_BP_PlayerController.K2Node_InputActionEvent_Key15
from Game.FactoryGame.Character.Player.BP_PlayerController import ExecuteUbergraph_BP_PlayerController.K2Node_Event_isJoining
from Script.FactoryGame import RagdollCharacter
from Game.FactoryGame.Character.Player.BP_PlayerController import ExecuteUbergraph_BP_PlayerController.K2Node_InputActionEvent_Key9
from Game.FactoryGame.Interface.UI.InGame.BP_GameUI import BP_GameUI
from Script.FactoryGame import GetIsMapUnlocked
from Script.FactoryGame import TogglePhotoMode
from Script.FactoryGame import CloseRespawnUI
from Script.FactoryGame import InventoryStack
from Game.FactoryGame.Interface.UI.Minimap.Widget_MapContainer import Widget_MapContainer
from Script.Engine import ReceiveBeginPlay
from Script.FactoryGame import AddStacks
from Script.Engine import Not_PreBool
from Script.Engine import K2_GetPawn
from Game.FactoryGame.-Shared.Blueprint.BP_HUD import BP_HUD
from Script.Engine import BeginDeferredActorSpawnFromClass
from Game.FactoryGame.-Shared.Crate.BP_Crate import BP_Crate
from Game.FactoryGame.Character.Player.BP_PlayerController import ExecuteUbergraph_BP_PlayerController.K2Node_InputActionEvent_Key12
from Script.FactoryGame import GetIsUsingGamepad
from Script.FactoryGame import GetCurrentAudioMessage
from Script.Engine import BooleanOR
from Script.FactoryGame import ConsolidateInventoryItems
from Script.FactoryGame import MakeInventoryItem
from Script.CoreUObject import Vector
from Script.FactoryGame import ExecuteShortcut
from Script.FactoryGame import FGHUD
from Script.Engine import GetInputMouseDelta
from Script.FactoryGame import FGUnlockSubsystem
from Game.FactoryGame.Interface.UI.InGame.Widget_SequenceHelper import Widget_SequenceHelper
from Game.FactoryGame.Character.Player.BP_PlayerController import ExecuteUbergraph_BP_PlayerController.K2Node_Event_PortableMiner
from Script.Engine import Actor
from Script.UMG import UMGSequencePlayer
from Script.Engine import ExecuteConsoleCommand
from Script.FactoryGame import SetIsUsingGamepad
from Game.FactoryGame.Character.Player.BP_PlayerController import ExecuteUbergraph_BP_PlayerController.K2Node_InputActionEvent_Key16
from Script.CoreUObject import Transform

class BP_PlayerController(FGPlayerController):
    mRespawnFadeOutTime: float = 1
    mPopupDataTest: PopupData = Namespace(Body='NSLOCTEXT("", "BE0277E2439E9972BFBBAA84158423ED", "Oh my god this is my body yeah \\\\n html here")', ID=0, Instigator={'$Empty': True}, PopupClass='/Game/FactoryGame/Interface/UI/InGame/Widget_Popup.Widget_Popup_C', PopupClosedDelegate=0, PopupConfirmClickedDelegate=0, Title='NSLOCTEXT("", "B1E331D943F98AAF5CBDF590A9A07C70", "Title here")')
    mMinimapWidget: Ptr[Widget_MapContainer]
    OnBeginTypeChat: FMulticastScriptDelegate
    PhotoModeInstructionsWidget: Ptr[Widget_PhotoMode]
    OnRespawnEnd: FMulticastScriptDelegate
    mCanAffectAudioVolumes = True
    mAttentionPingActorClass = NewObject[BP_AttentionPingActor]()
    mMapAreaCheckInterval = 0.25
    mMinPhotoModeFOV = 5
    mMaxPhotoModeFOV = 175
    mAllowedInputWhenDead = ['PrimaryFire', 'PauseGame', 'Chat']
    PlayerCameraManagerClass = NewObject[BP_PlayerCameraManager]()
    CheatClass = NewObject[BP_CheatManager]()
    TransformComponent = Namespace(ObjectClass='/Script/Engine.SceneComponent', ObjectFlags=2883617, ObjectName='TransformComponent0', bAbsoluteRotation=True)
    RootComponent = Namespace(ObjectClass='/Script/Engine.SceneComponent', ObjectFlags=2883617, ObjectName='TransformComponent0', bAbsoluteRotation=True)
    
    def DismantleGolfCart(self, GolfCart: Ptr[FGWheeledVehicle]):
        localGolfCart = GolfCart
        ReturnValue: Ptr[Pawn] = self.K2_GetPawn()
        Player: Ptr[FGCharacterPlayer] = Cast[FGCharacterPlayer](ReturnValue)
        bSuccess: bool = Player
        if not bSuccess:
            goto('L1947')
        ReturnValue1: Ptr[FGInventoryComponent] = Player.GetInventory()
        localPlayerInventory = ReturnValue1
        ReturnValue1_0: Ptr[FGInventoryComponent] = localGolfCart.GetStorageInventory()
        stacks1: List[InventoryStack] = []
        
        ReturnValue1_0.GetInventoryStacks(Ref[stacks1])
        localDismantleReturns = stacks1
        ReturnValue2: InventoryItem = Default__FGInventoryLibrary.MakeInventoryItem(Desc_GolfCart)
        ReturnValue2_0: InventoryStack = Default__FGInventoryLibrary.MakeInventoryStack(1, ReturnValue2)
        
        ReturnValue_0: int32 = localDismantleReturns.append(ReturnValue2_0)
        
        ReturnValue_1: bool = localPlayerInventory.HasEnoughSpaceForStacks(Ref[localDismantleReturns])
        if not ReturnValue_1:
            goto('L638')
        
        localPlayerInventory.AddStacks(Ref[localDismantleReturns])
        # Label 597
        localGolfCart.K2_DestroyActor()
        # End
        # Label 638
        ReturnValue1_1: InventoryItem = Default__FGInventoryLibrary.MakeInventoryItem(Desc_GolfCart)
        ReturnValue1_2: InventoryStack = Default__FGInventoryLibrary.MakeInventoryStack(1, ReturnValue1_1)
        
        ReturnValue_2: bool = localPlayerInventory.HasEnoughSpaceForStack(Ref[ReturnValue1_2])
        if not ReturnValue_2:
            goto('L1134')
        ReturnValue_3: InventoryItem = Default__FGInventoryLibrary.MakeInventoryItem(BP_ItemDescriptorPortableMiner)
        ReturnValue_4: InventoryStack = Default__FGInventoryLibrary.MakeInventoryStack(1, ReturnValue_3)
        
        ReturnValue_5: int32 = localPlayerInventory.AddStack(False, Ref[ReturnValue_4])
        ReturnValue_6: Ptr[FGInventoryComponent] = localGolfCart.GetStorageInventory()
        stacks: List[InventoryStack] = []
        
        ReturnValue_6.GetInventoryStacks(Ref[stacks])
        localDismantleReturns = stacks
        # Label 1134
        ReturnValue_7: Transform = localGolfCart.GetTransform()
        
        Location = None
        Rotation = None
        Scale = None
        BreakTransform(Ref[ReturnValue_7], Ref[Location], Ref[Rotation], Ref[Scale])
        ReturnValue_8: Vector = Location + Vector(0, 0, 100)
        ReturnValue_9: Transform = MakeTransform(ReturnValue_8, Rotator::FromPitchYawRoll(0, 0, 0), Vector(1, 1, 1))
        
        ReturnValue_10: Ptr[Actor] = Default__GameplayStatics.BeginDeferredActorSpawnFromClass(self, BP_Crate, 2, self, Ref[ReturnValue_9])
        ReturnValue_7 = localGolfCart.GetTransform()
        
        Location = None
        Rotation = None
        Scale = None
        BreakTransform(Ref[ReturnValue_7], Ref[Location], Ref[Rotation], Ref[Scale])
        ReturnValue_8 = Location + Vector(0, 0, 100)
        ReturnValue_9 = MakeTransform(ReturnValue_8, Rotator::FromPitchYawRoll(0, 0, 0), Vector(1, 1, 1))
        
        ReturnValue_11: Ptr[BP_Crate] = Default__GameplayStatics.FinishSpawningActor(ReturnValue_10, Ref[ReturnValue_9])
        
        Default__FGInventoryLibrary.ConsolidateInventoryItems(Ref[localDismantleReturns])
        
        ReturnValue_12: int32 = len(localDismantleReturns)
        ReturnValue_13: Ptr[FGInventoryComponent] = ReturnValue_11.GetInventory()
        ReturnValue_13.Resize(ReturnValue_12)
        # Label 1859
        ReturnValue_13 = ReturnValue_11.GetInventory()
        
        ReturnValue_13.AddStacks(Ref[localDismantleReturns])
        goto('L597')
    

    def OnSetupMovementWind(self):
        pass
    

    def OnDisabledInputChanged(self):
        if not self.mMinimapWidget.IsMapOpen:
            goto('L50')
        self.ToggleMiniMap()
    

    def ToggleMiniMap(self):
        ReturnValue: Ptr[FGUnlockSubsystem] = Default__FGUnlockSubsystem.Get(self)
        ReturnValue_0: bool = ReturnValue.GetIsMapUnlocked()
        if not ReturnValue_0:
            goto('L308')
        if not self.mMinimapWidget.IsMapOpen:
            goto('L224')
        Default__BPHUDHelpers.PopStackWidget(self, self.mMinimapWidget, self)
        self.mMinimapWidget.SetOpenMap(False)
        # End
        # Label 224
        Default__BPHUDHelpers.PushStackWidget(self, self.mMinimapWidget, self)
        self.mMinimapWidget.SetOpenMap(True)
    

    def DismantlePortableMiner(self, PortableMiner: Ptr[FGPortableMiner]):
        localMiner = PortableMiner
        ReturnValue: Ptr[Pawn] = self.K2_GetPawn()
        Player: Ptr[FGCharacterPlayer] = Cast[FGCharacterPlayer](ReturnValue)
        bSuccess: bool = Player
        if not bSuccess:
            goto('L1859')
        ReturnValue1: Ptr[FGInventoryComponent] = Player.GetInventory()
        localPlayerInventory = ReturnValue1
        ReturnValue1_0: List[InventoryStack] = localMiner.GetDismantleInventoryReturns()
        localDismantleReturns = ReturnValue1_0
        ReturnValue2: InventoryItem = Default__FGInventoryLibrary.MakeInventoryItem(BP_ItemDescriptorPortableMiner)
        ReturnValue2_0: InventoryStack = Default__FGInventoryLibrary.MakeInventoryStack(1, ReturnValue2)
        
        ReturnValue_0: int32 = localDismantleReturns.append(ReturnValue2_0)
        
        ReturnValue_1: bool = localPlayerInventory.HasEnoughSpaceForStacks(Ref[localDismantleReturns])
        if not ReturnValue_1:
            goto('L594')
        
        localPlayerInventory.AddStacks(Ref[localDismantleReturns])
        # Label 553
        localMiner.K2_DestroyActor()
        # End
        # Label 594
        ReturnValue1_1: InventoryItem = Default__FGInventoryLibrary.MakeInventoryItem(BP_ItemDescriptorPortableMiner)
        ReturnValue1_2: InventoryStack = Default__FGInventoryLibrary.MakeInventoryStack(1, ReturnValue1_1)
        
        ReturnValue_2: bool = localPlayerInventory.HasEnoughSpaceForStack(Ref[ReturnValue1_2])
        if not ReturnValue_2:
            goto('L1046')
        ReturnValue_3: InventoryItem = Default__FGInventoryLibrary.MakeInventoryItem(BP_ItemDescriptorPortableMiner)
        ReturnValue_4: InventoryStack = Default__FGInventoryLibrary.MakeInventoryStack(1, ReturnValue_3)
        
        ReturnValue_5: int32 = localPlayerInventory.AddStack(False, Ref[ReturnValue_4])
        ReturnValue_6: List[InventoryStack] = localMiner.GetDismantleInventoryReturns()
        localDismantleReturns = ReturnValue_6
        # Label 1046
        ReturnValue_7: Transform = localMiner.GetTransform()
        
        Location = None
        Rotation = None
        Scale = None
        BreakTransform(Ref[ReturnValue_7], Ref[Location], Ref[Rotation], Ref[Scale])
        ReturnValue_8: Vector = Location + Vector(0, 0, 100)
        ReturnValue_9: Transform = MakeTransform(ReturnValue_8, Rotator::FromPitchYawRoll(0, 0, 0), Vector(1, 1, 1))
        
        ReturnValue_10: Ptr[Actor] = Default__GameplayStatics.BeginDeferredActorSpawnFromClass(self, BP_Crate, 2, self, Ref[ReturnValue_9])
        ReturnValue_7 = localMiner.GetTransform()
        
        Location = None
        Rotation = None
        Scale = None
        BreakTransform(Ref[ReturnValue_7], Ref[Location], Ref[Rotation], Ref[Scale])
        ReturnValue_8 = Location + Vector(0, 0, 100)
        ReturnValue_9 = MakeTransform(ReturnValue_8, Rotator::FromPitchYawRoll(0, 0, 0), Vector(1, 1, 1))
        
        ReturnValue_11: Ptr[BP_Crate] = Default__GameplayStatics.FinishSpawningActor(ReturnValue_10, Ref[ReturnValue_9])
        
        Default__FGInventoryLibrary.ConsolidateInventoryItems(Ref[localDismantleReturns])
        
        ReturnValue_12: int32 = len(localDismantleReturns)
        ReturnValue_13: Ptr[FGInventoryComponent] = ReturnValue_11.GetInventory()
        ReturnValue_13.Resize(ReturnValue_12)
        ReturnValue_13 = ReturnValue_11.GetInventory()
        
        ReturnValue_13.AddStacks(Ref[localDismantleReturns])
        # Label 1854
        goto('L553')
    

    def InpActEvt_Chat_K2Node_InputActionEvent_16(self, Key: Key):
        ExecuteUbergraph_BP_PlayerController.K2Node_InputActionEvent_Key16 = Key #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_PlayerController(4563)
    

    def InpActEvt_Shortcut1_K2Node_InputActionEvent_15(self, Key: Key):
        ExecuteUbergraph_BP_PlayerController.K2Node_InputActionEvent_Key15 = Key #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_PlayerController(4027)
    

    def InpActEvt_Shortcut2_K2Node_InputActionEvent_14(self, Key: Key):
        ExecuteUbergraph_BP_PlayerController.K2Node_InputActionEvent_Key14 = Key #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_PlayerController(4022)
    

    def InpActEvt_Shortcut3_K2Node_InputActionEvent_13(self, Key: Key):
        ExecuteUbergraph_BP_PlayerController.K2Node_InputActionEvent_Key13 = Key #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_PlayerController(4017)
    

    def InpActEvt_Shortcut4_K2Node_InputActionEvent_12(self, Key: Key):
        ExecuteUbergraph_BP_PlayerController.K2Node_InputActionEvent_Key12 = Key #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_PlayerController(4012)
    

    def InpActEvt_Shortcut5_K2Node_InputActionEvent_11(self, Key: Key):
        ExecuteUbergraph_BP_PlayerController.K2Node_InputActionEvent_Key11 = Key #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_PlayerController(3983)
    

    def InpActEvt_Shortcut6_K2Node_InputActionEvent_10(self, Key: Key):
        ExecuteUbergraph_BP_PlayerController.K2Node_InputActionEvent_Key10 = Key #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_PlayerController(3958)
    

    def InpActEvt_Shortcut7_K2Node_InputActionEvent_9(self, Key: Key):
        ExecuteUbergraph_BP_PlayerController.K2Node_InputActionEvent_Key9 = Key #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_PlayerController(3773)
    

    def InpActEvt_Shortcut8_K2Node_InputActionEvent_8(self, Key: Key):
        ExecuteUbergraph_BP_PlayerController.K2Node_InputActionEvent_Key8 = Key #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_PlayerController(3599)
    

    def InpActEvt_Shortcut9_K2Node_InputActionEvent_7(self, Key: Key):
        ExecuteUbergraph_BP_PlayerController.K2Node_InputActionEvent_Key7 = Key #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_PlayerController(2530)
    

    def InpActEvt_Shortcut10_K2Node_InputActionEvent_6(self, Key: Key):
        ExecuteUbergraph_BP_PlayerController.K2Node_InputActionEvent_Key6 = Key #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_PlayerController(2156)
    

    def InpActEvt_PhotoMode_K2Node_InputActionEvent_5(self, Key: Key):
        ExecuteUbergraph_BP_PlayerController.K2Node_InputActionEvent_Key5 = Key #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_PlayerController(2145)
    

    def InpActEvt_ToggleMap_BuildGunNoSnapMode_K2Node_InputActionEvent_4(self, Key: Key):
        ExecuteUbergraph_BP_PlayerController.K2Node_InputActionEvent_Key4 = Key #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_PlayerController(2130)
    

    def InpActEvt_Prototype_RagdollPlayer_K2Node_InputActionEvent_3(self, Key: Key):
        ExecuteUbergraph_BP_PlayerController.K2Node_InputActionEvent_Key3 = Key #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_PlayerController(2009)
    

    def InpActEvt_SecondaryFire_K2Node_InputActionEvent_2(self, Key: Key):
        ExecuteUbergraph_BP_PlayerController.K2Node_InputActionEvent_Key2 = Key #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_PlayerController(1968)
    

    def InpActEvt_TogglePhotoModeUIVisibility_K2Node_InputActionEvent_1(self, Key: Key):
        ExecuteUbergraph_BP_PlayerController.K2Node_InputActionEvent_Key1 = Key #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_PlayerController(1870)
    

    def InpActEvt_PauseGame_K2Node_InputActionEvent_0(self, Key: Key):
        ExecuteUbergraph_BP_PlayerController.K2Node_InputActionEvent_Key = Key #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_PlayerController(1010)
    

    def ReceiveTick(self):
        ExecuteUbergraph_BP_PlayerController.K2Node_Event_DeltaSeconds = DeltaSeconds #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_PlayerController(4573)
    

    def OnStartRespawn(self):
        ExecuteUbergraph_BP_PlayerController.K2Node_Event_isJoining = isJoining #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_PlayerController(4568)
    

    def OnFinishRespawn(self):
        self.ExecuteUbergraph_BP_PlayerController(4177)
    

    def ReceiveBeginPlay(self):
        self.ExecuteUbergraph_BP_PlayerController(4113)
    

    def CheckAndUpdateGamepad(self):
        self.ExecuteUbergraph_BP_PlayerController(424)
    

    def Server_ForceRagdoll(self):
        self.ExecuteUbergraph_BP_PlayerController(787)
    

    def OnDisabledInputGateChanged(self):
        self.ExecuteUbergraph_BP_PlayerController(2256)
    

    def CreateSequenceList(self):
        self.ExecuteUbergraph_BP_PlayerController(2439)
    

    def TogglePhotoModeInstructionsWidget(self):
        self.ExecuteUbergraph_BP_PlayerController(3978)
    

    def PlayPhotoSound(self):
        self.ExecuteUbergraph_BP_PlayerController(4118)
    

    def TakePhoto(self):
        self.ExecuteUbergraph_BP_PlayerController(4172)
    

    def DoPause(self):
        self.ExecuteUbergraph_BP_PlayerController(4558)
    

    def OnDismantlePortableMiner(self):
        ExecuteUbergraph_BP_PlayerController.K2Node_Event_PortableMiner = PortableMiner #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_PlayerController(4730)
    

    def OnDismantleGolfCart(self):
        ExecuteUbergraph_BP_PlayerController.K2Node_Event_inGolfCart = inGolfCart #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_PlayerController(15)
    

    def ExecuteUbergraph_BP_PlayerController(self):
        goto(ComputedJump("EntryPoint"))
        self.DismantleGolfCart(inGolfCart)
        goto(ExecutionFlow.Pop())
        ReturnValue: bool = self.GetHiResPhotoModeEnabled()
        ReturnValue_0: FString = self.GetScreenshotPath(ReturnValue)
        Default__KismetSystemLibrary.ExecuteConsoleCommand(self, ReturnValue_0, self)
        self.PhotoModeInstructionsWidget.PhotoTaken()
        goto(ExecutionFlow.Pop())
        # Label 176
        Default__KismetSystemLibrary.PrintString(self, "OnStartRespawn: Completed Fade", False, True, LinearColor(R = 0, G = 0.6600000262260437, B = 1, A = 1), 2)
        self.Server_Respawn()
        ReturnValue_1: Ptr[HUD] = self.GetHUD()
        AsFGHUD: Ptr[FGHUD] = Cast[FGHUD](ReturnValue_1)
        bSuccess1: bool = AsFGHUD
        if not bSuccess1:
           goto(ExecutionFlow.Pop())
        AsFGHUD.ShowRespawnUI()
        goto(ExecutionFlow.Pop())
        ReturnValue_2: bool = self.GetIsUsingGamepad()
        if not ReturnValue_2:
            goto('L614')
        
        DeltaX = None
        DeltaY = None
        self.GetInputMouseDelta(Ref[DeltaX], Ref[DeltaY])
        ReturnValue1: bool = DeltaY > 0
        ReturnValue2: bool = DeltaX > 0
        ReturnValue_3: bool = BooleanOR(ReturnValue2, ReturnValue1)
        if not ReturnValue_3:
           goto(ExecutionFlow.Pop())
        self.SetIsUsingGamepad(False)
        goto(ExecutionFlow.Pop())
        
        StickX = None
        StickY = None
        # Label 614
        self.GetInputAnalogStickState(0, Ref[StickX], Ref[StickY])
        ReturnValue_4: bool = StickY > 0.10000000149011612
        ReturnValue3: bool = StickX > 0.10000000149011612
        ReturnValue1_0: bool = BooleanOR(ReturnValue3, ReturnValue_4)
        if not ReturnValue1_0:
           goto(ExecutionFlow.Pop())
        self.SetIsUsingGamepad(True)
        goto(ExecutionFlow.Pop())
        # Label 772
        self.CheckAndUpdateGamepad()
        goto(ExecutionFlow.Pop())
        ReturnValue_5: Ptr[Pawn] = self.K2_GetPawn()
        Player: Ptr[FGCharacterPlayer] = Cast[FGCharacterPlayer](ReturnValue_5)
        bSuccess: bool = Player
        if not bSuccess:
           goto(ExecutionFlow.Pop())
        ReturnValue_6: bool = Player.IsRagdolled()
        ReturnValue_7: bool = Not_PreBool(ReturnValue_6)
        Player.RagdollCharacter(ReturnValue_7)
        goto(ExecutionFlow.Pop())
        # Label 995
        self.Server_ForceRagdoll()
        goto(ExecutionFlow.Pop())
        ReturnValue2_0: bool = self.GetIsPhotoMode()
        if not ReturnValue2_0:
            goto('L1056')
        self.EnablePhotoMode(False)
        goto(ExecutionFlow.Pop())
        
        AsFGHUD_0 = None
        # Label 1056
        Default__BPHUDHelpers.GetFGHud(self, self, Ref[AsFGHUD_0])
        ReturnValue2_1: bool = Default__KismetSystemLibrary.IsValid(AsFGHUD_0)
        if not ReturnValue2_1:
           goto(ExecutionFlow.Pop())
        ReturnValue1_1: Ptr[FGGameUI] = AsFGHUD_0.GetGameUI()
        ReturnValue_8: Ptr[FGAudioMessage] = ReturnValue1_1.GetCurrentAudioMessage()
        ReturnValue_9: List[Ptr[FGInteractWidget]] = ReturnValue1_1.GetInteractWidgetStack()
        ReturnValue3_0: bool = Default__KismetSystemLibrary.IsValid(ReturnValue_8)
        
        ReturnValue_10: int32 = len(ReturnValue_9) - 1
        ReturnValue_11: bool = GreaterEqual_IntInt(ReturnValue_10, 0)
        ReturnValue2_2: bool = BooleanOR(ReturnValue_11, ReturnValue3_0)
        if not ReturnValue2_2:
            goto('L1569')
        ReturnValue1_1 = AsFGHUD_0.GetGameUI()
        ReturnValue1_1.CancelPressed()
        goto(ExecutionFlow.Pop())
        # Label 1569
        ReturnValue1_1 = AsFGHUD_0.GetGameUI()
        ReturnValue_12: Ptr[FGPopupWidget] = ReturnValue1_1.GetPopup()
        ReturnValue4: bool = Default__KismetSystemLibrary.IsValid(ReturnValue_12)
        if not ReturnValue4:
            goto('L1839')
        ReturnValue1_1 = AsFGHUD_0.GetGameUI()
        ReturnValue_12 = ReturnValue1_1.GetPopup()
        ReturnValue_12.OnEscapePressed()
        goto(ExecutionFlow.Pop())
        # Label 1839
        self.DoPause()
        goto(ExecutionFlow.Pop())
        # Label 1854
        self.ExecuteShortcut(0)
        goto(ExecutionFlow.Pop())
        ReturnValue1_2: bool = Default__KismetSystemLibrary.IsValid(self.PhotoModeInstructionsWidget)
        if not ReturnValue1_2:
           goto(ExecutionFlow.Pop())
        self.PhotoModeInstructionsWidget.ToggleVisibility()
        goto(ExecutionFlow.Pop())
        ReturnValue1_3: bool = self.GetIsPhotoMode()
        if not ReturnValue1_3:
           goto(ExecutionFlow.Pop())
        self.ToggleHiResPhotoMode()
        goto(ExecutionFlow.Pop())
        ReturnValue_13: bool = Default__KismetSystemLibrary.IsPackagedForDistribution()
        if not ReturnValue_13:
            goto('L995')
        goto(ExecutionFlow.Pop())
        # Label 2066
        self.ExecuteShortcut(1)
        goto(ExecutionFlow.Pop())
        # Label 2082
        self.ExecuteShortcut(2)
        goto(ExecutionFlow.Pop())
        # Label 2098
        self.ExecuteShortcut(3)
        goto(ExecutionFlow.Pop())
        # Label 2114
        self.ExecuteShortcut(4)
        goto(ExecutionFlow.Pop())
        self.ToggleMiniMap()
        goto(ExecutionFlow.Pop())
        self.TogglePhotoMode()
        goto(ExecutionFlow.Pop())
        self.ExecuteShortcut(9)
        goto(ExecutionFlow.Pop())
        # Label 2172
        self.ExecuteShortcut(5)
        goto(ExecutionFlow.Pop())
        # Label 2188
        self.ExecuteShortcut(6)
        goto(ExecutionFlow.Pop())
        # Label 2204
        self.ExecuteShortcut(7)
        goto(ExecutionFlow.Pop())
        # Label 2220
        self.ExecuteShortcut(8)
        goto(ExecutionFlow.Pop())
        # Label 2236
        self.OnBeginTypeChat.ProcessMulticastDelegate()
        goto(ExecutionFlow.Pop())
        if not self.mMinimapWidget.IsMapOpen:
           goto(ExecutionFlow.Pop())
        self.ToggleMiniMap()
        goto(ExecutionFlow.Pop())
        # Label 2303
        Default__WidgetBlueprintLibrary.SetInputMode_GameOnly(self)
        ReturnValue_14: bool = self.IsLocalPlayerController()
        if not ReturnValue_14:
           goto(ExecutionFlow.Pop())
        ReturnValue1_4: Ptr[Widget_MapContainer] = Default__WidgetBlueprintLibrary.Create(self, Widget_MapContainer, self)
        self.mMinimapWidget = ReturnValue1_4
        goto(ExecutionFlow.Pop())
        ReturnValue_15: Ptr[Widget_SequenceHelper] = Default__WidgetBlueprintLibrary.Create(self, Widget_SequenceHelper, self)
        ReturnValue_15.AddToViewport(0)
        goto(ExecutionFlow.Pop())
        goto('L2220')
        # Label 2535
        Default__KismetSystemLibrary.PrintString(self, "OnStartRespawn", False, True, LinearColor(R = 0, G = 0.6600000262260437, B = 1, A = 1), 2)
        ReturnValue_16: float = SelectFloat(0, self.mRespawnFadeOutTime, isJoining)
        self.PlayerCameraManager.StartCameraFade(0, 1, ReturnValue_16, LinearColor(R = 0.015208999626338482, G = 0.015208999626338482, B = 0.015208999626338482, A = 1), False, True)
        
        gameUI1 = None
        Default__HUDHelpers.GetFGGameUI(self, self, Ref[gameUI1])
        UI1: Ptr[BP_GameUI] = Cast[BP_GameUI](gameUI1)
        bSuccess4: bool = UI1
        if not bSuccess4:
            goto('L2983')
        ReturnValue_17: Ptr[UMGSequencePlayer] = UI1.PlayAnimation(UI1.FadeAnim, 0, 1, 1, 1)
        # Label 2983
        if not isJoining:
            goto('L3002')
        goto('L176')
        # Label 3002
        Default__KismetSystemLibrary.Delay(self, self.mRespawnFadeOutTime, LatentActionInfo(Linkage = 176, UUID = -185302138, ExecutionFunction = "ExecuteUbergraph_BP_PlayerController", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        # Label 3083
        Default__KismetSystemLibrary.PrintString(self, "OnFinishRespawn", False, True, LinearColor(R = 0, G = 0.6600000262260437, B = 1, A = 1), 2)
        self.PlayerCameraManager.StartCameraFade(1, 0, 2, LinearColor(R = 0.015208999626338482, G = 0.015208999626338482, B = 0.015208999626338482, A = 1), False, False)
        ReturnValue1_5: Ptr[HUD] = self.GetHUD()
        AsFGHUD1: Ptr[FGHUD] = Cast[FGHUD](ReturnValue1_5)
        bSuccess2: bool = AsFGHUD1
        if not bSuccess2:
           goto(ExecutionFlow.Pop())
        AsFGHUD1.CloseRespawnUI()
        
        gameUI = None
        Default__HUDHelpers.GetFGGameUI(self, self, Ref[gameUI])
        UI: Ptr[BP_GameUI] = Cast[BP_GameUI](gameUI)
        bSuccess3: bool = UI
        if not bSuccess3:
           goto(ExecutionFlow.Pop())
        UI.ShowRespawnMessage()
        UI.ForceStopRadiationUI()
        goto(ExecutionFlow.Pop())
        # Label 3583
        self.SetIsUsingGamepad(False)
        goto('L2303')
        goto('L2204')
        # Label 3604
        ReturnValue_18: bool = self.GetIsPhotoMode()
        if not ReturnValue_18:
           goto(ExecutionFlow.Pop())
        self.PlayPhotoSound()
        Default__KismetSystemLibrary.Delay(self, 0.10000000149011612, LatentActionInfo(Linkage = 39, UUID = -2073879089, ExecutionFunction = "ExecuteUbergraph_BP_PlayerController", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        # Label 3725
        self.PhotoModeInstructionsWidget.RemoveFromParent()
        self.PhotoModeInstructionsWidget = None
        goto(ExecutionFlow.Pop())
        goto('L2188')
        # Label 3778
        ReturnValue_19: bool = Default__KismetSystemLibrary.IsValid(self.PhotoModeInstructionsWidget)
        if not ReturnValue_19:
            goto('L3848')
        goto('L3725')
        # Label 3848
        ReturnValue2_3: Ptr[Widget_PhotoMode] = Default__WidgetBlueprintLibrary.Create(self, Widget_PhotoMode, self)
        ReturnValue2_3.AddToViewport(0)
        self.PhotoModeInstructionsWidget = ReturnValue2_3
        goto(ExecutionFlow.Pop())
        goto('L2172')
        # Label 3963
        self.ReceiveBeginPlay()
        goto('L3583')
        goto('L3778')
        goto('L2114')
        # Label 3988
        self.OnRespawnEnd.ProcessMulticastDelegate()
        goto('L3083')
        goto('L2098')
        goto('L2082')
        goto('L2066')
        goto('L1854')
        # Label 4032
        ReturnValue_20: DisabledInputGate = self.GetDisabledInputGate()
        ReturnValue1_6: bool = Not_PreBool(ReturnValue_20.mChat)
        if not ReturnValue1_6:
           goto(ExecutionFlow.Pop())
        goto('L2236')
        goto('L3963')
        ReturnValue_21: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_Camera_SnapShot, self, True)
        goto(ExecutionFlow.Pop())
        goto('L3604')
        goto('L3988')
        # Label 4182
        ReturnValue2_4: Ptr[HUD] = self.GetHUD()
        HUD: Ptr[BP_HUD] = Cast[BP_HUD](ReturnValue2_4)
        bSuccess5: bool = HUD
        if not bSuccess5:
           goto(ExecutionFlow.Pop())
        ReturnValue_22: Ptr[FGGameUI] = HUD.GetGameUI()
        UI2: Ptr[BP_GameUI] = Cast[BP_GameUI](ReturnValue_22)
        bSuccess6: bool = UI2
        if not bSuccess6:
           goto(ExecutionFlow.Pop())
        ReturnValue_23: Ptr[PanelSlot] = UI2.mMenuSlot.AddChild(ReturnValue3_1)
        ReturnValue3_1.OnMenuEnterDone()
        goto(ExecutionFlow.Pop())
        # Label 4500
        ReturnValue3_1: Ptr[BP_PauseWidget] = Default__WidgetBlueprintLibrary.Create(self, BP_PauseWidget, self)
        goto('L4182')
        goto('L4500')
        goto('L4032')
        goto('L2535')
        ReturnValue_24: Rotator = self.GetControlRotation()
        
        Roll = None
        Pitch = None
        Yaw = None
        BreakRotator(ReturnValue_24, Ref[Roll], Ref[Pitch], Ref[Yaw])
        ReturnValue_25: Rotator = MakeRotator(0, Pitch, Yaw)
        
        self.SetControlRotation(Ref[ReturnValue_25])
        goto('L772')
        self.DismantlePortableMiner(PortableMiner)
        goto(ExecutionFlow.Pop())
    

    def OnRespawnEnd__DelegateSignature(self):
        pass
    

    def OnBeginTypeChat__DelegateSignature(self):
        pass
    
