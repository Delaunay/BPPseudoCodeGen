
from codegen.ue4_stub import *

from Script.FactoryGame import FGCharacterPlayer
from Game.FactoryGame.Interface.UI.InGame.BP_GameUI import ExecuteUbergraph_BP_GameUI.K2Node_Event_radiationIntensity
from Game.FactoryGame.Interface.UI.InGame.BP_GameUI import ExecuteUbergraph_BP_GameUI.K2Node_Event_newContent
from Script.FactoryGame import EResourceForm
from Script.InputCore import Key
from Script.FactoryGame import GetHUDVisibility
from Script.UMG import OverlaySlot
from Script.Engine import FFloor
from Script.UMG import AddChild
from Game.FactoryGame.Interface.UI.InGame.BP_GameUI import ExecuteUbergraph_BP_GameUI.K2Node_CustomEvent_Velocity
from Game.FactoryGame.Character.Player.Widget_PlayerInventory import Widget_PlayerInventory
from Script.Engine import Default__KismetSystemLibrary
from Script.FactoryGame import FGAudioMessage
from Script.Engine import EqualEqual_FloatFloat
from Script.UMG import GetChildAt
from Script.UMG import Handled
from Script.Engine import FormatArgumentData
from Script.UMG import ESlateVisibility
from Game.FactoryGame.Interface.UI.InGame.BP_GameUI import ExecuteUbergraph_BP_GameUI.K2Node_Event_inMessage
from Game.FactoryGame.Interface.UI.InGame.Widget_Popup import Widget_Popup
from Script.Engine import TimerHandle
from Script.Engine import IsValid
from Script.FactoryGame import GetBoolOptionValue
from Script.FactoryGame import DisableVirtualCursor
from Script.UMG import Destruct
from Script.Engine import EqualEqual_IntInt
from Script.Engine import Default__KismetTextLibrary
from Script.FactoryGame import GetPlayerHasMessage
from Script.Engine import Conv_StringToText
from Script.UMG import Construct
from Script.FactoryGame import GetDesiredHorizontalAlignment
from Script.FactoryGame import HasAmmunition
from Script.FactoryGame import NeedRespawn
from Script.FactoryGame import FGWeapon
from Script.FactoryGame import FGPopupWidget
from Script.FactoryGame import TutorialHintData
from Script.FactoryGame import GetStackFromIndex
from Script.UMG import Create
from Game.FactoryGame.Character.Player.BP_DebugCameraController import BP_DebugCameraController
from Script.Engine import GetGameState
from Game.FactoryGame.Character.Player.BP_PlayerController import BP_PlayerController
from Script.FactoryGame import GetFloatOptionValue
from Script.FactoryGame import FindGroundLocationInfrontOfActor
from Game.FactoryGame.Interface.UI.InGame.BP_GameUI import ExecuteUbergraph_BP_GameUI.K2Node_Event_Duration
from Script.SlateCore import EHorizontalAlignment
from Script.CoreUObject import LinearColor
from Script.FactoryGame import AssignOnConcludedDelegate
from Script.Engine import SetClassPropertyByName
from Script.FactoryGame import FGPlayerController
from Script.FactoryGame import GetPumpiMode
from Script.Engine import Controller
from Script.Engine import EqualEqual_ByteByte
from Script.FactoryGame import GetFGGameUserSettings
from Script.Engine import Pawn
from Script.FactoryGame import GetShowBreakNotification
from Script.Engine import GreaterEqual_IntInt
from Script.UMG import AddChildToVerticalBox
from Script.UMG import GetChildrenCount
from Script.Engine import HUD
from Script.UMG import SetInputMode_GameOnly
from Script.FactoryGame import GetIsReloading
from Game.FactoryGame.Interface.UI.InGame.BP_GameUI import ExecuteUbergraph_BP_GameUI.K2Node_Event_Widget
from Script.Engine import Default__KismetArrayLibrary
from Script.Engine import GameStateBase
from Script.UMG import SetRenderTranslation
from Script.UMG import SetHorizontalAlignment
from Script.SlateCore import EVerticalAlignment
from Game.FactoryGame.Interface.UI.InGame.BP_GameUI import ExecuteUbergraph_BP_GameUI.K2Node_Event_radiationImmunity
from Game.FactoryGame.Interface.UI.Menu.BP_MenuBase import BP_MenuBase
from Script.UMG import SetUserSpecifiedScale
from Script.Engine import GetObjectClass
from Script.FactoryGame import FGEquipment
from Script.FactoryGame import GetDefaultFocusWidget
from Script.Engine import GetHUD
from Game.FactoryGame.Interface.UI.InGame.InventorySlots.Widget_InventorySlot import Widget_InventorySlot
from Game.FactoryGame.Interface.UI.InGame.BP_GameUI import ExecuteUbergraph_BP_GameUI.K2Node_Event_messageClass
from Script.FactoryGame import GetPopup
from Script.FactoryGame import Default__FGItemPickup_Spawnable
from Script.FactoryGame import FGGameUserSettings
from Game.FactoryGame.Interface.UI.InGame.Widget_WaterNotifier import Widget_WaterNotifier
from Script.FactoryGame import FGInteractWidget
from Script.FactoryGame import FGGameState
from Game.FactoryGame.Interface.UI.InGame.BP_GameUI import ExecuteUbergraph_BP_GameUI.K2Node_Event_Subtitle
from Script.Engine import GetGameTimeSinceCreation
from Game.FactoryGame.Interface.UI.Audio.MainMenu.Play_UI_MainMenu_DialBoxDropDown import Play_UI_MainMenu_DialBoxDropDown
from Script.FactoryGame import GetPartialPumpiMode
from Script.Engine import GetKey
from Script.Engine import NotEqual_ByteByte
from Script.AkAudio import Default__AkGameplayStatics
from Script.Engine import EqualEqual_KeyKey
from Script.Engine import RandomInteger
from Script.FactoryGame import RemoveInteractWidget
from Script.UMG import VerticalBoxSlot
from Script.FactoryGame import Default__FGItemDescriptor
from Game.FactoryGame.Interface.UI.InGame.BP_GameUI import ExecuteUbergraph_BP_GameUI
from Script.AkAudio import AkComponent
from Script.FactoryGame import BreakInventoryItem
from Script.FactoryGame import RemoveAudioMessage
from Script.FactoryGame import GetGameVersion
from Script.Engine import PrintString
from Script.UMG import EventReply
from Game.FactoryGame.Interface.UI.InGame.BP_GameUI import ExecuteUbergraph_BP_GameUI.K2Node_Event_tutorialHintData
from Script.UMG import SetUserFocus
from Script.Engine import SetTextPropertyByName
from Game.FactoryGame.Interface.UI.Debug.Debug_Aggro import Debug_Aggro
from Script.AkAudio import PostAkEvent
from Game.FactoryGame.Interface.UI.InGame.Widget_MessageNotifier import Widget_MessageNotifier
from Game.FactoryGame.Interface.UI.InGame.BP_GameUI import ExecuteUbergraph_BP_GameUI.K2Node_Event_Instigator
from Script.Engine import Delay
from Script.FactoryGame import PopAllWidgets
from Script.FactoryGame import BreakInventoryStack
from Script.FactoryGame import GetEquipmentInSlot
from Script.FactoryGame import PopWidget
from Script.UMG import GetEndTime
from Script.FactoryGame import FGChatManager
from Script.UMG import PanelSlot
from Script.FactoryGame import Default__FGInventoryLibrary
from Script.Engine import Conv_IntToFloat
from Script.Engine import TextIsEmpty
from Game.FactoryGame.Interface.UI.InGame.Widget_TutorialInfo import Widget_TutorialInfo
from Script.Engine import LatentActionInfo
from Script.FactoryGame import PopPopupQueue
from Game.FactoryGame.Interface.UI.InGame.BP_GameUI import ExecuteUbergraph_BP_GameUI.K2Node_Event_bUseDuration
from Script.Engine import PlayerController
from Script.UMG import SetInputMode_UIOnlyEx
from Script.FactoryGame import Get
from Script.Engine import GetController
from Script.UMG import PlayAnimation
from Script.UMG import Unhandled
from Script.FactoryGame import GetForm
from Script.FactoryGame import GetVersionString
from Script.UMG import Default__WidgetBlueprintLibrary
from Script.Engine import ClassIsChildOf
from Script.FactoryGame import SubscribeToDynamicOptionUpdate
from Script.Engine import Default__GameplayStatics
from Script.FactoryGame import GetInteractWidgetStack
from Game.FactoryGame.Interface.UI.InGame.Widget_UseableBase import Widget_UseableBase
from Script.Engine import EqualEqual_ObjectObject
from Script.Engine import Format
from Script.Engine import SetArrayPropertyByName
from Script.FactoryGame import FGGameUI
from Game.FactoryGame.Character.Player.Widget_PlayerInventoryAddon import Widget_PlayerInventoryAddon
from Script.FactoryGame import UnsubscribeToAllDynamicOptionUpdate
from Script.FactoryGame import FormatStringWithKeyNames
from Script.FactoryGame import GetRemoteCallObjectOfClass
from Script.UMG import HasAnyChildren
from Script.FactoryGame import GetDesiredVerticalAlignment
from Script.CoreUObject import Vector2D
from Script.FactoryGame import Default__FGVirtualCursorFunctionLibrary
from Script.Engine import GetForwardVector
from Script.FactoryGame import Default__FGVersionFunctionLibrary
from Script.UMG import SetVerticalAlignment
from Script.FactoryGame import AddInteractWidget
from Script.FactoryGame import IsAliveAndWell
from Script.UMG import RemoveChild
from Game.FactoryGame.Character.Player.BP_RemoteCallObject import BP_RemoteCallObject
from Script.Engine import Default__KismetInputLibrary
from Script.UMG import SetSize
from Script.FactoryGame import Default__FGChatManager
from Script.UMG import HorizontalBoxSlot
from Script.Engine import Not_PreBool
from Script.FactoryGame import CanReload
from Script.FactoryGame import GetDesiredAlignmentSize
from Script.FactoryGame import GetBestUsableActor
from Game.FactoryGame.Interface.UI.InGame.BP_GameUI import ExecuteUbergraph_BP_GameUI.K2Node_CustomEvent_TimeUntilAutosave
from Game.FactoryGame.Interface.UI.InGame.BP_GameUI import ExecuteUbergraph_BP_GameUI.K2Node_Event_Instigator1
from Game.FactoryGame.-Shared.Blueprint.BP_HUD import BP_HUD
from Script.FactoryGame import SetCurrentAudioMessage
from Script.UMG import SlateChildSize
from Script.FactoryGame import Default__FGGameUserSettings
from Script.FactoryGame import GetCurrentAudioMessage
from Script.Engine import BooleanOR
from Script.UMG import IsVisible
from Script.UMG import Widget
from Script.CoreUObject import Vector
from Game.FactoryGame.Buildable.Factory.BP_DragNDropInventory import BP_DragNDropInventory
from Script.FactoryGame import EGameVersion
from Script.UMG import WidgetAnimation
from Script.FactoryGame import FGHUD
from Script.FactoryGame import SetHUDVisibility
from Script.UMG import GetOwningPlayerPawn
from Game.FactoryGame.Interface.UI.InGame.BP_GameUI import ExecuteUbergraph_BP_GameUI.K2Node_CustomEvent_hintData
from Script.Engine import Actor
from Script.UMG import UMGSequencePlayer
from Script.FactoryGame import SetPopup
from Script.UMG import SetRenderOpacity
from Script.Engine import IsValidClass
from Game.FactoryGame.Interface.UI.InGame.BP_GameUI import ExecuteUbergraph_BP_GameUI.K2Node_Event_widgetToAdd
from Script.FactoryGame import CancelPlayback
from Script.UMG import AddChildToOverlay
from Script.FactoryGame import Default__FGInputLibrary

class BP_GameUI(FGGameUI):
    FadeAnim: Ptr[WidgetAnimation]
    JumpLand: Ptr[WidgetAnimation]
    mWidgetStack: List[Ptr[FGInteractWidget]]
    bpHUD: Ptr[BP_HUD]
    mAIDebug: Ptr[Debug_Aggro]
    mHUDShakeActive: bool
    CachedPlayerInventoryAddon: Ptr[Widget_PlayerInventoryAddon]
    mCachedTutorialHintData: TutorialHintData
    mIsSkippingIntro: bool
    mPlaytimeWarningMessages: List[FText]
    mPlaytimeWarningMessageIndex: int32
    mBreakNotificationTimer: TimerHandle
    mFGGameState: Ptr[FGGameState]
    mMinTimeBetweenAudioMessage = 1
    Priority = 10
    
    def GetEquipmentHUDParent(self):
        CmpSuccess: bool = NotEqual_ByteByte(slotType, 0)
        if not CmpSuccess:
            goto('L140')
        CmpSuccess = NotEqual_ByteByte(slotType, 1)
        if not CmpSuccess:
            goto('L140')
        CmpSuccess = NotEqual_ByteByte(slotType, 2)
        if not CmpSuccess:
            goto('L164')
        # End
        # Label 140
        overlayParent = self.mHandSlotOverlay
        # End
        # Label 164
        overlayParent = self.mBodySlotOverlay
    

    def FindWidgetToPop(self):
        ExecutionFlow.Push("L294")
        ReturnValue1: List[Ptr[FGInteractWidget]] = self.GetInteractWidgetStack()
        
        ReturnValue: int32 = len(ReturnValue1) - 1
        # Label 92
        index = ReturnValue
        # Label 119
        ReturnValue_0: bool = GreaterEqual_IntInt(index, 0)
        # Label 153
        if not ReturnValue_0:
            goto('L283')
        ExecutionFlow.Push("L119")
        ReturnValue_1: List[Ptr[FGInteractWidget]] = self.GetInteractWidgetStack()
        
        Item = None
        Item = ReturnValue_1[index]
        Widget = Item
        # End
        # Label 283
        Widget = None
    

    def GetMessageBox(self):
        messageBox = self.mMessageBox
    

    def GetShoppingList(self):
        shoppingList = self.Widget_ShoppingList_134
    

    def PopWidget(self):
        ExecutionFlow.Push("L1630")
        ExecutionFlow.Push("L40")
        ReturnValue: bool = self.PopWidget(WidgetToRemove)
        goto(ExecutionFlow.Pop())
        # Label 40
        self.PrePopWidget(WidgetToRemove)
        ReturnValue_0: bool = Default__KismetSystemLibrary.IsValid(WidgetToRemove)
        if not ReturnValue_0:
            goto('L1063')
        WidgetToPop = WidgetToRemove
        # Label 147
        Variable: bool = False
        Variable_0: int32 = 0
        Variable_1: int32 = 0
        # Label 204
        ReturnValue_1: bool = Not_PreBool(Variable)
        # Label 233
        ReturnValue3: List[Ptr[FGInteractWidget]] = self.GetInteractWidgetStack()
        
        ReturnValue1: int32 = len(ReturnValue3)
        ReturnValue_2: bool = Variable_0 <= ReturnValue1
        ReturnValue_3: bool = ReturnValue_1 and ReturnValue_2
        if not ReturnValue_3:
            goto('L1171')
        Variable_1 = Variable_0
        ExecutionFlow.Push("L1556")
        ReturnValue3 = self.GetInteractWidgetStack()
        
        Item1 = None
        Item1 = ReturnValue3[Variable_1]
        ReturnValue_4: bool = EqualEqual_ObjectObject(WidgetToPop, Item1)
        if not ReturnValue_4:
           goto(ExecutionFlow.Pop())
        didPop = True
        ReturnValue3 = self.GetInteractWidgetStack()
        
        Item1 = None
        # Label 616
        Item1 = ReturnValue3[Variable_1]
        ReturnValue_5: bool = self.mCenterWidgetBox.RemoveChild(Item1)
        ReturnValue3 = self.GetInteractWidgetStack()
        
        Item1 = None
        Item1 = ReturnValue3[Variable_1]
        Base: Ptr[Widget_UseableBase] = Cast[Widget_UseableBase](Item1)
        bSuccess: bool = Base
        if not bSuccess:
            goto('L956')
        OutputDelegate.BindUFunction(self, OnInventorySlotStackMove)
        Base.InventorySlotStackMoveEvent.Remove(OutputDelegate)
        # Label 956
        ReturnValue3 = self.GetInteractWidgetStack()
        
        Item1 = None
        Item1 = ReturnValue3[Variable_1]
        self.RemoveInteractWidget(Item1)
        goto(ExecutionFlow.Pop())
        
        widget = None
        # Label 1063
        self.FindWidgetToPop(Ref[widget])
        WidgetToPop = widget
        ReturnValue1_0: bool = Default__KismetSystemLibrary.IsValid(WidgetToPop)
        if not ReturnValue1_0:
           goto(ExecutionFlow.Pop())
        goto('L147')
        # Label 1171
        ReturnValue2: List[Ptr[FGInteractWidget]] = self.GetInteractWidgetStack()
        
        ReturnValue_6: int32 = len(ReturnValue2)
        ReturnValue_7: bool = EqualEqual_IntInt(ReturnValue_6, 0)
        if not ReturnValue_7:
            goto('L1335')
        self.ResetInput()
        self.UpdateHUDVisibility()
        goto(ExecutionFlow.Pop())
        # Label 1335
        if not didPop:
           goto(ExecutionFlow.Pop())
        ReturnValue_8: List[Ptr[FGInteractWidget]] = self.GetInteractWidgetStack()
        ReturnValue1_1: List[Ptr[FGInteractWidget]] = self.GetInteractWidgetStack()
        
        ReturnValue_9: int32 = len(ReturnValue1_1) - 1
        
        Item = None
        Item = ReturnValue_8[ReturnValue_9]
        Item.SetInputMode()
        goto(ExecutionFlow.Pop())
        # Label 1556
        ReturnValue_10: int32 = Variable_0 + 1
        Variable_0 = ReturnValue_10
        goto('L204')
    

    def OnPreviewKeyDown(self):
        
        ReturnValue: Key = Default__KismetInputLibrary.GetKey(Ref[InKeyEvent])
        ReturnValue_0: bool = Default__KismetInputLibrary.EqualEqual_KeyKey(ReturnValue, Key(KeyName = "Enter"))
        ReturnValue1: Ptr[FGAudioMessage] = self.GetCurrentAudioMessage()
        ReturnValue_1: bool = Default__KismetSystemLibrary.IsValid(ReturnValue1)
        ReturnValue_2: bool = ReturnValue_0 and ReturnValue_1
        if not ReturnValue_2:
            goto('L394')
        ReturnValue_3: Ptr[FGAudioMessage] = self.GetCurrentAudioMessage()
        ReturnValue_3.CancelPlayback()
        ReturnValue_4: EventReply = Default__WidgetBlueprintLibrary.Handled()
        ReturnValue_5: EventReply = ReturnValue_4
        # Label 389
        goto('L471')
        # Label 394
        ReturnValue_6: EventReply = Default__WidgetBlueprintLibrary.Unhandled()
        ReturnValue_5 = ReturnValue_6
    

    def SetVersionLabelPosition(self):
        Variable: Vector2D = Vector2D(X = 32, Y = 32)
        Variable1: Vector2D = Vector2D(X = 160, Y = 32)
        ReturnValue: uint8 = Default__FGVersionFunctionLibrary.GetGameVersion()
        ReturnValue_0: bool = EqualEqual_ByteByte(ReturnValue, 0)
        Variable_0: bool = ReturnValue_0
        
        switch = {
            False: Variable1,
            True: Variable
        }
        self.mVersionLabel.SetRenderTranslation(switch.get(Variable_0, None))
    

    def GetExperimentalVisibility(self):
        Variable: uint8 = 3
        Variable1: uint8 = 1
        # Label 40
        ReturnValue: uint8 = Default__FGVersionFunctionLibrary.GetGameVersion()
        ReturnValue_0: bool = EqualEqual_ByteByte(ReturnValue, 1)
        Variable_0: bool = ReturnValue_0
        
        switch = {
            False: Variable1,
            True: Variable
        }
        # Label 140
        self.mExperimentalBuildLabel.SetVisibility(switch.get(Variable_0, None))
    

    def GetChildUIVisibility(self):
        
        HUD = None
        self.GetFGHud(Ref[HUD])
        ReturnValue: bool = HUD.GetPartialPumpiMode()
        if not ReturnValue:
            goto('L104')
        ReturnValue_0: uint8 = 2
        goto('L124')
        # Label 104
        ReturnValue_0 = 4
    

    def PrePopWidget(self, WidgetBeingRemoved: Ptr[FGInteractWidget]):
        ExecutionFlow.Push("L429")
        ExecutionFlow.Push("L212")
        ReturnValue1: Ptr[PlayerController] = self.GetOwningPlayer()
        Controller1: Ptr[FGPlayerController] = Cast[FGPlayerController](ReturnValue1)
        bSuccess2: bool = Controller1
        if not bSuccess2:
           goto(ExecutionFlow.Pop())
        ReturnValue: TSubclassOf[FGInteractWidget] = Default__GameplayStatics.GetObjectClass(WidgetBeingRemoved)
        Controller1.OnToggleInteractionUI.ProcessMulticastDelegate(False, ReturnValue)
        goto(ExecutionFlow.Pop())
        # Label 212
        Inventory: Ptr[Widget_PlayerInventory] = Cast[Widget_PlayerInventory](WidgetBeingRemoved)
        bSuccess: bool = Inventory
        if not bSuccess:
           goto(ExecutionFlow.Pop())
        ReturnValue_0: Ptr[PlayerController] = self.GetOwningPlayer()
        Controller: Ptr[FGPlayerController] = Cast[FGPlayerController](ReturnValue_0)
        bSuccess1: bool = Controller
        if not bSuccess1:
           goto(ExecutionFlow.Pop())
        Controller.OnToggleInventory.ProcessMulticastDelegate(False)
        goto(ExecutionFlow.Pop())
    

    def ShowTutorialHint(self):
        ReturnValue: bool = self.mTutorialInfoSlot.HasAnyChildren()
        if not ReturnValue:
            goto('L92')
        self.mTutorialInfoSlot.ClearChildren()
        # Label 92
        ReturnValue_0: bool = EqualEqual_ByteByte(self.mCachedTutorialHintData.ID, 12)
        if not ReturnValue_0:
            goto('L151')
        # End
        
        self.mCachedTutorialHintData.HintTexts = None
        # Label 151
        ReturnValue_1: int32 = len(self.mCachedTutorialHintData.HintTexts)
        ReturnValue_2: bool = GreaterEqual_IntInt(ReturnValue_1, 1)
        
        self.mCachedTutorialHintData.Title = None
        ReturnValue_3: bool = Default__KismetTextLibrary.TextIsEmpty(Ref[self.mCachedTutorialHintData.Title])
        ReturnValue_4: bool = Not_PreBool(ReturnValue_3)
        ReturnValue_5: bool = BooleanOR(ReturnValue_4, ReturnValue_2)
        # Label 380
        if not ReturnValue_5:
            goto('L674')
        # Label 394
        ReturnValue_6: Ptr[PlayerController] = self.GetOwningPlayer()
        # Label 418
        ReturnValue_7: Ptr[Widget_TutorialInfo] = Default__WidgetBlueprintLibrary.Create(self, Widget_TutorialInfo, ReturnValue_6)
        
        self.mCachedTutorialHintData.Title = None
        Default__KismetSystemLibrary.SetTextPropertyByName(ReturnValue_7, "mTitle", Ref[self.mCachedTutorialHintData.Title])
        
        self.mCachedTutorialHintData.HintTexts = None
        Default__KismetArrayLibrary.SetArrayPropertyByName(ReturnValue_7, "mHints", Ref[self.mCachedTutorialHintData.HintTexts])
        ReturnValue_8: Ptr[PanelSlot] = self.mTutorialInfoSlot.AddChild(ReturnValue_7)
    

    def GetFGHud(self):
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_0: Ptr[HUD] = ReturnValue.GetHUD()
        AsFGHUD: Ptr[FGHUD] = Cast[FGHUD](ReturnValue_0)
        bSuccess1: bool = AsFGHUD
        if not bSuccess1:
            goto('L169')
        HUD = AsFGHUD
        # Label 164
        # End
        # Label 169
        ReturnValue = self.GetOwningPlayer()
        Controller: Ptr[BP_DebugCameraController] = Cast[BP_DebugCameraController](ReturnValue)
        bSuccess: bool = Controller
        if not bSuccess:
            goto('L318')
        HUD = Controller.mOriginalHUD
        # End
        # Label 318
        Default__KismetSystemLibrary.PrintString(self, "Cast failed to FGHUD", True, True, LinearColor(R = 0, G = 0.6600000262260437, B = 1, A = 1), 2)
        HUD = None
    

    def SetPrototypeCameraVisibility(self, New Visibility: bool):
        if not New Visibility:
            goto('L57')
        self.CameraCanvas.SetVisibility(4)
        # End
        # Label 57
        self.CameraCanvas.SetVisibility(2)
    

    def SetPrototypeVisibility(self, NewVisibility: bool):
        if not NewVisibility:
            goto('L95')
        self.HUD_Overlay.SetVisibility(4)
        self.StandardUI.SetVisibility(4)
        # End
        # Label 95
        self.HUD_Overlay.SetVisibility(2)
        self.StandardUI.SetVisibility(2)
    

    def OnInventorySlotStackMove(self, InventorySlot: Ptr[Widget_InventorySlot], InteractionDirection: uint8):
        ExecutionFlow.Push("L1130")
        CmpSuccess: bool = NotEqual_ByteByte(InteractionDirection, 0)
        if not CmpSuccess:
            goto('L96')
        CmpSuccess = NotEqual_ByteByte(InteractionDirection, 1)
        if not CmpSuccess:
            goto('L711')
        # Label 95
        goto(ExecutionFlow.Pop())
        # Label 96
        Variable: bool = False
        # Label 107
        Variable_0: int32 = 0
        Variable_1: int32 = 0
        # Label 153
        ReturnValue: bool = Not_PreBool(Variable)
        ReturnValue_0: List[Ptr[FGInteractWidget]] = self.GetInteractWidgetStack()
        
        ReturnValue_1: int32 = len(ReturnValue_0)
        ReturnValue_2: bool = Variable_0 <= ReturnValue_1
        ReturnValue_3: bool = ReturnValue and ReturnValue_2
        if not ReturnValue_3:
            goto('L629')
        Variable_1 = Variable_0
        ExecutionFlow.Push("L1056")
        ReturnValue_0 = self.GetInteractWidgetStack()
        
        Item = None
        Item = ReturnValue_0[Variable_1]
        Base: Ptr[Widget_UseableBase] = Cast[Widget_UseableBase](Item)
        # Label 514
        bSuccess1: bool = Base
        if not bSuccess1:
           goto(ExecutionFlow.Pop())
        
        WasStackMoved = None
        Base.DropInventorySlotStack(InventorySlot, Ref[WasStackMoved])
        if not WasStackMoved:
           goto(ExecutionFlow.Pop())
        Variable = True
        goto(ExecutionFlow.Pop())
        # Label 629
        ReturnValue_4: Ptr[Pawn] = self.GetOwningPlayerPawn()
        ReturnValue_5: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_UI_MainMenu_DialBoxDropDown, ReturnValue_4, True)
        goto(ExecutionFlow.Pop())
        # Label 711
        ReturnValue_6: bool = Default__KismetSystemLibrary.IsValid(self.CachedPlayerInventoryAddon)
        if not ReturnValue_6:
           goto(ExecutionFlow.Pop())
        ReturnValue_7: Ptr[PlayerController] = self.GetOwningPlayer()
        Controller: Ptr[FGPlayerController] = Cast[FGPlayerController](ReturnValue_7)
        bSuccess: bool = Controller
        if not bSuccess:
           goto(ExecutionFlow.Pop())
        ReturnValue_8: Ptr[BP_RemoteCallObject] = Controller.GetRemoteCallObjectOfClass(BP_RemoteCallObject)
        ReturnValue_8.Server_MoveItemIfSpace(InventorySlot.mCachedInventoryComponent, InventorySlot.mSlotIdx, self.CachedPlayerInventoryAddon.mInventoryComponent)
        goto('L629')
        # Label 1056
        ReturnValue_9: int32 = Variable_0 + 1
        Variable_0 = ReturnValue_9
        goto('L153')
    

    def CreateAddOnPlayerInventory(self, Container: Ptr[PanelWidget]):
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_0: Ptr[Widget_PlayerInventoryAddon] = Default__WidgetBlueprintLibrary.Create(self, Widget_PlayerInventoryAddon, ReturnValue)
        Variable: Const[FText] = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 105, 'Value': 'Relevant Items:'}"
        
        Default__KismetSystemLibrary.SetTextPropertyByName(ReturnValue_0, "mRelevantItemsText", Ref[Variable])
        ReturnValue_1: Ptr[PanelSlot] = Container.AddChild(ReturnValue_0)
        OutputDelegate.BindUFunction(self, OnInventorySlotStackMove)
        ReturnValue_0.SlotStackMoveEvent.AddUnique(OutputDelegate)
        self.CachedPlayerInventoryAddon = ReturnValue_0
        # Label 355
        CachedPlayerInventoryAddon = self.CachedPlayerInventoryAddon
    

    def IsChatWindowVisible(self):
        Variable: uint8 = 0
        Variable1: uint8 = 2
        
        HUD = None
        # Label 40
        self.GetFGHud(Ref[HUD])
        ReturnValue: bool = HUD.GetHUDVisibility()
        ReturnValue_0: bool = self.mChatWindow.GetInputWindowVisibility()
        
        IsFresh = None
        # Label 151
        self.mChatWindow.IsLastMessageFresh(Ref[IsFresh])
        ReturnValue_1: bool = HUD.GetPumpiMode()
        ReturnValue_2: bool = BooleanOR(ReturnValue_0, IsFresh)
        ReturnValue_3: bool = Not_PreBool(ReturnValue_1)
        ReturnValue1: bool = BooleanOR(ReturnValue_3, ReturnValue)
        ReturnValue_4: bool = ReturnValue1 and ReturnValue_2
        Variable_0: bool = ReturnValue_4
        
        switch = {
            False: Variable1,
            True: Variable
        }
        # Label 400
        ReturnValue_5: uint8 = switch.get(Variable_0, None)
    

    def GetUIVisibility(self):
        
        HUD = None
        self.GetFGHud(Ref[HUD])
        ReturnValue: bool = HUD.GetPumpiMode()
        if not ReturnValue:
            goto('L104')
        ReturnValue_0: uint8 = 2
        goto('L124')
        # Label 104
        ReturnValue_0 = 4
    

    def OnKeyDown(self):
        
        ReturnValue: Key = Default__KismetInputLibrary.GetKey(Ref[InKeyEvent])
        ReturnValue_0: bool = Default__KismetInputLibrary.EqualEqual_KeyKey(ReturnValue, Key(KeyName = "Escape"))
        ReturnValue1: bool = Default__KismetInputLibrary.EqualEqual_KeyKey(ReturnValue, Key(KeyName = "E"))
        ReturnValue_1: bool = BooleanOR(ReturnValue1, ReturnValue_0)
        if not ReturnValue_1:
            goto('L666')
        ReturnValue1_0: List[Ptr[FGInteractWidget]] = self.GetInteractWidgetStack()
        
        ReturnValue1_1: int32 = len(ReturnValue1_0) - 1
        ReturnValue_2: bool = GreaterEqual_IntInt(ReturnValue1_1, 0)
        if not ReturnValue_2:
            goto('L743')
        ReturnValue_3: List[Ptr[FGInteractWidget]] = self.GetInteractWidgetStack()
        
        ReturnValue_4: int32 = len(ReturnValue_3) - 1
        
        Item = None
        Item = ReturnValue_3[ReturnValue_4]
        Item.OnEscapePressed()
        ReturnValue_5: EventReply = Default__WidgetBlueprintLibrary.Handled()
        ReturnValue_6: EventReply = ReturnValue_5
        goto('L743')
        # Label 666
        ReturnValue_7: EventReply = Default__WidgetBlueprintLibrary.Unhandled()
        ReturnValue_6 = ReturnValue_7
    

    def HUDPanelVisibility(self):
        
        HUD = None
        self.GetFGHud(Ref[HUD])
        ReturnValue: bool = HUD.GetHUDVisibility()
        ReturnValue_0: bool = HUD.GetPumpiMode()
        # Label 107
        ReturnValue_1: bool = Not_PreBool(ReturnValue)
        ReturnValue_2: bool = BooleanOR(ReturnValue_0, ReturnValue_1)
        if not ReturnValue_2:
            goto('L213')
        ReturnValue_3: uint8 = 2
        goto('L233')
        # Label 213
        ReturnValue_3 = 3
    

    def GetMessageNotifierVisibility(self):
        
        HUD = None
        self.GetFGHud(Ref[HUD])
        ReturnValue: bool = HUD.GetPumpiMode()
        ReturnValue_0: bool = self.mMessageBox.HasAnyChildren()
        # Label 107
        ReturnValue_1: bool = Not_PreBool(ReturnValue_0)
        ReturnValue_2: bool = BooleanOR(ReturnValue, ReturnValue_1)
        if not ReturnValue_2:
            goto('L213')
        ReturnValue_3: uint8 = 2
        goto('L233')
        # Label 213
        ReturnValue_3 = 4
    

    def UpdateHUDVisibility(self):
        
        HUD = None
        self.GetFGHud(Ref[HUD])
        ReturnValue: bool = self.mCenterWidgetBox.HasAnyChildren()
        ReturnValue1: bool = self.PopupSlot.HasAnyChildren()
        # Label 107
        ReturnValue_0: bool = BooleanOR(ReturnValue1, ReturnValue)
        ReturnValue_1: bool = Not_PreBool(ReturnValue_0)
        HUD.SetHUDVisibility(ReturnValue_1)
    

    def GetSchematicPopupVisibility(self):
        Variable: uint8 = 2
        Variable1: uint8 = 3
        
        HUD = None
        # Label 40
        self.GetFGHud(Ref[HUD])
        ReturnValue: bool = HUD.GetPumpiMode()
        Variable_0: bool = ReturnValue
        
        switch = {
            False: Variable1,
            True: Variable
        }
        # Label 124
        ReturnValue_0: uint8 = switch.get(Variable_0, None)
    

    def AddMessageNotification(self, newMessage: TSubclassOf[FGMessageBase]):
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_0: Ptr[Widget_MessageNotifier] = Default__WidgetBlueprintLibrary.Create(self, Widget_MessageNotifier, ReturnValue)
        Default__KismetSystemLibrary.SetClassPropertyByName(ReturnValue_0, "mMessage", newMessage)
        ReturnValue_1: Ptr[VerticalBoxSlot] = self.mMessageBox.AddChildToVerticalBox(ReturnValue_0)
    

    def GetItemDropLocation(self):
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        
        OutLocation = None
        OutRotation = None
        ReturnValue.GetActorEyesViewPoint(Ref[OutLocation], Ref[OutRotation])
        ReturnValue_0: Vector = GetForwardVector(OutRotation)
        ReturnValue_1: Vector = ReturnValue_0 * 250
        ReturnValue_2: Vector = OutLocation + ReturnValue_1
        dropLocation = ReturnValue_2
    

    def OnDrop(self):
        ExecutionFlow.Push("L884")
        ExecutionFlow.Push("L865")
        Inventory: Ptr[BP_DragNDropInventory] = Cast[BP_DragNDropInventory](Operation)
        bSuccess: bool = Inventory
        if not bSuccess:
           goto(ExecutionFlow.Pop())
        handled: bool = True
        # Label 96
        Slot: Ptr[Widget_InventorySlot] = Cast[Widget_InventorySlot](Inventory.payload)
        bSuccess2: bool = Slot
        if not bSuccess2:
           goto(ExecutionFlow.Pop())
        
        stack = None
        ReturnValue: bool = Slot.mCachedInventoryComponent.GetStackFromIndex(Slot.mSlotIdx, Ref[stack])
        
        stack = None
        numItems = None
        item = None
        Default__FGInventoryLibrary.BreakInventoryStack(Ref[stack], Ref[numItems], Ref[item])
        
        item = None
        itemClass = None
        itemState = None
        Default__FGInventoryLibrary.BreakInventoryItem(Ref[item], Ref[itemClass], Ref[itemState])
        ReturnValue_0: uint8 = Default__FGItemDescriptor.GetForm(itemClass)
        ReturnValue_1: bool = EqualEqual_ByteByte(ReturnValue_0, 1)
        if not ReturnValue_1:
           goto(ExecutionFlow.Pop())
        ReturnValue_2: Ptr[Pawn] = self.GetOwningPlayerPawn()
        
        stack = None
        location = None
        rotation = None
        Default__FGItemPickup_Spawnable.FindGroundLocationInfrontOfActor(ReturnValue_2, 230, Ref[stack], Ref[location], Ref[rotation])
        ReturnValue_3: Ptr[PlayerController] = self.GetOwningPlayer()
        Controller: Ptr[FGPlayerController] = Cast[FGPlayerController](ReturnValue_3)
        bSuccess1: bool = Controller
        ReturnValue_4: Ptr[BP_RemoteCallObject] = Controller.GetRemoteCallObjectOfClass(BP_RemoteCallObject)
        ReturnValue_4.Server_DropItemIntoStack(Slot.mCachedInventoryComponent, Slot.mSlotIdx, location, rotation)
        goto(ExecutionFlow.Pop())
        # Label 865
        ReturnValue_5: bool = handled
    

    def RefreshInputMode(self):
        ReturnValue1: bool = self.PopupSlot.HasAnyChildren()
        if not ReturnValue1:
            goto('L249')
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_0: Ptr[Widget] = self.PopupSlot.GetChildAt(0)
        Popup: Ptr[Widget_Popup] = Cast[Widget_Popup](ReturnValue_0)
        bSuccess: bool = Popup
        Default__WidgetBlueprintLibrary.SetInputMode_UIOnlyEx(ReturnValue, Popup, 1)
        # End
        # Label 249
        ReturnValue_1: bool = self.mMenuSlot.HasAnyChildren()
        if not ReturnValue_1:
            goto('L310')
        # End
        # Label 310
        ReturnValue2: List[Ptr[FGInteractWidget]] = self.GetInteractWidgetStack()
        
        ReturnValue_2: int32 = len(ReturnValue2)
        ReturnValue_3: bool = ReturnValue_2 > 0
        if not ReturnValue_3:
            goto('L660')
        ReturnValue_4: List[Ptr[FGInteractWidget]] = self.GetInteractWidgetStack()
        
        ReturnValue_5: int32 = len(ReturnValue_4) - 1
        ReturnValue1_0: List[Ptr[FGInteractWidget]] = self.GetInteractWidgetStack()
        
        Item = None
        Item = ReturnValue1_0[ReturnValue_5]
        Item.SetInputMode()
        # End
        # Label 660
        self.ResetInput()
    

    def CreatePopupWidget(self):
        Popup: TSubclassOf[Widget_Popup] = ClassCast[Widget_Popup](PopupData.PopupClass)
        bSuccess: bool = Popup
        if not bSuccess:
            goto('L528')
        PopupClass = Popup
        # Label 107
        self.mPopupBlur.SetBlurStrength(1)
        self.mPopupModal.SetVisibility(0)
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_0: Ptr[Widget_Popup] = Default__WidgetBlueprintLibrary.Create(self, PopupClass, ReturnValue)
        ReturnValue_0.mPopupData = PopupData
        ReturnValue_1: Ptr[PanelSlot] = self.PopupSlot.AddChild(ReturnValue_0)
        ReturnValue = self.GetOwningPlayer()
        Default__WidgetBlueprintLibrary.SetInputMode_UIOnlyEx(ReturnValue, ReturnValue_0, 0)
        ReturnValue = self.GetOwningPlayer()
        # Label 471
        ReturnValue.bShowMouseCursor = True
        ReturnValue_2: Ptr[FGPopupWidget] = ReturnValue_0
        goto('L552')
        # Label 528
        PopupClass = Widget_Popup
        goto('L107')
    

    def GetReloadRespawnText(self):
        ReturnValue: Ptr[Pawn] = self.GetOwningPlayerPawn()
        Player: Ptr[FGCharacterPlayer] = Cast[FGCharacterPlayer](ReturnValue)
        bSuccess1: bool = Player
        if not bSuccess1:
            goto('L635')
        ReturnValue_0: bool = Player.IsAliveAndWell()
        if not ReturnValue_0:
            goto('L660')
        ReturnValue_1: Ptr[FGEquipment] = Player.GetEquipmentInSlot(1)
        AsFGWeapon: Ptr[FGWeapon] = Cast[FGWeapon](ReturnValue_1)
        bSuccess2: bool = AsFGWeapon
        if not bSuccess2:
            goto('L660')
        Variable1: FText = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 298, 'Value': 'Reloading...'}"
        ReturnValue1: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue1_0: FText = Default__FGInputLibrary.FormatStringWithKeyNames(ReturnValue1, "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 432, 'Value': 'Press [{Reload}] to Reload'}", False)
        ReturnValue_2: bool = AsFGWeapon.GetIsReloading()
        Variable: bool = ReturnValue_2
        
        switch = {
            False: ReturnValue1_0,
            True: Variable1
        }
        ReturnValue_3: FText = switch.get(Variable, None)
        goto('L1096')
        # Label 635
        ReturnValue_3 = 
        goto('L1096')
        # Label 660
        ReturnValue2: Ptr[PlayerController] = self.GetOwningPlayer()
        Controller: Ptr[FGPlayerController] = Cast[FGPlayerController](ReturnValue2)
        bSuccess: bool = Controller
        if not bSuccess:
            goto('L1076')
        Variable_0: FText = 
        ReturnValue_4: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_5: FText = Default__FGInputLibrary.FormatStringWithKeyNames(ReturnValue_4, "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 867, 'Value': 'Press [{PrimaryFire}] to respawn'}", False)
        ReturnValue_6: bool = Controller.NeedRespawn()
        Variable1_0: bool = ReturnValue_6
        
        switch_0 = {
            False: Variable_0,
            True: ReturnValue_5
        }
        ReturnValue_3 = switch_0.get(Variable1_0, None)
        goto('L1096')
        # Label 1076
        ReturnValue_3 = 
    

    def GetReloadRespawnTextVisibility(self):
        ReturnValue: Ptr[Pawn] = self.GetOwningPlayerPawn()
        Player: Ptr[FGCharacterPlayer] = Cast[FGCharacterPlayer](ReturnValue)
        bSuccess1: bool = Player
        if not bSuccess1:
            goto('L616')
        ReturnValue_0: bool = Player.IsAliveAndWell()
        if not ReturnValue_0:
            goto('L641')
        ReturnValue_1: Ptr[FGEquipment] = Player.GetEquipmentInSlot(1)
        AsFGWeapon: Ptr[FGWeapon] = Cast[FGWeapon](ReturnValue_1)
        bSuccess2: bool = AsFGWeapon
        if not bSuccess2:
            goto('L641')
        ReturnValue_2: bool = self.mPlayerInteractionMessages.IsVisible()
        ReturnValue_3: bool = Not_PreBool(ReturnValue_2)
        ReturnValue_4: bool = AsFGWeapon.HasAmmunition()
        ReturnValue_5: bool = AsFGWeapon.CanReload()
        ReturnValue1: bool = Not_PreBool(ReturnValue_4)
        ReturnValue1_0: bool = ReturnValue1 and ReturnValue_5
        ReturnValue2: bool = ReturnValue1_0 and ReturnValue_3
        if not ReturnValue2:
            goto('L1003')
        # Label 552
        ReturnValue_6: uint8 = self.HUDPanelVisibility()
        ReturnValue_7: uint8 = ReturnValue_6
        goto('L1023')
        # Label 616
        ReturnValue_7 = 2
        goto('L1023')
        # Label 641
        ReturnValue_8: Ptr[PlayerController] = self.GetOwningPlayer()
        Controller: Ptr[FGPlayerController] = Cast[FGPlayerController](ReturnValue_8)
        bSuccess: bool = Controller
        if not bSuccess:
            goto('L978')
        ReturnValue_9: bool = Default__KismetSystemLibrary.IsValid(Controller)
        ReturnValue_10: bool = Controller.NeedRespawn()
        ReturnValue_11: bool = ReturnValue_9 and ReturnValue_10
        if not ReturnValue_11:
            goto('L953')
        ReturnValue1_1: uint8 = self.HUDPanelVisibility()
        ReturnValue_7 = ReturnValue1_1
        goto('L1023')
        # Label 953
        ReturnValue_7 = 2
        goto('L1023')
        # Label 978
        ReturnValue_7 = 2
        goto('L1023')
        # Label 1003
        ReturnValue_7 = 2
    

    def PopAllWidgets_Internal(self):
        ExecutionFlow.Push("L418")
        ReturnValue1: List[Ptr[FGInteractWidget]] = self.GetInteractWidgetStack()
        
        ReturnValue: int32 = len(ReturnValue1) - 1
        # Label 92
        index = ReturnValue
        # Label 119
        ReturnValue_0: bool = GreaterEqual_IntInt(index, 0)
        # Label 153
        if not ReturnValue_0:
            goto('L389')
        ExecutionFlow.Push("L119")
        ReturnValue_1: List[Ptr[FGInteractWidget]] = self.GetInteractWidgetStack()
        
        Item = None
        Item = ReturnValue_1[index]
        ReturnValue_2: bool = self.PopWidget(Item)
        ReturnValue_3: int32 = index - 1
        Variable: int32 = ReturnValue_3
        index = Variable
        goto(ExecutionFlow.Pop())
        # Label 389
        self.RefreshInputMode()
        self.UpdateHUDVisibility()
        goto(ExecutionFlow.Pop())
    

    def DoesWidgetExist(self, WidgetClass: TSubclassOf[FGInteractWidget]):
        ExecutionFlow.Push("L514")
        Variable: int32 = 0
        Variable_0: int32 = 0
        # Label 51
        ReturnValue: List[Ptr[FGInteractWidget]] = self.GetInteractWidgetStack()
        
        ReturnValue_0: int32 = len(ReturnValue)
        ReturnValue_1: bool = Variable <= ReturnValue_0
        if not ReturnValue_1:
            goto('L424')
        Variable_0 = Variable
        ExecutionFlow.Push("L440")
        ReturnValue = self.GetInteractWidgetStack()
        
        Item = None
        Item = ReturnValue[Variable_0]
        ReturnValue_2: TSubclassOf[FGInteractWidget] = Default__GameplayStatics.GetObjectClass(Item)
        ReturnValue_3: bool = ClassIsChildOf(ReturnValue_2, WidgetClass)
        if not ReturnValue_3:
           goto(ExecutionFlow.Pop())
        doesExist = True
        # End
        # Label 424
        doesExist = False
        # End
        # Label 440
        ReturnValue_4: int32 = Variable + 1
        Variable = ReturnValue_4
        goto('L51')
    

    def GetPlayerInteractionVisibility(self):
        ReturnValue: Ptr[Pawn] = self.GetOwningPlayerPawn()
        Player: Ptr[FGCharacterPlayer] = Cast[FGCharacterPlayer](ReturnValue)
        bSuccess: bool = Player
        if not bSuccess:
            goto('L355')
        ReturnValue = self.GetOwningPlayerPawn()
        # Label 119
        Player = Cast[FGCharacterPlayer](ReturnValue)
        bSuccess = Player
        ReturnValue_0: Ptr[Actor] = Player.GetBestUsableActor()
        ReturnValue_1: bool = Default__KismetSystemLibrary.IsValid(ReturnValue_0)
        if not ReturnValue_1:
            goto('L380')
        ReturnValue_2: uint8 = self.HUDPanelVisibility()
        ReturnValue_3: uint8 = ReturnValue_2
        goto('L400')
        # Label 355
        ReturnValue_3 = 2
        goto('L400')
        # Label 380
        ReturnValue_3 = 2
    

    def Destruct(self):
        self.ExecuteUbergraph_BP_GameUI(5217)
    

    def Play Landed Effect(self, Velocity: float):
        ExecuteUbergraph_BP_GameUI.K2Node_CustomEvent_Velocity = Velocity #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_GameUI(4536)
    

    def ReceivedMessage(self):
        ExecuteUbergraph_BP_GameUI.K2Node_Event_inMessage = inMessage #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_GameUI(1237)
    

    def RemoveAudioMessage(self):
        self.ExecuteUbergraph_BP_GameUI(1412)
    

    def AddIntroTutorialInfo(self):
        ExecuteUbergraph_BP_GameUI.K2Node_Event_tutorialHintData = TutorialHintData #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_GameUI(1427)
    

    def UpdateTutorialInfo(self, hintData: TutorialHintData):
        ExecuteUbergraph_BP_GameUI.K2Node_CustomEvent_hintData = hintData #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_GameUI(1792)
    

    def HandleFocusLost(self):
        self.ExecuteUbergraph_BP_GameUI(1820)
    

    def AddPawnHUD(self):
        ExecuteUbergraph_BP_GameUI.K2Node_Event_newContent = newContent #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_GameUI(2626)
    

    def RemovePawnHUD(self):
        self.ExecuteUbergraph_BP_GameUI(2746)
    

    def AddInteractWidget(self):
        ExecuteUbergraph_BP_GameUI.K2Node_Event_widgetToAdd = widgetToAdd #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_GameUI(2783)
    

    def OnPlayerBeginTypeMessage(self):
        self.ExecuteUbergraph_BP_GameUI(3158)
    

    def Construct(self):
        self.ExecuteUbergraph_BP_GameUI(3344)
    

    def OnChatMessageReceived(self):
        self.ExecuteUbergraph_BP_GameUI(3837)
    

    def ClearHintOnTutorialStepCompleted(self):
        self.ExecuteUbergraph_BP_GameUI(3874)
    

    def ShowRespawnMessage(self):
        self.ExecuteUbergraph_BP_GameUI(3962)
    

    def ClosePopup(self):
        self.ExecuteUbergraph_BP_GameUI(4541)
    

    def OnReceiveRadiationStart(self):
        self.ExecuteUbergraph_BP_GameUI(4546)
    

    def OnReceiveRadiationStop(self):
        self.ExecuteUbergraph_BP_GameUI(4589)
    

    def OnRadiationIntensityUpdated(self):
        ExecuteUbergraph_BP_GameUI.K2Node_Event_radiationIntensity = radiationIntensity #  PERSISTENT_FRAME(
        ExecuteUbergraph_BP_GameUI.K2Node_Event_radiationImmunity = radiationImmunity #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_GameUI(4632)
    

    def ForceStopRadiationUI(self):
        self.ExecuteUbergraph_BP_GameUI(4708)
    

    def PushWidget(self):
        ExecuteUbergraph_BP_GameUI.K2Node_Event_Widget = Widget #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_GameUI(4907)
    

    def ShowDirectionalSubtitle(self):
        ExecuteUbergraph_BP_GameUI.K2Node_Event_Subtitle = Subtitle #  PERSISTENT_FRAME(
        ExecuteUbergraph_BP_GameUI.K2Node_Event_Instigator1 = Instigator #  PERSISTENT_FRAME(
        ExecuteUbergraph_BP_GameUI.K2Node_Event_Duration = Duration #  PERSISTENT_FRAME(
        ExecuteUbergraph_BP_GameUI.K2Node_Event_bUseDuration = bUseDuration #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_GameUI(5017)
    

    def StopSubtitle(self):
        ExecuteUbergraph_BP_GameUI.K2Node_Event_Instigator = Instigator #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_GameUI(5022)
    

    def EventUpdateHUDScaling(self):
        self.ExecuteUbergraph_BP_GameUI(5068)
    

    def PlayAudioMessage(self):
        ExecuteUbergraph_BP_GameUI.K2Node_Event_messageClass = MessageClass #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_GameUI(5237)
    

    def OnResumeGame(self):
        self.ExecuteUbergraph_BP_GameUI(5524)
    

    def ShowQuickSearch(self):
        self.ExecuteUbergraph_BP_GameUI(5561)
    

    def CreateBreakNotification(self):
        self.ExecuteUbergraph_BP_GameUI(5599)
    

    def PopAllWidgets(self):
        self.ExecuteUbergraph_BP_GameUI(7186)
    

    def OnInitialized(self):
        self.ExecuteUbergraph_BP_GameUI(7319)
    

    def OnAutosaveStart(self, TimeUntilAutosave: float):
        ExecuteUbergraph_BP_GameUI.K2Node_CustomEvent_TimeUntilAutosave = TimeUntilAutosave #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_GameUI(7918)
    

    def OnAutosaveFinished(self):
        self.ExecuteUbergraph_BP_GameUI(7964)
    

    def ResetInput(self):
        self.ExecuteUbergraph_BP_GameUI(8001)
    

    def ExecuteUbergraph_BP_GameUI(self):
        goto(ComputedJump("EntryPoint"))
        # Label 15
        ReturnValue: Ptr[GameStateBase] = Default__GameplayStatics.GetGameState(self)
        ReturnValue_0: Ptr[FGChatManager] = Default__FGChatManager.Get(ReturnValue)
        ReturnValue1: bool = Default__KismetSystemLibrary.IsValid(ReturnValue_0)
        if not ReturnValue1:
            goto('L369')
        ReturnValue = Default__GameplayStatics.GetGameState(self)
        ReturnValue_0 = Default__FGChatManager.Get(ReturnValue)
        OutputDelegate1.BindUFunction(self, OnChatMessageReceived)
        ReturnValue_0.OnChatMessageAdded.AddUnique(OutputDelegate1)
        self.mChatWindow.UpdateVisibility()
        goto(ExecutionFlow.Pop())
        # Label 369
        Default__KismetSystemLibrary.Delay(self, 0.20000000298023224, LatentActionInfo(Linkage = 15, UUID = -1918412098, ExecutionFunction = "ExecuteUbergraph_BP_GameUI", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        ReturnValue_1: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.FadeAnim, 0, 1, 0, 1)
        goto(ExecutionFlow.Pop())
        # Label 493
        self.UpdateHUDVisibility()
        goto(ExecutionFlow.Pop())
        # Label 508
        ReturnValue_2: Ptr[PlayerController] = self.GetOwningPlayer()
        Controller: Ptr[FGPlayerController] = Cast[FGPlayerController](ReturnValue_2)
        bSuccess: bool = Controller
        if not bSuccess:
           goto(ExecutionFlow.Pop())
        self.AddInteractWidget(Widget)
        ReturnValue_3: Ptr[PanelSlot] = self.mCenterWidgetBox.AddChild(Widget)
        Slot: Ptr[HorizontalBoxSlot] = Cast[HorizontalBoxSlot](ReturnValue_3)
        bSuccess5: bool = Slot
        if not bSuccess5:
           goto(ExecutionFlow.Pop())
        ReturnValue_4: uint8 = Widget.GetDesiredHorizontalAlignment()
        Slot.SetHorizontalAlignment(ReturnValue_4)
        ReturnValue_5: uint8 = Widget.GetDesiredVerticalAlignment()
        Slot.SetVerticalAlignment(ReturnValue_5)
        ReturnValue_6: SlateChildSize = Widget.GetDesiredAlignmentSize()
        Slot.SetSize(ReturnValue_6)
        ReturnValue_7: List[Ptr[FGInteractWidget]] = self.GetInteractWidgetStack()
        
        ReturnValue_8: int32 = len(ReturnValue_7)
        ReturnValue_9: bool = EqualEqual_IntInt(ReturnValue_8, 1)
        if not ReturnValue_9:
           goto(ExecutionFlow.Pop())
        Widget.SetupDefaultFocus()
        Widget.SetInputMode()
        goto('L493')
        Message: TSubclassOf[FGAudioMessage] = ClassCast[FGAudioMessage](inMessage)
        bSuccess_0: bool = Message
        if not bSuccess_0:
            goto('L1340')
        self.PlayAudioMessage(Message)
        goto(ExecutionFlow.Pop())
        # Label 1340
        self.AddMessageNotification(inMessage)
        goto(ExecutionFlow.Pop())
        # Label 1364
        self.mAudioMessageSlot.ClearChildren()
        self.SetCurrentAudioMessage(None)
        goto(ExecutionFlow.Pop())
        self.RemoveAudioMessage()
        goto('L1364')
        self.UpdateTutorialInfo(tutorialHintData)
        ReturnValue1_0: Ptr[PlayerController] = self.GetOwningPlayer()
        Controller1: Ptr[FGPlayerController] = Cast[FGPlayerController](ReturnValue1_0)
        bSuccess1: bool = Controller1
        if not bSuccess1:
           goto(ExecutionFlow.Pop())
        ReturnValue_10: bool = Default__KismetSystemLibrary.IsValidClass(tutorialHintData.MESSAGE)
        if not ReturnValue_10:
           goto(ExecutionFlow.Pop())
        ReturnValue_11: bool = Controller1.GetPlayerHasMessage(tutorialHintData.MESSAGE)
        ReturnValue_12: bool = Not_PreBool(ReturnValue_11)
        if not ReturnValue_12:
            goto('L1777')
        Controller1.Client_AddMessage(tutorialHintData.MESSAGE)
        goto(ExecutionFlow.Pop())
        # Label 1777
        self.ShowTutorialHint()
        goto(ExecutionFlow.Pop())
        self.mCachedTutorialHintData = hintData
        goto(ExecutionFlow.Pop())
        ReturnValue_13: int32 = self.mMenuSlot.GetChildrenCount()
        ReturnValue_14: bool = ReturnValue_13 > 0
        if not ReturnValue_14:
            goto('L2118')
        ReturnValue_15: Ptr[Widget] = self.mMenuSlot.GetChildAt(0)
        Base: Ptr[BP_MenuBase] = Cast[BP_MenuBase](ReturnValue_15)
        bSuccess2: bool = Base
        ReturnValue2: Ptr[PlayerController] = self.GetOwningPlayer()
        Base.mFocusWidget.SetUserFocus(ReturnValue2)
        goto(ExecutionFlow.Pop())
        # Label 2118
        ReturnValue1_1: List[Ptr[FGInteractWidget]] = self.GetInteractWidgetStack()
        
        ReturnValue1_2: int32 = len(ReturnValue1_1)
        ReturnValue1_3: bool = ReturnValue1_2 > 0
        if not ReturnValue1_3:
           goto(ExecutionFlow.Pop())
        ReturnValue2_0: List[Ptr[FGInteractWidget]] = self.GetInteractWidgetStack()
        
        Item = None
        Item = ReturnValue2_0[0]
        ReturnValue_16: Ptr[Widget] = Item.GetDefaultFocusWidget()
        ReturnValue_17: bool = Default__KismetSystemLibrary.IsValid(ReturnValue_16)
        if not ReturnValue_17:
           goto(ExecutionFlow.Pop())
        ReturnValue2_0 = self.GetInteractWidgetStack()
        
        Item = None
        Item = ReturnValue2_0[0]
        ReturnValue_16 = Item.GetDefaultFocusWidget()
        ReturnValue3: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_16.SetUserFocus(ReturnValue3)
        goto(ExecutionFlow.Pop())
        ReturnValue_18: Ptr[OverlaySlot] = self.mPawnHUDOverlay.AddChildToOverlay(newContent)
        ReturnValue_18.SetVerticalAlignment(0)
        ReturnValue_18.SetHorizontalAlignment(0)
        goto(ExecutionFlow.Pop())
        self.mPawnHUDOverlay.ClearChildren()
        goto(ExecutionFlow.Pop())
        self.AddInteractWidget(widgetToAdd)
        Base_0: Ptr[Widget_UseableBase] = Cast[Widget_UseableBase](widgetToAdd)
        bSuccess3: bool = Base_0
        if not bSuccess3:
           goto(ExecutionFlow.Pop())
        ReturnValue4: Ptr[PlayerController] = self.GetOwningPlayer()
        Controller2: Ptr[FGPlayerController] = Cast[FGPlayerController](ReturnValue4)
        bSuccess4: bool = Controller2
        if not bSuccess4:
            goto('L3082')
        ReturnValue_19: TSubclassOf[Widget_UseableBase] = Default__GameplayStatics.GetObjectClass(Base_0)
        Controller2.OnToggleInteractionUI.ProcessMulticastDelegate(True, ReturnValue_19)
        # Label 3082
        OutputDelegate.BindUFunction(self, OnInventorySlotStackMove)
        Base_0.InventorySlotStackMoveEvent.AddUnique(OutputDelegate)
        goto(ExecutionFlow.Pop())
        # Label 3147
        self.PopPopupQueue()
        goto(ExecutionFlow.Pop())
        ReturnValue3_0: List[Ptr[FGInteractWidget]] = self.GetInteractWidgetStack()
        
        ReturnValue2_1: int32 = len(ReturnValue3_0)
        ReturnValue2_2: bool = ReturnValue2_1 > 0
        if not ReturnValue2_2:
            goto('L3307')
        self.PopAllWidgets()
        # Label 3307
        self.mChatWindow.OnPlayerBeginTypeMessage()
        goto(ExecutionFlow.Pop())
        self.Construct()
        ExecutionFlow.Push("L3715")
        ExecutionFlow.Push("L3547")
        ReturnValue_20: FString = Default__FGVersionFunctionLibrary.GetVersionString()
        ReturnValue_21: FText = Default__KismetTextLibrary.Conv_StringToText(ReturnValue_20)
        self.mVersionLabel.SetText(ReturnValue_21)
        self.GetExperimentalVisibility()
        self.SetVersionLabelPosition()
        goto(ExecutionFlow.Pop())
        # Label 3547
        ReturnValue10: Ptr[PlayerController] = self.GetOwningPlayer()
        Controller_0: Ptr[BP_PlayerController] = Cast[BP_PlayerController](ReturnValue10)
        bSuccess8: bool = Controller_0
        if not bSuccess8:
           goto(ExecutionFlow.Pop())
        OutputDelegate6.BindUFunction(self, OnPlayerBeginTypeMessage)
        Controller_0.OnBeginTypeChat.AddUnique(OutputDelegate6)
        goto('L15')
        # Label 3715
        ReturnValue1_4: Ptr[FGGameUserSettings] = Default__FGGameUserSettings.GetFGGameUserSettings()
        OutputDelegate3.BindUFunction(self, EventUpdateHUDScaling)
        
        OutputDelegate3 = None
        ReturnValue1_4.SubscribeToDynamicOptionUpdate("FG.HUDScaling", Ref[OutputDelegate3])
        goto(ExecutionFlow.Pop())
        self.mChatWindow.OnChatMessageReceived()
        goto(ExecutionFlow.Pop())
        self.mTutorialInfoSlot.ClearChildren()
        self.mCachedTutorialHintData = TutorialHintData(ID = 0, Title = , HintTexts = List[TextProperty /Script/FactoryGame.TutorialHintData:HintTexts.HintTexts]([]), MESSAGE = None)
        goto(ExecutionFlow.Pop())
        self.mHudContainer.SetRenderOpacity(0)
        self.Widget_FicsitLogoSplash.ShowLogo()
        ReturnValue_22: float = self.Widget_FicsitLogoSplash.SpawnAnim.GetEndTime()
        Default__KismetSystemLibrary.Delay(self, ReturnValue_22, LatentActionInfo(Linkage = 446, UUID = -33259864, ExecutionFunction = "ExecuteUbergraph_BP_GameUI", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        # Label 4188
        ReturnValue_23: Ptr[FGPopupWidget] = self.GetPopup()
        ReturnValue_23.RemoveFromParent()
        self.SetPopup(None)
        self.mPopupBlur.SetBlurStrength(0)
        self.mPopupModal.SetVisibility(2)
        self.PopupSlot.ClearChildren()
        self.RefreshInputMode()
        self.UpdateHUDVisibility()
        goto(ExecutionFlow.Pop())
        # Label 4399
        ReturnValue_23 = self.GetPopup()
        ReturnValue2_3: bool = Default__KismetSystemLibrary.IsValid(ReturnValue_23)
        if not ReturnValue2_3:
            goto('L3147')
        goto('L4188')
        # Label 4489
        ReturnValue1_5: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.JumpLand, 0, 1, 0, 1)
        goto(ExecutionFlow.Pop())
        goto('L4489')
        goto('L4399')
        self.Widget_TakeDamage.UpdateRadiation(True, 0)
        goto(ExecutionFlow.Pop())
        # Label 4589
        self.Widget_TakeDamage.UpdateRadiation(False, 0)
        goto(ExecutionFlow.Pop())
        self.Widget_TakeDamage.UpdateRadiation(True, radiationIntensity)
        goto(ExecutionFlow.Pop())
        # Label 4679
        self.PopAllWidgets_Internal()
        self.ClosePopup()
        goto(ExecutionFlow.Pop())
        goto('L4589')
        # Label 4713
        ReturnValue_24: Ptr[FGGameUserSettings] = Default__FGGameUserSettings.GetFGGameUserSettings()
        ReturnValue_25: bool = ReturnValue_24.GetBoolOptionValue("FG.UseDirectionalSubtitle")
        if not ReturnValue_25:
           goto(ExecutionFlow.Pop())
        self.Widget_DirectionalSubtitlesContainer.CreateSubtitle(Subtitle, Instigator1, Duration, bUseDuration)
        goto(ExecutionFlow.Pop())
        goto('L508')
        # Label 4912
        self.ResetInput()
        ReturnValue3_1: Ptr[FGGameUserSettings] = Default__FGGameUserSettings.GetFGGameUserSettings()
        ReturnValue3_1.UnsubscribeToAllDynamicOptionUpdate(self)
        goto(ExecutionFlow.Pop())
        # Label 5002
        self.Destruct()
        goto('L4912')
        goto('L4713')
        
        Instigator = None
        self.Widget_DirectionalSubtitlesContainer.StopSubtitle(Ref[Instigator])
        goto(ExecutionFlow.Pop())
        ReturnValue2_4: Ptr[FGGameUserSettings] = Default__FGGameUserSettings.GetFGGameUserSettings()
        ReturnValue_26: float = ReturnValue2_4.GetFloatOptionValue("FG.HUDScaling")
        self.mHUDScaler.SetUserSpecifiedScale(ReturnValue_26)
        goto(ExecutionFlow.Pop())
        goto('L5002')
        # Label 5222
        self.PopAllWidgets()
        goto('L4679')
        ReturnValue5: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_27: Ptr[FGAudioMessage] = Default__WidgetBlueprintLibrary.Create(self, messageClass, ReturnValue5)
        ReturnValue_28: bool = EqualEqual_ByteByte(ReturnValue_27.mType, 1)
        if not ReturnValue_28:
            goto('L5453')
        OutputDelegate2.BindUFunction(self, ShowTutorialHint)
        ReturnValue_27.AssignOnConcludedDelegate(OutputDelegate2)
        # Label 5453
        ReturnValue1_6: Ptr[PanelSlot] = self.mAudioMessageSlot.AddChild(ReturnValue_27)
        self.SetCurrentAudioMessage(ReturnValue_27)
        goto(ExecutionFlow.Pop())
        self.mMenuSlot.ClearChildren()
        goto(ExecutionFlow.Pop())
        self.BPW_QuickSearch.SetQuickSearchVisibility(True)
        goto(ExecutionFlow.Pop())
        ReturnValue6: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_29: float = ReturnValue6.GetGameTimeSinceCreation()
        ReturnValue_30: int32 = FFloor(ReturnValue_29)
        ReturnValue_31: float = Conv_IntToFloat(ReturnValue_30)
        ReturnValue_32: float = ReturnValue_31 / 7200
        ReturnValue1_7: int32 = FFloor(ReturnValue_32)
        ReturnValue1_8: float = Conv_IntToFloat(ReturnValue1_7)
        ReturnValue_33: bool = EqualEqual_FloatFloat(ReturnValue_32, ReturnValue1_8)
        if not ReturnValue_33:
           goto(ExecutionFlow.Pop())
        ReturnValue4_0: Ptr[FGGameUserSettings] = Default__FGGameUserSettings.GetFGGameUserSettings()
        
        ReturnValue3_2: int32 = len(self.mPlaytimeWarningMessages)
        ReturnValue3_3: bool = ReturnValue3_2 > 0
        ReturnValue_34: bool = ReturnValue4_0.GetShowBreakNotification()
        ReturnValue_35: bool = ReturnValue_34 and ReturnValue3_3
        if not ReturnValue_35:
           goto(ExecutionFlow.Pop())
        
        ReturnValue3_2 = len(self.mPlaytimeWarningMessages)
        ReturnValue_36: int32 = RandomInteger(ReturnValue3_2)
        self.mPlaytimeWarningMessageIndex = ReturnValue_36
        ReturnValue7: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue1_9: Ptr[Widget_WaterNotifier] = Default__WidgetBlueprintLibrary.Create(self, Widget_WaterNotifier, ReturnValue7)
        
        Item1 = None
        Item1 = self.mPlaytimeWarningMessages[0]
        
        Item1 = None
        Default__KismetSystemLibrary.SetTextPropertyByName(ReturnValue1_9, "mText", Ref[Item1])
        ReturnValue6 = self.GetOwningPlayer()
        ReturnValue_29 = ReturnValue6.GetGameTimeSinceCreation()
        ReturnValue_30 = FFloor(ReturnValue_29)
        ReturnValue_31 = Conv_IntToFloat(ReturnValue_30)
        ReturnValue_32 = ReturnValue_31 / 7200
        ReturnValue1_7 = FFloor(ReturnValue_32)
        ReturnValue_37: int32 = ReturnValue1_7 * 2
        FormatArgumentData.ArgumentName = "A"
        FormatArgumentData.ArgumentValueType = 0
        FormatArgumentData.ArgumentValue = 
        FormatArgumentData.ArgumentValueInt = ReturnValue_37
        FormatArgumentData.ArgumentValueFloat = 0
        FormatArgumentData.ArgumentValueGender = 0
        Array: List[FormatArgumentData] = [FormatArgumentData]
        ReturnValue_38: FText = Default__KismetTextLibrary.Format("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 6987, 'Value': 'You have been playing for {A} hours.'}", Array)
        
        Default__KismetSystemLibrary.SetTextPropertyByName(ReturnValue1_9, "mTitleMessageText", Ref[ReturnValue_38])
        ReturnValue2_5: Ptr[PanelSlot] = self.mBreakNotificationBox.AddChild(ReturnValue1_9)
        goto(ExecutionFlow.Pop())
        goto('L5222')
        # Label 7191
        ReturnValue8: Ptr[PlayerController] = self.GetOwningPlayer()
        Default__FGVirtualCursorFunctionLibrary.DisableVirtualCursor(ReturnValue8)
        goto(ExecutionFlow.Pop())
        # Label 7257
        ReturnValue8 = self.GetOwningPlayer()
        ReturnValue8.bShowMouseCursor = False
        goto('L7191')
        ReturnValue1_10: Ptr[GameStateBase] = Default__GameplayStatics.GetGameState(self)
        State: Ptr[FGGameState] = Cast[FGGameState](ReturnValue1_10)
        bSuccess7: bool = State
        if not bSuccess7:
           goto(ExecutionFlow.Pop())
        self.mFGGameState = State
        OutputDelegate4.BindUFunction(self, OnAutosaveStart)
        self.mFGGameState.mOnAutoSaveTimeNotification.AddUnique(OutputDelegate4)
        OutputDelegate5.BindUFunction(self, OnAutosaveFinished)
        self.mFGGameState.mOnAutoSaveFinished.AddUnique(OutputDelegate5)
        goto(ExecutionFlow.Pop())
        # Label 7585
        ReturnValue9: Ptr[PlayerController] = self.GetOwningPlayer()
        Default__WidgetBlueprintLibrary.SetInputMode_GameOnly(ReturnValue9)
        ReturnValue_39: Ptr[Pawn] = self.GetOwningPlayerPawn()
        ReturnValue_40: Ptr[Controller] = ReturnValue_39.GetController()
        Controller_1: Ptr[PlayerController] = Cast[PlayerController](ReturnValue_40)
        bSuccess6: bool = Controller_1
        if not bSuccess6:
           goto(ExecutionFlow.Pop())
        Controller_1.ResetIgnoreInputFlags()
        goto('L7257')
        # Label 7828
        ReturnValue9 = self.GetOwningPlayer()
        ReturnValue3_4: bool = Default__KismetSystemLibrary.IsValid(ReturnValue9)
        if not ReturnValue3_4:
           goto(ExecutionFlow.Pop())
        goto('L7585')
        self.BPW_AutosaveNotification.OnAutosaveStarting(TimeUntilAutosave)
        goto(ExecutionFlow.Pop())
        self.BPW_AutosaveNotification.OnAutosaveFinished()
        goto(ExecutionFlow.Pop())
        goto('L7828')
    
