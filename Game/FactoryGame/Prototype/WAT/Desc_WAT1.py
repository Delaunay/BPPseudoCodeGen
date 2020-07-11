
from codegen.ue4_stub import *

from Script.FactoryGame import FGItemDescriptor

class Desc_WAT1(FGItemDescriptor):
    mUseDisplayNameAndDescription = True
    mDisplayName = NSLOCTEXT("", "FC15B62745B43D903BC8CCA3DB9727CF", "Somersloop WIP")
    mDescription = NSLOCTEXT("", "B98E4AF745D5703A912899980C8AA68C", "A strange alien thing with a mind-bending and somehow familiar shape.\r\nWORK IN PROGRESS\r\nANALYZING THIS WILL NOT GIVE YOU ANYTHING")
    mStackSize = EStackSize::SS_SMALL
    mCanBeDiscarded = True
    mRememberPickUp = True
    mForm = EResourceForm::RF_SOLID
    mInventoryIcon = Namespace(DrawAs=3, ImageSize={'X': 64, 'Y': 64}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$AssetPath': '/Game/FactoryGame/Prototype/WAT/UI/M_WAT1_Icon.M_WAT1_Icon'}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    mSmallIcon = Namespace(AssetPath='/Game/FactoryGame/Prototype/WAT/UI/Wat_1_64.Wat_1_64')
    mPersistentBigIcon = Namespace(AssetPath='/Game/FactoryGame/Prototype/WAT/UI/Wat_1_256.Wat_1_256')
    mConveyorMesh = Namespace(AssetPath='/Game/FactoryGame/World/Benefit/AlienArtifact/Mesh/AlienArtifact_01_static.AlienArtifact_01_static')
    mFluidDensity = 1
    mFluidViscosity = 1
    mFluidFriction = 0.10000000149011612
    
