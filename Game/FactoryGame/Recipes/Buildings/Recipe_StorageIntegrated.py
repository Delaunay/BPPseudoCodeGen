
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_StorageIntegrated(FGRecipe):
    mDisplayName = NSLOCTEXT("", "D54C567443E575A26E8EA8957C1EEC5F", "Expanded Storage Container")
    mProduct = [{'ItemClass': '/Game/FactoryGame/Buildable/Factory/StoragePlayer/Desc_StorageIntegrated.Desc_StorageIntegrated_C', 'amount': 1}]
    mManufactoringDuration = 1
    mManualManufacturingMultiplier = 1
    
