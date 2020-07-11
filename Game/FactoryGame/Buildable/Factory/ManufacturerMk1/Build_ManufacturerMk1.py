
from codegen.ue4_stub import *

from Game.FactoryGame.VFX.Factory.Manufacturer.P_CoolingSmokeSides_03 import P_CoolingSmokeSides_03
from Script.Engine import SpawnEmitterAtLocation
from Script.FactoryGame import TryStopProductionLoopEffects
from Script.FactoryGame import FGBuildableManufacturer
from Game.FactoryGame.Buildable.Factory.ManufacturerMk1.Audio.Play_F_Manufacturer_AmbienceLoopDirect import Play_F_Manufacturer_AmbienceLoopDirect
from Script.Engine import Default__KismetSystemLibrary
from Script.FactoryGame import StartProductionLoopEffects
from Script.FactoryGame import TryStartProductionLoopEffects
from Script.Engine import IsValid
from Game.FactoryGame.Buildable.Factory.ManufacturerMk1.Build_ManufacturerMk1 import ExecuteUbergraph_Build_ManufacturerMk1.K2Node_Event_didStartProducing
from Script.Engine import Default__GameplayStatics
from Script.FactoryGame import TryStartIdlingLoopEffects
from Script.CoreUObject import Vector
from Script.AkAudio import Default__AkGameplayStatics
from Script.FactoryGame import TryStopIdlingLoopEffects
from Script.AkAudio import PostAkEventAttached
from Script.Engine import K2_DestroyComponent
from Game.FactoryGame.Buildable.Factory.AssemblerMk1.Audio.Stop_F_Manufacturer_AmbienceLoopDirect import Stop_F_Manufacturer_AmbienceLoopDirect
from Script.FactoryGame import LostSignificance
from Script.Engine import ParticleSystemComponent
from Game.FactoryGame.Buildable.Factory.ManufacturerMk1.Audio.Play_F_Manufacturer_AmbienceStartupLoop import Play_F_Manufacturer_AmbienceStartupLoop
from Game.FactoryGame.Buildable.Factory.ManufacturerMk1.Build_ManufacturerMk1 import ExecuteUbergraph_Build_ManufacturerMk1.K2Node_Event_didStopProducing
from Game.FactoryGame.Buildable.Factory.ManufacturerMk1.Audio.Stop_F_Manufacturer_AmbienceLoop import Stop_F_Manufacturer_AmbienceLoop
from Game.FactoryGame.VFX.Factory.Manufacturer.P_Manufacturer_Chimney_01 import P_Manufacturer_Chimney_01
from Script.AkAudio import AkComponent
from Script.FactoryGame import GainedSignificance
from Script.FactoryGame import StopProductionLoopEffects
from Game.FactoryGame.Buildable.Factory.ManufacturerMk1.Build_ManufacturerMk1 import ExecuteUbergraph_Build_ManufacturerMk1

class Build_ManufacturerMk1(FGBuildableManufacturer):
    P_SideHeat_01: Ptr[ParticleSystemComponent]
    P_SideHeat_02: Ptr[ParticleSystemComponent]
    P_ChimneySmoke_01: Ptr[ParticleSystemComponent]
    P_CoolingTank_01: Ptr[ParticleSystemComponent]
    mManufacturingSpeed = 1
    mPowerConsumption = 55
    mPowerConsumptionExponent = 1.600000023841858
    mPowerInfoClass = NewObject[FGPowerInfoComponent]()
    mMinimumProducingTime = 2
    mMinimumStoppedTime = 5
    mNumCyclesForProductivity = 20
    mCanChangePotential = True
    mCurrentPotential = 1
    mPendingPotential = 1
    mMinPotential = 0.009999999776482582
    mMaxPotential = 1
    mMaxPotentialIncreasePerCrystal = 0.5
    mFluidStackSizeDefault = EStackSize::SS_FLUID
    mFluidStackSizeMultiplier = 1
    mAddToSignificanceManager = True
    mSignificanceRange = 18000
    mHologramClass = NewObject[FGFactoryHologram]()
    mDisplayName = NSLOCTEXT("", "F2F84BA44DC64F9CC65388BF8D7EE2EF", "Manufacturer")
    mDescription = NSLOCTEXT("", "A0D2CD4B4CC567617D0954ABDA23A1D6", "Crafts three or four parts into another part.\r\n\r\nCan be automated by feeding parts into it with a conveyor belt connected to the input. The produced parts can be automatically extracted by connecting a conveyor belt to the output.")
    MaxRenderDistance = -1
    mFactoryTickFunction = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=True, bTickEvenWhenPaused=False)
    mPrimaryColor = Namespace(A=1, B=-1, G=-1, R=-1)
    mSecondaryColor = Namespace(A=1, B=-1, G=-1, R=-1)
    mDismantleEffectClassName = Namespace(AssetPathName='/Game/FactoryGame/Buildable/Factory/-Shared/BP_MaterialEffect_Dismantle.BP_MaterialEffect_Dismantle_C', SubPathString='')
    mBuildEffectClassName = Namespace(AssetPathName='/Game/FactoryGame/Buildable/Factory/-Shared/BP_MaterialEffect_Build.BP_MaterialEffect_Build_C', SubPathString='')
    mHighlightParticleClassName = Namespace(AssetPathName='/Game/FactoryGame/Buildable/-Shared/Particle/NewBuildingPing.NewBuildingPing_C', SubPathString='')
    mCameraDistanceSq = 100000000376832
    mBuildingID = -1
    mInteractWidgetClass = NewObject[Widget_Manufacturing]()
    mIsUseable = True
    PrimaryActorTick = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=True, bTickEvenWhenPaused=False)
    bReplicates = True
    RemoteRole = 1
    NetCullDistanceSquared = 5624999936
    RootComponent = Namespace(Mobility=0, ObjectClass='/Script/Engine.SceneComponent', ObjectFlags=2883617, ObjectName='RootComponent')
    
    def SetText(self, intText: FString):
        pass
    

    def GainedSignificance(self):
        self.ExecuteUbergraph_Build_ManufacturerMk1(26)
    

    def LostSignificance(self):
        self.ExecuteUbergraph_Build_ManufacturerMk1(139)
    

    def StartProductionLoopEffects(self):
        ExecuteUbergraph_Build_ManufacturerMk1.K2Node_Event_didStartProducing = didStartProducing #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Build_ManufacturerMk1(308)
    

    def StopProductionLoopEffects(self):
        ExecuteUbergraph_Build_ManufacturerMk1.K2Node_Event_didStopProducing = didStopProducing #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Build_ManufacturerMk1(1078)
    

    def ExecuteUbergraph_Build_ManufacturerMk1(self):
        # Label 10
        self.TryStopIdlingLoopEffects(False)
        # End
        self.GainedSignificance()
        ReturnValue: bool = self.HasPower()
        if not ReturnValue:
            goto('L1539')
        self.TryStartIdlingLoopEffects(False)
        ReturnValue_0: bool = self.IsProducing()
        if not ReturnValue_0:
            goto('L1539')
        self.TryStartProductionLoopEffects(False)
        # End
        self.LostSignificance()
        ReturnValue1: bool = self.HasPower()
        ReturnValue1_0: bool = self.IsProducing()
        ReturnValue_1: bool = ReturnValue1 and ReturnValue1_0
        if not ReturnValue_1:
            goto('L265')
        self.TryStopProductionLoopEffects(False)
        goto('L10')
        # Label 265
        ReturnValue2: bool = self.HasPower()
        if not ReturnValue2:
            goto('L1539')
        goto('L10')
        self.StartProductionLoopEffects(didStartProducing)
        ReturnValue1_1: bool = Default__KismetSystemLibrary.IsValid(self.P_SideHeat_01)
        if not ReturnValue1_1:
            goto('L397')
        # End
        # Label 397
        ReturnValue2_0: Vector = self.MainMesh.GetSocketLocation("vfx_heatSocket_01")
        ReturnValue2_1: Ptr[ParticleSystemComponent] = Default__GameplayStatics.SpawnEmitterAtLocation(self, P_CoolingSmokeSides_03, ReturnValue2_0, Rotator::FromPitchYawRoll(0, 0, 0), Vector(1, 1, 1), True, 0)
        self.P_SideHeat_01 = ReturnValue2_1
        ReturnValue1_2: Vector = self.MainMesh.GetSocketLocation("vfx_heatSocket_02")
        ReturnValue1_3: Ptr[ParticleSystemComponent] = Default__GameplayStatics.SpawnEmitterAtLocation(self, P_CoolingSmokeSides_03, ReturnValue1_2, Rotator::FromPitchYawRoll(0, 180, 0), Vector(1, 1, 1), True, 0)
        self.P_SideHeat_02 = ReturnValue1_3
        ReturnValue_2: Vector = self.MainMesh.GetSocketLocation("vfx_ChimneySocket_01")
        ReturnValue_3: Ptr[ParticleSystemComponent] = Default__GameplayStatics.SpawnEmitterAtLocation(self, P_Manufacturer_Chimney_01, ReturnValue_2, Rotator::FromPitchYawRoll(0, 180, 0), Vector(1, 1, 1), True, 0)
        self.P_ChimneySmoke_01 = ReturnValue_3
        ReturnValue_4: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEventAttached(Play_F_Manufacturer_AmbienceStartupLoop, self.MainMesh, "sfx_AmbienceRoot", True)
        ReturnValue2_2: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEventAttached(Play_F_Manufacturer_AmbienceLoopDirect, self.MainMesh, "sfx_AmbienceRoot", True)
        # End
        self.StopProductionLoopEffects(didStopProducing)
        ReturnValue_5: bool = Default__KismetSystemLibrary.IsValid(self.P_SideHeat_01)
        if not ReturnValue_5:
            goto('L1539')
        ReturnValue2_3: bool = Default__KismetSystemLibrary.IsValid(self.P_SideHeat_02)
        if not ReturnValue2_3:
            goto('L1539')
        ReturnValue3: bool = Default__KismetSystemLibrary.IsValid(self.P_ChimneySmoke_01)
        if not ReturnValue3:
            goto('L1539')
        self.P_ChimneySmoke_01.K2_DestroyComponent(self)
        self.P_SideHeat_02.K2_DestroyComponent(self)
        self.P_SideHeat_01.K2_DestroyComponent(self)
        ReturnValue1_4: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEventAttached(Stop_F_Manufacturer_AmbienceLoop, self.MainMesh, "sfx_AmbienceRoot", True)
        ReturnValue3_0: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEventAttached(Stop_F_Manufacturer_AmbienceLoopDirect, self.MainMesh, "sfx_AmbienceRoot", True)
    
