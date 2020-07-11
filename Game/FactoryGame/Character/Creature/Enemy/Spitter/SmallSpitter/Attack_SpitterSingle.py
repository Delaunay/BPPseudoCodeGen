
from codegen.ue4_stub import *

from Script.FactoryGame import FGAttackRanged

class Attack_SpitterSingle(FGAttackRanged):
    mProjectileClass = NewObject[BP_SpitterProjectileSingle]()
    mAttackMontage = Namespace(AssetPath='/Game/FactoryGame/Character/Creature/Enemy/Spitter/Animation/SpitterAttackMontageSmall.SpitterAttackMontageSmall')
    mAttackRange = 2500
    mAttackActivationDistance = 2000
    mDamage = 5
    mDamageType = NewObject[DamageType_SpitterProjectile]()
    mAttackAngle = 60
    
