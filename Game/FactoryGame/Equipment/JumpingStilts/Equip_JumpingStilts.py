
from codegen.ue4_stub import *

from Game.FactoryGame.Equipment.JumpingStilts.Equip_JumpingStilts import ExecuteUbergraph_Equip_JumpingStilts
from Script.FactoryGame import FGJumpingStilts

class Equip_JumpingStilts(FGJumpingStilts):
    mFallDamageCurveOverride = Namespace(AssetPath='/Game/FactoryGame/Equipment/JumpingStilts/JumpingStilts_FallDamageCurve.JumpingStilts_FallDamageCurve')
    mSprintSpeedFactor = 1.5
    mJumpSpeedFactor = 1.5
    mAttachmentClass = NewObject[Attach_JumpingStilts_L]()
    mSecondaryAttachmentClass = NewObject[Attach_JumpingStilts_R]()
    mEquipmentSlot = EEquipmentSlot::ES_BACK
    mAttachSocket = jumpingstilt_lSocket
    mChildEquipmentClass = NewObject[EquipChild_JumpingStilts]()
    PrimaryActorTick = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=False, bTickEvenWhenPaused=False)
    bOnlyRelevantToOwner = True
    bNetUseOwnerRelevancy = True
    bReplicates = True
    RemoteRole = 1
    AutoReceiveInput = 1
    
    def WasEquipped(self):
        self.ExecuteUbergraph_Equip_JumpingStilts(15)
    

    def WasUnEquipped(self):
        self.ExecuteUbergraph_Equip_JumpingStilts(20)
    

    def ReceiveBeginPlay(self):
        self.ExecuteUbergraph_Equip_JumpingStilts(10)
    

    def ExecuteUbergraph_Equip_JumpingStilts(self):
        # End
        # End
    
