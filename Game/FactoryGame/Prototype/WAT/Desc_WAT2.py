
from codegen.ue4_stub import *

from Script.FactoryGame import FGItemDescriptor

class Desc_WAT2(FGItemDescriptor):
    mUseDisplayNameAndDescription = True
    mDisplayName = NSLOCTEXT("", "37F20CC4418DEE251D305B86E8D21C2E", "Mercer Sphere WIP")
    mDescription = NSLOCTEXT("", "5DC87CF14E98113D715E6280D184A734", "A Weird alien thing with an impossibly smooth surface.\r\nWORK IN PROGRESS\r\nANALYZING THIS WILL NOT GIVE YOU ANYTHING")
    mStackSize = EStackSize::SS_SMALL
    mCanBeDiscarded = True
    mRememberPickUp = True
    mForm = EResourceForm::RF_SOLID
    mInventoryIcon = Namespace(DrawAs=3, ImageSize={'X': 64, 'Y': 64}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$AssetPath': '/Game/FactoryGame/Prototype/WAT/UI/M_WAT2_Icon.M_WAT2_Icon'}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    mSmallIcon = Namespace(AssetPath='/Game/FactoryGame/Prototype/WAT/UI/Wat_2_64.Wat_2_64')
    mPersistentBigIcon = Namespace(AssetPath='/Game/FactoryGame/Prototype/WAT/UI/Wat_2_256.Wat_2_256')
    mConveyorMesh = Namespace(AssetPath='/Game/FactoryGame/World/Benefit/AlienArtifact/Mesh/AlienArtifact_03_static.AlienArtifact_03_static')
    mFluidDensity = 1
    mFluidViscosity = 1
    mFluidFriction = 0.10000000149011612
    
