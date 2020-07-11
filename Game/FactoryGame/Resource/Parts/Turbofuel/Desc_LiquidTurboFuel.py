
from codegen.ue4_stub import *

from Script.FactoryGame import FGItemDescriptor

class Desc_LiquidTurboFuel(FGItemDescriptor):
    mUseDisplayNameAndDescription = True
    mDisplayName = NSLOCTEXT("", "EB0CE40E46333A5BE8975AAC61A3636C", "Turbofuel")
    mDescription = NSLOCTEXT("", "FFDC0A924B9BAFDC2EEC9B9BA9183E4D", "A more efficient alternative to Fuel. Used in Fuel Generators.")
    mStackSize = EStackSize::SS_FLUID
    mCanBeDiscarded = True
    mEnergyValue = 2
    mForm = EResourceForm::RF_LIQUID
    mInventoryIcon = Namespace(DrawAs=3, ImageSize={'X': 64, 'Y': 64}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$Empty': True}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    mSmallIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/Turbofuel/UI/IconDesc_LiquidTurboFuel_Pipe_256.IconDesc_LiquidTurboFuel_Pipe_256')
    mPersistentBigIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/Turbofuel/UI/IconDesc_LiquidTurboFuel_Pipe_512.IconDesc_LiquidTurboFuel_Pipe_512')
    mConveyorMesh = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/Turbofuel/SM_TurboFuel_01.SM_TurboFuel_01')
    mItemCategory = NewObject[Cat_Fuel]()
    mFluidDensity = 1
    mFluidViscosity = 5
    mFluidFriction = 0.10000000149011612
    mFluidColor = Namespace(A=255, B=46, G=41, R=212)
    
