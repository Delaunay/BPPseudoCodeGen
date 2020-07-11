
from codegen.ue4_stub import *

from Script.FactoryGame import FGSchematic

class Research_Caterium_7_2(FGSchematic):
    mType = ESchematicType::EST_MAM
    mDisplayName = NSLOCTEXT("", "F906F26E463661974EF263A871686875", "Geothermal Generator")
    mSchematicCategory = NewObject[SC_Production]()
    mTechTier = 3
    mCost = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/ComputerSuper/Desc_ComputerSuper.Desc_ComputerSuper_C', 'amount': 50}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/ModularFrameHeavy/Desc_ModularFrameHeavy.Desc_ModularFrameHeavy_C', 'amount': 50}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/Rubber/Desc_Rubber.Desc_Rubber_C', 'amount': 300}]
    mTimeToComplete = 480
    mUnlocks = [{'$ObjectClass': '/Game/FactoryGame/Unlocks/BP_UnlockRecipe.BP_UnlockRecipe_C', '$ObjectFlags': 2621481, '$ObjectName': 'BP_UnlockRecipe_C_1', 'mRecipes': ['/Game/FactoryGame/Recipes/Buildings/Recipe_GeneratorGeoThermal.Recipe_GeneratorGeoThermal_C']}, {'$ObjectClass': '/Game/FactoryGame/Unlocks/BP_UnlockScannableResource.BP_UnlockScannableResource_C', '$ObjectFlags': 2621481, '$ObjectName': 'BP_UnlockScannableResource_C_0', 'mResourcesToAddToScanner': ['/Game/FactoryGame/Resource/RawResources/Geyser/Desc_Geyser.Desc_Geyser_C']}]
    mSchematicIcon = Namespace(DrawAs=3, ImageSize={'X': 256, 'Y': 256}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$AssetPath': '/Game/FactoryGame/Buildable/Factory/GeneratorGeoThermal/UI/GeoThermalPowerGenerator_256.GeoThermalPowerGenerator_256'}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    
