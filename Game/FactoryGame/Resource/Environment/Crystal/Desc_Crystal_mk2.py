
from codegen.ue4_stub import *

from Script.FactoryGame import FGItemDescriptor

class Desc_Crystal_mk2(FGItemDescriptor):
    mUseDisplayNameAndDescription = True
    mDisplayName = NSLOCTEXT("", "15087FDA48183638C4FCBA9A7D789AD7", "Yellow Power Slug")
    mDescription = NSLOCTEXT("", "CADAEA054F0E615FD644B0B90DEC4910", "A strange slug radiating a strange power.")
    mStackSize = EStackSize::SS_SMALL
    mCanBeDiscarded = True
    mRememberPickUp = True
    mForm = EResourceForm::RF_SOLID
    mInventoryIcon = Namespace(DrawAs=3, ImageSize={'X': 64, 'Y': 64}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$Empty': True}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    mSmallIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Environment/Crystal/UI/PowerSlugYellow_64.PowerSlugYellow_64')
    mPersistentBigIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Environment/Crystal/UI/PowerSlugYellow_256.PowerSlugYellow_256')
    mConveyorMesh = Namespace(AssetPath='/Game/FactoryGame/Character/Creature/Wildlife/PowerSnail/Mesh/PowerSnail.PowerSnail')
    mItemCategory = NewObject[Cat_PowerShards]()
    mFluidDensity = 1
    mFluidViscosity = 1
    mFluidFriction = 0.10000000149011612
    
