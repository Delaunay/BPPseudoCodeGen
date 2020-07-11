
from codegen.ue4_stub import *

from Script.Engine import Default__KismetSystemLibrary
from Script.UMG import GetOwningPlayerPawn
from Game.FactoryGame.Interface.UI.Audio.CursorParticles.Play_UI_CursorParticle_Glass import Play_UI_CursorParticle_Glass
from Game.FactoryGame.Interface.UI.InGame.CursorParticles.BP_CursorParticle import BP_CursorParticle
from Script.AkAudio import PostAkEvent
from Script.Engine import Delay
from Script.Engine import Pawn
from Script.AkAudio import AkComponent
from Script.AkAudio import Default__AkGameplayStatics
from Game.FactoryGame.Interface.UI.InGame.CursorParticles.CursorParticle_Glass import ExecuteUbergraph_CursorParticle_Glass
from Script.Engine import LatentActionInfo

class CursorParticle_Glass(BP_CursorParticle):
    
    
    def Construct(self):
        self.ExecuteUbergraph_CursorParticle_Glass(188)
    

    def ExecuteUbergraph_CursorParticle_Glass(self):
        goto(ComputedJump("EntryPoint"))
        self.RemoveFromParent()
        goto(ExecutionFlow.Pop())
        # Label 30
        ReturnValue: Ptr[Pawn] = self.GetOwningPlayerPawn()
        ReturnValue_0: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_UI_CursorParticle_Glass, ReturnValue, False)
        Default__KismetSystemLibrary.Delay(self, 0.20000000298023224, LatentActionInfo(Linkage = 15, UUID = -1661903783, ExecutionFunction = "ExecuteUbergraph_CursorParticle_Glass", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        goto('L30')
    
