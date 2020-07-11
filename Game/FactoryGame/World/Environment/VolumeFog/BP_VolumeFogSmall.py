
from codegen.ue4_stub import *

from Script.Engine import CurveFloat
from Script.FactoryGame import FGTimeOfDaySubsystem
from Script.FactoryGame import Get
from Script.Engine import Actor
from Script.Engine import ReceiveTick
from Script.FactoryGame import Default__FGTimeOfDaySubsystem
from Script.Engine import Lerp
from Script.CoreUObject import Vector
from Script.Engine import SetScalarParameterValueOnMaterials
from Game.FactoryGame.World.Environment.VolumeFog.BP_VolumeFogSmall import ExecuteUbergraph_BP_VolumeFogSmall
from Game.FactoryGame.World.Environment.VolumeFog.BP_VolumeFogSmall import ExecuteUbergraph_BP_VolumeFogSmall.K2Node_Event_DeltaSeconds
from Script.Engine import Conv_IntToFloat
from Script.Engine import ReceiveBeginPlay
from Script.Engine import GetFloatValue
from Script.FactoryGame import GetDayMinutes
from Game.FactoryGame.World.Environment.VolumeFog.BP_VolumeFogSmall import ExecuteUbergraph_BP_VolumeFogSmall.K2Node_Event_EndPlayReason

class BP_VolumeFogSmall(Actor):
    mBrightness: float = 65
    mAppear_Distance: float = 65000
    mFade_Transition: float = 17909
    mMountainFade: float = 5000
    mSize_X: float = 25
    mSize_Y: float = 25
    mBrightnessCurve: Ptr[CurveFloat] = Namespace(AssetPath='/Game/FactoryGame/World/Environment/VolumeFog/BrightnessCurve.BrightnessCurve')
    Debug_Duration: float = 0.009999999776482582
    PrimaryActorTick = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0.05000000074505806, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=True, bTickEvenWhenPaused=False)
    
    def UpdateBrightness(self):
        ReturnValue: Ptr[FGTimeOfDaySubsystem] = Default__FGTimeOfDaySubsystem.Get(self)
        ReturnValue_0: int32 = ReturnValue.GetDayMinutes()
        ReturnValue_1: float = Conv_IntToFloat(ReturnValue_0)
        ReturnValue_2: float = self.mBrightnessCurve.GetFloatValue(ReturnValue_1)
        ReturnValue_3: float = Lerp(7, self.mBrightness, ReturnValue_2)
        self.StaticMesh.SetScalarParameterValueOnMaterials("Brightness", ReturnValue_3)
    

    def UserConstructionScript(self):
        ReturnValue: Vector = Vector(self.mSize_X, self.mSize_Y, 1)
        self.StaticMesh.SetRelativeScale3D(ReturnValue)
        self.StaticMesh.SetScalarParameterValueOnMaterials("Brightness", self.mBrightness)
        self.StaticMesh.SetScalarParameterValueOnMaterials("AppearDistance", self.mAppear_Distance)
        self.StaticMesh.SetScalarParameterValueOnMaterials("FadeTransition", self.mFade_Transition)
        self.StaticMesh.SetScalarParameterValueOnMaterials("MountainFade", self.mMountainFade)
    

    def LostSignificance(self):
        self.ExecuteUbergraph_BP_VolumeFogSmall(15)
    

    def GainedSignificance(self):
        self.ExecuteUbergraph_BP_VolumeFogSmall(10)
    

    def ReceiveEndPlay(self):
        ExecuteUbergraph_BP_VolumeFogSmall.K2Node_Event_EndPlayReason = EndPlayReason #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_VolumeFogSmall(20)
    

    def ReceiveTick(self):
        ExecuteUbergraph_BP_VolumeFogSmall.K2Node_Event_DeltaSeconds = DeltaSeconds #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_VolumeFogSmall(40)
    

    def ReceiveBeginPlay(self):
        self.ExecuteUbergraph_BP_VolumeFogSmall(78)
    

    def ExecuteUbergraph_BP_VolumeFogSmall(self):
        # End
        # End
        # End
        # Label 25
        self.ReceiveBeginPlay()
        # End
        self.ReceiveTick(DeltaSeconds)
        self.UpdateBrightness()
        # End
        goto('L25')
    
