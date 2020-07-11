
from codegen.ue4_stub import *

from Script.FactoryGame import FGItemDescriptor

class Desc_PackagedOil(FGItemDescriptor):
    mUseDisplayNameAndDescription = True
    mDisplayName = NSLOCTEXT("", "1BB51CE6457EB995DAA439BB3AAE5F3D", "Packaged Oil")
    mDescription = NSLOCTEXT("", "9E41918246BE996602118FBC57317A0D", "Crude Oil, packaged for transportation or to be used as vehicle fuel.")
    mStackSize = EStackSize::SS_MEDIUM
    mCanBeDiscarded = True
    mEnergyValue = 320
    mForm = EResourceForm::RF_SOLID
    mInventoryIcon = Namespace(DrawAs=3, ImageSize={'X': 64, 'Y': 64}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$Empty': True}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    mSmallIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/RawResources/CrudeOil/UI/Oil_64.Oil_64')
    mPersistentBigIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/RawResources/CrudeOil/UI/Oil_256.Oil_256')
    mConveyorMesh = Namespace(AssetPath='/Game/FactoryGame/Resource/RawResources/CrudeOil/Mesh/CrudeOilBarrel.CrudeOilBarrel')
    mItemCategory = NewObject[Cat_Packaging]()
    mFluidDensity = 1
    mFluidViscosity = 1
    mFluidFriction = 0.10000000149011612
    
