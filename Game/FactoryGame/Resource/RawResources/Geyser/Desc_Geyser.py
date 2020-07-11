
from codegen.ue4_stub import *

from Script.FactoryGame import FGResourceDescriptorGeyser

class Desc_Geyser(FGResourceDescriptorGeyser):
    mDecalMaterial = Namespace(AssetPath='/Game/FactoryGame/Resource/RawResources/CrudeOil/Material/CrudeOil_Puddle.CrudeOil_Puddle')
    mDecalSize = 200
    mPingColor = Namespace(A=1, B=0, G=0, R=0)
    mCollectSpeedMultiplier = 1
    mCompassTexture = Namespace(AssetPath='/Game/FactoryGame/World/Environment/HotSpring/UI/IconDesc_Geyser_64.IconDesc_Geyser_64')
    mManualMiningAudioName = Metal
    mUseDisplayNameAndDescription = True
    mDisplayName = NSLOCTEXT("", "9DB1055C403E98F21C0F05B13DB0CECE", "Geyser")
    mDescription = NSLOCTEXT("", "98365DC044C0589967AD07921D4DFCA7", "Used to turn the turbines of the Geo Thermal Generator.")
    mStackSize = EStackSize::SS_MEDIUM
    mCanBeDiscarded = True
    mEnergyValue = 60
    mForm = EResourceForm::RF_HEAT
    mInventoryIcon = Namespace(DrawAs=3, ImageSize={'X': 64, 'Y': 64}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$Empty': True}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    mSmallIcon = Namespace(AssetPath='/Game/FactoryGame/World/Environment/HotSpring/UI/IconDesc_Geyser_64.IconDesc_Geyser_64')
    mPersistentBigIcon = Namespace(AssetPath='/Game/FactoryGame/World/Environment/HotSpring/UI/IconDesc_Geyser_128.IconDesc_Geyser_128')
    mConveyorMesh = Namespace(AssetPath='/Game/FactoryGame/Resource/RawResources/CrudeOil/Mesh/CrudeOilBarrel.CrudeOilBarrel')
    mItemCategory = NewObject[Cat_RawMaterials]()
    mFluidDensity = 1
    mFluidViscosity = 1
    mFluidFriction = 0.10000000149011612
    
