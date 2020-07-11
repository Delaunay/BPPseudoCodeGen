
from codegen.ue4_stub import *

from Script.FactoryGame import FGSchematic

class Research_Sulfur_3_1(FGSchematic):
    mType = ESchematicType::EST_MAM
    mDisplayName = NSLOCTEXT("", "88537E2F4D5BC426F35939B4109657AA", "Nobelisk Detonator")
    mSchematicCategory = NewObject[SC_Organisation]()
    mTechTier = 3
    mCost = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/SteelPlateReinforced/Desc_SteelPlateReinforced.Desc_SteelPlateReinforced_C', 'amount': 10}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/Cable/Desc_Cable.Desc_Cable_C', 'amount': 100}, {'ItemClass': '/Game/FactoryGame/Resource/Equipment/GemstoneScanner/BP_EquipmentDescriptorObjectScanner.BP_EquipmentDescriptorObjectScanner_C', 'amount': 5}]
    mTimeToComplete = 180
    mUnlocks = [{'$ObjectClass': '/Game/FactoryGame/Unlocks/BP_UnlockRecipe.BP_UnlockRecipe_C', '$ObjectFlags': 2621481, '$ObjectName': 'BP_UnlockRecipe_C_0', 'mRecipes': ['/Game/FactoryGame/Recipes/Equipment/Recipe_NobeliskDetonator.Recipe_NobeliskDetonator_C']}]
    mSchematicIcon = Namespace(DrawAs=3, ImageSize={'X': 64, 'Y': 64}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$AssetPath': '/Game/FactoryGame/Resource/Equipment/NobeliskDetonator/UI/Detonator_64.Detonator_64'}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    
