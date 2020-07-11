
from codegen.ue4_stub import *

from Script.Engine import Actor
from Script.AkAudio import PostAkEvent
from Game.FactoryGame.Cinematics.MainMenu.Audio.Play_MainMenu_2_Ambience import Play_MainMenu_2_Ambience
from Script.AkAudio import AkComponent
from Script.AkAudio import Default__AkGameplayStatics
from Game.FactoryGame.Cinematics.MainMenu.Audio.MainMenu_2_Audio import ExecuteUbergraph_MainMenu_2_Audio

class MainMenu_2_Audio(Actor):
    
    
    def ReceiveBeginPlay(self):
        self.ExecuteUbergraph_MainMenu_2_Audio(10)
    

    def ExecuteUbergraph_MainMenu_2_Audio(self):
        ReturnValue: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_MainMenu_2_Ambience, self, True)
    
