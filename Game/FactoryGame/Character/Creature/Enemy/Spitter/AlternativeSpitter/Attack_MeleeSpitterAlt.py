
from codegen.ue4_stub import *

from Script.FactoryGame import FGAttackRanged

class Attack_MeleeSpitterAlt(FGAttackRanged):
    mProjectileClass = NewObject[BP_SpitterMeleeAlt]()
    mAttackMontage = Namespace(AssetPath='/Game/FactoryGame/Character/Creature/Enemy/Spitter/Animation/SpitterAttackMontageAlt.SpitterAttackMontageAlt')
    mAttackRange = 7000
    mAttackActivationDistance = 6000
    mDamage = 20
    mDamageType = NewObject[DamageType_SpitterMelee]()
    mAttackAngle = 60
    
