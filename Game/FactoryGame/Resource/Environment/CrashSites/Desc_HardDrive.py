
from codegen.ue4_stub import *

from Script.FactoryGame import FGItemDescriptor

class Desc_HardDrive(FGItemDescriptor):
    mUseDisplayNameAndDescription = True
    mDisplayName = NSLOCTEXT("", "6BDEC8244A85F8D0BD62B5BEE653CC20", "Hard Drive")
    mDescription = NSLOCTEXT("", "391520F3449659FE5C3D249621EFD60E", "A hard drive with Ficsit data. Analyze it in the M.A.M. to salvage its contents.")
    mStackSize = EStackSize::SS_MEDIUM
    mCanBeDiscarded = True
    mRememberPickUp = True
    mForm = EResourceForm::RF_SOLID
    mInventoryIcon = Namespace(DrawAs=3, ImageSize={'X': 64, 'Y': 64}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$Empty': True}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    mSmallIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Environment/CrashSites/UI/HardDrive_64.HardDrive_64')
    mPersistentBigIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Environment/CrashSites/UI/HardDrive_256.HardDrive_256')
    mConveyorMesh = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/HardDrive/SM_HardDrive_01.SM_HardDrive_01')
    mFluidDensity = 1
    mFluidViscosity = 1
    mFluidFriction = 0.10000000149011612
    
