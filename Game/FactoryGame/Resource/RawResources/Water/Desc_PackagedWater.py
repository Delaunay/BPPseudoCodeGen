
from codegen.ue4_stub import *

from Script.FactoryGame import FGItemDescriptor

class Desc_PackagedWater(FGItemDescriptor):
    mUseDisplayNameAndDescription = True
    mDisplayName = NSLOCTEXT("", "77CD14484E453D04011A48926DDCAD0F", "Packaged Water")
    mDescription = NSLOCTEXT("", "D11F612F4168DD6CBEE5F29DBEE7C789", "Water, packaged for alternative transport.")
    mStackSize = EStackSize::SS_MEDIUM
    mCanBeDiscarded = True
    mForm = EResourceForm::RF_SOLID
    mInventoryIcon = Namespace(DrawAs=3, ImageSize={'X': 64, 'Y': 64}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$Empty': True}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    mSmallIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/PackagedWater/UI/IconDesc_PackagedWater_64.IconDesc_PackagedWater_64')
    mPersistentBigIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/PackagedWater/UI/IconDesc_PackagedWater_256.IconDesc_PackagedWater_256')
    mConveyorMesh = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/PackagedWater/SM_PackedWater_01.SM_PackedWater_01')
    mItemCategory = NewObject[Cat_Packaging]()
    mFluidDensity = 1
    mFluidViscosity = 1
    mFluidFriction = 0.10000000149011612
    
