
from codegen.ue4_stub import *

from Script.FactoryGame import FGFactorySettings

class BP_FactorySettings(FGFactorySettings):
    mDefaultValidPlacementMaterial = Namespace(AssetPath='/Game/FactoryGame/Equipment/BuildGun/Material/HologramColor_Inst.HologramColor_Inst')
    mDefaultValidPlacementMaterialSimplified = Namespace(AssetPath='/Game/FactoryGame/Equipment/BuildGun/Material/Hologram_Blue_Inst.Hologram_Blue_Inst')
    mDefaultInvalidPlacementMaterial = Namespace(AssetPath='/Game/FactoryGame/Equipment/BuildGun/Material/Hologram_Red_Inst.Hologram_Red_Inst')
    mDefaultInputConnectionMaterial = Namespace(AssetPath='/Game/FactoryGame/Equipment/BuildGun/Material/Hologram_Simple_Transparent_Input.Hologram_Simple_Transparent_Input')
    mDefaultOutputConnectionMaterial = Namespace(AssetPath='/Game/FactoryGame/Equipment/BuildGun/Material/Hologram_Simple_Transparent_Output.Hologram_Simple_Transparent_Output')
    mDefaultNeutralConnectionMaterial = Namespace(AssetPath='/Game/FactoryGame/Equipment/BuildGun/Material/Hologram_Simple_White.Hologram_Simple_White')
    mDefaultPowerConnectionMaterial = Namespace(AssetPath='/Game/FactoryGame/Equipment/BuildGun/Material/Hologram_Simple_Power.Hologram_Simple_Power')
    mDefaultConveyorConnectionFrameMesh = Namespace(AssetPath='/Game/FactoryGame/Equipment/BuildGun/Mesh/Input.Input')
    mDefaultConveyorConnectionArrowMesh = Namespace(AssetPath='/Game/FactoryGame/Equipment/BuildGun/Mesh/Arrows.Arrows')
    mDefaultPipeConnectionFrameMesh = Namespace(AssetPath='/Game/FactoryGame/Equipment/BuildGun/Mesh/PipeFrame_Temp.PipeFrame_Temp')
    mDefaultPipeConnectionArrowMesh = Namespace(AssetPath='/Game/FactoryGame/Equipment/BuildGun/Mesh/Arrows.Arrows')
    mDefaultPowerConnectionMesh = Namespace(AssetPath='/Game/FactoryGame/Buildable/Factory/PowerLine/Mesh/PowerLineHologramMesh.PowerLineHologramMesh')
    mClearanceMesh = Namespace(AssetPath='/Game/FactoryGame/Equipment/BuildGun/Mesh/ClearanceBox.ClearanceBox')
    mClearanceMaterial = Namespace(AssetPath='/Game/FactoryGame/Equipment/BuildGun/Material/Clearance_Inst.Clearance_Inst')
    mHologramLoopSound = Namespace(AssetPath='/Game/FactoryGame/Buildable/-Shared/Audio/BuildEffect_2018-05/Hologram/Play_BuildEffect_Hologram_Loop.Play_BuildEffect_Hologram_Loop')
    mHologramSnapSound = Namespace(AssetPath='/Game/FactoryGame/Interface/UI/Audio/Hologram/Play_UI_Hologram_Snap.Play_UI_Hologram_Snap')
    mBuildGuideMesh = Namespace(AssetPath='/Game/FactoryGame/World/Environment/Background/mesh/BG_Plane.BG_Plane')
    mBuildGuideMaterial = Namespace(AssetPath='/Game/FactoryGame/Equipment/BuildGun/Material/Hologram_Simple_Output.Hologram_Simple_Output')
    mConveyorBuildGuideMaterial = Namespace(AssetPath='/Game/FactoryGame/Equipment/BuildGun/Material/Hologram_Simple_Output.Hologram_Simple_Output')
    mInventoryDropCrate = NewObject[BP_Crate]()
    mPowerShardClass = NewObject[Desc_CrystalShard]()
    mConstructionSounds = [{'$AssetPath': '/Game/FactoryGame/Buildable/Factory/ConveyorBeltMk1/Audio/Play_F_Construction_ConveyorHub.Play_F_Construction_ConveyorHub'}]
    mDismantleSounds = [{'$AssetPath': '/Game/FactoryGame/Buildable/-Shared/Audio/Dismantle/Play_UI_Dismantle_M.Play_UI_Dismantle_M'}]
    mBuildEffect = NewObject[BP_MaterialEffect_Build]()
    mDismantleEffect = NewObject[BP_MaterialEffect_Dismantle]()
    mDismantlePendingMaterial = Namespace(AssetPath='/Game/FactoryGame/Equipment/BuildGun/Material/Hologram_Input.Hologram_Input')
    mBuildGunClass = NewObject[BP_BuildGun]()
    mResourceScannerClass = NewObject[BP_ResourceScanner]()
    mResourceMinerClass = NewObject[Equip_ResourceMiner]()
    mLegMesh = Namespace(AssetPath='/Game/FactoryGame/Buildable/-Shared/SharedParts/Mesh/FactoryLeg.FactoryLeg')
    mFootMesh = Namespace(AssetPath='/Game/FactoryGame/Buildable/-Shared/SharedParts/Mesh/FactoryFoot_01.FactoryFoot_01')
    mMaxFeetLength = 300
    mRecipeShortcutClass = NewObject[FGRecipeShortcut]()
    mShortcutMap = ['Shortcut1', 'Shortcut2', 'Shortcut3', 'Shortcut4', 'Shortcut5', 'Shortcut6', 'Shortcut7', 'Shortcut8', 'Shortcut9', 'Shortcut10']
    mNumHotbars = 10
    mNumPresetHotbars = 10
    mNumSlotsPerHotbar = 10
    mFluidToInventoryStackRate = 10000
    mInventoryStackToFluidRate = 10000
    mAddedPipeProductionPressure = 10
    mViscosityToPuddlePairs = [{'Viscosity': 0, 'Puddle': 0}, {'Viscosity': 1, 'Puddle': 0.05999999865889549}, {'Viscosity': 2, 'Puddle': 0.10000000149011612}, {'Viscosity': 4, 'Puddle': 0.12999999523162842}, {'Viscosity': 5, 'Puddle': 0.1599999964237213}, {'Viscosity': 10, 'Puddle': 0.23000000417232513}, {'Viscosity': 100, 'Puddle': 0.46000000834465027}]
    
