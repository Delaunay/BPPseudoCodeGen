
from codegen.ue4_stub import *

from Script.FactoryGame import FGItemDescriptor

class Desc_AluminaSolution(FGItemDescriptor):
    mUseDisplayNameAndDescription = True
    mDisplayName = NSLOCTEXT("", "CB485FAD4BA45994F129E7A193C95676", "Alumina Solution")
    mDescription = NSLOCTEXT("", "0C60304E44A767A6BC383695637150BF", "Dissolved Alumina, extracted from Bauxite. Can be further refined into pure Aluminum.")
    mStackSize = EStackSize::SS_FLUID
    mCanBeDiscarded = True
    mForm = EResourceForm::RF_LIQUID
    mInventoryIcon = Namespace(DrawAs=3, ImageSize={'X': 64, 'Y': 64}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$Empty': True}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    mSmallIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/Alumina/UI/LiquidAlumina_Pipe_256.LiquidAlumina_Pipe_256')
    mPersistentBigIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/Alumina/UI/LiquidAlumina_Pipe_512.LiquidAlumina_Pipe_512')
    mConveyorMesh = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/HeavyOilResidue/SM_HeavyOilResidue_01.SM_HeavyOilResidue_01')
    mItemCategory = NewObject[Cat_AdvancedRefinement]()
    mFluidDensity = 1
    mFluidViscosity = 4
    mFluidFriction = 0.10000000149011612
    mFluidColor = Namespace(A=255, B=193, G=193, R=193)
    
