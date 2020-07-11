
from codegen.ue4_stub import *

from Script.FactoryGame import FGSchematic

class Schematic_5-3(FGSchematic):
    mType = ESchematicType::EST_Milestone
    mDisplayName = NSLOCTEXT("", "484BC5CE497683F511C5CC933D47FAA7", "Logistics Mk.3")
    mSchematicCategory = NewObject[SC_Logistics]()
    mTechTier = 4
    mCost = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/SteelPlate/Desc_SteelPlate.Desc_SteelPlate_C', 'amount': 200}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/SteelPipe/Desc_SteelPipe.Desc_SteelPipe_C', 'amount': 100}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/Cement/Desc_Cement.Desc_Cement_C', 'amount': 500}]
    mTimeToComplete = 300
    mUnlocks = [{'$ObjectClass': '/Game/FactoryGame/Unlocks/BP_UnlockRecipe.BP_UnlockRecipe_C', '$ObjectFlags': 2621440, '$ObjectName': 'BP_UnlockRecipe_C_0', 'mRecipes': ['/Game/FactoryGame/Recipes/Buildings/Recipe_StorageContainerMk2.Recipe_StorageContainerMk2_C', '/Game/FactoryGame/Recipes/Buildings/Recipe_ConveyorBeltMk3.Recipe_ConveyorBeltMk3_C', '/Game/FactoryGame/Recipes/Buildings/Recipe_ConveyorLiftMk3.Recipe_ConveyorLiftMk3_C', '/Game/FactoryGame/Recipes/Buildings/Recipe_PipeSupportStackable.Recipe_PipeSupportStackable_C']}]
    mSchematicIcon = Namespace(DrawAs=3, ImageSize={'X': 256, 'Y': 256}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$AssetPath': '/Game/FactoryGame/Buildable/Factory/TradingPost/UI/SchematicIcons/SchematicIcon_Logistics.SchematicIcon_Logistics'}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    
