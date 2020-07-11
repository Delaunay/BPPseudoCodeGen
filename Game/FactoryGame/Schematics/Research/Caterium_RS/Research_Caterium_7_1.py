
from codegen.ue4_stub import *

from Script.FactoryGame import FGSchematic

class Research_Caterium_7_1(FGSchematic):
    mType = ESchematicType::EST_MAM
    mDisplayName = NSLOCTEXT("", "70858A2F40A99C9A69E280A7460455F4", "Programmable Splitter")
    mSchematicCategory = NewObject[SC_Organisation]()
    mTechTier = 3
    mCost = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/ComputerSuper/Desc_ComputerSuper.Desc_ComputerSuper_C', 'amount': 50}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/ModularFrameHeavy/Desc_ModularFrameHeavy.Desc_ModularFrameHeavy_C', 'amount': 50}]
    mTimeToComplete = 480
    mUnlocks = [{'$ObjectClass': '/Game/FactoryGame/Unlocks/BP_UnlockRecipe.BP_UnlockRecipe_C', '$ObjectFlags': 2621481, '$ObjectName': 'BP_UnlockRecipe_C_1', 'mRecipes': ['/Game/FactoryGame/Recipes/Buildings/Recipe_ConveyorAttachmentSplitterProgrammable.Recipe_ConveyorAttachmentSplitterProgrammable_C']}]
    mSchematicIcon = Namespace(DrawAs=3, ImageSize={'X': 256, 'Y': 256}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$AssetPath': '/Game/FactoryGame/Buildable/Factory/CA_SplitterProgrammable/UI/ProgrammableSplitter_256.ProgrammableSplitter_256'}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    
