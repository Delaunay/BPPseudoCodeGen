
from codegen.ue4_stub import *

from Script.FactoryGame import FGResourceDescriptor
from Script.FactoryGame import FGCharacterPlayer
from Script.Engine import Controller
from Game.FactoryGame.Character.Player.Animation.FirstPerson.MineMontage_01 import MineMontage_01
from Script.FactoryGame import GetInstigatorCharacter
from Script.Engine import Pawn
from Script.FactoryGame import WasEquipped
from Script.Engine import SpawnEmitterAtLocation
from Script.Engine import SpawnEmitterAttached
from Script.CoreUObject import Rotator
from Script.Engine import GetInstigator
from Game.FactoryGame.Equipment.ResourceCollector.Animation.RockPickMine_01_Montage import RockPickMine_01_Montage
from Script.FactoryGame import GetResourceNode
from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import GetAnimInstance
from Script.FactoryGame import GetFactoryMiningParticle
from Script.Engine import PlayerController
from Script.Engine import GetController
from Script.Engine import DecalComponent
from Script.FactoryGame import Default__FGResourceDescriptor
from Game.FactoryGame.Equipment.ResourceCollector.Particle.MiningHit import MiningHit
from Script.CoreUObject import Object
from Script.Engine import GetCameraRotation
from Script.Engine import IsValid
from Game.FactoryGame.Character.Player.CameraShake.BuildGunMine_01_CameraAnim import BuildGunMine_01_CameraAnim
from Script.FactoryGame import GetMesh1P
from Script.Engine import LineTraceSingle
from Game.FactoryGame.Equipment.ResourceCollector.Equip_ResourceMiner import ExecuteUbergraph_Equip_ResourceMiner
from Script.Engine import Default__GameplayStatics
from Script.Engine import BreakRotator
from Script.Engine import ParticleSystem
from Script.CoreUObject import Vector
from Script.FactoryGame import FGResourceNode
from Game.FactoryGame.Equipment.ResourceCollector.Material.Decals_Crack import Decals_Crack
from Script.Engine import BreakHitResult
from Script.Engine import Montage_Play
from Script.Engine import MakeRotator
from Script.Engine import K2_DestroyComponent
from Script.FactoryGame import FGResourceMiner
from Game.FactoryGame.Equipment.ResourceCollector.Animation.RockPickMineStop_01_Montage import RockPickMineStop_01_Montage
from Script.Engine import ParticleSystemComponent
from Script.Engine import MakeRotFromX
from Script.Engine import GetForwardVector
from Script.Engine import AnimInstance
from Game.FactoryGame.VFX.Character.Player.Mining.P_MiningHitComplete_01 import P_MiningHitComplete_01
from Game.FactoryGame.Character.Player.Animation.FirstPerson.BuildgunMineEnd_01_Montage import BuildgunMineEnd_01_Montage
from Script.Engine import SpawnDecalAtLocation
from Script.Engine import SkeletalMeshComponent
from Script.CoreUObject import LinearColor
from Script.Engine import RandomFloatInRange

class Equip_ResourceMiner(FGResourceMiner):
    mCachedWorldGenerator: Ptr[Object]
    mFirstDecal: Ptr[DecalComponent]
    mSecondDecal: Ptr[DecalComponent]
    mThirdDecal: Ptr[DecalComponent]
    mAttachmentClass = NewObject[Attach_ResourceMiner]()
    mEquipmentSlot = EEquipmentSlot::ES_ARMS
    mEquipSound = Namespace(AssetPath='/Game/FactoryGame/Character/Player/Audio/SB_CharacterEssentials/Play_P_ResourcePickUp.Play_P_ResourcePickUp')
    mAttachSocket = hand_rSocket
    mArmAnimation = EArmEquipment::AE_ResourceCollector
    mHasPersistentOwner = True
    PrimaryActorTick = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=False, bTickEvenWhenPaused=False)
    bOnlyRelevantToOwner = True
    bNetUseOwnerRelevancy = True
    bReplicates = True
    RemoteRole = 1
    RootComponent = Namespace(ObjectClass='/Script/Engine.SceneComponent', ObjectFlags=2883617, ObjectName='DefaultScene')
    
    def StopMining(self):
        self.ExecuteUbergraph_Equip_ResourceMiner(441)
    

    def StartMining(self):
        self.ExecuteUbergraph_Equip_ResourceMiner(698)
    

    def WasEquipped(self):
        self.ExecuteUbergraph_Equip_ResourceMiner(955)
    

    def PlayFinalEffects(self):
        self.ExecuteUbergraph_Equip_ResourceMiner(1056)
    

    def PlayMiningEffect(self):
        self.ExecuteUbergraph_Equip_ResourceMiner(2685)
    

    def StartCameraShake(self):
        self.ExecuteUbergraph_Equip_ResourceMiner(4514)
    

    def PlaySecondEffects(self):
        self.ExecuteUbergraph_Equip_ResourceMiner(4519)
    

    def ExecuteUbergraph_Equip_ResourceMiner(self):
        goto(ComputedJump("EntryPoint"))
        # Label 15
        ReturnValue: Ptr[AnimInstance] = self.SkeletalMesh.GetAnimInstance()
        ReturnValue_0: float = ReturnValue.Montage_Play(RockPickMine_01_Montage, 1, 0, 0, True)
        goto(ExecutionFlow.Pop())
        # Label 130
        ReturnValue1: Ptr[AnimInstance] = self.SkeletalMesh.GetAnimInstance()
        ReturnValue1_0: float = ReturnValue1.Montage_Play(RockPickMineStop_01_Montage, 1, 0, 0, True)
        ReturnValue2: Ptr[Pawn] = self.GetInstigator()
        ReturnValue1_1: Ptr[Controller] = ReturnValue2.GetController()
        Controller1: Ptr[PlayerController] = Cast[PlayerController](ReturnValue1_1)
        bSuccess1: bool = Controller1
        if not bSuccess1:
           goto(ExecutionFlow.Pop())
        Controller1.PlayerCameraManager.StopAllCameraAnims(True)
        goto(ExecutionFlow.Pop())
        ReturnValue1_2: Ptr[FGCharacterPlayer] = self.GetInstigatorCharacter()
        ReturnValue2_0: bool = ReturnValue1_2.IsLocallyControlled()
        if not ReturnValue2_0:
           goto(ExecutionFlow.Pop())
        ReturnValue1_2 = self.GetInstigatorCharacter()
        ReturnValue_1: Ptr[SkeletalMeshComponent] = ReturnValue1_2.GetMesh1P()
        ReturnValue2_1: Ptr[AnimInstance] = ReturnValue_1.GetAnimInstance()
        ReturnValue2_2: float = ReturnValue2_1.Montage_Play(BuildgunMineEnd_01_Montage, 1, 0, 0, True)
        goto('L130')
        ReturnValue_2: Ptr[FGCharacterPlayer] = self.GetInstigatorCharacter()
        ReturnValue1_3: bool = ReturnValue_2.IsLocallyControlled()
        if not ReturnValue1_3:
           goto(ExecutionFlow.Pop())
        ReturnValue_2 = self.GetInstigatorCharacter()
        ReturnValue1_4: Ptr[SkeletalMeshComponent] = ReturnValue_2.GetMesh1P()
        ReturnValue3: Ptr[AnimInstance] = ReturnValue1_4.GetAnimInstance()
        ReturnValue3_0: float = ReturnValue3.Montage_Play(MineMontage_01, 1, 0, 0, True)
        goto('L15')
        self.WasEquipped()
        ReturnValue_3: Ptr[Pawn] = self.GetInstigator()
        ReturnValue_4: bool = ReturnValue_3.IsLocallyControlled()
        if not ReturnValue_4:
           goto(ExecutionFlow.Pop())
        self.StartMining()
        goto(ExecutionFlow.Pop())
        self.mSecondDecal.K2_DestroyComponent(self)
        ReturnValue5: Ptr[Pawn] = self.GetInstigator()
        ReturnValue4: Ptr[Controller] = ReturnValue5.GetController()
        Controller4: Ptr[PlayerController] = Cast[PlayerController](ReturnValue4)
        bSuccess4: bool = Controller4
        if not bSuccess4:
           goto(ExecutionFlow.Pop())
        ReturnValue4_0: Ptr[FGCharacterPlayer] = self.GetInstigatorCharacter()
        ReturnValue4_1: Ptr[SkeletalMeshComponent] = ReturnValue4_0.GetMesh1P()
        ReturnValue2_3: Vector = ReturnValue4_1.GetSocketLocation("ArmBaseSocket")
        ReturnValue2_4: Rotator = Controller4.PlayerCameraManager.GetCameraRotation()
        ReturnValue2_5: Vector = GetForwardVector(ReturnValue2_4)
        ReturnValue2_6: Vector = ReturnValue2_5 * 300
        ReturnValue2_7: Vector = ReturnValue2_3 + ReturnValue2_6
        
        Variable2 = None
        OutHit2 = None
        ReturnValue2_8: bool = Default__KismetSystemLibrary.LineTraceSingle(self, ReturnValue2_3, ReturnValue2_7, 0, False, 0, True, LinearColor(R = 1, G = 0, B = 0, A = 1), LinearColor(R = 0, G = 1, B = 0, A = 1), 5, Ref[Variable2], Ref[OutHit2])
        ReturnValue_5: Ptr[FGResourceNode] = self.GetResourceNode()
        ReturnValue_6: TSubclassOf[FGResourceDescriptor] = GetInterfaceUObject(ReturnValue_5).GetResourceClass()
        ReturnValue_7: Ptr[ParticleSystem] = Default__FGResourceDescriptor.GetFactoryMiningParticle(ReturnValue_6)
        
        OutHit2 = None
        bBlockingHit2 = None
        bInitialOverlap2 = None
        Time2 = None
        Distance2 = None
        Location2 = None
        ImpactPoint2 = None
        Normal2 = None
        ImpactNormal2 = None
        PhysMat2 = None
        HitActor2 = None
        HitComponent2 = None
        HitBoneName2 = None
        HitItem2 = None
        FaceIndex2 = None
        TraceStart2 = None
        TraceEnd2 = None
        Default__GameplayStatics.BreakHitResult(Ref[OutHit2], Ref[bBlockingHit2], Ref[bInitialOverlap2], Ref[Time2], Ref[Distance2], Ref[Location2], Ref[ImpactPoint2], Ref[Normal2], Ref[ImpactNormal2], Ref[PhysMat2], Ref[HitActor2], Ref[HitComponent2], Ref[HitBoneName2], Ref[HitItem2], Ref[FaceIndex2], Ref[TraceStart2], Ref[TraceEnd2])
        ReturnValue2_9: Ptr[ParticleSystemComponent] = Default__GameplayStatics.SpawnEmitterAtLocation(self, ReturnValue_7, Location2, Rotator::FromPitchYawRoll(0, 0, 0), Vector(1, 1, 1), True, 0)
        ReturnValue2_10: float = RandomFloatInRange(-180, 180)
        
        OutHit2 = None
        bBlockingHit2 = None
        bInitialOverlap2 = None
        Time2 = None
        Distance2 = None
        Location2 = None
        ImpactPoint2 = None
        Normal2 = None
        ImpactNormal2 = None
        PhysMat2 = None
        HitActor2 = None
        HitComponent2 = None
        HitBoneName2 = None
        HitItem2 = None
        FaceIndex2 = None
        TraceStart2 = None
        TraceEnd2 = None
        Default__GameplayStatics.BreakHitResult(Ref[OutHit2], Ref[bBlockingHit2], Ref[bInitialOverlap2], Ref[Time2], Ref[Distance2], Ref[Location2], Ref[ImpactPoint2], Ref[Normal2], Ref[ImpactNormal2], Ref[PhysMat2], Ref[HitActor2], Ref[HitComponent2], Ref[HitBoneName2], Ref[HitItem2], Ref[FaceIndex2], Ref[TraceStart2], Ref[TraceEnd2])
        
        Normal2 = None
        ReturnValue_8: Rotator = MakeRotFromX(Ref[Normal2])
        
        Roll = None
        Pitch = None
        Yaw = None
        BreakRotator(ReturnValue_8, Ref[Roll], Ref[Pitch], Ref[Yaw])
        ReturnValue2_11: Rotator = MakeRotator(Roll, -90, ReturnValue2_10)
        ReturnValue2_12: Ptr[DecalComponent] = Default__GameplayStatics.SpawnDecalAtLocation(self, Decals_Crack, Vector(50, 35, 35), Location2, ReturnValue2_11, 3)
        self.mThirdDecal = ReturnValue2_12
        ReturnValue_9: Ptr[ParticleSystemComponent] = Default__GameplayStatics.SpawnEmitterAttached(P_MiningHitComplete_01, self.SkeletalMesh, "handleSocket", Vector(0, 0, 0), Rotator::FromPitchYawRoll(0, 0, 0), Vector(1, 1, 1), 0, True, 0)
        goto(ExecutionFlow.Pop())
        ExecutionFlow.Push("L2785")
        ReturnValue_10: bool = Default__KismetSystemLibrary.IsValid(self.mThirdDecal)
        if not ReturnValue_10:
           goto(ExecutionFlow.Pop())
        self.mThirdDecal.K2_DestroyComponent(self)
        goto(ExecutionFlow.Pop())
        # Label 2785
        ReturnValue3_1: Ptr[Pawn] = self.GetInstigator()
        ReturnValue2_13: Ptr[Controller] = ReturnValue3_1.GetController()
        Controller2: Ptr[PlayerController] = Cast[PlayerController](ReturnValue2_13)
        bSuccess2: bool = Controller2
        if not bSuccess2:
           goto(ExecutionFlow.Pop())
        ReturnValue2_14: Ptr[FGCharacterPlayer] = self.GetInstigatorCharacter()
        ReturnValue2_15: Ptr[SkeletalMeshComponent] = ReturnValue2_14.GetMesh1P()
        ReturnValue_11: Vector = ReturnValue2_15.GetSocketLocation("ArmBaseSocket")
        ReturnValue_12: Rotator = Controller2.PlayerCameraManager.GetCameraRotation()
        ReturnValue_13: Vector = GetForwardVector(ReturnValue_12)
        ReturnValue_14: Vector = ReturnValue_13 * 300
        ReturnValue_15: Vector = ReturnValue_11 + ReturnValue_14
        
        Variable1 = None
        OutHit = None
        ReturnValue_16: bool = Default__KismetSystemLibrary.LineTraceSingle(self, ReturnValue_11, ReturnValue_15, 0, False, 0, True, LinearColor(R = 1, G = 0, B = 0, A = 1), LinearColor(R = 0, G = 1, B = 0, A = 1), 5, Ref[Variable1], Ref[OutHit])
        
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
        ReturnValue1_5: Ptr[FGResourceNode] = self.GetResourceNode()
        ReturnValue1_6: TSubclassOf[FGResourceDescriptor] = GetInterfaceUObject(ReturnValue1_5).GetResourceClass()
        ReturnValue1_7: Ptr[ParticleSystem] = Default__FGResourceDescriptor.GetFactoryMiningParticle(ReturnValue1_6)
        ReturnValue_17: Ptr[ParticleSystemComponent] = Default__GameplayStatics.SpawnEmitterAtLocation(self, ReturnValue1_7, Location, Rotator::FromPitchYawRoll(0, 0, 0), Vector(1, 1, 1), True, 0)
        ReturnValue_18: float = RandomFloatInRange(-180, 180)
        ReturnValue_19: Rotator = MakeRotator(0, -90, ReturnValue_18)
        
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
        ReturnValue_20: Ptr[DecalComponent] = Default__GameplayStatics.SpawnDecalAtLocation(self, Decals_Crack, Vector(50, 25, 25), Location, ReturnValue_19, 3)
        self.mFirstDecal = ReturnValue_20
        ReturnValue2_16: Ptr[ParticleSystemComponent] = Default__GameplayStatics.SpawnEmitterAttached(MiningHit, self.SkeletalMesh, "handleSocket", Vector(0, 0, 0), Rotator::FromPitchYawRoll(0, 0, 0), Vector(1, 1, 1), 0, True, 0)
        goto(ExecutionFlow.Pop())
        # Label 4294
        ReturnValue1_8: Ptr[Pawn] = self.GetInstigator()
        ReturnValue_21: Ptr[Controller] = ReturnValue1_8.GetController()
        Controller: Ptr[PlayerController] = Cast[PlayerController](ReturnValue_21)
        bSuccess: bool = Controller
        if not bSuccess:
           goto(ExecutionFlow.Pop())
        Controller.ClientPlayCameraAnim(BuildGunMine_01_CameraAnim, 1, 1, 0, 0, False, False, 0, Rotator::FromPitchYawRoll(0, 0, 0))
        goto(ExecutionFlow.Pop())
        goto('L4294')
        self.mFirstDecal.K2_DestroyComponent(self)
        ReturnValue4_2: Ptr[Pawn] = self.GetInstigator()
        ReturnValue3_2: Ptr[Controller] = ReturnValue4_2.GetController()
        Controller3: Ptr[PlayerController] = Cast[PlayerController](ReturnValue3_2)
        bSuccess3: bool = Controller3
        if not bSuccess3:
           goto(ExecutionFlow.Pop())
        ReturnValue3_3: Ptr[FGCharacterPlayer] = self.GetInstigatorCharacter()
        ReturnValue3_4: Ptr[SkeletalMeshComponent] = ReturnValue3_3.GetMesh1P()
        ReturnValue1_9: Vector = ReturnValue3_4.GetSocketLocation("ArmBaseSocket")
        ReturnValue1_10: Rotator = Controller3.PlayerCameraManager.GetCameraRotation()
        ReturnValue1_11: Vector = GetForwardVector(ReturnValue1_10)
        ReturnValue1_12: Vector = ReturnValue1_11 * 300
        ReturnValue1_13: Vector = ReturnValue1_9 + ReturnValue1_12
        
        Variable = None
        OutHit1 = None
        ReturnValue1_14: bool = Default__KismetSystemLibrary.LineTraceSingle(self, ReturnValue1_9, ReturnValue1_13, 0, False, 0, True, LinearColor(R = 1, G = 0, B = 0, A = 1), LinearColor(R = 0, G = 1, B = 0, A = 1), 5, Ref[Variable], Ref[OutHit1])
        
        OutHit1 = None
        bBlockingHit1 = None
        bInitialOverlap1 = None
        Time1 = None
        Distance1 = None
        Location1 = None
        ImpactPoint1 = None
        Normal1 = None
        ImpactNormal1 = None
        PhysMat1 = None
        HitActor1 = None
        HitComponent1 = None
        HitBoneName1 = None
        HitItem1 = None
        FaceIndex1 = None
        TraceStart1 = None
        TraceEnd1 = None
        Default__GameplayStatics.BreakHitResult(Ref[OutHit1], Ref[bBlockingHit1], Ref[bInitialOverlap1], Ref[Time1], Ref[Distance1], Ref[Location1], Ref[ImpactPoint1], Ref[Normal1], Ref[ImpactNormal1], Ref[PhysMat1], Ref[HitActor1], Ref[HitComponent1], Ref[HitBoneName1], Ref[HitItem1], Ref[FaceIndex1], Ref[TraceStart1], Ref[TraceEnd1])
        ReturnValue2_17: Ptr[FGResourceNode] = self.GetResourceNode()
        ReturnValue2_18: TSubclassOf[FGResourceDescriptor] = GetInterfaceUObject(ReturnValue2_17).GetResourceClass()
        ReturnValue2_19: Ptr[ParticleSystem] = Default__FGResourceDescriptor.GetFactoryMiningParticle(ReturnValue2_18)
        ReturnValue1_15: Ptr[ParticleSystemComponent] = Default__GameplayStatics.SpawnEmitterAtLocation(self, ReturnValue2_19, Location1, Rotator::FromPitchYawRoll(0, 0, 0), Vector(1, 1, 1), True, 0)
        ReturnValue1_16: float = RandomFloatInRange(-180, 180)
        ReturnValue1_17: Rotator = MakeRotator(0, -90, ReturnValue1_16)
        
        OutHit1 = None
        bBlockingHit1 = None
        bInitialOverlap1 = None
        Time1 = None
        Distance1 = None
        Location1 = None
        ImpactPoint1 = None
        Normal1 = None
        ImpactNormal1 = None
        PhysMat1 = None
        HitActor1 = None
        HitComponent1 = None
        HitBoneName1 = None
        HitItem1 = None
        FaceIndex1 = None
        TraceStart1 = None
        TraceEnd1 = None
        Default__GameplayStatics.BreakHitResult(Ref[OutHit1], Ref[bBlockingHit1], Ref[bInitialOverlap1], Ref[Time1], Ref[Distance1], Ref[Location1], Ref[ImpactPoint1], Ref[Normal1], Ref[ImpactNormal1], Ref[PhysMat1], Ref[HitActor1], Ref[HitComponent1], Ref[HitBoneName1], Ref[HitItem1], Ref[FaceIndex1], Ref[TraceStart1], Ref[TraceEnd1])
        ReturnValue1_18: Ptr[DecalComponent] = Default__GameplayStatics.SpawnDecalAtLocation(self, Decals_Crack, Vector(50, 30, 30), Location1, ReturnValue1_17, 3)
        self.mSecondDecal = ReturnValue1_18
        ReturnValue1_19: Ptr[ParticleSystemComponent] = Default__GameplayStatics.SpawnEmitterAttached(MiningHit, self.SkeletalMesh, "handleSocket", Vector(0, 0, 0), Rotator::FromPitchYawRoll(0, 0, 0), Vector(1, 1, 1), 0, True, 0)
        goto(ExecutionFlow.Pop())
    
