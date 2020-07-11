
from codegen.ue4_stub import *

from Script.FactoryGame import FGRailroadSubsystem

class BP_RailroadSubsystem(FGRailroadSubsystem):
    mConnectDistance = 200
    mSwitchControlClass = NewObject[Build_RailroadSwitchControl]()
    mVehicleSoundComponentClass = NewObject[BP_RailroadVehicleSoundComponent]()
    PrimaryActorTick = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=True, bTickEvenWhenPaused=False)
    bAlwaysRelevant = True
    bReplicates = True
    RemoteRole = 1
    
