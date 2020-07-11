
from codegen.ue4_stub import *

from Script.Engine import Default__KismetSystemLibrary
from Script.UMG import GetOwningPlayerPawn
from Script.Engine import RandomIntegerInRange
from Game.FactoryGame.Interface.UI.InGame.CursorParticles.BP_CursorParticle import BP_CursorParticle
from Script.AkAudio import PostAkEvent
from Script.UMG import SetRenderScale
from Script.UMG import UMGSequencePlayer
from Script.UMG import PlayAnimation
from Script.Engine import Delay
from Script.CoreUObject import Vector2D
from Script.Engine import Pawn
from Game.FactoryGame.Interface.UI.InGame.CursorParticles.CursorParticle_Metal import ExecuteUbergraph_CursorParticle_Metal
from Game.FactoryGame.Interface.UI.Audio.CursorParticles.Play_UI_CursorParticle_Metal import Play_UI_CursorParticle_Metal
from Script.AkAudio import AkComponent
from Script.UMG import WidgetAnimation
from Script.AkAudio import Default__AkGameplayStatics
from Script.Engine import LatentActionInfo
from Script.Engine import RandomFloatInRange

class CursorParticle_Metal(BP_CursorParticle):
    FadeAnim: Ptr[WidgetAnimation]
    
    def Construct(self):
        self.ExecuteUbergraph_CursorParticle_Metal(30)
    

    def ExecuteUbergraph_CursorParticle_Metal(self):
        goto(ComputedJump("EntryPoint"))
        self.RemoveFromParent()
        goto(ExecutionFlow.Pop())
        ReturnValue: int32 = RandomIntegerInRange(3, 5)
        self.Widget_SparkParticles.CreateSparks(ReturnValue)
        ReturnValue_0: float = RandomFloatInRange(0.800000011920929, 1.2000000476837158)
        ReturnValue1: float = RandomFloatInRange(0.800000011920929, 1.2000000476837158)
        ReturnValue_1: Vector2D = Vector2D(ReturnValue1, ReturnValue_0)
        self.mScaler.SetRenderScale(ReturnValue_1)
        ReturnValue_2: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.FadeAnim, 0, 1, 0, 1)
        ReturnValue_3: Ptr[Pawn] = self.GetOwningPlayerPawn()
        ReturnValue_4: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_UI_CursorParticle_Metal, ReturnValue_3, False)
        Default__KismetSystemLibrary.Delay(self, 3, LatentActionInfo(Linkage = 15, UUID = -2040743904, ExecutionFunction = "ExecuteUbergraph_CursorParticle_Metal", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
    
