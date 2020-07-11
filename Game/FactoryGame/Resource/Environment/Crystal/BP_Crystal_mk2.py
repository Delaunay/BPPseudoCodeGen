
from codegen.ue4_stub import *

from Game.FactoryGame.Resource.Environment.Crystal.BP_Crystal import BP_Crystal

class BP_Crystal_mk2(BP_Crystal):
    mPickupItems = Namespace(Item={'ItemClass': '/Game/FactoryGame/Resource/Environment/Crystal/Desc_Crystal_mk2.Desc_Crystal_mk2_C', 'ItemState': {'ActorPtr': {'$Empty': True}}}, NumItems=1)
    mDestroyOnPickup = True
    mRespawnTimeIndays = -1
    mUpdatedOnDayNr = -1
    mItemState = EItemState::ES_NORMAL
    mGrowTimeInDays = 3
    mSavedNumItems = -1
    mMaxRespawns = -1
    bReplicates = True
    
