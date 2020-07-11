
from codegen.ue4_stub import *

from Script.Engine import Actor
from Script.AkAudio import PostAkEvent
from Game.FactoryGame.Buildable.-Shared.Audio.Play_BuildEffect_WaterPump_Thump import Play_BuildEffect_WaterPump_Thump
from Script.Engine import GetOwner
from Game.FactoryGame.Buildable.Factory.-Shared.BP_MaterialEffect_Build import BP_MaterialEffect_Build
from Script.AkAudio import AkComponent
from Game.FactoryGame.Buildable.Factory.WaterPump.MaterialEffect_WaterPump import ExecuteUbergraph_MaterialEffect_WaterPump
from Script.AkAudio import Default__AkGameplayStatics

class MaterialEffect_WaterPump(BP_MaterialEffect_Build):
    mAutoDestroy = True
    PrimaryComponentTick = Namespace(EndTickGroup=0, TickGroup=2, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=False, bTickEvenWhenPaused=False)
    bAutoActivate = True
    
    def PlayThumpSound(self):
        self.ExecuteUbergraph_MaterialEffect_WaterPump(96)
    

    def ExecuteUbergraph_MaterialEffect_WaterPump(self):
        # Label 10
        ReturnValue: Ptr[Actor] = self.GetOwner()
        ReturnValue_0: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_BuildEffect_WaterPump_Thump, ReturnValue, True)
        # End
        goto('L10')
    
