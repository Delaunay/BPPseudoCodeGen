
from codegen.ue4_stub import *

from Script.FactoryGame import FGTimeOfDaySubsystem

class BP_TimeOfDaySubsystem(FGTimeOfDaySubsystem):
    mSyncronizeTimeOfDayInterval = 5
    mDayLengthMinutes = 45
    mNightLengthMinutes = 5
    mDayStartTime = 6
    mNightStartTime = 18
    mSpeedMultiplier = 1
    mNumberOfPassedDays = -1
    mUpdateTime = True
    PrimaryActorTick = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=True, bTickEvenWhenPaused=False)
    bAlwaysRelevant = True
    bReplicates = True
    RemoteRole = 1
    
