
from codegen.ue4_stub import *

from Script.FactoryGame import FGSchematic

class Schematic_Tutorial5(FGSchematic):
    mType = ESchematicType::EST_Tutorial
    mDisplayName = NSLOCTEXT("", "D300297A4EBDD512998D9E8E526D051C", "Hub Upgrade 6")
    mSchematicCategory = NewObject[SC_Logistics]()
    mCost = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/IronRod/Desc_IronRod.Desc_IronRod_C', 'amount': 100}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/IronPlate/Desc_IronPlate.Desc_IronPlate_C', 'amount': 100}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/Wire/Desc_Wire.Desc_Wire_C', 'amount': 100}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/Cement/Desc_Cement.Desc_Cement_C', 'amount': 50}]
    mUnlocks = [{'$ObjectClass': '/Game/FactoryGame/Unlocks/BP_UnlockRecipe.BP_UnlockRecipe_C', '$ObjectFlags': 2621440, '$ObjectName': 'BP_UnlockRecipe_C_0', 'mRecipes': ['/Game/FactoryGame/Recipes/Buildings/TowTruck/Recipe_SpaceElevator.Recipe_SpaceElevator_C', '/Game/FactoryGame/Recipes/Buildings/Recipe_GeneratorBiomass.Recipe_GeneratorBiomass_C', '/Game/FactoryGame/Recipes/Constructor/Recipe_Biomass_Wood.Recipe_Biomass_Wood_C', '/Game/FactoryGame/Recipes/Constructor/Recipe_Biomass_Leaves.Recipe_Biomass_Leaves_C']}]
    mSchematicIcon = Namespace(DrawAs=3, ImageSize={'X': 256, 'Y': 256}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$AssetPath': '/Game/FactoryGame/Buildable/Factory/TradingPost/UI/SchematicIcons/SchematicIcon_Hub_5.SchematicIcon_Hub_5'}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    mSchematicDependencies = [{'$ObjectClass': '/Game/FactoryGame/AvailabilityDependencies/BP_SchematicPurchasedDependency.BP_SchematicPurchasedDependency_C', '$ObjectFlags': 2621440, '$ObjectName': 'BP_SchematicPurchasedDependency_C_0', 'mSchematics': ['/Game/FactoryGame/Schematics/Tutorial/Schematic_Tutorial4.Schematic_Tutorial4_C'], 'mRequireAllSchematicsToBePurchased': True}]
    mDependsOnSchematic = NewObject[Schematic_Tutorial4]()
    
