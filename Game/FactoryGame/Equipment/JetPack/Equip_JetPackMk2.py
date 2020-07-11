
from codegen.ue4_stub import *

from Game.FactoryGame.Equipment.JetPack.Equip_JetPack import Equip_JetPack
from Script.Engine import FClamp
from Game.FactoryGame.Equipment.JetPack.Equip_JetPackMk2 import ExecuteUbergraph_Equip_JetPackMk2
from Game.FactoryGame.Equipment.JetPack.Equip_JetPackMk2 import ExecuteUbergraph_Equip_JetPackMk2.K2Node_Event_delta

class Equip_JetPackMk2(Equip_JetPack):
    mFuelConsumeRate = 0.10000000149011612
    mFuelWorth = 1
    mAttachmentClass = NewObject[Attach_JetPackMk2]()
    mEquipmentSlot = EEquipmentSlot::ES_BACK
    mBackAnimation = EBackEquipment::BE_Jetpack
    PrimaryActorTick = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=False, bTickEvenWhenPaused=False)
    bOnlyRelevantToOwner = True
    bNetUseOwnerRelevancy = True
    bReplicates = True
    RemoteRole = 1
    
    def ConsumeFuel(self):
        ExecuteUbergraph_Equip_JetPackMk2.K2Node_Event_delta = Delta #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Equip_JetPackMk2(276)
    

    def ExecuteUbergraph_Equip_JetPackMk2(self):
        # Label 10
        self.mThrustCooldown = Equip_JetPack.ClassDefaultObject.mThrustCooldown
        # Label 59
        ReturnValue: float = self.mMaxFuel * self.mFuelConsumeRate
        ReturnValue1: float = delta * ReturnValue
        ReturnValue_0: float = self.mCurrentFuel - ReturnValue1
        ReturnValue_1: float = FClamp(ReturnValue_0, 0, 1)
        self.mCurrentFuel = ReturnValue_1
        # End
        ReturnValue = self.mMaxFuel * self.mFuelConsumeRate
        ReturnValue1 = delta * ReturnValue
        ReturnValue_0 = self.mCurrentFuel - ReturnValue1
        ReturnValue_2: bool = ReturnValue_0 <= 0
        if not ReturnValue_2:
            goto('L59')
        goto('L10')
    
