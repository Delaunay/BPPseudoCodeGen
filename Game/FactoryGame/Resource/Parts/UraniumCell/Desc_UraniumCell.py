
from codegen.ue4_stub import *

from Script.FactoryGame import FGItemDescriptor

class Desc_UraniumCell(FGItemDescriptor):
    mUseDisplayNameAndDescription = True
    mDisplayName = NSLOCTEXT("", "87F72107478C6E7013FF169CD850F0FB", "Encased Uranium Cell")
    mDescription = NSLOCTEXT("", "90FF273B49FCC02E278A4CB947975F49", "Uranium Cells are concrete encased uranium pellets. Primarily used to make Nuclear Fuel Rods\r\nModerately radioactive.")
    mStackSize = EStackSize::SS_BIG
    mCanBeDiscarded = True
    mRadioactiveDecay = 7.5
    mForm = EResourceForm::RF_SOLID
    mInventoryIcon = Namespace(DrawAs=3, ImageSize={'X': 64, 'Y': 64}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$Empty': True}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    mSmallIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/UraniumCell/UI/IconDesc_NuclearCell_64.IconDesc_NuclearCell_64')
    mPersistentBigIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/UraniumCell/UI/IconDesc_NuclearCell_256.IconDesc_NuclearCell_256')
    mConveyorMesh = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/UraniumCell/SM_UraniumCell_01.SM_UraniumCell_01')
    mItemCategory = NewObject[Cat_Nuclear]()
    mFluidDensity = 1
    mFluidViscosity = 1
    mFluidFriction = 0.10000000149011612
    
