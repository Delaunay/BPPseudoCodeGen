
from codegen.ue4_stub import *

from Game.FactoryGame.-Shared.Blueprint.BP_DamageType import BP_DamageType

class DamageType_Rifle(BP_DamageType):
    mImpactAudioSetting = 1
    mImpactParticle = Namespace(AssetPath='/Game/FactoryGame/VFX/Misc/Blood/P_HitImpactBlood_01.P_HitImpactBlood_01')
    mPlayImpactParticleOn = 1
    mDamageImpulseZ = 10000
    DamageImpulse = 60000
    
