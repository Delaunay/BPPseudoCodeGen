
from codegen.ue4_stub import *

from Script.FactoryGame import FGEquipmentDescriptor

class BP_EquipmentDescriptorObjectScanner(FGEquipmentDescriptor):
    mEquipmentClass = NewObject[Equip_ObjectScanner]()
    mUseDisplayNameAndDescription = True
    mDisplayName = NSLOCTEXT("", "5BBA7C5C4BCACB8002AFC2A831A49C0C", "Object Scanner")
    mDescription = NSLOCTEXT("", "19C6CB9F4B6B2BE78BACB68E911758EC", "Slot: Hands\r\n\r\nScans the area for a set item. Beeps at a rate proportional to proximity and direction.")
    mCanBeDiscarded = True
    mForm = EResourceForm::RF_SOLID
    mInventoryIcon = Namespace(DrawAs=3, ImageSize={'X': 64, 'Y': 64}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$Empty': True}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    mSmallIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Equipment/GemstoneScanner/UI/ObjectScanner_64.ObjectScanner_64')
    mPersistentBigIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Equipment/GemstoneScanner/UI/ObjectScanner_256.ObjectScanner_256')
    mConveyorMesh = Namespace(AssetPath='/Game/FactoryGame/Equipment/ObjectScanner/Mesh/CrystalScanner.CrystalScanner')
    mPreviewView = Namespace(CameraPitch=-25, Distance=200, FocalOffset={'X': 0, 'Y': 0, 'Z': 50})
    mItemCategory = NewObject[Cat_Hands]()
    mFluidDensity = 1
    mFluidViscosity = 1
    mFluidFriction = 0.10000000149011612
    
