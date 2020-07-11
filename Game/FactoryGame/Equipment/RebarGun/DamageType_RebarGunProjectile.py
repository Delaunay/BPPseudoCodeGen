
from codegen.ue4_stub import *

from Script.FactoryGame import FGDamageType

class DamageType_RebarGunProjectile(FGDamageType):
    mImpactParticle = Namespace(AssetPath='/Game/FactoryGame/Equipment/RebarGun/Particle/Hit.Hit')
    mPlayImpactParticleOn = 1
    mDamageImpulseZ = 100
    
