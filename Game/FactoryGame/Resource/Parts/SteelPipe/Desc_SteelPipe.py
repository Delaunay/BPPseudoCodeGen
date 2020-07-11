
from codegen.ue4_stub import *

from Script.FactoryGame import FGItemDescriptor

class Desc_SteelPipe(FGItemDescriptor):
    mUseDisplayNameAndDescription = True
    mDisplayName = NSLOCTEXT("", "BC7763FA48475F6D80DD79A0B1A7D5AA", "Steel Pipe")
    mDescription = NSLOCTEXT("", "F16EE2264FBFEE9A08BC0FAD1102FA1B", "Steel Pipes are used most often when constructing a little more advanced buildings.")
    mStackSize = EStackSize::SS_MEDIUM
    mCanBeDiscarded = True
    mForm = EResourceForm::RF_SOLID
    mInventoryIcon = Namespace(DrawAs=3, ImageSize={'X': 64, 'Y': 64}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$Empty': True}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    mSmallIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/SteelPipe/UI/IconDesc_SteelPipe_64.IconDesc_SteelPipe_64')
    mPersistentBigIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/SteelPipe/UI/IconDesc_SteelPipe_256.IconDesc_SteelPipe_256')
    mConveyorMesh = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/SteelPipe/SM_SteelPipe_01.SM_SteelPipe_01')
    mItemCategory = NewObject[Cat_StandardParts]()
    mFluidDensity = 1
    mFluidViscosity = 1
    mFluidFriction = 0.10000000149011612
    
