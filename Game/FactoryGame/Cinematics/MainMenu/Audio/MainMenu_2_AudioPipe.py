
from codegen.ue4_stub import *

from Script.Engine import Actor
from Script.AkAudio import PostAkEvent
from Game.FactoryGame.Cinematics.MainMenu.Audio.MainMenu_2_AudioPipe import ExecuteUbergraph_MainMenu_2_AudioPipe
from Game.FactoryGame.Cinematics.MainMenu.Audio.Play_MainMenu_2_Pipe import Play_MainMenu_2_Pipe
from Script.AkAudio import AkComponent
from Script.AkAudio import Default__AkGameplayStatics

class MainMenu_2_AudioPipe(Actor):
    
    
    def ReceiveBeginPlay(self):
        self.ExecuteUbergraph_MainMenu_2_AudioPipe(68)
    

    def ExecuteUbergraph_MainMenu_2_AudioPipe(self):
        # Label 10
        ReturnValue: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_MainMenu_2_Pipe, self, True)
        # End
        goto('L10')
    
