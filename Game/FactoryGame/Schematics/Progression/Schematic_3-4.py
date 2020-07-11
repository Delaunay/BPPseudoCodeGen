
from codegen.ue4_stub import *

from Script.FactoryGame import FGSchematic

class Schematic_3-4(FGSchematic):
    mType = ESchematicType::EST_Milestone
    mDisplayName = NSLOCTEXT("", "F1AD308A4D4503E048AB9BAA075F4F15", "Basic Steel Production")
    mSchematicCategory = NewObject[SC_Logistics]()
    mTechTier = 3
    mCost = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/ModularFrame/Desc_ModularFrame.Desc_ModularFrame_C', 'amount': 50}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/Rotor/Desc_Rotor.Desc_Rotor_C', 'amount': 150}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/Cement/Desc_Cement.Desc_Cement_C', 'amount': 300}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/Wire/Desc_Wire.Desc_Wire_C', 'amount': 1000}]
    mTimeToComplete = 480
    mUnlocks = [{'$ObjectClass': '/Game/FactoryGame/Unlocks/BP_UnlockRecipe.BP_UnlockRecipe_C', '$ObjectFlags': 2621440, '$ObjectName': 'BP_UnlockRecipe_C_0', 'mRecipes': ['/Game/FactoryGame/Recipes/Buildings/Recipe_SmelterMk1.Recipe_SmelterMk1_C', '/Game/FactoryGame/Recipes/Smelter/Recipe_IngotSteel.Recipe_IngotSteel_C', '/Game/FactoryGame/Recipes/Constructor/Recipe_SteelBeam.Recipe_SteelBeam_C', '/Game/FactoryGame/Recipes/Constructor/Recipe_SteelPipe.Recipe_SteelPipe_C', '/Game/FactoryGame/Recipes/SpaceElevatorParts/Recipe_SpaceElevatorPart_2.Recipe_SpaceElevatorPart_2_C']}]
    mSchematicIcon = Namespace(DrawAs=3, ImageSize={'X': 256, 'Y': 256}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$AssetPath': '/Game/FactoryGame/Buildable/Factory/TradingPost/UI/SchematicIcons/SchematicIcon_Factory.SchematicIcon_Factory'}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    
