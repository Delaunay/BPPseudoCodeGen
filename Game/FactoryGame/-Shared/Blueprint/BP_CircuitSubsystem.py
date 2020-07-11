
from codegen.ue4_stub import *

from Script.FactoryGame import FGCircuitSubsystem
from Script.AkAudio import PostAkEvent
from Script.Engine import Default__GameplayStatics
from Script.FactoryGame import FGGameState
from Script.Engine import GameStateBase
from Script.FactoryGame import SendMessageToAllPlayers
from Game.FactoryGame.Interface.UI.Message.Notification.PowerCircuitFuseTriggered import PowerCircuitFuseTriggered
from Script.Engine import GetGameState
from Script.AkAudio import AkComponent
from Game.FactoryGame.Interface.UI.Audio.PowerStatus.Play_UI_PowerLossWarning_PowerLoss import Play_UI_PowerLossWarning_PowerLoss
from Script.AkAudio import Default__AkGameplayStatics
from Game.FactoryGame.-Shared.Blueprint.BP_CircuitSubsystem import ExecuteUbergraph_BP_CircuitSubsystem

class BP_CircuitSubsystem(FGCircuitSubsystem):
    PrimaryActorTick = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=True, bTickEvenWhenPaused=False)
    bAlwaysRelevant = True
    bReplicates = True
    RemoteRole = 1
    
    def PowerCircuit_OnFuseSet(self):
        self.ExecuteUbergraph_BP_CircuitSubsystem(68)
    

    def Multicast_PlayFuseSetSound(self):
        self.ExecuteUbergraph_BP_CircuitSubsystem(250)
    

    def ExecuteUbergraph_BP_CircuitSubsystem(self):
        # Label 10
        ReturnValue: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_UI_PowerLossWarning_PowerLoss, self, True)
        # End
        ReturnValue_0: Ptr[GameStateBase] = Default__GameplayStatics.GetGameState(self)
        State: Ptr[FGGameState] = Cast[FGGameState](ReturnValue_0)
        bSuccess: bool = State
        if not bSuccess:
            goto('L255')
        State.SendMessageToAllPlayers(PowerCircuitFuseTriggered)
        self.Multicast_PlayFuseSetSound()
        # End
        goto('L10')
    
