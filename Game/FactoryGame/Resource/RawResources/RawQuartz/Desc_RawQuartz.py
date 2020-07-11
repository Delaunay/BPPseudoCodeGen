
from codegen.ue4_stub import *

from Script.FactoryGame import FGResourceDescriptor

class Desc_RawQuartz(FGResourceDescriptor):
    mDepositMesh = Namespace(AssetPath='/Game/FactoryGame/Resource/RawResources/Deposits/DepositCrystal_01.DepositCrystal_01')
    mDepositMaterial = Namespace(AssetPath='/Game/FactoryGame/Resource/RawResources/Deposits/Materials/DepositQuartz_Inst.DepositQuartz_Inst')
    mDecalSize = 200
    mPingColor = Namespace(A=1, B=0.7649999856948853, G=1, R=0.9836320281028748)
    mCollectSpeedMultiplier = 1
    mCompassTexture = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/QuartzCrystal/UI/IconDesc_QuartzCrystal_64.IconDesc_QuartzCrystal_64')
    mManualMiningParticle = Namespace(AssetPath='/Game/FactoryGame/VFX/Factory/Miner/P_Mining_Iron_01.P_Mining_Iron_01')
    mFactoryMiningParticle = Namespace(AssetPath='/Game/FactoryGame/Equipment/ResourceCollector/Particle/MiningHitGround_01.MiningHitGround_01')
    mDestroyedParticle = Namespace(AssetPath='/Game/FactoryGame/VFX/World/Destructible/P_Quartz_Destruction_01.P_Quartz_Destruction_01')
    mManualMiningAudioName = Metal
    mUseDisplayNameAndDescription = True
    mDisplayName = NSLOCTEXT("", "4E04D0E840050ABEFFEE399598A98235", "Raw Quartz")
    mDescription = NSLOCTEXT("", "F774972A4ED64576FAC1E7841F2C73C6", "Raw Quartz is processed into Quartz Crystals which are used for radar and quantum technology.")
    mStackSize = EStackSize::SS_MEDIUM
    mCanBeDiscarded = True
    mRememberPickUp = True
    mForm = EResourceForm::RF_SOLID
    mInventoryIcon = Namespace(DrawAs=3, ImageSize={'X': 64, 'Y': 64}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$Empty': True}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    mSmallIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/QuartzCrystal/UI/IconDesc_QuartzCrystal_64.IconDesc_QuartzCrystal_64')
    mPersistentBigIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/QuartzCrystal/UI/IconDesc_QuartzCrystal_256.IconDesc_QuartzCrystal_256')
    mConveyorMesh = Namespace(AssetPath='/Game/FactoryGame/Resource/RawResources/Ores/Meshes/SM_RawQuartz_01.SM_RawQuartz_01')
    mItemCategory = NewObject[Cat_RawMaterials]()
    mFluidDensity = 1
    mFluidViscosity = 1
    mFluidFriction = 0.10000000149011612
    
