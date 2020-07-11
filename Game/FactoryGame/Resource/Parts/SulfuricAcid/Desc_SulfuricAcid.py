
from codegen.ue4_stub import *

from Script.FactoryGame import FGItemDescriptor

class Desc_SulfuricAcid(FGItemDescriptor):
    mUseDisplayNameAndDescription = True
    mDisplayName = NSLOCTEXT("", "CA74988A46F5712C299C4ABA4C7D35E3", "Sulfuric Acid")
    mDescription = NSLOCTEXT("", "9DD3C7BD407B7CD94B7A239D36F2099C", "A liquid mostly used to extract elements from ore.")
    mStackSize = EStackSize::SS_FLUID
    mCanBeDiscarded = True
    mForm = EResourceForm::RF_LIQUID
    mInventoryIcon = Namespace(DrawAs=3, ImageSize={'X': 64, 'Y': 64}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$Empty': True}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    mSmallIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/SulfuricAcid/UI/IconDesc_LiquidSulfuricAcid_Pipe_256.IconDesc_LiquidSulfuricAcid_Pipe_256')
    mPersistentBigIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/SulfuricAcid/UI/IconDesc_LiquidSulfuricAcid_Pipe_512.IconDesc_LiquidSulfuricAcid_Pipe_512')
    mConveyorMesh = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/HeavyOilResidue/SM_HeavyOilResidue_01.SM_HeavyOilResidue_01')
    mItemCategory = NewObject[Cat_AdvancedRefinement]()
    mFluidDensity = 1
    mFluidViscosity = 5
    mFluidFriction = 0.10000000149011612
    mFluidColor = Namespace(A=255, B=0, G=255, R=255)
    
