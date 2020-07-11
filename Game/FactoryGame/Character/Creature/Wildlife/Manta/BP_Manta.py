
from codegen.ue4_stub import *

from Script.FactoryGame import LostSignificance
from Game.FactoryGame.Character.Creature.Wildlife.Manta.Audio.Stop_W_Manta_Body import Stop_W_Manta_Body
from Game.FactoryGame.Character.Creature.Wildlife.Manta.Audio.Play_W_Manta_Call import Play_W_Manta_Call
from Game.FactoryGame.Character.Creature.Wildlife.Manta.Audio.Play_W_Manta_Body import Play_W_Manta_Body
from Script.AkAudio import AkComponent
from Script.FactoryGame import GainedSignificance
from Game.FactoryGame.Character.Creature.Wildlife.Manta.Audio.Stop_W_Manta_Call import Stop_W_Manta_Call
from Script.AkAudio import Default__AkGameplayStatics
from Script.FactoryGame import FGManta
from Script.AkAudio import PostAkEventAttached
from Game.FactoryGame.Character.Creature.Wildlife.Manta.BP_Manta import ExecuteUbergraph_BP_Manta

class BP_Manta(FGManta):
    mSecondsPerLoop = 30
    mSignificanceRange = 130000
    mTickTransform = True
    mIsClosedSplineLoop = True
    PrimaryActorTick = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=True, bTickEvenWhenPaused=False)
    bReplicates = True
    RootComponent = Namespace(ObjectClass='/Script/Engine.SceneComponent', ObjectFlags=2883617, ObjectName='RootComponent')
    
    def GainedSignificance(self):
        self.ExecuteUbergraph_BP_Manta(10)
    

    def LostSignificance(self):
        self.ExecuteUbergraph_BP_Manta(173)
    

    def ExecuteUbergraph_BP_Manta(self):
        self.GainedSignificance()
        ReturnValue1: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEventAttached(Play_W_Manta_Call, self.Manta_01, "head", True)
        ReturnValue: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEventAttached(Play_W_Manta_Body, self.Manta_01, "Root", True)
        # End
        self.LostSignificance()
        ReturnValue2: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEventAttached(Stop_W_Manta_Call, self.Manta_01, "head", True)
        ReturnValue3: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEventAttached(Stop_W_Manta_Body, self.Manta_01, "Root", True)
    
