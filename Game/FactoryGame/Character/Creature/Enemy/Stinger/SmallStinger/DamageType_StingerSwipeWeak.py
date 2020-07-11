
from codegen.ue4_stub import *

from Game.FactoryGame.-Shared.Blueprint.BP_DamageType import BP_DamageType

class DamageType_StingerSwipeWeak(BP_DamageType):
    mShouldDamageDestructible = True
    mDamageImpulseZ = 8000
    DamageImpulse = 40000
    
