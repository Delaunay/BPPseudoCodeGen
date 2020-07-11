
from codegen.ue4_stub import *

from Script.FactoryGame import FGAttackRanged

class Attack_SpitterSingle_Big(FGAttackRanged):
    mProjectileClass = NewObject[BP_SpitterProjectileSingle_Big]()
    mAttackMontage = Namespace(AssetPath='/Game/FactoryGame/Character/Creature/Enemy/Spitter/Animation/SpitterAttackMontageAlt.SpitterAttackMontageAlt')
    mAttackRange = 10000
    mAttackActivationDistance = 9000
    mDamage = 5
    mDamageType = NewObject[DamageType_SpitterProjectile]()
    mAttackAngle = 60
    
