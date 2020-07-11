
from codegen.ue4_stub import *

from Script.FactoryGame import FGItemDescriptor

class Desc_HighSpeedWire(FGItemDescriptor):
    mUseDisplayNameAndDescription = True
    mDisplayName = NSLOCTEXT("", "9FCE731045CC10AF1CD07EA14A80029A", "Quickwire")
    mDescription = NSLOCTEXT("", "BBE6E8764508790B419577AC82AF032B", "Caterium\'s high conductivity and resistance to corrosion makes it ideal for small, advanced electronics.")
    mStackSize = EStackSize::SS_HUGE
    mCanBeDiscarded = True
    mForm = EResourceForm::RF_SOLID
    mInventoryIcon = Namespace(DrawAs=3, ImageSize={'X': 64, 'Y': 64}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$Empty': True}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    mSmallIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/HighSpeedWire/UI/IconDesc_Quickwire_64.IconDesc_Quickwire_64')
    mPersistentBigIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/HighSpeedWire/UI/IconDesc_Quickwire_256.IconDesc_Quickwire_256')
    mConveyorMesh = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/QuickWire/SM_Quickwire_01.SM_Quickwire_01')
    mItemCategory = NewObject[Cat_Electronics]()
    mFluidDensity = 1
    mFluidViscosity = 1
    mFluidFriction = 0.10000000149011612
    
