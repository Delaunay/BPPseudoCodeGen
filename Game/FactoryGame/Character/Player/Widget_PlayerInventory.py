
from codegen.ue4_stub import *

from Script.FactoryGame import FGEquipmentDescriptor
from Script.FactoryGame import FGCharacterPlayer
from Script.UMG import GetChildIndex
from Script.InputCore import Key
from Script.UMG import AddChild
from Script.Engine import FTrunc
from Script.Engine import Default__KismetSystemLibrary
from Script.UMG import GetChildAt
from Script.UMG import Handled
from Script.Engine import IsValid
from Game.FactoryGame.Character.Player.Widget_PlayerInventory import ExecuteUbergraph_Widget_PlayerInventory
from Script.UMG import Destruct
from Script.Engine import EqualEqual_IntInt
from Script.Engine import Default__KismetTextLibrary
from Script.Engine import Conv_StringToText
from Script.UMG import Construct
from Script.FactoryGame import Init
from Script.Engine import Default__KismetStringLibrary
from Script.UMG import Create
from Script.Engine import GetGameState
from Script.FactoryGame import GetSizeLinear
from Script.FactoryGame import GetEquipmentSlot
from Script.UMG import RemoveChildAt
from Script.FactoryGame import FGPlayerController
from Script.Engine import Pawn
from Script.UMG import GetChildrenCount
from Game.FactoryGame.Interface.UI.InGame.Widget_Button import Widget_Button
from Script.Engine import HUD
from Script.Engine import Default__KismetArrayLibrary
from Script.Engine import GameStateBase
from Script.FactoryGame import SortInventory
from Script.FactoryGame import FGInventoryComponent
from Script.Engine import GetHUD
from Script.FactoryGame import GetTotalPlayerArmEquipmentSlots
from Script.FactoryGame import FGInteractWidget
from Game.FactoryGame.Character.Player.Widget_PlayerInventory import ExecuteUbergraph_Widget_PlayerInventory.K2Node_Event_IsDesignTime
from Script.Engine import SetMouseLocation
from Script.Engine import GetKey
from Script.Engine import Conv_IntToString
from Script.Engine import EqualEqual_KeyKey
from Script.FactoryGame import GetStorageInventory
from Script.FactoryGame import Default__FGCentralStorageSubsystem
from Script.UMG import EventReply
from Game.FactoryGame.Character.Player.Widget_PlayerInventory import ExecuteUbergraph_Widget_PlayerInventory.K2Node_CustomEvent_ClickedButton
from Script.FactoryGame import FGCentralStorageContainer
from Script.UMG import SetUserFocus
from Script.UMG import Default__WidgetLayoutLibrary
from Script.UMG import PanelSlot
from Script.FactoryGame import SetShowInventory
from Script.FactoryGame import Get
from Script.Engine import PlayerController
from Script.UMG import Unhandled
from Script.UMG import Default__WidgetBlueprintLibrary
from Script.Engine import BreakVector2D
from Script.Engine import Default__GameplayStatics
from Script.UMG import HasFocusedDescendants
from Script.FactoryGame import GetGameUI
from Script.FactoryGame import SetWindowWantsInventoryAddon
from Script.FactoryGame import FGGameUI
from Game.FactoryGame.Character.Player.Widget_PlayerInventoryAddon import Widget_PlayerInventoryAddon
from Game.FactoryGame.Character.Player.Widget_PlayerInventory import ExecuteUbergraph_Widget_PlayerInventory.K2Node_ComponentBoundEvent_InventorySlot
from Script.FactoryGame import GetRemoteCallObjectOfClass
from Script.FactoryGame import FGItemDescriptor
from Script.CoreUObject import Vector2D
from Script.FactoryGame import FGCentralStorageSubsystem
from Game.FactoryGame.Character.Player.BP_RemoteCallObject import BP_RemoteCallObject
from Script.Engine import Default__KismetInputLibrary
from Script.UMG import GetViewportSize
from Script.Engine import Not_PreBool
from Script.FactoryGame import GetCentralStorageContainers
from Script.FactoryGame import FGInventoryComponentEquipment
from Game.FactoryGame.Resource.BP_HealthGainDescriptor import BP_HealthGainDescriptor
from Script.Engine import BooleanOR
from Script.UMG import Widget
from Script.FactoryGame import FGHUD
from Script.UMG import GetOwningPlayerPawn
from Script.Engine import Concat_StrStr

class Widget_PlayerInventory(FGInteractWidget):
    mInventoryComponent: Ptr[FGInventoryComponent]
    mEquipmentArmsInventoryComponent: Ptr[FGInventoryComponent]
    mEquipmentBackInventoryComponent: Ptr[FGInventoryComponent]
    mBeltIntentoryComponent: Ptr[FGInventoryComponent]
    mTrashInventoryComponent: Ptr[FGInventoryComponent]
    mExtraInputToPassThrough: List[FName]
    mInventorySlotItemClass: TSubclassOf[FGItemDescriptor]
    mCentralStorages: List[Ptr[FGCentralStorageContainer]]
    mShowCentralStorageIfPossible: bool
    mUseMouse = True
    mRestoreFocusWhenLost = True
    mInputToPassThrough = ['inventory']
    mDesiredHorizontalAlignment = 2
    mDesiredVerticalAlignment = 2
    mUseGamepadCursor = True
    mCallCustomTickOnConstruct = True
    Priority = 10
    
    def OnKeyUp(self):
        ReturnValue: bool = self.mInventory.HasFocusedDescendants()
        ReturnValue_0: bool = Not_PreBool(ReturnValue)
        if not ReturnValue_0:
            goto('L175')
        ReturnValue_1: EventReply = self.mInventory.OnNumKeyDown(InKeyEvent)
        ReturnValue_2: EventReply = ReturnValue_1
    

    def SetupArmInventoryResize(self):
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        Controller: Ptr[FGPlayerController] = Cast[FGPlayerController](ReturnValue)
        bSuccess1: bool = Controller
        if not bSuccess1:
            goto('L401')
        ReturnValue_0: Ptr[Pawn] = self.GetOwningPlayerPawn()
        Player: Ptr[FGCharacterPlayer] = Cast[FGCharacterPlayer](ReturnValue_0)
        bSuccess: bool = Player
        if not bSuccess:
            goto('L401')
        ReturnValue_1: int32 = Player.GetTotalPlayerArmEquipmentSlots()
        ReturnValue_2: Ptr[BP_RemoteCallObject] = Controller.GetRemoteCallObjectOfClass(BP_RemoteCallObject)
        ReturnValue_3: Ptr[FGInventoryComponentEquipment] = Player.GetEquipmentSlot(1)
        ReturnValue_2.Server_ResizeInventory(ReturnValue_1, ReturnValue_3)
    

    def IsArmEquipmentInventoryOutdated(self):
        ReturnValue: Ptr[Pawn] = self.GetOwningPlayerPawn()
        Player: Ptr[FGCharacterPlayer] = Cast[FGCharacterPlayer](ReturnValue)
        bSuccess: bool = Player
        if not bSuccess:
            goto('L300')
        ReturnValue_0: Ptr[FGInventoryComponentEquipment] = Player.GetEquipmentSlot(1)
        ReturnValue_1: int32 = Player.GetTotalPlayerArmEquipmentSlots()
        ReturnValue_2: int32 = ReturnValue_0.GetSizeLinear()
        ReturnValue_3: bool = ReturnValue_1 != ReturnValue_2
        isOutdated = ReturnValue_3
    

    def OnPreviewKeyDown(self):
        
        ReturnValue: Key = Default__KismetInputLibrary.GetKey(Ref[InKeyEvent])
        ReturnValue_0: bool = Default__KismetInputLibrary.EqualEqual_KeyKey(ReturnValue, Key(KeyName = "Tab"))
        if not ReturnValue_0:
            goto('L247')
        self.OnEscapePressed()
        ReturnValue_1: EventReply = Default__WidgetBlueprintLibrary.Handled()
        ReturnValue_2: EventReply = ReturnValue_1
        goto('L324')
        # Label 247
        ReturnValue_3: EventReply = Default__WidgetBlueprintLibrary.Unhandled()
        ReturnValue_2 = ReturnValue_3
    

    def OnDrop(self):
        ReturnValue = True
    

    def TryGetCentralStorages(self):
        ReturnValue: Ptr[GameStateBase] = Default__GameplayStatics.GetGameState(self)
        ReturnValue_0: Ptr[FGCentralStorageSubsystem] = Default__FGCentralStorageSubsystem.Get(ReturnValue)
        ReturnValue_1: List[Ptr[FGCentralStorageContainer]] = ReturnValue_0.GetCentralStorageContainers()
        self.mCentralStorages = ReturnValue_1
    

    def OnKeyDown(self):
        
        ReturnValue: Key = Default__KismetInputLibrary.GetKey(Ref[InKeyEvent])
        ReturnValue_0: bool = Default__KismetInputLibrary.EqualEqual_KeyKey(ReturnValue, Key(KeyName = "I"))
        ReturnValue1: bool = Default__KismetInputLibrary.EqualEqual_KeyKey(ReturnValue, Key(KeyName = "Tab"))
        ReturnValue_1: bool = BooleanOR(ReturnValue1, ReturnValue_0)
        if not ReturnValue_1:
            goto('L363')
        self.OnEscapePressed()
        ReturnValue_2: EventReply = Default__WidgetBlueprintLibrary.Handled()
        ReturnValue_3: EventReply = ReturnValue_2
        goto('L440')
        # Label 363
        ReturnValue_4: EventReply = Default__WidgetBlueprintLibrary.Unhandled()
        ReturnValue_3 = ReturnValue_4
    

    def Cleanup(self):
        self.mInventory.OnClose.Clear()
        self.mEquipmentWindowContainer.OnClose.Clear()
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_0: Ptr[HUD] = ReturnValue.GetHUD()
        AsFGHUD: Ptr[FGHUD] = Cast[FGHUD](ReturnValue_0)
        bSuccess: bool = AsFGHUD
        ReturnValue_1: Ptr[FGGameUI] = AsFGHUD.GetGameUI()
        ReturnValue_1.SetWindowWantsInventoryAddon(False)
        ReturnValue = self.GetOwningPlayer()
        ReturnValue_0 = ReturnValue.GetHUD()
        AsFGHUD = Cast[FGHUD](ReturnValue_0)
        bSuccess = AsFGHUD
        # Label 401
        ReturnValue_1 = AsFGHUD.GetGameUI()
        ReturnValue_1.SetShowInventory(False)
    

    def SetInventoryComponents(self, inventoryComponent: Ptr[FGInventoryComponent], arms: Ptr[FGInventoryComponent], Back: Ptr[FGInventoryComponent], head: Ptr[FGInventoryComponent], trash: Ptr[FGInventoryComponent]):
        self.mInventoryComponent = inventoryComponent
        self.mEquipmentArmsInventoryComponent = arms
        self.mEquipmentBackInventoryComponent = Back
        self.mBeltIntentoryComponent = head
        self.mTrashInventoryComponent = trash
    

    def Init(self):
        self.ExecuteUbergraph_Widget_PlayerInventory(2751)
    

    def CloseInventory(self):
        self.ExecuteUbergraph_Widget_PlayerInventory(3274)
    

    def Destruct(self):
        self.ExecuteUbergraph_Widget_PlayerInventory(3289)
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_PlayerInventory(3314)
    

    def CentralStorageButtonClicked(self, ClickedButton: Ptr[Widget_Button]):
        ExecuteUbergraph_Widget_PlayerInventory.K2Node_CustomEvent_ClickedButton = ClickedButton #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_PlayerInventory(3329)
    

    def OnCentralStorageAddedOrRemoved(self):
        self.ExecuteUbergraph_Widget_PlayerInventory(3880)
    

    def BndEvt__Widget_StandardButton_K2Node_ComponentBoundEvent_1_OnClicked__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_PlayerInventory(3932)
    

    def PreConstruct(self):
        ExecuteUbergraph_Widget_PlayerInventory.K2Node_Event_IsDesignTime = IsDesignTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_PlayerInventory(3937)
    

    def BndEvt__mInventory_K2Node_ComponentBoundEvent_0_OnRelevantShortcutPressed__DelegateSignature(self, InventorySlot: Ptr[Widget_InventorySlot]):
        ExecuteUbergraph_Widget_PlayerInventory.K2Node_ComponentBoundEvent_InventorySlot = InventorySlot #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_PlayerInventory(4350)
    

    def ExecuteUbergraph_Widget_PlayerInventory(self):
        goto(ComputedJump("EntryPoint"))
        # Label 15
        ReturnValue: bool = EqualEqual_IntInt(Variable, 0)
        if not ReturnValue:
           goto(ExecutionFlow.Pop())
        
        Item = None
        Item = self.mCentralStorages[Variable]
        ReturnValue_0: Ptr[FGInventoryComponent] = Item.GetStorageInventory()
        self.mCentralStorageInventory.Init(ReturnValue_0)
        goto(ExecutionFlow.Pop())
        # Label 206
        ReturnValue_1: Ptr[Widget] = self.mInventory.InventorySlot.GetChildAt(0)
        Addon: Ptr[Widget_PlayerInventoryAddon] = Cast[Widget_PlayerInventoryAddon](ReturnValue_1)
        bSuccess: bool = Addon
        if not bSuccess:
            goto('L391')
        Addon.SetDividerVisibility(False)
        # Label 391
        Variable2: int32 = 0
        Variable2_0: int32 = 0
        
        # Label 437
        ReturnValue1: int32 = len(self.mExtraInputToPassThrough)
        ReturnValue3: bool = Variable2 <= ReturnValue1
        if not ReturnValue3:
            goto('L708')
        Variable2_0 = Variable2
        ExecutionFlow.Push("L1635")
        
        Item3 = None
        Item3 = self.mExtraInputToPassThrough[Variable2_0]
        
        Item3 = None
        ReturnValue1_0: int32 = self.mInputToPassThrough.append(Item3)
        goto(ExecutionFlow.Pop())
        
        # Label 708
        ReturnValue3_0: int32 = len(self.mCentralStorages)
        ReturnValue1_1: bool = ReturnValue3_0 > 0
        ReturnValue_2: bool = self.mShowCentralStorageIfPossible and ReturnValue1_1
        if not ReturnValue_2:
            goto('L1596')
        Variable1: int32 = 0
        Variable: int32 = 0
        
        # Label 899
        ReturnValue4: int32 = len(self.mCentralStorages)
        ReturnValue1_2: bool = Variable1 <= ReturnValue4
        if not ReturnValue1_2:
           goto(ExecutionFlow.Pop())
        Variable = Variable1
        ExecutionFlow.Push("L1522")
        ReturnValue1_3: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_3: Ptr[Widget_Button] = Default__WidgetBlueprintLibrary.Create(self, Widget_Button, ReturnValue1_3)
        OutputDelegate1.BindUFunction(self, CentralStorageButtonClicked)
        ReturnValue_3.OnClickedWithRef.AddUnique(OutputDelegate1)
        ReturnValue_4: Ptr[PanelSlot] = self.mSideMenuVerticalSlot.AddChild(ReturnValue_3)
        ReturnValue_5: int32 = Variable + 1
        ReturnValue_6: FString = Default__KismetStringLibrary.Conv_IntToString(ReturnValue_5)
        ReturnValue_7: FString = Default__KismetStringLibrary.Concat_StrStr("Storage #", ReturnValue_6)
        ReturnValue_8: FText = Default__KismetTextLibrary.Conv_StringToText(ReturnValue_7)
        ReturnValue_3.mText = ReturnValue_8
        goto('L15')
        # Label 1522
        ReturnValue2: int32 = Variable1 + 1
        Variable1 = ReturnValue2
        goto('L899')
        # Label 1596
        self.mCentralStorageWindow.SetVisibility(1)
        goto(ExecutionFlow.Pop())
        # Label 1635
        ReturnValue3_1: int32 = Variable2 + 1
        Variable2 = ReturnValue3_1
        goto('L437')
        # Label 1709
        ExecutionFlow.Push("L1762")
        ReturnValue_9: bool = self.mSideMenuVerticalSlot.RemoveChildAt(0)
        goto(ExecutionFlow.Pop())
        # Label 1762
        ReturnValue_10: int32 = self.mSideMenuVerticalSlot.GetChildrenCount()
        ReturnValue2_0: bool = ReturnValue_10 > 0
        if not ReturnValue2_0:
            goto('L708')
        goto('L1709')
        # Label 1865
        Variable_0: int32 = 0
        Variable1_0: int32 = 0
        
        # Label 1911
        ReturnValue_11: int32 = len(self.mExtraInputToPassThrough)
        ReturnValue_12: bool = Variable_0 <= ReturnValue_11
        if not ReturnValue_12:
            goto('L2256')
        Variable1_0 = Variable_0
        ExecutionFlow.Push("L2182")
        
        Item1 = None
        Item1 = self.mExtraInputToPassThrough[Variable1_0]
        
        Item1 = None
        ReturnValue_13: int32 = self.mInputToPassThrough.append(Item1)
        goto(ExecutionFlow.Pop())
        # Label 2182
        ReturnValue1_4: int32 = Variable_0 + 1
        Variable_0 = ReturnValue1_4
        goto('L1911')
        # Label 2256
        if not self.mShowCentralStorageIfPossible:
            goto('L2392')
        self.TryGetCentralStorages()
        
        ReturnValue2_1: int32 = len(self.mCentralStorages)
        ReturnValue_14: bool = ReturnValue2_1 > 0
        if not ReturnValue_14:
            goto('L2392')
        goto(ExecutionFlow.Pop())
        # Label 2392
        self.mCentralStorageWindow.SetVisibility(1)
        ReturnValue_15: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_16: Vector2D = Default__WidgetLayoutLibrary.GetViewportSize(self)
        
        X = None
        Y = None
        BreakVector2D(ReturnValue_16, Ref[X], Ref[Y])
        ReturnValue_17: float = Y / 2
        ReturnValue1_5: float = X / 2
        ReturnValue_18: int32 = FTrunc(ReturnValue_17)
        ReturnValue1_6: int32 = FTrunc(ReturnValue1_5)
        ReturnValue_15.SetMouseLocation(ReturnValue1_6, ReturnValue_18)
        goto(ExecutionFlow.Pop())
        self.Init()
        self.PlayerEquipment.mHandsSlot.Init(self.mEquipmentArmsInventoryComponent)
        self.PlayerEquipment.mBackSlot.Init(self.mEquipmentBackInventoryComponent)
        if not self.mShowCentralStorageIfPossible:
            goto('L3067')
        ReturnValue_19: Ptr[GameStateBase] = Default__GameplayStatics.GetGameState(self)
        ReturnValue_20: Ptr[FGCentralStorageSubsystem] = Default__FGCentralStorageSubsystem.Get(ReturnValue_19)
        OutputDelegate2.BindUFunction(self, OnCentralStorageAddedOrRemoved)
        ReturnValue_20.CentralStorageAddedOrRemoved.AddUnique(OutputDelegate2)
        # Label 3067
        OutputDelegate.BindUFunction(self, OnEscapePressed)
        self.mInventory.OnClose.AddUnique(OutputDelegate)
        OutputDelegate3.BindUFunction(self, OnEscapePressed)
        self.mEquipmentWindowContainer.OnClose.AddUnique(OutputDelegate3)
        Array: Const[List[TSubclassOf[FGItemDescriptor]]] = [BP_HealthGainDescriptor, FGEquipmentDescriptor]
        
        self.mInventory.SetupRelevantInventory(Ref[Array])
        goto('L206')
        self.OnEscapePressed()
        goto(ExecutionFlow.Pop())
        self.Destruct()
        self.Cleanup()
        goto(ExecutionFlow.Pop())
        self.Construct()
        goto('L1865')
        
        ReturnValue5: int32 = len(self.mCentralStorages)
        ReturnValue_21: int32 = self.mSideMenuVerticalSlot.GetChildIndex(ClickedButton)
        ReturnValue2_2: bool = ReturnValue_21 <= ReturnValue5
        if not ReturnValue2_2:
           goto(ExecutionFlow.Pop())
        ReturnValue_21 = self.mSideMenuVerticalSlot.GetChildIndex(ClickedButton)
        
        Item2 = None
        Item2 = self.mCentralStorages[ReturnValue_21]
        ReturnValue_22: bool = Default__KismetSystemLibrary.IsValid(Item2)
        if not ReturnValue_22:
           goto(ExecutionFlow.Pop())
        ReturnValue_21 = self.mSideMenuVerticalSlot.GetChildIndex(ClickedButton)
        
        Item2 = None
        Item2 = self.mCentralStorages[ReturnValue_21]
        ReturnValue1_7: Ptr[FGInventoryComponent] = Item2.GetStorageInventory()
        self.mCentralStorageInventory.Init(ReturnValue1_7)
        goto(ExecutionFlow.Pop())
        self.TryGetCentralStorages()
        goto('L1762')
        # Label 3899
        self.mInventoryComponent.SortInventory()
        goto(ExecutionFlow.Pop())
        goto('L3899')
        ReturnValue2_3: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_23: Ptr[HUD] = ReturnValue2_3.GetHUD()
        AsFGHUD: Ptr[FGHUD] = Cast[FGHUD](ReturnValue_23)
        bSuccess1: bool = AsFGHUD
        ReturnValue_24: Ptr[FGGameUI] = AsFGHUD.GetGameUI()
        ReturnValue_24.SetWindowWantsInventoryAddon(True)
        ReturnValue2_3 = self.GetOwningPlayer()
        ReturnValue_23 = ReturnValue2_3.GetHUD()
        AsFGHUD = Cast[FGHUD](ReturnValue_23)
        bSuccess1 = AsFGHUD
        ReturnValue_24 = AsFGHUD.GetGameUI()
        ReturnValue_24.SetShowInventory(True)
        goto(ExecutionFlow.Pop())
        InventorySlot.QuickMoveInventory(False)
        self.mInventory.bIsFocusable = True
        ReturnValue3_2: Ptr[PlayerController] = self.GetOwningPlayer()
        self.mInventory.SetUserFocus(ReturnValue3_2)
        goto(ExecutionFlow.Pop())
    
