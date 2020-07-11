
from codegen.ue4_stub import *

from Script.Engine import Pawn
from Script.Engine import Default__KismetSystemLibrary
from Script.FactoryGame import Get
from Script.Engine import PlayerController
from Script.Engine import Default__KismetArrayLibrary
from Script.UMG import SetHorizontalAlignment
from Game.FactoryGame.Interface.UI.InGame.Widget_CostSlotWrapper import Widget_CostSlotWrapper
from Script.UMG import Default__WidgetBlueprintLibrary
from Script.UMG import AddChildToWrapBox
from Script.Engine import BooleanOR
from Script.FactoryGame import FGSchematic
from Script.UMG import WrapBoxSlot
from Script.UMG import UserWidget
from Script.UMG import GetOwningPlayerPawn
from Script.FactoryGame import IsSchematicPurchased
from Game.FactoryGame.Buildable.Factory.TradingPost.Build_TradingPost import Build_TradingPost
from Game.FactoryGame.Interface.UI.HUDHelpers.HUDHelpers import Default__HUDHelpers
from Script.FactoryGame import FGSchematicManager
from Script.UMG import Create
from Script.FactoryGame import ItemAmount
from Script.UMG import SetRenderOpacity
from Game.FactoryGame.-Shared.Blueprint.BP_SchematicHelper import Default__BP_SchematicHelper
from Script.Engine import IsValidClass
from Script.FactoryGame import Default__FGSchematicManager
from Script.FactoryGame import GetRemainingCostFor

class Widget_TradingPostSchematicCostInfo(UserWidget):
    mTradingPost: Ptr[Build_TradingPost]
    mSchematic: TSubclassOf[FGSchematic]
    mSchematicManager: Ptr[FGSchematicManager]
    AllCostSlots: List[Ptr[Widget_CostSlotWrapper]]
    padding = Namespace(Bottom=4, Left=4, Right=4, Top=4)
    
    def UpdateSchematicCosts(self, mSchematic: TSubclassOf[FGSchematic]):
        ExecutionFlow.Push("L2180")
        ReturnValue: bool = Default__KismetSystemLibrary.IsValidClass(mSchematic)
        if not ReturnValue:
           goto(ExecutionFlow.Pop())
        self.mCostGrid.ClearChildren()
        Variable: int32 = 0
        Variable_0: int32 = 0
        # Label 148
        ReturnValue1: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue1_0: Ptr[FGSchematicManager] = Default__FGSchematicManager.Get(ReturnValue1)
        ReturnValue_0: List[ItemAmount] = ReturnValue1_0.GetRemainingCostFor(mSchematic)
        
        ReturnValue_1: int32 = len(ReturnValue_0)
        ReturnValue_2: bool = Variable <= ReturnValue_1
        if not ReturnValue_2:
           goto(ExecutionFlow.Pop())
        Variable_0 = Variable
        ExecutionFlow.Push("L2106")
        ReturnValue1 = self.GetOwningPlayer()
        ReturnValue1_0 = Default__FGSchematicManager.Get(ReturnValue1)
        ReturnValue_0 = ReturnValue1_0.GetRemainingCostFor(mSchematic)
        
        Item = None
        Item = ReturnValue_0[Variable_0]
        ReturnValue1_1: bool = Default__KismetSystemLibrary.IsValidClass(Item.ItemClass)
        if not ReturnValue1_1:
           goto(ExecutionFlow.Pop())
        ReturnValue2: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_3: Ptr[Widget_CostSlotWrapper] = Default__WidgetBlueprintLibrary.Create(self, Widget_CostSlotWrapper, ReturnValue2)
        ReturnValue_3.mCostSlotContainer.SetRenderOpacity(0)
        ReturnValue_4: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_5: Ptr[FGSchematicManager] = Default__FGSchematicManager.Get(ReturnValue_4)
        
        IsLocked = None
        Default__BP_SchematicHelper.IsSchematicLockedInAnyWay(ReturnValue_4, mSchematic, self, Ref[IsLocked])
        ReturnValue_6: bool = ReturnValue_5.IsSchematicPurchased(mSchematic)
        ReturnValue_7: bool = BooleanOR(IsLocked, ReturnValue_6)
        Variable_1: int32 = 0
        Variable_2: bool = ReturnValue_7
        ReturnValue1 = self.GetOwningPlayer()
        ReturnValue1_0 = Default__FGSchematicManager.Get(ReturnValue1)
        ReturnValue_8: Ptr[Pawn] = self.GetOwningPlayerPawn()
        ReturnValue_0 = ReturnValue1_0.GetRemainingCostFor(mSchematic)
        
        Item = None
        Item = ReturnValue_0[Variable_0]
        ItemAmount.ItemClass = Item.ItemClass
        ItemAmount.amount = Item.amount
        
        numItems = None
        Default__HUDHelpers.GetNumItemsFromPlayerInventory(ReturnValue_8, Item.ItemClass, self, Ref[numItems])
        
        switch = {
            False: numItems,
            True: Variable_1
        }
        ReturnValue_3.Setup CostIcon(None, ItemAmount, None, 0, switch.get(Variable_2, None), False, False, False)
        ReturnValue_4 = self.GetOwningPlayer()
        ReturnValue_5 = Default__FGSchematicManager.Get(ReturnValue_4)
        
        IsLocked = None
        Default__BP_SchematicHelper.IsSchematicLockedInAnyWay(ReturnValue_4, mSchematic, self, Ref[IsLocked])
        ReturnValue_6 = ReturnValue_5.IsSchematicPurchased(mSchematic)
        ReturnValue_7 = BooleanOR(IsLocked, ReturnValue_6)
        Variable_3: float = 1
        Variable1: float = 0.5
        Variable1_0: bool = ReturnValue_7
        
        switch_0 = {
            False: Variable_3,
            True: Variable1
        }
        self.mCostGrid.SetRenderOpacity(switch_0.get(Variable1_0, None))
        ReturnValue_9: Ptr[WrapBoxSlot] = self.mCostGrid.AddChildToWrapBox(ReturnValue_3)
        ReturnValue_9.SetHorizontalAlignment(1)
        
        Variable_4 = None
        ReturnValue_10: int32 = self.AllCostSlots.append(Variable_4)
        goto(ExecutionFlow.Pop())
        # Label 2106
        ReturnValue_11: int32 = Variable + 1
        Variable = ReturnValue_11
        goto('L148')
    
