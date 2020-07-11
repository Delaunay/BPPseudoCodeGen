
from codegen.ue4_stub import *

from Script.FactoryGame import FGItemDescriptor

class Desc_TurboFuel(FGItemDescriptor):
    mUseDisplayNameAndDescription = True
    mDisplayName = NSLOCTEXT("", "85BC4F06447CDE09D795C6AC9B67B9EF", "Packaged Turbofuel")
    mDescription = NSLOCTEXT("", "DE17DE3949AD00F409512286C17E9FAE", "Packaged Turbofuel, a more efficient alternative to Fuel. Used in vehicles.")
    mStackSize = EStackSize::SS_MEDIUM
    mCanBeDiscarded = True
    mEnergyValue = 2000
    mForm = EResourceForm::RF_SOLID
    mInventoryIcon = Namespace(DrawAs=3, ImageSize={'X': 64, 'Y': 64}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$Empty': True}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    mSmallIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/Turbofuel/UI/IconDesc_TurboFuel_64.IconDesc_TurboFuel_64')
    mPersistentBigIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/Turbofuel/UI/IconDesc_TurboFuel_256.IconDesc_TurboFuel_256')
    mConveyorMesh = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/Turbofuel/SM_TurboFuel_01.SM_TurboFuel_01')
    mItemCategory = NewObject[Cat_Packaging]()
    mFluidDensity = 1
    mFluidViscosity = 1
    mFluidFriction = 0.10000000149011612
    
