
from codegen.ue4_stub import *

from Script.FactoryGame import FGSchematic

class Schematic_4-4(FGSchematic):
    mType = ESchematicType::EST_Milestone
    mDisplayName = NSLOCTEXT("", "4A5E48404B1F9CADDE644288CC2E6AE8", "Hyper Tubes")
    mSchematicCategory = NewObject[SC_Logistics]()
    mTechTier = 4
    mCost = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/CopperSheet/Desc_CopperSheet.Desc_CopperSheet_C', 'amount': 300}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/SteelPipe/Desc_SteelPipe.Desc_SteelPipe_C', 'amount': 300}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/SteelPlateReinforced/Desc_SteelPlateReinforced.Desc_SteelPlateReinforced_C', 'amount': 50}]
    mUnlocks = [{'$ObjectClass': '/Game/FactoryGame/Unlocks/BP_UnlockRecipe.BP_UnlockRecipe_C', '$ObjectFlags': 2621440, '$ObjectName': 'BP_UnlockRecipe_C_0', 'mRecipes': ['/Game/FactoryGame/Recipe_PipeHyperStart.Recipe_PipeHyperStart_C', '/Game/FactoryGame/Recipes/Buildings/Recipe_PipeHyper.Recipe_PipeHyper_C', '/Game/FactoryGame/Recipes/Buildings/Recipe_PipeHyperSupport.Recipe_PipeHyperSupport_C', '/Game/FactoryGame/Recipes/Buildings/Recipe_HyperPoleStackable.Recipe_HyperPoleStackable_C']}]
    mSchematicIcon = Namespace(DrawAs=3, ImageSize={'X': 256, 'Y': 256}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$AssetPath': '/Game/FactoryGame/Buildable/Factory/TradingPost/UI/SchematicIcons/SchematicIcon_Logistics.SchematicIcon_Logistics'}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    
