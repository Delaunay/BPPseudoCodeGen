
from codegen.ue4_stub import *

from Game.FactoryGame.-Shared.Blueprint.BP_DamageType import BP_DamageType

class DamageType_StingerSwipeStrong(BP_DamageType):
    mShouldDamageDestructible = True
    mDamageImpulseZ = 80000
    DamageImpulse = 90000
    
