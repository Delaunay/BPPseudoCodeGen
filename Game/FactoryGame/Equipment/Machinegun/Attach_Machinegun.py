
from codegen.ue4_stub import *

from Game.FactoryGame.Equipment.Machinegun.Attach_Machinegun import ExecuteUbergraph_Attach_Machinegun.K2Node_Event_flashLocation
from Script.Engine import GetAnimInstance
from Game.FactoryGame.Character.Player.Anim_3p import Anim_3p
from Script.AkAudio import PostAkEvent
from Script.FactoryGame import GetAttachedTo
from Script.FactoryGame import FGCharacterPlayer
from Game.FactoryGame.Equipment.Rifle.Audio.Play_EQ_Rifle_Reload import Play_EQ_Rifle_Reload
from Game.FactoryGame.Character.Player.Animation.ThirdPerson.RiflePrimary_Montage import RiflePrimary_Montage
from Script.AkAudio import PostAkEventAtLocation
from Script.Engine import Montage_IsPlaying
from Script.Engine import AnimInstance
from Script.AkAudio import AkComponent
from Script.Engine import Montage_Play
from Game.FactoryGame.Equipment.Rifle.Audio.Play_EQ_Rifle_Fire import Play_EQ_Rifle_Fire
from Script.AkAudio import Default__AkGameplayStatics
from Script.FactoryGame import FGWeaponAttachment
from Script.Engine import SkeletalMeshComponent
from Game.FactoryGame.Equipment.Machinegun.Attach_Machinegun import ExecuteUbergraph_Attach_Machinegun

class Attach_Machinegun(FGWeaponAttachment):
    mAttachSocket = weaponSocket_temp
    mArmAnimation = EArmEquipment::AE_Rifle
    mEquipmentSlot = EEquipmentSlot::ES_ARMS
    PrimaryActorTick = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=False, bTickEvenWhenPaused=False)
    bNetUseOwnerRelevancy = True
    bReplicates = True
    RemoteRole = 1
    
    def PlayFireEffect(self):
        ExecuteUbergraph_Attach_Machinegun.K2Node_Event_flashLocation = flashLocation #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Attach_Machinegun(471)
    

    def ClientPlayReloadEffect(self):
        self.ExecuteUbergraph_Attach_Machinegun(15)
    

    def ExecuteUbergraph_Attach_Machinegun(self):
        goto(ComputedJump("EntryPoint"))
        ReturnValue: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_EQ_Rifle_Reload, self, True)
        goto(ExecutionFlow.Pop())
        # Label 69
        ReturnValue_0: Ptr[FGCharacterPlayer] = self.GetAttachedTo()
        ReturnValue_1: Ptr[SkeletalMeshComponent] = ReturnValue_0.GetMesh3P()
        ReturnValue_2: Ptr[AnimInstance] = ReturnValue_1.GetAnimInstance()
        3p: Ptr[Anim_3p] = Cast[Anim_3p](ReturnValue_2)
        bSuccess: bool = 3p
        if not bSuccess:
           goto(ExecutionFlow.Pop())
        ReturnValue_3: bool = 3p.Montage_IsPlaying(RiflePrimary_Montage)
        if not ReturnValue_3:
            goto('L318')
        goto(ExecutionFlow.Pop())
        # Label 318
        ReturnValue_4: float = 3p.Montage_Play(RiflePrimary_Montage, 1, 0, 0, True)
        goto(ExecutionFlow.Pop())
        # Label 391
        ExecutionFlow.Push("L69")
        ReturnValue_5: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEventAtLocation(self, Play_EQ_Rifle_Fire, flashLocation, Rotator::FromPitchYawRoll(0, 0, 0))
        goto(ExecutionFlow.Pop())
        goto('L391')
    
