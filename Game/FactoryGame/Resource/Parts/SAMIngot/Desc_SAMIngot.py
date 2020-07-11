
from codegen.ue4_stub import *

from Script.FactoryGame import FGItemDescriptor

class Desc_SAMIngot(FGItemDescriptor):
    mUseDisplayNameAndDescription = True
    mDisplayName = NSLOCTEXT("", "86C667874153926A6DB083B72980046B", "S.A.M. Ingot")
    mDescription = NSLOCTEXT("", "FC2CF9DF4664D4D93FD6A5994C7FFB51", "Used to make S.A.M. Fluctuator.")
    mStackSize = EStackSize::SS_SMALL
    mCanBeDiscarded = True
    mForm = EResourceForm::RF_SOLID
    mInventoryIcon = Namespace(DrawAs=3, ImageSize={'X': 64, 'Y': 64}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$Empty': True}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    mConveyorMesh = Namespace(AssetPath='/Game/FactoryGame/Resource/RawResources/SAM/Mesh/SAMIngot.SAMIngot')
    mItemCategory = NewObject[Cat_Ingots]()
    mFluidDensity = 1
    mFluidViscosity = 1
    mFluidFriction = 0.10000000149011612
    
