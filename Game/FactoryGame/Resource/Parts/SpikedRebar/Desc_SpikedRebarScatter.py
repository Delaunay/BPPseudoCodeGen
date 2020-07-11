
from codegen.ue4_stub import *

from Script.FactoryGame import FGItemDescriptor

class Desc_SpikedRebarScatter(FGItemDescriptor):
    mUseDisplayNameAndDescription = True
    mDisplayName = NSLOCTEXT("", "1144413542FBCA88801AB188F70C4851", "Scatter Rebar")
    mDescription = NSLOCTEXT("", "7758716F475C03E7B8F255B5FF974FA0", "Ammo for the Rebar Scatter Gun.")
    mStackSize = EStackSize::SS_SMALL
    mCanBeDiscarded = True
    mForm = EResourceForm::RF_SOLID
    mInventoryIcon = Namespace(DrawAs=3, ImageSize={'X': 64, 'Y': 64}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$Empty': True}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    mSmallIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/SpikedRebar/UI/IconDesc_SpikedRebar_64.IconDesc_SpikedRebar_64')
    mPersistentBigIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/SpikedRebar/UI/IconDesc_SpikedRebar_256.IconDesc_SpikedRebar_256')
    mConveyorMesh = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/SpikedRebar/Mesh/SM_NailgunSpike_01.SM_NailgunSpike_01')
    mItemCategory = NewObject[Cat_Equipment]()
    mFluidDensity = 1
    mFluidViscosity = 1
    mFluidFriction = 0.10000000149011612
    
