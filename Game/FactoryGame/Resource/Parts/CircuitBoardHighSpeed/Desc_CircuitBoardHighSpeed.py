
from codegen.ue4_stub import *

from Script.FactoryGame import FGItemDescriptor

class Desc_CircuitBoardHighSpeed(FGItemDescriptor):
    mUseDisplayNameAndDescription = True
    mDisplayName = NSLOCTEXT("", "C2BCAA9842DE092F082BF4A1442A4154", "A.I. Limiter")
    mDescription = NSLOCTEXT("", "C94FE50644881DBD5D510D8FE0E0F332", "A.I. Limiter are super advanced electronics that are used to control A.I.s and keep them from evolving in malicious ways.")
    mStackSize = EStackSize::SS_MEDIUM
    mCanBeDiscarded = True
    mForm = EResourceForm::RF_SOLID
    mInventoryIcon = Namespace(DrawAs=3, ImageSize={'X': 64, 'Y': 64}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$Empty': True}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    mSmallIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/AIlimiter/UI/IconDesc_AILimiter_64.IconDesc_AILimiter_64')
    mPersistentBigIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/AIlimiter/UI/IconDesc_AILimiter_256.IconDesc_AILimiter_256')
    mConveyorMesh = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/AIlimiter/Mesh/SM_AILimiter_01.SM_AILimiter_01')
    mItemCategory = NewObject[Cat_Electronics]()
    mFluidDensity = 1
    mFluidViscosity = 1
    mFluidFriction = 0.10000000149011612
    
