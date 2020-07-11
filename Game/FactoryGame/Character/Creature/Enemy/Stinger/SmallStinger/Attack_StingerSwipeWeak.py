
from codegen.ue4_stub import *

from Script.FactoryGame import FGAttackMelee

class Attack_StingerSwipeWeak(FGAttackMelee):
    mAttackMontage = Namespace(AssetPath='/Game/FactoryGame/Character/Creature/Enemy/Stinger/Animation/Attack_02_MontageSmall.Attack_02_MontageSmall')
    mAttackRange = 400
    mAttackActivationDistance = 300
    mDamage = 5
    mDamageType = NewObject[DamageType_StingerSwipeWeak]()
    mAttackAngle = 70
    
