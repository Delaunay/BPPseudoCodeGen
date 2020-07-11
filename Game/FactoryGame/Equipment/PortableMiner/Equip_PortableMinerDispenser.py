
from codegen.ue4_stub import *

from Script.AkAudio import PostAkEvent
from Script.Engine import FinishSpawningActor
from Game.FactoryGame.Equipment.PortableMiner.Audio.Play_EQ_PM_Equip import Play_EQ_PM_Equip
from Script.FactoryGame import FGCharacterPlayer
from Script.FactoryGame import GetInstigatorCharacter
from Script.FactoryGame import WasEquipped
from Script.FactoryGame import WasUnEquipped
from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import GetAnimInstance
from Script.FactoryGame import FGPortableMinerDispenser
from Script.Engine import GetCurrentActiveMontage
from Script.FactoryGame import IsLocalInstigator
from Script.Engine import BeginDeferredActorSpawnFromClass
from Script.Engine import Montage_Stop
from Script.FactoryGame import GetMesh1P
from Script.Engine import LineTraceSingle
from Script.FactoryGame import FGInventoryComponentEquipment
from Game.FactoryGame.Equipment.PortableMiner.Equip_PortableMinerDispenser import ExecuteUbergraph_Equip_PortableMinerDispenser.K2Node_Event_resourceNode
from Game.FactoryGame.Equipment.PortableMiner.BP_PortableMiner import BP_PortableMiner
from Game.FactoryGame.Character.Player.Animation.FirstPerson.PortableMinerEquip_01_Montage import PortableMinerEquip_01_Montage
from Game.FactoryGame.Character.Player.Audio.SB_CharacterEssentials.Play_P_ResourcePickUp import Play_P_ResourcePickUp
from Script.Engine import Default__GameplayStatics
from Script.Engine import FlushNetDormancy
from Script.FactoryGame import GetActiveIndex
from Script.Engine import AnimMontage
from Game.FactoryGame.Equipment.PortableMiner.Equip_PortableMinerDispenser import ExecuteUbergraph_Equip_PortableMinerDispenser
from Script.CoreUObject import Vector
from Script.Engine import BreakHitResult
from Script.Engine import Montage_Play
from Script.AkAudio import Default__AkGameplayStatics
from Game.FactoryGame.Equipment.PortableMiner.Animation.1P.PortableMinerEquip_01_Montage import PortableMinerEquip_01_Montage
from Script.Engine import MakeTransform
from Script.Engine import Actor
from Game.FactoryGame.Equipment.PortableMiner.Animation.1P.PortableMinerStinger_01_Montage import PortableMinerStinger_01_Montage
from Game.FactoryGame.Character.Player.Animation.FirstPerson.PortableMinerStinger_01_Montage import PortableMinerStinger_01_Montage
from Game.FactoryGame.Equipment.PortableMiner.Equip_PortableMinerDispenser import ExecuteUbergraph_Equip_PortableMinerDispenser.K2Node_CustomEvent_portableMiner
from Script.Engine import GetForwardVector
from Script.Engine import Montage_IsPlaying
from Script.FactoryGame import GetEquipmentSlot
from Script.AkAudio import AkComponent
from Script.FactoryGame import ShouldShowStinger
from Script.Engine import AnimInstance
from Script.CoreUObject import Transform
from Script.Engine import SkeletalMeshComponent
from Script.FactoryGame import RemoveAllFromIndex
from Script.CoreUObject import LinearColor

class Equip_PortableMinerDispenser(FGPortableMinerDispenser):
    mAllowedResourceForms = ['EResourceForm::RF_SOLID']
    mPlaceDistanceMax = 1000
    mAttachmentClass = NewObject[Attach_PortableMinerDispenser]()
    mEquipmentSlot = EEquipmentSlot::ES_ARMS
    mAttachSocket = hand_rSocket
    mArmAnimation = EArmEquipment::AE_PortableMiner
    PrimaryActorTick = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=False, bTickEvenWhenPaused=False)
    bOnlyRelevantToOwner = True
    bNetUseOwnerRelevancy = True
    bReplicates = True
    RemoteRole = 1
    
    def SpawnPortableMiner(self):
        ExecuteUbergraph_Equip_PortableMinerDispenser.K2Node_Event_resourceNode = resourceNode #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Equip_PortableMinerDispenser(16)
    

    def PlaySpawnEffects(self, PortableMiner: Ptr[BP_PortableMiner]):
        ExecuteUbergraph_Equip_PortableMinerDispenser.K2Node_CustomEvent_portableMiner = PortableMiner #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Equip_PortableMinerDispenser(15)
    

    def WasEquipped(self):
        self.ExecuteUbergraph_Equip_PortableMinerDispenser(1245)
    

    def WasUnEquipped(self):
        self.ExecuteUbergraph_Equip_PortableMinerDispenser(2437)
    

    def ExecuteUbergraph_Equip_PortableMinerDispenser(self):
        goto(ComputedJump("EntryPoint"))
        goto(ExecutionFlow.Pop())
        ReturnValue4: Ptr[FGCharacterPlayer] = self.GetInstigatorCharacter()
        
        OutLocation = None
        OutRotation = None
        ReturnValue4.GetActorEyesViewPoint(Ref[OutLocation], Ref[OutRotation])
        ReturnValue: Vector = GetForwardVector(OutRotation)
        ReturnValue_0: Vector = ReturnValue * 3000
        ReturnValue_1: Vector = OutLocation + ReturnValue_0
        
        Variable = None
        OutHit = None
        ReturnValue_2: bool = Default__KismetSystemLibrary.LineTraceSingle(self, OutLocation, ReturnValue_1, 0, False, 0, True, LinearColor(R = 1, G = 0, B = 0, A = 1), LinearColor(R = 0, G = 1, B = 0, A = 1), 5, Ref[Variable], Ref[OutHit])
        
        OutHit = None
        bBlockingHit = None
        bInitialOverlap = None
        Time = None
        Distance = None
        Location = None
        ImpactPoint = None
        Normal = None
        ImpactNormal = None
        PhysMat = None
        HitActor = None
        HitComponent = None
        HitBoneName = None
        HitItem = None
        FaceIndex = None
        TraceStart = None
        TraceEnd = None
        Default__GameplayStatics.BreakHitResult(Ref[OutHit], Ref[bBlockingHit], Ref[bInitialOverlap], Ref[Time], Ref[Distance], Ref[Location], Ref[ImpactPoint], Ref[Normal], Ref[ImpactNormal], Ref[PhysMat], Ref[HitActor], Ref[HitComponent], Ref[HitBoneName], Ref[HitItem], Ref[FaceIndex], Ref[TraceStart], Ref[TraceEnd])
        ReturnValue_3: Transform = MakeTransform(Location, Rotator::FromPitchYawRoll(0, 0, 0), Vector(1, 1, 1))
        
        ReturnValue_4: Ptr[Actor] = Default__GameplayStatics.BeginDeferredActorSpawnFromClass(self, BP_PortableMiner, 0, None, Ref[ReturnValue_3])
        
        OutHit = None
        bBlockingHit = None
        bInitialOverlap = None
        Time = None
        Distance = None
        Location = None
        ImpactPoint = None
        Normal = None
        ImpactNormal = None
        PhysMat = None
        HitActor = None
        HitComponent = None
        HitBoneName = None
        HitItem = None
        FaceIndex = None
        TraceStart = None
        TraceEnd = None
        Default__GameplayStatics.BreakHitResult(Ref[OutHit], Ref[bBlockingHit], Ref[bInitialOverlap], Ref[Time], Ref[Distance], Ref[Location], Ref[ImpactPoint], Ref[Normal], Ref[ImpactNormal], Ref[PhysMat], Ref[HitActor], Ref[HitComponent], Ref[HitBoneName], Ref[HitItem], Ref[FaceIndex], Ref[TraceStart], Ref[TraceEnd])
        ReturnValue_3 = MakeTransform(Location, Rotator::FromPitchYawRoll(0, 0, 0), Vector(1, 1, 1))
        
        ReturnValue_5: Ptr[BP_PortableMiner] = Default__GameplayStatics.FinishSpawningActor(ReturnValue_4, Ref[ReturnValue_3])
        ReturnValue_5.FlushNetDormancy()
        ReturnValue_5.mExtractResourceNode = resourceNode
        ReturnValue3: Ptr[FGCharacterPlayer] = self.GetInstigatorCharacter()
        ReturnValue_6: Ptr[FGInventoryComponentEquipment] = ReturnValue3.GetEquipmentSlot(1)
        ReturnValue_7: int32 = ReturnValue_6.GetActiveIndex()
        ReturnValue_6.RemoveAllFromIndex(ReturnValue_7)
        self.PlaySpawnEffects(ReturnValue_5)
        goto(ExecutionFlow.Pop())
        self.WasEquipped()
        ReturnValue_8: bool = self.IsLocalInstigator()
        if not ReturnValue_8:
           goto(ExecutionFlow.Pop())
        ReturnValue_9: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_EQ_PM_Equip, self, True)
        ReturnValue_10: bool = self.ShouldShowStinger()
        if not ReturnValue_10:
            goto('L1542')
        ReturnValue1: Ptr[FGCharacterPlayer] = self.GetInstigatorCharacter()
        ReturnValue1_0: Ptr[SkeletalMeshComponent] = ReturnValue1.GetMesh1P()
        ReturnValue4_0: Ptr[AnimInstance] = ReturnValue1_0.GetAnimInstance()
        ReturnValue1_1: bool = ReturnValue4_0.Montage_IsPlaying(PortableMinerStinger_01_Montage)
        if not ReturnValue1_1:
            goto('L2009')
        goto(ExecutionFlow.Pop())
        # Label 1542
        ReturnValue_11: Ptr[FGCharacterPlayer] = self.GetInstigatorCharacter()
        ReturnValue_12: Ptr[SkeletalMeshComponent] = ReturnValue_11.GetMesh1P()
        ReturnValue3_0: Ptr[AnimInstance] = ReturnValue_12.GetAnimInstance()
        ReturnValue_13: bool = ReturnValue3_0.Montage_IsPlaying(PortableMinerEquip_01_Montage)
        if not ReturnValue_13:
            goto('L1712')
        goto(ExecutionFlow.Pop())
        # Label 1712
        ExecutionFlow.Push("L1894")
        ReturnValue_11 = self.GetInstigatorCharacter()
        ReturnValue_12 = ReturnValue_11.GetMesh1P()
        ReturnValue3_0 = ReturnValue_12.GetAnimInstance()
        ReturnValue2: float = ReturnValue3_0.Montage_Play(PortableMinerEquip_01_Montage, 1, 0, 0, True)
        goto(ExecutionFlow.Pop())
        # Label 1894
        ReturnValue2_0: Ptr[AnimInstance] = self.1P_PortableMiner.GetAnimInstance()
        ReturnValue1_2: float = ReturnValue2_0.Montage_Play(PortableMinerEquip_01_Montage, 1, 0, 0, True)
        goto(ExecutionFlow.Pop())
        # Label 2009
        ExecutionFlow.Push("L2191")
        ReturnValue1 = self.GetInstigatorCharacter()
        ReturnValue1_0 = ReturnValue1.GetMesh1P()
        ReturnValue4_0 = ReturnValue1_0.GetAnimInstance()
        ReturnValue3_1: float = ReturnValue4_0.Montage_Play(PortableMinerStinger_01_Montage, 1, 0, 0, True)
        goto(ExecutionFlow.Pop())
        # Label 2191
        ReturnValue1_3: Ptr[AnimInstance] = self.1P_PortableMiner.GetAnimInstance()
        ReturnValue_14: float = ReturnValue1_3.Montage_Play(PortableMinerStinger_01_Montage, 1, 0, 0, True)
        goto(ExecutionFlow.Pop())
        # Label 2306
        ReturnValue_15: Ptr[AnimInstance] = self.1P_PortableMiner.GetAnimInstance()
        ReturnValue_16: Ptr[AnimMontage] = ReturnValue_15.GetCurrentActiveMontage()
        ReturnValue_15.Montage_Stop(0, ReturnValue_16)
        goto(ExecutionFlow.Pop())
        self.WasUnEquipped()
        ReturnValue1_4: bool = self.IsLocalInstigator()
        if not ReturnValue1_4:
           goto(ExecutionFlow.Pop())
        ReturnValue2_1: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(None, self, True)
        ReturnValue1_5: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_P_ResourcePickUp, self, True)
        ReturnValue2_2: Ptr[FGCharacterPlayer] = self.GetInstigatorCharacter()
        ReturnValue2_3: Ptr[SkeletalMeshComponent] = ReturnValue2_2.GetMesh1P()
        ReturnValue5: Ptr[AnimInstance] = ReturnValue2_3.GetAnimInstance()
        ReturnValue1_6: Ptr[AnimMontage] = ReturnValue5.GetCurrentActiveMontage()
        ReturnValue5.Montage_Stop(0, ReturnValue1_6)
        goto('L2306')
    
