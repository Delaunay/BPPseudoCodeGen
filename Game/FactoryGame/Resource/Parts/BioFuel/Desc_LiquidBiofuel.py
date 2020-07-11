
from codegen.ue4_stub import *

from Script.FactoryGame import FGItemDescriptorBiomass

class Desc_LiquidBiofuel(FGItemDescriptorBiomass):
    mUseDisplayNameAndDescription = True
    mDisplayName = NSLOCTEXT("", "4796F9D34BAE890236859A9F39979FC7", "Liquid Biofuel")
    mDescription = NSLOCTEXT("", "51D757B44D163B29C94235B12020AB18", "Fuel.\r\nThe most energy efficient form of biomass.")
    mStackSize = EStackSize::SS_FLUID
    mCanBeDiscarded = True
    mEnergyValue = 0.75
    mForm = EResourceForm::RF_LIQUID
    mInventoryIcon = Namespace(DrawAs=3, ImageSize={'X': 64, 'Y': 64}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$Empty': True}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    mSmallIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/BioFuel/UI/IconDesc_LiquidBiofuel_Pipe_256.IconDesc_LiquidBiofuel_Pipe_256')
    mPersistentBigIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/BioFuel/UI/IconDesc_LiquidBiofuel_Pipe_512.IconDesc_LiquidBiofuel_Pipe_512')
    mConveyorMesh = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/Fuel/SM_FuelBio_01.SM_FuelBio_01')
    mPreviewView = Namespace(CameraPitch=-35, Distance=100, FocalOffset={'X': 0, 'Y': 0, 'Z': 100})
    mItemCategory = NewObject[Cat_Fuel]()
    mFluidDensity = 1
    mFluidViscosity = 2
    mFluidFriction = 0.10000000149011612
    mFluidColor = Namespace(A=255, B=44, G=83, R=59)
    
