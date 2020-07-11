
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_RailroadTrack(FGRecipe):
    mDisplayName = NSLOCTEXT("", "F639480541F3F8CF0A11ABA824F3D0C2", "Track")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/SteelPipe/Desc_SteelPipe.Desc_SteelPipe_C', 'amount': 1}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/SteelPlate/Desc_SteelPlate.Desc_SteelPlate_C', 'amount': 1}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Buildable/Factory/Train/Track/Desc_RailroadTrack.Desc_RailroadTrack_C', 'amount': 1}]
    mManufactoringDuration = 1
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Equipment/BuildGun/BP_BuildGun.BP_BuildGun_C']
    
