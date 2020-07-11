
from codegen.ue4_stub import *

from Script.FactoryGame import FGSchematic

class Schematic_2-3(FGSchematic):
    mType = ESchematicType::EST_Milestone
    mDisplayName = NSLOCTEXT("", "ECD747574C6AE7670BDD7DAB7F41989E", "Jump Pads")
    mSchematicCategory = NewObject[SC_Logistics]()
    mTechTier = 2
    mCost = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/Rotor/Desc_Rotor.Desc_Rotor_C', 'amount': 50}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/IronPlate/Desc_IronPlate.Desc_IronPlate_C', 'amount': 300}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/Cable/Desc_Cable.Desc_Cable_C', 'amount': 150}]
    mTimeToComplete = 240
    mUnlocks = [{'$ObjectClass': '/Game/FactoryGame/Unlocks/BP_UnlockRecipe.BP_UnlockRecipe_C', '$ObjectFlags': 2621440, '$ObjectName': 'BP_UnlockRecipe_C_0', 'mRecipes': ['/Game/FactoryGame/Recipes/Buildings/Recipe_JumpPad.Recipe_JumpPad_C', '/Game/FactoryGame/Recipes/Buildings/Recipe_JumpPadTilted.Recipe_JumpPadTilted_C', '/Game/FactoryGame/Recipes/Buildings/Recipe_UJellyLandingPad.Recipe_UJellyLandingPad_C']}]
    mSchematicIcon = Namespace(DrawAs=3, ImageSize={'X': 256, 'Y': 256}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$AssetPath': '/Game/FactoryGame/Buildable/Factory/TradingPost/UI/SchematicIcons/SchematicIcon_Logistics.SchematicIcon_Logistics'}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    
