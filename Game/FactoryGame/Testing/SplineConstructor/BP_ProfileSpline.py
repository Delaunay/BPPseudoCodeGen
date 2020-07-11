
from codegen.ue4_stub import *

from Script.Engine import FinishSpawningActor
from Game.FactoryGame.Testing.SplineConstructor.BP_ProfileSpline import ExecuteUbergraph_BP_ProfileSpline
from Script.Engine import Delay
from Script.Engine import SetVisibility
from Script.FactoryGame import FGPlayerController
from Script.Engine import K2_SetTimerDelegate
from Script.Engine import SceneComponent
from Script.Engine import GetComponentByClass
from Script.Engine import Pawn
from Script.Engine import GetTransformAtSplinePoint
from Script.Engine import BreakTransform
from Script.Engine import Not_PreBool
from Script.Engine import LatentActionInfo
from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import PlayerController
from Script.Engine import Default__KismetArrayLibrary
from Script.Engine import K2_GetPawn
from Script.Engine import PrimitiveComponent
from Script.Engine import Len
from Script.Engine import TimerHandle
from Script.Engine import K2_SetActorLocation
from Script.Engine import IsValid
from Script.Engine import GetCommandLine
from Script.Engine import GreaterEqual_FloatFloat
from Script.Engine import BeginDeferredActorSpawnFromClass
from Script.Engine import K2_GetRootComponent
from Script.Engine import GetPlayerController
from Script.Engine import CharacterMovementComponent
from Script.Engine import Default__GameplayStatics
from Game.FactoryGame.Testing.SplineConstructor.BP_ProfileSpline import ExecuteUbergraph_BP_ProfileSpline.K2Node_Event_DeltaSeconds
from Script.Engine import Concat_StrStr
from Script.Engine import CameraActor
from Script.Engine import Default__KismetStringLibrary
from Script.Engine import ExecuteConsoleCommand
from Script.Engine import K2_AttachToActor
from Script.Engine import FindSubstring
from Script.Engine import Actor
from Game.FactoryGame.Testing.SplineConstructor.BP_ProfileSplineAbstract import BP_ProfileSplineAbstract
from Script.Engine import K2_SetWorldTransform
from Script.Engine import QuitGame
from Script.Engine import K2_ClearAndInvalidateTimerHandle
from Script.Engine import GetCharacterArrayFromString
from Script.FactoryGame import IsRespawning
from Script.Engine import GetComponentsByClass
from Script.CoreUObject import Transform
from Script.Engine import GetTransformAtTime

class BP_ProfileSpline(BP_ProfileSplineAbstract):
    bInitialized: bool
    FindControllerTimer: TimerHandle
    FGCharacter: Ptr[FGPlayerController]
    FinalizeSpawningPlayer: TimerHandle
    CameraActor: Ptr[CameraActor]
    CurrenTime: float
    IsFactory: bool
    PrimaryActorTick = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=True, bTickEvenWhenPaused=False)
    
    def GetConsoleVariableByName(self, VariableName: FString):
        ExecutionFlow.Push("L912")
        ReturnValue: FString = Default__KismetSystemLibrary.GetCommandLine()
        OutString = ""
        ReturnValue_0: int32 = Default__KismetStringLibrary.Len(VariableName)
        ReturnValue_1: int32 = Default__KismetStringLibrary.FindSubstring(ReturnValue, VariableName, False, False, -1)
        ReturnValue_2: int32 = ReturnValue_1 + ReturnValue_0
        Variable: int32 = ReturnValue_2
        # Label 282
        ReturnValue_0 = Default__KismetStringLibrary.Len(VariableName)
        ReturnValue_1 = Default__KismetStringLibrary.FindSubstring(ReturnValue, VariableName, False, False, -1)
        ReturnValue_2 = ReturnValue_1 + ReturnValue_0
        ReturnValue1: int32 = Default__KismetStringLibrary.FindSubstring(ReturnValue, " ", False, False, ReturnValue_2)
        ReturnValue_3: bool = Variable <= ReturnValue1
        if not ReturnValue_3:
            goto('L806')
        ExecutionFlow.Push("L838")
        ReturnValue_4: List[FString] = Default__KismetStringLibrary.GetCharacterArrayFromString(ReturnValue)
        
        Item = None
        Item = ReturnValue_4[Variable]
        ReturnValue_5: FString = Default__KismetStringLibrary.Concat_StrStr(OutString, Item)
        OutString = ReturnValue_5
        goto(ExecutionFlow.Pop())
        # Label 806
        VariableInput = OutString
        # End
        # Label 838
        ReturnValue1_0: int32 = Variable + 1
        Variable = ReturnValue1_0
        goto('L282')
    

    def CheckDoneRespawning(self):
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(self.FGCharacter)
        if not ReturnValue:
            goto('L155')
        ReturnValue_0: bool = self.FGCharacter.IsRespawning()
        ReturnValue_1: bool = Not_PreBool(ReturnValue_0)
        bDoneSpawning = ReturnValue_1
    

    def GetPlayerController(self):
        ReturnValue: Ptr[PlayerController] = Default__GameplayStatics.GetPlayerController(self, 0)
        ReturnValue_0: bool = Default__KismetSystemLibrary.IsValid(ReturnValue)
        bIsValid = ReturnValue_0
        PlayerController = ReturnValue
    

    def StartProfile(self):
        self.ExecuteUbergraph_BP_ProfileSpline(3764)
    

    def ReceiveTick(self):
        ExecuteUbergraph_BP_ProfileSpline.K2Node_Event_DeltaSeconds = DeltaSeconds #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_ProfileSpline(3083)
    

    def FetchPlayerPawn(self):
        self.ExecuteUbergraph_BP_ProfileSpline(2227)
    

    def EnsurePlayerDoneSpawning(self):
        self.ExecuteUbergraph_BP_ProfileSpline(547)
    

    def DebugStart(self):
        self.ExecuteUbergraph_BP_ProfileSpline(3769)
    

    def ExecuteUbergraph_BP_ProfileSpline(self):
        goto(ComputedJump("EntryPoint"))
        ReturnValue1: Ptr[PlayerController] = Default__GameplayStatics.GetPlayerController(self, 0)
        ReturnValue1.SetViewTargetWithBlend(self.CameraActor, 0, 0, 0, False)
        Default__KismetSystemLibrary.Delay(self, 60, LatentActionInfo(Linkage = 198, UUID = 461137502, ExecutionFunction = "ExecuteUbergraph_BP_ProfileSpline", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        ExecutionFlow.Push("L419")
        ExecutionFlow.Push("L314")
        ReturnValue3: Ptr[PlayerController] = Default__GameplayStatics.GetPlayerController(self, 0)
        Default__KismetSystemLibrary.ExecuteConsoleCommand(self, "StartFPSChart", ReturnValue3)
        goto(ExecutionFlow.Pop())
        # Label 314
        ReturnValue3 = Default__GameplayStatics.GetPlayerController(self, 0)
        Default__KismetSystemLibrary.ExecuteConsoleCommand(self, "StartCollect", ReturnValue3)
        goto(ExecutionFlow.Pop())
        # Label 419
        self.bInitialized = True
        goto(ExecutionFlow.Pop())
        # Label 431
        OutputDelegate.BindUFunction(self, EnsurePlayerDoneSpawning)
        ReturnValue: TimerHandle = Default__KismetSystemLibrary.K2_SetTimerDelegate(OutputDelegate, 0.5, True)
        self.FinalizeSpawningPlayer = ReturnValue
        goto(ExecutionFlow.Pop())
        
        bDoneSpawning = None
        self.CheckDoneRespawning(Ref[bDoneSpawning])
        
        Default__KismetSystemLibrary.K2_ClearAndInvalidateTimerHandle(self, Ref[self.FinalizeSpawningPlayer])
        if not bDoneSpawning:
           goto(ExecutionFlow.Pop())
        ReturnValue_0: Transform = self.Spline.GetTransformAtSplinePoint(0, 0, False)
        
        ReturnValue_1: Ptr[Actor] = Default__GameplayStatics.BeginDeferredActorSpawnFromClass(self, CameraActor, 0, self, Ref[ReturnValue_0])
        ReturnValue_0 = self.Spline.GetTransformAtSplinePoint(0, 0, False)
        
        ReturnValue_2: Ptr[CameraActor] = Default__GameplayStatics.FinishSpawningActor(ReturnValue_1, Ref[ReturnValue_0])
        self.CameraActor = ReturnValue_2
        self.FGCharacter.K2_AttachToActor(self, "None", 0, 0, 0, True)
        self.CameraActor.K2_AttachToActor(self, "None", 0, 0, 0, True)
        Default__KismetSystemLibrary.Delay(self, 2, LatentActionInfo(Linkage = 15, UUID = 1248513990, ExecutionFunction = "ExecuteUbergraph_BP_ProfileSpline", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        # Label 1064
        ReturnValue_3: Ptr[PlayerController] = Default__GameplayStatics.GetPlayerController(self, 0)
        Default__KismetSystemLibrary.ExecuteConsoleCommand(self, "t.StorageWithNoOutputSinksResources 1", ReturnValue_3)
        Variable: int32 = 0
        Variable_0: int32 = 0
        # Label 1239
        ReturnValue1_0: Ptr[Pawn] = self.FGCharacter.K2_GetPawn()
        ReturnValue_4: List[Ptr[PrimitiveComponent]] = ReturnValue1_0.GetComponentsByClass(PrimitiveComponent)
        
        ReturnValue_5: int32 = len(ReturnValue_4)
        ReturnValue_6: bool = Variable <= ReturnValue_5
        if not ReturnValue_6:
            goto('L1752')
        Variable_0 = Variable
        ExecutionFlow.Push("L1678")
        ReturnValue1_0 = self.FGCharacter.K2_GetPawn()
        ReturnValue_4 = ReturnValue1_0.GetComponentsByClass(PrimitiveComponent)
        
        Item = None
        Item = ReturnValue_4[Variable_0]
        Item.SetVisibility(False, False)
        goto(ExecutionFlow.Pop())
        # Label 1678
        ReturnValue_7: int32 = Variable + 1
        Variable = ReturnValue_7
        goto('L1239')
        # Label 1752
        ReturnValue_8: Ptr[CharacterMovementComponent] = self.FGCharacter.GetComponentByClass(CharacterMovementComponent)
        ReturnValue_9: bool = Default__KismetSystemLibrary.IsValid(ReturnValue_8)
        if not ReturnValue_9:
            goto('L431')
        ReturnValue_8 = self.FGCharacter.GetComponentByClass(CharacterMovementComponent)
        ReturnValue_8.SetMovementMode(5, 0)
        goto('L431')
        # Label 1964
        OutputDelegate1.BindUFunction(self, FetchPlayerPawn)
        ReturnValue1_1: TimerHandle = Default__KismetSystemLibrary.K2_SetTimerDelegate(OutputDelegate1, 0.5, True)
        self.FindControllerTimer = ReturnValue1_1
        goto(ExecutionFlow.Pop())
        # Label 2080
        ReturnValue_3 = Default__GameplayStatics.GetPlayerController(self, 0)
        Default__KismetSystemLibrary.ExecuteConsoleCommand(self, "God", ReturnValue_3)
        goto('L1064')
        
        # Label 2180
        Default__KismetSystemLibrary.K2_ClearAndInvalidateTimerHandle(self, Ref[self.FindControllerTimer])
        goto('L2080')
        
        bIsvalid = None
        PlayerController = None
        self.GetPlayerController(Ref[bIsvalid], Ref[PlayerController])
        if not bIsvalid:
           goto(ExecutionFlow.Pop())
        Controller: Ptr[FGPlayerController] = Cast[FGPlayerController](PlayerController)
        bSuccess: bool = Controller
        if not bSuccess:
           goto(ExecutionFlow.Pop())
        self.FGCharacter = Controller
        goto('L2180')
        # Label 2368
        ReturnValue2: Ptr[PlayerController] = Default__GameplayStatics.GetPlayerController(self, 0)
        ReturnValue2.SetViewTargetWithBlend(self.CameraActor, 0, 0, 0, False)
        if not self.IsFactory:
           goto(ExecutionFlow.Pop())
        ReturnValue_10: float = self.Duration * 60
        ReturnValue_11: Ptr[Pawn] = self.FGCharacter.K2_GetPawn()
        ReturnValue_12: float = self.CurrenTime / ReturnValue_10
        ReturnValue_13: Transform = self.Spline.GetTransformAtTime(ReturnValue_12, 1, True, False)
        
        Location = None
        Rotation = None
        Scale = None
        BreakTransform(Ref[ReturnValue_13], Ref[Location], Ref[Rotation], Ref[Scale])
        
        SweepHitResult = None
        ReturnValue_14: bool = ReturnValue_11.K2_SetActorLocation(Location, False, True, Ref[SweepHitResult])
        ReturnValue_10 = self.Duration * 60
        ReturnValue_12 = self.CurrenTime / ReturnValue_10
        ReturnValue_13 = self.Spline.GetTransformAtTime(ReturnValue_12, 1, True, False)
        
        Location = None
        Rotation = None
        Scale = None
        BreakTransform(Ref[ReturnValue_13], Ref[Location], Ref[Rotation], Ref[Scale])
        
        SweepHitResult1 = None
        ReturnValue1_2: bool = self.FGCharacter.K2_SetActorLocation(Location, False, True, Ref[SweepHitResult1])
        goto(ExecutionFlow.Pop())
        # Label 3045
        Default__KismetSystemLibrary.QuitGame(self, None, 0, False)
        goto(ExecutionFlow.Pop())
        if not self.bInitialized:
           goto(ExecutionFlow.Pop())
        ReturnValue_15: float = self.CurrenTime + DeltaSeconds
        self.CurrenTime = ReturnValue_15
        ReturnValue_10 = self.Duration * 60
        ReturnValue_12 = self.CurrenTime / ReturnValue_10
        ReturnValue_16: bool = GreaterEqual_FloatFloat(ReturnValue_12, 1)
        if not ReturnValue_16:
            goto('L3514')
        ReturnValue4: Ptr[PlayerController] = Default__GameplayStatics.GetPlayerController(self, 0)
        Default__KismetSystemLibrary.ExecuteConsoleCommand(self, "StopFPSChart", ReturnValue4)
        ReturnValue4 = Default__GameplayStatics.GetPlayerController(self, 0)
        Default__KismetSystemLibrary.ExecuteConsoleCommand(self, "StopCollect", ReturnValue4)
        goto('L3045')
        # Label 3514
        ReturnValue_17: Ptr[SceneComponent] = self.CameraActor.K2_GetRootComponent()
        ReturnValue_10 = self.Duration * 60
        ReturnValue_12 = self.CurrenTime / ReturnValue_10
        ReturnValue_13 = self.Spline.GetTransformAtTime(ReturnValue_12, 1, True, False)
        
        SweepHitResult = None
        ReturnValue_17.K2_SetWorldTransform(False, False, Ref[ReturnValue_13], Ref[SweepHitResult])
        goto('L2368')
        goto('L1964')
        goto('L1964')
    
