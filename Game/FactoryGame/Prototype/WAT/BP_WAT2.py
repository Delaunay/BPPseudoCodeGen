
from codegen.ue4_stub import *

from Game.FactoryGame.Prototype.WAT.BP_WAT1 import BP_WAT1

class BP_WAT2(BP_WAT1):
    mTimeToPickUp = 3
    mPickupItems = Namespace(Item={'ItemClass': '/Game/FactoryGame/Prototype/WAT/Desc_WAT2.Desc_WAT2_C', 'ItemState': {'ActorPtr': {'$Empty': True}}}, NumItems=1)
    mDestroyOnPickup = True
    mRespawnTimeIndays = -1
    mUpdatedOnDayNr = -1
    mItemState = EItemState::ES_NORMAL
    mGrowTimeInDays = 3
    mSavedNumItems = -1
    mMaxRespawns = -1
    bReplicates = True
    
