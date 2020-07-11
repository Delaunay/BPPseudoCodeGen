
from codegen.ue4_stub import *

from Script.FactoryGame import FGHealthComponent
from Script.FactoryGame import GetHealthComponent
from Script.FactoryGame import Heal
from Script.FactoryGame import ConsumedBy
from Script.FactoryGame import FGConsumableDescriptor
from Script.Engine import HasAuthority

class BP_HealthGainDescriptor(FGConsumableDescriptor):
    mHealthGain: float
    mCustomHandsMeshScale = 1
    mEquipmentClass = NewObject[BP_ConsumeableEquipment]()
    mUseDisplayNameAndDescription = True
    mStackSize = EStackSize::SS_MEDIUM
    mCanBeDiscarded = True
    mForm = EResourceForm::RF_SOLID
    mFluidDensity = 1
    mFluidViscosity = 1
    mFluidFriction = 0.10000000149011612
    
    def ConsumedBy(self):
        self.ConsumedBy(Player)
        ReturnValue: bool = Player.HasAuthority()
        if not ReturnValue:
            goto('L158')
        ReturnValue_0: Ptr[FGHealthComponent] = Player.GetHealthComponent()
        ReturnValue_0.Heal(self.mHealthGain)
    
