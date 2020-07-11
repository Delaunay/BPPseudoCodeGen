
from codegen.ue4_stub import *

from Script.Engine import Conv_TextToString
from Script.Engine import Conv_VectorToString
from Script.FactoryGame import FGPlayerController
from Script.FactoryGame import GetRealActor
from Script.Engine import GetDisplayName
from Script.FactoryGame import GetVisitedMapAreas
from Script.FactoryGame import GetCurrentMapArea
from Script.Engine import Default__KismetSystemLibrary
from Script.FactoryGame import GetAreaDisplayName
from Script.Engine import PlayerController
from Script.FactoryGame import Get
from Script.Engine import ReceiveTick
from Script.Engine import Default__KismetArrayLibrary
from Game.FactoryGame.-Shared.Blueprint.BP_GameState import ExecuteUbergraph_BP_GameState
from Script.FactoryGame import Default__FGActorRepresentationManager
from Script.Engine import Default__KismetTextLibrary
from Script.Engine import GetPlayerController
from Script.FactoryGame import FGMapArea
from Script.Engine import Default__GameplayStatics
from Script.FactoryGame import FGGameState
from Script.FactoryGame import GetAllActorRepresentations
from Script.CoreUObject import Vector
from Script.FactoryGame import FGActorRepresentationManager
from Script.Engine import Default__KismetStringLibrary
from Script.Engine import Conv_IntToString
from Game.FactoryGame.-Shared.Blueprint.BP_GameState import ExecuteUbergraph_BP_GameState.K2Node_Event_DeltaSeconds
from Script.FactoryGame import Default__FGMapArea
from Script.Engine import Actor
from Script.FactoryGame import GetActorLocation
from Script.Engine import Concat_StrStr
from Script.Engine import PrintString
from Script.CoreUObject import LinearColor

class BP_GameState(FGGameState):
    mTurboModeMultiplier = 8
    mPowerCircuitFuseTriggeredMessage = NewObject[PowerCircuitFuseTriggered]()
    mPlannedRestartTime = 24
    mHubPartClass = NewObject[Desc_HUBParts]()
    PrimaryActorTick = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=120, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=True, bTickEvenWhenPaused=True)
    
    def DumpVisistedMapAreas(self):
        ExecutionFlow.Push("L975")
        ReturnValue: Ptr[PlayerController] = Default__GameplayStatics.GetPlayerController(self, 0)
        Controller: Ptr[FGPlayerController] = Cast[FGPlayerController](ReturnValue)
        bSuccess: bool = Controller
        ReturnValue_0: TSubclassOf[FGMapArea] = Controller.GetCurrentMapArea()
        ReturnValue1: FText = Default__FGMapArea.GetAreaDisplayName(ReturnValue_0)
        
        ReturnValue1_0: FString = Default__KismetTextLibrary.Conv_TextToString(Ref[ReturnValue1])
        ReturnValue_1: FString = Default__KismetStringLibrary.Concat_StrStr("Player is in: ", ReturnValue1_0)
        Default__KismetSystemLibrary.PrintString(self, ReturnValue_1, True, False, LinearColor(R = 0.3371640145778656, G = 0.32777801156044006, B = 0.03688900172710419, A = 1), 0)
        
        self.GetVisitedMapAreas(Ref[mapAreas])
        Variable: int32 = 0
        Variable_0: int32 = 0
        
        # Label 501
        ReturnValue_2: int32 = len(mapAreas)
        ReturnValue_3: bool = Variable <= ReturnValue_2
        if not ReturnValue_3:
           goto(ExecutionFlow.Pop())
        Variable_0 = Variable
        ExecutionFlow.Push("L901")
        
        Item = None
        Item = mapAreas[Variable_0]
        ReturnValue_4: FText = Default__FGMapArea.GetAreaDisplayName(Item)
        
        ReturnValue_5: FString = Default__KismetTextLibrary.Conv_TextToString(Ref[ReturnValue_4])
        Default__KismetSystemLibrary.PrintString(self, ReturnValue_5, True, False, LinearColor(R = 0, G = 0.6600000262260437, B = 1, A = 1), 0)
        goto(ExecutionFlow.Pop())
        # Label 901
        ReturnValue_6: int32 = Variable + 1
        Variable = ReturnValue_6
        goto('L501')
    

    def DumpActorRepresentations(self):
        ExecutionFlow.Push("L1020")
        ReturnValue: Ptr[FGActorRepresentationManager] = Default__FGActorRepresentationManager.Get(self)
        
        ReturnValue.GetAllActorRepresentations(Ref[allRepresentations])
        Variable: int32 = 0
        Variable_0: int32 = 0
        
        # Label 135
        ReturnValue_0: int32 = len(allRepresentations)
        ReturnValue_1: bool = Variable <= ReturnValue_0
        if not ReturnValue_1:
           goto(ExecutionFlow.Pop())
        Variable_0 = Variable
        ExecutionFlow.Push("L946")
        ReturnValue_2: FString = Default__KismetStringLibrary.Conv_IntToString(Variable_0)
        ReturnValue_3: FString = Default__KismetStringLibrary.Concat_StrStr(ReturnValue_2, ": ")
        
        Item = None
        Item = allRepresentations[Variable_0]
        ReturnValue_4: Vector = Item.GetActorLocation()
        ReturnValue_5: FString = Default__KismetStringLibrary.Conv_VectorToString(ReturnValue_4)
        ReturnValue_6: Ptr[Actor] = Item.GetRealActor()
        ReturnValue_7: FString = Default__KismetSystemLibrary.GetDisplayName(ReturnValue_6)
        ReturnValue1: FString = Default__KismetStringLibrary.Concat_StrStr(ReturnValue_3, ReturnValue_7)
        ReturnValue2: FString = Default__KismetStringLibrary.Concat_StrStr(ReturnValue1, "")
        ReturnValue3: FString = Default__KismetStringLibrary.Concat_StrStr(ReturnValue2, ReturnValue_5)
        Default__KismetSystemLibrary.PrintString(self, ReturnValue3, True, True, LinearColor(R = 0, G = 0.6600000262260437, B = 1, A = 1), 9.999999747378752e-05)
        goto(ExecutionFlow.Pop())
        # Label 946
        ReturnValue_8: int32 = Variable + 1
        Variable = ReturnValue_8
        goto('L135')
    

    def ReceiveTick(self):
        ExecuteUbergraph_BP_GameState.K2Node_Event_DeltaSeconds = DeltaSeconds #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_GameState(10)
    

    def ExecuteUbergraph_BP_GameState(self):
        self.ReceiveTick(DeltaSeconds)
    
