
from codegen.ue4_stub import *

from Script.Engine import Texture
from Script.Engine import Texture2D
from Script.Engine import FClamp
from Game.FactoryGame.Interface.UI.InGame.Widget_CostSlotWrapper import ExecuteUbergraph_Widget_CostSlotWrapper.K2Node_CustomEvent_BigSlot
from Game.FactoryGame.Interface.UI.InGame.Widget_CostSlotWrapper import ExecuteUbergraph_Widget_CostSlotWrapper.K2Node_Event_MouseEvent
from Game.FactoryGame.Interface.UI.InGame.Widget_CostSlotWrapper import ExecuteUbergraph_Widget_CostSlotWrapper
from Script.FactoryGame import EResourceForm
from Script.UMG import OverlaySlot
from Game.FactoryGame.Interface.UI.InGame.Widget_CostSlotWrapper import ExecuteUbergraph_Widget_CostSlotWrapper.K2Node_CustomEvent_IconTexture
from Script.UMG import Default__WidgetLayoutLibrary
from Script.FactoryGame import Default__FGInventoryLibrary
from Script.Engine import Conv_IntToFloat
from Script.UMG import SlotAsOverlaySlot
from Script.UMG import SetJustification
from Game.FactoryGame.Interface.UI.InGame.Widget_CostSlotWrapper import ExecuteUbergraph_Widget_CostSlotWrapper.K2Node_CustomEvent_ForceOrangeTextbox
from Game.FactoryGame.Interface.UI.InGame.Widget_CostSlotWrapper import ExecuteUbergraph_Widget_CostSlotWrapper.K2Node_Event_InDeltaTime
from Game.FactoryGame.Interface.UI.InGame.Widget_CostSlotWrapper import ExecuteUbergraph_Widget_CostSlotWrapper.K2Node_Event_IsDesignTime
from Script.Engine import Ease
from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import EqualEqual_FloatFloat
from Game.FactoryGame.Interface.UI.InGame.Widget_CostSlotWrapper import ExecuteUbergraph_Widget_CostSlotWrapper.K2Node_CustomEvent_CurrentNumInSlot
from Script.FactoryGame import GetAmountConvertedByForm
from Script.UMG import SetHorizontalAlignment
from Script.UMG import SetRenderTranslation
from Script.Engine import FormatArgumentData
from Script.UMG import PlayAnimation
from Script.FactoryGame import GetBigIcon
from Script.Engine import Conv_FloatToText
from Script.FactoryGame import GetForm
from Script.FactoryGame import FGInventoryComponent
from Script.Engine import GetWorldDeltaSeconds
from Script.Engine import IsValid
from Script.UMG import StopAnimation
from Game.FactoryGame.Interface.UI.InGame.Widget_CostSlotWrapper import ExecuteUbergraph_Widget_CostSlotWrapper.K2Node_Event_MyGeometry1
from Script.UMG import SetColorAndOpacity
from Script.Engine import EqualEqual_IntInt
from Script.Engine import Default__KismetTextLibrary
from Script.FactoryGame import GetSmallIcon
from Script.Engine import BooleanOR
from Script.Engine import Default__GameplayStatics
from Script.FactoryGame import GetNumItems
from Script.Engine import Format
from Script.UMG import WidgetAnimation
from Script.UMG import UserWidget
from Game.FactoryGame.Interface.UI.HUDHelpers.HUDHelpers import Default__HUDHelpers
from Game.FactoryGame.Interface.UI.InGame.Widget_CostSlotWrapper import ExecuteUbergraph_Widget_CostSlotWrapper.K2Node_CustomEvent_SlotIdx
from Game.FactoryGame.Interface.UI.InGame.Widget_CostSlotWrapper import ExecuteUbergraph_Widget_CostSlotWrapper.K2Node_CustomEvent_SmallSlot
from Script.UMG import UMGSequencePlayer
from Script.FactoryGame import Default__FGItemDescriptor
from Script.UMG import IsAnimationPlaying
from Script.FactoryGame import FGItemDescriptor
from Script.CoreUObject import Vector2D
from Script.SlateCore import SlateBrush
from Game.FactoryGame.Interface.UI.InGame.Widget_CostSlotWrapper import ExecuteUbergraph_Widget_CostSlotWrapper.K2Node_Event_MyGeometry
from Script.FactoryGame import ItemAmount
from Game.FactoryGame.Interface.UI.InGame.Widget_CostSlotWrapper import ExecuteUbergraph_Widget_CostSlotWrapper.K2Node_CustomEvent_ItemAmount
from Script.Engine import IsValidClass
from Game.FactoryGame.Interface.UI.InGame.Widget_CostSlotWrapper import ExecuteUbergraph_Widget_CostSlotWrapper.K2Node_CustomEvent_CachedInventoryComponent
from Script.CoreUObject import LinearColor

class Widget_CostSlotWrapper(UserWidget):
    FadeAnim: Ptr[WidgetAnimation]
    mCost: int32
    mIconBrush: Ptr[Texture]
    DefaultBrush: SlateBrush = Namespace(DrawAs=3, ImageSize={'X': 26, 'Y': 26}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$AssetPath': '/Game/FactoryGame/Interface/UI/Assets/BuildMenu/Cross.Cross'}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 0, 'B': 0, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    HasIconBrush: bool
    mItemCost: ItemAmount
    mCurrentNumInSlot: int32
    mFejkInventoryComponent: Ptr[FGInventoryComponent]
    T: float
    LerpTime: float = 0.5
    LastValue: float
    mForceOrangeTextbox: bool
    itemDescriptor: TSubclassOf[FGItemDescriptor]
    mForceEmptyAnim: bool
    mSmallSlot: bool
    mBigSlot: bool
    
    def FormatNumbers(self, NumItems: int32):
        ReturnValue: bool = Default__KismetSystemLibrary.IsValidClass(self.itemDescriptor)
        if not ReturnValue:
            goto('L334')
        ReturnValue_0: uint8 = Default__FGItemDescriptor.GetForm(self.itemDescriptor)
        LocalForm = ReturnValue_0
        # Label 151
        ReturnValue_1: float = Default__FGInventoryLibrary.GetAmountConvertedByForm(NumItems, LocalForm)
        ReturnValue_2: FText = Default__KismetTextLibrary.Conv_FloatToText(ReturnValue_1, 0, False, True, 1, 324, 0, 1)
        Out Text = ReturnValue_2
        # End
        # Label 334
        LocalForm = 1
        goto('L151')
    

    def SetIconBrush(self, IconTexture: Ptr[Texture]):
        self.mIconBrush = IconTexture
        self.HasIconBrush = True
    

    def GetProgressbarPercent(self):
        ReturnValue: bool = self.mCost <= 0
        ReturnValue_0: bool = BooleanOR(self.mForceOrangeTextbox, ReturnValue)
        # Label 72
        if not ReturnValue_0:
            goto('L114')
        ReturnValue_1: float = 1
        goto('L2730')
        # Label 114
        ReturnValue1: bool = self.mCurrentNumInSlot > 0
        if not ReturnValue1:
            goto('L1309')
        ReturnValue_2: float = Default__GameplayStatics.GetWorldDeltaSeconds(self)
        ReturnValue_3: float = ReturnValue_2 / self.LerpTime
        ReturnValue_4: float = ReturnValue_3 + self.T
        self.T = ReturnValue_4
        ReturnValue_5: float = FClamp(self.T, 0, 1)
        ReturnValue1_0: float = Conv_IntToFloat(self.mCost)
        ReturnValue2: float = Conv_IntToFloat(self.mCurrentNumInSlot)
        ReturnValue2_0: float = ReturnValue2 / ReturnValue1_0
        ReturnValue2_1: float = FClamp(ReturnValue2_0, 0, 1)
        ReturnValue_6: float = Ease(self.LastValue, ReturnValue2_1, ReturnValue_5, 7, 2, 2)
        ReturnValue_7: bool = EqualEqual_FloatFloat(ReturnValue_6, ReturnValue2_1)
        if not ReturnValue_7:
            goto('L996')
        ReturnValue_5 = FClamp(self.T, 0, 1)
        ReturnValue1_0 = Conv_IntToFloat(self.mCost)
        ReturnValue2 = Conv_IntToFloat(self.mCurrentNumInSlot)
        ReturnValue2_0 = ReturnValue2 / ReturnValue1_0
        ReturnValue2_1 = FClamp(ReturnValue2_0, 0, 1)
        ReturnValue_6 = Ease(self.LastValue, ReturnValue2_1, ReturnValue_5, 7, 2, 2)
        self.LastValue = ReturnValue_6
        self.T = 0
        # Label 996
        ReturnValue_5 = FClamp(self.T, 0, 1)
        ReturnValue1_0 = Conv_IntToFloat(self.mCost)
        ReturnValue2 = Conv_IntToFloat(self.mCurrentNumInSlot)
        ReturnValue2_0 = ReturnValue2 / ReturnValue1_0
        ReturnValue2_1 = FClamp(ReturnValue2_0, 0, 1)
        ReturnValue_6 = Ease(self.LastValue, ReturnValue2_1, ReturnValue_5, 7, 2, 2)
        ReturnValue_1 = ReturnValue_6
        goto('L2730')
        
        Num = None
        # Label 1309
        self.Widget_InventorySlot.GetNumItems(Ref[Num])
        ReturnValue_8: bool = Num > 0
        if not ReturnValue_8:
            goto('L2684')
        ReturnValue1_1: float = Default__GameplayStatics.GetWorldDeltaSeconds(self)
        ReturnValue1_2: float = ReturnValue1_1 / self.LerpTime
        ReturnValue1_3: float = ReturnValue1_2 + self.T
        self.T = ReturnValue1_3
        ReturnValue1_4: float = FClamp(self.T, 0, 1)
        
        Num1 = None
        self.Widget_InventorySlot.GetNumItems(Ref[Num1])
        ReturnValue_9: float = Conv_IntToFloat(Num1)
        ReturnValue3: float = Conv_IntToFloat(self.mCost)
        ReturnValue3_0: float = ReturnValue_9 / ReturnValue3
        ReturnValue3_1: float = FClamp(ReturnValue3_0, 0, 1)
        ReturnValue1_5: float = Ease(self.LastValue, ReturnValue3_1, ReturnValue1_4, 7, 2, 2)
        ReturnValue1_6: bool = EqualEqual_FloatFloat(ReturnValue3_1, ReturnValue1_5)
        if not ReturnValue1_6:
            goto('L2326')
        ReturnValue1_4 = FClamp(self.T, 0, 1)
        
        Num1 = None
        self.Widget_InventorySlot.GetNumItems(Ref[Num1])
        ReturnValue_9 = Conv_IntToFloat(Num1)
        ReturnValue3 = Conv_IntToFloat(self.mCost)
        ReturnValue3_0 = ReturnValue_9 / ReturnValue3
        ReturnValue3_1 = FClamp(ReturnValue3_0, 0, 1)
        ReturnValue1_5 = Ease(self.LastValue, ReturnValue3_1, ReturnValue1_4, 7, 2, 2)
        self.LastValue = ReturnValue1_5
        self.T = 0
        # Label 2326
        ReturnValue1_4 = FClamp(self.T, 0, 1)
        
        Num1 = None
        self.Widget_InventorySlot.GetNumItems(Ref[Num1])
        ReturnValue_9 = Conv_IntToFloat(Num1)
        ReturnValue3 = Conv_IntToFloat(self.mCost)
        ReturnValue3_0 = ReturnValue_9 / ReturnValue3
        ReturnValue3_1 = FClamp(ReturnValue3_0, 0, 1)
        ReturnValue1_5 = Ease(self.LastValue, ReturnValue3_1, ReturnValue1_4, 7, 2, 2)
        ReturnValue_1 = ReturnValue1_5
        goto('L2730')
        # Label 2684
        self.LastValue = 0
        ReturnValue_1 = 0
    

    def GetOrange(self):
        ReturnValue: bool = Default__KismetSystemLibrary.IsValidClass(self.itemDescriptor)
        if not ReturnValue:
            goto('L534')
        Variable: LinearColor = LinearColor(R = 0.7835379838943481, G = 0.2917709946632385, B = 0.057805001735687256, A = 1)
        Variable1: LinearColor = LinearColor(R = 0.7835379838943481, G = 0.2917709946632385, B = 0.057805001735687256, A = 1)
        Variable2: LinearColor = LinearColor(R = 0.10588199645280838, G = 0.3803919851779938, B = 0.556863009929657, A = 1)
        Variable3: LinearColor = LinearColor(R = 0.7835379838943481, G = 0.2917709946632385, B = 0.057805001735687256, A = 1)
        Variable4: LinearColor = LinearColor(R = 0.7835379838943481, G = 0.2917709946632385, B = 0.057805001735687256, A = 1)
        ReturnValue_0: uint8 = Default__FGItemDescriptor.GetForm(self.itemDescriptor)
        Variable_0: uint8 = ReturnValue_0
        
        switch = {
            0: Variable4,
            1: Variable3,
            2: Variable2,
            3: Variable1,
            4: Variable
        }
        ReturnValue_1: LinearColor = switch.get(Variable_0, None)
        goto('L616')
        
        Orange = None
        OrangeText = None
        # Label 534
        Default__HUDHelpers.GetFactoryGameOrange(self, Ref[Orange], Ref[OrangeText])
        ReturnValue_1 = Orange
    

    def SetTextboxFormating(self, HasItems: bool):
        if not HasItems:
            goto('L279')
        ReturnValue1: Ptr[OverlaySlot] = Default__WidgetLayoutLibrary.SlotAsOverlaySlot(self.TextboxContainer)
        ReturnValue1.SetHorizontalAlignment(0)
        self.StackSizeOverlay.SetRenderTranslation(Vector2D(X = 0, Y = 1))
        self.mStackSizeLbl.SetJustification(1)
        ReturnValue: Ptr[OverlaySlot] = Default__WidgetLayoutLibrary.SlotAsOverlaySlot(self.mStackSizeLbl)
        ReturnValue.SetHorizontalAlignment(0)
        # End
        # Label 279
        ReturnValue1 = Default__WidgetLayoutLibrary.SlotAsOverlaySlot(self.TextboxContainer)
        ReturnValue1.SetHorizontalAlignment(3)
        self.StackSizeOverlay.SetRenderTranslation(Vector2D(X = 1, Y = 1))
        self.mStackSizeLbl.SetJustification(2)
        ReturnValue = Default__WidgetLayoutLibrary.SlotAsOverlaySlot(self.mStackSizeLbl)
        ReturnValue.SetHorizontalAlignment(3)
    

    def GetDarkGray(self):
        
        Text = None
        Graphics = None
        Default__HUDHelpers.GetFactoryGameDarkGray(self, Ref[Text], Ref[Graphics])
        ReturnValue = Graphics
    

    def SetPartsNumbers(self):
        ReturnValue1: bool = self.mCurrentNumInSlot > 0
        
        Num1 = None
        self.Widget_InventorySlot.GetNumItems(Ref[Num1])
        ReturnValue2: bool = Num1 > 0
        ReturnValue: bool = BooleanOR(ReturnValue2, ReturnValue1)
        # Label 151
        if not ReturnValue:
            goto('L835')
        ReturnValue_0: bool = self.mCurrentNumInSlot > 0
        if not ReturnValue_0:
            goto('L914')
        self.SetTextboxFormating(True)
        
        Text1 = None
        self.FormatNumbers(self.mCost, Ref[Text1])
        FormatArgumentData1.ArgumentName = "1"
        FormatArgumentData1.ArgumentValueType = 4
        FormatArgumentData1.ArgumentValue = Text1
        FormatArgumentData1.ArgumentValueInt = 0
        FormatArgumentData1.ArgumentValueFloat = 0
        FormatArgumentData1.ArgumentValueGender = 0
        
        Text2 = None
        self.FormatNumbers(self.mCurrentNumInSlot, Ref[Text2])
        FormatArgumentData2.ArgumentName = "0"
        FormatArgumentData2.ArgumentValueType = 4
        FormatArgumentData2.ArgumentValue = Text2
        FormatArgumentData2.ArgumentValueInt = 0
        FormatArgumentData2.ArgumentValueFloat = 0
        FormatArgumentData2.ArgumentValueGender = 0
        Array: List[FormatArgumentData] = [FormatArgumentData2, FormatArgumentData1]
        ReturnValue_1: FText = Default__KismetTextLibrary.Format("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 748, 'Value': '{0}/{1}'}", Array)
        ReturnValue_2: FText = ReturnValue_1
        goto('L1576')
        # Label 835
        self.SetTextboxFormating(False)
        
        Text4 = None
        self.FormatNumbers(self.mCost, Ref[Text4])
        ReturnValue_2 = Text4
        goto('L1576')
        # Label 914
        self.SetTextboxFormating(True)
        
        Num = None
        self.Widget_InventorySlot.GetNumItems(Ref[Num])
        
        Text = None
        self.FormatNumbers(Num, Ref[Text])
        FormatArgumentData.ArgumentName = "0"
        FormatArgumentData.ArgumentValueType = 4
        FormatArgumentData.ArgumentValue = Text
        FormatArgumentData.ArgumentValueInt = 0
        FormatArgumentData.ArgumentValueFloat = 0
        FormatArgumentData.ArgumentValueGender = 0
        
        Text3 = None
        self.FormatNumbers(self.mCost, Ref[Text3])
        FormatArgumentData3.ArgumentName = "1"
        FormatArgumentData3.ArgumentValueType = 4
        FormatArgumentData3.ArgumentValue = Text3
        FormatArgumentData3.ArgumentValueInt = 0
        FormatArgumentData3.ArgumentValueFloat = 0
        FormatArgumentData3.ArgumentValueGender = 0
        Array1: List[FormatArgumentData] = [FormatArgumentData, FormatArgumentData3]
        ReturnValue1_0: FText = Default__KismetTextLibrary.Format("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 1494, 'Value': '{0}/{1}'}", Array1)
        ReturnValue_2 = ReturnValue1_0
    

    def Setup CostIcon(self, IconTexture: Ptr[Texture], ItemAmount: ItemAmount, CachedInventoryComponent: Ptr[FGInventoryComponent], slotIdx: int32, CurrentNumInSlot: int32, SmallSlot: bool, BigSlot: bool, ForceOrangeTextbox: bool):
        ExecuteUbergraph_Widget_CostSlotWrapper.K2Node_CustomEvent_IconTexture = IconTexture #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_CostSlotWrapper.K2Node_CustomEvent_ItemAmount = ItemAmount #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_CostSlotWrapper.K2Node_CustomEvent_CachedInventoryComponent = CachedInventoryComponent #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_CostSlotWrapper.K2Node_CustomEvent_SlotIdx = slotIdx #  PERSISTENT_FRAME(
        # Label 72
        ExecuteUbergraph_Widget_CostSlotWrapper.K2Node_CustomEvent_CurrentNumInSlot = CurrentNumInSlot #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_CostSlotWrapper.K2Node_CustomEvent_SmallSlot = SmallSlot #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_CostSlotWrapper.K2Node_CustomEvent_BigSlot = BigSlot #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_CostSlotWrapper.K2Node_CustomEvent_ForceOrangeTextbox = ForceOrangeTextbox #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_CostSlotWrapper(1529)
    

    def Tick(self):
        ExecuteUbergraph_Widget_CostSlotWrapper.K2Node_Event_MyGeometry1 = MyGeometry #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_CostSlotWrapper.K2Node_Event_InDeltaTime = InDeltaTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_CostSlotWrapper(10)
    

    def PreConstruct(self):
        ExecuteUbergraph_Widget_CostSlotWrapper.K2Node_Event_IsDesignTime = IsDesignTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_CostSlotWrapper(1733)
    

    def OnMouseEnter(self):
        ExecuteUbergraph_Widget_CostSlotWrapper.K2Node_Event_MyGeometry = MyGeometry #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_CostSlotWrapper.K2Node_Event_MouseEvent = MouseEvent #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_CostSlotWrapper(1784)
    

    def ExecuteUbergraph_Widget_CostSlotWrapper(self):
        if not self.mForceEmptyAnim:
            goto('L164')
        ReturnValue: bool = EqualEqual_IntInt(self.mCurrentNumInSlot, 0)
        if not ReturnValue:
            goto('L450')
        # Label 72
        ReturnValue_0: bool = self.Widget_InventorySlot.IsAnimationPlaying(self.Widget_InventorySlot.EmptySlot)
        if not ReturnValue_0:
            goto('L606')
        # End
        # Label 164
        ReturnValue_1: bool = Default__KismetSystemLibrary.IsValid(self.Widget_InventorySlot.mCachedInventoryComponent)
        if not ReturnValue_1:
            goto('L450')
        ReturnValue_2: bool = Default__KismetSystemLibrary.IsValidClass(self.itemDescriptor)
        if not ReturnValue_2:
            goto('L450')
        ReturnValue_3: int32 = self.Widget_InventorySlot.mCachedInventoryComponent.GetNumItems(self.itemDescriptor)
        ReturnValue1: bool = EqualEqual_IntInt(ReturnValue_3, 0)
        if not ReturnValue1:
            goto('L450')
        goto('L72')
        # Label 450
        self.Widget_InventorySlot.StopAnimation(self.Widget_InventorySlot.EmptySlot)
        self.Widget_InventorySlot.mItemImage.SetColorAndOpacity(LinearColor(R = 1, G = 1, B = 1, A = 1))
        # End
        # Label 606
        ReturnValue_4: Ptr[UMGSequencePlayer] = self.Widget_InventorySlot.PlayAnimation(self.Widget_InventorySlot.EmptySlot, 0, 0, 0, 1)
        # End
        # Label 701
        self.Widget_InventorySlot.OnItemClassUpdated()
        # End
        # Label 742
        ReturnValue_5: Ptr[Texture2D] = Default__FGItemDescriptor.GetBigIcon(self.Widget_InventorySlot.mFilterItemDescriptor)
        self.mIconBrush = ReturnValue_5
        self.Widget_InventorySlot.mCostSlotBrush = self.mIconBrush
        # Label 875
        self.Widget_InventorySlot.mIsCostSlot = True
        self.mCost = ItemAmount.amount
        ReturnValue1_0: bool = Default__KismetSystemLibrary.IsValid(CachedInventoryComponent)
        if not ReturnValue1_0:
            goto('L1104')
        self.Widget_InventorySlot.mCachedInventoryComponent = CachedInventoryComponent
        self.Widget_InventorySlot.mSlotIdx = SlotIdx
        goto('L701')
        # Label 1104
        self.mCurrentNumInSlot = CurrentNumInSlot
        goto('L701')
        # Label 1136
        ReturnValue_6: Ptr[Texture2D] = Default__FGItemDescriptor.GetSmallIcon(self.Widget_InventorySlot.mFilterItemDescriptor)
        self.mIconBrush = ReturnValue_6
        self.Widget_InventorySlot.mCostSlotBrush = self.mIconBrush
        goto('L875')
        # Label 1274
        self.itemDescriptor = self.Widget_InventorySlot.mFilterItemDescriptor
        ReturnValue_7: bool = BooleanOR(self.mBigSlot, BigSlot)
        if not ReturnValue_7:
            goto('L1136')
        goto('L742')
        # Label 1372
        ReturnValue1_1: bool = Default__KismetSystemLibrary.IsValidClass(self.Widget_InventorySlot.mFilterItemDescriptor)
        if not ReturnValue1_1:
            goto('L1464')
        goto('L1274')
        # Label 1464
        self.mIconBrush = IconTexture
        self.Widget_InventorySlot.mCostSlotBrush = self.mIconBrush
        goto('L875')
        self.mForceOrangeTextbox = ForceOrangeTextbox
        ReturnValue_7 = BooleanOR(self.mBigSlot, BigSlot)
        ReturnValue1_2: bool = BooleanOR(self.mSmallSlot, SmallSlot)
        self.Widget_InventorySlot.SetSlotSize(ReturnValue1_2, ReturnValue_7)
        self.Widget_InventorySlot.mFilterItemDescriptor = ItemAmount.ItemClass
        goto('L1372')
        self.Widget_InventorySlot.SetSlotSize(self.mSmallSlot, False)
        # End
    
