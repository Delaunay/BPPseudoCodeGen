
from codegen.ue4_stub import *

from Script.AIModule import GetBlackboardValueAsActor
from Script.Engine import EqualEqual_ClassClass
from Script.FactoryGame import BreakInventoryStack
from Script.FactoryGame import Default__FGInventoryLibrary
from Script.FactoryGame import FGCreature
from Script.AIModule import Default__BTFunctionLibrary
from Game.FactoryGame.Character.Creature.Wildlife.SpaceRabbit.AI.BTT_EatItem import ExecuteUbergraph_BTT_EatItem
from Script.AIModule import FinishExecute
from Script.FactoryGame import GetPickupItems
from Script.AIModule import BlackboardKeySelector
from Script.FactoryGame import FGItemPickup_Spawnable
from Script.AIModule import BTTask_BlueprintBase
from Script.FactoryGame import PickupByAmount
from Game.FactoryGame.Character.Creature.Wildlife.SpaceRabbit.AI.BTT_EatItem import ExecuteUbergraph_BTT_EatItem.K2Node_Event_OwnerController
from Script.Engine import Actor
from Script.FactoryGame import FGItemDescriptor
from Script.FactoryGame import BreakInventoryItem
from Game.FactoryGame.Character.Creature.Wildlife.SpaceRabbit.AI.BTT_EatItem import ExecuteUbergraph_BTT_EatItem.K2Node_Event_ControlledPawn
from Script.FactoryGame import InventoryStack

class BTT_EatItem(BTTask_BlueprintBase):
    mTargetItemBBKey: BlackboardKeySelector
    mDesiredItemClass: TSubclassOf[FGItemDescriptor]
    mAmountToPickup: int32
    mCreature: Ptr[FGCreature]
    
    def ReceiveExecuteAI(self):
        ExecuteUbergraph_BTT_EatItem.K2Node_Event_OwnerController = OwnerController #  PERSISTENT_FRAME(
        ExecuteUbergraph_BTT_EatItem.K2Node_Event_ControlledPawn = ControlledPawn #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BTT_EatItem(10)
    

    def ExecuteUbergraph_BTT_EatItem(self):
        AsFGCreature: Ptr[FGCreature] = Cast[FGCreature](ControlledPawn)
        bSuccess: bool = AsFGCreature
        if not bSuccess:
            goto('L721')
        self.mCreature = AsFGCreature
        
        ReturnValue: Ptr[Actor] = Default__BTFunctionLibrary.GetBlackboardValueAsActor(self, Ref[self.mTargetItemBBKey])
        Spawnable: Ptr[FGItemPickup_Spawnable] = Cast[FGItemPickup_Spawnable](ReturnValue)
        bSuccess1: bool = Spawnable
        if not bSuccess1:
            goto('L737')
        ReturnValue_0: InventoryStack = Spawnable.GetPickupItems()
        
        numItems = None
        item = None
        Default__FGInventoryLibrary.BreakInventoryStack(Ref[ReturnValue_0], Ref[numItems], Ref[item])
        
        item = None
        itemClass = None
        itemState = None
        Default__FGInventoryLibrary.BreakInventoryItem(Ref[item], Ref[itemClass], Ref[itemState])
        ReturnValue_1: bool = EqualEqual_ClassClass(self.mDesiredItemClass, itemClass)
        if not ReturnValue_1:
            goto('L753')
        
        ReturnValue1: Ptr[Actor] = Default__BTFunctionLibrary.GetBlackboardValueAsActor(self, Ref[self.mTargetItemBBKey])
        Spawnable1: Ptr[FGItemPickup_Spawnable] = Cast[FGItemPickup_Spawnable](ReturnValue1)
        bSuccess2: bool = Spawnable1
        if not bSuccess2:
            goto('L764')
        ReturnValue_2: bool = Spawnable1.PickupByAmount(1)
        if not ReturnValue_2:
            goto('L753')
        self.mCreature.Multicast_ConsumeItem(self.mDesiredItemClass, self.mAmountToPickup)
        self.FinishExecute(True)
        # End
        # Label 721
        self.FinishExecute(False)
        # End
        # Label 737
        self.FinishExecute(False)
        # End
        # Label 753
        self.FinishExecute(False)
    
