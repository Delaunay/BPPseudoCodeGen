
from codegen.ue4_stub import *

from Game.FactoryGame.Resource.BP_Pickup import BP_Pickup

class BP_AlphaHogParts(BP_Pickup):
    mPickupItems = Namespace(Item={'ItemClass': '/Game/FactoryGame/Resource/Parts/AnimalParts/Desc_HogParts.Desc_HogParts_C', 'ItemState': {'ActorPtr': {'$Empty': True}}}, NumItems=3)
    mDestroyOnPickup = True
    mRespawnTimeIndays = -1
    mUpdatedOnDayNr = -1
    mItemState = EItemState::ES_NORMAL
    mGrowTimeInDays = 3
    mSavedNumItems = -1
    mMaxRespawns = -1
    bReplicates = True
    RemoteRole = 1
    
