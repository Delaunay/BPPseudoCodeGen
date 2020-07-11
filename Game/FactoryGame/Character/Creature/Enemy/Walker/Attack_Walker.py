
from codegen.ue4_stub import *

from Script.FactoryGame import FGAttackMelee

class Attack_Walker(FGAttackMelee):
    mAttackMontage = Namespace(AssetPath='/Game/FactoryGame/Character/Creature/Enemy/Walker/Animation/WalkerAttackMontage.WalkerAttackMontage')
    mStopsMovement = True
    mAttackRange = 750
    mAttackActivationDistance = 500
    mDamage = 10
    mDamageType = NewObject[DamageType_WalkerHit]()
    mAttackAngle = 60
    
