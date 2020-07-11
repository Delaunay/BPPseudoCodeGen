
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_Alternate_ElectrodeCircuitBoard(FGRecipe):
    mDisplayNameOverride = True
    mDisplayName = NSLOCTEXT("", "9FEA5240448D4AA63A3ABAA4D2FE2F06", "Alternate: Electrode Circuit Board")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/Rubber/Desc_Rubber.Desc_Rubber_C', 'amount': 6}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/PetroleumCoke/Desc_PetroleumCoke.Desc_PetroleumCoke_C', 'amount': 9}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/CircuitBoard/Desc_CircuitBoard.Desc_CircuitBoard_C', 'amount': 1}]
    mManufactoringDuration = 12
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Buildable/Factory/AssemblerMk1/Build_AssemblerMk1.Build_AssemblerMk1_C']
    
