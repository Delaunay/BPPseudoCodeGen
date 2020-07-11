
from codegen.ue4_stub import *

from Script.FactoryGame import FGItemDescriptor

class Desc_PackagedOilResidue(FGItemDescriptor):
    mUseDisplayNameAndDescription = True
    mDisplayName = NSLOCTEXT("", "0A380B0749E0D6BF5E65359BFDD859CD", "Packaged Heavy Oil Residue")
    mDescription = NSLOCTEXT("", "03BDFBB840FFAF6E603E0AA82CB354D5", "Heavy Oil Residue, packaged for alternative transport.")
    mStackSize = EStackSize::SS_MEDIUM
    mCanBeDiscarded = True
    mEnergyValue = 400
    mForm = EResourceForm::RF_SOLID
    mInventoryIcon = Namespace(DrawAs=3, ImageSize={'X': 64, 'Y': 64}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$Empty': True}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    mSmallIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/RawResources/CrudeOil/UI/OilResidue_64.OilResidue_64')
    mPersistentBigIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/RawResources/CrudeOil/UI/OilResidue_256.OilResidue_256')
    mConveyorMesh = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/HeavyOilResidue/SM_HeavyOilResidue_01.SM_HeavyOilResidue_01')
    mItemCategory = NewObject[Cat_Packaging]()
    mFluidDensity = 1
    mFluidViscosity = 1
    mFluidFriction = 0.10000000149011612
    
