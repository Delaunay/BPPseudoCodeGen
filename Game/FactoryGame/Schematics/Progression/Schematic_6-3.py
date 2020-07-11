
from codegen.ue4_stub import *

from Script.FactoryGame import FGSchematic

class Schematic_6-3(FGSchematic):
    mType = ESchematicType::EST_Milestone
    mDisplayName = NSLOCTEXT("", "E03093B24DC8832F2158E9882D4A9131", "Monorail Train Technology")
    mSchematicCategory = NewObject[SC_Logistics]()
    mTechTier = 6
    mCost = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/Computer/Desc_Computer.Desc_Computer_C', 'amount': 50}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/ModularFrameHeavy/Desc_ModularFrameHeavy.Desc_ModularFrameHeavy_C', 'amount': 100}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/SteelPlate/Desc_SteelPlate.Desc_SteelPlate_C', 'amount': 500}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/SteelPipe/Desc_SteelPipe.Desc_SteelPipe_C', 'amount': 600}]
    mTimeToComplete = 900
    mUnlocks = [{'$ObjectClass': '/Game/FactoryGame/Unlocks/BP_UnlockRecipe.BP_UnlockRecipe_C', '$ObjectFlags': 2621440, '$ObjectName': 'BP_UnlockRecipe_C_0', 'mRecipes': ['/Game/FactoryGame/Recipes/Vehicle/Train/Recipe_Locomotive.Recipe_Locomotive_C', '/Game/FactoryGame/Recipes/Vehicle/Train/Recipe_FreightWagon.Recipe_FreightWagon_C', '/Game/FactoryGame/Recipes/Buildings/Recipe_RailroadTrack.Recipe_RailroadTrack_C', '/Game/FactoryGame/Buildable/Factory/Train/Station/Recipe_TrainStation.Recipe_TrainStation_C', '/Game/FactoryGame/Buildable/Factory/Train/Station/Recipe_TrainDockingStation.Recipe_TrainDockingStation_C', '/Game/FactoryGame/Buildable/Factory/Train/Station/Recipe_TrainDockingStationLiquid.Recipe_TrainDockingStationLiquid_C', '/Game/FactoryGame/Buildable/Factory/Train/Station/Recipe_TrainPlatformEmpty.Recipe_TrainPlatformEmpty_C']}]
    mSchematicIcon = Namespace(DrawAs=3, ImageSize={'X': 256, 'Y': 256}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$AssetPath': '/Game/FactoryGame/Buildable/Factory/TradingPost/UI/SchematicIcons/SchematicIcon_Vehicle.SchematicIcon_Vehicle'}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    
