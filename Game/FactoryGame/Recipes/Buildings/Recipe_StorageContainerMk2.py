
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_StorageContainerMk2(FGRecipe):
    mDisplayName = NSLOCTEXT("", "C607F6614B95C32AC3D53BA6DDDA72D5", "Expanded Storage Container")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/SteelPlate/Desc_SteelPlate.Desc_SteelPlate_C', 'amount': 20}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/SteelPipe/Desc_SteelPipe.Desc_SteelPipe_C', 'amount': 20}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Buildable/Factory/StorageContainerMk2/Desc_StorageContainerMk2.Desc_StorageContainerMk2_C', 'amount': 1}]
    mManufactoringDuration = 1
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Equipment/BuildGun/BP_BuildGun.BP_BuildGun_C']
    
