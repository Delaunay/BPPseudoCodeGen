
from codegen.ue4_stub import *

from Script.FactoryGame import CreateAndAddNewRepresentation
from Game.FactoryGame.Buildable.Factory.TruckStation.UI.TruckStation import TruckStation
from Game.FactoryGame.Buildable.Factory.TruckStation.Build_TruckStation import ExecuteUbergraph_Build_TruckStation.K2Node_ComponentBoundEvent_OtherComp
from Script.Engine import ReceiveBeginPlay
from Game.FactoryGame.Buildable.Factory.TruckStation.Build_TruckStation import ExecuteUbergraph_Build_TruckStation
from Script.Engine import Not_PreBool
from Script.Engine import HasAuthority
from Script.Engine import Default__KismetSystemLibrary
from Script.FactoryGame import Get
from Game.FactoryGame.Buildable.Factory.TruckStation.Build_TruckStation import ExecuteUbergraph_Build_TruckStation.K2Node_ComponentBoundEvent_OtherBodyIndex
from Game.FactoryGame.Buildable.Factory.TruckStation.Build_TruckStation import ExecuteUbergraph_Build_TruckStation.K2Node_Event_EndPlayReason
from Game.FactoryGame.Buildable.Factory.TruckStation.Build_TruckStation import ExecuteUbergraph_Build_TruckStation.K2Node_ComponentBoundEvent_SweepResult
from Script.Engine import IsValid
from Script.FactoryGame import Default__FGActorRepresentationManager
from Game.FactoryGame.Buildable.Factory.TruckStation.Build_TruckStation import ExecuteUbergraph_Build_TruckStation.K2Node_ComponentBoundEvent_OtherActor
from Game.FactoryGame.Buildable.Factory.TruckStation.Build_TruckStation import ExecuteUbergraph_Build_TruckStation.K2Node_ComponentBoundEvent_OtherComp1
from Game.FactoryGame.Buildable.Factory.TruckStation.Build_TruckStation import ExecuteUbergraph_Build_TruckStation.K2Node_Event_newColor
from Script.FactoryGame import UpdateRepresentation
from Game.FactoryGame.Buildable.Factory.TruckStation.Build_TruckStation import ExecuteUbergraph_Build_TruckStation.K2Node_ComponentBoundEvent_OtherBodyIndex1
from Game.FactoryGame.Buildable.Factory.TruckStation.Build_TruckStation import ExecuteUbergraph_Build_TruckStation.K2Node_ComponentBoundEvent_OverlappedComponent1
from Script.FactoryGame import FGDockableInterface
from Script.CoreUObject import Vector
from Game.FactoryGame.Buildable.Factory.TruckStation.Build_TruckStation import ExecuteUbergraph_Build_TruckStation.K2Node_ComponentBoundEvent_bFromSweep
from Script.FactoryGame import FGActorRepresentationManager
from Game.FactoryGame.Buildable.Factory.TruckStation.Build_TruckStation import ExecuteUbergraph_Build_TruckStation.K2Node_ComponentBoundEvent_OverlappedComponent
from Script.Engine import EqualEqual_ObjectObject
from Game.FactoryGame.Buildable.Factory.TruckStation.Build_TruckStation import ExecuteUbergraph_Build_TruckStation.K2Node_ComponentBoundEvent_OtherActor1
from Script.FactoryGame import FGBuildableDockingStation
from Game.FactoryGame.Interface.UI.HUDHelpers.HUDHelpers import Default__HUDHelpers
from Script.Engine import Actor
from Script.Engine import K2_GetActorLocation
from Script.Engine import ReceiveEndPlay
from Script.FactoryGame import RemoveRepresentationOfActor
from Script.FactoryGame import GetDockedActor

class Build_TruckStation(FGBuildableDockingStation):
    mMapText: FText
    mStorageSizeX = 8
    mStorageSizeY = 6
    mTransferSpeed = 0.5
    mFuelTransferSpeed = 5
    mFuelInventoryHandler = Namespace(ObjectClass='/Script/FactoryGame.FGReplicationDetailInventoryComponent', ObjectFlags=2883617, ObjectName='FuelInventoryHandler')
    mInventoryHandler = Namespace(ObjectClass='/Script/FactoryGame.FGReplicationDetailInventoryComponent', ObjectFlags=2883617, ObjectName='InventoryHandler')
    mIsInLoadMode = True
    mStackTransferSize = 1
    mPowerConsumption = 20
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
    mAddToSignificanceManager = True
    mSignificanceRange = 18000
    mHologramClass = NewObject[FGFactoryHologram]()
    mDisplayName = NSLOCTEXT("", "3B3576E9482BA277C308C88DFCB73D1B", "Truck Station")
    mDescription = NewObject[ Has an inventory with 48 slots.\r\nTransfers up to 120 stacks per minute to/from docked vehicle. \r\nAlways refuels vehicles if it has access to a matching fuel type..\r\n")]()
    MaxRenderDistance = -1
    mFactoryTickFunction = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=True, bTickEvenWhenPaused=False)
    mPrimaryColor = Namespace(A=1, B=-1, G=-1, R=-1)
    mSecondaryColor = Namespace(A=1, B=-1, G=-1, R=-1)
    mDismantleEffectClassName = Namespace(AssetPathName='/Game/FactoryGame/Buildable/Factory/-Shared/BP_MaterialEffect_Dismantle.BP_MaterialEffect_Dismantle_C', SubPathString='')
    mBuildEffectClassName = Namespace(AssetPathName='/Game/FactoryGame/Buildable/Factory/-Shared/BP_MaterialEffect_Build.BP_MaterialEffect_Build_C', SubPathString='')
    mHighlightParticleClassName = Namespace(AssetPathName='/Game/FactoryGame/Buildable/-Shared/Particle/NewBuildingPing.NewBuildingPing_C', SubPathString='')
    mCameraDistanceSq = 100000000376832
    mBuildingID = -1
    mInteractWidgetClass = NewObject[Widget_DockingStation]()
    mIsUseable = True
    bReplicates = True
    RemoteRole = 1
    NetCullDistanceSquared = 5624999936
    RootComponent = Namespace(Mobility=0, ObjectClass='/Script/Engine.SceneComponent', ObjectFlags=2883617, ObjectName='RootComponent')
    Tags = ['Fuel']
    
    def GetActorCompassViewDistance(self):
        ReturnValue = 4
    

    def SetActorCompassViewDistance(self):
        ReturnValue = 0
    

    def AddAsRepresentation(self):
        ReturnValue: bool = self.HasAuthority()
        if not ReturnValue:
            goto('L145')
        ReturnValue_0: Ptr[FGActorRepresentationManager] = Default__FGActorRepresentationManager.Get(self)
        ReturnValue_1: bool = ReturnValue_0.CreateAndAddNewRepresentation(self, False)
        ReturnValue_2: bool = ReturnValue_1
        goto('L156')
        # Label 145
        ReturnValue_2 = False
    

    def GetActorFogOfWarRevealRadius(self):
        ReturnValue = 0
    

    def GetActorFogOfWarRevealType(self):
        ReturnValue = 0
    

    def GetActorRepresentationColor(self):
        
        Text = None
        Graphics = None
        Default__HUDHelpers.GetFactoryGameDarkGray(self, Ref[Text], Ref[Graphics])
        ReturnValue = Graphics
    

    def GetActorRepresentationText(self):
        ReturnValue = self.mDisplayName
    

    def GetActorRepresentationTexture(self):
        ReturnValue = TruckStation
    

    def GetActorRepresentationType(self):
        ReturnValue = 13
    

    def GetActorShouldShowInCompass(self):
        ReturnValue = True
    

    def GetActorShouldShowOnMap(self):
        ReturnValue = True
    

    def GetRealActorLocation(self):
        ReturnValue: Vector = self.K2_GetActorLocation()
        ReturnValue_0: Vector = ReturnValue
    

    def GetRealActorRotation(self):
        ReturnValue = Rotator::FromPitchYawRoll(0, 0, 0)
    

    def IsActorStatic(self):
        ReturnValue = True
    

    def RemoveAsRepresentation(self):
        ReturnValue: bool = self.HasAuthority()
        if not ReturnValue:
            goto('L144')
        ReturnValue_0: Ptr[FGActorRepresentationManager] = Default__FGActorRepresentationManager.Get(self)
        ReturnValue_1: bool = ReturnValue_0.RemoveRepresentationOfActor(self)
        ReturnValue_2: bool = ReturnValue_1
        goto('L155')
        # Label 144
        ReturnValue_2 = False
    

    def SetActorRepresentationText(self):
        self.mMapText = self.mDisplayName
        ReturnValue = self.mMapText
    

    def UpdateRepresentation(self):
        ReturnValue: bool = self.HasAuthority()
        if not ReturnValue:
            goto('L145')
        ReturnValue_0: Ptr[FGActorRepresentationManager] = Default__FGActorRepresentationManager.Get(self)
        ReturnValue_1: bool = ReturnValue_0.UpdateRepresentation(self, False)
        ReturnValue_2: bool = ReturnValue_1
        goto('L156')
        # Label 145
        ReturnValue_2 = False
    

    def SetActorRepresentationColor(self):
        ExecuteUbergraph_Build_TruckStation.K2Node_Event_newColor = NewColor #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Build_TruckStation(39)
    

    def BndEvt__Box_K2Node_ComponentBoundEvent_0_ComponentBeginOverlapSignature__DelegateSignature(self, OverlappedComponent: Ptr[PrimitiveComponent], OtherActor: Ptr[Actor], OtherComp: Ptr[PrimitiveComponent], OtherBodyIndex: int32, bFromSweep: bool, SweepResult: Const[Ref[HitResult]]):
        ExecuteUbergraph_Build_TruckStation.K2Node_ComponentBoundEvent_OverlappedComponent1 = OverlappedComponent #  PERSISTENT_FRAME(
        ExecuteUbergraph_Build_TruckStation.K2Node_ComponentBoundEvent_OtherActor1 = OtherActor #  PERSISTENT_FRAME(
        ExecuteUbergraph_Build_TruckStation.K2Node_ComponentBoundEvent_OtherComp1 = OtherComp #  PERSISTENT_FRAME(
        ExecuteUbergraph_Build_TruckStation.K2Node_ComponentBoundEvent_OtherBodyIndex1 = OtherBodyIndex #  PERSISTENT_FRAME(
        ExecuteUbergraph_Build_TruckStation.K2Node_ComponentBoundEvent_bFromSweep = bFromSweep #  PERSISTENT_FRAME(
        ExecuteUbergraph_Build_TruckStation.K2Node_ComponentBoundEvent_SweepResult = SweepResult #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Build_TruckStation(44)
    

    def BndEvt__Box_K2Node_ComponentBoundEvent_1_ComponentEndOverlapSignature__DelegateSignature(self, OverlappedComponent: Ptr[PrimitiveComponent], OtherActor: Ptr[Actor], OtherComp: Ptr[PrimitiveComponent], OtherBodyIndex: int32):
        ExecuteUbergraph_Build_TruckStation.K2Node_ComponentBoundEvent_OverlappedComponent = OverlappedComponent #  PERSISTENT_FRAME(
        ExecuteUbergraph_Build_TruckStation.K2Node_ComponentBoundEvent_OtherActor = OtherActor #  PERSISTENT_FRAME(
        ExecuteUbergraph_Build_TruckStation.K2Node_ComponentBoundEvent_OtherComp = OtherComp #  PERSISTENT_FRAME(
        ExecuteUbergraph_Build_TruckStation.K2Node_ComponentBoundEvent_OtherBodyIndex = OtherBodyIndex #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Build_TruckStation(497)
    

    def ReceiveBeginPlay(self):
        self.ExecuteUbergraph_Build_TruckStation(502)
    

    def ReceiveEndPlay(self):
        ExecuteUbergraph_Build_TruckStation.K2Node_Event_EndPlayReason = EndPlayReason #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Build_TruckStation(541)
    

    def ExecuteUbergraph_Build_TruckStation(self):
        # Label 10
        ReturnValue: bool = self.RemoveAsRepresentation()
        # End
        # End
        ReturnValue1: bool = self.HasAuthority()
        if not ReturnValue1:
            goto('L565')
        ReturnValue1_0: Ptr[Actor] = self.GetDockedActor()
        ReturnValue_0: bool = Default__KismetSystemLibrary.IsValid(ReturnValue1_0)
        ReturnValue_1: bool = Not_PreBool(ReturnValue_0)
        if not ReturnValue_1:
            goto('L565')
        Interface: TScriptInterface[FGDockableInterface] = QueryInterface[FGDockableInterface](OtherActor1)
        bSuccess: bool = Interface
        if not bSuccess:
            goto('L565')
        ReturnValue_2: bool = GetInterfaceUObject(Interface).CanDock(1)
        if not ReturnValue_2:
            goto('L565')
        ReturnValue_3: bool = self.Dock(OtherActor1)
        # End
        # Label 372
        ReturnValue_4: bool = self.HasAuthority()
        if not ReturnValue_4:
            goto('L565')
        ReturnValue_5: Ptr[Actor] = self.GetDockedActor()
        ReturnValue_6: bool = EqualEqual_ObjectObject(OtherActor, ReturnValue_5)
        if not ReturnValue_6:
            goto('L565')
        self.Undock()
        # End
        goto('L372')
        self.ReceiveBeginPlay()
        ReturnValue_7: bool = self.AddAsRepresentation()
        # End
        self.ReceiveEndPlay(EndPlayReason)
        goto('L10')
    
