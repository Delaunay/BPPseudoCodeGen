
from codegen.ue4_stub import *

from Script.FactoryGame import FGSchematic

class Schematic_3-1(FGSchematic):
    mType = ESchematicType::EST_Milestone
    mDisplayName = NSLOCTEXT("", "960136734A9C18A20AC899816D882265", "Coal Power")
    mSchematicCategory = NewObject[SC_Logistics]()
    mTechTier = 3
    mCost = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/IronPlateReinforced/Desc_IronPlateReinforced.Desc_IronPlateReinforced_C', 'amount': 150}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/Rotor/Desc_Rotor.Desc_Rotor_C', 'amount': 50}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/Cable/Desc_Cable.Desc_Cable_C', 'amount': 300}]
    mTimeToComplete = 480
    mUnlocks = [{'$ObjectClass': '/Game/FactoryGame/Unlocks/BP_UnlockRecipe.BP_UnlockRecipe_C', '$ObjectFlags': 2621440, '$ObjectName': 'BP_UnlockRecipe_C_0', 'mRecipes': ['/Game/FactoryGame/Recipes/Buildings/Recipe_GeneratorCoal.Recipe_GeneratorCoal_C', '/Game/FactoryGame/Recipes/Buildings/Recipe_WaterPump.Recipe_WaterPump_C', '/Game/FactoryGame/Recipes/Buildings/Recipe_Pipeline.Recipe_Pipeline_C', '/Game/FactoryGame/Recipes/Buildings/Recipe_PipeSupport.Recipe_PipeSupport_C', '/Game/FactoryGame/Recipes/Buildings/Recipe_PipelineJunction_Cross.Recipe_PipelineJunction_Cross_C', '/Game/FactoryGame/Recipes/Buildings/Recipe_PipelinePump.Recipe_PipelinePump_C', '/Game/FactoryGame/Recipes/Buildings/Recipe_PipeStorageTank.Recipe_PipeStorageTank_C']}, {'$ObjectClass': '/Game/FactoryGame/Unlocks/BP_UnlockScannableResource.BP_UnlockScannableResource_C', '$ObjectFlags': 2621440, '$ObjectName': 'BP_UnlockScannableResource_C_0', 'mResourcesToAddToScanner': ['/Game/FactoryGame/Resource/RawResources/Coal/Desc_Coal.Desc_Coal_C']}]
    mSchematicIcon = Namespace(DrawAs=3, ImageSize={'X': 256, 'Y': 256}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$AssetPath': '/Game/FactoryGame/Buildable/Factory/TradingPost/UI/SchematicIcons/SchematicIcon_Factory.SchematicIcon_Factory'}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    
