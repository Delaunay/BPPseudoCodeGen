
from codegen.ue4_stub import *

from Script.FactoryGame import FGItemDescriptor

class Desc_ModularFrameLightweight(FGItemDescriptor):
    mUseDisplayNameAndDescription = True
    mDisplayName = NSLOCTEXT("", "954758C74A92CA8C008737968A508505", "Radio Control Unit")
    mDescription = NSLOCTEXT("", "C94A310E4DABDEA37E89C0B9B1C5978C", "Enhances and directs radio signals")
    mStackSize = EStackSize::SS_SMALL
    mCanBeDiscarded = True
    mForm = EResourceForm::RF_SOLID
    mInventoryIcon = Namespace(DrawAs=3, ImageSize={'X': 64, 'Y': 64}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$Empty': True}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    mSmallIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/RadioControlUnit/UI/IconDesc_RadioControlUnit_64.IconDesc_RadioControlUnit_64')
    mPersistentBigIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/RadioControlUnit/UI/IconDesc_RadioControlUnit_256.IconDesc_RadioControlUnit_256')
    mConveyorMesh = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/RadioControlUnit/SM_RadioControlUnit_01.SM_RadioControlUnit_01')
    mPreviewView = Namespace(CameraPitch=-35, Distance=50, FocalOffset={'X': 0, 'Y': 0, 'Z': 0})
    mItemCategory = NewObject[Cat_Communications]()
    mFluidDensity = 1
    mFluidViscosity = 1
    mFluidFriction = 0.10000000149011612
    
