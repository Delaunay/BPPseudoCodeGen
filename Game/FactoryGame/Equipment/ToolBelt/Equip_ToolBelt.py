
from codegen.ue4_stub import *

from Script.FactoryGame import FGToolBelt

class Equip_ToolBelt(FGToolBelt):
    mNumArmSlotsToUnlock = 2
    PrimaryActorTick = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=False, bTickEvenWhenPaused=False)
    bOnlyRelevantToOwner = True
    bNetUseOwnerRelevancy = True
    bReplicates = True
    RemoteRole = 1
    
