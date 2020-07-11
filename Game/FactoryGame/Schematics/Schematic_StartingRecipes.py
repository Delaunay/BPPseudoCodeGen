
from codegen.ue4_stub import *

from Script.FactoryGame import FGSchematic

class Schematic_StartingRecipes(FGSchematic):
    mDisplayName = NSLOCTEXT("", "3F07675E42A29885006CC9881ACFD2FB", "Starting Blueprints")
    mSchematicCategory = NewObject[SC_Logistics]()
    mUnlocks = [{'$ObjectClass': '/Game/FactoryGame/Unlocks/BP_UnlockRecipe.BP_UnlockRecipe_C', '$ObjectFlags': 2621440, '$ObjectName': 'BP_UnlockRecipe_C_0', 'mRecipes': ['/Game/FactoryGame/Recipes/Smelter/Recipe_IngotIron.Recipe_IngotIron_C', '/Game/FactoryGame/Recipes/Constructor/Recipe_IronPlate.Recipe_IronPlate_C', '/Game/FactoryGame/Recipes/Constructor/Recipe_IronRod.Recipe_IronRod_C', '/Game/FactoryGame/Recipes/Buildings/Recipe_TradingPost.Recipe_TradingPost_C', '/Game/FactoryGame/Recipes/RawResources/Recipe_OreIron.Recipe_OreIron_C', '/Game/FactoryGame/Recipes/RawResources/Recipe_OreCopper.Recipe_OreCopper_C', '/Game/FactoryGame/Recipes/RawResources/Recipe_OreBauxite.Recipe_OreBauxite_C', '/Game/FactoryGame/Recipes/RawResources/Recipe_OreCaterium.Recipe_OreCaterium_C', '/Game/FactoryGame/Recipes/RawResources/Recipe_OreUranium.Recipe_OreUranium_C', '/Game/FactoryGame/Recipes/RawResources/Recipe_CrudeOil.Recipe_CrudeOil_C', '/Game/FactoryGame/Recipes/RawResources/Recipe_Sulfur.Recipe_Sulfur_C', '/Game/FactoryGame/Recipes/RawResources/Recipe_Limestone.Recipe_Limestone_C', '/Game/FactoryGame/Recipes/RawResources/Recipe_Coal.Recipe_Coal_C', '/Game/FactoryGame/Recipes/RawResources/Recipe_RawQuartz.Recipe_RawQuartz_C', '/Game/FactoryGame/Recipes/Equipment/Recipe_XenoZapper.Recipe_XenoZapper_C', '/Game/FactoryGame/Recipes/Buildings/Recipe_WorkBench.Recipe_WorkBench_C']}, {'$ObjectClass': '/Game/FactoryGame/Unlocks/BP_UnlockScannableResource.BP_UnlockScannableResource_C', '$ObjectFlags': 2621440, '$ObjectName': 'BP_UnlockScannableResource_C_0', 'mResourcesToAddToScanner': ['/Game/FactoryGame/Resource/RawResources/OreIron/Desc_OreIron.Desc_OreIron_C']}]
    
