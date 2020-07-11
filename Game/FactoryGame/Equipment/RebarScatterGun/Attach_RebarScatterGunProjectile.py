
from codegen.ue4_stub import *

from Game.FactoryGame.Equipment.RebarGun.Attach_RebarGunProjectile import Attach_RebarGunProjectile

class Attach_RebarScatterGunProjectile(Attach_RebarGunProjectile):
    PrimaryActorTick = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=False, bTickEvenWhenPaused=False)
    bNetUseOwnerRelevancy = True
    bReplicates = True
    RemoteRole = 1
    
