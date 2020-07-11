
from codegen.ue4_stub import *

from Script.FactoryGame import FGRadioactivitySubsystem

class BP_RadioactiveSubsystem(FGRadioactivitySubsystem):
    PrimaryActorTick = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=True, bTickEvenWhenPaused=False)
    bAlwaysRelevant = True
    bReplicates = True
    RemoteRole = 1
    
