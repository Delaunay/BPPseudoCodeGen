
from codegen.ue4_stub import *

from Game.FactoryGame.Equipment.Rifle.Equip_Rifle import Equip_Rifle

class Equip_Rifle_Mk2(Equip_Rifle):
    mInstantHitDamage = 14
    mMagSize = 6
    mAttachmentClass = NewObject[Attach_Rifle_Mk2]()
    mEquipmentSlot = EEquipmentSlot::ES_ARMS
    PrimaryActorTick = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=False, bTickEvenWhenPaused=False)
    bOnlyRelevantToOwner = True
    bNetUseOwnerRelevancy = True
    bReplicates = True
    RemoteRole = 1
    
