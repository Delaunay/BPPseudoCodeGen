
from codegen.ue4_stub import *

from Script.FactoryGame import FGAttackRanged

class Attack_Spitter(FGAttackRanged):
    mProjectileClass = NewObject[BP_SpitterProjectile]()
    mAttackMontage = Namespace(AssetPath='/Game/FactoryGame/Character/Creature/Enemy/Spitter/Animation/SpitterAttackMontage.SpitterAttackMontage')
    mStopsMovement = True
    mAttackRange = 7000
    mAttackActivationDistance = 6000
    mDamage = 10
    mDamageType = NewObject[DamageType_SpitterProjectile]()
    mAttackAngle = 60
    
