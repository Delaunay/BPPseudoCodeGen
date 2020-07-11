
from codegen.ue4_stub import *

from Script.FactoryGame import FGAttackMeleeJump

class Attack_StingerJump(FGAttackMeleeJump):
    mJumpRange = 3500
    mPreJumpMontage = Namespace(AssetPath='/Game/FactoryGame/Character/Creature/Enemy/Stinger/Animation/LeapAttack_01_RootMotion_Montage.LeapAttack_01_RootMotion_Montage')
    mAttackRange = 1000
    mAttackActivationDistance = 2800
    mDamage = 50
    mDamageType = NewObject[DamageType_StingerJump]()
    mAttackAngle = 180
    
