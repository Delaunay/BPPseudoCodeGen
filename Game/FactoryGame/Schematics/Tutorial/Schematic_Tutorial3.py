
from codegen.ue4_stub import *

from Script.FactoryGame import FGSchematic

class Schematic_Tutorial3(FGSchematic):
    mType = ESchematicType::EST_Tutorial
    mDisplayName = NSLOCTEXT("", "3993A77540BBEC3CAE09C1BD94EC6B4E", "Hub Upgrade 4")
    mSchematicCategory = NewObject[SC_Logistics]()
    mCost = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/IronPlate/Desc_IronPlate.Desc_IronPlate_C', 'amount': 75}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/Cable/Desc_Cable.Desc_Cable_C', 'amount': 20}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/Cement/Desc_Cement.Desc_Cement_C', 'amount': 10}]
    mUnlocks = [{'$ObjectClass': '/Game/FactoryGame/Unlocks/BP_UnlockRecipe.BP_UnlockRecipe_C', '$ObjectFlags': 2621440, '$ObjectName': 'BP_UnlockRecipe_C_0', 'mRecipes': ['/Game/FactoryGame/Recipes/Buildings/Recipe_ConveyorPole.Recipe_ConveyorPole_C', '/Game/FactoryGame/Recipes/Buildings/Recipe_ConveyorBeltMk1.Recipe_ConveyorBeltMk1_C']}, {'$ObjectClass': '/Game/FactoryGame/Unlocks/BP_UnlockInventorySlot.BP_UnlockInventorySlot_C', '$ObjectFlags': 2621440, '$ObjectName': 'BP_UnlockInventorySlot_C_0', 'mNumInventorySlotsToUnlock': 3}]
    mSchematicIcon = Namespace(DrawAs=3, ImageSize={'X': 256, 'Y': 256}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$AssetPath': '/Game/FactoryGame/Buildable/Factory/TradingPost/UI/SchematicIcons/SchematicIcon_Hub_3.SchematicIcon_Hub_3'}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    mSchematicDependencies = [{'$ObjectClass': '/Game/FactoryGame/AvailabilityDependencies/BP_SchematicPurchasedDependency.BP_SchematicPurchasedDependency_C', '$ObjectFlags': 2621440, '$ObjectName': 'BP_SchematicPurchasedDependency_C_0', 'mSchematics': ['/Game/FactoryGame/Schematics/Tutorial/Schematic_Tutorial2.Schematic_Tutorial2_C'], 'mRequireAllSchematicsToBePurchased': True}]
    mDependsOnSchematic = NewObject[Schematic_Tutorial2]()
    
