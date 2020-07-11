
from codegen.ue4_stub import *

from Game.FactoryGame.-Shared.Blueprint.BP_DamageType import BP_DamageType

class DamageType_XenoZapper(BP_DamageType):
    mImpactAudioEvent = Namespace(AssetPath='/Game/FactoryGame/Equipment/ShockShank/Audio/Rework/Play_EQ_ShockShank_Zap.Play_EQ_ShockShank_Zap')
    mImpactParticle = Namespace(AssetPath='/Game/FactoryGame/VFX/Equipment/Weapons/XenoBasher_Shank/P_XenoHit_01.P_XenoHit_01')
    mPlayImpactParticleOn = 1
    mDamageImpulseZ = 35000
    DamageImpulse = 70000
    
