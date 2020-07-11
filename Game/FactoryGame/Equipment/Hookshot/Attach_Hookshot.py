
from codegen.ue4_stub import *

from Script.FactoryGame import FGEquipmentAttachment

class Attach_Hookshot(FGEquipmentAttachment):
    mAttachSocket = weaponSocket_temp
    PrimaryActorTick = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=False, bTickEvenWhenPaused=False)
    bNetUseOwnerRelevancy = True
    bReplicates = True
    RemoteRole = 1
    
