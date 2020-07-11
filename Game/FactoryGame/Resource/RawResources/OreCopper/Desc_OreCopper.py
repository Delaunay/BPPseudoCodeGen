
from codegen.ue4_stub import *

from Script.FactoryGame import FGResourceDescriptor

class Desc_OreCopper(FGResourceDescriptor):
    mDepositMaterial = Namespace(AssetPath='/Game/FactoryGame/Resource/RawResources/Deposits/Materials/Deposit_Copper_Inst.Deposit_Copper_Inst')
    mDecalSize = 200
    mPingColor = Namespace(A=1, B=0.15000000596046448, G=0.5, R=0.05000000074505806)
    mCollectSpeedMultiplier = 1
    mCompassTexture = Namespace(AssetPath='/Game/FactoryGame/Resource/RawResources/Nodes/UI/CopperOre_64.CopperOre_64')
    mManualMiningParticle = Namespace(AssetPath='/Game/FactoryGame/VFX/Factory/Miner/P_Mining_Iron_01.P_Mining_Iron_01')
    mFactoryMiningParticle = Namespace(AssetPath='/Game/FactoryGame/Equipment/ResourceCollector/Particle/MiningHitGround_Copper.MiningHitGround_Copper')
    mDestroyedParticle = Namespace(AssetPath='/Game/FactoryGame/VFX/World/Destructible/P_Copper_Destruction_01.P_Copper_Destruction_01')
    mManualMiningAudioName = Metal
    mUseDisplayNameAndDescription = True
    mDisplayName = NSLOCTEXT("", "5385E3FA4319A76BABA2329ACED5F215", "Copper Ore")
    mDescription = NSLOCTEXT("", "D5772BEC4D3E080A093B87B670B682C2", "Used for crafting.\r\nBasic resource mainly used for electricity.")
    mStackSize = EStackSize::SS_MEDIUM
    mCanBeDiscarded = True
    mRememberPickUp = True
    mForm = EResourceForm::RF_SOLID
    mInventoryIcon = Namespace(DrawAs=3, ImageSize={'X': 64, 'Y': 64}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$Empty': True}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    mSmallIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/RawResources/Nodes/UI/CopperOre_64.CopperOre_64')
    mPersistentBigIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/RawResources/Nodes/UI/CopperOre_256.CopperOre_256')
    mConveyorMesh = Namespace(AssetPath='/Game/FactoryGame/Resource/RawResources/Ores/Meshes/SM_CopperOre_02.SM_CopperOre_02')
    mItemCategory = NewObject[Cat_RawMaterials]()
    mFluidDensity = 1
    mFluidViscosity = 1
    mFluidFriction = 0.10000000149011612
    
