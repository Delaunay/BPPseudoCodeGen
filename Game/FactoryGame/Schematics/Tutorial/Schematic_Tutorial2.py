
from codegen.ue4_stub import *

from Script.FactoryGame import FGSchematic

class Schematic_Tutorial2(FGSchematic):
    mType = ESchematicType::EST_Tutorial
    mDisplayName = NSLOCTEXT("", "4287BE7543655085E3595AA0605C8E8D", "Hub Upgrade 3")
    mSchematicCategory = NewObject[SC_Logistics]()
    mCost = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/IronPlate/Desc_IronPlate.Desc_IronPlate_C', 'amount': 20}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/IronRod/Desc_IronRod.Desc_IronRod_C', 'amount': 20}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/Wire/Desc_Wire.Desc_Wire_C', 'amount': 20}]
    mUnlocks = [{'$ObjectClass': '/Game/FactoryGame/Unlocks/BP_UnlockRecipe.BP_UnlockRecipe_C', '$ObjectFlags': 2621440, '$ObjectName': 'BP_UnlockRecipe_C_0', 'mRecipes': ['/Game/FactoryGame/Recipes/Buildings/Recipe_ConstructorMk1.Recipe_ConstructorMk1_C', '/Game/FactoryGame/Recipes/Buildings/Recipe_PowerPoleMk1.Recipe_PowerPoleMk1_C', '/Game/FactoryGame/Recipes/Constructor/Recipe_Concrete.Recipe_Concrete_C', '/Game/FactoryGame/Recipes/Constructor/Recipe_Screw.Recipe_Screw_C', '/Game/FactoryGame/Recipes/Assembler/Recipe_IronPlateReinforced.Recipe_IronPlateReinforced_C']}, {'$ObjectClass': '/Game/FactoryGame/Unlocks/BP_UnlockScannableResource.BP_UnlockScannableResource_C', '$ObjectFlags': 2621440, '$ObjectName': 'BP_UnlockScannableResource_C_0', 'mResourcesToAddToScanner': ['/Game/FactoryGame/Resource/RawResources/Stone/Desc_Stone.Desc_Stone_C']}]
    mSchematicIcon = Namespace(DrawAs=3, ImageSize={'X': 256, 'Y': 256}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$AssetPath': '/Game/FactoryGame/Buildable/Factory/TradingPost/UI/SchematicIcons/SchematicIcon_Hub_2.SchematicIcon_Hub_2'}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    mSchematicDependencies = [{'$ObjectClass': '/Game/FactoryGame/AvailabilityDependencies/BP_SchematicPurchasedDependency.BP_SchematicPurchasedDependency_C', '$ObjectFlags': 2621440, '$ObjectName': 'BP_SchematicPurchasedDependency_C_0', 'mSchematics': ['/Game/FactoryGame/Schematics/Tutorial/Schematic_Tutorial1_5.Schematic_Tutorial1_5_C'], 'mRequireAllSchematicsToBePurchased': True}]
    mDependsOnSchematic = NewObject[Schematic_Tutorial1_5]()
    
