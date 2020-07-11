
from codegen.ue4_stub import *

from Script.UMG import GetOwningPlayerPawn
from Script.Engine import RandomIntegerInRange
from Game.FactoryGame.Interface.UI.Audio.CursorParticles.Play_UI_CursorParticle_Plastic import Play_UI_CursorParticle_Plastic
from Script.AkAudio import PostAkEvent
from Script.Engine import Pawn
from Game.FactoryGame.Interface.UI.InGame.CursorParticles.CursorParticle_Plastic import ExecuteUbergraph_CursorParticle_Plastic
from Script.AkAudio import AkComponent
from Script.AkAudio import Default__AkGameplayStatics
from Game.FactoryGame.Interface.UI.InGame.CursorParticles.BP_CursorParticle import BP_CursorParticle

class CursorParticle_Plastic(BP_CursorParticle):
    
    
    def Construct(self):
        self.ExecuteUbergraph_CursorParticle_Plastic(96)
    

    def ExecuteUbergraph_CursorParticle_Plastic(self):
        # Label 10
        ReturnValue: Ptr[Pawn] = self.GetOwningPlayerPawn()
        ReturnValue_0: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_UI_CursorParticle_Plastic, ReturnValue, False)
        # End
        ReturnValue_1: int32 = RandomIntegerInRange(5, 8)
        self.Widget_GenericParticleSpawner.CreateParticles(ReturnValue_1)
        goto('L10')
    
