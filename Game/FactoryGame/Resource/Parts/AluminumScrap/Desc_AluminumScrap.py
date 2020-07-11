
from codegen.ue4_stub import *

from Script.FactoryGame import FGItemDescriptor

class Desc_AluminumScrap(FGItemDescriptor):
    mUseDisplayNameAndDescription = True
    mDisplayName = NSLOCTEXT("", "56B3AE584ED98CAE58A2B8B4CB7CF337", "Aluminum Scrap")
    mDescription = NSLOCTEXT("", "A1AD3F7B4666DA06E6E6B39D50F3ABE2", "Aluminum Scrap is pure aluminum refined from Alumina. Can be smelted down to Aluminum Ingots for industrial usage.")
    mStackSize = EStackSize::SS_HUGE
    mCanBeDiscarded = True
    mForm = EResourceForm::RF_SOLID
    mInventoryIcon = Namespace(DrawAs=3, ImageSize={'X': 64, 'Y': 64}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$Empty': True}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    mSmallIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/AluminumScrap/UI/IconDesc_AluminiumScrap_64.IconDesc_AluminiumScrap_64')
    mPersistentBigIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/AluminumScrap/UI/IconDesc_AluminiumScrap_256.IconDesc_AluminiumScrap_256')
    mConveyorMesh = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/AluminumScrap/Mesh/SM_AluminiumScrap_01.SM_AluminiumScrap_01')
    mItemCategory = NewObject[Cat_AdvancedRefinement]()
    mFluidDensity = 1
    mFluidViscosity = 1
    mFluidFriction = 0.10000000149011612
    
