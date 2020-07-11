
from codegen.ue4_stub import *

from Script.FactoryGame import FGItemDescriptor

class Desc_SteelIngot(FGItemDescriptor):
    mUseDisplayNameAndDescription = True
    mDisplayName = NSLOCTEXT("", "B949A9A742A017935CA85EADB0582AB5", "Steel Ingot")
    mDescription = NSLOCTEXT("", "FBE8B02F431AF078584653B023E302C6", "Steel Ingots are made from Iron Ore that\'s been smelted with Coal. They are made into several parts used in building construction.")
    mStackSize = EStackSize::SS_MEDIUM
    mCanBeDiscarded = True
    mForm = EResourceForm::RF_SOLID
    mInventoryIcon = Namespace(DrawAs=3, ImageSize={'X': 64, 'Y': 64}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$Empty': True}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    mSmallIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/SteelIngot/UI/IconDesc_SteelIngot_64.IconDesc_SteelIngot_64')
    mPersistentBigIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/SteelIngot/UI/IconDesc_SteelIngot_256.IconDesc_SteelIngot_256')
    mConveyorMesh = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/SteelIngot/SteelIngot.SteelIngot')
    mItemCategory = NewObject[Cat_Ingots]()
    mFluidDensity = 1
    mFluidViscosity = 1
    mFluidFriction = 0.10000000149011612
    
