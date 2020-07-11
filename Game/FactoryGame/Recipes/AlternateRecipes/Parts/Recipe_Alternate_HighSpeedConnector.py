
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_Alternate_HighSpeedConnector(FGRecipe):
    mDisplayNameOverride = True
    mDisplayName = NSLOCTEXT("", "83A9F00140F09B776E2D2284444DC60C", "Alternate: Silicone High-Speed Connector")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/HighSpeedWire/Desc_HighSpeedWire.Desc_HighSpeedWire_C', 'amount': 60}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/Silica/Desc_Silica.Desc_Silica_C', 'amount': 25}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/CircuitBoard/Desc_CircuitBoard.Desc_CircuitBoard_C', 'amount': 2}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/HighSpeedConnector/Desc_HighSpeedConnector.Desc_HighSpeedConnector_C', 'amount': 2}]
    mManufactoringDuration = 40
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Buildable/Factory/ManufacturerMk1/Build_ManufacturerMk1.Build_ManufacturerMk1_C']
    
