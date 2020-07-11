
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_CyberWagon(FGRecipe):
    mDisplayNameOverride = True
    mDisplayName = NSLOCTEXT("", "4C6338F84707DDEC75827C9C376B02BB", "Cyber Wagon")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/IronPlateReinforced/Desc_IronPlateReinforced.Desc_IronPlateReinforced_C', 'amount': 10}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Buildable/Vehicle/Cyberwagon/Desc_CyberWagon.Desc_CyberWagon_C', 'amount': 1}]
    mManufactoringDuration = 1
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Equipment/BuildGun/BP_BuildGun.BP_BuildGun_C']
    
