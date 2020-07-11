
from codegen.ue4_stub import *

from Script.FactoryGame import FGSchematic

class Schematic_2-2(FGSchematic):
    mType = ESchematicType::EST_Milestone
    mDisplayName = NSLOCTEXT("", "29DB4E1B4D981AC88B0750A53C04AC32", "Obstacle Clearing")
    mSchematicCategory = NewObject[SC_Logistics]()
    mTechTier = 2
    mCost = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/IronScrew/Desc_IronScrew.Desc_IronScrew_C', 'amount': 500}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/Cable/Desc_Cable.Desc_Cable_C', 'amount': 100}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/Cement/Desc_Cement.Desc_Cement_C', 'amount': 100}]
    mTimeToComplete = 180
    mUnlocks = [{'$ObjectClass': '/Game/FactoryGame/Unlocks/BP_UnlockRecipe.BP_UnlockRecipe_C', '$ObjectFlags': 2621440, '$ObjectName': 'BP_UnlockRecipe_C_0', 'mRecipes': ['/Game/FactoryGame/Recipes/Equipment/Recipe_Chainsaw.Recipe_Chainsaw_C', '/Game/FactoryGame/Recipes/Constructor/Recipe_Biofuel.Recipe_Biofuel_C']}, {'$ObjectClass': '/Game/FactoryGame/Unlocks/BP_UnlockInventorySlot.BP_UnlockInventorySlot_C', '$ObjectFlags': 2621440, '$ObjectName': 'BP_UnlockInventorySlot_C_0', 'mNumInventorySlotsToUnlock': 5}]
    mSchematicIcon = Namespace(DrawAs=3, ImageSize={'X': 256, 'Y': 256}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$AssetPath': '/Game/FactoryGame/Buildable/Factory/TradingPost/UI/SchematicIcons/SchematicIcon_Equipment.SchematicIcon_Equipment'}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    
