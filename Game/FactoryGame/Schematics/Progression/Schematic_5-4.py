
from codegen.ue4_stub import *

from Script.FactoryGame import FGSchematic

class Schematic_5-4(FGSchematic):
    mType = ESchematicType::EST_Milestone
    mDisplayName = NSLOCTEXT("", "0B75D24A47191236FA324DB603D8015E", "Alternative Fluid Transport")
    mSchematicCategory = NewObject[SC_Logistics]()
    mTechTier = 5
    mCost = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/ModularFrameHeavy/Desc_ModularFrameHeavy.Desc_ModularFrameHeavy_C', 'amount': 25}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/Motor/Desc_Motor.Desc_Motor_C', 'amount': 100}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/Plastic/Desc_Plastic.Desc_Plastic_C', 'amount': 200}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/Wire/Desc_Wire.Desc_Wire_C', 'amount': 3000}]
    mTimeToComplete = 480
    mUnlocks = [{'$ObjectClass': '/Game/FactoryGame/Unlocks/BP_UnlockRecipe.BP_UnlockRecipe_C', '$ObjectFlags': 2621440, '$ObjectName': 'BP_UnlockRecipe_C_0', 'mRecipes': ['/Game/FactoryGame/Recipes/Buildings/Recipe_IndustrialTank.Recipe_IndustrialTank_C', '/Game/FactoryGame/Recipes/Constructor/Recipe_FluidCanister.Recipe_FluidCanister_C', '/Game/FactoryGame/Recipes/OilRefinery/Recipe_PackagedWater.Recipe_PackagedWater_C', '/Game/FactoryGame/Recipes/OilRefinery/Recipe_PackagedCrudeOil.Recipe_PackagedCrudeOil_C', '/Game/FactoryGame/Recipes/OilRefinery/Recipe_Fuel.Recipe_Fuel_C', '/Game/FactoryGame/Recipes/OilRefinery/Recipe_PackagedOilResidue.Recipe_PackagedOilResidue_C', '/Game/FactoryGame/Recipes/OilRefinery/Recipe_PackagedBiofuel.Recipe_PackagedBiofuel_C', '/Game/FactoryGame/Recipes/OilRefinery/Recipe_LiquidBiofuel.Recipe_LiquidBiofuel_C']}, {'$ObjectClass': '/Game/FactoryGame/Unlocks/BP_UnlockSchematic.BP_UnlockSchematic_C', '$ObjectFlags': 2621481, '$ObjectName': 'BP_UnlockSchematic_C_0', 'mSchematics': ['/Game/FactoryGame/Schematics/Progression/Schematic_5-4-1.Schematic_5-4-1_C']}]
    mSchematicIcon = Namespace(DrawAs=3, ImageSize={'X': 256, 'Y': 256}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$AssetPath': '/Game/FactoryGame/Buildable/Factory/TradingPost/UI/SchematicIcons/SchematicIcon_Factory.SchematicIcon_Factory'}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    
