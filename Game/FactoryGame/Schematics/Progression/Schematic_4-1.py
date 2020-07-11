
from codegen.ue4_stub import *

from Script.FactoryGame import FGSchematic

class Schematic_4-1(FGSchematic):
    mType = ESchematicType::EST_Milestone
    mDisplayName = NSLOCTEXT("", "A426F6634C14B6E30C089CBFF2CA8169", "Advanced Steel Production")
    mSchematicCategory = NewObject[SC_Logistics]()
    mTechTier = 4
    mCost = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/SteelPipe/Desc_SteelPipe.Desc_SteelPipe_C', 'amount': 200}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/Rotor/Desc_Rotor.Desc_Rotor_C', 'amount': 200}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/Wire/Desc_Wire.Desc_Wire_C', 'amount': 1500}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/Cement/Desc_Cement.Desc_Cement_C', 'amount': 300}]
    mUnlocks = [{'$ObjectClass': '/Game/FactoryGame/Unlocks/BP_UnlockRecipe.BP_UnlockRecipe_C', '$ObjectFlags': 2621440, '$ObjectName': 'BP_UnlockRecipe_C_0', 'mRecipes': ['/Game/FactoryGame/Recipes/Buildings/Recipe_MinerMk2.Recipe_MinerMk2_C', '/Game/FactoryGame/Recipes/Assembler/Recipe_EncasedIndustrialBeam.Recipe_EncasedIndustrialBeam_C', '/Game/FactoryGame/Recipes/Assembler/Recipe_Stator.Recipe_Stator_C', '/Game/FactoryGame/Recipes/Assembler/Recipe_Motor.Recipe_Motor_C', '/Game/FactoryGame/Recipes/SpaceElevatorParts/Recipe_SpaceElevatorPart_3.Recipe_SpaceElevatorPart_3_C', '/Game/FactoryGame/Recipes/Manufacturer/Recipe_ModularFrameHeavy.Recipe_ModularFrameHeavy_C']}]
    mSchematicIcon = Namespace(DrawAs=3, ImageSize={'X': 256, 'Y': 256}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$AssetPath': '/Game/FactoryGame/Buildable/Factory/TradingPost/UI/SchematicIcons/SchematicIcon_Factory.SchematicIcon_Factory'}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    
