
from codegen.ue4_stub import *

from Script.FactoryGame import FGItemDescriptor

class Desc_Fuel(FGItemDescriptor):
    mUseDisplayNameAndDescription = True
    mDisplayName = NSLOCTEXT("", "75F060B34F361C77B83B528BBC642E9A", "Packaged Fuel")
    mDescription = NSLOCTEXT("", "AC252B154E9B8D601F9F2C9B6DA34F74", "Fuel.\r\nPackaged Fuel, either converted into electricity or as fuel for vehicles.")
    mStackSize = EStackSize::SS_MEDIUM
    mCanBeDiscarded = True
    mEnergyValue = 600
    mForm = EResourceForm::RF_SOLID
    mInventoryIcon = Namespace(DrawAs=3, ImageSize={'X': 64, 'Y': 64}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$Empty': True}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    mSmallIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/Fuel/UI/IconDesc_Fuel_64.IconDesc_Fuel_64')
    mPersistentBigIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/Fuel/UI/IconDesc_Fuel_256.IconDesc_Fuel_256')
    mConveyorMesh = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/Fuel/SM_Fuel_01.SM_Fuel_01')
    mPreviewView = Namespace(CameraPitch=-35, Distance=130, FocalOffset={'X': 0, 'Y': 0, 'Z': 20})
    mItemCategory = NewObject[Cat_Packaging]()
    mFluidDensity = 1
    mFluidViscosity = 1
    mFluidFriction = 0.10000000149011612
    
