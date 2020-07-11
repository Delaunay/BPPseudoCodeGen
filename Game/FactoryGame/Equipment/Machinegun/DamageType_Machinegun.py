
from codegen.ue4_stub import *

from Game.FactoryGame.-Shared.Blueprint.BP_DamageType import BP_DamageType

class DamageType_Machinegun(BP_DamageType):
    mImpactAudioSetting = 1
    mPlayImpactParticleOn = 1
    mDamageImpulseZ = 10000
    DamageImpulse = 60000
    
