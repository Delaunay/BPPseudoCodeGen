
from codegen.ue4_stub import *

from Script.Engine import FinishSpawningActor
from Script.FactoryGame import BreakInventoryStack
from Script.FactoryGame import FGCharacterPlayer
from Script.FactoryGame import GetInstigatorCharacter
from Script.FactoryGame import WasEquipped
from Script.CoreUObject import Rotator
from Script.FactoryGame import Default__FGInventoryLibrary
from Game.FactoryGame.Character.Player.Animation.FirstPerson.DecorEquip_01_Montage import DecorEquip_01_Montage
from Script.FactoryGame import Default__FGDecorationDescriptor
from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import GetAnimInstance
from Script.FactoryGame import GetDecorationActorClass
from Script.Engine import IsValid
from Script.FactoryGame import IsLocalInstigator
from Script.Engine import BeginDeferredActorSpawnFromClass
from Script.FactoryGame import GetMesh1P
from Script.Engine import LineTraceSingle
from Script.FactoryGame import FGInventoryComponentEquipment
from Script.Engine import Default__GameplayStatics
from Script.Engine import BreakRotator
from Script.Engine import FlushNetDormancy
from Script.FactoryGame import GetActiveIndex
from Script.CoreUObject import Vector
from Script.FactoryGame import FGDecorationActor
from Script.Engine import BreakHitResult
from Game.FactoryGame.Equipment.Decoration.Equip_Decoration import ExecuteUbergraph_Equip_Decoration
from Script.Engine import Montage_Play
from Script.Engine import MakeRotator
from Script.Engine import MakeTransform
from Script.FactoryGame import FGEquipmentDecoration
from Script.Engine import Actor
from Script.FactoryGame import GetStackFromIndex
from Script.Engine import GetForwardVector
from Script.FactoryGame import FGDecorationDescriptor
from Script.FactoryGame import GetEquipmentSlot
from Script.FactoryGame import BreakInventoryItem
from Script.Engine import AnimInstance
from Script.Engine import IsValidClass
from Script.CoreUObject import Transform
from Script.Engine import SkeletalMeshComponent
from Script.FactoryGame import RemoveAllFromIndex
from Script.Engine import StaticMesh
from Script.CoreUObject import LinearColor

class Equip_Decoration(FGEquipmentDecoration):
    mCachedDescriptorClass: TSubclassOf[FGDecorationDescriptor]
    mPlaceDistanceMax = 1000
    mAttachmentClass = NewObject[Attach_Decoration]()
    mEquipmentSlot = EEquipmentSlot::ES_ARMS
    mAttachSocket = hand_rSocket
    mArmAnimation = EArmEquipment::AE_Generic1Hand
    mIdlePoseAnimation = Namespace(AssetPath='/Game/FactoryGame/Character/Player/Animation/FirstPerson/DecorIdle_01.DecorIdle_01')
    mIdlePoseAnimation3p = Namespace(AssetPath='/Game/FactoryGame/Character/Player/Animation/ThirdPerson/Consumablesdle_01.Consumablesdle_01')
    PrimaryActorTick = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=False, bTickEvenWhenPaused=False)
    bOnlyRelevantToOwner = True
    bNetUseOwnerRelevancy = True
    bReplicates = True
    RemoteRole = 1
    
    def SetupActor(self, InActor: Ptr[Actor]):
        Actor: Ptr[FGDecorationActor] = Cast[FGDecorationActor](InActor)
        bSuccess: bool = Actor
        if not bSuccess:
            goto('L152')
        Actor.FlushNetDormancy()
        Actor.mDecorationDescriptor = self.mCachedDescriptorClass
    

    def CacheDescriptor(self):
        ReturnValue: Ptr[FGCharacterPlayer] = self.GetInstigatorCharacter()
        ReturnValue_0: Ptr[FGInventoryComponentEquipment] = ReturnValue.GetEquipmentSlot(1)
        ReturnValue_1: int32 = ReturnValue_0.GetActiveIndex()
        
        stack = None
        ReturnValue_2: bool = ReturnValue_0.GetStackFromIndex(ReturnValue_1, Ref[stack])
        
        stack = None
        numItems = None
        item = None
        Default__FGInventoryLibrary.BreakInventoryStack(Ref[stack], Ref[numItems], Ref[item])
        
        item = None
        itemClass = None
        itemState = None
        Default__FGInventoryLibrary.BreakInventoryItem(Ref[item], Ref[itemClass], Ref[itemState])
        Descriptor: TSubclassOf[FGDecorationDescriptor] = ClassCast[FGDecorationDescriptor](itemClass)
        bSuccess: bool = Descriptor
        if not bSuccess:
            goto('L390')
        self.mCachedDescriptorClass = Descriptor
    

    def WasEquipped(self):
        self.ExecuteUbergraph_Equip_Decoration(10)
    

    def SpawnDecoration(self):
        self.ExecuteUbergraph_Equip_Decoration(684)
    

    def ExecuteUbergraph_Equip_Decoration(self):
        self.WasEquipped()
        self.CacheDescriptor()
        ReturnValue: bool = self.IsLocalInstigator()
        if not ReturnValue:
            goto('L2381')
        ReturnValue_0: Ptr[StaticMesh] = Default__FGDecorationDescriptor.GetMesh1P(self.mCachedDescriptorClass)
        ReturnValue_1: bool = self.StaticMesh.SetStaticMesh(ReturnValue_0)
        ReturnValue3: Ptr[FGCharacterPlayer] = self.GetInstigatorCharacter()
        ReturnValue1: Ptr[SkeletalMeshComponent] = ReturnValue3.GetMesh1P()
        ReturnValue_2: Ptr[AnimInstance] = ReturnValue1.GetAnimInstance()
        ReturnValue_3: bool = Default__KismetSystemLibrary.IsValid(ReturnValue_2)
        if not ReturnValue_3:
            goto('L2381')
        ReturnValue3 = self.GetInstigatorCharacter()
        ReturnValue1 = ReturnValue3.GetMesh1P()
        ReturnValue_2 = ReturnValue1.GetAnimInstance()
        ReturnValue_4: float = ReturnValue_2.Montage_Play(DecorEquip_01_Montage, 1, 0, 0, True)
        # End
        # Label 524
        ReturnValue_5: Ptr[FGCharacterPlayer] = self.GetInstigatorCharacter()
        ReturnValue_6: Ptr[FGInventoryComponentEquipment] = ReturnValue_5.GetEquipmentSlot(1)
        ReturnValue_7: int32 = ReturnValue_6.GetActiveIndex()
        ReturnValue_6.RemoveAllFromIndex(ReturnValue_7)
        # End
        ReturnValue_8: TSubclassOf[Actor] = Default__FGDecorationDescriptor.GetDecorationActorClass(self.mCachedDescriptorClass)
        ReturnValue_9: bool = Default__KismetSystemLibrary.IsValidClass(ReturnValue_8)
        if not ReturnValue_9:
            goto('L2381')
        ReturnValue1_0: Ptr[FGCharacterPlayer] = self.GetInstigatorCharacter()
        
        OutLocation = None
        OutRotation = None
        ReturnValue1_0.GetActorEyesViewPoint(Ref[OutLocation], Ref[OutRotation])
        ReturnValue_10: Vector = GetForwardVector(OutRotation)
        ReturnValue_11: Vector = ReturnValue_10 * 3000
        ReturnValue_12: Vector = OutLocation + ReturnValue_11
        
        Variable = None
        OutHit = None
        ReturnValue_13: bool = Default__KismetSystemLibrary.LineTraceSingle(self, OutLocation, ReturnValue_12, 0, False, 0, True, LinearColor(R = 1, G = 0, B = 0, A = 1), LinearColor(R = 0, G = 1, B = 0, A = 1), 5, Ref[Variable], Ref[OutHit])
        
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
            goto('L2381')
        
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
        ReturnValue1_1: TSubclassOf[Actor] = Default__FGDecorationDescriptor.GetDecorationActorClass(self.mCachedDescriptorClass)
        ReturnValue2: Ptr[FGCharacterPlayer] = self.GetInstigatorCharacter()
        
        OutLocation1 = None
        OutRotation1 = None
        ReturnValue2.GetActorEyesViewPoint(Ref[OutLocation1], Ref[OutRotation1])
        
        Roll = None
        Pitch = None
        Yaw = None
        BreakRotator(OutRotation1, Ref[Roll], Ref[Pitch], Ref[Yaw])
        ReturnValue_14: Rotator = MakeRotator(0, 0, Yaw)
        ReturnValue_15: Transform = MakeTransform(Location, ReturnValue_14, Vector(1, 1, 1))
        
        ReturnValue_16: Ptr[Actor] = Default__GameplayStatics.BeginDeferredActorSpawnFromClass(self, ReturnValue1_1, 2, None, Ref[ReturnValue_15])
        
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
        ReturnValue2 = self.GetInstigatorCharacter()
        
        OutLocation1 = None
        OutRotation1 = None
        ReturnValue2.GetActorEyesViewPoint(Ref[OutLocation1], Ref[OutRotation1])
        
        Roll = None
        Pitch = None
        Yaw = None
        BreakRotator(OutRotation1, Ref[Roll], Ref[Pitch], Ref[Yaw])
        ReturnValue_14 = MakeRotator(0, 0, Yaw)
        ReturnValue_15 = MakeTransform(Location, ReturnValue_14, Vector(1, 1, 1))
        
        ReturnValue_17: Ptr[Actor] = Default__GameplayStatics.FinishSpawningActor(ReturnValue_16, Ref[ReturnValue_15])
        self.SetupActor(ReturnValue_17)
        goto('L524')
    
