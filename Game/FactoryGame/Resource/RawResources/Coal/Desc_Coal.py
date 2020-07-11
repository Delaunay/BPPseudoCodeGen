
from codegen.ue4_stub import *

from Script.FactoryGame import FGResourceDescriptor

class Desc_Coal(FGResourceDescriptor):
    mDepositMaterial = Namespace(AssetPath='/Game/FactoryGame/Resource/RawResources/Deposits/Materials/Deposit_Coal_Inst.Deposit_Coal_Inst')
    mDecalSize = 200
    mPingColor = Namespace(A=1, B=0.0481720007956028, G=0.0481720007956028, R=0.0481720007956028)
    mCollectSpeedMultiplier = 1
    mCompassTexture = Namespace(AssetPath='/Game/FactoryGame/Resource/RawResources/Coal/UI/CoalOre_64.CoalOre_64')
    mManualMiningParticle = Namespace(AssetPath='/Game/FactoryGame/VFX/Factory/Miner/P_Mining_Iron_01.P_Mining_Iron_01')
    mFactoryMiningParticle = Namespace(AssetPath='/Game/FactoryGame/Equipment/ResourceCollector/Particle/MiningHitGround_Coal.MiningHitGround_Coal')
    mDestroyedParticle = Namespace(AssetPath='/Game/FactoryGame/VFX/World/Destructible/P_Coal_Destruction_01.P_Coal_Destruction_01')
    mManualMiningAudioName = Metal
    mUseDisplayNameAndDescription = True
    mDisplayName = NSLOCTEXT("", "2D87B04D42150A99CBD6A08DCA906603", "Coal")
    mDescription = NSLOCTEXT("", "75D9E93C42EBBADA8F64ED8DA28D3CAF", "Mainly used as fuel for vehicles & coal generators and for steel production.")
    mStackSize = EStackSize::SS_MEDIUM
    mCanBeDiscarded = True
    mRememberPickUp = True
    mEnergyValue = 300
    mForm = EResourceForm::RF_SOLID
    mInventoryIcon = Namespace(DrawAs=3, ImageSize={'X': 64, 'Y': 64}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$Empty': True}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    mSmallIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/RawResources/Coal/UI/CoalOre_64.CoalOre_64')
    mPersistentBigIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/RawResources/Coal/UI/CoalOre_256.CoalOre_256')
    mConveyorMesh = Namespace(AssetPath='/Game/FactoryGame/Resource/RawResources/Ores/Meshes/SM_CoalOre_01.SM_CoalOre_01')
    mPreviewView = Namespace(CameraPitch=-35, Distance=130, FocalOffset={'X': 0, 'Y': 0, 'Z': 0})
    mItemCategory = NewObject[Cat_RawMaterials]()
    mFluidDensity = 1
    mFluidViscosity = 1
    mFluidFriction = 0.10000000149011612
    
