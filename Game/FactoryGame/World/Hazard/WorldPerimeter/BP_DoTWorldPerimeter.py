
from codegen.ue4_stub import *

from Script.FactoryGame import FGDamageOverTime

class BP_DoTWorldPerimeter(FGDamageOverTime):
    mDamageInterval = 0.20000000298023224
    mDamageAmount = 1
    mDamageClass = NewObject[DamageType_WorldPerimeter]()
    mActorFilter = ['/Script/FactoryGame.FGCharacterPlayer', '/Script/FactoryGame.FGVehicle']
    
