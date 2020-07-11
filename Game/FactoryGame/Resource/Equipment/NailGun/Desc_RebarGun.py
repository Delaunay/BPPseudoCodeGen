
from codegen.ue4_stub import *

from Script.FactoryGame import FGEquipmentDescriptor

class Desc_RebarGun(FGEquipmentDescriptor):
    mEquipmentClass = NewObject[Equip_RebarGun_Projectile]()
    mUseDisplayNameAndDescription = True
    mDisplayName = NSLOCTEXT("", "D733F8FF49B4FD2F7A7CA0B93FB2963F", "Rebar Gun (OLD)")
    mDescription = NSLOCTEXT("", "050E8DA14B719E9001A777A73F0E8AEA", "The Rebar Gun is an improvised weapon, used to protect yourself from dangerous wildlife.")
    mCanBeDiscarded = True
    mForm = EResourceForm::RF_SOLID
    mInventoryIcon = Namespace(DrawAs=3, ImageSize={'X': 64, 'Y': 64}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$Empty': True}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    mSmallIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Equipment/NailGun/UI/RebarGun_64.RebarGun_64')
    mPersistentBigIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Equipment/NailGun/UI/RebarGun_256.RebarGun_256')
    mConveyorMesh = Namespace(AssetPath='/Game/FactoryGame/Equipment/RebarGun/Mesh/RebarGun_GroundMesh.RebarGun_GroundMesh')
    mPreviewView = Namespace(CameraPitch=-35, Distance=200, FocalOffset={'X': 0, 'Y': 0, 'Z': 20})
    mItemCategory = NewObject[Cat_Hands]()
    mFluidDensity = 1
    mFluidViscosity = 1
    mFluidFriction = 0.10000000149011612
    
