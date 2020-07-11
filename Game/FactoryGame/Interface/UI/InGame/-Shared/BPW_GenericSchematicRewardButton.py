
from codegen.ue4_stub import *

from Script.FactoryGame import FGResourceDescriptor
from Script.UMG import CanvasPanelSlot
from Script.FactoryGame import FGUnlockInventorySlot
from Script.FactoryGame import GetItemsToGive
from Script.UMG import Default__WidgetLayoutLibrary
from Script.UMG import SlotAsCanvasSlot
from Script.FactoryGame import GetRecipesToUnlock
from Script.Engine import Default__KismetSystemLibrary
from Script.FactoryGame import GetProducts
from Script.Engine import PlayerController
from Script.Engine import SetStructurePropertyByName
from Script.Engine import Default__KismetArrayLibrary
from Script.FactoryGame import FGUnlockArmEquipmentSlot
from Script.UMG import Unhandled
from Script.FactoryGame import FGUnlockRecipe
from Game.FactoryGame.Interface.UI.InGame.Widget_Tooltip import Widget_Tooltip
from Script.UMG import Open
from Script.UMG import Default__WidgetBlueprintLibrary
from Script.FactoryGame import FGUnlockScannableResource
from Script.FactoryGame import GetResourcesToAddToScanner
from Script.FactoryGame import FGUnlockMap
from Script.UMG import Default__SlateBlueprintLibrary
from Script.UMG import Widget
from Script.FactoryGame import Default__FGRecipe
from Game.FactoryGame.Unlocks.FUnlockDataStruct import FUnlockDataStruct
from Script.UMG import Close
from Script.UMG import UserWidget
from Script.FactoryGame import FGUnlockGiveItem
from Script.Engine import Subtract_Vector2DVector2D
from Script.FactoryGame import FGUnlockBuildEfficiency
from Script.UMG import Create
from Script.UMG import GetMousePositionOnViewport
from Script.FactoryGame import FGItemDescriptor
from Script.CoreUObject import Vector2D
from Script.FactoryGame import FGRecipe
from Script.UMG import SetPosition
from Script.FactoryGame import ItemAmount
from Game.FactoryGame.Interface.UI.InGame.-Shared.BPW_GenericSchematicRewardButton import ExecuteUbergraph_BPW_GenericSchematicRewardButton
from Script.UMG import LocalToViewport
from Script.Engine import IsValidClass
from Script.Engine import Add_Vector2DVector2D
from Script.Engine import PrintString
from Script.UMG import EventReply
from Script.CoreUObject import LinearColor

class BPW_GenericSchematicRewardButton(UserWidget):
    mUnlockData: FUnlockDataStruct
    mItemDescriptor: TSubclassOf[FGItemDescriptor]
    mShouldAlwaysAutoScrollText: bool
    
    def OnMouseMove(self):
        ReturnValue: Vector2D = Default__WidgetLayoutLibrary.GetMousePositionOnViewport(self)
        
        PixelPosition = None
        ViewportPosition = None
        Default__SlateBlueprintLibrary.LocalToViewport(self, Vector2D(X = 0, Y = 0), Ref[MyGeometry], Ref[PixelPosition], Ref[ViewportPosition])
        ReturnValue_0: Ptr[CanvasPanelSlot] = Default__WidgetLayoutLibrary.SlotAsCanvasSlot(self.mToolTip)
        ReturnValue_1: Vector2D = Subtract_Vector2DVector2D(ReturnValue, ViewportPosition)
        ReturnValue_2: Vector2D = Add_Vector2DVector2D(ReturnValue_1, Vector2D(X = 15, Y = 15))
        ReturnValue_0.SetPosition(ReturnValue_2)
        ReturnValue_3: EventReply = Default__WidgetBlueprintLibrary.Unhandled()
        ReturnValue_4: EventReply = ReturnValue_3
    

    def GetTooltip(self):
        ReturnValue: bool = Default__KismetSystemLibrary.IsValidClass(self.mItemDescriptor)
        if not ReturnValue:
            goto('L378')
        ReturnValue_0: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_1: Ptr[Widget_Tooltip] = Default__WidgetBlueprintLibrary.Create(self, Widget_Tooltip, ReturnValue_0)
        ItemAmount.ItemClass = self.mItemDescriptor
        ItemAmount.amount = 0
        
        ItemAmount = None
        Default__KismetSystemLibrary.SetStructurePropertyByName(ReturnValue_1, "mItemDescriptor", Ref[ItemAmount])
        Default__KismetSystemLibrary.PrintString(self, "Hello", True, True, LinearColor(R = 0, G = 0.6600000262260437, B = 1, A = 1), 2)
        ReturnValue_2: Ptr[Widget] = ReturnValue_1
        goto('L389')
        # Label 378
        ReturnValue_2 = None
    

    def SetUnlockData(self, mUnlockStruct: FUnlockDataStruct):
        SlateBrush.ImageSize = self.mIconObject.Brush.ImageSize
        SlateBrush.Margin = self.mIconObject.Brush.Margin
        SlateBrush.TintColor = self.mIconObject.Brush.TintColor
        SlateBrush.ResourceObject = self.mUnlockData.UnlockIcon_9_3E3B124C41C68907A6EB9FAD36C04BC4
        SlateBrush.DrawAs = self.mIconObject.Brush.DrawAs
        SlateBrush.Tiling = self.mIconObject.Brush.Tiling
        SlateBrush.Mirroring = self.mIconObject.Brush.Mirroring
        
        SlateBrush = None
        self.mIconObject.SetBrush(Ref[SlateBrush])
        self.mTextObject.SetText(self.mUnlockData.UnlockName_2_490383D6421D4A92D86E1F835769488A)
        Recipe: Ptr[FGUnlockRecipe] = Cast[FGUnlockRecipe](self.mUnlockData.Unlock_29_06E6D017481991B0E94072A4F21FCC03)
        bSuccess6: bool = Recipe
        if not bSuccess6:
            goto('L892')
        ReturnValue: List[TSubclassOf[FGRecipe]] = Recipe.GetRecipesToUnlock()
        
        Item2 = None
        Item2 = ReturnValue[self.mUnlockData.UnlockStructIndex_34_716E881C402D058998F7CDA17E1E4BF2]
        ReturnValue_0: List[ItemAmount] = Default__FGRecipe.GetProducts(Item2, False)
        
        Item3 = None
        Item3 = ReturnValue_0[0]
        self.mItemDescriptor = Item3.ItemClass
        # End
        # Label 892
        Resource: Ptr[FGUnlockScannableResource] = Cast[FGUnlockScannableResource](self.mUnlockData.Unlock_29_06E6D017481991B0E94072A4F21FCC03)
        bSuccess5: bool = Resource
        if not bSuccess5:
            goto('L1122')
        ReturnValue_1: List[TSubclassOf[FGResourceDescriptor]] = Resource.GetResourcesToAddToScanner()
        
        Item1 = None
        Item1 = ReturnValue_1[self.mUnlockData.UnlockStructIndex_34_716E881C402D058998F7CDA17E1E4BF2]
        self.mItemDescriptor = Item1
        # End
        # Label 1122
        Slot: Ptr[FGUnlockInventorySlot] = Cast[FGUnlockInventorySlot](self.mUnlockData.Unlock_29_06E6D017481991B0E94072A4F21FCC03)
        bSuccess4: bool = Slot
        if not bSuccess4:
            goto('L1215')
        # End
        # Label 1215
        Item: Ptr[FGUnlockGiveItem] = Cast[FGUnlockGiveItem](self.mUnlockData.Unlock_29_06E6D017481991B0E94072A4F21FCC03)
        bSuccess3: bool = Item
        if not bSuccess3:
            goto('L1454')
        ReturnValue_2: List[ItemAmount] = Item.GetItemsToGive()
        
        Item_0 = None
        Item_0 = ReturnValue_2[self.mUnlockData.UnlockStructIndex_34_716E881C402D058998F7CDA17E1E4BF2]
        self.mItemDescriptor = Item_0.ItemClass
        # End
        # Label 1454
        Slot_0: Ptr[FGUnlockArmEquipmentSlot] = Cast[FGUnlockArmEquipmentSlot](self.mUnlockData.Unlock_29_06E6D017481991B0E94072A4F21FCC03)
        bSuccess2: bool = Slot_0
        if not bSuccess2:
            goto('L1547')
        # End
        # Label 1547
        Efficiency: Ptr[FGUnlockBuildEfficiency] = Cast[FGUnlockBuildEfficiency](self.mUnlockData.Unlock_29_06E6D017481991B0E94072A4F21FCC03)
        bSuccess1: bool = Efficiency
        if not bSuccess1:
            goto('L1640')
        # End
        # Label 1640
        Map: Ptr[FGUnlockMap] = Cast[FGUnlockMap](self.mUnlockData.Unlock_29_06E6D017481991B0E94072A4F21FCC03)
        bSuccess: bool = Map
        if not bSuccess:
            goto('L1728')
    

    def Construct(self):
        self.ExecuteUbergraph_BPW_GenericSchematicRewardButton(70)
    

    def BndEvt__mButton_K2Node_ComponentBoundEvent_0_OnButtonHoverEvent__DelegateSignature(self):
        self.ExecuteUbergraph_BPW_GenericSchematicRewardButton(98)
    

    def BndEvt__mButton_K2Node_ComponentBoundEvent_1_OnButtonHoverEvent__DelegateSignature(self):
        self.ExecuteUbergraph_BPW_GenericSchematicRewardButton(136)
    

    def ExecuteUbergraph_BPW_GenericSchematicRewardButton(self):
        # Label 10
        if not self.mShouldAlwaysAutoScrollText:
            goto('L168')
        self.Widget_AutoScrollingContainer.DelayedStartAutoScroll(0.5)
        # End
        self.SetUnlockData(self.mUnlockData)
        goto('L10')
        self.mToolTip.Open(False)
        # End
        self.mToolTip.Close()
    
