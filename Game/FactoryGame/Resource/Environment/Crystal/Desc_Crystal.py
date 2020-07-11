
from codegen.ue4_stub import *

from Script.FactoryGame import FGItemDescriptor

class Desc_Crystal(FGItemDescriptor):
    mUseDisplayNameAndDescription = True
    mDisplayName = NSLOCTEXT("", "691790CF48631111BA0AC8A41C185301", "Green Power Slug")
    mDescription = NSLOCTEXT("", "BE17B0724F48C3AE06FED88DE4916B05", "A strange slug radiating a weak strange power.")
    mStackSize = EStackSize::SS_SMALL
    mCanBeDiscarded = True
    mRememberPickUp = True
    mForm = EResourceForm::RF_SOLID
    mInventoryIcon = Namespace(DrawAs=3, ImageSize={'X': 64, 'Y': 64}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$Empty': True}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    mSmallIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Environment/Crystal/UI/PowerSlugGreen_64.PowerSlugGreen_64')
    mPersistentBigIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Environment/Crystal/UI/PowerSlugGreen_256.PowerSlugGreen_256')
    mConveyorMesh = Namespace(AssetPath='/Game/FactoryGame/Character/Creature/Wildlife/PowerSnail/Mesh/PowerSnail.PowerSnail')
    mItemCategory = NewObject[Cat_PowerShards]()
    mFluidDensity = 1
    mFluidViscosity = 1
    mFluidFriction = 0.10000000149011612
    
