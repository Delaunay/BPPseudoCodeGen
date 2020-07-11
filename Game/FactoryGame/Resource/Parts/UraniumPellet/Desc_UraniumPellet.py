
from codegen.ue4_stub import *

from Script.FactoryGame import FGItemDescriptor

class Desc_UraniumPellet(FGItemDescriptor):
    mUseDisplayNameAndDescription = True
    mDisplayName = NSLOCTEXT("", "4AF47E8C44F61B0C92D2FD86F1912BB7", "Uranium Pellet")
    mDescription = NSLOCTEXT("", "0446EB1840B4F1050235E0BD7385C4BB", "Produced in the Refniery, Uranium Pellets are purified and cast from Uranium Ore. \r\nPrimarily used to make Uranium Cells.\r\nModerately radioactive.")
    mStackSize = EStackSize::SS_BIG
    mCanBeDiscarded = True
    mRadioactiveDecay = 7.5
    mForm = EResourceForm::RF_SOLID
    mInventoryIcon = Namespace(DrawAs=3, ImageSize={'X': 64, 'Y': 64}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$Empty': True}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    mSmallIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/UraniumPellet/UI/IconDesc_UraniumPellets_64.IconDesc_UraniumPellets_64')
    mPersistentBigIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/UraniumPellet/UI/IconDesc_UraniumPellets_256.IconDesc_UraniumPellets_256')
    mConveyorMesh = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/UraniumPellet/SM_UraniumPellets_01.SM_UraniumPellets_01')
    mItemCategory = NewObject[Cat_AdvancedRefinement]()
    mFluidDensity = 1
    mFluidViscosity = 1
    mFluidFriction = 0.10000000149011612
    
