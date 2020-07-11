
from codegen.ue4_stub import *

from Script.Engine import Default__KismetSystemLibrary
from Game.FactoryGame.Cinematics.MainMenu.Audio.Play_MainMenu_2_Pump import Play_MainMenu_2_Pump
from Script.Engine import K2_SetTimer
from Script.Engine import ETimelineDirection
from Script.AkAudio import PostAkEvent
from Script.Engine import K2_ClearAndInvalidateTimerHandle
from Script.Engine import Actor
from Script.Engine import PlayFromStart
from Script.AkAudio import SetActorRTPCValue
from Script.Engine import TimerHandle
from Script.Engine import SetComponentTickInterval
from Script.AkAudio import AkComponent
from Script.AkAudio import Default__AkGameplayStatics
from Game.FactoryGame.Cinematics.MainMenu.Audio.MainMenu_2_AudioPump import ExecuteUbergraph_MainMenu_2_AudioPump
from Script.Engine import K2_DestroyComponent

class MainMenu_2_AudioPump(Actor):
    PumpVolumeFade_NewTrack_0_AD68D94545EE557A1846F7B664324027: float
    PumpVolumeFade__Direction_AD68D94545EE557A1846F7B664324027: uint8
    mTimerPump: TimerHandle
    
    def FunctionPump(self):
        ReturnValue: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_MainMenu_2_Pump, self, True)
    

    def PumpVolumeFade__FinishedFunc(self):
        self.ExecuteUbergraph_MainMenu_2_AudioPump(10)
    

    def PumpVolumeFade__UpdateFunc(self):
        self.ExecuteUbergraph_MainMenu_2_AudioPump(53)
    

    def ReceiveBeginPlay(self):
        self.ExecuteUbergraph_MainMenu_2_AudioPump(155)
    

    def ReceiveDestroyed(self):
        self.ExecuteUbergraph_MainMenu_2_AudioPump(295)
    

    def ExecuteUbergraph_MainMenu_2_AudioPump(self):
        # End
        # Label 15
        self.PumpVolumeFade.K2_DestroyComponent(self)
        # End
        Default__AkGameplayStatics.SetActorRTPCValue("RTPC_MainMenu_2_Pump", self.PumpVolumeFade_NewTrack_0_AD68D94545EE557A1846F7B664324027, 0, self)
        # End
        # Label 118
        self.PumpVolumeFade.PlayFromStart()
        # End
        self.PumpVolumeFade.SetComponentTickInterval(0.10000000149011612)
        ReturnValue: TimerHandle = Default__KismetSystemLibrary.K2_SetTimer(self, "FunctionPump", 0.3499999940395355, True)
        self.mTimerPump = ReturnValue
        goto('L118')
        
        Default__KismetSystemLibrary.K2_ClearAndInvalidateTimerHandle(self, Ref[self.mTimerPump])
        goto('L15')
    
