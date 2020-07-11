
from codegen.ue4_stub import *

from Script.FactoryGame import FGEquipment
from Script.FactoryGame import GetEquipmentInSlot
from Script.FactoryGame import FGConsumableDescriptor
from Game.FactoryGame.Equipment.Beacon.Equip_Beacon import Equip_Beacon

class BP_EquipmentDescriptorBeacon(FGConsumableDescriptor):
    mCustomHandsMeshScale = 1
    mEquipmentClass = NewObject[Equip_Beacon]()
    mUseDisplayNameAndDescription = True
    mDisplayName = NSLOCTEXT("", "D64A527F44BA0A1595F8829AC513B6B9", "Beacon")
    mDescription = NSLOCTEXT("", "8CC28DA441D999C30FEB9EB76AAA849D", "Slot: Hands\r\nConsumable\r\n\r\nUsed to mark areas of interest. Displayed on your compass with the color and name you set for it.")
    mStackSize = EStackSize::SS_MEDIUM
    mCanBeDiscarded = True
    mForm = EResourceForm::RF_SOLID
    mInventoryIcon = Namespace(DrawAs=3, ImageSize={'X': 64, 'Y': 64}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$Empty': True}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    mSmallIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Equipment/Beacon/UI/IconDesc_Beacon_64.IconDesc_Beacon_64')
    mPersistentBigIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Equipment/Beacon/UI/IconDesc_Beacon_256.IconDesc_Beacon_256')
    mConveyorMesh = Namespace(AssetPath='/Game/FactoryGame/Equipment/Beacon/Mesh/Beacon_01.Beacon_01')
    mItemCategory = NewObject[Cat_Hands]()
    mFluidDensity = 1
    mFluidViscosity = 1
    mFluidFriction = 0.10000000149011612
    
    def ConsumedBy(self):
        ReturnValue: Ptr[FGEquipment] = Player.GetEquipmentInSlot(1)
        Beacon: Ptr[Equip_Beacon] = Cast[Equip_Beacon](ReturnValue)
        bSuccess: bool = Beacon
        if not bSuccess:
            goto('L159')
        Beacon.SpawnBeacon()
    
