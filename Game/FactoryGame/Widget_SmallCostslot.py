
from codegen.ue4_stub import *

from Script.Engine import Default__KismetSystemLibrary
from Script.UMG import GetOwningPlayerPawn
from Game.FactoryGame.Interface.UI.HUDHelpers.HUDHelpers import Default__HUDHelpers
from Game.FactoryGame.Widget_SmallCostslot import ExecuteUbergraph_Widget_SmallCostSlot
from Script.Engine import Pawn
from Script.FactoryGame import ItemAmount
from Game.FactoryGame.Widget_SmallCostslot import ExecuteUbergraph_Widget_SmallCostSlot.K2Node_Event_MyGeometry
from Script.Engine import IsValidClass
from Game.FactoryGame.Widget_SmallCostslot import ExecuteUbergraph_Widget_SmallCostSlot.K2Node_Event_InDeltaTime
from Script.UMG import UserWidget

class Widget_SmallCostSlot(UserWidget):
    mCost: ItemAmount
    
    def Tick(self):
        ExecuteUbergraph_Widget_SmallCostSlot.K2Node_Event_MyGeometry = MyGeometry #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_SmallCostSlot.K2Node_Event_InDeltaTime = InDeltaTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_SmallCostSlot(10)
    

    def ExecuteUbergraph_Widget_SmallCostSlot(self):
        ReturnValue: bool = Default__KismetSystemLibrary.IsValidClass(self.mCost.ItemClass)
        if not ReturnValue:
            goto('L393')
        ReturnValue1: Ptr[Pawn] = self.GetOwningPlayerPawn()
        
        numItems1 = None
        Default__HUDHelpers.GetNumItemsFromPlayerInventory(ReturnValue1, self.mCost.ItemClass, self, Ref[numItems1])
        ReturnValue_0: bool = self.Widget_CostSlotWrapper.mCurrentNumInSlot != numItems1
        if not ReturnValue_0:
            goto('L393')
        ReturnValue_1: Ptr[Pawn] = self.GetOwningPlayerPawn()
        
        numItems = None
        Default__HUDHelpers.GetNumItemsFromPlayerInventory(ReturnValue_1, self.mCost.ItemClass, self, Ref[numItems])
        self.Widget_CostSlotWrapper.mCurrentNumInSlot = numItems
    
