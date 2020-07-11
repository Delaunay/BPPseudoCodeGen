
from codegen.ue4_stub import *

from Script.Engine import FinishSpawningActor
from Script.Engine import Map_Contains
from Script.Engine import Pawn
from Script.Engine import Conv_IntToFloat
from Script.Engine import Conv_VectorToTransform
from Script.Engine import FTrunc
from Script.Engine import K2_TeleportTo
from Script.Engine import PlayerController
from Script.Engine import Map_Remove
from Script.Engine import Default__KismetArrayLibrary
from Script.Engine import K2_GetPawn
from Script.Engine import Sqrt
from Script.Engine import GreaterEqual_FloatFloat
from Script.Engine import BeginDeferredActorSpawnFromClass
from Game.WeatherOverhaul.RainActor import RainActor
from Script.Engine import Map_Values
from Script.Engine import GetPlayerController
from Script.Engine import Default__GameplayStatics
from Script.CoreUObject import Vector
from Script.Engine import Map_Add
from Game.FactoryGame.Interface.UI.InGame.-Shared.IntVector2d import IntVector2D
from Script.Engine import Actor
from Script.Engine import K2_GetActorLocation
from Script.Engine import Abs
from Game.WeatherOverhaul.RainSpawnerActor import ExecuteUbergraph_RainSpawnerActor.K2Node_Event_DeltaSeconds
from Script.Engine import Default__BlueprintMapLibrary
from Game.WeatherOverhaul.RainSpawnerActor import ExecuteUbergraph_RainSpawnerActor
from Script.CoreUObject import Transform

class RainSpawnerActor(Actor):
    SpawnedComponentMap: Dict[IntVector2D, Actor*]
    PrimaryActorTick = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=True, bTickEvenWhenPaused=False)
    
    def ReceiveTick(self):
        ExecuteUbergraph_RainSpawnerActor.K2Node_Event_DeltaSeconds = DeltaSeconds #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_RainSpawnerActor(6762)
    

    def ExecuteUbergraph_RainSpawnerActor(self):
        goto(ComputedJump("EntryPoint"))
        # Label 15
        ExecutionFlow.Push("L1746")
        ReturnValue: Ptr[PlayerController] = Default__GameplayStatics.GetPlayerController(self, 0)
        
        Values1 = None
        Item1 = None
        Item1 = Values1[Variable]
        ReturnValue_0: Ptr[Pawn] = ReturnValue.K2_GetPawn()
        ReturnValue1: Vector = Item1.K2_GetActorLocation()
        ReturnValue2: Vector = ReturnValue_0.K2_GetActorLocation()
        
        X1 = None
        Y1 = None
        Z1 = None
        X1, Y1, Z1 = BreakVector(ReturnValue1)
        
        X2 = None
        Y2 = None
        Z2 = None
        X2, Y2, Z2 = BreakVector(ReturnValue2)
        ReturnValue_1: float = Y1 / 1000
        ReturnValue1_0: float = Y2 / 1000
        ReturnValue_2: int32 = FTrunc(ReturnValue_1)
        ReturnValue1_1: int32 = FTrunc(ReturnValue1_0)
        ReturnValue2_0: float = X2 / 1000
        ReturnValue3: float = X1 / 1000
        ReturnValue2_1: int32 = FTrunc(ReturnValue2_0)
        ReturnValue3_0: int32 = FTrunc(ReturnValue3)
        IntVector2D.X_2_3FF107F84D30EB52DD50898C7D2CAD67 = ReturnValue2_1
        IntVector2D.Y_4_F18C5B824136D7759146338CAA496F0A = ReturnValue1_1
        IntVector2D1.X_2_3FF107F84D30EB52DD50898C7D2CAD67 = ReturnValue3_0
        IntVector2D1.Y_4_F18C5B824136D7759146338CAA496F0A = ReturnValue_2
        ReturnValue_3: int32 = IntVector2D1.Y_4_F18C5B824136D7759146338CAA496F0A - IntVector2D.Y_4_F18C5B824136D7759146338CAA496F0A
        ReturnValue1_2: int32 = IntVector2D1.X_2_3FF107F84D30EB52DD50898C7D2CAD67 - IntVector2D.X_2_3FF107F84D30EB52DD50898C7D2CAD67
        ReturnValue_4: int32 = ReturnValue_3 * ReturnValue_3
        ReturnValue1_3: int32 = ReturnValue1_2 * ReturnValue1_2
        ReturnValue4: int32 = ReturnValue1_3 + ReturnValue_4
        ReturnValue_5: float = Conv_IntToFloat(ReturnValue4)
        ReturnValue_6: float = Sqrt(ReturnValue_5)
        ReturnValue_7: bool = GreaterEqual_FloatFloat(ReturnValue_6, 6)
        if not ReturnValue_7:
           goto(ExecutionFlow.Pop())
        
        Values1 = None
        Item1 = None
        Item1 = Values1[Variable]
        Item1.K2_DestroyActor()
        
        Values1 = None
        Item1 = None
        Item1 = Values1[Variable]
        ReturnValue1 = Item1.K2_GetActorLocation()
        
        X1 = None
        Y1 = None
        Z1 = None
        X1, Y1, Z1 = BreakVector(ReturnValue1)
        ReturnValue_1 = Y1 / 1000
        ReturnValue_2 = FTrunc(ReturnValue_1)
        ReturnValue3 = X1 / 1000
        ReturnValue3_0 = FTrunc(ReturnValue3)
        IntVector2D1.X_2_3FF107F84D30EB52DD50898C7D2CAD67 = ReturnValue3_0
        IntVector2D1.Y_4_F18C5B824136D7759146338CAA496F0A = ReturnValue_2
        
        IntVector2D1 = None
        ReturnValue_8: bool = Default__BlueprintMapLibrary.Map_Remove(Ref[self.SpawnedComponentMap], Ref[IntVector2D1])
        goto(ExecutionFlow.Pop())
        # Label 1746
        ReturnValue3_1: int32 = Variable1 + 1
        Variable1: int32 = ReturnValue3_1
        
        Values1 = None
        # Label 1815
        ReturnValue1_4: int32 = len(Values1)
        ReturnValue1_5: bool = Variable1 <= ReturnValue1_4
        if not ReturnValue1_5:
            goto('L1958')
        Variable: int32 = Variable1
        goto('L15')
        # Label 1958
        Variable_0: int32 = -5
        # Label 1981
        ReturnValue_9: bool = Variable_0 <= 5
        if not ReturnValue_9:
            goto('L2779')
        ExecutionFlow.Push("L4028")
        Variable1_0: int32 = -5
        # Label 2057
        ReturnValue1_6: bool = Variable1_0 <= 5
        if not ReturnValue1_6:
           goto(ExecutionFlow.Pop())
        ExecutionFlow.Push("L4102")
        ReturnValue = Default__GameplayStatics.GetPlayerController(self, 0)
        ReturnValue_0 = ReturnValue.K2_GetPawn()
        ReturnValue2 = ReturnValue_0.K2_GetActorLocation()
        
        X2 = None
        Y2 = None
        Z2 = None
        X2, Y2, Z2 = BreakVector(ReturnValue2)
        ReturnValue1_0 = Y2 / 1000
        ReturnValue1_1 = FTrunc(ReturnValue1_0)
        ReturnValue2_0 = X2 / 1000
        ReturnValue2_1 = FTrunc(ReturnValue2_0)
        IntVector2D.X_2_3FF107F84D30EB52DD50898C7D2CAD67 = ReturnValue2_1
        IntVector2D.Y_4_F18C5B824136D7759146338CAA496F0A = ReturnValue1_1
        ReturnValue5: int32 = Variable_0 + IntVector2D.Y_4_F18C5B824136D7759146338CAA496F0A
        ReturnValue6: int32 = Variable1_0 + IntVector2D.X_2_3FF107F84D30EB52DD50898C7D2CAD67
        IntVector2D2.X_2_3FF107F84D30EB52DD50898C7D2CAD67 = ReturnValue6
        IntVector2D2.Y_4_F18C5B824136D7759146338CAA496F0A = ReturnValue5
        
        IntVector2D2 = None
        ReturnValue_10: bool = Default__BlueprintMapLibrary.Map_Contains(Ref[self.SpawnedComponentMap], Ref[IntVector2D2])
        if not ReturnValue_10:
            goto('L4176')
        goto(ExecutionFlow.Pop())
        # Label 2779
        Values: List[Ptr[Actor]] = []
        
        Default__BlueprintMapLibrary.Map_Values(Ref[self.SpawnedComponentMap], Ref[Values])
        Variable_1: int32 = 0
        Variable1_1: int32 = 0
        
        # Label 2886
        ReturnValue_11: int32 = len(Values)
        ReturnValue_12: bool = Variable_1 <= ReturnValue_11
        if not ReturnValue_12:
           goto(ExecutionFlow.Pop())
        Variable1_1 = Variable_1
        ExecutionFlow.Push("L3954")
        
        Item = None
        Item = Values[Variable1_1]
        ReturnValue_13: Vector = Item.K2_GetActorLocation()
        
        X = None
        Y = None
        Z = None
        X, Y, Z = BreakVector(ReturnValue_13)
        ReturnValue = Default__GameplayStatics.GetPlayerController(self, 0)
        ReturnValue_0 = ReturnValue.K2_GetPawn()
        ReturnValue3_2: Vector = ReturnValue_0.K2_GetActorLocation()
        
        X3 = None
        Y3 = None
        Z3 = None
        X3, Y3, Z3 = BreakVector(ReturnValue3_2)
        ReturnValue_14: float = Z3 - Z
        ReturnValue_15: float = Abs(ReturnValue_14)
        ReturnValue1_7: bool = GreaterEqual_FloatFloat(ReturnValue_15, 500)
        if not ReturnValue1_7:
           goto(ExecutionFlow.Pop())
        
        Item = None
        Item = Values[Variable1_1]
        ReturnValue_13 = Item.K2_GetActorLocation()
        
        X = None
        Y = None
        Z = None
        X, Y, Z = BreakVector(ReturnValue_13)
        ReturnValue = Default__GameplayStatics.GetPlayerController(self, 0)
        ReturnValue_0 = ReturnValue.K2_GetPawn()
        ReturnValue3_2 = ReturnValue_0.K2_GetActorLocation()
        
        X3 = None
        Y3 = None
        Z3 = None
        X3, Y3, Z3 = BreakVector(ReturnValue3_2)
        ReturnValue1_8: Vector = Vector(X, Y, Z3)
        ReturnValue_16: bool = Item.K2_TeleportTo(ReturnValue1_8, Rotator::FromPitchYawRoll(0, 0, 0))
        goto(ExecutionFlow.Pop())
        # Label 3954
        ReturnValue2_2: int32 = Variable_1 + 1
        Variable_1 = ReturnValue2_2
        goto('L2886')
        # Label 4028
        ReturnValue_17: int32 = Variable_0 + 1
        Variable_0 = ReturnValue_17
        goto('L1981')
        # Label 4102
        ReturnValue1_9: int32 = Variable1_0 + 1
        Variable1_0 = ReturnValue1_9
        goto('L2057')
        # Label 4176
        ReturnValue = Default__GameplayStatics.GetPlayerController(self, 0)
        ReturnValue_0 = ReturnValue.K2_GetPawn()
        ReturnValue2 = ReturnValue_0.K2_GetActorLocation()
        
        X2 = None
        Y2 = None
        Z2 = None
        X2, Y2, Z2 = BreakVector(ReturnValue2)
        ReturnValue1_0 = Y2 / 1000
        ReturnValue1_1 = FTrunc(ReturnValue1_0)
        ReturnValue2_0 = X2 / 1000
        ReturnValue2_1 = FTrunc(ReturnValue2_0)
        IntVector2D.X_2_3FF107F84D30EB52DD50898C7D2CAD67 = ReturnValue2_1
        IntVector2D.Y_4_F18C5B824136D7759146338CAA496F0A = ReturnValue1_1
        ReturnValue5 = Variable_0 + IntVector2D.Y_4_F18C5B824136D7759146338CAA496F0A
        ReturnValue6 = Variable1_0 + IntVector2D.X_2_3FF107F84D30EB52DD50898C7D2CAD67
        IntVector2D2.X_2_3FF107F84D30EB52DD50898C7D2CAD67 = ReturnValue6
        IntVector2D2.Y_4_F18C5B824136D7759146338CAA496F0A = ReturnValue5
        ReturnValue_18: float = IntVector2D2.Y_4_F18C5B824136D7759146338CAA496F0A * 1000
        ReturnValue1_10: float = IntVector2D2.X_2_3FF107F84D30EB52DD50898C7D2CAD67 * 1000
        ReturnValue3_2 = ReturnValue_0.K2_GetActorLocation()
        
        X3 = None
        Y3 = None
        Z3 = None
        X3, Y3, Z3 = BreakVector(ReturnValue3_2)
        ReturnValue_19: Vector = Vector(ReturnValue1_10, ReturnValue_18, Z3)
        ReturnValue_20: Transform = Conv_VectorToTransform(ReturnValue_19)
        
        ReturnValue_21: Ptr[Actor] = Default__GameplayStatics.BeginDeferredActorSpawnFromClass(self, RainActor, 1, None, Ref[ReturnValue_20])
        ReturnValue = Default__GameplayStatics.GetPlayerController(self, 0)
        ReturnValue_0 = ReturnValue.K2_GetPawn()
        ReturnValue2 = ReturnValue_0.K2_GetActorLocation()
        
        X2 = None
        Y2 = None
        Z2 = None
        X2, Y2, Z2 = BreakVector(ReturnValue2)
        ReturnValue1_0 = Y2 / 1000
        ReturnValue1_1 = FTrunc(ReturnValue1_0)
        ReturnValue2_0 = X2 / 1000
        ReturnValue2_1 = FTrunc(ReturnValue2_0)
        IntVector2D.X_2_3FF107F84D30EB52DD50898C7D2CAD67 = ReturnValue2_1
        IntVector2D.Y_4_F18C5B824136D7759146338CAA496F0A = ReturnValue1_1
        ReturnValue5 = Variable_0 + IntVector2D.Y_4_F18C5B824136D7759146338CAA496F0A
        ReturnValue6 = Variable1_0 + IntVector2D.X_2_3FF107F84D30EB52DD50898C7D2CAD67
        IntVector2D2.X_2_3FF107F84D30EB52DD50898C7D2CAD67 = ReturnValue6
        IntVector2D2.Y_4_F18C5B824136D7759146338CAA496F0A = ReturnValue5
        ReturnValue_18 = IntVector2D2.Y_4_F18C5B824136D7759146338CAA496F0A * 1000
        ReturnValue1_10 = IntVector2D2.X_2_3FF107F84D30EB52DD50898C7D2CAD67 * 1000
        ReturnValue3_2 = ReturnValue_0.K2_GetActorLocation()
        
        X3 = None
        Y3 = None
        Z3 = None
        X3, Y3, Z3 = BreakVector(ReturnValue3_2)
        ReturnValue_19 = Vector(ReturnValue1_10, ReturnValue_18, Z3)
        ReturnValue_20 = Conv_VectorToTransform(ReturnValue_19)
        
        ReturnValue_22: Ptr[RainActor] = Default__GameplayStatics.FinishSpawningActor(ReturnValue_21, Ref[ReturnValue_20])
        ReturnValue = Default__GameplayStatics.GetPlayerController(self, 0)
        ReturnValue_0 = ReturnValue.K2_GetPawn()
        ReturnValue2 = ReturnValue_0.K2_GetActorLocation()
        
        X2 = None
        Y2 = None
        Z2 = None
        X2, Y2, Z2 = BreakVector(ReturnValue2)
        ReturnValue1_0 = Y2 / 1000
        ReturnValue1_1 = FTrunc(ReturnValue1_0)
        ReturnValue2_0 = X2 / 1000
        ReturnValue2_1 = FTrunc(ReturnValue2_0)
        IntVector2D.X_2_3FF107F84D30EB52DD50898C7D2CAD67 = ReturnValue2_1
        IntVector2D.Y_4_F18C5B824136D7759146338CAA496F0A = ReturnValue1_1
        ReturnValue5 = Variable_0 + IntVector2D.Y_4_F18C5B824136D7759146338CAA496F0A
        ReturnValue6 = Variable1_0 + IntVector2D.X_2_3FF107F84D30EB52DD50898C7D2CAD67
        IntVector2D2.X_2_3FF107F84D30EB52DD50898C7D2CAD67 = ReturnValue6
        IntVector2D2.Y_4_F18C5B824136D7759146338CAA496F0A = ReturnValue5
        
        IntVector2D2 = None
        Default__BlueprintMapLibrary.Map_Add(Ref[self.SpawnedComponentMap], Ref[IntVector2D2], Ref[ReturnValue_22])
        goto(ExecutionFlow.Pop())
        # Label 6734
        Variable = 0
        goto('L1815')
        Values1: List[Ptr[Actor]] = []
        
        Default__BlueprintMapLibrary.Map_Values(Ref[self.SpawnedComponentMap], Ref[Values1])
        Variable1 = 0
        goto('L6734')
    
