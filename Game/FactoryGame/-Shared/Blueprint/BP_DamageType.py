
from codegen.ue4_stub import *

from Script.FactoryGame import FGDamageType

class BP_DamageType(FGDamageType):
    mFromGas: bool
    mFromRadiation: bool
    mFromHeat: bool
    mDamageImpulseZ = 100
    
