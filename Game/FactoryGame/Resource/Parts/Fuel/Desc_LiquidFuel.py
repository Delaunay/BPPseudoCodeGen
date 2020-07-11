
from codegen.ue4_stub import *

from Script.FactoryGame import FGItemDescriptor

class Desc_LiquidFuel(FGItemDescriptor):
    mUseDisplayNameAndDescription = True
    mDisplayName = NSLOCTEXT("", "CC5A74DA44B3F473C67C81996CD22CA0", "Fuel")
    mDescription = NSLOCTEXT("", "292D10CD4F0B231FA8CD08AE1BAD1990", "Fuel is either converted into electricity or as fuel for vehicles.")
    mStackSize = EStackSize::SS_FLUID
    mCanBeDiscarded = True
    mEnergyValue = 0.6000000238418579
    mForm = EResourceForm::RF_LIQUID
    mInventoryIcon = Namespace(DrawAs=3, ImageSize={'X': 64, 'Y': 64}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$Empty': True}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    mSmallIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/Fuel/UI/IconDesc_LiquidFuel_Pipe_256.IconDesc_LiquidFuel_Pipe_256')
    mPersistentBigIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/Fuel/UI/IconDesc_LiquidFuel_Pipe_512.IconDesc_LiquidFuel_Pipe_512')
    mConveyorMesh = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/Fuel/SM_Fuel_01.SM_Fuel_01')
    mPreviewView = Namespace(CameraPitch=-35, Distance=130, FocalOffset={'X': 0, 'Y': 0, 'Z': 20})
    mItemCategory = NewObject[Cat_Fuel]()
    mFluidDensity = 1
    mFluidViscosity = 2
    mFluidFriction = 0.10000000149011612
    mFluidColor = Namespace(A=255, B=21, G=125, R=235)
    
