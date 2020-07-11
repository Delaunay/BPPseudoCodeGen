
from codegen.ue4_stub import *

from Script.FactoryGame import GetConsumeable
from Script.AkAudio import PostAkEvent
from Script.Engine import Delay
from Script.FactoryGame import FGCharacterPlayer
from Script.Engine import SetCastShadow
from Script.Engine import Controller
from Game.FactoryGame.Character.Player.Animation.FirstPerson.ConsumablesEquip_01_Montage import ConsumablesEquip_01_Montage
from Script.FactoryGame import GetInstigatorCharacter
from Game.FactoryGame.Equipment.-Shared.Consumeable.BP_ConsumeableEquipment import ExecuteUbergraph_BP_ConsumeableEquipment.K2Node_Event_consumable
from Script.Engine import Pawn
from Script.FactoryGame import WasEquipped
from Script.Engine import K2_SetRelativeLocationAndRotation
from Script.Engine import GetInstigator
from Script.Engine import LatentActionInfo
from Script.FactoryGame import FGConsumableEquipment
from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import GetAnimInstance
from Script.Engine import PlayerController
from Script.Engine import ReceiveTick
from Script.Engine import GetController
from Script.Engine import SkeletalMesh
from Script.FactoryGame import PlayConsumeEffects
from Game.FactoryGame.Equipment.-Shared.Consumeable.BP_ConsumeableEquipment import ExecuteUbergraph_BP_ConsumeableEquipment
from Script.Engine import IsValid
from Script.FactoryGame import IsLocalInstigator
from Script.FactoryGame import OnPrimaryFire
from Game.FactoryGame.Equipment.-Shared.Consumeable.BP_ConsumeableEquipment import ExecuteUbergraph_BP_ConsumeableEquipment.K2Node_Event_DeltaSeconds
from Game.FactoryGame.Character.Player.Animation.FirstPerson.Eat_02_Montage import Eat_02_Montage
from Script.FactoryGame import GetFPOverrideMesh
from Script.FactoryGame import GetMesh1P
from Script.CoreUObject import Vector
from Script.Engine import Montage_Play
from Game.FactoryGame.Character.Player.CameraShake.Eat_02_CameraAnim import Eat_02_CameraAnim
from Script.AkAudio import Default__AkGameplayStatics
from Script.FactoryGame import Default__FGConsumableDescriptor
from Script.Engine import Montage_IsPlaying
from Script.Engine import AnimInstance
from Script.AkAudio import AkComponent
from Script.Engine import IsValidClass
from Script.Engine import SkeletalMeshComponent

class BP_ConsumeableEquipment(FGConsumableEquipment):
    mRandomAnim: int32
    mCanPress: bool
    mAttachmentClass = NewObject[BP_ConsumeableEquipmentAttachment]()
    mEquipmentSlot = EEquipmentSlot::ES_ARMS
    mEquipSound = Namespace(AssetPath='/Game/FactoryGame/Character/Player/Audio/SB_CharacterEssentials/Play_P_ResourcePickUp.Play_P_ResourcePickUp')
    mAttachSocket = hand_rSocket
    mArmAnimation = EArmEquipment::AE_Consumables
    mIdlePoseAnimation3p = Namespace(AssetPath='/Game/FactoryGame/Character/Player/Animation/ThirdPerson/Consumablesdle_01.Consumablesdle_01')
    PrimaryActorTick = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=False, bTickEvenWhenPaused=False)
    bOnlyRelevantToOwner = True
    bNetUseOwnerRelevancy = True
    bReplicates = True
    RemoteRole = 1
    
    def PlayConsumeEffects(self):
        ExecuteUbergraph_BP_ConsumeableEquipment.K2Node_Event_consumable = consumable #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_ConsumeableEquipment(1721)
    

    def ReceiveTick(self):
        ExecuteUbergraph_BP_ConsumeableEquipment.K2Node_Event_DeltaSeconds = DeltaSeconds #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_ConsumeableEquipment(788)
    

    def WasEquipped(self):
        self.ExecuteUbergraph_BP_ConsumeableEquipment(1142)
    

    def ExecuteUbergraph_BP_ConsumeableEquipment(self):
        goto(ComputedJump("EntryPoint"))
        self.OnPrimaryFire()
        self.mCanPress = True
        ReturnValue: Ptr[FGCharacterPlayer] = self.GetInstigatorCharacter()
        ReturnValue_0: Ptr[SkeletalMeshComponent] = ReturnValue.GetMesh1P()
        ReturnValue_1: Ptr[AnimInstance] = ReturnValue_0.GetAnimInstance()
        ReturnValue_2: float = ReturnValue_1.Montage_Play(ConsumablesEquip_01_Montage, 1, 0, 0, True)
        goto(ExecutionFlow.Pop())
        
        consumeable = None
        numConsumeable = None
        # Label 213
        self.GetConsumeable(Ref[consumeable], Ref[numConsumeable])
        ReturnValue_3: bool = Default__KismetSystemLibrary.IsValidClass(consumeable)
        if not ReturnValue_3:
           goto(ExecutionFlow.Pop())
        
        consumeable = None
        numConsumeable = None
        self.GetConsumeable(Ref[consumeable], Ref[numConsumeable])
        ReturnValue_4: Ptr[SkeletalMesh] = Default__FGConsumableDescriptor.GetFPOverrideMesh(consumeable)
        self.ConsumeableMesh.SetSkeletalMesh(ReturnValue_4, False)
        self.ConsumeableMesh.SetCastShadow(False)
        
        consumeable = None
        numConsumeable = None
        self.GetConsumeable(Ref[consumeable], Ref[numConsumeable])
        ReturnValue_5: Vector = Vector(consumeable.ClassDefaultObject.mCustomHandsMeshScale, consumeable.ClassDefaultObject.mCustomHandsMeshScale, consumeable.ClassDefaultObject.mCustomHandsMeshScale)
        self.ConsumeableMesh.SetRelativeScale3D(ReturnValue_5)
        
        consumeable = None
        numConsumeable = None
        self.GetConsumeable(Ref[consumeable], Ref[numConsumeable])
        
        SweepHitResult = None
        self.ConsumeableMesh.K2_SetRelativeLocationAndRotation(consumeable.ClassDefaultObject.mCustomLocation, consumeable.ClassDefaultObject.mCustomRotation, False, True, Ref[SweepHitResult])
        goto(ExecutionFlow.Pop())
        self.ReceiveTick(DeltaSeconds)
        ReturnValue_6: bool = self.IsLocalInstigator()
        if not ReturnValue_6:
           goto(ExecutionFlow.Pop())
        goto('L213')
        # Label 842
        ReturnValue_7: Ptr[Pawn] = self.GetInstigator()
        ReturnValue_8: Ptr[Controller] = ReturnValue_7.GetController()
        Controller: Ptr[PlayerController] = Cast[PlayerController](ReturnValue_8)
        bSuccess: bool = Controller
        if not bSuccess:
           goto(ExecutionFlow.Pop())
        Controller.ClientPlayCameraAnim(Eat_02_CameraAnim, 1, 1, 0, 0, False, False, 0, Rotator::FromPitchYawRoll(0, 0, 0))
        Default__KismetSystemLibrary.Delay(self, ReturnValue2, LatentActionInfo(Linkage = 15, UUID = -1065361517, ExecutionFunction = "ExecuteUbergraph_BP_ConsumeableEquipment", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        self.WasEquipped()
        ReturnValue1: bool = self.IsLocalInstigator()
        if not ReturnValue1:
           goto(ExecutionFlow.Pop())
        self.mCanPress = True
        ReturnValue1_0: Ptr[FGCharacterPlayer] = self.GetInstigatorCharacter()
        ReturnValue1_1: Ptr[SkeletalMeshComponent] = ReturnValue1_0.GetMesh1P()
        ReturnValue1_2: Ptr[AnimInstance] = ReturnValue1_1.GetAnimInstance()
        ReturnValue1_3: float = ReturnValue1_2.Montage_Play(ConsumablesEquip_01_Montage, 1, 0, 0, True)
        goto(ExecutionFlow.Pop())
        # Label 1370
        ReturnValue2: Ptr[FGCharacterPlayer] = self.GetInstigatorCharacter()
        ReturnValue2_0: Ptr[SkeletalMeshComponent] = ReturnValue2.GetMesh1P()
        ReturnValue2_1: Ptr[AnimInstance] = ReturnValue2_0.GetAnimInstance()
        ReturnValue2 = ReturnValue2_1.Montage_Play(Eat_02_Montage, 1, 0, 0, True)
        goto('L842')
        # Label 1551
        ReturnValue2 = self.GetInstigatorCharacter()
        ReturnValue2_0 = ReturnValue2.GetMesh1P()
        ReturnValue2_1 = ReturnValue2_0.GetAnimInstance()
        ReturnValue_9: bool = ReturnValue2_1.Montage_IsPlaying(Eat_02_Montage)
        if not ReturnValue_9:
            goto('L1370')
        goto(ExecutionFlow.Pop())
        self.PlayConsumeEffects(consumable)
        if not self.mCanPress:
           goto(ExecutionFlow.Pop())
        self.mCanPress = False
        ReturnValue_10: bool = Default__KismetSystemLibrary.IsValid(consumable.mConsumeEvent)
        if not ReturnValue_10:
            goto('L1551')
        ReturnValue_11: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(consumable.mConsumeEvent, self, True)
        goto('L1551')
    
