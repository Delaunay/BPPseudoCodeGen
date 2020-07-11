
from codegen.ue4_stub import *

from Game.FactoryGame.Equipment.Beacon.Animation.BeaconStinger_02_Montage import BeaconStinger_02_Montage
from Script.AkAudio import PostAkEvent
from Script.Engine import FinishSpawningActor
from Script.FactoryGame import FGCharacterPlayer
from Script.Engine import IsAnyMontagePlaying
from Script.FactoryGame import GetInstigatorCharacter
from Script.Engine import Pawn
from Script.Engine import SetObjectPropertyByName
from Script.AkAudio import PostAkEventAtLocation
from Script.FactoryGame import WasEquipped
from Game.FactoryGame.Character.Player.Animation.FirstPerson.OneHandEquipmentEquip_01_Montage import OneHandEquipmentEquip_01_Montage
from Script.Engine import GetInstigator
from Script.FactoryGame import IsLocallyHumanControlled
from Game.FactoryGame.Equipment.Beacon.Audio.Play_EQ_Beacon_Stinger import Play_EQ_Beacon_Stinger
from Game.FactoryGame.Character.Player.Animation.FirstPerson.BeaconStinger_02_Montage import BeaconStinger_02_Montage
from Script.FactoryGame import WasUnEquipped
from Script.FactoryGame import FGConsumableEquipment
from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import GetAnimInstance
from Game.FactoryGame.Equipment.Beacon.Equip_Beacon import ExecuteUbergraph_Equip_Beacon
from Script.FactoryGame import PlayConsumeEffects
from Script.Engine import GetCurrentActiveMontage
from Script.Engine import BeginDeferredActorSpawnFromClass
from Script.FactoryGame import OnPrimaryFire
from Script.Engine import Montage_Stop
from Script.FactoryGame import GetMesh1P
from Script.Engine import LineTraceSingle
from Game.FactoryGame.Equipment.Beacon.Audio.Stop_EQ_Beacon_Stinger import Stop_EQ_Beacon_Stinger
from Script.Engine import Default__GameplayStatics
from Script.Engine import AnimMontage
from Script.Engine import Subtract_VectorVector
from Script.CoreUObject import Vector
from Script.Engine import Normal
from Script.Engine import BreakHitResult
from Script.Engine import Montage_Play
from Script.AkAudio import Default__AkGameplayStatics
from Script.FactoryGame import Default__FGBlueprintFunctionLibrary
from Game.FactoryGame.Equipment.Beacon.Equip_Beacon import ExecuteUbergraph_Equip_Beacon.K2Node_Event_consumable
from Script.Engine import MakeTransform
from Game.FactoryGame.Equipment.Beacon.Audio.Play_EQ_Beacon_Plant import Play_EQ_Beacon_Plant
from Script.Engine import Actor
from Script.Engine import K2_GetActorLocation
from Game.FactoryGame.Equipment.Beacon.Audio.Play_EQ_Beacon_Equip import Play_EQ_Beacon_Equip
from Script.Engine import GetForwardVector
from Script.Engine import Montage_IsPlaying
from Script.FactoryGame import ShouldShowStinger
from Script.AkAudio import AkComponent
from Script.Engine import AnimInstance
from Script.CoreUObject import Transform
from Script.Engine import SkeletalMeshComponent
from Game.FactoryGame.Equipment.Beacon.BP_Beacon import BP_Beacon
from Script.CoreUObject import LinearColor

class Equip_Beacon(FGConsumableEquipment):
    mAttachmentClass = NewObject[Attach_Beacon]()
    mEquipmentSlot = EEquipmentSlot::ES_ARMS
    mAttachSocket = hand_rSocket
    mArmAnimation = EArmEquipment::AE_OneHandEquipment
    mIdlePoseAnimation3p = Namespace(AssetPath='/Game/FactoryGame/Character/Player/Animation/ThirdPerson/MedkitIdle_01.MedkitIdle_01')
    PrimaryActorTick = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=False, bTickEvenWhenPaused=False)
    bOnlyRelevantToOwner = True
    bNetUseOwnerRelevancy = True
    bReplicates = True
    RemoteRole = 1
    
    def SpawnBeacon(self):
        ReturnValue: Ptr[FGCharacterPlayer] = self.GetInstigatorCharacter()
        
        OutLocation = None
        OutRotation = None
        ReturnValue.GetActorEyesViewPoint(Ref[OutLocation], Ref[OutRotation])
        ReturnValue_0: Vector = GetForwardVector(OutRotation)
        
        X = None
        Y = None
        Z = None
        X, Y, Z = BreakVector(ReturnValue_0)
        ReturnValue_1: Vector = Vector(X, Y, 0)
        ReturnValue_2: Vector = Normal(ReturnValue_1, 9.999999747378752e-05)
        ReturnValue_3: Vector = ReturnValue_2 * 150
        ReturnValue_4: Vector = OutLocation + ReturnValue_3
        ReturnValue_5: Vector = Subtract_VectorVector(ReturnValue_4, Vector(0, 0, 1000))
        
        Variable = None
        OutHit = None
        ReturnValue_6: bool = Default__KismetSystemLibrary.LineTraceSingle(self, ReturnValue_4, ReturnValue_5, 0, False, 0, True, LinearColor(R = 1, G = 0, B = 0, A = 1), LinearColor(R = 0, G = 1, B = 0, A = 1), 5, Ref[Variable], Ref[OutHit])
        
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
        if not bBlockingHit:
            goto('L1476')
        ReturnValue_7: Ptr[Pawn] = self.GetInstigator()
        
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
        ReturnValue_8: Transform = MakeTransform(Location, Rotator::FromPitchYawRoll(0, 0, 0), Vector(1, 1, 1))
        
        ReturnValue_9: Ptr[Actor] = Default__GameplayStatics.BeginDeferredActorSpawnFromClass(self, BP_Beacon, 0, ReturnValue_7, Ref[ReturnValue_8])
        ReturnValue_7 = self.GetInstigator()
        Default__KismetSystemLibrary.SetObjectPropertyByName(ReturnValue_9, "Instigator", ReturnValue_7)
        
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
        ReturnValue_8 = MakeTransform(Location, Rotator::FromPitchYawRoll(0, 0, 0), Vector(1, 1, 1))
        
        ReturnValue_10: Ptr[BP_Beacon] = Default__GameplayStatics.FinishSpawningActor(ReturnValue_9, Ref[ReturnValue_8])
    

    def WasEquipped(self):
        self.ExecuteUbergraph_Equip_Beacon(181)
    

    def WasUnEquipped(self):
        self.ExecuteUbergraph_Equip_Beacon(1433)
    

    def PlayConsumeEffects(self):
        ExecuteUbergraph_Equip_Beacon.K2Node_Event_consumable = consumable #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Equip_Beacon(1900)
    

    def ExecuteUbergraph_Equip_Beacon(self):
        goto(ComputedJump("EntryPoint"))
        # Label 15
        self.OnPrimaryFire()
        ReturnValue: Vector = self.K2_GetActorLocation()
        ReturnValue_0: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEventAtLocation(self, Play_EQ_Beacon_Plant, ReturnValue, Rotator::FromPitchYawRoll(0, 0, 0))
        ReturnValue3: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Stop_EQ_Beacon_Stinger, self, True)
        goto(ExecutionFlow.Pop())
        self.WasEquipped()
        ReturnValue3_0: Ptr[FGCharacterPlayer] = self.GetInstigatorCharacter()
        ReturnValue_1: bool = Default__FGBlueprintFunctionLibrary.IsLocallyHumanControlled(ReturnValue3_0)
        if not ReturnValue_1:
           goto(ExecutionFlow.Pop())
        ReturnValue_2: bool = self.ShouldShowStinger()
        if not ReturnValue_2:
            goto('L481')
        ExecutionFlow.Push("L980")
        ReturnValue_3: Ptr[FGCharacterPlayer] = self.GetInstigatorCharacter()
        ReturnValue_4: Ptr[SkeletalMeshComponent] = ReturnValue_3.GetMesh1P()
        ReturnValue2: Ptr[AnimInstance] = ReturnValue_4.GetAnimInstance()
        ReturnValue1: bool = ReturnValue2.Montage_IsPlaying(BeaconStinger_02_Montage)
        if not ReturnValue1:
            goto('L1203')
        goto(ExecutionFlow.Pop())
        # Label 481
        ReturnValue1_0: Ptr[AnimInstance] = self.Bacon_skl.GetAnimInstance()
        ReturnValue_5: bool = ReturnValue1_0.IsAnyMontagePlaying()
        if not ReturnValue_5:
            goto('L580')
        goto(ExecutionFlow.Pop())
        # Label 580
        ReturnValue1_1: Ptr[FGCharacterPlayer] = self.GetInstigatorCharacter()
        ReturnValue1_2: Ptr[SkeletalMeshComponent] = ReturnValue1_1.GetMesh1P()
        ReturnValue3_1: Ptr[AnimInstance] = ReturnValue1_2.GetAnimInstance()
        ReturnValue2_0: bool = ReturnValue3_1.Montage_IsPlaying(OneHandEquipmentEquip_01_Montage)
        if not ReturnValue2_0:
            goto('L750')
        goto(ExecutionFlow.Pop())
        # Label 750
        ReturnValue1_1 = self.GetInstigatorCharacter()
        ReturnValue1_2 = ReturnValue1_1.GetMesh1P()
        ReturnValue3_1 = ReturnValue1_2.GetAnimInstance()
        ReturnValue2_1: float = ReturnValue3_1.Montage_Play(OneHandEquipmentEquip_01_Montage, 1, 0, 0, True)
        ReturnValue2_2: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_EQ_Beacon_Equip, self, True)
        goto(ExecutionFlow.Pop())
        # Label 980
        ReturnValue_6: Ptr[AnimInstance] = self.Bacon_skl.GetAnimInstance()
        ReturnValue_7: bool = ReturnValue_6.Montage_IsPlaying(BeaconStinger_02_Montage)
        if not ReturnValue_7:
            goto('L1088')
        goto(ExecutionFlow.Pop())
        # Label 1088
        ReturnValue_6 = self.Bacon_skl.GetAnimInstance()
        ReturnValue_8: float = ReturnValue_6.Montage_Play(BeaconStinger_02_Montage, 1, 0, 0, True)
        goto(ExecutionFlow.Pop())
        # Label 1203
        ReturnValue_3 = self.GetInstigatorCharacter()
        ReturnValue_4 = ReturnValue_3.GetMesh1P()
        ReturnValue2 = ReturnValue_4.GetAnimInstance()
        ReturnValue1_3: float = ReturnValue2.Montage_Play(BeaconStinger_02_Montage, 1, 0, 0, True)
        ReturnValue_9: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_EQ_Beacon_Stinger, self, True)
        goto(ExecutionFlow.Pop())
        self.WasUnEquipped()
        ReturnValue4: Ptr[FGCharacterPlayer] = self.GetInstigatorCharacter()
        ReturnValue1_4: bool = Default__FGBlueprintFunctionLibrary.IsLocallyHumanControlled(ReturnValue4)
        if not ReturnValue1_4:
           goto(ExecutionFlow.Pop())
        ReturnValue2_3: Ptr[FGCharacterPlayer] = self.GetInstigatorCharacter()
        ReturnValue2_4: Ptr[SkeletalMeshComponent] = ReturnValue2_3.GetMesh1P()
        ReturnValue5: Ptr[AnimInstance] = ReturnValue2_4.GetAnimInstance()
        ReturnValue1_5: Ptr[AnimMontage] = ReturnValue5.GetCurrentActiveMontage()
        ReturnValue5.Montage_Stop(0, ReturnValue1_5)
        ReturnValue4_0: Ptr[AnimInstance] = self.Bacon_skl.GetAnimInstance()
        ReturnValue_10: Ptr[AnimMontage] = ReturnValue4_0.GetCurrentActiveMontage()
        ReturnValue4_0.Montage_Stop(0, ReturnValue_10)
        ReturnValue1_6: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Stop_EQ_Beacon_Stinger, self, True)
        goto(ExecutionFlow.Pop())
        self.PlayConsumeEffects(consumable)
        goto('L15')
    
