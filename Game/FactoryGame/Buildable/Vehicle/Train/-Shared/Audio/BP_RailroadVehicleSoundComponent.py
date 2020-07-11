
from codegen.ue4_stub import *

from Game.FactoryGame.Buildable.Vehicle.Train.-Shared.Audio.Play_Vehicle_Train_Brake_Squeal import Play_Vehicle_Train_Brake_Squeal
from Game.FactoryGame.Buildable.Vehicle.Train.-Shared.Audio.Rework.Play_Train_Rework_Engine_MetalGroan import Play_Train_Rework_Engine_MetalGroan
from Script.AkAudio import PostAkEvent
from Script.Engine import FClamp
from Game.FactoryGame.Buildable.Vehicle.Train.-Shared.Audio.Rework.Play_Train_Rework_Passby import Play_Train_Rework_Passby
from Game.FactoryGame.Buildable.Vehicle.Train.-Shared.Audio.Rework.Stop_Train_Rework_Engine_Brakes_02_Quick import Stop_Train_Rework_Engine_Brakes_02_Quick
from Game.FactoryGame.Buildable.Vehicle.Train.-Shared.Audio.Rework.Play_Train_Rework_StartGroan import Play_Train_Rework_StartGroan
from Game.FactoryGame.Buildable.Vehicle.Train.-Shared.Audio.Stop_Vehicle_Train_Brake_Squeal import Stop_Vehicle_Train_Brake_Squeal
from Game.FactoryGame.Buildable.Vehicle.Train.-Shared.Audio.Rework.Stop_Train_Rework_Engine_Brakes_01 import Stop_Train_Rework_Engine_Brakes_01
from Script.Engine import Default__KismetSystemLibrary
from Script.FactoryGame import GetMaxAirBrakingEffort
from Script.FactoryGame import GetTractiveForce
from Game.FactoryGame.Buildable.Vehicle.Train.-Shared.Audio.Play_Vehicle_Train_WindForce import Play_Vehicle_Train_WindForce
from Game.FactoryGame.Buildable.Vehicle.Train.-Shared.Audio.Rework.Play_Train_Rework_Engine_Brakes_01 import Play_Train_Rework_Engine_Brakes_01
from Script.Engine import GreaterEqual_FloatFloat
from Script.Engine import IsValid
from Game.FactoryGame.Buildable.Vehicle.Train.-Shared.Audio.Stop_Vehicle_Train_RailMovement import Stop_Vehicle_Train_RailMovement
from Script.FactoryGame import CmS2KmH
from Game.FactoryGame.Buildable.Vehicle.Train.-Shared.Audio.Rework.Play_Train_Rework_Engine_Idle import Play_Train_Rework_Engine_Idle
from Game.FactoryGame.Buildable.Vehicle.Train.-Shared.Audio.Rework.Play_Train_Engine import Play_Train_Engine
from Game.FactoryGame.Buildable.Vehicle.Train.-Shared.Audio.Rework.Stop_Train_Rework_Engine_MetalGroan import Stop_Train_Rework_Engine_MetalGroan
from Game.FactoryGame.Buildable.Vehicle.Train.-Shared.Audio.Rework.Stop_Train_Rework_StartGroan import Stop_Train_Rework_StartGroan
from Game.FactoryGame.Buildable.Vehicle.Train.-Shared.Audio.Stop_Vehicle_Train_WindForce import Stop_Vehicle_Train_WindForce
from Script.AkAudio import Stop
from Game.FactoryGame.Buildable.Vehicle.Train.-Shared.Audio.Rework.Stop_Train_Engine import Stop_Train_Engine
from Script.FactoryGame import GetAirBrakingForce
from Game.FactoryGame.Buildable.Vehicle.Train.-Shared.Audio.Play_Vehicle_Train_RailMovement import Play_Vehicle_Train_RailMovement
from Game.FactoryGame.Buildable.Vehicle.Train.-Shared.Audio.Stop_Vehicle_Train_Engine_Noise import Stop_Vehicle_Train_Engine_Noise
from Game.FactoryGame.Buildable.Vehicle.Train.-Shared.Audio.Rework.Stop_Train_Rework_Engine_Brakes_02 import Stop_Train_Rework_Engine_Brakes_02
from Script.FactoryGame import Default__FGBlueprintFunctionLibrary
from Game.FactoryGame.Buildable.Vehicle.Train.-Shared.Audio.Play_Vehicle_Train_Engine_Noise import Play_Vehicle_Train_Engine_Noise
from Game.FactoryGame.Buildable.Vehicle.Train.-Shared.Audio.BP_RailroadVehicleSoundComponent import ExecuteUbergraph_BP_RailroadVehicleSoundComponent
from Game.FactoryGame.Buildable.Vehicle.Train.-Shared.Audio.Rework.Stop_Train_Rework_Passby import Stop_Train_Rework_Passby
from Script.FactoryGame import FGRailroadVehicleSoundComponent
from Script.Engine import Abs
from Game.FactoryGame.Buildable.Vehicle.Train.-Shared.Audio.Rework.Stop_Train_Rework_Engine_Brakes_01_Quick import Stop_Train_Rework_Engine_Brakes_01_Quick
from Script.AkAudio import SeekOnEventBySeconds
from Script.AkAudio import SetRTPCValue
from Script.FactoryGame import GetForwardSpeed
from Game.FactoryGame.Buildable.Vehicle.Train.-Shared.Audio.Rework.Play_Train_Rework_Engine_Brakes_02 import Play_Train_Rework_Engine_Brakes_02
from Script.Engine import RandomFloatInRange

class BP_RailroadVehicleSoundComponent(FGRailroadVehicleSoundComponent):
    PrimaryComponentTick = Namespace(EndTickGroup=0, TickGroup=2, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=True, bTickEvenWhenPaused=False)
    
    def mSpeedKmH(self):
        ReturnValue: float = self.mVehicleMovementComponent.GetForwardSpeed()
        ReturnValue_0: float = Default__FGBlueprintFunctionLibrary.CmS2KmH(ReturnValue)
        ReturnValue_1: float = Abs(ReturnValue_0)
        Speed = ReturnValue_1
    

    def OnStartedMoving(self):
        self.ExecuteUbergraph_BP_RailroadVehicleSoundComponent(2601)
    

    def OnStoppedMoving(self):
        self.ExecuteUbergraph_BP_RailroadVehicleSoundComponent(3415)
    

    def UpdateRTPCs(self):
        self.ExecuteUbergraph_BP_RailroadVehicleSoundComponent(3410)
    

    def OnDynamicBrakesApplied(self):
        self.ExecuteUbergraph_BP_RailroadVehicleSoundComponent(48)
    

    def OnAirBrakesApplied(self):
        self.ExecuteUbergraph_BP_RailroadVehicleSoundComponent(827)
    

    def OnAirBrakesReleased(self):
        self.ExecuteUbergraph_BP_RailroadVehicleSoundComponent(832)
    

    def OnDynamicBrakesReleased(self):
        self.ExecuteUbergraph_BP_RailroadVehicleSoundComponent(1010)
    

    def OnThrottleReleased(self):
        self.ExecuteUbergraph_BP_RailroadVehicleSoundComponent(1966)
    

    def OnThrottleApplied(self):
        self.ExecuteUbergraph_BP_RailroadVehicleSoundComponent(1967)
    

    def OnStoppedMovingRelay(self):
        self.ExecuteUbergraph_BP_RailroadVehicleSoundComponent(2159)
    

    def StartIdleSounds(self):
        self.ExecuteUbergraph_BP_RailroadVehicleSoundComponent(3420)
    

    def StopAllSounds(self):
        self.ExecuteUbergraph_BP_RailroadVehicleSoundComponent(3480)
    

    def ExecuteUbergraph_BP_RailroadVehicleSoundComponent(self):
        goto(ComputedJump("EntryPoint"))
        # Label 15
        self.mAllVehicleCentersAkComponent.Stop()
        goto(ExecutionFlow.Pop())
        
        Speed = None
        # Label 48
        self.mSpeedKmH(Ref[Speed])
        ReturnValue2: bool = GreaterEqual_FloatFloat(Speed, 1)
        if not ReturnValue2:
           goto(ExecutionFlow.Pop())
        ExecutionFlow.Push("L391")
        ReturnValue1: bool = GreaterEqual_FloatFloat(Speed, 80)
        if not ReturnValue1:
            goto('L663')
        ReturnValue2_0: int32 = self.mWheelsetsAkComponent.PostAkEvent(Play_Train_Rework_Engine_MetalGroan)
        ReturnValue: int32 = self.mWheelsetsAkComponent.PostAkEvent(Play_Train_Rework_Engine_Brakes_01)
        ReturnValue2_1: float = RandomFloatInRange(0, 3)
        ReturnValue2_2: bool = self.mWheelsetsAkComponent.SeekOnEventBySeconds(Play_Train_Rework_Engine_Brakes_01, ReturnValue2_1, False, 0)
        goto(ExecutionFlow.Pop())
        # Label 391
        ReturnValue_0: bool = GreaterEqual_FloatFloat(Speed, 60)
        if not ReturnValue_0:
            goto('L603')
        ReturnValue9: int32 = self.mWheelsetsAkComponent.PostAkEvent(Play_Train_Rework_Engine_Brakes_01)
        ReturnValue_1: float = RandomFloatInRange(2, 6)
        ReturnValue_2: bool = self.mWheelsetsAkComponent.SeekOnEventBySeconds(Play_Train_Rework_Engine_Brakes_01, ReturnValue_1, False, 0)
        goto(ExecutionFlow.Pop())
        # Label 603
        ReturnValue8: int32 = self.mWheelsetsAkComponent.PostAkEvent(Play_Train_Rework_Engine_Brakes_02)
        goto(ExecutionFlow.Pop())
        # Label 663
        ReturnValue1_0: int32 = self.mWheelsetsAkComponent.PostAkEvent(Play_Train_Rework_Engine_MetalGroan)
        ReturnValue1_1: float = RandomFloatInRange(1, 4)
        ReturnValue1_2: bool = self.mWheelsetsAkComponent.SeekOnEventBySeconds(Play_Train_Rework_Engine_MetalGroan, ReturnValue1_1, False, 0)
        goto(ExecutionFlow.Pop())
        goto('L48')
        # Label 832
        ReturnValue12: int32 = self.mWheelsetsAkComponent.PostAkEvent(Stop_Train_Rework_Engine_MetalGroan)
        ReturnValue11: int32 = self.mWheelsetsAkComponent.PostAkEvent(Stop_Train_Rework_Engine_Brakes_01_Quick)
        ReturnValue10: int32 = self.mWheelsetsAkComponent.PostAkEvent(Stop_Train_Rework_Engine_Brakes_02_Quick)
        goto(ExecutionFlow.Pop())
        goto('L832')
        # Label 1015
        ReturnValue3: int32 = self.mEnginesAkComponent.PostAkEvent(Stop_Vehicle_Train_Engine_Noise)
        ReturnValue13: int32 = self.mAllVehicleCentersAkComponent.PostAkEvent(Stop_Train_Rework_StartGroan)
        goto(ExecutionFlow.Pop())
        # Label 1134
        ReturnValue4: int32 = self.mWheelsetsAkComponent.PostAkEvent(Stop_Train_Rework_Engine_Brakes_02)
        goto(ExecutionFlow.Pop())
        # Label 1194
        ReturnValue1_3: float = self.mVehicleMovementComponent.GetMaxAirBrakingEffort()
        ReturnValue1_4: float = self.mVehicleMovementComponent.GetAirBrakingForce()
        ReturnValue1_5: float = ReturnValue1_4 / ReturnValue1_3
        ReturnValue3_0: bool = GreaterEqual_FloatFloat(ReturnValue1_5, 1)
        if not ReturnValue3_0:
            goto('L1388')
        # Label 1388
        ReturnValue1_6: float = self.mVehicleMovementComponent.GetForwardSpeed()
        ReturnValue1_7: float = Default__FGBlueprintFunctionLibrary.CmS2KmH(ReturnValue1_6)
        ReturnValue1_8: float = Abs(ReturnValue1_7)
        ReturnValue2_3: float = ReturnValue1_8 / 100
        ReturnValue_3: float = self.mLocomotiveMovementComponent.GetTractiveForce()
        ReturnValue3_1: float = ReturnValue_3 / 1000000
        ReturnValue_4: float = FClamp(ReturnValue3_1, 10, 200)
        ReturnValue_5: float = ReturnValue_4 * ReturnValue2_3
        self.mEnginesAkComponent.SetRTPCValue("RTPC_V_Train_Tracktive_Force", ReturnValue_5, 0)
        goto(ExecutionFlow.Pop())
        # Label 1838
        ReturnValue5: int32 = self.mWheelsetsAkComponent.PostAkEvent(Stop_Train_Rework_Engine_Brakes_01)
        goto('L1134')
        # Label 1902
        ReturnValue6: int32 = self.mWheelsetsAkComponent.PostAkEvent(Stop_Train_Rework_Engine_MetalGroan)
        goto('L1838')
        goto(ExecutionFlow.Pop())
        goto(ExecutionFlow.Pop())
        
        Speed1 = None
        # Label 1968
        self.mSpeedKmH(Ref[Speed1])
        ReturnValue_6: bool = Speed1 <= 1
        if not ReturnValue_6:
           goto(ExecutionFlow.Pop())
        ReturnValue14: int32 = self.mAllVehicleCentersAkComponent.PostAkEvent(Play_Train_Rework_StartGroan)
        goto(ExecutionFlow.Pop())
        # Label 2095
        ReturnValue7: int32 = self.mEnginesAkComponent.PostAkEvent(Play_Vehicle_Train_Engine_Noise)
        goto('L1968')
        goto('L1902')
        # Label 2164
        self.OnStoppedMovingRelay()
        ReturnValue22: int32 = self.mWheelsetsAkComponent.PostAkEvent(Stop_Vehicle_Train_RailMovement)
        ReturnValue17: int32 = self.mWheelsetsAkComponent.PostAkEvent(Stop_Train_Rework_Passby)
        ReturnValue20: int32 = self.mWheelsetsAkComponent.PostAkEvent(Stop_Vehicle_Train_Brake_Squeal)
        ReturnValue15: int32 = self.mEnginesAkComponent.PostAkEvent(Stop_Vehicle_Train_WindForce)
        ReturnValue19: int32 = self.mEnginesAkComponent.PostAkEvent(Stop_Train_Engine)
        goto('L1015')
        # Label 2478
        ReturnValue16: int32 = self.mEnginesAkComponent.PostAkEvent(Play_Vehicle_Train_WindForce)
        ReturnValue23: int32 = self.mEnginesAkComponent.PostAkEvent(Play_Train_Engine)
        goto('L2095')
        ReturnValue24: int32 = self.mWheelsetsAkComponent.PostAkEvent(Play_Vehicle_Train_RailMovement)
        ReturnValue18: int32 = self.mWheelsetsAkComponent.PostAkEvent(Play_Train_Rework_Passby)
        ReturnValue21: int32 = self.mWheelsetsAkComponent.PostAkEvent(Play_Vehicle_Train_Brake_Squeal)
        goto('L2478')
        # Label 2783
        ReturnValue_7: bool = Default__KismetSystemLibrary.IsValid(self.mLocomotiveMovementComponent)
        if not ReturnValue_7:
           goto(ExecutionFlow.Pop())
        ReturnValue_8: float = self.mVehicleMovementComponent.GetForwardSpeed()
        ReturnValue_9: float = Default__FGBlueprintFunctionLibrary.CmS2KmH(ReturnValue_8)
        ReturnValue_10: float = Abs(ReturnValue_9)
        self.mWheelsetsAkComponent.SetRTPCValue("RTPC_V_Train_Speed", ReturnValue_10, 0)
        self.mEnginesAkComponent.SetRTPCValue("RTPC_V_Train_Speed", ReturnValue_10, 0)
        self.mAllVehicleCentersAkComponent.SetRTPCValue("RTPC_V_Train_Speed", ReturnValue_10, 0)
        ReturnValue_11: float = self.mVehicleMovementComponent.GetMaxAirBrakingEffort()
        ReturnValue_12: float = self.mVehicleMovementComponent.GetAirBrakingForce()
        ReturnValue_13: float = ReturnValue_12 / ReturnValue_11
        self.mWheelsetsAkComponent.SetRTPCValue("RTPC_V_Train_BrakeForce", ReturnValue_13, 0)
        goto('L1194')
        goto('L2783')
        goto('L2164')
        ReturnValue25: int32 = self.mEnginesAkComponent.PostAkEvent(Play_Train_Rework_Engine_Idle)
        goto(ExecutionFlow.Pop())
        self.mWheelsetsAkComponent.Stop()
        self.mEnginesAkComponent.Stop()
        goto('L15')
    
