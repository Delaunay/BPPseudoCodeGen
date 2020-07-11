
from codegen.ue4_stub import *

from Script.FactoryGame import FGSchematic

class Research_Caterium_5(FGSchematic):
    mType = ESchematicType::EST_MAM
    mDisplayName = NSLOCTEXT("", "F4FAE44B428CEC331770D5993299565A", "High Speed Connector")
    mSchematicCategory = NewObject[SC_Production]()
    mTechTier = 3
    mCost = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/HighSpeedWire/Desc_HighSpeedWire.Desc_HighSpeedWire_C', 'amount': 500}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/Plastic/Desc_Plastic.Desc_Plastic_C', 'amount': 50}]
    mTimeToComplete = 3
    mUnlocks = [{'$ObjectClass': '/Game/FactoryGame/Unlocks/BP_UnlockRecipe.BP_UnlockRecipe_C', '$ObjectFlags': 2621481, '$ObjectName': 'BP_UnlockRecipe_C_1', 'mRecipes': ['/Game/FactoryGame/Recipes/Manufacturer/Recipe_HighSpeedConnector.Recipe_HighSpeedConnector_C']}]
    mSchematicIcon = Namespace(DrawAs=3, ImageSize={'X': 64, 'Y': 64}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$AssetPath': '/Game/FactoryGame/Resource/Parts/HighSpeedConnector/UI/IconDesc_HighSpeedConnector_64.IconDesc_HighSpeedConnector_64'}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    
