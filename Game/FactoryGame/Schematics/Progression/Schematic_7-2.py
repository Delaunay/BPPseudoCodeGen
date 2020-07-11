
from codegen.ue4_stub import *

from Script.FactoryGame import FGSchematic

class Schematic_7-2(FGSchematic):
    mType = ESchematicType::EST_Milestone
    mDisplayName = NSLOCTEXT("", "DB07187F43AB3519CDB9FDAF6FDACAC8", "Advanced Aluminum Production")
    mSchematicCategory = NewObject[SC_Logistics]()
    mTechTier = 7
    mCost = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/AluminumPlate/Desc_AluminumPlate.Desc_AluminumPlate_C', 'amount': 200}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/Motor/Desc_Motor.Desc_Motor_C', 'amount': 300}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/ModularFrameHeavy/Desc_ModularFrameHeavy.Desc_ModularFrameHeavy_C', 'amount': 150}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/Computer/Desc_Computer.Desc_Computer_C', 'amount': 150}]
    mTimeToComplete = 900
    mUnlocks = [{'$ObjectClass': '/Game/FactoryGame/Unlocks/BP_UnlockRecipe.BP_UnlockRecipe_C', '$ObjectFlags': 2621440, '$ObjectName': 'BP_UnlockRecipe_C_0', 'mRecipes': ['/Game/FactoryGame/Recipes/Buildings/Recipe_MinerMk3.Recipe_MinerMk3_C', '/Game/FactoryGame/Recipes/Assembler/Recipe_HeatSink.Recipe_HeatSink_C', '/Game/FactoryGame/Recipes/Manufacturer/Recipe_MotorTurbo.Recipe_MotorTurbo_C', '/Game/FactoryGame/Recipes/Manufacturer/Recipe_Battery.Recipe_Battery_C']}]
    mSchematicIcon = Namespace(DrawAs=3, ImageSize={'X': 256, 'Y': 256}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$AssetPath': '/Game/FactoryGame/Buildable/Factory/TradingPost/UI/SchematicIcons/SchematicIcon_Factory.SchematicIcon_Factory'}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    
