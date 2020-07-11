
from codegen.ue4_stub import *

from Script.Engine import MakeTransform
from Script.Engine import Actor
from Script.Engine import Default__GameplayStatics
from Game.WeatherOverhaul.RainSpawnerActor import RainSpawnerActor
from Script.Engine import FinishSpawningActor
from Game.WeatherOverhaul.InitMod import ExecuteUbergraph_InitMod
from Script.Engine import BeginDeferredActorSpawnFromClass
from Script.SML import SMLInitMod
from Script.CoreUObject import Transform

class InitMod(SMLInitMod):
    mChatCommands = ['/Game/WeatherOverhaul/ChatCommandKillAll.ChatCommandKillAll_C']
    
    def PostInit(self):
        self.ExecuteUbergraph_InitMod(273)
    

    def ExecuteUbergraph_InitMod(self):
        # Label 10
        ReturnValue: Transform = MakeTransform(Vector(0, 0, 0), Rotator::FromPitchYawRoll(0, 0, 0), Vector(1, 1, 1))
        
        ReturnValue_0: Ptr[Actor] = Default__GameplayStatics.BeginDeferredActorSpawnFromClass(self, RainSpawnerActor, 1, None, Ref[ReturnValue])
        ReturnValue = MakeTransform(Vector(0, 0, 0), Rotator::FromPitchYawRoll(0, 0, 0), Vector(1, 1, 1))
        
        ReturnValue_1: Ptr[RainSpawnerActor] = Default__GameplayStatics.FinishSpawningActor(ReturnValue_0, Ref[ReturnValue])
        # End
        goto('L10')
    
