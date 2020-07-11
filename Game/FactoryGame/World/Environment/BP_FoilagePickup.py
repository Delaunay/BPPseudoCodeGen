
from codegen.ue4_stub import *

from Script.Engine import Default__KismetSystemLibrary
from Script.FactoryGame import FGFoliagePickup
from Script.Engine import ParticleSystemComponent
from Script.Engine import Default__GameplayStatics
from Game.FactoryGame.World.Environment.BP_FoilagePickup import ExecuteUbergraph_BP_FoilagePickup.K2Node_Event_atLocation
from Script.AkAudio import PostAkEventAtLocation
from Script.Engine import SpawnEmitterAtLocation
from Script.Engine import IsValid
from Game.FactoryGame.World.Environment.BP_FoilagePickup import ExecuteUbergraph_BP_FoilagePickup
from Script.AkAudio import AkComponent
from Script.AkAudio import Default__AkGameplayStatics
from Game.FactoryGame.World.Environment.BP_FoilagePickup import ExecuteUbergraph_BP_FoilagePickup.K2Node_Event_foliageUserData

class BP_FoilagePickup(FGFoliagePickup):
    bHidden = True
    bOnlyRelevantToOwner = True
    bNetUseOwnerRelevancy = True
    bReplicates = True
    RemoteRole = 1
    
    def PlayPickupEffect(self):
        ExecuteUbergraph_BP_FoilagePickup.K2Node_Event_foliageUserData = foliageUserData #  PERSISTENT_FRAME(
        ExecuteUbergraph_BP_FoilagePickup.K2Node_Event_atLocation = atLocation #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_FoilagePickup(10)
    

    def ExecuteUbergraph_BP_FoilagePickup(self):
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(foliageUserData.mPickupEffect)
        if not ReturnValue:
            goto('L392')
        ReturnValue_0: Ptr[ParticleSystemComponent] = Default__GameplayStatics.SpawnEmitterAtLocation(self, foliageUserData.mPickupEffect, atLocation, Rotator::FromPitchYawRoll(0, 0, 0), Vector(1, 1, 1), True, 0)
        ReturnValue1: bool = Default__KismetSystemLibrary.IsValid(foliageUserData.mPickupEvent)
        if not ReturnValue1:
            goto('L392')
        ReturnValue_1: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEventAtLocation(self, foliageUserData.mPickupEvent, atLocation, Rotator::FromPitchYawRoll(0, 0, 0))
    
