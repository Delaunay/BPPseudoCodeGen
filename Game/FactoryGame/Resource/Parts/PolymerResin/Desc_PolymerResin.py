
from codegen.ue4_stub import *

from Script.FactoryGame import FGItemDescriptor

class Desc_PolymerResin(FGItemDescriptor):
    mUseDisplayNameAndDescription = True
    mDisplayName = NSLOCTEXT("", "776D2EEA4983B05859810D95304ACF0D", "Polymer Resin")
    mDescription = NSLOCTEXT("", "8B31AE304BD87335DE5CD98DCDD08AFC", "Used for crafting.\r\nA by-product of oil refinement into fuel. Commonly used to manufacture plastics.")
    mStackSize = EStackSize::SS_BIG
    mCanBeDiscarded = True
    mForm = EResourceForm::RF_SOLID
    mInventoryIcon = Namespace(DrawAs=3, ImageSize={'X': 64, 'Y': 64}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$Empty': True}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    mSmallIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/PolymerResin/UI/IconDesc_PolymerResin_64.IconDesc_PolymerResin_64')
    mPersistentBigIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/PolymerResin/UI/IconDesc_PolymerResin_256.IconDesc_PolymerResin_256')
    mConveyorMesh = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/PolymerResin/SM_PolymerResin_01.SM_PolymerResin_01')
    mItemCategory = NewObject[Cat_SolidOilProducts]()
    mFluidDensity = 1
    mFluidViscosity = 1
    mFluidFriction = 0.10000000149011612
    
