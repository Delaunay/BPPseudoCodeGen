
from codegen.ue4_stub import *

from Game.FactoryGame.Character.Creature.Enemy.Stinger.Particle.StingerGas_01 import StingerGas_01
from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import ETimelineDirection
from Script.Engine import Default__GameplayStatics
from Script.Engine import K2_GetActorLocation
from Script.Engine import Actor
from Script.Engine import K2_AddActorWorldOffset
from Script.Engine import Delay
from Script.Engine import PlayFromStart
from Script.CoreUObject import Vector
from Script.Engine import Conv_FloatToVector
from Script.Engine import SpawnEmitterAtLocation
from Script.Engine import GetWorldDeltaSeconds
from Script.Engine import K2_AddWorldOffset
from Script.Engine import SetWorldScale3D
from Game.FactoryGame.Character.Creature.Enemy.Stinger.BigStinger.BP_StingerGas import ExecuteUbergraph_BP_StingerGas
from Script.Engine import LatentActionInfo
from Script.Engine import K2_DestroyComponent

class BP_StingerGas(Actor):
    Timeline_1_NewTrack_0_21A6CF6E4A8791016A73379F30BF737A: float
    Timeline_1__Direction_21A6CF6E4A8791016A73379F30BF737A: uint8
    Timeline_0_NewTrack_0_3359A77142CE01FC3766F29C0D8F5F9D: float
    Timeline_0__Direction_3359A77142CE01FC3766F29C0D8F5F9D: uint8
    
    def Timeline_1__FinishedFunc(self):
        self.ExecuteUbergraph_BP_StingerGas(15)
    

    def Timeline_1__UpdateFunc(self):
        self.ExecuteUbergraph_BP_StingerGas(380)
    

    def Timeline_0__FinishedFunc(self):
        self.ExecuteUbergraph_BP_StingerGas(370)
    

    def Timeline_0__UpdateFunc(self):
        self.ExecuteUbergraph_BP_StingerGas(291)
    

    def ReceiveBeginPlay(self):
        self.ExecuteUbergraph_BP_StingerGas(375)
    

    def ExecuteUbergraph_BP_StingerGas(self):
        goto(ComputedJump("EntryPoint"))
        ReturnValue.K2_DestroyComponent(self)
        self.K2_DestroyActor()
        goto(ExecutionFlow.Pop())
        self.Timeline_1.PlayFromStart()
        goto(ExecutionFlow.Pop())
        # Label 96
        ReturnValue: Vector = self.K2_GetActorLocation()
        ReturnValue = Default__GameplayStatics.SpawnEmitterAtLocation(self, StingerGas_01, ReturnValue, Rotator::FromPitchYawRoll(0, 0, 0), Vector(1.2000000476837158, 1.2000000476837158, 1.2000000476837158), True, 0)
        # Label 214
        Default__KismetSystemLibrary.Delay(self, 25, LatentActionInfo(Linkage = 63, UUID = 118518804, ExecutionFunction = "ExecuteUbergraph_BP_StingerGas", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        ReturnValue_0: Vector = Conv_FloatToVector(self.Timeline_0_NewTrack_0_3359A77142CE01FC3766F29C0D8F5F9D)
        ReturnValue.SetWorldScale3D(ReturnValue_0)
        goto(ExecutionFlow.Pop())
        goto('L214')
        goto('L96')
        ReturnValue_1: float = Default__GameplayStatics.GetWorldDeltaSeconds(self)
        ReturnValue_2: float = self.Timeline_1_NewTrack_0_21A6CF6E4A8791016A73379F30BF737A * ReturnValue_1
        ReturnValue1: float = ReturnValue_2 * 30
        ReturnValue1_0: Vector = Vector(0, 0, ReturnValue1)
        
        SweepHitResult = None
        self.K2_AddActorWorldOffset(ReturnValue1_0, False, False, Ref[SweepHitResult])
        ReturnValue_1 = Default__GameplayStatics.GetWorldDeltaSeconds(self)
        ReturnValue_2 = self.Timeline_1_NewTrack_0_21A6CF6E4A8791016A73379F30BF737A * ReturnValue_1
        ReturnValue1 = ReturnValue_2 * 30
        ReturnValue_3: Vector = Vector(0, 0, ReturnValue1)
        
        SweepHitResult = None
        ReturnValue.K2_AddWorldOffset(ReturnValue_3, False, False, Ref[SweepHitResult])
        goto(ExecutionFlow.Pop())
    
