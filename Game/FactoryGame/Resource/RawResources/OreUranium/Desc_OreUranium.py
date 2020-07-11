
from codegen.ue4_stub import *

from Script.FactoryGame import FGResourceDescriptor

class Desc_OreUranium(FGResourceDescriptor):
    mDepositMaterial = Namespace(AssetPath='/Game/FactoryGame/Resource/RawResources/Deposits/Materials/Deposit_Uranium_Inst.Deposit_Uranium_Inst')
    mDecalSize = 200
    mPingColor = Namespace(A=1, B=0.04060899838805199, G=1, R=0)
    mCollectSpeedMultiplier = 1
    mCompassTexture = Namespace(AssetPath='/Game/FactoryGame/Resource/RawResources/OreUranium/UI/UraniumOre_64.UraniumOre_64')
    mManualMiningParticle = Namespace(AssetPath='/Game/FactoryGame/VFX/Factory/Miner/P_Mining_Iron_01.P_Mining_Iron_01')
    mFactoryMiningParticle = Namespace(AssetPath='/Game/FactoryGame/Equipment/ResourceCollector/Particle/MiningHitGround_01.MiningHitGround_01')
    mDestroyedParticle = Namespace(AssetPath='/Game/FactoryGame/World/Environment/Particle/ResourceDepositDeplete_Uranium_01.ResourceDepositDeplete_Uranium_01')
    mManualMiningAudioName = Metal
    mUseDisplayNameAndDescription = True
    mDisplayName = NSLOCTEXT("", "96C780194CA1A516CA01379CA13C826C", "Uranium")
    mDescription = NSLOCTEXT("", "6B20A90240BA2991CA99D7988A304D4C", "Uranium is radioactive. Mainly used in Nuclear Power Plants.")
    mStackSize = EStackSize::SS_MEDIUM
    mCanBeDiscarded = True
    mRememberPickUp = True
    mRadioactiveDecay = 15
    mForm = EResourceForm::RF_SOLID
    mInventoryIcon = Namespace(DrawAs=3, ImageSize={'X': 64, 'Y': 64}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$Empty': True}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    mSmallIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/RawResources/OreUranium/UI/UraniumOre_64.UraniumOre_64')
    mPersistentBigIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/RawResources/OreUranium/UI/UraniumOre_256.UraniumOre_256')
    mConveyorMesh = Namespace(AssetPath='/Game/FactoryGame/Resource/RawResources/Ores/Meshes/SM_UraniumOre_01.SM_UraniumOre_01')
    mItemCategory = NewObject[Cat_RawMaterials]()
    mFluidDensity = 1
    mFluidViscosity = 1
    mFluidFriction = 0.10000000149011612
    
