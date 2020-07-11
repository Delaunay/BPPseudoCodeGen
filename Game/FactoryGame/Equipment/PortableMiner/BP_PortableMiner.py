
from codegen.ue4_stub import *

from Script.AkAudio import AkAudioEvent
from Game.FactoryGame.Equipment.PortableMiner.BP_PortableMiner import ExecuteUbergraph_BP_PortableMiner
from Script.FactoryGame import ShowOutline
from Script.Engine import K2_GetActorLocation
from Game.FactoryGame.Equipment.PortableMiner.BP_PortableMiner import ExecuteUbergraph_BP_PortableMiner.K2Node_Event_state
from Game.FactoryGame.Equipment.PortableMiner.BP_PortableMiner import ExecuteUbergraph_BP_PortableMiner.K2Node_Event_state1
from Script.CoreUObject import Vector
from Game.FactoryGame.Equipment.PortableMiner.BP_PortableMiner import ExecuteUbergraph_BP_PortableMiner.K2Node_Event_byCharacter
from Script.AkAudio import PostAkEventAtLocation
from Script.AkAudio import AkComponent
from Script.FactoryGame import HideOutline
from Script.FactoryGame import FGPortableMiner
from Script.FactoryGame import Default__FGBlueprintFunctionLibrary
from Game.FactoryGame.Character.Player.Audio.SB_CharacterEssentials.Play_P_ResourcePickUp import Play_P_ResourcePickUp
from Game.FactoryGame.Equipment.PortableMiner.BP_PortableMiner import ExecuteUbergraph_BP_PortableMiner.K2Node_Event_byCharacter1
from Script.AkAudio import Default__AkGameplayStatics

class BP_PortableMiner(FGPortableMiner):
    mAmbientLoop: Ptr[AkAudioEvent]
    mAmbientStop: Ptr[AkAudioEvent]
    mExtractCycleTime = 1.5
    mInteractWidgetClass = NewObject[Widget_PortableMiner]()
    mInventorySize = 1
    PrimaryActorTick = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=True, bTickEvenWhenPaused=False)
    bReplicates = True
    RemoteRole = 1
    
    def StopIsLookedAt(self):
        ExecuteUbergraph_BP_PortableMiner.K2Node_Event_byCharacter1 = byCharacter #  PERSISTENT_FRAME(
        ExecuteUbergraph_BP_PortableMiner.K2Node_Event_state1 = State #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_PortableMiner(195)
    

    def StartIsLookedAt(self):
        ExecuteUbergraph_BP_PortableMiner.K2Node_Event_byCharacter = byCharacter #  PERSISTENT_FRAME(
        ExecuteUbergraph_BP_PortableMiner.K2Node_Event_state = State #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_PortableMiner(200)
    

    def ReceiveDestroyed(self):
        self.ExecuteUbergraph_BP_PortableMiner(205)
    

    def ExecuteUbergraph_BP_PortableMiner(self):
        # Label 10
        Default__FGBlueprintFunctionLibrary.ShowOutline(None, 252)
        # End
        # Label 50
        ReturnValue: Vector = self.K2_GetActorLocation()
        ReturnValue_0: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEventAtLocation(self, Play_P_ResourcePickUp, ReturnValue, Rotator::FromPitchYawRoll(0, 0, 0))
        # End
        # Label 157
        Default__FGBlueprintFunctionLibrary.HideOutline(None)
        # End
        goto('L157')
        goto('L10')
        goto('L50')
    
