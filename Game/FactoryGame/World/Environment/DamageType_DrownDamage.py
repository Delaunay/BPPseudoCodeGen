
from codegen.ue4_stub import *

from Game.FactoryGame.-Shared.Blueprint.BP_DamageType import BP_DamageType

class DamageType_DrownDamage(BP_DamageType):
    mImpactParticle = Namespace(AssetPath='/Game/FactoryGame/Character/Creature/Enemy/Hog/Particle/Drool.Drool')
    mDamageImpulseZ = 100
    bCausedByWorld = True
    
