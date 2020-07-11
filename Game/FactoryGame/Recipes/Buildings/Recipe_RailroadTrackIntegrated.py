
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_RailroadTrackIntegrated(FGRecipe):
    mDisplayName = NSLOCTEXT("", "F639480541F3F8CF0A11ABA824F3D0C2", "Track")
    mProduct = [{'ItemClass': '/Game/FactoryGame/Buildable/Factory/Train/Track/Desc_RailroadTrackIntegrated.Desc_RailroadTrackIntegrated_C', 'amount': 1}]
    mManufactoringDuration = 1
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Equipment/BuildGun/BP_BuildGun.BP_BuildGun_C']
    
