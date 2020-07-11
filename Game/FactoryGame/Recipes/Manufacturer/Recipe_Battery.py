
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_Battery(FGRecipe):
    mDisplayName = NSLOCTEXT("", "064A7A5D414BBC91992CA7B96E7782F4", "Battery")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/AluminumPlate/Desc_AluminumPlate.Desc_AluminumPlate_C', 'amount': 8}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/Wire/Desc_Wire.Desc_Wire_C', 'amount': 16}, {'ItemClass': '/Game/FactoryGame/Resource/RawResources/Sulfur/Desc_Sulfur.Desc_Sulfur_C', 'amount': 20}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/Plastic/Desc_Plastic.Desc_Plastic_C', 'amount': 8}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/Battery/Desc_Battery.Desc_Battery_C', 'amount': 3}]
    mManufactoringDuration = 32
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Buildable/Factory/ManufacturerMk1/Build_ManufacturerMk1.Build_ManufacturerMk1_C', '/Game/FactoryGame/Buildable/-Shared/WorkBench/BP_WorkBenchComponent.BP_WorkBenchComponent_C', '/Script/FactoryGame.FGBuildableAutomatedWorkBench']
    
