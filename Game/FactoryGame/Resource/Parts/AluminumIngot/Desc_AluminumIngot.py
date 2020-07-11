
from codegen.ue4_stub import *

from Script.FactoryGame import FGItemDescriptor

class Desc_AluminumIngot(FGItemDescriptor):
    mUseDisplayNameAndDescription = True
    mDisplayName = NSLOCTEXT("", "6FF55ACD4D36160D3A245FA501C4C0C9", "Aluminum Ingot")
    mDescription = NSLOCTEXT("", "1F87FAC04915863A286AE2AEAF03E2AB", "Aluminum Ingots are made from Aluminum Scrap. It is mostly used to produce specialized aluminum-based parts.")
    mStackSize = EStackSize::SS_MEDIUM
    mCanBeDiscarded = True
    mForm = EResourceForm::RF_SOLID
    mInventoryIcon = Namespace(DrawAs=3, ImageSize={'X': 64, 'Y': 64}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$Empty': True}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    mSmallIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/AluminumIngot/UI/IconDesc_AluminiumIngot_64.IconDesc_AluminiumIngot_64')
    mPersistentBigIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/AluminumIngot/UI/IconDesc_AluminiumIngot_256.IconDesc_AluminiumIngot_256')
    mConveyorMesh = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/AluminumIngot/Mesh/SM_AluminumIngot_01.SM_AluminumIngot_01')
    mItemCategory = NewObject[Cat_Ingots]()
    mFluidDensity = 1
    mFluidViscosity = 1
    mFluidFriction = 0.10000000149011612
    
