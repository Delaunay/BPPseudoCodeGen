
from codegen.ue4_stub import *

from Script.FactoryGame import FGEquipmentDescriptor
from Script.Engine import K2_IsTimerActiveHandle
from Game.FactoryGame.Interface.UI.InGame.InventorySlots.Widget_InventorySlot import ExecuteUbergraph_Widget_InventorySlot.K2Node_Event_InDeltaTime
from Script.Engine import Texture
from Script.Engine import Texture2D
from Script.FactoryGame import Default__FGEquipmentDescriptor
from Script.FactoryGame import CanSplitStackAtIdx
from Game.FactoryGame.Interface.UI.InGame.InventorySlots.Widget_InventorySlot import ExecuteUbergraph_Widget_InventorySlot.K2Node_Event_InFocusEvent
from Script.FactoryGame import FGCharacterPlayer
from Game.FactoryGame.Interface.UI.InGame.InventorySlots.Widget_InventorySlot import ExecuteUbergraph_Widget_InventorySlot.K2Node_Event_MouseEvent1
from Script.FactoryGame import EResourceForm
from Script.InputCore import Key
from Script.SlateCore import Margin
from Script.Engine import InputEvent_IsShiftDown
from Game.FactoryGame.Character.Player.Widget_PlayerInventory import Widget_PlayerInventory
from Script.FactoryGame import GetAllowedItemOnIndex
from Script.Engine import FTrunc
from Script.Engine import Default__KismetSystemLibrary
from Script.UMG import Handled
from Script.Engine import Divide_Vector2DFloat
from Script.UMG import ESlateVisibility
from Script.UMG import GetLocalSize
from Script.Engine import TimerHandle
from Script.UMG import StopAnimation
from Script.Engine import IsValid
from Script.FactoryGame import GetBoolOptionValue
from Script.UMG import SetColorAndOpacity
from Script.UMG import SetHeightOverride
from Script.Engine import Default__KismetTextLibrary
from Script.FactoryGame import GetSmallIcon
from Script.FactoryGame import GetActiveIndex
from Script.UMG import PanelWidget
from Script.UMG import SetWidthOverride
from Script.UMG import UserWidget
from Script.FactoryGame import Default__FGEquipment
from Game.FactoryGame.Interface.UI.InGame.InventorySlots.Widget_InventorySlot import ExecuteUbergraph_Widget_InventorySlot.K2Node_Event_PointerEvent1
from Script.FactoryGame import GetStackFromIndex
from Script.UMG import Create
from Script.SlateCore import SlateBrush
from Game.FactoryGame.Resource.Parts.ResourceSinkCoupon.Desc_ResourceSinkCoupon import Desc_ResourceSinkCoupon
from Script.SlateCore import SlateColor
from Script.FactoryGame import AddPopupWithCloseDelegate
from Game.FactoryGame.Resource.Parts.NuclearWaste.Desc_NuclearWaste import Desc_NuclearWaste
from Script.FactoryGame import GetEquipmentSlot
from Script.UMG import GetDynamicMaterial
from Script.Engine import K2_ClearAndInvalidateTimerHandle
from Script.CoreUObject import LinearColor
from Script.Engine import EqualEqual_ClassClass
from Script.FactoryGame import FGPlayerController
from Script.FactoryGame import GetFGGameUserSettings
from Script.Engine import SetObjectPropertyByName
from Script.Engine import Pawn
from Script.Engine import Multiply_Vector2DVector2D
from Script.Engine import MaterialInstanceDynamic
from Script.Engine import Max
from Script.Engine import HUD
from Script.Engine import SetStructurePropertyByName
from Game.FactoryGame.Interface.UI.InGame.InventorySlots.Widget_InventorySlot import ExecuteUbergraph_Widget_InventorySlot.K2Node_Event_PointerEvent
from Script.Engine import Default__KismetArrayLibrary
from Script.FactoryGame import GetAmountConvertedByForm
from Script.FactoryGame import GetInventory
from Script.Engine import SetVectorParameterValue
from Script.FactoryGame import FGEquipment
from Script.CoreUObject import Object
from Script.FactoryGame import FGInventoryComponent
from Game.FactoryGame.Interface.UI.InGame.InventorySlots.Widget_InventorySlot import Widget_InventorySlot
from Script.Engine import GetHUD
from Game.FactoryGame.Interface.UI.Audio.Play_UI_Inventory_MouseOver import Play_UI_Inventory_MouseOver
from Script.FactoryGame import FGGameUserSettings
from Game.FactoryGame.Interface.UI.InGame.InventorySlots.Widget_InventorySlot import ExecuteUbergraph_Widget_InventorySlot.K2Node_Event_IsDesignTime
from Script.FactoryGame import IsValidIndex
from Script.Engine import SetMouseLocation
from Script.UMG import SetFont
from Script.AkAudio import Default__AkGameplayStatics
from Script.Engine import NotEqual_ByteByte
from Script.Engine import EqualEqual_KeyKey
from Script.UMG import Close
from Game.FactoryGame.Interface.UI.HUDHelpers.BPHUDHelpers import Default__BPHUDHelpers
from Script.FactoryGame import Default__FGItemDescriptor
from Game.FactoryGame.Interface.UI.InGame.InventorySlots.Widget_InventorySlot import ExecuteUbergraph_Widget_InventorySlot.K2Node_Event_MyGeometry1
from Script.UMG import GetViewportScale
from Game.FactoryGame.Interface.UI.InGame.InventorySlots.Widget_InventorySlot import ExecuteUbergraph_Widget_InventorySlot.K2Node_Event_Operation1
from Script.FactoryGame import GetTrashSlot
from Script.SlateCore import ESlateBrushDrawType
from Script.FactoryGame import BreakInventoryItem
from Script.AkAudio import AkComponent
from Script.FactoryGame import EEquipmentSlot
from Script.UMG import EventReply
from Script.FactoryGame import GetOuterActor
from Game.FactoryGame.Interface.UI.InGame.InventorySlots.Widget_InventorySlot import ExecuteUbergraph_Widget_InventorySlot.K2Node_Event_Operation
from Script.Engine import MakeLiteralByte
from Script.UMG import SetUserFocus
from Script.FactoryGame import GetStackSize
from Script.UMG import GetAllChildren
from Script.UMG import GetParent
from Game.FactoryGame.Interface.UI.InGame.InventorySlots.Widget_InventorySlot import ExecuteUbergraph_Widget_InventorySlot.K2Node_CustomEvent_ConfirmClicked
from Script.AkAudio import PostAkEvent
from Script.Engine import K2_SetTimerDelegate
from Script.FactoryGame import BreakInventoryStack
from Script.UMG import Default__WidgetLayoutLibrary
from Script.FactoryGame import Default__FGInventoryLibrary
from Script.Engine import TextIsEmpty
from Script.Engine import SetBytePropertyByName
from Script.Engine import SetTextureParameterValue
from Script.Engine import PlayerController
from Script.UMG import PlayAnimation
from Script.UMG import Unhandled
from Script.Engine import PointerEvent_IsMouseButtonDown
from Script.Engine import Conv_FloatToText
from Game.FactoryGame.EDragNDropHoverState import EDragNDropHoverState
from Script.FactoryGame import GetForm
from Script.UMG import Default__WidgetBlueprintLibrary
from Script.UMG import GetInputEventFromPointerEvent
from Game.FactoryGame.Interface.UI.InGame.InventorySlots.Widget_InventorySlot import ExecuteUbergraph_Widget_InventorySlot.K2Node_CustomEvent_isNuclearWaste
from Script.Engine import BreakVector2D
from Script.FactoryGame import IsItemAllowed
from Script.SlateCore import InputEvent
from Script.FactoryGame import GetGameUI
from Script.CoreUObject import Box2D
from Script.Engine import EqualEqual_ObjectObject
from Game.FactoryGame.Interface.UI.InGame.Widget_InventoryDragNDropRep import Widget_InventoryDragNDropRep
from Script.Engine import InputEvent_IsLeftControlDown
from Script.FactoryGame import FGGameUI
from Script.FactoryGame import Default__FGBlueprintFunctionLibrary
from Script.FactoryGame import GetRemoteCallObjectOfClass
from Script.FactoryGame import IsSomethingOnIndex
from Game.FactoryGame.Interface.UI.Assets.Shared.WindowWidget.Rectangle_Background_Square import Rectangle_Background_Square
from Script.UMG import GetInputEventFromKeyEvent
from Script.FactoryGame import FGItemDescriptor
from Script.CoreUObject import Vector2D
from Game.FactoryGame.Interface.UI.InGame.InventorySlots.Widget_InventorySlot import ExecuteUbergraph_Widget_InventorySlot.K2Node_Event_MyGeometry2
from Script.UMG import LocalToViewport
from Script.Engine import InputEvent_IsControlDown
from Game.FactoryGame.Character.Player.BP_RemoteCallObject import BP_RemoteCallObject
from Script.Engine import Default__KismetInputLibrary
from Script.Engine import SetScalarParameterValue
from Game.FactoryGame.Interface.UI.InGame.InventorySlots.EInventorySlot_State_Content import EInventorySlot_State_Content
from Script.Engine import Not_PreBool
from Script.UMG import DetectDragIfPressed
from Script.FactoryGame import GetAbbreviatedDisplayName
from Script.FactoryGame import GetBigIcon
from Script.UMG import Open
from Game.FactoryGame.Interface.UI.InGame.Widget_Tooltip import Widget_Tooltip
from Game.FactoryGame.Interface.UI.InGame.InventorySlots.EInventorySlot_State_Interact import EInventorySlot_State_Interact
from Script.FactoryGame import FGInventoryComponentEquipment
from Script.UMG import CreateDragDropOperation
from Game.FactoryGame.Interface.UI.InGame.InventorySlots.Widget_InventorySlot import ExecuteUbergraph_Widget_InventorySlot.K2Node_Event_MouseEvent
from Script.Engine import Divide_IntInt
from Script.FactoryGame import Default__FGGameUserSettings
from Script.FactoryGame import GetIsUsingGamepad
from Script.UMG import Default__SlateBlueprintLibrary
from Script.Engine import BooleanOR
from Game.FactoryGame.Interface.UI.InGame.InventorySlots.Widget_InventorySlot import ExecuteUbergraph_Widget_InventorySlot
from Script.UMG import Widget
from Game.FactoryGame.Interface.UI.InGame.InventorySlots.Widget_InventorySlot import ExecuteUbergraph_Widget_InventorySlot.K2Node_Event_MyGeometry
from Script.FactoryGame import GetEquipmentClass
from Game.FactoryGame.Buildable.Factory.BP_DragNDropInventory import BP_DragNDropInventory
from Script.UMG import WidgetAnimation
from Script.FactoryGame import FGHUD
from Script.UMG import GetAllWidgetsOfClass
from Script.Engine import PointerEvent_GetEffectingButton
from Game.FactoryGame.Interface.UI.Assets.Shared.Circle_Background import Circle_Background
from Script.UMG import GetOwningPlayerPawn
from Script.Engine import Actor
from Script.UMG import UMGSequencePlayer
from Script.FactoryGame import ClosePopup
from Game.FactoryGame.Interface.UI.InGame.Widget_StackSplitSlider import Widget_StackSplitSlider
from Script.Engine import IsValidClass
from Script.Engine import Character

class Widget_InventorySlot(UserWidget):
    EmptySlot: Ptr[WidgetAnimation]
    OnHover: Ptr[WidgetAnimation]
    mSlotIdx: int32
    mNumItems: int32
    mCachedInventoryComponent: Ptr[FGInventoryComponent]
    mItemClass: TSubclassOf[FGItemDescriptor]
    mTooltipWidget: Ptr[Object]
    mFilterItemDescriptor: TSubclassOf[FGItemDescriptor]
    OnSlotHovered: FMulticastScriptDelegate
    mShouldGrabAllOfType: bool
    mCostSlotBrush: Ptr[Texture]
    OnMoveStack: FMulticastScriptDelegate
    mUpdateTimer: TimerHandle
    mSlotBgMaterial: Ptr[MaterialInstanceDynamic]
    mSplitStackTimerHandle: TimerHandle
    mSplitStackHoldTime: float = 0.20000000298023224
    mInventorySlotToRepresent: Ptr[Widget_InventorySlot]
    mContentState: uint8
    mDragAndDropState: uint8
    mInteractState: uint8
    mResourceForm: uint8
    mPreviousItemClass: TSubclassOf[FGItemDescriptor]
    mIsCostSlot: bool
    mBigSlot: bool
    mSmallSlot: bool
    mIsLocked: bool
    mAbbreviateName: bool
    ForegroundColor = Namespace(ColorUseRule=2, SpecifiedColor={'R': 1, 'G': 1, 'B': 1, 'A': 1})
    bIsFocusable = True
    
    def GetItemOrFilterClass(self):
        ReturnValue: bool = Default__KismetSystemLibrary.IsValidClass(self.mItemClass)
        if not ReturnValue:
            goto('L89')
        ReturnValue_0: TSubclassOf[FGItemDescriptor] = self.mItemClass
        goto('L132')
        # Label 89
        ReturnValue_1: TSubclassOf[FGItemDescriptor] = self.GetFilterClass()
        ReturnValue_0 = ReturnValue_1
    

    def GetFilterClass(self):
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(self.mCachedInventoryComponent)
        if not ReturnValue:
            goto('L256')
        ReturnValue_0: TSubclassOf[FGItemDescriptor] = self.mCachedInventoryComponent.GetAllowedItemOnIndex(self.mSlotIdx)
        ReturnValue1: bool = Default__KismetSystemLibrary.IsValidClass(ReturnValue_0)
        if not ReturnValue1:
            goto('L256')
        ReturnValue_0 = self.mCachedInventoryComponent.GetAllowedItemOnIndex(self.mSlotIdx)
        ReturnValue_1: TSubclassOf[FGItemDescriptor] = ReturnValue_0
        goto('L356')
        # Label 256
        ReturnValue_2: bool = Default__KismetSystemLibrary.IsValidClass(self.mFilterItemDescriptor)
        if not ReturnValue_2:
            goto('L345')
        ReturnValue_1 = self.mFilterItemDescriptor
        goto('L356')
        # Label 345
        ReturnValue_1 = None
    

    def OnItemClassUpdated(self):
        self.mPreviousItemClass = self.mItemClass
        
        ContentState = None
        self.GetContentState(Ref[ContentState])
        self.SetContentState(ContentState)
        
        Form = None
        self.GetItemForm(Ref[Form])
        self.SetResourceForm(Form)
        ReturnValue: SlateBrush = self.GetItemImageBrush()
        
        self.mItemImage.SetBrush(Ref[ReturnValue])
        ReturnValue_0: TSubclassOf[FGItemDescriptor] = self.GetItemOrFilterClass()
        LocalItemOrFilter = ReturnValue_0
        ReturnValue_1: bool = Default__KismetSystemLibrary.IsValidClass(LocalItemOrFilter)
        if not ReturnValue_1:
            goto('L730')
        ReturnValue_2: FText = Default__FGItemDescriptor.GetAbbreviatedDisplayName(LocalItemOrFilter)
        
        ReturnValue_3: bool = Default__KismetTextLibrary.TextIsEmpty(Ref[ReturnValue_2])
        ReturnValue_4: bool = Not_PreBool(ReturnValue_3)
        Variable: uint8 = 3
        Variable1: uint8 = 2
        ReturnValue_5: bool = ReturnValue_4 and self.mAbbreviateName
        Variable_0: bool = ReturnValue_5
        
        switch = {
            False: Variable1,
            True: Variable
        }
        self.mAbbreviationOverlay.SetVisibility(switch.get(Variable_0, None))
        ReturnValue1: FText = Default__FGItemDescriptor.GetAbbreviatedDisplayName(LocalItemOrFilter)
        self.mAbbreviation.SetText(ReturnValue1)
        # End
        # Label 730
        self.mAbbreviationOverlay.SetVisibility(2)
    

    def GetIsItemStackable(self):
        ReturnValue: bool = Default__KismetSystemLibrary.IsValidClass(self.mItemClass)
        if not ReturnValue:
            goto('L182')
        ReturnValue_0: int32 = Default__FGItemDescriptor.GetStackSize(self.mItemClass)
        ReturnValue_1: bool = ReturnValue_0 > 1
        IsStackable = ReturnValue_1
        # End
        # Label 182
        IsStackable = False
    

    def SetResourceForm(self, NewResourceForm: uint8):
        ReturnValue: bool = NotEqual_ByteByte(NewResourceForm, self.mResourceForm)
        if not ReturnValue:
            goto('L2267')
        self.mResourceForm = NewResourceForm
        Variable: LinearColor = LinearColor(R = 0.7835379838943481, G = 0.2917709946632385, B = 0.057805001735687256, A = 1)
        Variable1: LinearColor = LinearColor(R = 0.7835379838943481, G = 0.2917709946632385, B = 0.057805001735687256, A = 1)
        Variable2: LinearColor = LinearColor(R = 0.10588199645280838, G = 0.3803919851779938, B = 0.556863009929657, A = 1)
        Variable3: LinearColor = LinearColor(R = 0.7835379838943481, G = 0.2917709946632385, B = 0.057805001735687256, A = 1)
        Variable4: LinearColor = LinearColor(R = 0.7835379838943481, G = 0.2917709946632385, B = 0.057805001735687256, A = 1)
        Variable5: uint8 = self.mResourceForm
        
        switch = {
            0: Variable4,
            1: Variable3,
            2: Variable2,
            3: Variable1,
            4: Variable
        }
        LocalFormColor = switch.get(Variable5, None)
        self.mCross.SetColorAndOpacity(LocalFormColor)
        self.mTextBackground.SetColorAndOpacity(LocalFormColor)
        FontOutlineSettings.OutlineSize = self.mStackSizeLbl.Font.OutlineSettings.OutlineSize
        FontOutlineSettings.bSeparateFillAlpha = self.mStackSizeLbl.Font.OutlineSettings.bSeparateFillAlpha
        FontOutlineSettings.bApplyOutlineToDropShadows = self.mStackSizeLbl.Font.OutlineSettings.bApplyOutlineToDropShadows
        FontOutlineSettings.OutlineMaterial = self.mStackSizeLbl.Font.OutlineSettings.OutlineMaterial
        FontOutlineSettings.OutlineColor = LocalFormColor
        SlateFontInfo.FontObject = self.mStackSizeLbl.Font.FontObject
        SlateFontInfo.FontMaterial = self.mStackSizeLbl.Font.FontMaterial
        SlateFontInfo.OutlineSettings = FontOutlineSettings
        SlateFontInfo.TypefaceFontName = self.mStackSizeLbl.Font.TypefaceFontName
        SlateFontInfo.Size = self.mStackSizeLbl.Font.Size
        self.mStackSizeLbl.SetFont(SlateFontInfo)
        Variable_0: uint8 = 1
        Variable1_0: uint8 = 3
        Variable2_0: uint8 = 1
        Variable3_0: uint8 = 1
        Variable6: uint8 = 1
        Variable7: uint8 = self.mResourceForm
        SlateBrush.ImageSize = self.mSlotBg.Brush.ImageSize
        SlateBrush.Margin = self.mSlotBg.Brush.Margin
        SlateBrush.TintColor = self.mSlotBg.Brush.TintColor
        SlateBrush.ResourceObject = self.mSlotBg.Brush.ResourceObject
        
        switch_0 = {
            0: Variable3_0,
            1: Variable2_0,
            2: Variable1_0,
            3: Variable_0,
            4: Variable6
        }
        SlateBrush.DrawAs = switch_0.get(Variable7, None)
        SlateBrush.Tiling = self.mSlotBg.Brush.Tiling
        SlateBrush.Mirroring = self.mSlotBg.Brush.Mirroring
        
        SlateBrush = None
        self.mSlotBg.SetBrush(Ref[SlateBrush])
        ReturnValue_0: Ptr[MaterialInstanceDynamic] = self.mSlotBg.GetDynamicMaterial()
        ReturnValue_0.SetVectorParameterValue("AccentColor", LocalFormColor)
        Variable_1: Ptr[Texture] = Rectangle_Background_Square
        Variable1_1: Ptr[Texture] = Rectangle_Background_Square
        Variable2_1: Ptr[Texture] = Circle_Background
        Variable3_1: Ptr[Texture] = Rectangle_Background_Square
        Variable4_0: Ptr[Texture] = Rectangle_Background_Square
        Variable4_1: uint8 = self.mResourceForm
        
        switch_1 = {
            0: Variable4_0,
            1: Variable3_1,
            2: Variable2_1,
            3: Variable1_1,
            4: Variable_1
        }
        ReturnValue_0.SetTextureParameterValue("SlotTexture", switch_1.get(Variable4_1, None))
    

    def GetContentState(self):
        
        slotHasItems = None
        self.CheckSlotHasItems(Ref[slotHasItems])
        if not slotHasItems:
            goto('L141')
        Descriptor: TSubclassOf[FGEquipmentDescriptor] = ClassCast[FGEquipmentDescriptor](self.mItemClass)
        bSuccess1: bool = Descriptor
        if not bSuccess1:
            goto('L280')
        ContentState = 4
        # End
        # Label 141
        ReturnValue: TSubclassOf[FGItemDescriptor] = self.GetFilterClass()
        ReturnValue_0: bool = Default__KismetSystemLibrary.IsValidClass(ReturnValue)
        if not ReturnValue_0:
            goto('L255')
        ContentState = 2
        # End
        # Label 255
        ContentState = 1
        # End
        # Label 280
        Coupon: TSubclassOf[Desc_ResourceSinkCoupon] = ClassCast[Desc_ResourceSinkCoupon](self.mItemClass)
        bSuccess: bool = Coupon
        # Label 345
        if not bSuccess:
            goto('L384')
        ContentState = 5
        # End
        # Label 384
        ContentState = 3
    

    def SetInteractState(self, NewInteractState: uint8):
        ReturnValue: bool = NotEqual_ByteByte(NewInteractState, self.mInteractState)
        if not ReturnValue:
            goto('L294')
        self.mInteractState = NewInteractState
        CmpSuccess: bool = NotEqual_ByteByte(self.mInteractState, 1)
        if not CmpSuccess:
            goto('L174')
        CmpSuccess = NotEqual_ByteByte(self.mInteractState, 2)
        if not CmpSuccess:
            goto('L248')
        # Label 169
        # End
        # Label 174
        self.StopAnimation(self.OnHover)
        self.mSlotBgMaterial.SetScalarParameterValue("Alpha1", 0)
        # End
        # Label 248
        ReturnValue_0: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.OnHover, 0, 1, 0, 1)
    

    def SetDragAndDropState(self, NewDragAndDropState: uint8):
        ReturnValue: bool = NotEqual_ByteByte(NewDragAndDropState, self.mDragAndDropState)
        if not ReturnValue:
            goto('L556')
        self.mDragAndDropState = NewDragAndDropState
        Variable: bool = False
        Variable1: bool = True
        Variable2: bool = False
        Variable_0: float = 1
        # Label 135
        Variable1_0: float = 0
        Variable4: uint8 = self.mDragAndDropState
        
        switch = {
            0: Variable2,
            1: Variable1,
            2: Variable
        }
        Variable3: bool = switch.get(Variable4, None)
        
        switch_0 = {
            False: Variable1_0,
            True: Variable_0
        }
        self.mSlotBgMaterial.SetScalarParameterValue("Alpha2", switch_0.get(Variable3, None))
        Variable1_1: uint8 = 3
        Variable2_0: uint8 = 2
        Variable3_0: uint8 = 2
        Variable_1: uint8 = self.mDragAndDropState
        
        switch_1 = {
            0: Variable3_0,
            1: Variable2_0,
            2: Variable1_1
        }
        self.mCross.SetVisibility(switch_1.get(Variable_1, None))
    

    def SetContentState(self, NewContentState: uint8):
        ReturnValue: bool = NotEqual_ByteByte(NewContentState, self.mContentState)
        if not ReturnValue:
            goto('L2384')
        self.mContentState = NewContentState
        ReturnValue_0: Ptr[MaterialInstanceDynamic] = self.mSlotBg.GetDynamicMaterial()
        Variable6: LinearColor = LinearColor(R = 0.04970699921250343, G = 0.04970699921250343, B = 0.04970699921250343, A = 1)
        Variable7: LinearColor = LinearColor(R = 1, G = 1, B = 1, A = 1)
        Variable8: LinearColor = LinearColor(R = 0.6038280129432678, G = 0.5972020030021667, B = 0.5972020030021667, A = 1)
        # Label 277
        Variable9: LinearColor = LinearColor(R = 0.13286800682544708, G = 0.13286800682544708, B = 0.13563300669193268, A = 0.2980389893054962)
        Variable10: LinearColor = LinearColor(R = 0.13286800682544708, G = 0.13286800682544708, B = 0.13563300669193268, A = 0.2980389893054962)
        Variable11: LinearColor = LinearColor(R = 0, G = 0, B = 0, A = 0)
        Variable24: uint8 = self.mContentState
        
        switch = {
            0: Variable11,
            1: Variable10,
            2: Variable9,
            3: Variable8,
            4: Variable7,
            5: Variable6
        }
        # Label 460
        ReturnValue_0.SetVectorParameterValue("SlotColor", switch.get(Variable24, None))
        Variable: LinearColor = LinearColor(R = 0, G = 0, B = 0, A = 0)
        # Label 672
        Variable1: LinearColor = LinearColor(R = 0.7835379838943481, G = 0.2917709946632385, B = 0.057805001735687256, A = 1)
        Variable2: LinearColor = LinearColor(R = 0, G = 0, B = 0, A = 0)
        Variable3: LinearColor = LinearColor(R = 0, G = 0, B = 0, A = 0)
        Variable4: LinearColor = LinearColor(R = 0, G = 0, B = 0, A = 0)
        Variable5: LinearColor = LinearColor(R = 0, G = 0, B = 0, A = 0)
        Variable23: uint8 = self.mContentState
        
        switch_0 = {
            0: Variable5,
            1: Variable4,
            2: Variable3,
            3: Variable2,
            4: Variable1,
            5: Variable
        }
        self.mSlotBorder.SetColorAndOpacity(switch_0.get(Variable23, None))
        Variable17: uint8 = 2
        Variable18: uint8 = 3
        Variable19: uint8 = 2
        Variable20: uint8 = 2
        Variable21: uint8 = 2
        Variable22: uint8 = 2
        Variable16: uint8 = self.mContentState
        
        switch_1 = {
            0: Variable22,
            1: Variable21,
            2: Variable20,
            3: Variable19,
            4: Variable18,
            5: Variable17
        }
        self.mSlotBorder.SetVisibility(switch_1.get(Variable16, None))
        Variable_0: uint8 = 3
        Variable10_0: uint8 = 3
        Variable11_0: uint8 = 3
        Variable12: uint8 = 3
        Variable13: uint8 = 3
        Variable14: uint8 = 2
        Variable15: uint8 = 2
        Variable_1: bool = self.mIsCostSlot
        Variable9_0: uint8 = self.mContentState
        
        switch_2 = {
            0: Variable15,
            1: Variable14,
            2: Variable13,
            3: Variable12,
            4: Variable11_0,
            5: Variable10_0
        }
        
        switch_3 = {
            False: switch_2.get(Variable9_0, None),
            True: Variable_0
        }
        self.mItemImage.SetVisibility(switch_3.get(Variable_1, None))
        Variable1_0: uint8 = 2
        Variable3_0: uint8 = 3
        Variable4_0: uint8 = 3
        Variable5_0: uint8 = 3
        # Label 1865
        Variable6_0: uint8 = 2
        Variable7_0: uint8 = 2
        Variable8_0: uint8 = 2
        
        IsStackable = None
        self.GetIsItemStackable(Ref[IsStackable])
        Variable1_1: bool = IsStackable
        Variable2_0: uint8 = self.mContentState
        
        switch_4 = {
            0: Variable8_0,
            1: Variable7_0,
            2: Variable6_0,
            3: Variable5_0,
            4: Variable4_0,
            5: Variable3_0
        }
        
        switch_5 = {
            False: Variable1_0,
            True: switch_4.get(Variable2_0, None)
        }
        self.mStackSizeOverlay.SetVisibility(switch_5.get(Variable1_1, None))
        
        switch_6 = {
            0: Variable8_0,
            1: Variable7_0,
            2: Variable6_0,
            3: Variable5_0,
            4: Variable4_0,
            5: Variable3_0
        }
        
        switch_7 = {
            False: Variable1_0,
            True: switch_6.get(Variable2_0, None)
        }
        self.mStackSizeLbl.SetVisibility(switch_7.get(Variable1_1, None))
    

    def MoveAllWithSameItemClass(self):
        ExecutionFlow.Push("L746")
        self.mShouldGrabAllOfType = True
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(self.mInventorySlotToRepresent)
        if not ReturnValue:
            goto('L118')
        self.mInventorySlotToRepresent.MoveAllWithSameItemClass()
        goto(ExecutionFlow.Pop())
        # Label 118
        ReturnValue_0: Ptr[PanelWidget] = self.GetParent()
        ReturnValue_1: List[Ptr[Widget]] = ReturnValue_0.GetAllChildren()
        localChildWidgets = ReturnValue_1
        Variable: int32 = 0
        Variable_0: int32 = 0
        
        # Label 261
        ReturnValue_2: int32 = len(localChildWidgets)
        ReturnValue_3: bool = Variable <= ReturnValue_2
        if not ReturnValue_3:
            goto('L660')
        Variable_0 = Variable
        ExecutionFlow.Push("L672")
        
        Item = None
        Item = localChildWidgets[Variable_0]
        Slot: Ptr[Widget_InventorySlot] = Cast[Widget_InventorySlot](Item)
        bSuccess: bool = Slot
        if not bSuccess:
           goto(ExecutionFlow.Pop())
        
        ItemClass = None
        Slot.GetItemClass(Ref[ItemClass])
        ReturnValue_4: bool = EqualEqual_ClassClass(ItemClass, self.mItemClass)
        if not ReturnValue_4:
           goto(ExecutionFlow.Pop())
        self.OnMoveStack.ProcessMulticastDelegate(Slot)
        goto(ExecutionFlow.Pop())
        # Label 660
        self.mShouldGrabAllOfType = False
        goto(ExecutionFlow.Pop())
        # Label 672
        ReturnValue_5: int32 = Variable + 1
        Variable = ReturnValue_5
        goto('L261')
    

    def ShowSplitStackWidget(self):
        self.mSplitMenuAnchor.Open(True)
    

    def OnMouseButtonDoubleClick(self):
        
        ReturnValue: InputEvent = Default__WidgetBlueprintLibrary.GetInputEventFromPointerEvent(Ref[InMouseEvent])
        
        ReturnValue_0: Key = Default__KismetInputLibrary.PointerEvent_GetEffectingButton(Ref[InMouseEvent])
        
        # Label 118
        ReturnValue_1: bool = Default__KismetInputLibrary.InputEvent_IsControlDown(Ref[ReturnValue])
        # Label 169
        ReturnValue_2: bool = Default__KismetInputLibrary.EqualEqual_KeyKey(ReturnValue_0, Key(KeyName = "LeftMouseButton"))
        ReturnValue_3: bool = Not_PreBool(ReturnValue_1)
        
        ReturnValue_4: bool = Default__KismetInputLibrary.InputEvent_IsShiftDown(Ref[ReturnValue])
        ReturnValue1: bool = Not_PreBool(ReturnValue_4)
        # Label 356
        ReturnValue_5: bool = ReturnValue_2 and ReturnValue1
        ReturnValue1_0: bool = ReturnValue_5 and ReturnValue_3
        if not ReturnValue1_0:
            goto('L559')
        self.QuickMoveInventory(False)
        self.SetInteractState(1)
        ReturnValue_6: EventReply = Default__WidgetBlueprintLibrary.Handled()
        ReturnValue_7: EventReply = ReturnValue_6
        goto('L636')
        # Label 559
        ReturnValue_8: EventReply = Default__WidgetBlueprintLibrary.Unhandled()
        ReturnValue_7 = ReturnValue_8
    

    def GetItemForm(self):
        ReturnValue: TSubclassOf[FGItemDescriptor] = self.GetItemOrFilterClass()
        LocalItemClass = ReturnValue
        ReturnValue_0: bool = Default__KismetSystemLibrary.IsValidClass(LocalItemClass)
        if not ReturnValue_0:
            goto('L199')
        ReturnValue_1: uint8 = Default__FGItemDescriptor.GetForm(LocalItemClass)
        form = ReturnValue_1
        # End
        # Label 199
        form = 0
    

    def CheckForNuclearWaste(self, Object: TSubclassOf[Object]):
        ReturnValue: Ptr[Pawn] = self.GetOwningPlayerPawn()
        ReturnValue_0: bool = EqualEqual_ClassClass(Object, Desc_NuclearWaste)
        Player: Ptr[FGCharacterPlayer] = Cast[FGCharacterPlayer](ReturnValue)
        bSuccess: bool = Player
        ReturnValue_1: Ptr[FGInventoryComponent] = Player.GetTrashSlot()
        ReturnValue_2: bool = EqualEqual_ObjectObject(ReturnValue_1, self.mCachedInventoryComponent)
        ReturnValue_3: bool = ReturnValue_2 and ReturnValue_0
        self.Event CreateNuclearWastePopup(ReturnValue_3)
    

    def QuickMoveInventory(self, MoveAllItemsOfSameType: bool):
        Descriptor: TSubclassOf[FGEquipmentDescriptor] = ClassCast[FGEquipmentDescriptor](self.mItemClass)
        bSuccess: bool = Descriptor
        if not bSuccess:
            goto('L1207')
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        Controller: Ptr[FGPlayerController] = Cast[FGPlayerController](ReturnValue)
        bSuccess2: bool = Controller
        if not bSuccess2:
            goto('L1641')
        # Label 182
        ReturnValue_0: Ptr[HUD] = Controller.GetHUD()
        AsFGHUD: Ptr[FGHUD] = Cast[FGHUD](ReturnValue_0)
        bSuccess3: bool = AsFGHUD
        if not bSuccess3:
            goto('L1641')
        ReturnValue_1: Ptr[FGGameUI] = AsFGHUD.GetGameUI()
        
        Widget = None
        # Label 345
        Default__BPHUDHelpers.FindWidgetOfClass(Widget_PlayerInventory, ReturnValue_1, self, Ref[Widget])
        ReturnValue_2: bool = Default__KismetSystemLibrary.IsValid(Widget)
        # Label 460
        if not ReturnValue_2:
            goto('L1207')
        ReturnValue1: Ptr[Pawn] = self.GetOwningPlayerPawn()
        # Label 494
        Player1: Ptr[FGCharacterPlayer] = Cast[FGCharacterPlayer](ReturnValue1)
        bSuccess1: bool = Player1
        # Label 559
        if not bSuccess1:
            goto('L1641')
        ReturnValue_3: TSubclassOf[FGEquipment] = Default__FGEquipmentDescriptor.GetEquipmentClass(Descriptor)
        ReturnValue_4: uint8 = Default__FGEquipment.GetEquipmentSlot(ReturnValue_3)
        ReturnValue1_0: Ptr[FGInventoryComponentEquipment] = Player1.GetEquipmentSlot(ReturnValue_4)
        ReturnValue_5: bool = EqualEqual_ObjectObject(self.mCachedInventoryComponent, ReturnValue1_0)
        if not ReturnValue_5:
            goto('L1265')
        ReturnValue_6: Ptr[Pawn] = self.GetOwningPlayerPawn()
        Player: Ptr[FGCharacterPlayer] = Cast[FGCharacterPlayer](ReturnValue_6)
        bSuccess_0: bool = Player
        if not bSuccess_0:
            goto('L1641')
        ReturnValue_7: Ptr[FGInventoryComponent] = Player.GetInventory()
        ReturnValue_8: Ptr[BP_RemoteCallObject] = Controller.GetRemoteCallObjectOfClass(BP_RemoteCallObject)
        ReturnValue_3 = Default__FGEquipmentDescriptor.GetEquipmentClass(Descriptor)
        ReturnValue_4 = Default__FGEquipment.GetEquipmentSlot(ReturnValue_3)
        ReturnValue1_0 = Player1.GetEquipmentSlot(ReturnValue_4)
        ReturnValue_8.Server_MoveItemIfSpace(ReturnValue1_0, self.mSlotIdx, ReturnValue_7)
        # End
        # Label 1207
        if not MoveAllItemsOfSameType:
            goto('L1240')
        self.MoveAllWithSameItemClass()
        # End
        # Label 1240
        self.OnMoveStack.ProcessMulticastDelegate(self)
        # End
        # Label 1265
        ReturnValue_3 = Default__FGEquipmentDescriptor.GetEquipmentClass(Descriptor)
        ReturnValue1_1: Ptr[BP_RemoteCallObject] = Controller.GetRemoteCallObjectOfClass(BP_RemoteCallObject)
        ReturnValue_4 = Default__FGEquipment.GetEquipmentSlot(ReturnValue_3)
        ReturnValue1_0 = Player1.GetEquipmentSlot(ReturnValue_4)
        ReturnValue_9: int32 = ReturnValue1_0.GetActiveIndex()
        ReturnValue_10: int32 = Max(ReturnValue_9, 0)
        ReturnValue1_1.Server_MoveItem(self.mCachedInventoryComponent, ReturnValue1_0, self.mSlotIdx, ReturnValue_10)
    

    def SetSlotSize(self, SmallSlot: bool, BigSlot: bool):
        if not SmallSlot:
            goto('L93')
        self.mSlotSizeBox.SetHeightOverride(42)
        self.mSlotSizeBox.SetWidthOverride(42)
        # End
        # Label 93
        if not BigSlot:
            goto('L186')
        self.mSlotSizeBox.SetHeightOverride(128)
        self.mSlotSizeBox.SetWidthOverride(128)
        # End
        # Label 186
        self.mSlotSizeBox.SetHeightOverride(64)
        self.mSlotSizeBox.SetWidthOverride(64)
    

    def DropOntoInventorySlot(self, OtherInventorySlot: Ptr[Widget_InventorySlot]):
        ExecutionFlow.Push("L1109")
        self.CloseSplitStack()
        OtherInventorySlot.CloseSplitStack()
        self.CheckForNuclearWaste(OtherInventorySlot.mItemClass)
        # Label 114
        ReturnValue: bool = self.mCachedInventoryComponent.IsItemAllowed(OtherInventorySlot.mItemClass, self.mSlotIdx)
        ReturnValue_0: bool = Not_PreBool(self.mIsLocked)
        ReturnValue_1: bool = ReturnValue and ReturnValue_0
        if not ReturnValue_1:
            goto('L913')
        # Label 277
        ReturnValue_2: Ptr[PlayerController] = self.GetOwningPlayer()
        Controller: Ptr[FGPlayerController] = Cast[FGPlayerController](ReturnValue_2)
        bSuccess: bool = Controller
        if not bSuccess:
            goto('L913')
        ExecutionFlow.Push("L913")
        # Label 385
        ReturnValue_3: bool = OtherInventorySlot.mCachedInventoryComponent.IsValidIndex(OtherInventorySlot.mSlotIdx)
        ReturnValue1: bool = self.mCachedInventoryComponent.IsValidIndex(self.mSlotIdx)
        ReturnValue1_0: bool = ReturnValue_3 and ReturnValue1
        # Label 569
        if not ReturnValue1_0:
           goto(ExecutionFlow.Pop())
        ReturnValue_4: bool = OtherInventorySlot.mCachedInventoryComponent.IsSomethingOnIndex(OtherInventorySlot.mSlotIdx)
        if not ReturnValue_4:
           goto(ExecutionFlow.Pop())
        if not OtherInventorySlot.mShouldGrabAllOfType:
            goto('L937')
        
        ItemClass = None
        OtherInventorySlot.GetItemClass(Ref[ItemClass])
        ReturnValue_5: Ptr[BP_RemoteCallObject] = Controller.GetRemoteCallObjectOfClass(BP_RemoteCallObject)
        # Label 816
        ReturnValue_5.Server_GrabAllItemsFromInventory(OtherInventorySlot.mCachedInventoryComponent, self.mCachedInventoryComponent, ItemClass)
        # Label 901
        LocalResult = True
        goto(ExecutionFlow.Pop())
        # Label 913
        Result = LocalResult
        # End
        # Label 937
        ReturnValue_5 = Controller.GetRemoteCallObjectOfClass(BP_RemoteCallObject)
        ReturnValue_5.Server_MoveItem(OtherInventorySlot.mCachedInventoryComponent, self.mCachedInventoryComponent, OtherInventorySlot.mSlotIdx, self.mSlotIdx)
        goto('L901')
    

    def OnMouseButtonUp(self):
        ExecutionFlow.Push("L1054")
        ExecutionFlow.Push("L299")
        # Label 10
        ReturnValue: bool = Default__KismetSystemLibrary.K2_IsTimerActiveHandle(self, self.mSplitStackTimerHandle)
        if not ReturnValue:
           goto(ExecutionFlow.Pop())
        
        Default__KismetSystemLibrary.K2_ClearAndInvalidateTimerHandle(self, Ref[self.mSplitStackTimerHandle])
        # Label 114
        ReturnValue_0: Ptr[PlayerController] = self.GetOwningPlayer()
        
        RCO = None
        Default__BPHUDHelpers.GetDefaultRCO(ReturnValue_0, self, Ref[RCO])
        ReturnValue_1: int32 = Divide_IntInt(self.mNumItems, 2)
        RCO.Server_SplitResource(self.mCachedInventoryComponent, self.mSlotIdx, ReturnValue_1)
        goto(ExecutionFlow.Pop())
        
        # Label 299
        ReturnValue_2: InputEvent = Default__WidgetBlueprintLibrary.GetInputEventFromPointerEvent(Ref[MouseEvent])
        
        ReturnValue_3: bool = Default__KismetInputLibrary.InputEvent_IsControlDown(Ref[ReturnValue_2])
        
        ReturnValue1: InputEvent = Default__WidgetBlueprintLibrary.GetInputEventFromPointerEvent(Ref[MouseEvent])
        
        ReturnValue_4: bool = Default__KismetInputLibrary.InputEvent_IsShiftDown(Ref[ReturnValue1])
        
        ReturnValue_5: Key = Default__KismetInputLibrary.PointerEvent_GetEffectingButton(Ref[MouseEvent])
        ReturnValue_6: bool = BooleanOR(ReturnValue_4, ReturnValue_3)
        ReturnValue_7: bool = Default__KismetInputLibrary.EqualEqual_KeyKey(ReturnValue_5, Key(KeyName = "LeftMouseButton"))
        ReturnValue_8: bool = ReturnValue_7 and ReturnValue_6
        if not ReturnValue_8:
            goto('L977')
        
        # Label 746
        ReturnValue_2 = Default__WidgetBlueprintLibrary.GetInputEventFromPointerEvent(Ref[MouseEvent])
        
        ReturnValue_3 = Default__KismetInputLibrary.InputEvent_IsControlDown(Ref[ReturnValue_2])
        self.QuickMoveInventory(ReturnValue_3)
        self.SetInteractState(1)
        ReturnValue_9: EventReply = Default__WidgetBlueprintLibrary.Handled()
        ReturnValue_10: EventReply = ReturnValue_9
        goto('L1054')
        # Label 977
        ReturnValue_11: EventReply = Default__WidgetBlueprintLibrary.Unhandled()
        ReturnValue_10 = ReturnValue_11
    

    def OnKeyUp(self):
        
        ReturnValue: InputEvent = Default__WidgetBlueprintLibrary.GetInputEventFromKeyEvent(Ref[InKeyEvent])
        
        ReturnValue_0: bool = Default__KismetInputLibrary.InputEvent_IsLeftControlDown(Ref[ReturnValue])
        self.mShouldGrabAllOfType = ReturnValue_0
        ReturnValue_1: EventReply = Default__WidgetBlueprintLibrary.Unhandled()
        ReturnValue_2: EventReply = ReturnValue_1
    

    def OnKeyDown(self):
        
        ReturnValue: InputEvent = Default__WidgetBlueprintLibrary.GetInputEventFromKeyEvent(Ref[InKeyEvent])
        
        ReturnValue_0: bool = Default__KismetInputLibrary.InputEvent_IsLeftControlDown(Ref[ReturnValue])
        self.mShouldGrabAllOfType = ReturnValue_0
        ReturnValue_1: EventReply = Default__WidgetBlueprintLibrary.Unhandled()
        ReturnValue_2: EventReply = ReturnValue_1
    

    def CheckSlotHasItems(self):
        ReturnValue: bool = self.mNumItems > 0
        slotHasItems = ReturnValue
    

    def GetNumItems(self):
        Num = self.mNumItems
    

    def GetItemClass(self):
        ItemClass = self.mItemClass
    

    def GetStack(self):
        
        stack = None
        ReturnValue: bool = self.mCachedInventoryComponent.GetStackFromIndex(self.mSlotIdx, Ref[stack])
        stack = stack
    

    def GetTooltipWidget(self):
        ReturnValue: bool = Default__KismetSystemLibrary.IsValidClass(self.mItemClass)
        if not ReturnValue:
            goto('L297')
        ReturnValue1: Ptr[PlayerController] = self.GetOwningPlayer()
        # Label 89
        ReturnValue1_0: Ptr[Widget_Tooltip] = Default__WidgetBlueprintLibrary.Create(self, Widget_Tooltip, ReturnValue1)
        ItemAmount1.ItemClass = self.mItemClass
        ItemAmount1.amount = 0
        
        ItemAmount1 = None
        Default__KismetSystemLibrary.SetStructurePropertyByName(ReturnValue1_0, "mItemDescriptor", Ref[ItemAmount1])
        ReturnValue_0: Ptr[Widget] = ReturnValue1_0
        goto('L605')
        # Label 297
        ReturnValue1_1: bool = Default__KismetSystemLibrary.IsValidClass(self.mFilterItemDescriptor)
        if not ReturnValue1_1:
            goto('L594')
        ReturnValue_1: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_2: Ptr[Widget_Tooltip] = Default__WidgetBlueprintLibrary.Create(self, Widget_Tooltip, ReturnValue_1)
        ItemAmount.ItemClass = self.mFilterItemDescriptor
        ItemAmount.amount = 0
        
        ItemAmount = None
        Default__KismetSystemLibrary.SetStructurePropertyByName(ReturnValue_2, "mItemDescriptor", Ref[ItemAmount])
        ReturnValue_0 = ReturnValue_2
        goto('L605')
        # Label 594
        ReturnValue_0 = None
    

    def CreateSplitSlider(self):
        ExecutionFlow.Push("L591")
        FoundWidgets: List[Ptr[Widget_StackSplitSlider]] = []
        
        Default__WidgetBlueprintLibrary.GetAllWidgetsOfClass(self, Widget_StackSplitSlider, False, Ref[FoundWidgets])
        Variable: int32 = 0
        Variable_0: int32 = 0
        
        # Label 114
        ReturnValue: int32 = len(FoundWidgets)
        ReturnValue_0: bool = Variable <= ReturnValue
        if not ReturnValue_0:
            goto('L353')
        Variable_0 = Variable
        ExecutionFlow.Push("L517")
        
        Item = None
        Item = FoundWidgets[Variable_0]
        Item.CloseStackSplitSlider()
        goto(ExecutionFlow.Pop())
        # Label 353
        ReturnValue_1: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_2: Ptr[Widget_StackSplitSlider] = Default__WidgetBlueprintLibrary.Create(self, Widget_StackSplitSlider, ReturnValue_1)
        Default__KismetSystemLibrary.SetObjectPropertyByName(ReturnValue_2, "mSourceSlot", self)
        ReturnValue_3: Ptr[Widget] = ReturnValue_2
        goto('L591')
        # Label 517
        ReturnValue_4: int32 = Variable + 1
        # Label 559
        Variable = ReturnValue_4
        goto('L114')
    

    def OnFocusReceived(self):
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        Controller: Ptr[FGPlayerController] = Cast[FGPlayerController](ReturnValue)
        bSuccess: bool = Controller
        # Label 89
        if not bSuccess:
            goto('L739')
        ReturnValue_0: bool = Controller.GetIsUsingGamepad()
        if not ReturnValue_0:
            goto('L739')
        
        ReturnValue_1: Vector2D = Default__SlateBlueprintLibrary.GetLocalSize(Ref[MyGeometry])
        ReturnValue_2: Vector2D = Divide_Vector2DFloat(ReturnValue_1, 2)
        
        PixelPosition = None
        ViewportPosition = None
        Default__SlateBlueprintLibrary.LocalToViewport(self, ReturnValue_2, Ref[MyGeometry], Ref[PixelPosition], Ref[ViewportPosition])
        ReturnValue1: Ptr[PlayerController] = self.GetOwningPlayer()
        # Label 353
        ReturnValue_3: float = Default__WidgetLayoutLibrary.GetViewportScale(self)
        ReturnValue_4: Vector2D = Vector2D(ReturnValue_3, ReturnValue_3)
        ReturnValue_5: Vector2D = Multiply_Vector2DVector2D(ViewportPosition, ReturnValue_4)
        
        X = None
        Y = None
        BreakVector2D(ReturnValue_5, Ref[X], Ref[Y])
        ReturnValue_6: int32 = FTrunc(X)
        ReturnValue1_0: int32 = FTrunc(Y)
        ReturnValue1.SetMouseLocation(ReturnValue_6, ReturnValue1_0)
        ReturnValue_7: EventReply = Default__WidgetBlueprintLibrary.Handled()
        ReturnValue_8: EventReply = ReturnValue_7
        goto('L816')
        # Label 739
        ReturnValue_9: EventReply = Default__WidgetBlueprintLibrary.Unhandled()
        ReturnValue_8 = ReturnValue_9
    

    def GetGamepadButtonIsEnabled(self):
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        Controller: Ptr[FGPlayerController] = Cast[FGPlayerController](ReturnValue)
        bSuccess: bool = Controller
        # Label 89
        if not bSuccess:
            goto('L169')
        ReturnValue_0: bool = Controller.GetIsUsingGamepad()
        ReturnValue_1: bool = ReturnValue_0
        goto('L180')
        # Label 169
        ReturnValue_1 = False
    

    def GetFilterImage(self):
        ReturnValue: TSubclassOf[FGItemDescriptor] = self.GetFilterClass()
        LocalFilter = ReturnValue
        ReturnValue_0: bool = Default__KismetSystemLibrary.IsValidClass(LocalFilter)
        if not ReturnValue_0:
            goto('L713')
        if not self.mBigSlot:
            goto('L946')
        ReturnValue_1: Ptr[Texture2D] = Default__FGItemDescriptor.GetBigIcon(LocalFilter)
        Icon = ReturnValue_1
        # Label 192
        SlateColor.SpecifiedColor = LinearColor(R = 1, G = 1, B = 1, A = 0.5)
        SlateColor.ColorUseRule = 0
        SlateBrush.ImageSize = self.mItemImage.Brush.ImageSize
        SlateBrush.Margin = self.mItemImage.Brush.Margin
        SlateBrush.TintColor = SlateColor
        SlateBrush.ResourceObject = Icon
        SlateBrush.DrawAs = self.mItemImage.Brush.DrawAs
        SlateBrush.Tiling = self.mItemImage.Brush.Tiling
        SlateBrush.Mirroring = self.mItemImage.Brush.Mirroring
        ReturnValue_2: SlateBrush = SlateBrush
        goto('L1021')
        # Label 713
        ReturnValue_2 = SlateBrush(ImageSize = Vector2D(X = 32, Y = 32), Margin = Margin(Left = 0, Top = 0, Right = 0, Bottom = 0), TintColor = SlateColor(SpecifiedColor = LinearColor(R = 1, G = 1, B = 1, A = 1), ColorUseRule = 0), ResourceObject = None, ResourceName = "None", UVRegion = Box2D(Min = Vector2D(X = 0, Y = 0), Max = Vector2D(X = 0, Y = 0), bIsValid = 0), DrawAs = 3, Tiling = 0, Mirroring = 0, ImageType = 0, bIsDynamicallyLoaded = False, bHasUObject = False)
        goto('L1021')
        # Label 946
        ReturnValue_3: Ptr[Texture2D] = Default__FGItemDescriptor.GetSmallIcon(LocalFilter)
        Icon = ReturnValue_3
        goto('L192')
    

    def PlaySomeSound(self):
        ReturnValue: Ptr[Actor] = Default__FGBlueprintFunctionLibrary.GetOuterActor(self.mCachedInventoryComponent)
        AsCharacter: Ptr[Character] = Cast[Character](ReturnValue)
        bSuccess: bool = AsCharacter
        if not bSuccess:
            goto('L135')
        # End
    

    def GetItemImageBrush(self):
        if not self.mIsCostSlot:
            goto('L600')
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(self.mCostSlotBrush)
        if not ReturnValue:
            goto('L600')
        SlateColor.SpecifiedColor = LinearColor(R = 1, G = 1, B = 1, A = 1)
        SlateColor.ColorUseRule = 0
        # Label 169
        SlateBrush.ImageSize = self.mItemImage.Brush.ImageSize
        SlateBrush.Margin = self.mItemImage.Brush.Margin
        SlateBrush.TintColor = SlateColor
        SlateBrush.ResourceObject = self.mCostSlotBrush
        SlateBrush.DrawAs = self.mItemImage.Brush.DrawAs
        SlateBrush.Tiling = self.mItemImage.Brush.Tiling
        SlateBrush.Mirroring = self.mItemImage.Brush.Mirroring
        ReturnValue_0: SlateBrush = SlateBrush
        goto('L1470')
        
        slotHasItems = None
        # Label 600
        self.CheckSlotHasItems(Ref[slotHasItems])
        ReturnValue_1: bool = Default__KismetSystemLibrary.IsValidClass(self.mItemClass)
        ReturnValue_2: bool = ReturnValue_1 and slotHasItems
        if not ReturnValue_2:
            goto('L1331')
        if not self.mBigSlot:
            goto('L1395')
        ReturnValue_3: Ptr[Texture2D] = Default__FGItemDescriptor.GetBigIcon(self.mItemClass)
        Icon = ReturnValue_3
        # Label 810
        SlateColor1.SpecifiedColor = LinearColor(R = 1, G = 1, B = 1, A = 1)
        SlateColor1.ColorUseRule = 0
        SlateBrush1.ImageSize = self.mItemImage.Brush.ImageSize
        SlateBrush1.Margin = self.mItemImage.Brush.Margin
        SlateBrush1.TintColor = SlateColor1
        SlateBrush1.ResourceObject = Icon
        SlateBrush1.DrawAs = self.mItemImage.Brush.DrawAs
        SlateBrush1.Tiling = self.mItemImage.Brush.Tiling
        SlateBrush1.Mirroring = self.mItemImage.Brush.Mirroring
        ReturnValue_0 = SlateBrush1
        goto('L1470')
        # Label 1331
        ReturnValue_4: SlateBrush = self.GetFilterImage()
        ReturnValue_0 = ReturnValue_4
        goto('L1470')
        # Label 1395
        ReturnValue_5: Ptr[Texture2D] = Default__FGItemDescriptor.GetSmallIcon(self.mItemClass)
        Icon = ReturnValue_5
        goto('L810')
    

    def OnDrop(self):
        if not self.mIsLocked:
            goto('L46')
        self.SetDragAndDropState(0)
        # Label 30
        ReturnValue = False
        goto('L312')
        # Label 46
        Inventory: Ptr[BP_DragNDropInventory] = Cast[BP_DragNDropInventory](Operation)
        bSuccess: bool = Inventory
        if not bSuccess:
            goto('L277')
        Slot: Ptr[Widget_InventorySlot] = Cast[Widget_InventorySlot](Inventory.payload)
        bSuccess1: bool = Slot
        if not bSuccess1:
            goto('L277')
        
        Result = None
        self.DropOntoInventorySlot(Slot, Ref[Result])
        LocalResult = Result
        # Label 277
        self.SetDragAndDropState(0)
        ReturnValue = LocalResult
    

    def OnMouseButtonDown(self):
        localMouseEvent = MouseEvent
        
        ReturnValue: bool = Default__KismetInputLibrary.PointerEvent_IsMouseButtonDown(Key(KeyName = "RightMouseButton"), Ref[localMouseEvent])
        if not ReturnValue:
            goto('L385')
        ReturnValue_0: bool = self.mCachedInventoryComponent.CanSplitStackAtIdx(self.mSlotIdx)
        if not ReturnValue_0:
            goto('L651')
        OutputDelegate.BindUFunction(self, ShowSplitStackWidget)
        ReturnValue_1: TimerHandle = Default__KismetSystemLibrary.K2_SetTimerDelegate(OutputDelegate, self.mSplitStackHoldTime, False)
        self.mSplitStackTimerHandle = ReturnValue_1
        ReturnValue_2: EventReply = Default__WidgetBlueprintLibrary.Handled()
        # Label 353
        ReturnValue_3: EventReply = ReturnValue_2
        goto('L728')
        # Label 385
        ReturnValue_4: bool = self.mCachedInventoryComponent.IsSomethingOnIndex(self.mSlotIdx)
        if not ReturnValue_4:
            goto('L569')
        
        ReturnValue_5: EventReply = Default__WidgetBlueprintLibrary.DetectDragIfPressed(self, Key(KeyName = "LeftMouseButton"), Ref[localMouseEvent])
        ReturnValue_3 = ReturnValue_5
        goto('L728')
        # Label 569
        ReturnValue1: EventReply = Default__WidgetBlueprintLibrary.Unhandled()
        ReturnValue_3 = ReturnValue1
        goto('L728')
        # Label 651
        ReturnValue_6: EventReply = Default__WidgetBlueprintLibrary.Unhandled()
        ReturnValue_3 = ReturnValue_6
    

    def OnDragDetected(self):
        if not self.mIsLocked:
            goto('L30')
        Operation = None
        # End
        # Label 30
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_0: Ptr[Widget_InventoryDragNDropRep] = Default__WidgetBlueprintLibrary.Create(self, Widget_InventoryDragNDropRep, ReturnValue)
        Default__KismetSystemLibrary.SetObjectPropertyByName(ReturnValue_0, "mInventorySlotWidget", self)
        ReturnValue_1: Ptr[BP_DragNDropInventory] = Default__WidgetBlueprintLibrary.CreateDragDropOperation(BP_DragNDropInventory)
        Default__KismetSystemLibrary.SetObjectPropertyByName(ReturnValue_1, "payload", self)
        Default__KismetSystemLibrary.SetObjectPropertyByName(ReturnValue_1, "DefaultDragVisual", ReturnValue_0)
        ReturnValue_2: uint8 = Default__KismetSystemLibrary.MakeLiteralByte(1)
        Default__KismetSystemLibrary.SetBytePropertyByName(ReturnValue_1, "Pivot", ReturnValue_2)
        Variable: Const[Vector2D] = Vector2D(X = 0, Y = 0.10000000149011612)
        
        Default__KismetSystemLibrary.SetStructurePropertyByName(ReturnValue_1, "Offset", Ref[Variable])
        # Label 559
        Operation = ReturnValue_1
    

    def GetStackSizeText(self):
        ReturnValue: float = Default__FGInventoryLibrary.GetAmountConvertedByForm(self.mNumItems, self.mResourceForm)
        ReturnValue_0: FText = Default__KismetTextLibrary.Conv_FloatToText(ReturnValue, 0, False, True, 1, 324, 0, 1)
        ReturnValue_1: FText = ReturnValue_0
    

    def CacheSlotData(self):
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(self.mCachedInventoryComponent)
        if not ReturnValue:
            goto('L494')
        
        stack = None
        ReturnValue_0: bool = self.mCachedInventoryComponent.GetStackFromIndex(self.mSlotIdx, Ref[stack])
        if not ReturnValue_0:
            goto('L460')
        
        stack = None
        numItems = None
        item = None
        Default__FGInventoryLibrary.BreakInventoryStack(Ref[stack], Ref[numItems], Ref[item])
        self.mNumItems = numItems
        
        stack = None
        numItems = None
        item = None
        Default__FGInventoryLibrary.BreakInventoryStack(Ref[stack], Ref[numItems], Ref[item])
        
        item = None
        itemClass = None
        itemState = None
        Default__FGInventoryLibrary.BreakInventoryItem(Ref[item], Ref[itemClass], Ref[itemState])
        ReturnValue_1: bool = EqualEqual_ClassClass(itemClass, None)
        Variable: bool = ReturnValue_1
        
        switch = {
            False: itemClass,
            True: self.mFilterItemDescriptor
        }
        self.mItemClass = switch.get(Variable, None)
        # End
        # Label 460
        self.mNumItems = 0
        # Label 483
        self.mItemClass = None
    

    def OnMouseEnter(self):
        ExecuteUbergraph_Widget_InventorySlot.K2Node_Event_MyGeometry2 = MyGeometry #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_InventorySlot.K2Node_Event_MouseEvent1 = MouseEvent #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_InventorySlot(29)
    

    def OnMouseLeave(self):
        ExecuteUbergraph_Widget_InventorySlot.K2Node_Event_MouseEvent = MouseEvent #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_InventorySlot(215)
    

    def OnFocusLost(self):
        ExecuteUbergraph_Widget_InventorySlot.K2Node_Event_InFocusEvent = InFocusEvent #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_InventorySlot(236)
    

    def PreConstruct(self):
        ExecuteUbergraph_Widget_InventorySlot.K2Node_Event_IsDesignTime = IsDesignTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_InventorySlot(305)
    

    def UpdateStyle(self):
        self.ExecuteUbergraph_Widget_InventorySlot(342)
    

    def Destruct(self):
        self.ExecuteUbergraph_Widget_InventorySlot(755)
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_InventorySlot(802)
    

    def Event CreateNuclearWastePopup(self, isNuclearWaste: bool):
        ExecuteUbergraph_Widget_InventorySlot.K2Node_CustomEvent_isNuclearWaste = isNuclearWaste #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_InventorySlot(868)
    

    def CloseNuclearWastePopup(self, ConfirmClicked: bool):
        ExecuteUbergraph_Widget_InventorySlot.K2Node_CustomEvent_ConfirmClicked = ConfirmClicked #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_InventorySlot(1160)
    

    def CloseSplitStack(self):
        self.ExecuteUbergraph_Widget_InventorySlot(1244)
    

    def OnDragLeave(self):
        ExecuteUbergraph_Widget_InventorySlot.K2Node_Event_PointerEvent1 = PointerEvent #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_InventorySlot.K2Node_Event_Operation1 = Operation #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_InventorySlot(1281)
    

    def OnDragEnter(self):
        ExecuteUbergraph_Widget_InventorySlot.K2Node_Event_MyGeometry1 = MyGeometry #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_InventorySlot.K2Node_Event_PointerEvent = PointerEvent #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_InventorySlot.K2Node_Event_Operation = Operation #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_InventorySlot(1381)
    

    def Tick(self):
        ExecuteUbergraph_Widget_InventorySlot.K2Node_Event_MyGeometry = MyGeometry #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_InventorySlot.K2Node_Event_InDeltaTime = InDeltaTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_InventorySlot(1860)
    

    def ExecuteUbergraph_Widget_InventorySlot(self):
        # Label 10
        self.OnItemClassUpdated()
        # End
        ReturnValue1: Ptr[PlayerController] = self.GetOwningPlayer()
        self.SetUserFocus(ReturnValue1)
        
        slotHasItems = None
        self.CheckSlotHasItems(Ref[slotHasItems])
        if not slotHasItems:
            goto('L1865')
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_0: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_UI_Inventory_MouseOver, ReturnValue, True)
        self.SetInteractState(2)
        # End
        self.SetInteractState(1)
        # End
        self.mShouldGrabAllOfType = False
        
        slotHasItems1 = None
        self.CheckSlotHasItems(Ref[slotHasItems1])
        if not slotHasItems1:
            goto('L1865')
        self.SetInteractState(1)
        # End
        self.SetSlotSize(self.mSmallSlot, self.mBigSlot)
        # End
        self.OnItemClassUpdated()
        # Label 356
        ReturnValue_1: FText = self.GetStackSizeText()
        self.mBackgroundText.SetText(ReturnValue_1)
        self.mStackSizeLbl.SetText(ReturnValue_1)
        # End
        # Label 483
        self.UpdateStyle()
        OutputDelegate.BindUFunction(self, UpdateStyle)
        ReturnValue_2: TimerHandle = Default__KismetSystemLibrary.K2_SetTimerDelegate(OutputDelegate, 0.10000000149011612, True)
        self.mUpdateTimer = ReturnValue_2
        self.CacheSlotData()
        ReturnValue_3: Ptr[FGGameUserSettings] = Default__FGGameUserSettings.GetFGGameUserSettings()
        ReturnValue_4: bool = ReturnValue_3.GetBoolOptionValue("FG.ItemAbbreviation")
        self.mAbbreviateName = ReturnValue_4
        goto('L10')
        
        Default__KismetSystemLibrary.K2_ClearAndInvalidateTimerHandle(self, Ref[self.mUpdateTimer])
        # End
        ReturnValue_5: Ptr[MaterialInstanceDynamic] = self.mSlotBg.GetDynamicMaterial()
        self.mSlotBgMaterial = ReturnValue_5
        goto('L483')
        if not isNuclearWaste:
            goto('L1865')
        ReturnValue2: Ptr[PlayerController] = self.GetOwningPlayer()
        OutputDelegate1.BindUFunction(self, CloseNuclearWastePopup)
        
        OutputDelegate1 = None
        Default__FGBlueprintFunctionLibrary.AddPopupWithCloseDelegate(ReturnValue2, "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 971, 'Value': 'Nuclear Waste cannot be destroyed.'}", "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 1045, 'Value': 'Nuclear Waste cannot be destroyed.\r\nFicsit does not waste.'}", 0, None, None, Ref[OutputDelegate1])
        # End
        if not ConfirmClicked:
            goto('L1865')
        ReturnValue3: Ptr[PlayerController] = self.GetOwningPlayer()
        Default__FGBlueprintFunctionLibrary.ClosePopup(ReturnValue3)
        # End
        self.mSplitMenuAnchor.Close()
        # End
        Inventory: Ptr[BP_DragNDropInventory] = Cast[BP_DragNDropInventory](Operation1)
        bSuccess: bool = Inventory
        if not bSuccess:
            goto('L1865')
        self.SetDragAndDropState(0)
        # End
        Inventory1: Ptr[BP_DragNDropInventory] = Cast[BP_DragNDropInventory](Operation)
        bSuccess1: bool = Inventory1
        if not bSuccess1:
            goto('L1865')
        Slot: Ptr[Widget_InventorySlot] = Cast[Widget_InventorySlot](Inventory1.payload)
        bSuccess2: bool = Slot
        if not bSuccess2:
            goto('L1865')
        Variable: uint8 = 1
        Variable1: uint8 = 2
        ReturnValue_6: bool = Not_PreBool(self.mIsLocked)
        ReturnValue_7: bool = self.mCachedInventoryComponent.IsItemAllowed(Slot.mItemClass, self.mSlotIdx)
        ReturnValue_8: bool = ReturnValue_7 and ReturnValue_6
        Variable_0: bool = ReturnValue_8
        
        switch = {
            False: Variable1,
            True: Variable
        }
        self.SetDragAndDropState(switch.get(Variable_0, None))
        # End
        # Label 1841
        self.CacheSlotData()
        # End
        goto('L1841')
    

    def OnMoveStack__DelegateSignature(self, Sender: Ptr[Widget_InventorySlot]):
        pass
    

    def OnSlotHovered__DelegateSignature(self, SelfInventorySlot: Ptr[Widget_InventorySlot]):
        pass
    
