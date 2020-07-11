
from codegen.ue4_stub import *

from Game.FactoryGame.Buildable.-Shared.WorkBench.BP_ManualManufacturingRecipeComponent import BP_ManualManufacturingRecipeComponent

class BP_CrystalFurnitureTradingComponent(BP_ManualManufacturingRecipeComponent):
    mFatigueMultiplier = 0.20000000298023224
    mFatigueDecreaseSpeedMultiplier = 3
    mHoldProduceTime = 0.20000000298023224
    mFatigueUpdaterInterval = 10
    mCooldownDelay = 1.5
    mIsFatigueEnabled = True
    PrimaryComponentTick = Namespace(EndTickGroup=0, TickGroup=2, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=True, bTickEvenWhenPaused=False)
    bReplicates = True
    bAutoActivate = True
    
