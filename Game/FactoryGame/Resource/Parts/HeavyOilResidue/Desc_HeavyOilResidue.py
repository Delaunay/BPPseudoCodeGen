
from codegen.ue4_stub import *

from Script.FactoryGame import FGItemDescriptor

class Desc_HeavyOilResidue(FGItemDescriptor):
    mUseDisplayNameAndDescription = True
    mDisplayName = NSLOCTEXT("", "525EBF694736E14409B25C812DC88FA9", "Heavy Oil Residue")
    mDescription = NSLOCTEXT("", "0F03DD4E498B68E39CFC2FAD99C63E8B", "A by-product of Plastic and Rubber production. Can be further refined into Fuel and Petroleum Coke.")
    mStackSize = EStackSize::SS_FLUID
    mCanBeDiscarded = True
    mEnergyValue = 0.4000000059604645
    mForm = EResourceForm::RF_LIQUID
    mInventoryIcon = Namespace(DrawAs=3, ImageSize={'X': 64, 'Y': 64}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$Empty': True}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    mSmallIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/HeavyOilResidue/UI/IconDesc_LiquidHeavyOilResidue_Pipe_256.IconDesc_LiquidHeavyOilResidue_Pipe_256')
    mPersistentBigIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/HeavyOilResidue/UI/IconDesc_LiquidHeavyOilResidue_Pipe_512.IconDesc_LiquidHeavyOilResidue_Pipe_512')
    mConveyorMesh = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/HeavyOilResidue/SM_HeavyOilResidue_01.SM_HeavyOilResidue_01')
    mItemCategory = NewObject[Cat_Unpackaging]()
    mFluidDensity = 1
    mFluidViscosity = 6
    mFluidFriction = 0.10000000149011612
    mFluidColor = Namespace(A=255, B=120, G=45, R=109)
    
