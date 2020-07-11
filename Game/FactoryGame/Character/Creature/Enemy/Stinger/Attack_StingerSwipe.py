
from codegen.ue4_stub import *

from Script.FactoryGame import FGAttackMelee

class Attack_StingerSwipe(FGAttackMelee):
    mAttackMontage = Namespace(AssetPath='/Game/FactoryGame/Character/Creature/Enemy/Stinger/Animation/Attack_02_Montage.Attack_02_Montage')
    mAttackRange = 700
    mAttackActivationDistance = 400
    mDamage = 30
    mDamageType = NewObject[DamageType_StingerSwipe]()
    mAttackAngle = 40
    
