
from codegen.ue4_stub import *

from Script.FactoryGame import FGSchematic

class Research_Nutrients_4(FGSchematic):
    mType = ESchematicType::EST_MAM
    mDisplayName = NSLOCTEXT("", "6BD1C92441288A1508EDE2A8F1541AB3", "Nutritional Inhaler")
    mSchematicCategory = NewObject[SC_Organisation]()
    mTechTier = 3
    mCost = [{'ItemClass': '/Game/FactoryGame/Resource/Environment/DesertShroom/Desc_Shroom.Desc_Shroom_C', 'amount': 2}, {'ItemClass': '/Game/FactoryGame/Resource/Environment/Berry/Desc_Berry.Desc_Berry_C', 'amount': 4}, {'ItemClass': '/Game/FactoryGame/Resource/Environment/Nut/Desc_Nut.Desc_Nut_C', 'amount': 10}]
    mUnlocks = [{'$ObjectClass': '/Game/FactoryGame/Unlocks/BP_UnlockRecipe.BP_UnlockRecipe_C', '$ObjectFlags': 2621440, '$ObjectName': 'BP_UnlockRecipe_C_0', 'mRecipes': ['/Game/FactoryGame/Recipes/Equipment/Recipe_NutritionalInhaler.Recipe_NutritionalInhaler_C']}]
    mSchematicIcon = Namespace(DrawAs=3, ImageSize={'X': 64, 'Y': 64}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$AssetPath': '/Game/FactoryGame/Resource/Equipment/Medkit/UI/Inhaler_64.Inhaler_64'}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    
