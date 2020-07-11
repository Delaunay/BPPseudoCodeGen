
from codegen.ue4_stub import *

from Game.FactoryGame.Resource.BP_Pickup import BP_Pickup

class BP_Crystal(BP_Pickup):
    mPickupEvent = Namespace(AssetPath='/Game/FactoryGame/Resource/Environment/Crystal/Audio/Play_Pickup_Slugs.Play_Pickup_Slugs')
    mDesiredGainSignificanceDistance = 16000
    mAddToSignificanceManager = True
    mTimeToPickUp = 3
    mPickupItems = Namespace(Item={'ItemClass': '/Game/FactoryGame/Resource/Environment/Crystal/Desc_Crystal.Desc_Crystal_C', 'ItemState': {'ActorPtr': {'$Empty': True}}}, NumItems=1)
    mDestroyOnPickup = True
    mAudioEvent = Namespace(AssetPath='/Game/FactoryGame/World/Environment/Audio/Play_W_Crystal_Shimmer.Play_W_Crystal_Shimmer')
    mRespawnTimeIndays = -1
    mUpdatedOnDayNr = -1
    mItemState = EItemState::ES_NORMAL
    mGrowTimeInDays = 3
    mSavedNumItems = -1
    mMaxRespawns = -1
    bReplicates = True
    RemoteRole = 1
    
