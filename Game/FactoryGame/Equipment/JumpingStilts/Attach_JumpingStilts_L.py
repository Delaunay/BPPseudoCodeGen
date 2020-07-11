
from codegen.ue4_stub import *

from Script.FactoryGame import FGJumpingStiltsAttachment

class Attach_JumpingStilts_L(FGJumpingStiltsAttachment):
    mAttachSocket = jumpingstilt_lSocket
    PrimaryActorTick = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=False, bTickEvenWhenPaused=False)
    bNetUseOwnerRelevancy = True
    bReplicates = True
    RemoteRole = 1
    
