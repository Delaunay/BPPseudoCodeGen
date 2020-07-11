
from codegen.ue4_stub import *

from Script.FactoryGame import FGItemDescriptor

class Desc_SteelPlateReinforced(FGItemDescriptor):
    mUseDisplayNameAndDescription = True
    mDisplayName = NSLOCTEXT("", "0463F80E45BB9C6EED03E9B96E62CFA7", "Encased Industrial Beam")
    mDescription = NSLOCTEXT("", "9BB7145849FA8B0238CE949446DD9937", "Encased Industrial Beams utilizes the compressive strength of concrete and tensile strength of steel simultaneously.\r\nMostly used as a stable basis for constructing buildings.")
    mStackSize = EStackSize::SS_MEDIUM
    mCanBeDiscarded = True
    mForm = EResourceForm::RF_SOLID
    mInventoryIcon = Namespace(DrawAs=3, ImageSize={'X': 64, 'Y': 64}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$Empty': True}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    mSmallIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/SteelPlateReinforced/UI/IconDesc_EncasedSteelBeam_64.IconDesc_EncasedSteelBeam_64')
    mPersistentBigIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/SteelPlateReinforced/UI/IconDesc_EncasedSteelBeam_256.IconDesc_EncasedSteelBeam_256')
    mConveyorMesh = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/EncasedIndustrialBeam/SM_EncasedIndustrialBeam_01.SM_EncasedIndustrialBeam_01')
    mItemCategory = NewObject[Cat_StandardParts]()
    mFluidDensity = 1
    mFluidViscosity = 1
    mFluidFriction = 0.10000000149011612
    
