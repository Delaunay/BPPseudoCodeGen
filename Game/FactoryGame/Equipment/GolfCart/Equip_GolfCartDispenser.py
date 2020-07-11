
from codegen.ue4_stub import *

from Script.AkAudio import PostAkEvent
from Game.FactoryGame.Equipment.PortableMiner.Audio.Play_EQ_PM_Equip import Play_EQ_PM_Equip
from Script.Engine import FinishSpawningActor
from Script.FactoryGame import FGCharacterPlayer
from Script.FactoryGame import FGGolfCartDispenser
from Game.FactoryGame.Equipment.GolfCart.Equip_GolfCartDispenser import ExecuteUbergraph_Equip_GolfCartDispenser.K2Node_CustomEvent_golfCart
from Script.FactoryGame import GetInstigatorCharacter
from Script.FactoryGame import WasEquipped
from Script.FactoryGame import WasUnEquipped
from Game.FactoryGame.Equipment.GolfCart.Equip_GolfCartDispenser import ExecuteUbergraph_Equip_GolfCartDispenser
from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import GetAnimInstance
from Script.Engine import GetCurrentActiveMontage
from Script.FactoryGame import IsLocalInstigator
from Script.Engine import BeginDeferredActorSpawnFromClass
from Game.FactoryGame.Buildable.Vehicle.Golfcart.BP_Golfcart import BP_Golfcart
from Script.Engine import Montage_Stop
from Game.FactoryGame.Character.Player.Audio.SB_CharacterEssentials.Play_P_ResourcePickUp import Play_P_ResourcePickUp
from Script.FactoryGame import GetMesh1P
from Script.FactoryGame import FGInventoryComponentEquipment
from Script.Engine import LineTraceSingle
from Script.Engine import Default__GameplayStatics
from Script.FactoryGame import GetActiveIndex
from Script.Engine import AnimMontage
from Script.CoreUObject import Vector
from Script.Engine import BreakHitResult
from Script.Engine import Montage_Play
from Script.AkAudio import Default__AkGameplayStatics
from Script.Engine import MakeTransform
from Script.Engine import Actor
from Script.Engine import GetForwardVector
from Script.Engine import Montage_IsPlaying
from Script.Engine import AnimInstance
from Script.AkAudio import AkComponent
from Game.FactoryGame.Character.Player.Animation.FirstPerson.GolfcartEquip_01_Montage import GolfcartEquip_01_Montage
from Script.FactoryGame import GetEquipmentSlot
from Script.CoreUObject import Transform
from Script.Engine import SkeletalMeshComponent
from Script.FactoryGame import RemoveAllFromIndex
from Script.CoreUObject import LinearColor

class Equip_GolfCartDispenser(FGGolfCartDispenser):
    mPlaceDistanceMax = 1000
    mAttachmentClass = NewObject[Attach_GolfCartDispenser]()
    mEquipmentSlot = EEquipmentSlot::ES_ARMS
    mAttachSocket = hand_rSocket
    mArmAnimation = EArmEquipment::AE_Generic2Hand
    mIdlePoseAnimation = Namespace(AssetPath='/Game/FactoryGame/Character/Player/Animation/FirstPerson/GolfcartIdle_01.GolfcartIdle_01')
    mIdlePoseAnimation3p = Namespace(AssetPath='/Game/FactoryGame/Character/Player/Animation/ThirdPerson/GolfcartIdle_01.GolfcartIdle_01')
    PrimaryActorTick = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=False, bTickEvenWhenPaused=False)
    bOnlyRelevantToOwner = True
    bNetUseOwnerRelevancy = True
    bReplicates = True
    RemoteRole = 1
    
    def WasEquipped(self):
        self.ExecuteUbergraph_Equip_GolfCartDispenser(791)
    

    def PlaySpawnEffects(self, GolfCart: Ptr[BP_Golfcart]):
        ExecuteUbergraph_Equip_GolfCartDispenser.K2Node_CustomEvent_golfCart = GolfCart #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Equip_GolfCartDispenser(796)
    

    def WasUnEquipped(self):
        self.ExecuteUbergraph_Equip_GolfCartDispenser(816)
    

    def SpawnGolfCart(self):
        self.ExecuteUbergraph_Equip_GolfCartDispenser(1004)
    

    def ExecuteUbergraph_Equip_GolfCartDispenser(self):
        # Label 10
        self.WasEquipped()
        ReturnValue1: bool = self.IsLocalInstigator()
        if not ReturnValue1:
            goto('L2185')
        ReturnValue1_0: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_EQ_PM_Equip, self, True)
        ReturnValue: Ptr[FGCharacterPlayer] = self.GetInstigatorCharacter()
        ReturnValue_0: Ptr[SkeletalMeshComponent] = ReturnValue.GetMesh1P()
        ReturnValue_1: Ptr[AnimInstance] = ReturnValue_0.GetAnimInstance()
        ReturnValue_2: bool = ReturnValue_1.Montage_IsPlaying(GolfcartEquip_01_Montage)
        if not ReturnValue_2:
            goto('L281')
        # End
        # Label 281
        ReturnValue = self.GetInstigatorCharacter()
        ReturnValue_0 = ReturnValue.GetMesh1P()
        ReturnValue_1 = ReturnValue_0.GetAnimInstance()
        ReturnValue_3: float = ReturnValue_1.Montage_Play(GolfcartEquip_01_Montage, 1, 0, 0, True)
        # End
        # Label 462
        ReturnValue_4: bool = self.IsLocalInstigator()
        if not ReturnValue_4:
            goto('L2185')
        ReturnValue2: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(None, self, True)
        ReturnValue_5: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_P_ResourcePickUp, self, True)
        ReturnValue1_1: Ptr[FGCharacterPlayer] = self.GetInstigatorCharacter()
        ReturnValue1_2: Ptr[SkeletalMeshComponent] = ReturnValue1_1.GetMesh1P()
        ReturnValue1_3: Ptr[AnimInstance] = ReturnValue1_2.GetAnimInstance()
        ReturnValue_6: Ptr[AnimMontage] = ReturnValue1_3.GetCurrentActiveMontage()
        ReturnValue1_3.Montage_Stop(0, ReturnValue_6)
        # End
        goto('L10')
        # End
        # Label 801
        self.WasUnEquipped()
        goto('L462')
        goto('L801')
        # Label 821
        ReturnValue2_0: Ptr[FGCharacterPlayer] = self.GetInstigatorCharacter()
        ReturnValue_7: Ptr[FGInventoryComponentEquipment] = ReturnValue2_0.GetEquipmentSlot(1)
        ReturnValue_8: int32 = ReturnValue_7.GetActiveIndex()
        ReturnValue_7.RemoveAllFromIndex(ReturnValue_8)
        self.PlaySpawnEffects(ReturnValue_9)
        # End
        ReturnValue3: Ptr[FGCharacterPlayer] = self.GetInstigatorCharacter()
        
        OutLocation = None
        OutRotation = None
        ReturnValue3.GetActorEyesViewPoint(Ref[OutLocation], Ref[OutRotation])
        ReturnValue_9: Vector = GetForwardVector(OutRotation)
        ReturnValue_10: Vector = ReturnValue_9 * 3000
        ReturnValue_11: Vector = OutLocation + ReturnValue_10
        
        Variable = None
        OutHit = None
        ReturnValue_12: bool = Default__KismetSystemLibrary.LineTraceSingle(self, OutLocation, ReturnValue_11, 0, False, 0, True, LinearColor(R = 1, G = 0, B = 0, A = 1), LinearColor(R = 0, G = 1, B = 0, A = 1), 5, Ref[Variable], Ref[OutHit])
        
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
            goto('L2185')
        
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
        ReturnValue_13: Transform = MakeTransform(Location, Rotator::FromPitchYawRoll(0, 0, 0), Vector(1, 1, 1))
        
        ReturnValue_14: Ptr[Actor] = Default__GameplayStatics.BeginDeferredActorSpawnFromClass(self, BP_Golfcart, 2, None, Ref[ReturnValue_13])
        
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
        ReturnValue_13 = MakeTransform(Location, Rotator::FromPitchYawRoll(0, 0, 0), Vector(1, 1, 1))
        
        ReturnValue_9 = Default__GameplayStatics.FinishSpawningActor(ReturnValue_14, Ref[ReturnValue_13])
        goto('L821')
    
