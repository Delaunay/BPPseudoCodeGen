
from codegen.ue4_stub import *

from Script.FactoryGame import FGItemDescriptor

class Desc_MotorLightweight(FGItemDescriptor):
    mUseDisplayNameAndDescription = True
    mDisplayName = NSLOCTEXT("", "6180060D4609F43DDDD5F7888441563A", "Turbo Motor")
    mDescription = NSLOCTEXT("", "5CDF490445B714424DDD75B86F7F1978", "The Turbo Motor is a more complex, and more powerful, version of the regular Motor.")
    mStackSize = EStackSize::SS_SMALL
    mCanBeDiscarded = True
    mForm = EResourceForm::RF_SOLID
    mInventoryIcon = Namespace(DrawAs=3, ImageSize={'X': 64, 'Y': 64}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$Empty': True}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    mSmallIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/TurboMotor/UI/IconDesc_TurboMotor_64.IconDesc_TurboMotor_64')
    mPersistentBigIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/TurboMotor/UI/IconDesc_TurboMotor_256.IconDesc_TurboMotor_256')
    mConveyorMesh = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/TurboMotor/SM_TurboMotor_01.SM_TurboMotor_01')
    mPreviewView = Namespace(CameraPitch=-35, Distance=50, FocalOffset={'X': 0, 'Y': 0, 'Z': 0})
    mItemCategory = NewObject[Cat_IndustrialParts]()
    mFluidDensity = 1
    mFluidViscosity = 1
    mFluidFriction = 0.10000000149011612
    
