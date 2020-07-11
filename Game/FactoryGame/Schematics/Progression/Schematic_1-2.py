
from codegen.ue4_stub import *

from Script.FactoryGame import FGSchematic

class Schematic_1-2(FGSchematic):
    mType = ESchematicType::EST_Milestone
    mDisplayName = NSLOCTEXT("", "2659B1B34B3206C3D698248F8940F102", "Logistics")
    mSchematicCategory = NewObject[SC_Logistics]()
    mTechTier = 1
    mCost = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/IronPlate/Desc_IronPlate.Desc_IronPlate_C', 'amount': 150}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/IronRod/Desc_IronRod.Desc_IronRod_C', 'amount': 150}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/Wire/Desc_Wire.Desc_Wire_C', 'amount': 300}]
    mTimeToComplete = 240
    mUnlocks = [{'$ObjectClass': '/Game/FactoryGame/Unlocks/BP_UnlockRecipe.BP_UnlockRecipe_C', '$ObjectFlags': 2621440, '$ObjectName': 'BP_UnlockRecipe_C_0', 'mRecipes': ['/Game/FactoryGame/Recipes/Buildings/Recipe_ConveyorAttachmentSplitter.Recipe_ConveyorAttachmentSplitter_C', '/Game/FactoryGame/Recipes/Buildings/Recipe_ConveyorAttachmentMerger.Recipe_ConveyorAttachmentMerger_C', '/Game/FactoryGame/Recipes/Buildings/Recipe_ConveyorLiftMk1.Recipe_ConveyorLiftMk1_C']}, {'$ObjectClass': '/Game/FactoryGame/Unlocks/BP_UnlockBuildEfficiency.BP_UnlockBuildEfficiency_C', '$ObjectFlags': 2621440, '$ObjectName': 'BP_UnlockBuildEfficiency_C_0'}]
    mSchematicIcon = Namespace(DrawAs=3, ImageSize={'X': 256, 'Y': 256}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$AssetPath': '/Game/FactoryGame/Buildable/Factory/TradingPost/UI/SchematicIcons/SchematicIcon_Logistics.SchematicIcon_Logistics'}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    
