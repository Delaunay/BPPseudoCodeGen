
from codegen.ue4_stub import *

from Script.FactoryGame import FGItemDescriptor

class Desc_Stator(FGItemDescriptor):
    mUseDisplayNameAndDescription = True
    mDisplayName = NSLOCTEXT("", "A92A731B4BB5E14EB1E930981BD86A8E", "Stator")
    mDescription = NSLOCTEXT("", "5D204F804BC38CE4164486898F2B8313", "The static parts of a motor")
    mStackSize = EStackSize::SS_MEDIUM
    mCanBeDiscarded = True
    mForm = EResourceForm::RF_SOLID
    mInventoryIcon = Namespace(DrawAs=3, ImageSize={'X': 64, 'Y': 64}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$Empty': True}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    mSmallIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/Stator/UI/IconDesc_Stator_64.IconDesc_Stator_64')
    mPersistentBigIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/Stator/UI/IconDesc_Stator_256.IconDesc_Stator_256')
    mConveyorMesh = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/Stator/SM_Stator_01.SM_Stator_01')
    mItemCategory = NewObject[Cat_IndustrialParts]()
    mFluidDensity = 1
    mFluidViscosity = 1
    mFluidFriction = 0.10000000149011612
    
