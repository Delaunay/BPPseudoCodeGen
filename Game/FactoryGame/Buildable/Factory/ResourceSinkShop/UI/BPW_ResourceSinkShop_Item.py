
from codegen.ue4_stub import *

from Game.FactoryGame.Buildable.Factory.ResourceSinkShop.UI.E_ResourceSinkShop_Item_State import E_ResourceSinkShop_Item_State
from Script.Engine import SetScalarParameterValue
from Script.Engine import Texture2D
from Script.Engine import SetClassPropertyByName
from Script.Engine import EqualEqual_ByteByte
from Script.FactoryGame import GetItemIcon
from Script.Engine import MaterialInstanceDynamic
from Script.SlateCore import Margin
from Game.FactoryGame.Buildable.Factory.ResourceSinkShop.UI.BPW_ResourceSink_InfoBox import BPW_ResourceSink_InfoBox
from Script.UMG import GetEffectMaterial
from Script.Engine import Default__KismetSystemLibrary
from Script.FactoryGame import Get
from Script.Engine import PlayerController
from Script.UMG import PlayAnimation
from Script.Engine import FormatArgumentData
from Game.FactoryGame.Buildable.Factory.ResourceSinkShop.UI.BPW_ResourceSinkShop_Item import ExecuteUbergraph_BPW_ResourceSinkShop_Item
from Script.FactoryGame import IsRepeatPurchasesAllowed
from Script.UMG import Open
from Script.UMG import Default__WidgetBlueprintLibrary
from Script.Engine import Conv_IntToText
from Script.Engine import Default__KismetTextLibrary
from Script.Engine import TextToUpper
from Script.UMG import Widget
from Script.Engine import Format
from Script.FactoryGame import FGButtonWidget
from Script.FactoryGame import FGSchematic
from Script.UMG import WidgetAnimation
from Script.Engine import NotEqual_ByteByte
from Script.UMG import Close
from Script.UMG import GetBrushResourceAsTexture2D
from Script.FactoryGame import IsSchematicPurchased
from Script.UMG import UMGSequencePlayer
from Script.FactoryGame import FGSchematicManager
from Script.UMG import Create
from Script.FactoryGame import Default__FGSchematic
from Script.CoreUObject import Vector2D
from Script.SlateCore import SlateBrush
from Script.SlateCore import SlateColor
from Script.FactoryGame import Default__FGSchematicManager
from Script.Engine import IsValidClass
from Script.FactoryGame import GetSchematicDisplayName
from Script.CoreUObject import LinearColor

class BPW_ResourceSinkShop_Item(FGButtonWidget):
    AddedToCartAnim: Ptr[WidgetAnimation]
    OnHoverAnim: Ptr[WidgetAnimation]
    FGSchematic: TSubclassOf[FGSchematic]
    OnShopItemClicked: FMulticastScriptDelegate
    OnShopItemHovered: FMulticastScriptDelegate
    mSchematicCost: int32
    mItemNameText: FText
    mItemIconBrush: Ptr[Texture2D]
    mItemCostText: FText
    OnBuyButtonClicked: FMulticastScriptDelegate
    mForceHover: bool
    mIsAddedToCart: bool
    mTooltipWidget: Ptr[BPW_ResourceSink_InfoBox]
    mOldState: uint8
    padding = Namespace(Bottom=12, Left=12, Right=12, Top=12)
    
    def OnClicked(self):
        
        State = None
        self.GetButtonState(Ref[State])
        ReturnValue: bool = EqualEqual_ByteByte(State, 0)
        if not ReturnValue:
            goto('L156')
        self.OnShopItemClicked.ProcessMulticastDelegate(self.FGSchematic)
        # Label 96
        self.UpdateButtonState()
        ReturnValue_0: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.AddedToCartAnim, 0, 1, 0, 1)
    

    def GetButtonState(self):
        ReturnValue: bool = Default__FGSchematic.IsRepeatPurchasesAllowed(self.FGSchematic)
        if not ReturnValue:
            goto('L90')
        State = 0
        # End
        # Label 90
        if not self.mIsAddedToCart:
            goto('L129')
        State = 1
        # End
        # Label 129
        ReturnValue_0: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_1: Ptr[FGSchematicManager] = Default__FGSchematicManager.Get(ReturnValue_0)
        ReturnValue_2: bool = ReturnValue_1.IsSchematicPurchased(self.FGSchematic)
        # Label 255
        if not ReturnValue_2:
            goto('L294')
        State = 2
        # End
        # Label 294
        State = 0
    

    def OpenTooltipMenu(self):
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_0: Ptr[BPW_ResourceSink_InfoBox] = Default__WidgetBlueprintLibrary.Create(self, BPW_ResourceSink_InfoBox, ReturnValue)
        Default__KismetSystemLibrary.SetClassPropertyByName(ReturnValue_0, "mHoveredSchematic", self.FGSchematic)
        self.mTooltipWidget = ReturnValue_0
        self.mTooltipWidget.UpdateTooltipInfo(self.FGSchematic)
        ReturnValue_1: Ptr[Widget] = self.mTooltipWidget
    

    def UpdateButtonState(self):
        0: uint8 = 0
        
        State1 = None
        self.GetButtonState(Ref[State1])
        CmpSuccess: bool = NotEqual_ByteByte(State1, 0)
        if not CmpSuccess:
            goto('L183')
        CmpSuccess = NotEqual_ByteByte(State1, 1)
        if not CmpSuccess:
            goto('L406')
        CmpSuccess = NotEqual_ByteByte(State1, 2)
        if not CmpSuccess:
            goto('L669')
        # End
        # Label 183
        self.mAddToCart_Button.SetVisibility(0)
        self.mUnavailableText.SetVisibility(2)
        ReturnValue: Ptr[MaterialInstanceDynamic] = self.mRetainerBox.GetEffectMaterial()
        ReturnValue.SetScalarParameterValue("amount", 0)
        
        State = None
        # Label 351
        self.GetButtonState(Ref[State])
        self.mOldState = State
        # End
        # Label 406
        self.mUnavailableText.SetVisibility(0)
        self.mUnavailableText.SetText("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 481, 'Value': 'ALREADY IN CART'}")
        self.mAddToCart_Button.SetVisibility(2)
        ReturnValue1: bool = EqualEqual_ByteByte(self.mOldState, 0)
        if not ReturnValue1:
            goto('L1026')
        ReturnValue1_0: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.OnHoverAnim, 0, 1, 1, 1)
        goto('L351')
        # Label 669
        self.mAddToCart_Button.SetVisibility(2)
        self.mUnavailableText.SetVisibility(0)
        self.mUnavailableText.SetText("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 782, 'Value': 'P U R C H A S E D'}")
        ReturnValue1_1: Ptr[MaterialInstanceDynamic] = self.mRetainerBox.GetEffectMaterial()
        ReturnValue1_1.SetScalarParameterValue("amount", 1)
        ReturnValue_0: bool = EqualEqual_ByteByte(self.mOldState, 0)
        if not ReturnValue_0:
            goto('L1026')
        ReturnValue_1: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.OnHoverAnim, 0, 1, 1, 1)
        goto('L351')
    

    def GetItemCost(self, Cost: int32):
        ReturnValue: FText = Default__KismetTextLibrary.Conv_IntToText(Cost, False, True, 1, 324)
        self.mItemCostText = ReturnValue
        FormatArgumentData.ArgumentName = "Cost"
        FormatArgumentData.ArgumentValueType = 4
        FormatArgumentData.ArgumentValue = self.mItemCostText
        FormatArgumentData.ArgumentValueInt = 0
        FormatArgumentData.ArgumentValueFloat = 0
        FormatArgumentData.ArgumentValueGender = 0
        Array: List[FormatArgumentData] = [FormatArgumentData]
        ReturnValue_0: FText = Default__KismetTextLibrary.Format("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 360, 'Value': 'x{Cost} '}", Array)
        self.mSchematicCostText.SetText(ReturnValue_0)
    

    def GetItemIcon(self):
        ReturnValue: bool = Default__KismetSystemLibrary.IsValidClass(self.FGSchematic)
        if not ReturnValue:
            goto('L543')
        ReturnValue_0: SlateBrush = Default__FGSchematic.GetItemIcon(self.FGSchematic)
        
        ReturnValue_1: Ptr[Texture2D] = Default__WidgetBlueprintLibrary.GetBrushResourceAsTexture2D(Ref[ReturnValue_0])
        self.mItemIconBrush = ReturnValue_1
        SlateBrush.ImageSize = Vector2D(X = 32, Y = 32)
        SlateBrush.Margin = Margin(Left = 0, Top = 0, Right = 0, Bottom = 0)
        SlateBrush.TintColor = SlateColor(SpecifiedColor = LinearColor(R = 1, G = 1, B = 1, A = 1), ColorUseRule = 0)
        SlateBrush.ResourceObject = self.mItemIconBrush
        SlateBrush.DrawAs = 3
        SlateBrush.Tiling = 0
        SlateBrush.Mirroring = 0
        
        SlateBrush = None
        self.mIcon.SetBrush(Ref[SlateBrush])
    

    def GetItemName(self):
        ReturnValue: bool = Default__KismetSystemLibrary.IsValidClass(self.FGSchematic)
        if not ReturnValue:
            goto('L255')
        ReturnValue_0: FText = Default__FGSchematic.GetSchematicDisplayName(self.FGSchematic)
        self.mItemNameText = ReturnValue_0
        
        ReturnValue_1: FText = Default__KismetTextLibrary.TextToUpper(Ref[self.mItemNameText])
        self.mShopItemName.SetText(ReturnValue_1)
    

    def Construct(self):
        self.ExecuteUbergraph_BPW_ResourceSinkShop_Item(77)
    

    def BndEvt__mShopItemButton_K2Node_ComponentBoundEvent_0_OnButtonClickedEvent__DelegateSignature(self):
        self.ExecuteUbergraph_BPW_ResourceSinkShop_Item(215)
    

    def BndEvt__mShopItemButton_K2Node_ComponentBoundEvent_1_OnButtonHoverEvent__DelegateSignature(self):
        self.ExecuteUbergraph_BPW_ResourceSinkShop_Item(234)
    

    def BndEvt__mShopItemButton_K2Node_ComponentBoundEvent_2_OnButtonHoverEvent__DelegateSignature(self):
        self.ExecuteUbergraph_BPW_ResourceSinkShop_Item(351)
    

    def SimulateOnHovered(self):
        self.ExecuteUbergraph_BPW_ResourceSinkShop_Item(538)
    

    def SimulateOnUnhovered(self):
        self.ExecuteUbergraph_BPW_ResourceSinkShop_Item(554)
    

    def BndEvt__mAddToCart_Button_K2Node_ComponentBoundEvent_4_OnButtonClickedEvent__DelegateSignature(self):
        self.ExecuteUbergraph_BPW_ResourceSinkShop_Item(570)
    

    def ExecuteUbergraph_BPW_ResourceSinkShop_Item(self):
        # Label 10
        self.GetItemIcon()
        self.GetItemCost(self.mSchematicCost)
        self.bIsFocusable = True
        self.UpdateButtonState()
        # End
        self.GetItemName()
        goto('L10')
        
        State = None
        # Label 96
        self.GetButtonState(Ref[State])
        ReturnValue: bool = EqualEqual_ByteByte(State, 0)
        if not ReturnValue:
            goto('L584')
        ReturnValue_0: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.OnHoverAnim, 0, 1, 0, 1)
        # End
        self.OnClicked()
        # End
        # Label 234
        self.OnShopItemHovered.ProcessMulticastDelegate(self.FGSchematic, self)
        self.Widget_AutoScrollingContainer.StartAutoScroll()
        self.mTooltipMenuAnchor.Open(False)
        goto('L96')
        # Label 351
        self.Widget_AutoScrollingContainer.StopAutoScroll()
        self.mTooltipMenuAnchor.Close()
        
        State1 = None
        self.GetButtonState(Ref[State1])
        ReturnValue1: bool = EqualEqual_ByteByte(State1, 0)
        if not ReturnValue1:
            goto('L584')
        ReturnValue1_0: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.OnHoverAnim, 0, 1, 1, 1)
        # End
        self.mForceHover = True
        goto('L234')
        self.mForceHover = False
        goto('L351')
        self.OnClicked()
    

    def OnBuyButtonClicked__DelegateSignature(self, mSchematic: TSubclassOf[FGSchematic]):
        pass
    

    def OnShopItemHovered__DelegateSignature(self, FGSchematic: TSubclassOf[FGSchematic], Button: Ptr[BPW_ResourceSinkShop_Item]):
        pass
    

    def OnShopItemClicked__DelegateSignature(self, FGSchematic: TSubclassOf[FGSchematic]):
        pass
    
