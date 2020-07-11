
from codegen.ue4_stub import *

from Script.FactoryGame import FGSchematic

class Schematic_7-1(FGSchematic):
    mType = ESchematicType::EST_Milestone
    mDisplayName = NSLOCTEXT("", "F031CB7D42FEC13D54B7549E4FAAEA17", "Bauxite Refinement")
    mSchematicCategory = NewObject[SC_Logistics]()
    mTechTier = 7
    mCost = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/Motor/Desc_Motor.Desc_Motor_C', 'amount': 200}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/Computer/Desc_Computer.Desc_Computer_C', 'amount': 100}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/ModularFrameHeavy/Desc_ModularFrameHeavy.Desc_ModularFrameHeavy_C', 'amount': 100}]
    mTimeToComplete = 900
    mUnlocks = [{'$ObjectClass': '/Game/FactoryGame/Unlocks/BP_UnlockRecipe.BP_UnlockRecipe_C', '$ObjectFlags': 2621440, '$ObjectName': 'BP_UnlockRecipe_C_0', 'mRecipes': ['/Game/FactoryGame/Recipes/Buildings/Recipe_ConveyorBeltMk5.Recipe_ConveyorBeltMk5_C', '/Game/FactoryGame/Recipes/Buildings/Recipe_ConveyorLiftMk5.Recipe_ConveyorLiftMk5_C', '/Game/FactoryGame/Recipes/Constructor/Recipe_AluminumSheet.Recipe_AluminumSheet_C', '/Game/FactoryGame/Recipes/Smelter/Recipe_IngotAluminum.Recipe_IngotAluminum_C', '/Game/FactoryGame/Recipes/OilRefinery/Recipe_AluminumScrap.Recipe_AluminumScrap_C', '/Game/FactoryGame/Recipes/OilRefinery/Recipe_AluminaSolution.Recipe_AluminaSolution_C']}, {'$ObjectClass': '/Game/FactoryGame/Unlocks/BP_UnlockScannableResource.BP_UnlockScannableResource_C', '$ObjectFlags': 2621440, '$ObjectName': 'BP_UnlockScannableResource_C_0', 'mResourcesToAddToScanner': ['/Game/FactoryGame/Resource/RawResources/OreBauxite/Desc_OreBauxite.Desc_OreBauxite_C', '/Game/FactoryGame/Resource/RawResources/RawQuartz/Desc_RawQuartz.Desc_RawQuartz_C']}]
    mSchematicIcon = Namespace(DrawAs=3, ImageSize={'X': 256, 'Y': 256}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$AssetPath': '/Game/FactoryGame/Buildable/Factory/TradingPost/UI/SchematicIcons/SchematicIcon_Factory.SchematicIcon_Factory'}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    
