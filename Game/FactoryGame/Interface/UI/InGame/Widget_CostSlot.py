
from codegen.ue4_stub import *

from Script.UMG import GetParent
from Script.Engine import Texture2D
from Script.Engine import Pawn
from Script.UMG import GetChildIndex
from Script.UMG import GetChildrenCount
from Game.FactoryGame.Interface.UI.InGame.Widget_CostSlot import ExecuteUbergraph_Widget_CostSlot.K2Node_Event_MyGeometry
from Script.Engine import Default__KismetSystemLibrary
from Game.FactoryGame.Interface.UI.InGame.Widget_CostSlot import ExecuteUbergraph_Widget_CostSlot.K2Node_Event_InDeltaTime
from Script.FactoryGame import GetItemName
from Script.UMG import ESlateVisibility
from Script.FactoryGame import FGInventoryComponent
from Script.Engine import EqualEqual_IntInt
from Script.FactoryGame import GetSmallIcon
from Game.FactoryGame.Interface.UI.InGame.Widget_CostSlot import ExecuteUbergraph_Widget_CostSlot.K2Node_CustomEvent_SlotIdx
from Script.UMG import PanelWidget
from Game.FactoryGame.Interface.UI.InGame.Widget_CostSlot import ExecuteUbergraph_Widget_CostSlot
from Script.UMG import WidgetAnimation
from Script.UMG import UserWidget
from Script.UMG import GetOwningPlayerPawn
from Game.FactoryGame.Interface.UI.HUDHelpers.HUDHelpers import Default__HUDHelpers
from Script.FactoryGame import Default__FGItemDescriptor
from Script.FactoryGame import ItemAmount
from Script.Engine import IsValidClass

class Widget_CostSlot(UserWidget):
    EmptySlot: Ptr[WidgetAnimation]
    mCost: ItemAmount
    isPlayerInventory: bool
    mCachedInventory: Ptr[FGInventoryComponent]
    
    def GetDividerTopVisibility(self):
        ReturnValue: Ptr[PanelWidget] = self.GetParent()
        ReturnValue_0: int32 = ReturnValue.GetChildIndex(self)
        ReturnValue_1: int32 = ReturnValue.GetChildrenCount()
        ReturnValue_2: bool = EqualEqual_IntInt(ReturnValue_0, 0)
        ReturnValue_3: bool = ReturnValue_1 <= 4
        ReturnValue_4: bool = ReturnValue_3 and ReturnValue_2
        if not ReturnValue_4:
            goto('L266')
        ReturnValue_5: uint8 = 0
        goto('L286')
        # Label 266
        ReturnValue_5 = 1
    

    def GetItemName(self):
        ReturnValue: FText = Default__FGItemDescriptor.GetItemName(self.mCost.ItemClass)
        ReturnValue_0: FText = ReturnValue
    

    def SetCostSlot(self, slotIdx: int32):
        ExecuteUbergraph_Widget_CostSlot.K2Node_CustomEvent_SlotIdx = slotIdx #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_CostSlot(10)
    

    def Tick(self):
        ExecuteUbergraph_Widget_CostSlot.K2Node_Event_MyGeometry = MyGeometry #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_CostSlot.K2Node_Event_InDeltaTime = InDeltaTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_CostSlot(252)
    

    def ExecuteUbergraph_Widget_CostSlot(self):
        ReturnValue: Ptr[Texture2D] = Default__FGItemDescriptor.GetSmallIcon(self.mCost.ItemClass)
        ReturnValue2: Ptr[Pawn] = self.GetOwningPlayerPawn()
        
        numItems2 = None
        Default__HUDHelpers.GetNumItemsFromPlayerInventory(ReturnValue2, self.mCost.ItemClass, self, Ref[numItems2])
        self.Widget_CostSlotWrapper.Setup CostIcon(ReturnValue, self.mCost, self.mCachedInventory, SlotIdx, numItems2, False, False, False)
        # End
        ReturnValue_0: bool = Default__KismetSystemLibrary.IsValidClass(self.mCost.ItemClass)
        if not ReturnValue_0:
            goto('L635')
        ReturnValue_1: Ptr[Pawn] = self.GetOwningPlayerPawn()
        
        numItems = None
        Default__HUDHelpers.GetNumItemsFromPlayerInventory(ReturnValue_1, self.mCost.ItemClass, self, Ref[numItems])
        ReturnValue_2: bool = self.Widget_CostSlotWrapper.mCurrentNumInSlot != numItems
        if not ReturnValue_2:
            goto('L635')
        ReturnValue1: Ptr[Pawn] = self.GetOwningPlayerPawn()
        
        numItems1 = None
        Default__HUDHelpers.GetNumItemsFromPlayerInventory(ReturnValue1, self.mCost.ItemClass, self, Ref[numItems1])
        self.Widget_CostSlotWrapper.mCurrentNumInSlot = numItems1
    
