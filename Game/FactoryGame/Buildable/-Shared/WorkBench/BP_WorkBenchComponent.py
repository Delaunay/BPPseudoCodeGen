
from codegen.ue4_stub import *

from Game.FactoryGame.Buildable.-Shared.WorkBench.BP_ManualManufacturingComponent import BP_ManualManufacturingComponent

class BP_WorkBenchComponent(BP_ManualManufacturingComponent):
    mManufacturingSpeed = 8
    mFatigueMultiplier = 0.5
    mFatigueDecreaseSpeedMultiplier = 0.5
    mHoldProduceTime = 0.25
    mFatigueUpdaterInterval = 10
    mCooldownDelay = 1
    PrimaryComponentTick = Namespace(EndTickGroup=0, TickGroup=2, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=True, bTickEvenWhenPaused=False)
    bReplicates = True
    bAutoActivate = True
    
