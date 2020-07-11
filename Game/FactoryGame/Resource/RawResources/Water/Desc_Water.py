
from codegen.ue4_stub import *

from Script.FactoryGame import FGResourceDescriptor

class Desc_Water(FGResourceDescriptor):
    mDecalSize = 200
    mCollectSpeedMultiplier = 1
    mManualMiningAudioName = Metal
    mUseDisplayNameAndDescription = True
    mDisplayName = NSLOCTEXT("", "42E272954ECF5B2F7DFF598A978FC098", "Water")
    mDescription = NSLOCTEXT("", "3726A6EA4352F89FE72F6FA80ED987A8", "It\'s water.")
    mStackSize = EStackSize::SS_FLUID
    mCanBeDiscarded = True
    mForm = EResourceForm::RF_LIQUID
    mInventoryIcon = Namespace(DrawAs=3, ImageSize={'X': 64, 'Y': 64}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$Empty': True}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    mSmallIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/RawResources/Water/UI/LiquidWater_Pipe_256.LiquidWater_Pipe_256')
    mPersistentBigIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/RawResources/Water/UI/LiquidWater_Pipe_512.LiquidWater_Pipe_512')
    mConveyorMesh = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/PackagedWater/SM_PackedWater_01.SM_PackedWater_01')
    mItemCategory = NewObject[Cat_Unpackaging]()
    mFluidDensity = 1
    mFluidViscosity = 1
    mFluidFriction = 0.10000000149011612
    mFluidColor = Namespace(A=255, B=212, G=176, R=122)
    
