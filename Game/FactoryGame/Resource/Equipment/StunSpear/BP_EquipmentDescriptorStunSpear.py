
from codegen.ue4_stub import *

from Script.FactoryGame import FGEquipmentDescriptor

class BP_EquipmentDescriptorStunSpear(FGEquipmentDescriptor):
    mEquipmentClass = NewObject[Equip_StunSpear]()
    mUseDisplayNameAndDescription = True
    mDisplayName = NSLOCTEXT("", "3289EB48445C6BA7432C5099A41FF905", "Xeno-Basher")
    mDescription = NSLOCTEXT("", "F45ECDE6468D3881C73C148F864E7DE0", "Slot: Hands\r\n\r\nHeavy electroshock self defense weapon for melee range.")
    mCanBeDiscarded = True
    mForm = EResourceForm::RF_SOLID
    mInventoryIcon = Namespace(DrawAs=3, ImageSize={'X': 64, 'Y': 64}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$Empty': True}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    mSmallIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Equipment/StunSpear/UI/ShockBaton_64.ShockBaton_64')
    mPersistentBigIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Equipment/StunSpear/UI/ShockBaton_256.ShockBaton_256')
    mConveyorMesh = Namespace(AssetPath='/Game/FactoryGame/Equipment/StunSpear/Mesh/StunSpear.StunSpear')
    mItemCategory = NewObject[Cat_Hands]()
    mFluidDensity = 1
    mFluidViscosity = 1
    mFluidFriction = 0.10000000149011612
    
