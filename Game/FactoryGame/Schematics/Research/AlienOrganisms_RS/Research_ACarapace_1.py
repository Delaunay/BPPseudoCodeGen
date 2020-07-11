
from codegen.ue4_stub import *

from Script.FactoryGame import FGSchematic

class Research_ACarapace_1(FGSchematic):
    mType = ESchematicType::EST_MAM
    mDisplayName = NSLOCTEXT("", "E844ACCD4F83DE5B9464FD8638F45212", "Structural Analysis")
    mSchematicCategory = NewObject[SC_Organisation]()
    mTechTier = 3
    mCost = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/AnimalParts/Desc_HogParts.Desc_HogParts_C', 'amount': 10}]
    mTimeToComplete = 3
    mUnlocks = [{'$ObjectClass': '/Game/FactoryGame/Unlocks/BP_UnlockRecipe.BP_UnlockRecipe_C', '$ObjectFlags': 2621481, '$ObjectName': 'BP_UnlockRecipe_C_0', 'mRecipes': ['/Game/FactoryGame/Recipes/Constructor/Recipe_Biomass_AlienCarapace.Recipe_Biomass_AlienCarapace_C']}]
    mSchematicIcon = Namespace(DrawAs=3, ImageSize={'X': 64, 'Y': 64}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$AssetPath': '/Game/FactoryGame/Resource/Parts/GenericBiomass/UI/IconDesc_Biomass_Final_64.IconDesc_Biomass_Final_64'}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    
