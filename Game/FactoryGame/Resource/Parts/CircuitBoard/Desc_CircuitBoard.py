
from codegen.ue4_stub import *

from Script.FactoryGame import FGItemDescriptor

class Desc_CircuitBoard(FGItemDescriptor):
    mUseDisplayNameAndDescription = True
    mDisplayName = NSLOCTEXT("", "511A77854C0A6EF78F070CBEBBAF5417", "Circuit Board")
    mDescription = NSLOCTEXT("", "CB39282E4A0D09DA7ACE2FBCD8F8D899", "Circuit Boards are advanced electronics that are used in a plethora of different ways.")
    mStackSize = EStackSize::SS_BIG
    mCanBeDiscarded = True
    mForm = EResourceForm::RF_SOLID
    mInventoryIcon = Namespace(DrawAs=3, ImageSize={'X': 64, 'Y': 64}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$Empty': True}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    mSmallIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/CircuitBoard/UI/IconDesc_CircuitBoard_64.IconDesc_CircuitBoard_64')
    mPersistentBigIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/CircuitBoard/UI/IconDesc_CircuitBoard_256.IconDesc_CircuitBoard_256')
    mConveyorMesh = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/CircuitBoard/SM_CircuitBoard.SM_CircuitBoard')
    mItemCategory = NewObject[Cat_Electronics]()
    mFluidDensity = 1
    mFluidViscosity = 1
    mFluidFriction = 0.10000000149011612
    
