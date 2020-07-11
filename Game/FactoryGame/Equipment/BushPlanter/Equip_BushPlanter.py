
from codegen.ue4_stub import *

from Game.FactoryGame.Equipment.Decoration.Equip_Decoration import Equip_Decoration
from Game.FactoryGame.Equipment.BushPlanter.Equip_BushPlanter import ExecuteUbergraph_Equip_BushPlanter.K2Node_Event_inActor
from Script.FactoryGame import PlantPickup
from Script.FactoryGame import FGItemPickup
from Game.FactoryGame.Equipment.BushPlanter.Equip_BushPlanter import ExecuteUbergraph_Equip_BushPlanter

class Equip_BushPlanter(Equip_Decoration):
    mPlaceDistanceMax = 1000
    mArmAnimation = EArmEquipment::AE_Generic1Hand
    PrimaryActorTick = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=False, bTickEvenWhenPaused=False)
    bOnlyRelevantToOwner = True
    bNetUseOwnerRelevancy = True
    bReplicates = True
    RemoteRole = 1
    
    def SetupActor(self):
        ExecuteUbergraph_Equip_BushPlanter.K2Node_Event_inActor = InActor #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Equip_BushPlanter(10)
    

    def ExecuteUbergraph_Equip_BushPlanter(self):
        Pickup: Ptr[FGItemPickup] = Cast[FGItemPickup](inActor)
        bSuccess: bool = Pickup
        if not bSuccess:
            goto('L121')
        Pickup.PlantPickup()
    
