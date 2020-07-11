
from codegen.ue4_stub import *

from Script.FactoryGame import FGAttackMelee

class Attack_HogRoar(FGAttackMelee):
    mAttackMontage = Namespace(AssetPath='/Game/FactoryGame/Character/Creature/Enemy/Hog/Animation/HogRoarMontage.HogRoarMontage')
    mStopsMovement = True
    mAttackRange = 20000
    mAttackActivationDistance = 20000
    mDamageType = NewObject[DamageType_HogHit]()
    mAttackAngle = 60
    
