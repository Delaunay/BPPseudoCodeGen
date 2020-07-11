
from codegen.ue4_stub import *

from Script.FactoryGame import FGSchematic

class Schematic_Alternate_FusedWire(FGSchematic):
    mType = ESchematicType::EST_Alternate
    mDisplayName = NSLOCTEXT("", "F2AB8E6A4B4F701A59CA72B8CB6D1BD2", "Alternate: Fused Wire")
    mSchematicCategory = NewObject[SC_Logistics]()
    mUnlocks = [{'$ObjectClass': '/Game/FactoryGame/Unlocks/BP_UnlockRecipe.BP_UnlockRecipe_C', '$ObjectFlags': 2621440, '$ObjectName': 'BP_UnlockRecipe_C_0', 'mRecipes': ['/Game/FactoryGame/Recipes/AlternateRecipes/New_Update3/Recipe_Alternate_FusedWire.Recipe_Alternate_FusedWire_C']}]
    mSchematicIcon = Namespace(DrawAs=3, ImageSize={'X': 256, 'Y': 256}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$AssetPath': '/Game/FactoryGame/Buildable/Factory/TradingPost/UI/SchematicIcons/SchematicIcon_MAM.SchematicIcon_MAM'}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    mSchematicDependencies = [{'$ObjectClass': '/Game/FactoryGame/AvailabilityDependencies/BP_SchematicPurchasedDependency.BP_SchematicPurchasedDependency_C', '$ObjectFlags': 2621440, '$ObjectName': 'BP_SchematicPurchasedDependency_C_0', 'mSchematics': ['/Game/FactoryGame/Schematics/Research/Caterium_RS/Research_Caterium_0.Research_Caterium_0_C'], 'mRequireAllSchematicsToBePurchased': True}]
    mDependsOnSchematic = NewObject[Research_Caterium_0]()
    
