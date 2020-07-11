
from codegen.ue4_stub import *

from Script.FactoryGame import FGItemDescriptor

class Desc_GoldIngot(FGItemDescriptor):
    mUseDisplayNameAndDescription = True
    mDisplayName = NSLOCTEXT("", "8B425C07441CF895344B6DBC5449741C", "Caterium Ingot")
    mDescription = NSLOCTEXT("", "0F9C1FC74F5888A4C664888E733A7F70", "Caterium Ingots are smelted from Caterium Ore. Caterium Ingots are mostly used for advanced electronics.")
    mStackSize = EStackSize::SS_MEDIUM
    mCanBeDiscarded = True
    mForm = EResourceForm::RF_SOLID
    mInventoryIcon = Namespace(DrawAs=3, ImageSize={'X': 64, 'Y': 64}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$AssetPath': '/Game/FactoryGame/Resource/Parts/GoldIngot/UI/M_GoldIngot_Icon.M_GoldIngot_Icon'}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    mSmallIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/GoldIngot/UI/IconDesc_CateriumIngot_64.IconDesc_CateriumIngot_64')
    mPersistentBigIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/GoldIngot/UI/IconDesc_CateriumIngot_256.IconDesc_CateriumIngot_256')
    mConveyorMesh = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/CateriumIngot/Mesh/SM_CateriumIngot_01.SM_CateriumIngot_01')
    mItemCategory = NewObject[Cat_Ingots]()
    mFluidDensity = 1
    mFluidViscosity = 1
    mFluidFriction = 0.10000000149011612
    
