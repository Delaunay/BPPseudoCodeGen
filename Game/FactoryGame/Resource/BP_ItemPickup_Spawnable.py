
from codegen.ue4_stub import *

from Script.AkAudio import AkAudioEvent
from Script.Engine import ParticleSystemComponent
from Script.AkAudio import PostAkEvent
from Script.Engine import K2_GetActorLocation
from Script.Engine import Default__GameplayStatics
from Game.FactoryGame.-Shared.Particle.Particle.ResourceDropPing import ResourceDropPing
from Script.CoreUObject import Vector
from Game.FactoryGame.Resource.BP_ItemPickup_Spawnable import ExecuteUbergraph_BP_ItemPickup_Spawnable
from Script.Engine import SpawnEmitterAtLocation
from Script.FactoryGame import PlayPickupEffect
from Script.FactoryGame import FGItemPickup_Spawnable
from Script.AkAudio import AkComponent
from Script.AkAudio import Default__AkGameplayStatics

class BP_ItemPickup_Spawnable(FGItemPickup_Spawnable):
    mPickupEvent: Ptr[AkAudioEvent] = Namespace(AssetPath='/Game/FactoryGame/Character/Player/Audio/SB_CharacterEssentials/Play_P_ResourcePickUp.Play_P_ResourcePickUp')
    mMeshComponent = Namespace(Mobility=1, ObjectClass='/Script/Engine.StaticMeshComponent', ObjectFlags=2883617, ObjectName='Mesh')
    mDestroyOnPickup = True
    mRespawnTimeIndays = -1
    mUpdatedOnDayNr = -1
    mItemState = EItemState::ES_NORMAL
    mGrowTimeInDays = 3
    mSavedNumItems = -1
    mMaxRespawns = -1
    bReplicates = True
    RemoteRole = 1
    RootComponent = Namespace(Mobility=1, ObjectClass='/Script/Engine.StaticMeshComponent', ObjectFlags=2883617, ObjectName='Mesh')
    
    def PlayPickupEffect(self):
        self.ExecuteUbergraph_BP_ItemPickup_Spawnable(78)
    

    def PlaySpawnEffect(self):
        self.ExecuteUbergraph_BP_ItemPickup_Spawnable(83)
    

    def ExecuteUbergraph_BP_ItemPickup_Spawnable(self):
        # Label 10
        self.PlayPickupEffect()
        ReturnValue: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(self.mPickupEvent, self, True)
        # End
        goto('L10')
        ReturnValue_0: Vector = self.K2_GetActorLocation()
        ReturnValue_1: Ptr[ParticleSystemComponent] = Default__GameplayStatics.SpawnEmitterAtLocation(self, ResourceDropPing, ReturnValue_0, Rotator::FromPitchYawRoll(0, 0, 0), Vector(1, 1, 1), True, 0)
    
