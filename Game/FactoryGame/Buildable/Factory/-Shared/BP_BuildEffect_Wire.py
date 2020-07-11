
from codegen.ue4_stub import *

from Script.AkAudio import PostAkEvent
from Script.Engine import Delay
from Script.Engine import PlayFromStart
from Script.Engine import SpawnEmitterAtLocation
from Script.CoreUObject import Rotator
from Game.FactoryGame.Buildable.Factory.PowerLine.Particle.PowerlineSparks_01 import PowerlineSparks_01
from Script.FactoryGame import FGCircuitConnectionComponent
from Script.Engine import LatentActionInfo
from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import ETimelineDirection
from Script.FactoryGame import GetConnection
from Script.Engine import IsValid
from Game.FactoryGame.Buildable.Factory.-Shared.BP_BuildEffect_Wire import ExecuteUbergraph_BP_BuildEffect_Wire
from Script.FactoryGame import FGBuildableWire
from Game.FactoryGame.Buildable.-Shared.Audio.Play_F_PowerConnection import Play_F_PowerConnection
from Script.Engine import Default__GameplayStatics
from Script.Engine import SetVectorParameterValueOnMaterials
from Script.Engine import Subtract_VectorVector
from Script.CoreUObject import Vector
from Script.Engine import K2_GetComponentLocation
from Script.AkAudio import Default__AkGameplayStatics
from Script.Engine import Actor
from Script.Engine import ParticleSystemComponent
from Script.Engine import MakeRotFromX
from Script.Engine import GetOwner
from Script.AkAudio import AkComponent

class BP_BuildEffect_Wire(Actor):
    Timeline_0_NewTrack_0_C21AB6204CE0D2E20CFA12B09E73FB8B: Vector
    Timeline_0__Direction_C21AB6204CE0D2E20CFA12B09E73FB8B: uint8
    
    def Timeline_0__FinishedFunc(self):
        self.ExecuteUbergraph_BP_BuildEffect_Wire(1103)
    

    def Timeline_0__UpdateFunc(self):
        self.ExecuteUbergraph_BP_BuildEffect_Wire(15)
    

    def ReceiveBeginPlay(self):
        self.ExecuteUbergraph_BP_BuildEffect_Wire(1098)
    

    def ExecuteUbergraph_BP_BuildEffect_Wire(self):
        goto(ComputedJump("EntryPoint"))
        ReturnValue: Ptr[Actor] = self.GetOwner()
        Wire: Ptr[FGBuildableWire] = Cast[FGBuildableWire](ReturnValue)
        bSuccess: bool = Wire
        Wire.mWireMesh.SetVectorParameterValueOnMaterials("Disp_Direction", self.Timeline_0_NewTrack_0_C21AB6204CE0D2E20CFA12B09E73FB8B)
        goto(ExecutionFlow.Pop())
        # Label 177
        ReturnValue2: Ptr[Actor] = self.GetOwner()
        Wire1: Ptr[FGBuildableWire] = Cast[FGBuildableWire](ReturnValue2)
        bSuccess1: bool = Wire1
        ReturnValue2_0: Ptr[FGCircuitConnectionComponent] = Wire1.GetConnection(1)
        ReturnValue_0: bool = Default__KismetSystemLibrary.IsValid(ReturnValue2_0)
        if not ReturnValue_0:
            goto('L1021')
        ReturnValue1: Ptr[Actor] = self.GetOwner()
        ReturnValue_1: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_F_PowerConnection, ReturnValue1, True)
        ReturnValue = self.GetOwner()
        Wire = Cast[FGBuildableWire](ReturnValue)
        bSuccess = Wire
        ReturnValue1_0: Ptr[FGCircuitConnectionComponent] = Wire.GetConnection(0)
        ReturnValue = self.GetOwner()
        Wire = Cast[FGBuildableWire](ReturnValue)
        bSuccess = Wire
        ReturnValue_2: Ptr[FGCircuitConnectionComponent] = Wire.GetConnection(1)
        ReturnValue_3: Vector = ReturnValue_2.K2_GetComponentLocation()
        ReturnValue1_1: Vector = ReturnValue1_0.K2_GetComponentLocation()
        ReturnValue_4: Vector = Subtract_VectorVector(ReturnValue1_1, ReturnValue_3)
        
        ReturnValue_5: Rotator = MakeRotFromX(Ref[ReturnValue_4])
        ReturnValue_6: Ptr[ParticleSystemComponent] = Default__GameplayStatics.SpawnEmitterAtLocation(self, PowerlineSparks_01, ReturnValue_3, ReturnValue_5, Vector(1, 1, 1), True, 0)
        self.Timeline_0.PlayFromStart()
        goto(ExecutionFlow.Pop())
        # Label 1021
        Default__KismetSystemLibrary.Delay(self, 0.20000000298023224, LatentActionInfo(Linkage = 177, UUID = 1586607350, ExecutionFunction = "ExecuteUbergraph_BP_BuildEffect_Wire", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        goto('L177')
        goto(ExecutionFlow.Pop())
    
