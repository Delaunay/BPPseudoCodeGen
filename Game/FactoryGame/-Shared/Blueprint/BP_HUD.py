
from codegen.ue4_stub import *

from Script.AkAudio import PostAkEvent
from Game.FactoryGame.-Shared.Blueprint.BP_HUD import ExecuteUbergraph_BP_HUD.K2Node_Event_widgetClass
from Script.FactoryGame import FindWidgetByClass
from Script.FactoryGame import FGCharacterPlayer
from Game.FactoryGame.-Shared.Blueprint.BP_HUD import ExecuteUbergraph_BP_HUD.K2Node_Event_slot1
from Script.Engine import SetObjectPropertyByName
from Script.Engine import Pawn
from Script.UMG import OverlaySlot
from Script.FactoryGame import IsEquipped
from Game.FactoryGame.-Shared.Blueprint.BP_HUD import ExecuteUbergraph_BP_HUD.K2Node_Event_widgetClass1
from Game.FactoryGame.Character.Player.Widget_PlayerInventory import Widget_PlayerInventory
from Script.Engine import LatentActionInfo
from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import PlayerController
from Script.FactoryGame import GetBeltSlot
from Script.UMG import SetHorizontalAlignment
from Script.FactoryGame import GetInventory
from Game.FactoryGame.-Shared.Blueprint.BP_HUD import ExecuteUbergraph_BP_HUD
from Script.Engine import IsValid
from Script.FactoryGame import FGInventoryComponent
from Script.UMG import Default__WidgetBlueprintLibrary
from Script.FactoryGame import FGInventoryComponentEquipment
from Script.AkAudio import AkAudioEvent
from Script.FactoryGame import FGInteractWidget
from Script.FactoryGame import ToggleBuildGun
from Script.FactoryGame import GetGameUI
from Script.FactoryGame import GetBuildGun
from Script.FactoryGame import SetDesiredVerticalAlignment
from Script.FactoryGame import FGHUD
from Script.FactoryGame import FGGameUI
from Script.Engine import GetOwningPlayerController
from Script.UMG import Overlay
from Script.Engine import RetriggerableDelay
from Script.Engine import GetOwningPawn
from Script.AkAudio import Default__AkGameplayStatics
from Script.UMG import UserWidget
from Script.FactoryGame import FGInventoryComponentBeltSlot
from Game.FactoryGame.Interface.UI.HUDHelpers.HUDHelpers import Default__HUDHelpers
from Game.FactoryGame.-Shared.Blueprint.BP_HUD import ExecuteUbergraph_BP_HUD.K2Node_Event_slot
from Game.FactoryGame.-Shared.Blueprint.BP_HUD import ExecuteUbergraph_BP_HUD.K2Node_Event_interactObject
from Script.FactoryGame import SetShowCrossHair
from Script.UMG import Create
from Script.FactoryGame import FGBuildGun
from Game.FactoryGame.Interface.UI.InGame.BP_GameUI import BP_GameUI
from Script.FactoryGame import GetTrashSlot
from Script.UMG import SetVerticalAlignment
from Script.FactoryGame import GetEquipmentSlot
from Game.FactoryGame.Interface.UI.BPI_GameUI import BPI_GameUI
from Script.AkAudio import AkComponent
from Script.Engine import IsValidClass
from Script.Engine import PrintString
from Script.UMG import AddChildToOverlay
from Script.CoreUObject import LinearColor

class BP_HUD(FGHUD):
    mOpenInventorySound: Ptr[AkAudioEvent] = Namespace(AssetPath='/Game/FactoryGame/Interface/UI/Audio/Play_UI_Inventory_Open.Play_UI_Inventory_Open')
    mCloseInventorySound: Ptr[AkAudioEvent] = Namespace(AssetPath='/Game/FactoryGame/Interface/UI/Audio/Play_UI_Inventory_Close.Play_UI_Inventory_Close')
    mGameUIClass = NewObject[BP_GameUI]()
    mRespawnUIClass = NewObject[Widget_Respawn]()
    mDefaultCrosshair = Namespace(AssetPath='/Game/FactoryGame/Interface/UI/Assets/Crosshair/default_-reticule.default_-reticule')
    mPickupCrosshair = Namespace(AssetPath='/Game/FactoryGame/Interface/UI/Assets/Crosshair/pick_up.pick_up')
    mVehicleCrosshair = Namespace(AssetPath='/Game/FactoryGame/Interface/UI/Assets/Crosshair/use_vehicle.use_vehicle')
    mWeaponCrosshair = Namespace(AssetPath='/Game/FactoryGame/Interface/UI/Assets/Crosshair/weapon_reticule.weapon_reticule')
    mWorkbenchCrosshair = Namespace(AssetPath='/Game/FactoryGame/Interface/UI/Assets/Crosshair/use_workbench.use_workbench')
    mBuildCrosshair = Namespace(AssetPath='/Game/FactoryGame/Interface/UI/Assets/Crosshair/build_reticule.build_reticule')
    mDismantleCrosshair = Namespace(AssetPath='/Game/FactoryGame/Interface/UI/Assets/Crosshair/dismantle_reticule.dismantle_reticule')
    mGeneralCrosshair = Namespace(AssetPath='/Game/FactoryGame/Interface/UI/Assets/Crosshair/use_general.use_general')
    mPreviewStageClass = NewObject[BP_BuildingPreview]()
    
    def IsInventoryOpen(self):
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayerController()
        
        gameUI = None
        Default__HUDHelpers.GetFGGameUI(ReturnValue, self, Ref[gameUI])
        ReturnValue_0: Ptr[FGInteractWidget] = gameUI.FindWidgetByClass(Widget_PlayerInventory)
        ReturnValue_1: bool = Default__KismetSystemLibrary.IsValid(ReturnValue_0)
        IsOpen = ReturnValue_1
    

    def GetBP_GameUI(self):
        ReturnValue: Ptr[FGGameUI] = self.GetGameUI()
        UI: Ptr[BP_GameUI] = Cast[BP_GameUI](ReturnValue)
        bSuccess: bool = UI
        if not bSuccess:
            goto('L123')
        BPGameUI = UI
        # End
        # Label 123
        Default__KismetSystemLibrary.PrintString(self, "Could not cast to BP_GameUI", True, True, LinearColor(R = 0, G = 0.6600000262260437, B = 1, A = 1), 2)
        BPGameUI = None
    

    def SetupFrontEnd(self):
        self.SetShowCrossHair(False)
        ReturnValue: Ptr[FGGameUI] = self.GetGameUI()
        ReturnValue.RemoveFromParent()
    

    def ToggleInventoryUI(self):
        self.ExecuteUbergraph_BP_HUD(841)
    

    def OpenInventoryUI(self):
        self.ExecuteUbergraph_BP_HUD(2677)
    

    def OpenInteractUI(self):
        ExecuteUbergraph_BP_HUD.K2Node_Event_widgetClass1 = WidgetClass #  PERSISTENT_FRAME(
        ExecuteUbergraph_BP_HUD.K2Node_Event_interactObject = interactObject #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_HUD(3816)
    

    def RemovePawnHUD(self):
        self.ExecuteUbergraph_BP_HUD(4364)
    

    def AddEquipmentHUD(self):
        ExecuteUbergraph_BP_HUD.K2Node_Event_widgetClass = WidgetClass #  PERSISTENT_FRAME(
        ExecuteUbergraph_BP_HUD.K2Node_Event_slot1 = Slot #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_HUD(4502)
    

    def RemoveEquipmentHUD(self):
        ExecuteUbergraph_BP_HUD.K2Node_Event_slot = Slot #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_HUD(4568)
    

    def CloseInteractUIIfOpen(self):
        self.ExecuteUbergraph_BP_HUD(4573)
    

    def ExecuteUbergraph_BP_HUD(self):
        goto(ComputedJump("EntryPoint"))
        # Label 15
        ReturnValue1: Ptr[FGGameUI] = self.GetGameUI()
        ReturnValue1_0: bool = Default__KismetSystemLibrary.IsValid(ReturnValue1)
        if not ReturnValue1_0:
            goto('L455')
        ReturnValue2: Ptr[PlayerController] = self.GetOwningPlayerController()
        ReturnValue3: Ptr[UserWidget] = Default__WidgetBlueprintLibrary.Create(self, widgetClass, ReturnValue2)
        ReturnValue8: Ptr[FGGameUI] = self.GetGameUI()
        UI1: TScriptInterface[BPI_GameUI] = QueryInterface[BPI_GameUI](ReturnValue8)
        bSuccess3: bool = UI1
        if not bSuccess3:
            goto('L532')
        
        overlayParent1 = None
        GetInterfaceUObject(UI1).GetEquipmentHUDParent(slot1, Ref[overlayParent1])
        # Label 335
        ReturnValue: Ptr[OverlaySlot] = overlayParent1.AddChildToOverlay(ReturnValue3)
        ReturnValue.SetVerticalAlignment(0)
        ReturnValue.SetHorizontalAlignment(0)
        goto(ExecutionFlow.Pop())
        # Label 455
        Default__KismetSystemLibrary.RetriggerableDelay(self, 0.20000000298023224, LatentActionInfo(Linkage = 15, UUID = -1339538882, ExecutionFunction = "ExecuteUbergraph_BP_HUD", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        # Label 532
        overlayParent1: Ptr[Overlay] = None
        goto('L335')
        # Label 548
        ReturnValue_0: Ptr[FGGameUI] = self.GetGameUI()
        UI: TScriptInterface[BPI_GameUI] = QueryInterface[BPI_GameUI](ReturnValue_0)
        bSuccess: bool = UI
        if not bSuccess:
            goto('L739')
        
        overlayParent = None
        GetInterfaceUObject(UI).GetEquipmentHUDParent(slot, Ref[overlayParent])
        # Label 702
        overlayParent.ClearChildren()
        goto(ExecutionFlow.Pop())
        # Label 739
        overlayParent: Ptr[Overlay] = None
        goto('L702')
        # Label 755
        ReturnValue_0 = self.GetGameUI()
        ReturnValue_1: bool = Default__KismetSystemLibrary.IsValid(ReturnValue_0)
        if not ReturnValue_1:
           goto(ExecutionFlow.Pop())
        goto('L548')
        
        IsOpen = None
        self.IsInventoryOpen(Ref[IsOpen])
        if not IsOpen:
            goto('L1161')
        ReturnValue5: Ptr[FGGameUI] = self.GetGameUI()
        ReturnValue3_0: Ptr[PlayerController] = self.GetOwningPlayerController()
        
        gameUI1 = None
        Default__HUDHelpers.GetFGGameUI(ReturnValue3_0, self, Ref[gameUI1])
        ReturnValue_2: Ptr[FGInteractWidget] = gameUI1.FindWidgetByClass(Widget_PlayerInventory)
        ReturnValue_3: bool = ReturnValue5.PopWidget(ReturnValue_2)
        ReturnValue1_1: Ptr[Pawn] = self.GetOwningPawn()
        ReturnValue_4: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(self.mCloseInventorySound, ReturnValue1_1, True)
        goto(ExecutionFlow.Pop())
        # Label 1161
        ReturnValue3_1: Ptr[Pawn] = self.GetOwningPawn()
        Player1: Ptr[FGCharacterPlayer] = Cast[FGCharacterPlayer](ReturnValue3_1)
        bSuccess2: bool = Player1
        ReturnValue_5: Ptr[FGBuildGun] = Player1.GetBuildGun()
        ReturnValue_6: bool = ReturnValue_5.IsEquipped()
        if not ReturnValue_6:
            goto('L1461')
        ReturnValue3_1 = self.GetOwningPawn()
        Player1 = Cast[FGCharacterPlayer](ReturnValue3_1)
        bSuccess2 = Player1
        Player1.ToggleBuildGun()
        # Label 1461
        ReturnValue2_0: Ptr[Pawn] = self.GetOwningPawn()
        ReturnValue1_2: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(self.mOpenInventorySound, ReturnValue2_0, True)
        ReturnValue_7: Ptr[PlayerController] = self.GetOwningPlayerController()
        ReturnValue1_3: Ptr[Widget_PlayerInventory] = Default__WidgetBlueprintLibrary.Create(self, Widget_PlayerInventory, ReturnValue_7)
        ReturnValue_8: Ptr[Pawn] = self.GetOwningPawn()
        Player: Ptr[FGCharacterPlayer] = Cast[FGCharacterPlayer](ReturnValue_8)
        bSuccess1: bool = Player
        ReturnValue_9: Ptr[FGInventoryComponent] = Player.GetInventory()
        Default__KismetSystemLibrary.SetObjectPropertyByName(ReturnValue1_3, "mInventoryComponent", ReturnValue_9)
        ReturnValue_8 = self.GetOwningPawn()
        Player = Cast[FGCharacterPlayer](ReturnValue_8)
        bSuccess1 = Player
        ReturnValue1_4: Ptr[FGInventoryComponentEquipment] = Player.GetEquipmentSlot(1)
        Default__KismetSystemLibrary.SetObjectPropertyByName(ReturnValue1_3, "mEquipmentArmsInventoryComponent", ReturnValue1_4)
        ReturnValue_8 = self.GetOwningPawn()
        Player = Cast[FGCharacterPlayer](ReturnValue_8)
        bSuccess1 = Player
        ReturnValue_10: Ptr[FGInventoryComponentEquipment] = Player.GetEquipmentSlot(2)
        Default__KismetSystemLibrary.SetObjectPropertyByName(ReturnValue1_3, "mEquipmentBackInventoryComponent", ReturnValue_10)
        ReturnValue_8 = self.GetOwningPawn()
        Player = Cast[FGCharacterPlayer](ReturnValue_8)
        bSuccess1 = Player
        ReturnValue1_5: Ptr[FGInventoryComponentBeltSlot] = Player.GetBeltSlot()
        Default__KismetSystemLibrary.SetObjectPropertyByName(ReturnValue1_3, "mBeltIntentoryComponent", ReturnValue1_5)
        ReturnValue_8 = self.GetOwningPawn()
        Player = Cast[FGCharacterPlayer](ReturnValue_8)
        bSuccess1 = Player
        ReturnValue_11: Ptr[FGInventoryComponent] = Player.GetTrashSlot()
        Default__KismetSystemLibrary.SetObjectPropertyByName(ReturnValue1_3, "mTrashInventoryComponent", ReturnValue_11)
        ReturnValue1_3.SetDesiredVerticalAlignment(2)
        ReturnValue6: Ptr[FGGameUI] = self.GetGameUI()
        ReturnValue6.PushWidget(ReturnValue1_3)
        goto(ExecutionFlow.Pop())
        
        IsOpen1 = None
        self.IsInventoryOpen(Ref[IsOpen1])
        if not IsOpen1:
            goto('L2715')
        goto(ExecutionFlow.Pop())
        # Label 2715
        ReturnValue_7 = self.GetOwningPlayerController()
        ReturnValue_12: Ptr[Widget_PlayerInventory] = Default__WidgetBlueprintLibrary.Create(self, Widget_PlayerInventory, ReturnValue_7)
        ReturnValue_8 = self.GetOwningPawn()
        Player = Cast[FGCharacterPlayer](ReturnValue_8)
        bSuccess1 = Player
        ReturnValue_9 = Player.GetInventory()
        Default__KismetSystemLibrary.SetObjectPropertyByName(ReturnValue_12, "mInventoryComponent", ReturnValue_9)
        ReturnValue_8 = self.GetOwningPawn()
        Player = Cast[FGCharacterPlayer](ReturnValue_8)
        bSuccess1 = Player
        ReturnValue1_4 = Player.GetEquipmentSlot(1)
        Default__KismetSystemLibrary.SetObjectPropertyByName(ReturnValue_12, "mEquipmentArmsInventoryComponent", ReturnValue1_4)
        ReturnValue_8 = self.GetOwningPawn()
        Player = Cast[FGCharacterPlayer](ReturnValue_8)
        bSuccess1 = Player
        ReturnValue_10 = Player.GetEquipmentSlot(2)
        Default__KismetSystemLibrary.SetObjectPropertyByName(ReturnValue_12, "mEquipmentBackInventoryComponent", ReturnValue_10)
        ReturnValue_8 = self.GetOwningPawn()
        Player = Cast[FGCharacterPlayer](ReturnValue_8)
        bSuccess1 = Player
        ReturnValue_13: Ptr[FGInventoryComponentBeltSlot] = Player.GetBeltSlot()
        Default__KismetSystemLibrary.SetObjectPropertyByName(ReturnValue_12, "mBeltIntentoryComponent", ReturnValue_13)
        ReturnValue_8 = self.GetOwningPawn()
        Player = Cast[FGCharacterPlayer](ReturnValue_8)
        bSuccess1 = Player
        ReturnValue_11 = Player.GetTrashSlot()
        Default__KismetSystemLibrary.SetObjectPropertyByName(ReturnValue_12, "mTrashInventoryComponent", ReturnValue_11)
        ReturnValue7: Ptr[FGGameUI] = self.GetGameUI()
        ReturnValue7.PushWidget(ReturnValue_12)
        goto(ExecutionFlow.Pop())
        ReturnValue9: Ptr[FGGameUI] = self.GetGameUI()
        UI2: TScriptInterface[BPI_GameUI] = QueryInterface[BPI_GameUI](ReturnValue9)
        bSuccess4: bool = UI2
        if not bSuccess4:
            goto('L4348')
        
        widget = None
        GetInterfaceUObject(UI2).FindWidgetToPop(Ref[widget])
        # Label 3961
        ReturnValue3_2: bool = Default__KismetSystemLibrary.IsValid(widget)
        if not ReturnValue3_2:
            goto('L4083')
        ReturnValue2_1: Ptr[FGGameUI] = self.GetGameUI()
        ReturnValue2_1.PopAllWidgets()
        goto(ExecutionFlow.Pop())
        # Label 4083
        ReturnValue1_6: Ptr[PlayerController] = self.GetOwningPlayerController()
        ReturnValue2_2: Ptr[FGInteractWidget] = Default__WidgetBlueprintLibrary.Create(self, widgetClass1, ReturnValue1_6)
        Default__KismetSystemLibrary.SetObjectPropertyByName(ReturnValue2_2, "mInteractObject", interactObject)
        ReturnValue1_6 = self.GetOwningPlayerController()
        
        gameUI = None
        Default__HUDHelpers.GetFGGameUI(ReturnValue1_6, self, Ref[gameUI])
        gameUI.PushWidget(ReturnValue2_2)
        goto(ExecutionFlow.Pop())
        # Label 4348
        widget: Ptr[FGInteractWidget] = None
        goto('L3961')
        ReturnValue3_3: Ptr[FGGameUI] = self.GetGameUI()
        ReturnValue2_3: bool = Default__KismetSystemLibrary.IsValid(ReturnValue3_3)
        if not ReturnValue2_3:
           goto(ExecutionFlow.Pop())
        ReturnValue3_3 = self.GetGameUI()
        ReturnValue3_3.RemovePawnHUD()
        goto(ExecutionFlow.Pop())
        ReturnValue_14: bool = Default__KismetSystemLibrary.IsValidClass(widgetClass)
        if not ReturnValue_14:
           goto(ExecutionFlow.Pop())
        goto('L15')
        goto('L755')
        ReturnValue10: Ptr[FGGameUI] = self.GetGameUI()
        UI3: TScriptInterface[BPI_GameUI] = QueryInterface[BPI_GameUI](ReturnValue10)
        bSuccess5: bool = UI3
        if not bSuccess5:
            goto('L4836')
        
        widget1 = None
        GetInterfaceUObject(UI3).FindWidgetToPop(Ref[widget1])
        # Label 4718
        ReturnValue4: bool = Default__KismetSystemLibrary.IsValid(widget1)
        if not ReturnValue4:
           goto(ExecutionFlow.Pop())
        ReturnValue4_0: Ptr[FGGameUI] = self.GetGameUI()
        ReturnValue4_0.PopAllWidgets()
        goto(ExecutionFlow.Pop())
        # Label 4836
        widget1: Ptr[FGInteractWidget] = None
        goto('L4718')
    
