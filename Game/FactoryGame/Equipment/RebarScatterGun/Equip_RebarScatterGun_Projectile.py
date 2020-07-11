
from codegen.ue4_stub import *

from Game.FactoryGame.Equipment.RebarGun.Equip_RebarGun_Projectile import Equip_RebarGun_Projectile

class Equip_RebarScatterGun_Projectile(Equip_RebarGun_Projectile):
    mProjectileData = Namespace(CanTriggerExplodeBySameClass=True, DamageType='/Game/FactoryGame/Equipment/RebarGun/DamageType_RebarGunProjectile.DamageType_RebarGunProjectile_C', DamageTypeExplode='/Script/FactoryGame.FGDamageType', ExplodeAtEndOfLife=False, ExplosionDamage=20, ExplosionRadius=0, ImpactDamage=20, ProjectileClass='/Game/FactoryGame/Equipment/RebarScatterGun/BP_RebarScatterProjectile.BP_RebarScatterProjectile_C', ProjectileLifeSpan=10, ProjectileStickSpan=5, ShouldExplodeOnImpact=False)
    mAmmunitionClass = NewObject[Desc_SpikedRebarScatter]()
    mAttachmentClass = NewObject[Attach_RebarScatterGunProjectile]()
    mEquipmentSlot = EEquipmentSlot::ES_ARMS
    PrimaryActorTick = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=False, bTickEvenWhenPaused=False)
    bOnlyRelevantToOwner = True
    bNetUseOwnerRelevancy = True
    bReplicates = True
    RemoteRole = 1
    
