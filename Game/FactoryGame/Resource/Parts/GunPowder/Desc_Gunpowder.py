
from codegen.ue4_stub import *

from Script.FactoryGame import FGItemDescriptor

class Desc_Gunpowder(FGItemDescriptor):
    mUseDisplayNameAndDescription = True
    mDisplayName = NSLOCTEXT("", "750819CE48BD88ED076FD9ABB51D6201", "Black powder")
    mDescription = NSLOCTEXT("", "008BBDF74EF889F13136C893CCF7CC14", "An explosive powder that is commonly used in explosives and cartridges.")
    mStackSize = EStackSize::SS_MEDIUM
    mCanBeDiscarded = True
    mForm = EResourceForm::RF_SOLID
    mInventoryIcon = Namespace(DrawAs=3, ImageSize={'X': 64, 'Y': 64}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$Empty': True}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    mSmallIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/GunPowder/UI/IconDesc_Gunpowder_64.IconDesc_Gunpowder_64')
    mPersistentBigIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/GunPowder/UI/IconDesc_Gunpowder_256.IconDesc_Gunpowder_256')
    mConveyorMesh = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/GunPowder/SM_GunPowder_01.SM_GunPowder_01')
    mItemCategory = NewObject[Cat_Equipment]()
    mFluidDensity = 1
    mFluidViscosity = 1
    mFluidFriction = 0.10000000149011612
    
