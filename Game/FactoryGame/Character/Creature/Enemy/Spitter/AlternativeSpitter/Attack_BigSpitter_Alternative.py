
from codegen.ue4_stub import *

from Script.FactoryGame import FGAttackRanged

class Attack_BigSpitter_Alternative(FGAttackRanged):
    mProjectileClass = NewObject[BP_SpitterProjectileBig_Alternative]()
    mAttackMontage = Namespace(AssetPath='/Game/FactoryGame/Character/Creature/Enemy/Spitter/Animation/SpitterAttackMontageAlt.SpitterAttackMontageAlt')
    mStopsMovement = True
    mAttackRange = 7000
    mAttackActivationDistance = 6000
    mDamage = 8
    mDamageType = NewObject[DamageType_SpitterProjectile]()
    mAttackAngle = 60
    
