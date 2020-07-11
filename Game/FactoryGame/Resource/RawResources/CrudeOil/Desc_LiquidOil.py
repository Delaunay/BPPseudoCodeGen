
from codegen.ue4_stub import *

from Script.FactoryGame import FGResourceDescriptor

class Desc_LiquidOil(FGResourceDescriptor):
    mDecalMaterial = Namespace(AssetPath='/Game/FactoryGame/Resource/RawResources/CrudeOil/Material/CrudeOil_Puddle.CrudeOil_Puddle')
    mDecalSize = 200
    mPingColor = Namespace(A=1, B=0, G=0, R=0)
    mCollectSpeedMultiplier = 1
    mCompassTexture = Namespace(AssetPath='/Game/FactoryGame/Resource/RawResources/CrudeOil/UI/LiquidOil_Pipe_256.LiquidOil_Pipe_256')
    mManualMiningAudioName = Metal
    mUseDisplayNameAndDescription = True
    mDisplayName = NSLOCTEXT("", "7B79816141CFD604CD8F188177995F76", "Crude Oil")
    mDescription = NSLOCTEXT("", "D12C66654895E2720884918AFA99F2BE", "Crude Oil is refined into all kinds of Oil-based resources, like Fuel and Plastic.")
    mStackSize = EStackSize::SS_FLUID
    mCanBeDiscarded = True
    mEnergyValue = 0.3199999928474426
    mForm = EResourceForm::RF_LIQUID
    mInventoryIcon = Namespace(DrawAs=3, ImageSize={'X': 64, 'Y': 64}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$Empty': True}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    mSmallIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/RawResources/CrudeOil/UI/LiquidOil_Pipe_256.LiquidOil_Pipe_256')
    mPersistentBigIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/RawResources/CrudeOil/UI/LiquidOil_Pipe_512.LiquidOil_Pipe_512')
    mConveyorMesh = Namespace(AssetPath='/Game/FactoryGame/Resource/RawResources/CrudeOil/Mesh/CrudeOilBarrel.CrudeOilBarrel')
    mItemCategory = NewObject[Cat_Unpackaging]()
    mFluidDensity = 1
    mFluidViscosity = 3
    mFluidFriction = 0.10000000149011612
    mFluidColor = Namespace(A=255, B=25, G=0, R=25)
    
