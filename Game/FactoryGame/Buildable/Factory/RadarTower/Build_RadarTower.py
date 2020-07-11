
from codegen.ue4_stub import *

from Game.FactoryGame.Character.Player.BP_RemoteCallObject import BP_RemoteCallObject
from Script.FactoryGame import FGPlayerController
from Script.FactoryGame import CreateAndAddNewRepresentation
from Script.FactoryGame import FGBuildableRadarTower
from Script.CoreUObject import Rotator
from Script.Engine import GetComponentBounds
from Script.Engine import HasAuthority
from Script.Engine import Default__KismetSystemLibrary
from Script.FactoryGame import Get
from Script.Engine import PlayerController
from Script.FactoryGame import Default__FGActorRepresentationManager
from Script.FactoryGame import GetCurrentRevealRadius
from Script.FactoryGame import UpdateRepresentation
from Script.Engine import GetPlayerController
from Script.Engine import Default__GameplayStatics
from Script.Engine import FlushNetDormancy
from Script.CoreUObject import Vector
from Script.FactoryGame import FGActorRepresentationManager
from Game.FactoryGame.Interface.UI.Assets.Map.MapCompass_Icon_radartower import MapCompass_Icon_radartower
from Script.Engine import K2_GetActorRotation
from Script.FactoryGame import GetRemoteCallObjectOfClass
from Game.FactoryGame.Interface.UI.HUDHelpers.HUDHelpers import Default__HUDHelpers
from Game.FactoryGame.Buildable.Factory.RadarTower.Build_RadarTower import ExecuteUbergraph_Build_RadarTower
from Script.Engine import K2_GetActorLocation
from Script.FactoryGame import RemoveRepresentationOfActor
from Game.FactoryGame.Buildable.Factory.RadarTower.Build_RadarTower import ExecuteUbergraph_Build_RadarTower.K2Node_Event_EndPlayReason
from Game.FactoryGame.Buildable.Factory.RadarTower.Build_RadarTower import ExecuteUbergraph_Build_RadarTower.K2Node_Event_newColor
from Script.FactoryGame import EFogOfWarRevealType

class Build_RadarTower(FGBuildableRadarTower):
    mMapText: FText = NSLOCTEXT("", "CDF0BA8D44E9F4BED2864AAC21BDA5B9", "Radar Tower")
    mMinRevealRadius = 35000
    mMaxRevealRadius = 70000
    mNumRadarExpansionSteps = 11
    mRadarExpansionInterval = 300
    mTimeToNextExpansion = 300
    mPowerConsumption = 30
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
    mDisplayName = NSLOCTEXT("", "A23E89434DAEB0ED399BCF8005371E37", "Radar Tower")
    mDescription = NSLOCTEXT("", "4124C71741E44AA6E3F376B1BF46DDE2", "Reveals an area around itself on the map. The area grows over time to a max.\r\nPlacing the tower heigher up increases the max area revealed.")
    MaxRenderDistance = -1
    mFactoryTickFunction = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=True, bTickEvenWhenPaused=False)
    mPrimaryColor = Namespace(A=1, B=-1, G=-1, R=-1)
    mSecondaryColor = Namespace(A=1, B=-1, G=-1, R=-1)
    mDismantleEffectClassName = Namespace(AssetPathName='/Game/FactoryGame/Buildable/Factory/-Shared/BP_MaterialEffect_Dismantle.BP_MaterialEffect_Dismantle_C', SubPathString='')
    mBuildEffectClassName = Namespace(AssetPathName='/Game/FactoryGame/Buildable/Factory/-Shared/BP_MaterialEffect_Build.BP_MaterialEffect_Build_C', SubPathString='')
    mHighlightParticleClassName = Namespace(AssetPathName='/Game/FactoryGame/Buildable/-Shared/Particle/NewBuildingPing.NewBuildingPing_C', SubPathString='')
    mCameraDistanceSq = 100000000376832
    mBuildingID = -1
    mInteractWidgetClass = NewObject[Widget_RadarTower]()
    mIsUseable = True
    PrimaryActorTick = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=True, bTickEvenWhenPaused=False)
    bReplicates = True
    RemoteRole = 1
    NetCullDistanceSquared = 5624999936
    NetUpdateFrequency = 1
    RootComponent = Namespace(Mobility=0, ObjectClass='/Script/Engine.SceneComponent', ObjectFlags=2883617, ObjectName='RootComponent')
    
    def GetActorCompassViewDistance(self):
        ReturnValue = 4
    

    def SetActorCompassViewDistance(self):
        ReturnValue = 0
    

    def SetActorRepresentationText(self):
        ReturnValue: bool = self.HasAuthority()
        if not ReturnValue:
            goto('L127')
        self.FlushNetDormancy()
        self.mMapText = newText
        ReturnValue_0: bool = self.UpdateRepresentation()
        # Label 95
        ReturnValue_1: FText = newText
        goto('L356')
        # Label 127
        ReturnValue_2: Ptr[PlayerController] = Default__GameplayStatics.GetPlayerController(self, 0)
        Controller: Ptr[FGPlayerController] = Cast[FGPlayerController](ReturnValue_2)
        bSuccess: bool = Controller
        if not bSuccess:
            goto('L356')
        ReturnValue_3: Ptr[BP_RemoteCallObject] = Controller.GetRemoteCallObjectOfClass(BP_RemoteCallObject)
        ReturnValue_3.Server_SetActorRepresentationText(self, newText)
        goto('L95')
    

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
    

    def GetActorRepresentationColor(self):
        
        Text = None
        Graphics = None
        Default__HUDHelpers.GetFactoryGameDarkGray(self, Ref[Text], Ref[Graphics])
        ReturnValue = Graphics
    

    def GetActorRepresentationText(self):
        ReturnValue = self.mMapText
    

    def GetActorRepresentationTexture(self):
        ReturnValue = MapCompass_Icon_radartower
    

    def GetActorRepresentationType(self):
        ReturnValue = 6
    

    def GetActorShouldShowInCompass(self):
        ReturnValue = True
    

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
        ReturnValue: float = self.GetCurrentRevealRadius()
        ReturnValue_0: float = ReturnValue
    

    def GetActorFogOfWarRevealType(self):
        Variable: uint8 = 2
        Variable1: uint8 = 0
        ReturnValue: bool = self.HasPower()
        Variable_0: bool = ReturnValue
        
        switch = {
            False: Variable1,
            True: Variable
        }
        ReturnValue_0: uint8 = switch.get(Variable_0, None)
    

    def GetActorShouldShowOnMap(self):
        ReturnValue = True
    

    def GetRealActorLocation(self):
        ReturnValue: Vector = self.K2_GetActorLocation()
        
        Origin = None
        BoxExtent = None
        SphereRadius = None
        Default__KismetSystemLibrary.GetComponentBounds(self.FGColoredInstanceMeshProxy, Ref[Origin], Ref[BoxExtent], Ref[SphereRadius])
        
        X = None
        Y = None
        Z = None
        X, Y, Z = BreakVector(BoxExtent)
        ReturnValue_0: Vector = Vector(0, 0, Z)
        ReturnValue_1: Vector = ReturnValue + ReturnValue_0
        ReturnValue_2: Vector = ReturnValue_1
    

    def GetRealActorRotation(self):
        ReturnValue: Rotator = self.K2_GetActorRotation()
        ReturnValue_0: Rotator = ReturnValue
    

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
    

    def SetActorRepresentationColor(self):
        ExecuteUbergraph_Build_RadarTower.K2Node_Event_newColor = NewColor #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Build_RadarTower(57)
    

    def ReceiveBeginPlay(self):
        self.ExecuteUbergraph_Build_RadarTower(62)
    

    def ReceiveEndPlay(self):
        ExecuteUbergraph_Build_RadarTower.K2Node_Event_EndPlayReason = EndPlayReason #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Build_RadarTower(91)
    

    def OnRadiusUpdateTriggered(self):
        self.ExecuteUbergraph_Build_RadarTower(120)
    

    def ExecuteUbergraph_Build_RadarTower(self):
        # Label 10
        OutputDelegate.BindUFunction(self, OnRadiusUpdateTriggered)
        self.OnRadarTowerRadiusUpdated.AddUnique(OutputDelegate)
        # End
        # End
        ReturnValue: bool = self.AddAsRepresentation()
        goto('L10')
        ReturnValue_0: bool = self.RemoveAsRepresentation()
        # End
        ReturnValue_1: bool = self.UpdateRepresentation()
    
