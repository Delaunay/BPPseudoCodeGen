
from codegen.ue4_stub import *

from Game.FactoryGame.Buildable.Factory.JumpPad.Build_JumpPad import ExecuteUbergraph_Build_JumpPad
from Script.AkAudio import PostAkEvent
from Game.FactoryGame.Buildable.Factory.JumpPad.Build_JumpPad import ExecuteUbergraph_Build_JumpPad.K2Node_ComponentBoundEvent_OtherBodyIndex
from Script.Engine import SetVisibility
from Game.FactoryGame.Buildable.Factory.JumpPad.Build_JumpPad import ExecuteUbergraph_Build_JumpPad.K2Node_Event_newHasPower
from Script.CoreUObject import Rotator
from Script.FactoryGame import FGCharacterBase
from Game.FactoryGame.Buildable.Factory.JumpPad.Build_JumpPad import ExecuteUbergraph_Build_JumpPad.K2Node_ComponentBoundEvent_OtherComp
from Script.FactoryGame import FGBuildableFactory
from Script.AkAudio import AkAudioEvent
from Script.Engine import CharacterMovementComponent
from Script.CoreUObject import Vector
from Script.Engine import K2_GetComponentRotation
from Script.Engine import PawnMovementComponent
from Script.AkAudio import Default__AkGameplayStatics
from Game.FactoryGame.Buildable.Factory.JumpPad.Build_JumpPad import ExecuteUbergraph_Build_JumpPad.K2Node_ComponentBoundEvent_SweepResult
from Game.FactoryGame.Buildable.Factory.JumpPad.Build_JumpPad import ExecuteUbergraph_Build_JumpPad.K2Node_ComponentBoundEvent_bFromSweep
from Game.FactoryGame.Buildable.Factory.JumpPad.Build_JumpPad import ExecuteUbergraph_Build_JumpPad.K2Node_ComponentBoundEvent_OverlappedComponent
from Script.Engine import GetUpVector
from Game.FactoryGame.Buildable.Factory.JumpPad.Build_JumpPad import ExecuteUbergraph_Build_JumpPad.K2Node_ComponentBoundEvent_OtherActor
from Script.AkAudio import AkComponent

class Build_JumpPad(FGBuildableFactory):
    JumpForceCharacter: float = 2500
    mAkEvent: Ptr[AkAudioEvent] = Namespace(AssetPath='/Game/FactoryGame/Buildable/Factory/-Shared/Audio/Traversal_Shared/Play_B_FactoryTraversal_Air_Push_01.Play_B_FactoryTraversal_Air_Push_01')
    JumpForcePhysics: float = 200000
    mPowerConsumption = 2
    mPowerConsumptionExponent = 1.600000023841858
    mPowerInfoClass = NewObject[FGPowerInfoComponent]()
    mMinimumProducingTime = 2
    mMinimumStoppedTime = 5
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
    mDisplayName = NSLOCTEXT("", "5C7397674656688A5C530991564A68FA", "Jump Pad")
    mDescription = NSLOCTEXT("", "7D8E78D346E855AF871A3989CEA21750", "Propels you upwards through the air.\r\nMake sure you land softly.")
    MaxRenderDistance = -1
    mFactoryTickFunction = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=True, bTickEvenWhenPaused=False)
    mPrimaryColor = Namespace(A=1, B=-1, G=-1, R=-1)
    mSecondaryColor = Namespace(A=1, B=-1, G=-1, R=-1)
    mDismantleEffectClassName = Namespace(AssetPathName='/Game/FactoryGame/Buildable/Factory/-Shared/BP_MaterialEffect_Dismantle.BP_MaterialEffect_Dismantle_C', SubPathString='')
    mBuildEffectClassName = Namespace(AssetPathName='/Game/FactoryGame/Buildable/Factory/-Shared/BP_MaterialEffect_Build.BP_MaterialEffect_Build_C', SubPathString='')
    mHighlightParticleClassName = Namespace(AssetPathName='/Game/FactoryGame/Buildable/-Shared/Particle/NewBuildingPing.NewBuildingPing_C', SubPathString='')
    mCameraDistanceSq = 100000000376832
    mBuildingID = -1
    PrimaryActorTick = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=False, bTickEvenWhenPaused=False)
    bReplicates = True
    RemoteRole = 1
    NetCullDistanceSquared = 5624999936
    RootComponent = Namespace(Mobility=0, ObjectClass='/Script/Engine.SceneComponent', ObjectFlags=2883617, ObjectName='RootComponent')
    
    def CanProduce(self):
        ReturnValue = True
    

    def BndEvt__Box_K2Node_ComponentBoundEvent_0_ComponentBeginOverlapSignature__DelegateSignature(self, OverlappedComponent: Ptr[PrimitiveComponent], OtherActor: Ptr[Actor], OtherComp: Ptr[PrimitiveComponent], OtherBodyIndex: int32, bFromSweep: bool, SweepResult: Const[Ref[HitResult]]):
        ExecuteUbergraph_Build_JumpPad.K2Node_ComponentBoundEvent_OverlappedComponent = OverlappedComponent #  PERSISTENT_FRAME(
        ExecuteUbergraph_Build_JumpPad.K2Node_ComponentBoundEvent_OtherActor = OtherActor #  PERSISTENT_FRAME(
        ExecuteUbergraph_Build_JumpPad.K2Node_ComponentBoundEvent_OtherComp = OtherComp #  PERSISTENT_FRAME(
        ExecuteUbergraph_Build_JumpPad.K2Node_ComponentBoundEvent_OtherBodyIndex = OtherBodyIndex #  PERSISTENT_FRAME(
        ExecuteUbergraph_Build_JumpPad.K2Node_ComponentBoundEvent_bFromSweep = bFromSweep #  PERSISTENT_FRAME(
        ExecuteUbergraph_Build_JumpPad.K2Node_ComponentBoundEvent_SweepResult = SweepResult #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Build_JumpPad(10)
    

    def OnHasPowerChanged(self):
        ExecuteUbergraph_Build_JumpPad.K2Node_Event_newHasPower = newHasPower #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Build_JumpPad(1061)
    

    def ExecuteUbergraph_Build_JumpPad(self):
        ReturnValue: bool = self.IsProducing()
        if not ReturnValue:
            goto('L1103')
        Base: Ptr[FGCharacterBase] = Cast[FGCharacterBase](OtherActor)
        bSuccess: bool = Base
        if not bSuccess:
            goto('L649')
        ReturnValue_0: Ptr[PawnMovementComponent] = Base.GetMovementComponent()
        Component: Ptr[CharacterMovementComponent] = Cast[CharacterMovementComponent](ReturnValue_0)
        bSuccess1: bool = Component
        if not bSuccess1:
            goto('L1103')
        Component.SetMovementMode(3, 0)
        ReturnValue_0 = Base.GetMovementComponent()
        ReturnValue_1: Rotator = self.Box.K2_GetComponentRotation()
        ReturnValue_2: Vector = GetUpVector(ReturnValue_1)
        ReturnValue1: Vector = ReturnValue_2 * self.JumpForceCharacter
        ReturnValue_0.Velocity = ReturnValue1
        # Label 520
        self.ParticleSystem.SetVisibility(True, False)
        self.ParticleSystem.Activate(False)
        ReturnValue_3: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(self.mAkEvent, self, True)
        # End
        # Label 649
        ReturnValue_4: bool = OtherComp.IsSimulatingPhysics("None")
        if not ReturnValue_4:
            goto('L1103')
        ReturnValue_5: float = OtherComp.GetMass()
        ReturnValue_6: float = ReturnValue_5 * 0.699999988079071
        ReturnValue1_0: float = ReturnValue_6 * self.JumpForceCharacter
        ReturnValue_1 = self.Box.K2_GetComponentRotation()
        ReturnValue_2 = GetUpVector(ReturnValue_1)
        ReturnValue_7: Vector = ReturnValue_2 * ReturnValue1_0
        OtherComp.AddImpulse(ReturnValue_7, "None", False)
        goto('L520')
        self.ParticleSystem.SetVisibility(newHasPower, False)
    
