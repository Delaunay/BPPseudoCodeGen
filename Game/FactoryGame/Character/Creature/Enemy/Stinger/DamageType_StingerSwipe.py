
from codegen.ue4_stub import *

from Game.FactoryGame.-Shared.Blueprint.BP_DamageType import BP_DamageType

class DamageType_StingerSwipe(BP_DamageType):
    mShouldDamageDestructible = True
    mDamageImpulseZ = 40000
    DamageImpulse = 90000
    
