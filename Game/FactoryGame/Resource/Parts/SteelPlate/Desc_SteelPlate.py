
from codegen.ue4_stub import *

from Script.FactoryGame import FGItemDescriptor

class Desc_SteelPlate(FGItemDescriptor):
    mUseDisplayNameAndDescription = True
    mDisplayName = NSLOCTEXT("", "CE7C20C04BBEAE9BBC8368B83C21FA8A", "Steel Beam")
    mDescription = NSLOCTEXT("", "5BE7CCB64490E7A3CBDDC28B7BE44A81", "Steel Beams are used most often when constructing a little more advanced buildings.")
    mStackSize = EStackSize::SS_MEDIUM
    mCanBeDiscarded = True
    mForm = EResourceForm::RF_SOLID
    mInventoryIcon = Namespace(DrawAs=3, ImageSize={'X': 64, 'Y': 64}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$Empty': True}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    mSmallIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/SteelPlate/UI/IconDesc_SteelBeam_64.IconDesc_SteelBeam_64')
    mPersistentBigIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/SteelPlate/UI/IconDesc_SteelBeam_256.IconDesc_SteelBeam_256')
    mConveyorMesh = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/SteelBeam/SM_SteelBeam_01.SM_SteelBeam_01')
    mItemCategory = NewObject[Cat_StandardParts]()
    mFluidDensity = 1
    mFluidViscosity = 1
    mFluidFriction = 0.10000000149011612
    
