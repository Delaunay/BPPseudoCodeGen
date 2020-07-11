
from codegen.ue4_stub import *

from Script.FactoryGame import FGResourceDescriptor

class Desc_OreBauxite(FGResourceDescriptor):
    mDepositMaterial = Namespace(AssetPath='/Game/FactoryGame/Resource/RawResources/Deposits/Materials/Deposit_Bauxite_Inst.Deposit_Bauxite_Inst')
    mDecalSize = 200
    mPingColor = Namespace(A=1, B=0, G=0, R=1)
    mCollectSpeedMultiplier = 1
    mCompassTexture = Namespace(AssetPath='/Game/FactoryGame/Resource/RawResources/Nodes/UI/Bauxite_64.Bauxite_64')
    mManualMiningParticle = Namespace(AssetPath='/Game/FactoryGame/VFX/Factory/Miner/P_Mining_Iron_01.P_Mining_Iron_01')
    mFactoryMiningParticle = Namespace(AssetPath='/Game/FactoryGame/Equipment/ResourceCollector/Particle/MiningHitGround_01.MiningHitGround_01')
    mDestroyedParticle = Namespace(AssetPath='/Game/FactoryGame/VFX/World/Destructible/P_Bauxite_Destruction_01.P_Bauxite_Destruction_01')
    mManualMiningAudioName = Metal
    mUseDisplayNameAndDescription = True
    mDisplayName = NSLOCTEXT("", "C3DF126F4607A74BC7D5E0A90F367418", "Bauxite")
    mDescription = NSLOCTEXT("", "EA1A41634C09C44A5E4A079785A8B085", "Bauxite is turned into Aluminum Ingots via an advanced smelting process.")
    mStackSize = EStackSize::SS_MEDIUM
    mCanBeDiscarded = True
    mRememberPickUp = True
    mForm = EResourceForm::RF_SOLID
    mInventoryIcon = Namespace(DrawAs=3, ImageSize={'X': 64, 'Y': 64}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$Empty': True}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    mSmallIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/RawResources/Nodes/UI/Bauxite_64.Bauxite_64')
    mPersistentBigIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/RawResources/Nodes/UI/Bauxite_256.Bauxite_256')
    mConveyorMesh = Namespace(AssetPath='/Game/FactoryGame/Resource/RawResources/Ores/Meshes/SM_BauxiteOre_01.SM_BauxiteOre_01')
    mItemCategory = NewObject[Cat_RawMaterials]()
    mFluidDensity = 1
    mFluidViscosity = 1
    mFluidFriction = 0.10000000149011612
    
