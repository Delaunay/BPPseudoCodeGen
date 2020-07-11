
from codegen.ue4_stub import *

from Script.FactoryGame import FGEquipmentDescriptor

class BP_EquipmentDescriptorJumpingStilts(FGEquipmentDescriptor):
    mEquipmentClass = NewObject[Equip_JumpingStilts]()
    mUseDisplayNameAndDescription = True
    mDisplayName = NSLOCTEXT("", "A859FC5F49ADDCD3EAB6B39155EE5B28", "Blade Runners")
    mDescription = NSLOCTEXT("", "8E44CA5842FDE41C6B9D5BBC36E86EAF", "Slot: Body\r\n\r\nA exoskeleton for your lower legs that assist your movement, allowing you to sprint faster and jump higher.\r\nAlso dampens the impact of landing.")
    mCanBeDiscarded = True
    mForm = EResourceForm::RF_SOLID
    mInventoryIcon = Namespace(DrawAs=3, ImageSize={'X': 64, 'Y': 64}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$Empty': True}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    mSmallIcon = Namespace(AssetPath='/Game/FactoryGame/Equipment/JumpingStilts/UI/SprintingStilts_64.SprintingStilts_64')
    mPersistentBigIcon = Namespace(AssetPath='/Game/FactoryGame/Equipment/JumpingStilts/UI/SprintingStilts_256.SprintingStilts_256')
    mConveyorMesh = Namespace(AssetPath='/Game/FactoryGame/Equipment/JumpingStilts/Mesh/JumpingStilts_02.JumpingStilts_02')
    mItemCategory = NewObject[Cat_Body]()
    mFluidDensity = 1
    mFluidViscosity = 1
    mFluidFriction = 0.10000000149011612
    
