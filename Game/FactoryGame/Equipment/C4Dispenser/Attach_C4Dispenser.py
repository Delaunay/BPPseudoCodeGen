
from codegen.ue4_stub import *

from Script.FactoryGame import FGWeaponAttachment

class Attach_C4Dispenser(FGWeaponAttachment):
    mAttachSocket = equipmentSocket
    mArmAnimation = EArmEquipment::AE_Nobelisk
    PrimaryActorTick = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=False, bTickEvenWhenPaused=False)
    bNetUseOwnerRelevancy = True
    bReplicates = True
    RemoteRole = 1
    
