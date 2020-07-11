
from codegen.ue4_stub import *

from Script.FactoryGame import FGSchematic

class Schematic_5-2(FGSchematic):
    mType = ESchematicType::EST_Milestone
    mDisplayName = NSLOCTEXT("", "FFCD364B47D56545D7B4E18760BB53E4", "Industrial Manufacturing")
    mSchematicCategory = NewObject[SC_Logistics]()
    mTechTier = 5
    mCost = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/Motor/Desc_Motor.Desc_Motor_C', 'amount': 100}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/Plastic/Desc_Plastic.Desc_Plastic_C', 'amount': 200}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/Rubber/Desc_Rubber.Desc_Rubber_C', 'amount': 200}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/Cable/Desc_Cable.Desc_Cable_C', 'amount': 1000}]
    mTimeToComplete = 720
    mUnlocks = [{'$ObjectClass': '/Game/FactoryGame/Unlocks/BP_UnlockRecipe.BP_UnlockRecipe_C', '$ObjectFlags': 2621440, '$ObjectName': 'BP_UnlockRecipe_C_0', 'mRecipes': ['/Game/FactoryGame/Recipes/Buildings/Recipe_ManufacturerMk1.Recipe_ManufacturerMk1_C', '/Game/FactoryGame/Recipes/Vehicle/Recipe_Truck.Recipe_Truck_C', '/Game/FactoryGame/Recipes/Manufacturer/Recipe_Computer.Recipe_Computer_C', '/Game/FactoryGame/Recipes/SpaceElevatorParts/Recipe_SpaceElevatorPart_4.Recipe_SpaceElevatorPart_4_C', '/Game/FactoryGame/Recipes/SpaceElevatorParts/Recipe_SpaceElevatorPart_5.Recipe_SpaceElevatorPart_5_C']}]
    mSchematicIcon = Namespace(DrawAs=3, ImageSize={'X': 256, 'Y': 256}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$AssetPath': '/Game/FactoryGame/Buildable/Factory/TradingPost/UI/SchematicIcons/SchematicIcon_Factory.SchematicIcon_Factory'}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    
