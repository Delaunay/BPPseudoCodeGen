
from codegen.ue4_stub import *

from Script.Engine import SetScalarParameterValue
from Script.AkAudio import PostAkEvent
from Script.Engine import Texture2D
from Script.Engine import Delay
from Script.Engine import SetVisibility
from Script.Engine import K2_SetTimerDelegate
from Script.FactoryGame import FGCharacterPlayer
from Script.Engine import Controller
from Script.FactoryGame import CreateAndAddNewRepresentationNoActor
from Script.Engine import EqualEqual_ByteByte
from Script.Engine import SetObjectPropertyByName
from Script.Engine import Pawn
from Script.AkAudio import PostAkEventAtLocation
from Script.Engine import SpawnEmitterAtLocation
from Game.FactoryGame.Equipment.ResourceScanner.BP_ResourceScanner import ExecuteUbergraph_BP_ResourceScanner.K2Node_Event_clusters
from Script.Engine import VSize
from Script.Engine import GetInstigator
from Script.FactoryGame import GetInstigatorCharacter
from Script.FactoryGame import IsEquipped
from Game.FactoryGame.Equipment.BuildGun.Animation.BuildgunScan_01_Montage import BuildgunScan_01_Montage
from Script.Engine import LatentActionInfo
from Game.FactoryGame.Equipment.BuildGun.Animation.BuildgunScan_03_Montage import BuildgunScan_03_Montage
from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import GetAnimInstance
from Script.FactoryGame import Get
from Script.Engine import ETimelineDirection
from Script.Engine import PlayerController
from Script.Engine import Default__KismetArrayLibrary
from Script.FactoryGame import Default__FGResourceDescriptor
from Script.Engine import GetController
from Script.FactoryGame import FGResourceScanner
from Script.Engine import TimerHandle
from Game.FactoryGame.PostProcess.PostProcessParameters import PostProcessParameters
from Script.Engine import IsValid
from Script.FactoryGame import Default__FGActorRepresentationManager
from Game.FactoryGame.Equipment.ResourceScanner.UI.Widget_ResourceScanner import Widget_ResourceScanner
from Script.Engine import PlayFromStart
from Script.UMG import Default__WidgetBlueprintLibrary
from Script.FactoryGame import GetMesh1P
from Game.FactoryGame.Character.Player.Animation.FirstPerson.BuildgunScan_02_Montage import BuildgunScan_02_Montage
from Game.FactoryGame.Character.Player.Animation.FirstPerson.BuildgunScan_01_Montage import BuildgunScan_01_Montage
from Script.Engine import Default__GameplayStatics
from Script.UMG import IsVisible
from Script.FactoryGame import ToggleBuildGun
from Script.Engine import BooleanOR
from Script.Engine import Default__KismetMaterialLibrary
from Game.FactoryGame.Character.Player.Animation.FirstPerson.BuildgunScan_03_Montage import BuildgunScan_03_Montage
from Script.Engine import Subtract_VectorVector
from Script.CoreUObject import Vector
from Game.FactoryGame.Character.Player.Char_Player import Char_Player
from Script.FactoryGame import GetBuildGun
from Script.FactoryGame import FGActorRepresentationManager
from Script.Engine import Montage_Play
from Script.AkAudio import Default__AkGameplayStatics
from Game.FactoryGame.Equipment.ResourceScanner.Audio.Play_EQ_Resource_Ping_Hit import Play_EQ_Resource_Ping_Hit
from Game.FactoryGame.Interface.UI.HUDHelpers.BPHUDHelpers import Default__BPHUDHelpers
from Game.FactoryGame.VFX.Misc.Ping.P_HitPing_01 import P_HitPing_01
from Script.Engine import ParticleSystemComponent
from Script.FactoryGame import GetCompasTexture
from Script.Engine import K2_GetActorLocation
from Script.Engine import Actor
from Game.FactoryGame.Equipment.BuildGun.BP_BuildGun import BP_BuildGun
from Script.UMG import Create
from Script.FactoryGame import FGBuildGun
from Game.FactoryGame.Equipment.ResourceScanner.Audio.Play_EQ_Resource_Ping_Fire import Play_EQ_Resource_Ping_Fire
from Game.FactoryGame.Equipment.BuildGun.Animation.BuildgunScan_02_Montage import BuildgunScan_02_Montage
from Script.Engine import GetOwner
from Script.FactoryGame import FGAnimPlayer
from Script.Engine import AnimInstance
from Script.AkAudio import AkComponent
from Game.FactoryGame.Equipment.ResourceScanner.BP_ResourceScanner import ExecuteUbergraph_BP_ResourceScanner
from Script.Engine import SkeletalMeshComponent
from Script.CoreUObject import LinearColor

class BP_ResourceScanner(FGResourceScanner):
    Timeline_0_NewTrack_0_8D03DE94407B43FDF4CBEDAE711F64BC: float
    Timeline_0__Direction_8D03DE94407B43FDF4CBEDAE711F64BC: uint8
    scannerWidget: Ptr[Widget_ResourceScanner]
    mScannerTravelSpeed: float = 10000
    mFakeLoopIndex: int32
    mAcumulatedDelay: float
    mDelayAfterSound: float = 0.8999999761581421
    OnClustersFound: FMulticastScriptDelegate
    mActorRepresentationManager: Ptr[FGActorRepresentationManager]
    mNrOfClosestClustersToMark = 3
    mHoldDownDurationForUI = 0.25
    mDistBetweenNodesInCluster = 15000
    mAttachmentClass = NewObject[Attach_ResourceScanner]()
    mEquipmentSlot = EEquipmentSlot::ES_ARMS
    mAttachSocket = buildgun_Socket
    mArmAnimation = EArmEquipment::AE_ResourceScanner
    PrimaryActorTick = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=False, bTickEvenWhenPaused=False)
    bOnlyRelevantToOwner = True
    bNetUseOwnerRelevancy = True
    bReplicates = True
    RemoteRole = 1
    
    def IsScannerWheelVisible(self):
        ReturnValue: bool = self.scannerWidget.IsVisible()
        IsVisible = ReturnValue
    

    def Timeline_0__FinishedFunc(self):
        self.ExecuteUbergraph_BP_ResourceScanner(5492)
    

    def Timeline_0__UpdateFunc(self):
        self.ExecuteUbergraph_BP_ResourceScanner(5427)
    

    def ShowResourceDescriptorSelectUI(self):
        self.ExecuteUbergraph_BP_ResourceScanner(2879)
    

    def CloseResourceDescriptorSelectUI(self):
        self.ExecuteUbergraph_BP_ResourceScanner(2874)
    

    def PlayClusterEffects(self):
        ExecuteUbergraph_BP_ResourceScanner.K2Node_Event_clusters = clusters #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_ResourceScanner(2884)
    

    def Event Play Pulse Effect(self):
        self.ExecuteUbergraph_BP_ResourceScanner(5382)
    

    def CustomEvent_0(self):
        self.ExecuteUbergraph_BP_ResourceScanner(5422)
    

    def ExecuteUbergraph_BP_ResourceScanner(self):
        goto(ComputedJump("EntryPoint"))
        ReturnValue3: Ptr[Pawn] = self.GetInstigator()
        ReturnValue: Vector = ReturnValue3.K2_GetActorLocation()
        
        clusters = None
        Item = None
        Item = clusters[self.mFakeLoopIndex]
        ReturnValue_0: Vector = Subtract_VectorVector(ReturnValue, Item.MidPoint)
        ReturnValue_1: float = VSize(ReturnValue_0)
        ReturnValue_2: float = ReturnValue_1 / self.mScannerTravelSpeed
        ReturnValue_3: float = ReturnValue_2 - self.mAcumulatedDelay
        ReturnValue_4: float = ReturnValue_3 + self.mAcumulatedDelay
        self.mAcumulatedDelay = ReturnValue_4
        
        clusters = None
        Item = None
        Item = clusters[self.mFakeLoopIndex]
        ReturnValue_5: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEventAtLocation(self, Play_EQ_Resource_Ping_Hit, Item.MidPoint, Rotator::FromPitchYawRoll(0, 0, 0))
        
        clusters = None
        Item = None
        Item = clusters[self.mFakeLoopIndex]
        ReturnValue_6: Ptr[Texture2D] = Default__FGResourceDescriptor.GetCompasTexture(Item.ResourceDescriptor)
        ReturnValue_7: bool = self.mActorRepresentationManager.CreateAndAddNewRepresentationNoActor(Item.MidPoint, ReturnValue_6, LinearColor(R = 1, G = 1, B = 1, A = 1), 25, True, True, 7, True)
        Variable: int32 = 0
        Variable_0: int32 = 0
        
        clusters[self.mFakeLoopIndex].Nodes = None
        # Label 821
        ReturnValue1: int32 = len(clusters[self.mFakeLoopIndex].Nodes)
        ReturnValue1_0: bool = Variable <= ReturnValue1
        if not ReturnValue1_0:
            goto('L1202')
        Variable_0 = Variable
        ExecutionFlow.Push("L1799")
        
        clusters[self.mFakeLoopIndex].Nodes = None
        Item1 = None
        Item1 = clusters[self.mFakeLoopIndex].Nodes[Variable_0]
        ReturnValue1_1: Vector = Item1.K2_GetActorLocation()
        ReturnValue_8: Ptr[ParticleSystemComponent] = Default__GameplayStatics.SpawnEmitterAtLocation(self, P_HitPing_01, ReturnValue1_1, Rotator::FromPitchYawRoll(0, 0, 0), Vector(1, 1, 1), True, 0)
        goto(ExecutionFlow.Pop())
        # Label 1202
        ReturnValue_9: int32 = self.mFakeLoopIndex + 1
        Variable_1: int32 = ReturnValue_9
        self.mFakeLoopIndex = Variable_1
        
        clusters = None
        # Label 1298
        ReturnValue_10: int32 = len(clusters)
        ReturnValue_11: bool = self.mFakeLoopIndex <= ReturnValue_10
        if not ReturnValue_11:
           goto(ExecutionFlow.Pop())
        ReturnValue3 = self.GetInstigator()
        ReturnValue = ReturnValue3.K2_GetActorLocation()
        
        clusters = None
        Item = None
        Item = clusters[self.mFakeLoopIndex]
        ReturnValue_0 = Subtract_VectorVector(ReturnValue, Item.MidPoint)
        ReturnValue_1 = VSize(ReturnValue_0)
        ReturnValue_2 = ReturnValue_1 / self.mScannerTravelSpeed
        ReturnValue_3 = ReturnValue_2 - self.mAcumulatedDelay
        Default__KismetSystemLibrary.Delay(self, ReturnValue_3, LatentActionInfo(Linkage = 15, UUID = 1524315453, ExecutionFunction = "ExecuteUbergraph_BP_ResourceScanner", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        # Label 1799
        ReturnValue1_2: int32 = Variable + 1
        Variable = ReturnValue1_2
        goto('L821')
        self.mFakeLoopIndex = 0
        self.Event Play Pulse Effect()
        self.mAcumulatedDelay = 0
        goto('L1298')
        # Label 1938
        ReturnValue_12: Ptr[Pawn] = self.GetInstigator()
        ReturnValue_13: Ptr[Controller] = ReturnValue_12.GetController()
        Controller: Ptr[PlayerController] = Cast[PlayerController](ReturnValue_13)
        bSuccess: bool = Controller
        if not bSuccess:
           goto(ExecutionFlow.Pop())
        ReturnValue_14: Ptr[Widget_ResourceScanner] = Default__WidgetBlueprintLibrary.Create(self, Widget_ResourceScanner, Controller)
        Default__KismetSystemLibrary.SetObjectPropertyByName(ReturnValue_14, "mResourceScanner", self)
        self.scannerWidget = ReturnValue_14
        ReturnValue4: Ptr[FGCharacterPlayer] = self.GetInstigatorCharacter()
        ReturnValue1_3: Ptr[FGBuildGun] = ReturnValue4.GetBuildGun()
        ReturnValue_15: bool = ReturnValue1_3.IsEquipped()
        if not ReturnValue_15:
            goto('L2380')
        ReturnValue5: Ptr[FGCharacterPlayer] = self.GetInstigatorCharacter()
        ReturnValue5.ToggleBuildGun()
        # Label 2380
        ReturnValue2: Ptr[Pawn] = self.GetInstigator()
        ReturnValue2_0: Ptr[Controller] = ReturnValue2.GetController()
        Default__BPHUDHelpers.PushStackWidget(ReturnValue2_0, self.scannerWidget, self)
        ReturnValue2 = self.GetInstigator()
        ReturnValue2_0 = ReturnValue2.GetController()
        ReturnValue2_0.SetIgnoreLookInput(True)
        goto(ExecutionFlow.Pop())
        # Label 2597
        ReturnValue_16: bool = Default__KismetSystemLibrary.IsValid(self.scannerWidget)
        if not ReturnValue_16:
           goto(ExecutionFlow.Pop())
        ReturnValue1_4: Ptr[Pawn] = self.GetInstigator()
        ReturnValue1_5: Ptr[Controller] = ReturnValue1_4.GetController()
        Default__BPHUDHelpers.PopStackWidget(ReturnValue1_5, self.scannerWidget, self)
        ReturnValue1_4 = self.GetInstigator()
        ReturnValue1_5 = ReturnValue1_4.GetController()
        ReturnValue1_5.ResetIgnoreLookInput()
        goto(ExecutionFlow.Pop())
        goto('L2597')
        goto('L1938')
        ReturnValue6: Ptr[FGCharacterPlayer] = self.GetInstigatorCharacter()
        ReturnValue3_0: Ptr[SkeletalMeshComponent] = ReturnValue6.GetMesh1P()
        ReturnValue6_0: Ptr[AnimInstance] = ReturnValue3_0.GetAnimInstance()
        ReturnValue1_6: bool = Default__KismetSystemLibrary.IsValid(ReturnValue6_0)
        if not ReturnValue1_6:
           goto(ExecutionFlow.Pop())
        self.BuildGun.SetVisibility(True, False)
        ReturnValue2_1: Ptr[FGCharacterPlayer] = self.GetInstigatorCharacter()
        ReturnValue1_7: Ptr[SkeletalMeshComponent] = ReturnValue2_1.GetMesh1P()
        ReturnValue4_0: Ptr[AnimInstance] = ReturnValue1_7.GetAnimInstance()
        Player: Ptr[FGAnimPlayer] = Cast[FGAnimPlayer](ReturnValue4_0)
        bSuccess3: bool = Player
        if not bSuccess3:
           goto(ExecutionFlow.Pop())
        ExecutionFlow.Push("L4216")
        ReturnValue1_8: bool = EqualEqual_ByteByte(Player.mArmSlotType, 0)
        ReturnValue2_2: bool = EqualEqual_ByteByte(Player.mArmSlotType, 1)
        ReturnValue3_1: bool = EqualEqual_ByteByte(Player.mArmSlotType, 4)
        ReturnValue_17: bool = BooleanOR(ReturnValue1_8, ReturnValue2_2)
        ReturnValue1_9: bool = BooleanOR(ReturnValue_17, ReturnValue3_1)
        if not ReturnValue1_9:
            goto('L3636')
        ExecutionFlow.Push("L4556")
        ReturnValue_18: Ptr[AnimInstance] = self.BuildGun.GetAnimInstance()
        ReturnValue_19: float = ReturnValue_18.Montage_Play(BuildgunScan_01_Montage, 1, 0, 0, True)
        goto(ExecutionFlow.Pop())
        # Label 3636
        ReturnValue_20: bool = EqualEqual_ByteByte(Player.mArmSlotType, 3)
        if not ReturnValue_20:
            goto('L3919')
        self.BuildGun.SetVisibility(False, False)
        ExecutionFlow.Push("L4733")
        ReturnValue3_2: Ptr[FGCharacterPlayer] = self.GetInstigatorCharacter()
        ReturnValue2_3: Ptr[SkeletalMeshComponent] = ReturnValue3_2.GetMesh1P()
        ReturnValue5_0: Ptr[AnimInstance] = ReturnValue2_3.GetAnimInstance()
        ReturnValue5_1: float = ReturnValue5_0.Montage_Play(BuildgunScan_03_Montage, 1, 0, 0, True)
        goto(ExecutionFlow.Pop())
        # Label 3919
        ExecutionFlow.Push("L4101")
        ReturnValue3_2 = self.GetInstigatorCharacter()
        ReturnValue2_3 = ReturnValue3_2.GetMesh1P()
        ReturnValue5_0 = ReturnValue2_3.GetAnimInstance()
        ReturnValue4_1: float = ReturnValue5_0.Montage_Play(BuildgunScan_02_Montage, 1, 0, 0, True)
        goto(ExecutionFlow.Pop())
        # Label 4101
        ReturnValue1_10: Ptr[AnimInstance] = self.BuildGun.GetAnimInstance()
        ReturnValue1_11: float = ReturnValue1_10.Montage_Play(BuildgunScan_02_Montage, 1, 0, 0, True)
        goto(ExecutionFlow.Pop())
        # Label 4216
        OutputDelegate.BindUFunction(self, CustomEvent_0)
        ReturnValue_21: TimerHandle = Default__KismetSystemLibrary.K2_SetTimerDelegate(OutputDelegate, 1.899999976158142, False)
        self.OnClustersFound.ProcessMulticastDelegate(Ref[clusters])
        ReturnValue_22: Ptr[FGActorRepresentationManager] = Default__FGActorRepresentationManager.Get(self)
        self.mActorRepresentationManager = ReturnValue_22
        ReturnValue4_2: Ptr[Pawn] = self.GetInstigator()
        ReturnValue_23: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_EQ_Resource_Ping_Fire, ReturnValue4_2, True)
        Default__KismetSystemLibrary.Delay(self, self.mDelayAfterSound, LatentActionInfo(Linkage = 1873, UUID = 1798278144, ExecutionFunction = "ExecuteUbergraph_BP_ResourceScanner", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        # Label 4556
        ReturnValue1_12: Ptr[FGCharacterPlayer] = self.GetInstigatorCharacter()
        ReturnValue_24: Ptr[SkeletalMeshComponent] = ReturnValue1_12.GetMesh1P()
        ReturnValue2_4: Ptr[AnimInstance] = ReturnValue_24.GetAnimInstance()
        ReturnValue2_5: float = ReturnValue2_4.Montage_Play(BuildgunScan_01_Montage, 1, 0, 0, True)
        goto(ExecutionFlow.Pop())
        # Label 4733
        ReturnValue_25: Ptr[FGCharacterPlayer] = self.GetInstigatorCharacter()
        ReturnValue_26: Ptr[FGBuildGun] = ReturnValue_25.GetBuildGun()
        Gun: Ptr[BP_BuildGun] = Cast[BP_BuildGun](ReturnValue_26)
        bSuccess2: bool = Gun
        ReturnValue3_3: Ptr[AnimInstance] = Gun.BuildGun_Skl_01.GetAnimInstance()
        ReturnValue3_4: float = ReturnValue3_3.Montage_Play(BuildgunScan_03_Montage, 1, 0, 0, True)
        goto(ExecutionFlow.Pop())
        # Label 4997
        ReturnValue_27: Ptr[Actor] = self.GetOwner()
        Player_0: Ptr[Char_Player] = Cast[Char_Player](ReturnValue_27)
        bSuccess1: bool = Player_0
        if not bSuccess1:
           goto(ExecutionFlow.Pop())
        Player_0.PPSpawnScanner.Activate(False)
        Player_0.PPSpawnScanner.BlendWeight = 1
        self.Timeline_0.PlayFromStart()
        goto(ExecutionFlow.Pop())
        # Label 5251
        Player_0.PPSpawnScanner.BlendWeight = 0
        goto(ExecutionFlow.Pop())
        # Label 5319
        Player_0.PPSpawnScanner.Deactivate()
        goto('L5251')
        goto('L4997')
        # Label 5387
        self.BuildGun.SetVisibility(False, False)
        goto(ExecutionFlow.Pop())
        goto('L5387')
        Default__KismetMaterialLibrary.SetScalarParameterValue(self, PostProcessParameters, "ScanTime", self.Timeline_0_NewTrack_0_8D03DE94407B43FDF4CBEDAE711F64BC)
        goto(ExecutionFlow.Pop())
        goto('L5319')
    

    def OnClustersFound__DelegateSignature(self, ClustersFound: Ref[List[NodeClusterData]]):
        pass
    
