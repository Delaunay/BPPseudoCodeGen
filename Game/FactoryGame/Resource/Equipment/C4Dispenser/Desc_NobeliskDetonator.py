
from codegen.ue4_stub import *

from Script.FactoryGame import FGEquipmentDescriptor

class Desc_NobeliskDetonator(FGEquipmentDescriptor):
    mEquipmentClass = NewObject[Equip_C4Dispenser]()
    mUseDisplayNameAndDescription = True
    mDisplayName = NSLOCTEXT("", "D29EAB8D4D7A52F4F1CF1C89C1B2E8C2", "Nobelisk Detonator OUTDATED")
    mDescription = NSLOCTEXT("", "2E3CDBEE43F177AEA967DDBF9153836D", "Can be equiped in the hand-slot to place and detonate Nobelisks. Press the right-mouse button to detonate placed Nobelisks.")
    mCanBeDiscarded = True
    mForm = EResourceForm::RF_SOLID
    mInventoryIcon = Namespace(DrawAs=3, ImageSize={'X': 64, 'Y': 64}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$Empty': True}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    mConveyorMesh = Namespace(AssetPath='/Game/FactoryGame/Equipment/C4Dispenser/Mesh/C4Dispenser_01.C4Dispenser_01')
    mItemCategory = NewObject[Cat_Hands]()
    mFluidDensity = 1
    mFluidViscosity = 1
    mFluidFriction = 0.10000000149011612
    
