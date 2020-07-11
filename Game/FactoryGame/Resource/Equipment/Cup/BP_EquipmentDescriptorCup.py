
from codegen.ue4_stub import *

from Script.FactoryGame import FGEquipmentDescriptor

class BP_EquipmentDescriptorCup(FGEquipmentDescriptor):
    mEquipmentClass = NewObject[Equip_Cup]()
    mUseDisplayNameAndDescription = True
    mDisplayName = NSLOCTEXT("", "BFE67C2B4617CC0E14E834A5CCC6DF82", "Cup")
    mDescription = NSLOCTEXT("", "C552AC8B43E804A53CED53A99F0A8EDE", "Slot: Hands\r\n\r\nStandard issue Cup for melee range.")
    mCanBeDiscarded = True
    mForm = EResourceForm::RF_SOLID
    mInventoryIcon = Namespace(DrawAs=3, ImageSize={'X': 64, 'Y': 64}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$Empty': True}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    mSmallIcon = Namespace(AssetPath='/Game/FactoryGame/Equipment/Cup/UI/CoffeeCup_64.CoffeeCup_64')
    mPersistentBigIcon = Namespace(AssetPath='/Game/FactoryGame/Equipment/Cup/UI/CoffeeCup_256.CoffeeCup_256')
    mConveyorMesh = Namespace(AssetPath='/Game/FactoryGame/Equipment/Cup/Mesh/SM_Cup.SM_Cup')
    mItemCategory = NewObject[Cat_Hands]()
    mFluidDensity = 1
    mFluidViscosity = 1
    mFluidFriction = 0.10000000149011612
    
