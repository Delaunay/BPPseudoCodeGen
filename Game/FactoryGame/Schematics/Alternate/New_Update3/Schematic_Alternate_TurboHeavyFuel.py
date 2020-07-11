
from codegen.ue4_stub import *

from Script.FactoryGame import FGSchematic

class Schematic_Alternate_TurboHeavyFuel(FGSchematic):
    mType = ESchematicType::EST_Alternate
    mDisplayName = NSLOCTEXT("", "BBAD21E14E5B53B573C4C8836F5831E2", "Alternate: Turbo Heavy Fuel")
    mSchematicCategory = NewObject[SC_Logistics]()
    mUnlocks = [{'$ObjectClass': '/Game/FactoryGame/Unlocks/BP_UnlockRecipe.BP_UnlockRecipe_C', '$ObjectFlags': 2621440, '$ObjectName': 'BP_UnlockRecipe_C_0', 'mRecipes': ['/Game/FactoryGame/Recipes/AlternateRecipes/New_Update3/Recipe_Alternate_TurboHeavyFuel.Recipe_Alternate_TurboHeavyFuel_C', '/Game/FactoryGame/Recipes/OilRefinery/Recipe_PackagedTurboFuel.Recipe_PackagedTurboFuel_C', '/Game/FactoryGame/Recipes/OilRefinery/Recipe_UnpackageTurboFuel.Recipe_UnpackageTurboFuel_C']}]
    mSchematicIcon = Namespace(DrawAs=3, ImageSize={'X': 256, 'Y': 256}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$AssetPath': '/Game/FactoryGame/Buildable/Factory/TradingPost/UI/SchematicIcons/SchematicIcon_MAM.SchematicIcon_MAM'}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    mSchematicDependencies = [{'$ObjectClass': '/Game/FactoryGame/AvailabilityDependencies/BP_SchematicPurchasedDependency.BP_SchematicPurchasedDependency_C', '$ObjectFlags': 2621440, '$ObjectName': 'BP_SchematicPurchasedDependency_C_0', 'mSchematics': ['/Game/FactoryGame/Schematics/Progression/Schematic_5-1.Schematic_5-1_C', '/Game/FactoryGame/Schematics/Alternate/Parts/Schematic_Alternate_EnrichedCoal.Schematic_Alternate_EnrichedCoal_C'], 'mRequireAllSchematicsToBePurchased': True}]
    mDependsOnSchematic = NewObject[Schematic_5-1]()
    mAdditionalSchematicDependencies = ['/Game/FactoryGame/Schematics/Alternate/Parts/Schematic_Alternate_EnrichedCoal.Schematic_Alternate_EnrichedCoal_C']
    
