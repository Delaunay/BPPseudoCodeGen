
from codegen.ue4_stub import *

from Game.FactoryGame.-Shared.Blueprint.BP_DamageType import BP_DamageType

class DamageType_GasCloud(BP_DamageType):
    mFromGas = True
    mDamageImpulseZ = 100
    bCausedByWorld = True
    
