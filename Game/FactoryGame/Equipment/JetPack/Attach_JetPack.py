
from codegen.ue4_stub import *

from Script.AkAudio import PostAkEvent
from Game.FactoryGame.Equipment.JetPack.Audio.Play_EQ_JetPack_Activate import Play_EQ_JetPack_Activate
from Game.FactoryGame.Equipment.JetPack.Audio.Play_EQ_JetPack_Deactivate import Play_EQ_JetPack_Deactivate
from Script.FactoryGame import FGJetPackAttachment
from Script.AkAudio import AkComponent
from Game.FactoryGame.Equipment.JetPack.Attach_JetPack import ExecuteUbergraph_Attach_JetPack
from Script.AkAudio import Default__AkGameplayStatics
from Script.Engine import ReceiveBeginPlay

class Attach_JetPack(FGJetPackAttachment):
    mAttachSocket = backpack
    PrimaryActorTick = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=False, bTickEvenWhenPaused=False)
    bNetUseOwnerRelevancy = True
    bReplicates = True
    RemoteRole = 1
    
    def OnStopThrusting(self):
        self.ExecuteUbergraph_Attach_JetPack(2126)
    

    def OnStartThrusting(self):
        self.ExecuteUbergraph_Attach_JetPack(1371)
    

    def ReceiveBeginPlay(self):
        self.ExecuteUbergraph_Attach_JetPack(591)
    

    def ExecuteUbergraph_Attach_JetPack(self):
        # Label 10
        ReturnValue: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_EQ_JetPack_Deactivate, self, True)
        # End
        # Label 68
        ReturnValue1: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_EQ_JetPack_Activate, self, True)
        # End
        # Label 126
        self.ReceiveBeginPlay()
        self.JetpackExhaust.SetEmitterEnable("MeshLong", False)
        self.JetpackExhaust2.SetEmitterEnable("MeshLong", False)
        self.JetpackExhaust1.SetEmitterEnable("MeshLong", False)
        self.JetpackExhaust.SetEmitterEnable("LongThrust_L", False)
        self.JetpackExhaust2.SetEmitterEnable("LongThrust_L", False)
        self.JetpackExhaust1.SetEmitterEnable("LongThrust_L", False)
        self.JetpackExhaust.SetEmitterEnable("StreaksLong", False)
        self.JetpackExhaust2.SetEmitterEnable("StreaksLong", False)
        self.JetpackExhaust1.SetEmitterEnable("StreaksLong", False)
        # End
        goto('L126')
        # Label 596
        self.JetpackExhaust.SetEmitterEnable("StreaksShort", True)
        self.JetpackExhaust1.SetEmitterEnable("StreaksShort", True)
        self.JetpackExhaust2.SetEmitterEnable("StreaksShort", True)
        goto('L10')
        # Label 751
        self.JetpackExhaust.SetEmitterEnable("StreaksLong", False)
        self.JetpackExhaust1.SetEmitterEnable("StreaksLong", False)
        self.JetpackExhaust2.SetEmitterEnable("StreaksLong", False)
        goto('L596')
        # Label 906
        self.JetpackExhaust2.SetEmitterEnable("LongThrust_L", False)
        self.JetpackExhaust.SetEmitterEnable("LongThrust_L", False)
        self.JetpackExhaust1.SetEmitterEnable("LongThrust_L", False)
        goto('L751')
        # Label 1061
        self.JetpackExhaust2.SetEmitterEnable("MeshShort", True)
        self.JetpackExhaust.SetEmitterEnable("MeshShort", True)
        self.JetpackExhaust1.SetEmitterEnable("MeshShort", True)
        goto('L906')
        # Label 1216
        self.JetpackExhaust.SetEmitterEnable("MeshLong", False)
        self.JetpackExhaust1.SetEmitterEnable("MeshLong", False)
        self.JetpackExhaust2.SetEmitterEnable("MeshLong", False)
        goto('L1061')
        self.JetpackExhaust.SetEmitterEnable("MeshShort", False)
        self.JetpackExhaust1.SetEmitterEnable("MeshShort", False)
        self.JetpackExhaust2.SetEmitterEnable("MeshShort", False)
        self.JetpackExhaust.SetEmitterEnable("MeshLong", True)
        self.JetpackExhaust1.SetEmitterEnable("MeshLong", True)
        self.JetpackExhaust2.SetEmitterEnable("MeshLong", True)
        self.JetpackExhaust.SetEmitterEnable("LongThrust_L", True)
        self.JetpackExhaust1.SetEmitterEnable("LongThrust_L", True)
        self.JetpackExhaust2.SetEmitterEnable("LongThrust_L", True)
        self.JetpackExhaust.SetEmitterEnable("StreaksLong", True)
        self.JetpackExhaust1.SetEmitterEnable("StreaksLong", True)
        self.JetpackExhaust2.SetEmitterEnable("StreaksLong", True)
        self.JetpackExhaust.SetEmitterEnable("StreaksShort", False)
        self.JetpackExhaust1.SetEmitterEnable("StreaksShort", False)
        self.JetpackExhaust2.SetEmitterEnable("StreaksShort", False)
        goto('L68')
        goto('L1216')
    
