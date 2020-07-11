
from codegen.ue4_stub import *

from Script.FactoryGame import FGSchematic

class Research_Caterium_4_1_1(FGSchematic):
    mType = ESchematicType::EST_MAM
    mDisplayName = NSLOCTEXT("", "00A06FA7400F1753AE5F40B72FA5ED1D", "Smart Splitter")
    mSchematicCategory = NewObject[SC_Logistics]()
    mTechTier = 3
    mCost = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/CircuitBoardHighSpeed/Desc_CircuitBoardHighSpeed.Desc_CircuitBoardHighSpeed_C', 'amount': 10}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/IronPlateReinforced/Desc_IronPlateReinforced.Desc_IronPlateReinforced_C', 'amount': 50}]
    mTimeToComplete = 300
    mUnlocks = [{'$ObjectClass': '/Game/FactoryGame/Unlocks/BP_UnlockRecipe.BP_UnlockRecipe_C', '$ObjectFlags': 2621481, '$ObjectName': 'BP_UnlockRecipe_C_0', 'mRecipes': ['/Game/FactoryGame/Recipes/Buildings/Recipe_ConveyorAttachmentSplitterSmart.Recipe_ConveyorAttachmentSplitterSmart_C']}]
    mSchematicIcon = Namespace(DrawAs=3, ImageSize={'X': 256, 'Y': 256}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$AssetPath': '/Game/FactoryGame/Buildable/Factory/CA_SplitterSmart/UI/SmartSplitter_256.SmartSplitter_256'}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    
