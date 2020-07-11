
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_ConveyorAttachmentSplitterProgrammable(FGRecipe):
    mDisplayName = NSLOCTEXT("", "FACA870E414AB55202E3C18D0EFD99AB", "Conveyor Splitter")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/ModularFrameHeavy/Desc_ModularFrameHeavy.Desc_ModularFrameHeavy_C', 'amount': 1}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/Motor/Desc_Motor.Desc_Motor_C', 'amount': 1}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/ComputerSuper/Desc_ComputerSuper.Desc_ComputerSuper_C', 'amount': 1}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Buildable/Factory/CA_SplitterProgrammable/Desc_ConveyorAttachmentSplitterProgrammable.Desc_ConveyorAttachmentSplitterProgrammable_C', 'amount': 1}]
    mManufactoringDuration = 1
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Equipment/BuildGun/BP_BuildGun.BP_BuildGun_C']
    
