
from codegen.ue4_stub import *

from Script.FactoryGame import FGAttackMelee

class Attack_StingerGasCloud(FGAttackMelee):
    mAttackMontage = Namespace(AssetPath='/Game/FactoryGame/Character/Creature/Enemy/Stinger/Animation/LeapAttack_Start_Montage.LeapAttack_Start_Montage')
    mStopsMovement = True
    mAttackRange = 900
    mAttackActivationDistance = 500
    mDamageType = NewObject[DamageType_StingerSwipeStrong]()
    mAttackAngle = 180
    
