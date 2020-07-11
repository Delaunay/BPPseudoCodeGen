
from codegen.ue4_stub import *

from Script.FactoryGame import FGSchematic

class Schematic_5-4-1(FGSchematic):
    mDisplayName = NSLOCTEXT("", "8B53638544BE9723E7DC83A73916AF40", " Alternative Fluid Transport 2")
    mSchematicCategory = NewObject[SC_Logistics]()
    mTechTier = 5
    mUnlocks = [{'$ObjectClass': '/Game/FactoryGame/Unlocks/BP_UnlockRecipe.BP_UnlockRecipe_C', '$ObjectFlags': 2621440, '$ObjectName': 'BP_UnlockRecipe_C_0', 'mRecipes': ['/Game/FactoryGame/Recipes/OilRefinery/Recipe_UnpackageWater.Recipe_UnpackageWater_C', '/Game/FactoryGame/Recipes/OilRefinery/Recipe_UnpackageOil.Recipe_UnpackageOil_C', '/Game/FactoryGame/Recipes/OilRefinery/Recipe_UnpackageFuel.Recipe_UnpackageFuel_C', '/Game/FactoryGame/Recipes/OilRefinery/Recipe_UnpackageOilResidue.Recipe_UnpackageOilResidue_C', '/Game/FactoryGame/Recipes/OilRefinery/Recipe_UnpackageBioFuel.Recipe_UnpackageBioFuel_C']}]
    mSchematicIcon = Namespace(DrawAs=3, ImageSize={'X': 256, 'Y': 256}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$AssetPath': '/Game/FactoryGame/Buildable/Factory/TradingPost/UI/SchematicIcons/SchematicIcon_Factory.SchematicIcon_Factory'}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    
