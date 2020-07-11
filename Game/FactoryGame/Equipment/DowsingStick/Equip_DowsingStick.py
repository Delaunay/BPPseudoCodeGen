
from codegen.ue4_stub import *

from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import GetAnimInstance
from Script.Engine import K2_GetActorLocation
from Script.Engine import K2_SetTimerDelegate
from Script.Engine import Subtract_VectorVector
from Script.CoreUObject import Vector
from Script.Engine import Normal
from Script.FactoryGame import GetWaterLocation
from Script.Engine import TimerHandle
from Game.FactoryGame.Equipment.DowsingStick.Equip_DowsingStick import ExecuteUbergraph_Equip_DowsingStick
from Script.Engine import AnimInstance
from Game.FactoryGame.Equipment.DowsingStick.SM_FindingWater_Skeleton_AnimBP import SM_FindingWater_Skeleton_AnimBP
from Script.Engine import DrawDebugSphere
from Script.FactoryGame import FGDowsingStick
from Script.CoreUObject import LinearColor

class Equip_DowsingStick(FGDowsingStick):
    mNumVolumesPerTick = 20
    mAttachmentClass = NewObject[Attach_DowsingStick]()
    mEquipmentSlot = EEquipmentSlot::ES_ARMS
    mAttachSocket = hand_rSocket
    mArmAnimation = EArmEquipment::AE_OneHandEquipment
    PrimaryActorTick = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=True, bTickEvenWhenPaused=False)
    bOnlyRelevantToOwner = True
    bNetUseOwnerRelevancy = True
    bReplicates = True
    RemoteRole = 1
    
    def CustomEvent_0(self):
        self.ExecuteUbergraph_Equip_DowsingStick(464)
    

    def ReceiveBeginPlay(self):
        self.ExecuteUbergraph_Equip_DowsingStick(593)
    

    def ExecuteUbergraph_Equip_DowsingStick(self):
        # Label 10
        ReturnValue: Ptr[AnimInstance] = self.SkeletalMesh.GetAnimInstance()
        BP: Ptr[SM_FindingWater_Skeleton_AnimBP] = Cast[SM_FindingWater_Skeleton_AnimBP](ReturnValue)
        bSuccess: bool = BP
        if not bSuccess:
            goto('L598')
        ReturnValue_0: Vector = self.GetWaterLocation()
        ReturnValue_1: Vector = self.K2_GetActorLocation()
        ReturnValue_2: Vector = Subtract_VectorVector(ReturnValue_0, ReturnValue_1)
        ReturnValue_3: Vector = Normal(ReturnValue_2, 9.999999747378752e-05)
        ReturnValue_4: Vector = ReturnValue_3 * 100
        BP.mForce = ReturnValue_4
        # End
        # Label 371
        OutputDelegate.BindUFunction(self, CustomEvent_0)
        ReturnValue_5: TimerHandle = Default__KismetSystemLibrary.K2_SetTimerDelegate(OutputDelegate, 1, True)
        # End
        ReturnValue_0 = self.GetWaterLocation()
        Default__KismetSystemLibrary.DrawDebugSphere(self, ReturnValue_0, 300, 12, LinearColor(R = 1, G = 0, B = 0.014251000247895718, A = 1), 1, 2)
        goto('L10')
        goto('L371')
    
