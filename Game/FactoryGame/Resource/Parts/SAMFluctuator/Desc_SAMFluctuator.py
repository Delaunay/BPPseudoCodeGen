
from codegen.ue4_stub import *

from Script.FactoryGame import FGItemDescriptor

class Desc_SAMFluctuator(FGItemDescriptor):
    mUseDisplayNameAndDescription = True
    mDisplayName = NSLOCTEXT("", "CB71017A442E240598187F977A4EF23B", "S.A.M. Fluctuator")
    mDescription = NSLOCTEXT("", "6A3567DD4B60445E645E0BA6578A527F", "Special part used to build the Converter.")
    mStackSize = EStackSize::SS_SMALL
    mCanBeDiscarded = True
    mForm = EResourceForm::RF_SOLID
    mInventoryIcon = Namespace(DrawAs=3, ImageSize={'X': 64, 'Y': 64}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$Empty': True}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    mConveyorMesh = Namespace(AssetPath='/Game/FactoryGame/Resource/RawResources/Ores/Meshes/SM_SAMOre_01.SM_SAMOre_01')
    mItemCategory = NewObject[Cat_Communications]()
    mFluidDensity = 1
    mFluidViscosity = 1
    mFluidFriction = 0.10000000149011612
    
