
from codegen.ue4_stub import *

from Script.FactoryGame import FGBuildableRailroadSwitchControl
from Script.Engine import BreakRotator
from Script.FactoryGame import GetSwitchPosition
from Script.CoreUObject import Rotator
from Script.Engine import K2_SetRelativeRotation
from Script.Engine import MakeRotator
from Game.FactoryGame.Buildable.Factory.Train.SwitchControl.Build_RailroadSwitchControl import ExecuteUbergraph_Build_RailroadSwitchControl

class Build_RailroadSwitchControl(FGBuildableRailroadSwitchControl):
    mPowerConsumptionExponent = 1.600000023841858
    mPowerInfoClass = NewObject[FGPowerInfoComponent]()
    mMinimumProducingTime = 2
    mMinimumStoppedTime = 5
    mNumCyclesForProductivity = 20
    mCurrentPotential = 1
    mPendingPotential = 1
    mMinPotential = 0.009999999776482582
    mMaxPotential = 1
    mMaxPotentialIncreasePerCrystal = 0.5
    mFluidStackSizeDefault = EStackSize::SS_FLUID
    mFluidStackSizeMultiplier = 1
    mSignificanceRange = 18000
    mHologramClass = NewObject[FGFactoryHologram]()
    mDisplayName = NSLOCTEXT("", "AB8E9E654E6CFB4B4ED99D843670C2B7", "Railroad Switch Control")
    MaxRenderDistance = -1
    mFactoryTickFunction = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=True, bTickEvenWhenPaused=False)
    mPrimaryColor = Namespace(A=1, B=-1, G=-1, R=-1)
    mSecondaryColor = Namespace(A=1, B=-1, G=-1, R=-1)
    mDismantleEffectClassName = Namespace(AssetPathName='/Game/FactoryGame/Buildable/Factory/-Shared/BP_MaterialEffect_Dismantle.BP_MaterialEffect_Dismantle_C', SubPathString='')
    mBuildEffectClassName = Namespace(AssetPathName='/Game/FactoryGame/Buildable/Factory/-Shared/BP_MaterialEffect_Build.BP_MaterialEffect_Build_C', SubPathString='')
    mHighlightParticleClassName = Namespace(AssetPathName='/Game/FactoryGame/Buildable/-Shared/Particle/NewBuildingPing.NewBuildingPing_C', SubPathString='')
    mCameraDistanceSq = 100000000376832
    mBuildingID = -1
    bReplicates = True
    RemoteRole = 1
    NetCullDistanceSquared = 5624999936
    RootComponent = Namespace(Mobility=0, ObjectClass='/Script/Engine.SceneComponent', ObjectFlags=2883617, ObjectName='RootComponent')
    
    def UpdateSwitchPositionVisuals(self):
        self.ExecuteUbergraph_Build_RailroadSwitchControl(10)
    

    def ExecuteUbergraph_Build_RailroadSwitchControl(self):
        ReturnValue: int32 = self.GetSwitchPosition()
        ReturnValue_0: float = ReturnValue * 90
        
        Roll = None
        Pitch = None
        Yaw = None
        BreakRotator(self.SwitchLeveler.RelativeRotation, Ref[Roll], Ref[Pitch], Ref[Yaw])
        ReturnValue_1: float = ReturnValue_0 - 45
        ReturnValue_2: Rotator = MakeRotator(ReturnValue_1, Pitch, Yaw)
        
        SweepHitResult = None
        self.SwitchLeveler.K2_SetRelativeRotation(ReturnValue_2, False, False, Ref[SweepHitResult])
    
