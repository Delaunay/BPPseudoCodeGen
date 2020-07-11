
from codegen.ue4_stub import *

from Script.AkAudio import PostAkEvent
from Game.FactoryGame.Equipment.JetPack.Audio.Play_EQ_JetPack_Activate import Play_EQ_JetPack_Activate
from Game.FactoryGame.Equipment.JetPack.Audio.Play_EQ_JetPack_Deactivate import Play_EQ_JetPack_Deactivate
from Script.FactoryGame import FGJetPackAttachment
from Script.AkAudio import AkComponent
from Script.AkAudio import Default__AkGameplayStatics
from Script.Engine import ReceiveBeginPlay
from Game.FactoryGame.Equipment.JetPack.Attach_JetPackMk2 import ExecuteUbergraph_Attach_JetPackMk2

class Attach_JetPackMk2(FGJetPackAttachment):
    mAttachSocket = spineSocket
    PrimaryActorTick = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=False, bTickEvenWhenPaused=False)
    bNetUseOwnerRelevancy = True
    bReplicates = True
    RemoteRole = 1
    
    def OnStopThrusting(self):
        self.ExecuteUbergraph_Attach_JetPackMk2(68)
    

    def OnStartThrusting(self):
        self.ExecuteUbergraph_Attach_JetPackMk2(823)
    

    def ReceiveBeginPlay(self):
        self.ExecuteUbergraph_Attach_JetPackMk2(1631)
    

    def ExecuteUbergraph_Attach_JetPackMk2(self):
        # Label 10
        ReturnValue: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_EQ_JetPack_Deactivate, self, True)
        # End
        self.JetpackExhaust.SetEmitterEnable("Thrust_L", False)
        self.JetpackExhaust1.SetEmitterEnable("Thrust_L", False)
        self.JetpackExhaust2.SetEmitterEnable("Thrust_L", False)
        self.JetpackExhaust.SetEmitterEnable("Lights_Thrust", False)
        self.JetpackExhaust1.SetEmitterEnable("Lights_Thrust", False)
        self.JetpackExhaust2.SetEmitterEnable("Lights_Thrust", False)
        self.JetpackExhaust.SetEmitterEnable("LongThrust_L", False)
        self.JetpackExhaust1.SetEmitterEnable("LongThrust_L", False)
        self.JetpackExhaust2.SetEmitterEnable("LongThrust_L", False)
        self.JetpackExhaust.SetEmitterEnable("Sparks_L", False)
        self.JetpackExhaust1.SetEmitterEnable("Sparks_L", False)
        self.JetpackExhaust2.SetEmitterEnable("Sparks_L", False)
        self.JetpackExhaust.SetEmitterEnable("Smoke_L", False)
        self.JetpackExhaust1.SetEmitterEnable("Smoke_L", False)
        self.JetpackExhaust2.SetEmitterEnable("Smoke_L", False)
        goto('L10')
        self.JetpackExhaust.SetEmitterEnable("Thrust_L", True)
        self.JetpackExhaust1.SetEmitterEnable("Thrust_L", True)
        self.JetpackExhaust2.SetEmitterEnable("Thrust_L", True)
        self.JetpackExhaust.SetEmitterEnable("Lights_Thrust", True)
        self.JetpackExhaust1.SetEmitterEnable("Lights_Thrust", True)
        self.JetpackExhaust2.SetEmitterEnable("Lights_Thrust", True)
        self.JetpackExhaust.SetEmitterEnable("LongThrust_L", True)
        self.JetpackExhaust1.SetEmitterEnable("LongThrust_L", True)
        self.JetpackExhaust2.SetEmitterEnable("LongThrust_L", True)
        self.JetpackExhaust.SetEmitterEnable("Sparks_L", True)
        self.JetpackExhaust1.SetEmitterEnable("Sparks_L", True)
        self.JetpackExhaust2.SetEmitterEnable("Sparks_L", True)
        self.JetpackExhaust.SetEmitterEnable("Smoke_L", True)
        self.JetpackExhaust1.SetEmitterEnable("Smoke_L", True)
        self.JetpackExhaust2.SetEmitterEnable("Smoke_L", True)
        ReturnValue1: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_EQ_JetPack_Activate, self, True)
        # End
        self.ReceiveBeginPlay()
        self.JetpackExhaust.SetEmitterEnable("Thrust_L", False)
        self.JetpackExhaust1.SetEmitterEnable("Thrust_L", False)
        self.JetpackExhaust2.SetEmitterEnable("Thrust_L", False)
        self.JetpackExhaust.SetEmitterEnable("Lights_Thrust", False)
        self.JetpackExhaust1.SetEmitterEnable("Lights_Thrust", False)
        self.JetpackExhaust2.SetEmitterEnable("Lights_Thrust", False)
        self.JetpackExhaust.SetEmitterEnable("LongThrust_L", False)
        self.JetpackExhaust1.SetEmitterEnable("LongThrust_L", False)
        self.JetpackExhaust2.SetEmitterEnable("LongThrust_L", False)
        self.JetpackExhaust.SetEmitterEnable("Sparks_L", False)
        self.JetpackExhaust1.SetEmitterEnable("Sparks_L", False)
        self.JetpackExhaust2.SetEmitterEnable("Sparks_L", False)
        self.JetpackExhaust.SetEmitterEnable("Smoke_L", False)
        self.JetpackExhaust1.SetEmitterEnable("Smoke_L", False)
        self.JetpackExhaust2.SetEmitterEnable("Smoke_L", False)
    
