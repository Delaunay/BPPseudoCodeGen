
from codegen.ue4_stub import *

from Script.FactoryGame import FGEquipmentDescriptor

class Desc_ToolBelt(FGEquipmentDescriptor):
    mEquipmentClass = NewObject[Equip_ToolBelt]()
    mUseDisplayNameAndDescription = True
    mDisplayName = NSLOCTEXT("", "EB2008EC40BC3AED4704C28272D56E7C", "Tool Belt")
    mDescription = NSLOCTEXT("", "3A88EF1A4646570484073B89C3D7AF2A", "This is a tool belt")
    mCanBeDiscarded = True
    mForm = EResourceForm::RF_SOLID
    mPersistentBigIcon = Namespace(AssetPath='/Game/FactoryGame/Equipment/JumpingStilts/UI/SprintingStilts_256.SprintingStilts_256')
    mConveyorMesh = Namespace(AssetPath='/Game/Geometry/Meshes/1M_Cube_Chamfer.1M_Cube_Chamfer')
    mFluidDensity = 1
    mFluidViscosity = 1
    mFluidFriction = 0.10000000149011612
    
