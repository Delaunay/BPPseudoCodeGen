
from codegen.ue4_stub import *

from Script.FactoryGame import FGItemDescriptor

class Desc_AluminumPlateReinforced(FGItemDescriptor):
    mUseDisplayNameAndDescription = True
    mDisplayName = NSLOCTEXT("", "FA1193DC40A26DBB4660EBB8C7347684", "Heat Sink")
    mDescription = NSLOCTEXT("", "E3A7525949F9BD98BDB69DAEEDA0E654", "Used to dissipate heat faster.")
    mStackSize = EStackSize::SS_MEDIUM
    mCanBeDiscarded = True
    mForm = EResourceForm::RF_SOLID
    mInventoryIcon = Namespace(DrawAs=3, ImageSize={'X': 64, 'Y': 64}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$Empty': True}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    mSmallIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/HeatSink/UI/IconDesc_Heatsink_64.IconDesc_Heatsink_64')
    mPersistentBigIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/HeatSink/UI/IconDesc_Heatsink_256.IconDesc_Heatsink_256')
    mConveyorMesh = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/HeatSink/SM_HeatSink_01.SM_HeatSink_01')
    mItemCategory = NewObject[Cat_IndustrialParts]()
    mFluidDensity = 1
    mFluidViscosity = 1
    mFluidFriction = 0.10000000149011612
    
