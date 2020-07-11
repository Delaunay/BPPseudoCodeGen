
from codegen.ue4_stub import *

from Game.FactoryGame.Resource.BP_Pickup import ReceiveBeginPlay
from Script.Engine import SetHiddenInGame
from Game.FactoryGame.Resource.BP_Pickup import PlayPickupEffect
from Script.FactoryGame import BreakInventoryStack
from Script.FactoryGame import IsPickedUp
from Script.FactoryGame import GetPickupItems
from Game.FactoryGame.Resource.BP_Pickup import BP_Pickup
from Game.FactoryGame.World.Benefit.BP_Edible import ExecuteUbergraph_BP_Edible
from Script.FactoryGame import UpdateVisuals
from Script.FactoryGame import Default__FGInventoryLibrary
from Script.FactoryGame import GetDestroyOnPickup
from Script.Engine import EqualEqual_IntInt
from Script.Engine import StaticMesh
from Script.FactoryGame import InventoryStack

class BP_Edible(BP_Pickup):
    mSeedMesh: Ptr[StaticMesh] = Namespace(AssetPath='/Game/FactoryGame/World/Benefit/NutBush/Mesh/Nut_01.Nut_01')
    mRespawnTimeIndays = -1
    mUpdatedOnDayNr = -1
    mItemState = EItemState::ES_NORMAL
    mGrowTimeInDays = 3
    mSavedNumItems = -1
    mMaxRespawns = -1
    bReplicates = True
    RemoteRole = 1
    
    def UpdateVisiblityState(self):
        ReturnValue: bool = self.IsPickedUp()
        self.StaticMesh.SetHiddenInGame(ReturnValue, False)
    

    def PlayPickupEffect(self):
        self.ExecuteUbergraph_BP_Edible(29)
    

    def UpdateVisuals(self):
        self.ExecuteUbergraph_BP_Edible(58)
    

    def ReceiveBeginPlay(self):
        self.ExecuteUbergraph_BP_Edible(295)
    

    def ExecuteUbergraph_BP_Edible(self):
        # Label 10
        self.UpdateVisiblityState()
        # End
        self.PlayPickupEffect()
        self.UpdateVisiblityState()
        # End
        self.UpdateVisuals()
        self.UpdateVisiblityState()
        ReturnValue: InventoryStack = self.GetPickupItems()
        
        numItems = None
        item = None
        Default__FGInventoryLibrary.BreakInventoryStack(Ref[ReturnValue], Ref[numItems], Ref[item])
        ReturnValue_0: bool = EqualEqual_IntInt(numItems, 0)
        ReturnValue_1: bool = self.GetDestroyOnPickup()
        ReturnValue_2: bool = ReturnValue_1 and ReturnValue_0
        if not ReturnValue_2:
            goto('L310')
        self.SetActorHiddenInGame(True)
        # End
        self.ReceiveBeginPlay()
        goto('L10')
    
