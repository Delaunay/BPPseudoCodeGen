
from codegen.ue4_stub import *

from Script.Engine import Lerp
from Script.Engine import Conv_IntToFloat
from Script.Engine import ReceiveBeginPlay
from Script.Engine import Default__KismetSystemLibrary
from Script.FactoryGame import Get
from Script.Engine import ReceiveTick
from Script.Engine import SetScalarParameterValueOnMaterials
from Script.Engine import IsValid
from Script.Engine import CurveFloat
from Script.FactoryGame import FGTimeOfDaySubsystem
from Game.FactoryGame.World.Environment.VolumeFog.BP_VolumeFog import ExecuteUbergraph_BP_VolumeFog
from Script.CoreUObject import Vector
from Game.FactoryGame.World.Environment.VolumeFog.BP_VolumeFog import ExecuteUbergraph_BP_VolumeFog.K2Node_Event_EndPlayReason
from Game.FactoryGame.World.Environment.VolumeFog.BP_VolumeFog import ExecuteUbergraph_BP_VolumeFog.K2Node_Event_DeltaSeconds
from Script.Engine import Actor
from Script.Engine import ReceiveEndPlay
from Script.Engine import IsDedicatedServer
from Script.FactoryGame import Default__FGTimeOfDaySubsystem
from Script.Engine import GetFloatValue
from Script.FactoryGame import GetDayMinutes

class BP_VolumeFog(Actor):
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
        ReturnValue: bool = Default__KismetSystemLibrary.IsDedicatedServer(self)
        if not ReturnValue:
            goto('L62')
        # End
        # Label 62
        ReturnValue_0: Ptr[FGTimeOfDaySubsystem] = Default__FGTimeOfDaySubsystem.Get(self)
        ReturnValue_1: bool = Default__KismetSystemLibrary.IsValid(ReturnValue_0)
        if not ReturnValue_1:
            goto('L464')
        ReturnValue_0 = Default__FGTimeOfDaySubsystem.Get(self)
        ReturnValue_2: int32 = ReturnValue_0.GetDayMinutes()
        ReturnValue_3: float = Conv_IntToFloat(ReturnValue_2)
        ReturnValue_4: float = self.mBrightnessCurve.GetFloatValue(ReturnValue_3)
        ReturnValue_5: float = Lerp(7, self.mBrightness, ReturnValue_4)
        self.StaticMesh.SetScalarParameterValueOnMaterials("Brightness", ReturnValue_5)
    

    def UserConstructionScript(self):
        ReturnValue: Vector = Vector(self.mSize_X, self.mSize_Y, 1)
        self.StaticMesh.SetRelativeScale3D(ReturnValue)
        self.StaticMesh.SetScalarParameterValueOnMaterials("Brightness", self.mBrightness)
        self.StaticMesh.SetScalarParameterValueOnMaterials("AppearDistance", self.mAppear_Distance)
        self.StaticMesh.SetScalarParameterValueOnMaterials("FadeTransition", self.mFade_Transition)
        self.StaticMesh.SetScalarParameterValueOnMaterials("MountainFade", self.mMountainFade)
    

    def LostSignificance(self):
        self.ExecuteUbergraph_BP_VolumeFog(15)
    

    def GainedSignificance(self):
        self.ExecuteUbergraph_BP_VolumeFog(10)
    

    def ReceiveEndPlay(self):
        ExecuteUbergraph_BP_VolumeFog.K2Node_Event_EndPlayReason = EndPlayReason #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_VolumeFog(20)
    

    def ReceiveTick(self):
        ExecuteUbergraph_BP_VolumeFog.K2Node_Event_DeltaSeconds = DeltaSeconds #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_VolumeFog(59)
    

    def ReceiveBeginPlay(self):
        self.ExecuteUbergraph_BP_VolumeFog(97)
    

    def ExecuteUbergraph_BP_VolumeFog(self):
        # End
        # End
        self.ReceiveEndPlay(EndPlayReason)
        # End
        # Label 44
        self.ReceiveBeginPlay()
        # End
        self.ReceiveTick(DeltaSeconds)
        self.UpdateBrightness()
        # End
        goto('L44')
    
