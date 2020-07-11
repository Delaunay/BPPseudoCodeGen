
from codegen.ue4_stub import *

from Game.FactoryGame.-Shared.Blueprint.BP_DamageType import BP_DamageType

class DamageType_SpitterProjectile(BP_DamageType):
    mImpactParticle = Namespace(AssetPath='/Game/FactoryGame/Character/Creature/Enemy/Hog/Particle/Eating_01.Eating_01')
    mDamageImpulseZ = 100
    
