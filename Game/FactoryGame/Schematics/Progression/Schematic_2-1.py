
from codegen.ue4_stub import *

from Script.FactoryGame import FGSchematic

class Schematic_2-1(FGSchematic):
    mType = ESchematicType::EST_Milestone
    mDisplayName = NSLOCTEXT("", "927B71864356E6113A95A0842B5DA7FC", "Part Assembly")
    mSchematicCategory = NewObject[SC_Logistics]()
    mTechTier = 2
    mCost = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/Cable/Desc_Cable.Desc_Cable_C', 'amount': 200}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/IronRod/Desc_IronRod.Desc_IronRod_C', 'amount': 200}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/IronScrew/Desc_IronScrew.Desc_IronScrew_C', 'amount': 500}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/IronPlate/Desc_IronPlate.Desc_IronPlate_C', 'amount': 300}]
    mTimeToComplete = 360
    mUnlocks = [{'$ObjectClass': '/Game/FactoryGame/Unlocks/BP_UnlockRecipe.BP_UnlockRecipe_C', '$ObjectFlags': 2621440, '$ObjectName': 'BP_UnlockRecipe_C_0', 'mRecipes': ['/Game/FactoryGame/Recipes/Buildings/Recipe_AssemblerMk1.Recipe_AssemblerMk1_C', '/Game/FactoryGame/Recipes/Constructor/Recipe_CopperSheet.Recipe_CopperSheet_C', '/Game/FactoryGame/Recipes/Assembler/Recipe_Rotor.Recipe_Rotor_C', '/Game/FactoryGame/Recipes/Assembler/Recipe_ModularFrame.Recipe_ModularFrame_C', '/Game/FactoryGame/Recipes/SpaceElevatorParts/Recipe_SpaceElevatorPart_1.Recipe_SpaceElevatorPart_1_C']}]
    mSchematicIcon = Namespace(DrawAs=3, ImageSize={'X': 256, 'Y': 256}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$AssetPath': '/Game/FactoryGame/Buildable/Factory/TradingPost/UI/SchematicIcons/SchematicIcon_Factory.SchematicIcon_Factory'}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    
