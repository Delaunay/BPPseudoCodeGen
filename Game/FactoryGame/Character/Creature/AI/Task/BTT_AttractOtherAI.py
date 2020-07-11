
from codegen.ue4_stub import *

from Script.AIModule import GetBlackboardValueAsActor
from Script.AIModule import BlackboardComponent
from Script.AIModule import SetValueAsBool
from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import Default__KismetArrayLibrary
from Script.AIModule import Default__BTFunctionLibrary
from Script.AIModule import FinishExecute
from Game.FactoryGame.Character.Creature.AI.Task.BTT_AttractOtherAI import ExecuteUbergraph_BTT_AttractOtherAI.K2Node_Event_ControlledPawn
from Script.AIModule import BlackboardKeySelector
from Script.AIModule import Default__AIBlueprintHelperLibrary
from Script.Engine import IsValid
from Script.Engine import GetAllActorsOfClass
from Game.FactoryGame.Character.Creature.Enemy.Hog.Char_Hog import Char_Hog
from Script.Engine import Default__GameplayStatics
from Script.AIModule import BTTask_BlueprintBase
from Game.FactoryGame.Character.Creature.AI.Task.BTT_AttractOtherAI import ExecuteUbergraph_BTT_AttractOtherAI.K2Node_Event_OwnerController
from Script.AIModule import GetBlackboard
from Script.CoreUObject import Vector
from Script.Engine import MinOfFloatArray
from Script.Engine import Actor
from Script.Engine import GetDistanceTo
from Script.AIModule import SetValueAsObject
from Script.Engine import Min
from Script.Engine import Array_Clear
from Game.FactoryGame.Character.Creature.AI.Task.BTT_AttractOtherAI import ExecuteUbergraph_BTT_AttractOtherAI

class BTT_AttractOtherAI(BTTask_BlueprintBase):
    RequiredBoolKey: FName = DidHearNoise
    SummonLocationKey: FName = NoiseLocation
    MinimumRange: float = 3000
    MaximumRange: float = 20000
    DistanceArray: List[float]
    MaxSummonedHogs: int32 = 3
    SortedHogs: List[Ptr[Char_Hog]]
    NearbyHogs: List[Ptr[Char_Hog]]
    mOtherLocationOption: BlackboardKeySelector
    UsedLocation: Vector
    
    def ReceiveExecuteAI(self):
        ExecuteUbergraph_BTT_AttractOtherAI.K2Node_Event_OwnerController = OwnerController #  PERSISTENT_FRAME(
        ExecuteUbergraph_BTT_AttractOtherAI.K2Node_Event_ControlledPawn = ControlledPawn #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BTT_AttractOtherAI(15)
    

    def ExecuteUbergraph_BTT_AttractOtherAI(self):
        goto(ComputedJump("EntryPoint"))
        OutActors: List[Ptr[Char_Hog]] = []
        
        Default__GameplayStatics.GetAllActorsOfClass(self, Char_Hog, Ref[OutActors])
        Variable: int32 = 0
        Variable_0: int32 = 0
        
        # Label 123
        ReturnValue1: int32 = len(OutActors)
        ReturnValue: bool = Variable <= ReturnValue1
        if not ReturnValue:
            goto('L822')
        Variable_0 = Variable
        ExecutionFlow.Push("L2035")
        
        Item1 = None
        Item1 = OutActors[Variable_0]
        ReturnValue_0: float = Item1.GetDistanceTo(ControlledPawn)
        ReturnValue_1: bool = ReturnValue_0 <= self.MaximumRange
        ReturnValue_2: bool = ReturnValue_0 > self.MinimumRange
        ReturnValue_3: bool = ReturnValue_2 and ReturnValue_1
        if not ReturnValue_3:
           goto(ExecutionFlow.Pop())
        
        Item1 = None
        Item1 = OutActors[Variable_0]
        
        Item1 = None
        ReturnValue1_0: int32 = self.NearbyHogs.append(Item1)
        
        Item1 = None
        Item1 = OutActors[Variable_0]
        ReturnValue_0 = Item1.GetDistanceTo(ControlledPawn)
        
        ReturnValue_4: int32 = self.DistanceArray.append(ReturnValue_0)
        goto(ExecutionFlow.Pop())
        
        # Label 822
        ReturnValue2: int32 = len(self.DistanceArray)
        ReturnValue_5: bool = ReturnValue2 > 0
        if not ReturnValue_5:
            goto('L1273')
        ExecutionFlow.Push("L822")
        
        IndexOfMinValue = None
        MinValue = None
        MinOfFloatArray(Ref[self.DistanceArray], Ref[IndexOfMinValue], Ref[MinValue])
        
        Item2 = None
        Item2 = self.NearbyHogs[IndexOfMinValue]
        
        Item2 = None
        ReturnValue2_0: int32 = self.SortedHogs.append(Item2)
        
        IndexOfMinValue = None
        MinValue = None
        MinOfFloatArray(Ref[self.DistanceArray], Ref[IndexOfMinValue], Ref[MinValue])
        
        self.DistanceArray.remove(IndexOfMinValue)
        
        IndexOfMinValue = None
        MinValue = None
        MinOfFloatArray(Ref[self.DistanceArray], Ref[IndexOfMinValue], Ref[MinValue])
        
        self.NearbyHogs.remove(IndexOfMinValue)
        goto(ExecutionFlow.Pop())
        # Label 1273
        Variable_1: int32 = 0
        
        # Label 1296
        ReturnValue_6: int32 = len(self.SortedHogs)
        ReturnValue_7: int32 = Min(ReturnValue_6, self.MaxSummonedHogs)
        ReturnValue_8: int32 = ReturnValue_7 - 1
        ReturnValue_9: bool = Variable_1 <= ReturnValue_8
        if not ReturnValue_9:
            goto('L1982')
        ExecutionFlow.Push("L2109")
        
        ReturnValue_10: Ptr[Actor] = Default__BTFunctionLibrary.GetBlackboardValueAsActor(self, Ref[self.mOtherLocationOption])
        ReturnValue_11: bool = Default__KismetSystemLibrary.IsValid(ReturnValue_10)
        if not ReturnValue_11:
            goto('L2183')
        
        Item = None
        Item = self.SortedHogs[Variable_1]
        ReturnValue_12: Ptr[BlackboardComponent] = Default__AIBlueprintHelperLibrary.GetBlackboard(Item)
        
        ReturnValue_10 = Default__BTFunctionLibrary.GetBlackboardValueAsActor(self, Ref[self.mOtherLocationOption])
        
        ReturnValue_12.SetValueAsObject(ReturnValue_10, Ref[self.SummonLocationKey])
        
        Item = None
        Item = self.SortedHogs[Variable_1]
        ReturnValue_12 = Default__AIBlueprintHelperLibrary.GetBlackboard(Item)
        
        ReturnValue_12.SetValueAsBool(True, Ref[self.RequiredBoolKey])
        goto(ExecutionFlow.Pop())
        
        # Label 1982
        Default__KismetArrayLibrary.Array_Clear(Ref[self.SortedHogs])
        self.FinishExecute(True)
        goto(ExecutionFlow.Pop())
        # Label 2035
        ReturnValue1_1: int32 = Variable + 1
        Variable = ReturnValue1_1
        goto('L123')
        # Label 2109
        ReturnValue_13: int32 = Variable_1 + 1
        Variable_1 = ReturnValue_13
        goto('L1296')
        
        Item = None
        # Label 2183
        Item = self.SortedHogs[Variable_1]
        ReturnValue_12 = Default__AIBlueprintHelperLibrary.GetBlackboard(Item)
        
        ReturnValue_12.SetValueAsObject(ControlledPawn, Ref[self.SummonLocationKey])
        goto(ExecutionFlow.Pop())
    
