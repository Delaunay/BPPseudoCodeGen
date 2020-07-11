
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_Alternate_EnrichedCoal(FGRecipe):
    mDisplayNameOverride = True
    mDisplayName = NSLOCTEXT("", "8D2459A343E049BB568D828CAC98714A", "Alternate: Compacted Coal")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/RawResources/Coal/Desc_Coal.Desc_Coal_C', 'amount': 5}, {'ItemClass': '/Game/FactoryGame/Resource/RawResources/Sulfur/Desc_Sulfur.Desc_Sulfur_C', 'amount': 5}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/CompactedCoal/Desc_CompactedCoal.Desc_CompactedCoal_C', 'amount': 5}]
    mManufactoringDuration = 12
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Buildable/Factory/AssemblerMk1/Build_AssemblerMk1.Build_AssemblerMk1_C']
    
