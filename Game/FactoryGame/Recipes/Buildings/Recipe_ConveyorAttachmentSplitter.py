﻿
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_ConveyorAttachmentSplitter(FGRecipe):
    mDisplayName = NSLOCTEXT("", "FACA870E414AB55202E3C18D0EFD99AB", "Conveyor Splitter")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/IronPlate/Desc_IronPlate.Desc_IronPlate_C', 'amount': 2}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/Cable/Desc_Cable.Desc_Cable_C', 'amount': 2}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Buildable/Factory/CA_Splitter/Desc_ConveyorAttachmentSplitter.Desc_ConveyorAttachmentSplitter_C', 'amount': 1}]
    mManufactoringDuration = 1
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Equipment/BuildGun/BP_BuildGun.BP_BuildGun_C']
    
