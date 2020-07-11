
from codegen.ue4_stub import *

from Game.FactoryGame.Buildable.-Shared.WorkBench.BP_ManualManufacturingComponent import BP_ManualManufacturingComponent

class BP_WorkshopComponent(BP_ManualManufacturingComponent):
    mManufacturingSpeed = 16
    mFatigueMultiplier = 0.20000000298023224
    mFatigueDecreaseSpeedMultiplier = 3
    mHoldProduceTime = 0.20000000298023224
    mFatigueUpdaterInterval = 10
    mCooldownDelay = 1.5
    PrimaryComponentTick = Namespace(EndTickGroup=0, TickGroup=2, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=True, bTickEvenWhenPaused=False)
    bReplicates = True
    bAutoActivate = True
    
