
from codegen.ue4_stub import *

from Game.FactoryGame.Resource.BP_Pickup import ReceiveBeginPlay
from Game.FactoryGame.Resource.Environment.AnimalParts.BP_HogParts import BP_HogParts
from Script.Engine import HasAuthority
from Script.Engine import UserConstructionScript
from Script.Engine import K2_AddActorWorldOffset
from Game.FactoryGame.Resource.Environment.AnimalParts.BP_CrabEggParts import ExecuteUbergraph_BP_CrabEggParts

class BP_CrabEggParts(BP_HogParts):
    mDestroyOnPickup = True
    mRespawnTimeIndays = -1
    mUpdatedOnDayNr = -1
    mItemState = EItemState::ES_NORMAL
    mGrowTimeInDays = 3
    mSavedNumItems = -1
    mMaxRespawns = -1
    bReplicates = True
    
    def UserConstructionScript(self):
        self.UserConstructionScript()
        # Label 10
        ReturnValue: bool = self.HasAuthority()
        if not ReturnValue:
            goto('L78')
        
        SweepHitResult = None
        self.K2_AddActorWorldOffset(Vector(0, 0, -133), False, False, Ref[SweepHitResult])
    

    def ReceiveBeginPlay(self):
        self.ExecuteUbergraph_BP_CrabEggParts(25)
    

    def ExecuteUbergraph_BP_CrabEggParts(self):
        # Label 10
        self.ReceiveBeginPlay()
        # End
        goto('L10')
    
