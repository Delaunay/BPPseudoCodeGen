
from codegen.ue4_stub import *

from Game.FactoryGame.-Shared.Blueprint.BP_DamageType import BP_DamageType

class DamageType_WorldPerimeter(BP_DamageType):
    mDamageImpulseZ = 100
    bCausedByWorld = True
    
