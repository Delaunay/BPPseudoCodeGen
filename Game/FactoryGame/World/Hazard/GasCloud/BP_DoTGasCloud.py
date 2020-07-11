
from codegen.ue4_stub import *

from Script.FactoryGame import FGDamageOverTime

class BP_DoTGasCloud(FGDamageOverTime):
    mDamageInterval = 1
    mDamageAmount = 5
    mDamageClass = NewObject[DamageType_GasCloud]()
    mActorFilter = ['/Script/FactoryGame.FGCharacterPlayer', '/Script/FactoryGame.FGVehicle']
    
