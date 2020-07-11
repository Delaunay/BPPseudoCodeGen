
from codegen.ue4_stub import *

from Game.FactoryGame.Buildable.Factory.LandingPad.Build_LandingPad import ExecuteUbergraph_Build_LandingPad.K2Node_ComponentBoundEvent_OtherBodyIndex1
from Script.Engine import ReceiveDestroyed
from Script.AkAudio import PostAkEvent
from Game.FactoryGame.Buildable.Factory.-Shared.Audio.Traversal_Shared.Stop_B_FactoryTraversal_Jelly_Outside import Stop_B_FactoryTraversal_Jelly_Outside
from Game.FactoryGame.Buildable.Factory.LandingPad.Build_LandingPad import ExecuteUbergraph_Build_LandingPad
from Script.Engine import SetVisibility
from Script.FactoryGame import FGCharacterPlayer
from Game.FactoryGame.Buildable.Factory.LandingPad.Build_LandingPad import ExecuteUbergraph_Build_LandingPad.K2Node_ComponentBoundEvent_OverlappedComponent
from Script.Engine import HasAuthority
from Script.Engine import Default__KismetArrayLibrary
from Game.FactoryGame.Buildable.Factory.-Shared.Audio.Traversal_Shared.Play_B_FactoryTraversal_Jelly_Inside import Play_B_FactoryTraversal_Jelly_Inside
from Script.FactoryGame import FGBuildableFactory
from Script.FactoryGame import GetComponentFlagSoftLanding
from Game.FactoryGame.Buildable.Factory.LandingPad.Build_LandingPad import ExecuteUbergraph_Build_LandingPad.K2Node_ComponentBoundEvent_OtherBodyIndex
from Game.FactoryGame.Buildable.Factory.LandingPad.Build_LandingPad import ExecuteUbergraph_Build_LandingPad.K2Node_ComponentBoundEvent_OtherComp1
from Script.Engine import Array_AddUnique
from Script.CoreUObject import Vector
from Game.FactoryGame.Buildable.Factory.LandingPad.Build_LandingPad import ExecuteUbergraph_Build_LandingPad.K2Node_ComponentBoundEvent_bFromSweep
from Game.FactoryGame.Buildable.Factory.LandingPad.Build_LandingPad import ExecuteUbergraph_Build_LandingPad.K2Node_ComponentBoundEvent_SweepResult
from Game.FactoryGame.Buildable.Factory.-Shared.Audio.Traversal_Shared.Stop_B_FactoryTraversal_Jelly_Inside import Stop_B_FactoryTraversal_Jelly_Inside
from Game.FactoryGame.Buildable.Factory.LandingPad.Build_LandingPad import ExecuteUbergraph_Build_LandingPad.K2Node_Event_newHasPower
from Game.FactoryGame.Buildable.Factory.LandingPad.Build_LandingPad import ExecuteUbergraph_Build_LandingPad.K2Node_ComponentBoundEvent_OverlappedComponent1
from Script.Engine import Array_RemoveItem
from Script.Engine import PawnMovementComponent
from Script.AkAudio import Default__AkGameplayStatics
from Script.FactoryGame import Default__FGBlueprintFunctionLibrary
from Game.FactoryGame.Buildable.Factory.LandingPad.Build_LandingPad import ExecuteUbergraph_Build_LandingPad.K2Node_ComponentBoundEvent_OtherComp
from Game.FactoryGame.Buildable.Factory.LandingPad.Build_LandingPad import ExecuteUbergraph_Build_LandingPad.K2Node_Event_DeltaSeconds
from Game.FactoryGame.Buildable.Factory.-Shared.Audio.Traversal_Shared.Play_B_FactoryTraversal_Jelly_Outside import Play_B_FactoryTraversal_Jelly_Outside
from Game.FactoryGame.Buildable.Factory.LandingPad.Build_LandingPad import ExecuteUbergraph_Build_LandingPad.K2Node_ComponentBoundEvent_OtherActor1
from Script.AkAudio import AkComponent
from Game.FactoryGame.Buildable.Factory.-Shared.Audio.Traversal_Shared.Play_B_FactoryTraversal_Jelly_Inside_ExitBlob import Play_B_FactoryTraversal_Jelly_Inside_ExitBlob
from Game.FactoryGame.Buildable.Factory.LandingPad.Build_LandingPad import ExecuteUbergraph_Build_LandingPad.K2Node_ComponentBoundEvent_OtherActor

class Build_LandingPad(FGBuildableFactory):
    mDampeningFactor: float = 0.824999988079071
    mPlayerList: List[Ptr[FGCharacterPlayer]]
    mPowerConsumption = 5
    mPowerConsumptionExponent = 1.600000023841858
    mPowerInfoClass = NewObject[FGPowerInfoComponent]()
    mMinimumStoppedTime = 0.25
    mNumCyclesForProductivity = 20
    mCurrentPotential = 1
    mPendingPotential = 1
    mMinPotential = 0.009999999776482582
    mMaxPotential = 1
    mMaxPotentialIncreasePerCrystal = 0.5
    mFluidStackSizeDefault = EStackSize::SS_FLUID
    mFluidStackSizeMultiplier = 1
    mAddToSignificanceManager = True
    mSignificanceRange = 18000
    mHologramClass = NewObject[FGFactoryHologram]()
    mDisplayName = NSLOCTEXT("", "40EA941E48CEFB59722E2F81443B383D", "U-Jelly Landing Pad")
    mDescription = NSLOCTEXT("", "C34118414305B8CB72BDE989142D7A90", "Generates a speed dampening jelly.\r\nGuarantees a soft landing.")
    MaxRenderDistance = -1
    mFactoryTickFunction = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=True, bTickEvenWhenPaused=False)
    mPrimaryColor = Namespace(A=1, B=-1, G=-1, R=-1)
    mSecondaryColor = Namespace(A=1, B=-1, G=-1, R=-1)
    mDismantleEffectClassName = Namespace(AssetPathName='/Game/FactoryGame/Buildable/Factory/-Shared/BP_MaterialEffect_Dismantle.BP_MaterialEffect_Dismantle_C', SubPathString='')
    mBuildEffectClassName = Namespace(AssetPathName='/Game/FactoryGame/Buildable/Factory/-Shared/BP_MaterialEffect_Build.BP_MaterialEffect_Build_C', SubPathString='')
    mHighlightParticleClassName = Namespace(AssetPathName='/Game/FactoryGame/Buildable/-Shared/Particle/NewBuildingPing.NewBuildingPing_C', SubPathString='')
    mCameraDistanceSq = 100000000376832
    mBuildingID = -1
    PrimaryActorTick = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=True, bTickEvenWhenPaused=False)
    bReplicates = True
    RemoteRole = 1
    NetCullDistanceSquared = 5624999936
    RootComponent = Namespace(Mobility=0, ObjectClass='/Script/Engine.SceneComponent', ObjectFlags=2883617, ObjectName='RootComponent')
    
    def UpdateAudioState(self):
        ExecutionFlow.Push("L687")
        Variable: int32 = 0
        Variable_0: int32 = 0
        
        # Label 51
        ReturnValue: int32 = len(self.mPlayerList)
        ReturnValue_0: bool = Variable <= ReturnValue
        if not ReturnValue_0:
           goto(ExecutionFlow.Pop())
        Variable_0 = Variable
        ExecutionFlow.Push("L492")
        # Label 190
        ReturnValue_1: bool = self.HasPower()
        
        Item = None
        Item = self.mPlayerList[Variable_0]
        ReturnValue_2: bool = Item.IsLocallyControlled()
        ReturnValue_3: bool = ReturnValue_1 and ReturnValue_2
        if not ReturnValue_3:
            goto('L566')
        
        Item = None
        Item = self.mPlayerList[Variable_0]
        ReturnValue1: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_B_FactoryTraversal_Jelly_Inside, Item, True)
        goto(ExecutionFlow.Pop())
        # Label 492
        ReturnValue_4: int32 = Variable + 1
        Variable = ReturnValue_4
        goto('L51')
        
        Item = None
        # Label 566
        Item = self.mPlayerList[Variable_0]
        ReturnValue_5: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Stop_B_FactoryTraversal_Jelly_Inside, Item, True)
        goto(ExecutionFlow.Pop())
    

    def CanProduce(self):
        ReturnValue = True
    

    def ReceiveTick(self):
        ExecuteUbergraph_Build_LandingPad.K2Node_Event_DeltaSeconds = DeltaSeconds #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Build_LandingPad(899)
    

    def BndEvt__StaticMesh1_K2Node_ComponentBoundEvent_0_ComponentBeginOverlapSignature__DelegateSignature(self, OverlappedComponent: Ptr[PrimitiveComponent], OtherActor: Ptr[Actor], OtherComp: Ptr[PrimitiveComponent], OtherBodyIndex: int32, bFromSweep: bool, SweepResult: Const[Ref[HitResult]]):
        ExecuteUbergraph_Build_LandingPad.K2Node_ComponentBoundEvent_OverlappedComponent1 = OverlappedComponent #  PERSISTENT_FRAME(
        ExecuteUbergraph_Build_LandingPad.K2Node_ComponentBoundEvent_OtherActor1 = OtherActor #  PERSISTENT_FRAME(
        ExecuteUbergraph_Build_LandingPad.K2Node_ComponentBoundEvent_OtherComp1 = OtherComp #  PERSISTENT_FRAME(
        ExecuteUbergraph_Build_LandingPad.K2Node_ComponentBoundEvent_OtherBodyIndex1 = OtherBodyIndex #  PERSISTENT_FRAME(
        ExecuteUbergraph_Build_LandingPad.K2Node_ComponentBoundEvent_bFromSweep = bFromSweep #  PERSISTENT_FRAME(
        ExecuteUbergraph_Build_LandingPad.K2Node_ComponentBoundEvent_SweepResult = SweepResult #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Build_LandingPad(1042)
    

    def BndEvt__StaticMesh1_K2Node_ComponentBoundEvent_1_ComponentEndOverlapSignature__DelegateSignature(self, OverlappedComponent: Ptr[PrimitiveComponent], OtherActor: Ptr[Actor], OtherComp: Ptr[PrimitiveComponent], OtherBodyIndex: int32):
        ExecuteUbergraph_Build_LandingPad.K2Node_ComponentBoundEvent_OverlappedComponent = OverlappedComponent #  PERSISTENT_FRAME(
        ExecuteUbergraph_Build_LandingPad.K2Node_ComponentBoundEvent_OtherActor = OtherActor #  PERSISTENT_FRAME(
        ExecuteUbergraph_Build_LandingPad.K2Node_ComponentBoundEvent_OtherComp = OtherComp #  PERSISTENT_FRAME(
        ExecuteUbergraph_Build_LandingPad.K2Node_ComponentBoundEvent_OtherBodyIndex = OtherBodyIndex #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Build_LandingPad(1200)
    

    def Factory_ReceiveStartProducing(self):
        self.ExecuteUbergraph_Build_LandingPad(1576)
    

    def Factory_ReceiveStopProducing(self):
        self.ExecuteUbergraph_Build_LandingPad(1770)
    

    def OnHasPowerChanged(self):
        ExecuteUbergraph_Build_LandingPad.K2Node_Event_newHasPower = newHasPower #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Build_LandingPad(1960)
    

    def ReceiveDestroyed(self):
        self.ExecuteUbergraph_Build_LandingPad(1975)
    

    def ReceiveBeginPlay(self):
        self.ExecuteUbergraph_Build_LandingPad(2039)
    

    def ExecuteUbergraph_Build_LandingPad(self):
        goto(ComputedJump("EntryPoint"))
        # Label 15
        ReturnValue: bool = self.IsProducing()
        if not ReturnValue:
           goto(ExecutionFlow.Pop())
        ReturnValue1: FName = Default__FGBlueprintFunctionLibrary.GetComponentFlagSoftLanding()
        
        self.FGColoredInstanceMeshProxy.ComponentTags = None
        ReturnValue2: int32 = Default__KismetArrayLibrary.Array_AddUnique(Ref[self.FGColoredInstanceMeshProxy.ComponentTags], Ref[ReturnValue1])
        goto(ExecutionFlow.Pop())
        # Label 190
        ReturnValue_0: bool = self.HasAuthority()
        if not ReturnValue_0:
           goto(ExecutionFlow.Pop())
        
        ReturnValue1_0: int32 = len(self.mPlayerList)
        ReturnValue_1: bool = ReturnValue1_0 > 0
        ReturnValue1_1: bool = self.IsProducing()
        ReturnValue_2: bool = ReturnValue1_1 and ReturnValue_1
        if not ReturnValue_2:
           goto(ExecutionFlow.Pop())
        Variable: int32 = 0
        Variable_0: int32 = 0
        
        # Label 431
        ReturnValue_3: int32 = len(self.mPlayerList)
        ReturnValue_4: bool = Variable <= ReturnValue_3
        if not ReturnValue_4:
           goto(ExecutionFlow.Pop())
        Variable_0 = Variable
        ExecutionFlow.Push("L825")
        
        Item = None
        Item = self.mPlayerList[Variable_0]
        ReturnValue_5: Ptr[PawnMovementComponent] = Item.GetMovementComponent()
        ReturnValue_6: Vector = Item.GetVelocity()
        ReturnValue_7: Vector = ReturnValue_6 * self.mDampeningFactor
        ReturnValue_5.Velocity = ReturnValue_7
        goto(ExecutionFlow.Pop())
        # Label 825
        ReturnValue_8: int32 = Variable + 1
        Variable = ReturnValue_8
        goto('L431')
        ExecutionFlow.Push("L976")
        ExecutionFlow.Push("L190")
        ReturnValue1_1 = self.IsProducing()
        self.EffectMesh.SetVisibility(ReturnValue1_1, False)
        goto(ExecutionFlow.Pop())
        # Label 976
        ReturnValue1_1 = self.IsProducing()
        self.PostProcess.bEnabled = ReturnValue1_1
        goto(ExecutionFlow.Pop())
        Player: Ptr[FGCharacterPlayer] = Cast[FGCharacterPlayer](OtherActor1)
        bSuccess: bool = Player
        if not bSuccess:
           goto(ExecutionFlow.Pop())
        
        ReturnValue_9: int32 = Default__KismetArrayLibrary.Array_AddUnique(Ref[self.mPlayerList], Ref[Player])
        self.UpdateAudioState()
        goto(ExecutionFlow.Pop())
        Player1: Ptr[FGCharacterPlayer] = Cast[FGCharacterPlayer](OtherActor)
        bSuccess1: bool = Player1
        if not bSuccess1:
           goto(ExecutionFlow.Pop())
        
        ReturnValue_10: bool = Default__KismetArrayLibrary.Array_RemoveItem(Ref[self.mPlayerList], Ref[Player1])
        # Label 1335
        ReturnValue1_2: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Stop_B_FactoryTraversal_Jelly_Inside, Player1, True)
        ReturnValue_11: bool = Player1.IsLocallyControlled()
        ReturnValue_12: bool = self.HasPower()
        ReturnValue1_3: bool = ReturnValue_12 and ReturnValue_11
        if not ReturnValue1_3:
           goto(ExecutionFlow.Pop())
        ReturnValue_13: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_B_FactoryTraversal_Jelly_Inside_ExitBlob, Player1, True)
        goto(ExecutionFlow.Pop())
        ReturnValue2_0: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_B_FactoryTraversal_Jelly_Outside, self, True)
        ReturnValue_14: FName = Default__FGBlueprintFunctionLibrary.GetComponentFlagSoftLanding()
        
        self.FGColoredInstanceMeshProxy.ComponentTags = None
        ReturnValue1_4: int32 = Default__KismetArrayLibrary.Array_AddUnique(Ref[self.FGColoredInstanceMeshProxy.ComponentTags], Ref[ReturnValue_14])
        goto(ExecutionFlow.Pop())
        ReturnValue3: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Stop_B_FactoryTraversal_Jelly_Outside, self, True)
        ReturnValue_14 = Default__FGBlueprintFunctionLibrary.GetComponentFlagSoftLanding()
        
        self.FGColoredInstanceMeshProxy.ComponentTags = None
        ReturnValue1_5: bool = Default__KismetArrayLibrary.Array_RemoveItem(Ref[self.FGColoredInstanceMeshProxy.ComponentTags], Ref[ReturnValue_14])
        goto('L1335')
        self.UpdateAudioState()
        goto(ExecutionFlow.Pop())
        self.ReceiveDestroyed()
        ReturnValue4: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Stop_B_FactoryTraversal_Jelly_Inside, self, True)
        goto(ExecutionFlow.Pop())
        goto('L15')
    
