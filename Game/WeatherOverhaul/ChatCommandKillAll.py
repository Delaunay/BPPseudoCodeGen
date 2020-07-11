
from codegen.ue4_stub import *

from Script.FactoryGame import FGHealthComponent
from Script.Engine import Conv_TextToString
from Script.FactoryGame import FGPlayerController
from Script.Engine import GetComponentByClass
from Script.Engine import Pawn
from Script.Engine import SphereOverlapActors
from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import Default__KismetArrayLibrary
from Script.Engine import K2_GetPawn
from Script.Engine import FormatArgumentData
from Script.Engine import IsValid
from Script.Engine import EObjectTypeQuery
from Script.Engine import Default__KismetTextLibrary
from Script.CoreUObject import Vector
from Script.Engine import Format
from Script.Engine import Default__KismetStringLibrary
from Script.SML import EExecutionStatus
from Script.SML import ChatCommandInstance
from Script.FactoryGame import Kill
from Script.Engine import Actor
from Script.Engine import K2_GetActorLocation
from Script.Engine import Conv_StringToFloat
from Script.CoreUObject import LinearColor

class ChatCommandKillAll(ChatCommandInstance):
    bOnlyUsableByPlayer = True
    MinNumberOfArguments = 1
    modid = SML
    CommandName = killall
    Usage = NewObject[]()
    
    def ExecuteCommand(self):
        ExecutionFlow.Push("L1810")
        ReturnValue: Ptr[FGPlayerController] = Sender.GetPlayer()
        ReturnValue_0: float = Default__KismetStringLibrary.Conv_StringToFloat(Arguments[0])
        ReturnValue_1: Ptr[Pawn] = ReturnValue.K2_GetPawn()
        Array: Const[List[Ptr[Actor]]] = [ReturnValue_1]
        ReturnValue_2: Vector = ReturnValue_1.K2_GetActorLocation()
        ReturnValue_3: float = ReturnValue_0 * 100
        Array1: Const[List[uint8]] = [2]
        OutActors: List[Ptr[Actor]] = []
        
        ReturnValue_4: bool = Default__KismetSystemLibrary.SphereOverlapActors(self, ReturnValue_2, ReturnValue_3, Pawn, Ref[Array1], Ref[Array], Ref[OutActors])
        Variable: int32 = 0
        Variable_0: int32 = 0
        
        # Label 437
        ReturnValue_5: int32 = len(OutActors)
        ReturnValue_6: bool = Variable <= ReturnValue_5
        if not ReturnValue_6:
            goto('L963')
        Variable_0 = Variable
        ExecutionFlow.Push("L1736")
        
        Item = None
        Item = OutActors[Variable_0]
        ReturnValue_7: Ptr[FGHealthComponent] = Item.GetComponentByClass(FGHealthComponent)
        ReturnValue_8: bool = Default__KismetSystemLibrary.IsValid(ReturnValue_7)
        if not ReturnValue_8:
           goto(ExecutionFlow.Pop())
        
        Item = None
        Item = OutActors[Variable_0]
        ReturnValue_7 = Item.GetComponentByClass(FGHealthComponent)
        ReturnValue_7.Kill()
        ReturnValue1: int32 = EntitiesDamaged + 1
        EntitiesDamaged = ReturnValue1
        goto(ExecutionFlow.Pop())
        # Label 963
        ReturnValue_0 = Default__KismetStringLibrary.Conv_StringToFloat(Arguments[0])
        FormatArgumentData.ArgumentName = "Radius"
        FormatArgumentData.ArgumentValueType = 2
        FormatArgumentData.ArgumentValue = 
        FormatArgumentData.ArgumentValueInt = 0
        FormatArgumentData.ArgumentValueFloat = ReturnValue_0
        FormatArgumentData.ArgumentValueGender = 0
        FormatArgumentData1.ArgumentName = "Count"
        FormatArgumentData1.ArgumentValueType = 0
        FormatArgumentData1.ArgumentValue = 
        FormatArgumentData1.ArgumentValueInt = EntitiesDamaged
        FormatArgumentData1.ArgumentValueFloat = 0
        FormatArgumentData1.ArgumentValueGender = 0
        Array2: List[FormatArgumentData] = [FormatArgumentData1, FormatArgumentData]
        ReturnValue_9: FText = Default__KismetTextLibrary.Format("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 1487, 'Value': 'Killed {Count} creatures in {Radius}m.'}", Array2)
        
        ReturnValue_10: FString = Default__KismetTextLibrary.Conv_TextToString(Ref[ReturnValue_9])
        Sender.SendChatMessage(ReturnValue_10, LinearColor(R = 0, G = 1, B = 0, A = 1))
        ReturnValue_11: uint8 = 0
        goto('L1810')
        # Label 1736
        ReturnValue_12: int32 = Variable + 1
        Variable = ReturnValue_12
        goto('L437')
    
