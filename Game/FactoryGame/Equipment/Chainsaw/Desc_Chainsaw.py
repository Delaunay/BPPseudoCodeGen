
from codegen.ue4_stub import *

from Script.FactoryGame import FGEquipmentDescriptor

class Desc_Chainsaw(FGEquipmentDescriptor):
    mEquipmentClass = NewObject[Equip_Chainsaw]()
    mUseDisplayNameAndDescription = True
    mDisplayName = NSLOCTEXT("", "639C6BB0437832EBE3F0BAB28FC7D6A9", "Chainsaw")
    mDescription = NSLOCTEXT("", "CA524A04465A3187485FA8928B1F9FF7", "Slot: Hands\r\nFuel: Biofuel\r\n\r\nUsed to clear an area of flora that is too difficult to remove by hand.")
    mCanBeDiscarded = True
    mForm = EResourceForm::RF_SOLID
    mInventoryIcon = Namespace(DrawAs=3, ImageSize={'X': 64, 'Y': 64}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$AssetPath': '/Game/FactoryGame/Equipment/Chainsaw/UI/M_Chainsaw_Icon.M_Chainsaw_Icon'}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    mSmallIcon = Namespace(AssetPath='/Game/FactoryGame/Equipment/Chainsaw/UI/Chainsaw_64.Chainsaw_64')
    mPersistentBigIcon = Namespace(AssetPath='/Game/FactoryGame/Equipment/Chainsaw/UI/Chainsaw_256.Chainsaw_256')
    mConveyorMesh = Namespace(AssetPath='/Game/FactoryGame/Equipment/Chainsaw/Mesh/chainsaw_dropped.chainsaw_dropped')
    mPreviewView = Namespace(CameraPitch=-35, Distance=200, FocalOffset={'X': 0, 'Y': 0, 'Z': 1.2824821472167969})
    mItemCategory = NewObject[Cat_Hands]()
    mFluidDensity = 1
    mFluidViscosity = 1
    mFluidFriction = 0.10000000149011612
    
