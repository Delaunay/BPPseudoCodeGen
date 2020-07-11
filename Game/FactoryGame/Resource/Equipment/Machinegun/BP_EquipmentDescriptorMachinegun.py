
from codegen.ue4_stub import *

from Script.FactoryGame import FGEquipmentDescriptor

class BP_EquipmentDescriptorMachinegun(FGEquipmentDescriptor):
    mEquipmentClass = NewObject[Equip_Machinegun]()
    mUseDisplayNameAndDescription = True
    mDisplayName = NSLOCTEXT("", "96ED88FE42CE333978B2F6A1385C4D3A", "Machinegun")
    mDescription = NSLOCTEXT("", "32367FF2445BECEFC6F785906E442DF3", "A deadly machinegun made for one thing - effective disposal of irritating wildlife.")
    mCanBeDiscarded = True
    mForm = EResourceForm::RF_SOLID
    mConveyorMesh = Namespace(AssetPath='/Game/FactoryGame/Resource/DefaultItemMesh.DefaultItemMesh')
    mItemCategory = NewObject[Cat_Hands]()
    mFluidDensity = 1
    mFluidViscosity = 1
    mFluidFriction = 0.10000000149011612
    
