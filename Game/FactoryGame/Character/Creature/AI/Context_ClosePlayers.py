
from codegen.ue4_stub import *

from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import Default__GameplayStatics
from Script.Engine import K2_GetActorLocation
from Script.Engine import Default__KismetArrayLibrary
from Script.FactoryGame import FGCharacterPlayer
from Script.Engine import Subtract_VectorVector
from Script.CoreUObject import Vector
from Script.Engine import GetDisplayName
from Script.Engine import Array_AddUnique
from Script.AIModule import EnvQueryContext_BlueprintBase
from Script.Engine import GetAllActorsOfClass
from Script.Engine import VSize
from Script.Engine import PrintString
from Script.CoreUObject import LinearColor

class Context_ClosePlayers(EnvQueryContext_BlueprintBase):
    
    
    def ProvideSingleActor(self):
        ReturnValue: FString = Default__KismetSystemLibrary.GetDisplayName(QuerierActor)
        Default__KismetSystemLibrary.PrintString(self, ReturnValue, True, True, LinearColor(R = 0, G = 0.6600000262260437, B = 1, A = 1), 2)
        OutActors: List[Ptr[FGCharacterPlayer]] = []
        
        Default__GameplayStatics.GetAllActorsOfClass(self, FGCharacterPlayer, Ref[OutActors])
        
        Item = None
        Item = OutActors[0]
        ResultingActor = Item
    

    def ProvideActorsSet(self):
        ExecutionFlow.Push("L776")
        OutActors: List[Ptr[FGCharacterPlayer]] = []
        
        Default__GameplayStatics.GetAllActorsOfClass(self, FGCharacterPlayer, Ref[OutActors])
        Variable: int32 = 0
        Variable_0: int32 = 0
        
        # Label 113
        ReturnValue: int32 = len(OutActors)
        ReturnValue_0: bool = Variable <= ReturnValue
        if not ReturnValue_0:
            goto('L670')
        Variable_0 = Variable
        ExecutionFlow.Push("L702")
        ReturnValue_1: Vector = QuerierActor.K2_GetActorLocation()
        
        Item = None
        Item = OutActors[Variable_0]
        ReturnValue1: Vector = Item.K2_GetActorLocation()
        ReturnValue_2: Vector = Subtract_VectorVector(ReturnValue_1, ReturnValue1)
        ReturnValue_3: float = VSize(ReturnValue_2)
        ReturnValue_4: bool = ReturnValue_3 <= 20000
        if not ReturnValue_4:
           goto(ExecutionFlow.Pop())
        
        Item = None
        Item = OutActors[Variable_0]
        
        Item = None
        ReturnValue_5: int32 = Default__KismetArrayLibrary.Array_AddUnique(Ref[closeCharacters], Ref[Item])
        goto(ExecutionFlow.Pop())
        # Label 670
        ResultingActorsSet = closeCharacters
        # End
        # Label 702
        ReturnValue_6: int32 = Variable + 1
        Variable = ReturnValue_6
        goto('L113')
    
