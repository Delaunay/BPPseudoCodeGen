
from codegen.ue4_stub import *

from Script.FactoryGame import FGSchematic

class Schematic_Alternate_CrystalOscillator(FGSchematic):
    mType = ESchematicType::EST_Alternate
    mDisplayName = NSLOCTEXT("", "E8D3D62F40EAD0692FAF4AAAAEB2CB3F", "Alternate: Insulated Crystal Oscillator")
    mSchematicCategory = NewObject[SC_Logistics]()
    mTechTier = 5
    mUnlocks = [{'$ObjectClass': '/Game/FactoryGame/Unlocks/BP_UnlockRecipe.BP_UnlockRecipe_C', '$ObjectFlags': 2621440, '$ObjectName': 'BP_UnlockRecipe_C_0', 'mRecipes': ['/Game/FactoryGame/Recipes/AlternateRecipes/Parts/Recipe_Alternate_CrystalOscillator.Recipe_Alternate_CrystalOscillator_C']}]
    mSchematicIcon = Namespace(DrawAs=3, ImageSize={'X': 256, 'Y': 256}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$AssetPath': '/Game/FactoryGame/Buildable/Factory/TradingPost/UI/SchematicIcons/SchematicIcon_MAM.SchematicIcon_MAM'}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    mSchematicDependencies = [{'$ObjectClass': '/Game/FactoryGame/AvailabilityDependencies/BP_SchematicPurchasedDependency.BP_SchematicPurchasedDependency_C', '$ObjectFlags': 2621440, '$ObjectName': 'BP_SchematicPurchasedDependency_C_0', 'mSchematics': ['/Game/FactoryGame/Schematics/Research/Quartz_RS/Research_Quartz_2.Research_Quartz_2_C', '/Game/FactoryGame/Schematics/Research/Caterium_RS/Research_Caterium_3.Research_Caterium_3_C', '/Game/FactoryGame/Schematics/Progression/Schematic_5-1.Schematic_5-1_C'], 'mRequireAllSchematicsToBePurchased': True}]
    mDependsOnSchematic = NewObject[Research_Quartz_2]()
    mAdditionalSchematicDependencies = ['/Game/FactoryGame/Schematics/Research/Caterium_RS/Research_Caterium_3.Research_Caterium_3_C', '/Game/FactoryGame/Schematics/Progression/Schematic_5-1.Schematic_5-1_C']
    
