
from codegen.ue4_stub import *

from Game.FactoryGame.Equipment.Rifle.Attach_Rifle import Attach_Rifle

class Attach_Rifle_Mk2(Attach_Rifle):
    PrimaryActorTick = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=False, bTickEvenWhenPaused=False)
    bNetUseOwnerRelevancy = True
    bReplicates = True
    RemoteRole = 1
    
