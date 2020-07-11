
from codegen.ue4_stub import *

from Script.FactoryGame import FGSchematic

class Schematic_5-1(FGSchematic):
    mType = ESchematicType::EST_Milestone
    mDisplayName = NSLOCTEXT("", "5415C3E749C59B867C7CAF94A4116313", "Oil Processing")
    mSchematicCategory = NewObject[SC_Logistics]()
    mTechTier = 5
    mCost = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/Motor/Desc_Motor.Desc_Motor_C', 'amount': 50}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/SteelPlateReinforced/Desc_SteelPlateReinforced.Desc_SteelPlateReinforced_C', 'amount': 100}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/SteelPipe/Desc_SteelPipe.Desc_SteelPipe_C', 'amount': 500}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/CopperSheet/Desc_CopperSheet.Desc_CopperSheet_C', 'amount': 500}]
    mTimeToComplete = 720
    mUnlocks = [{'$ObjectClass': '/Game/FactoryGame/Unlocks/BP_UnlockRecipe.BP_UnlockRecipe_C', '$ObjectFlags': 2621440, '$ObjectName': 'BP_UnlockRecipe_C_0', 'mRecipes': ['/Game/FactoryGame/Recipes/Buildings/Recipe_OilPump.Recipe_OilPump_C', '/Game/FactoryGame/Recipes/Buildings/Recipe_OilRefinery.Recipe_OilRefinery_C', '/Game/FactoryGame/Recipes/OilRefinery/Recipe_Plastic.Recipe_Plastic_C', '/Game/FactoryGame/Recipes/OilRefinery/Recipe_Rubber.Recipe_Rubber_C', '/Game/FactoryGame/Recipes/OilRefinery/Recipe_LiquidFuel.Recipe_LiquidFuel_C', '/Game/FactoryGame/Recipes/OilRefinery/Recipe_PetroleumCoke.Recipe_PetroleumCoke_C', '/Game/FactoryGame/Recipes/Assembler/Recipe_CircuitBoard.Recipe_CircuitBoard_C']}, {'$ObjectClass': '/Game/FactoryGame/Unlocks/BP_UnlockScannableResource.BP_UnlockScannableResource_C', '$ObjectFlags': 2621440, '$ObjectName': 'BP_UnlockScannableResource_C_0', 'mResourcesToAddToScanner': ['/Game/FactoryGame/Resource/RawResources/CrudeOil/Desc_LiquidOil.Desc_LiquidOil_C']}, {'$ObjectClass': '/Game/FactoryGame/Unlocks/BP_UnlockSchematic.BP_UnlockSchematic_C', '$ObjectFlags': 2621481, '$ObjectName': 'BP_UnlockSchematic_C_0', 'mSchematics': ['/Game/FactoryGame/Schematics/Progression/Schematic_5-1-1.Schematic_5-1-1_C']}]
    mSchematicIcon = Namespace(DrawAs=3, ImageSize={'X': 256, 'Y': 256}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$AssetPath': '/Game/FactoryGame/Buildable/Factory/TradingPost/UI/SchematicIcons/SchematicIcon_Factory.SchematicIcon_Factory'}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    
