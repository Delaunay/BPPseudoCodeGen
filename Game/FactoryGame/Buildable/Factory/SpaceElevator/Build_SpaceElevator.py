
from codegen.ue4_stub import *

from Game.FactoryGame.Character.Player.CameraShake.SpelevatorImpact_03 import SpelevatorImpact_03
from Script.Engine import ReceiveDestroyed
from Script.AkAudio import PostAkEvent
from Script.LevelSequence import LevelSequenceActor
from Script.FactoryGame import FGGamePhaseManager
from Script.Engine import SetVisibility
from Script.FactoryGame import CreateAndAddNewRepresentation
from Game.FactoryGame.Character.Player.CameraShake.SpelevatorImpact_02 import SpelevatorImpact_02
from Script.CoreUObject import Rotator
from Script.LevelSequence import SetEventReceivers
from Script.MovieScene import Play
from Script.Engine import ReceiveBeginPlay
from Script.MovieScene import MovieSceneSequencePlaybackSettings
from Script.FactoryGame import Default__FGGamePhaseManager
from Script.Engine import HasAuthority
from Script.FactoryGame import Get
from Game.FactoryGame.Buildable.Factory.SpaceElevator.Audio.Stop_SpaceElevator_SendOff import Stop_SpaceElevator_SendOff
from Game.FactoryGame.Buildable.Factory.SpaceElevator.Build_SpaceElevator import ExecuteUbergraph_Build_SpaceElevator.K2Node_Event_EndPlayReason
from Game.FactoryGame.Buildable.Factory.SpaceElevator.Audio.Play_SpaceElevator_StartUp_TestVersion import Play_SpaceElevator_StartUp_TestVersion
from Script.FactoryGame import Default__FGActorRepresentationManager
from Script.Engine import PlayWorldCameraShake
from Script.MovieScene import MovieSceneObjectBindingID
from Game.FactoryGame.Character.Player.CameraShake.SpelevatorImpact_04 import SpelevatorImpact_04
from Game.FactoryGame.Character.Player.CameraShake.SpelevatorImpact_01 import SpelevatorImpact_01
from Script.Engine import Default__GameplayStatics
from Script.Engine import FlushNetDormancy
from Game.FactoryGame.Interface.UI.Assets.Map.MapCompass_Icon_Spelevator import MapCompass_Icon_Spelevator
from Script.LevelSequence import LevelSequencePlayer
from Script.LevelSequence import Default__LevelSequencePlayer
from Game.FactoryGame.Buildable.Factory.SpaceElevator.Audio.Stop_SpaceElevator_StartUp_TestVersion import Stop_SpaceElevator_StartUp_TestVersion
from Script.CoreUObject import Vector
from Game.FactoryGame.Buildable.Factory.SpaceElevator.Build_SpaceElevator import ExecuteUbergraph_Build_SpaceElevator
from Script.FactoryGame import FGActorRepresentationManager
from Script.LevelSequence import CreateLevelSequencePlayer
from Script.Engine import K2_GetActorRotation
from Script.AkAudio import Default__AkGameplayStatics
from Game.FactoryGame.Buildable.Factory.SpaceElevator.Animation.SpaceElevatorSendOff import SpaceElevatorSendOff
from Game.FactoryGame.Buildable.Factory.SpaceElevator.Build_SpaceElevator import ExecuteUbergraph_Build_SpaceElevator.K2Node_Event_newColor
from Game.FactoryGame.Buildable.Factory.SpaceElevator.Audio.Play_SpaceElevator_SendOff import Play_SpaceElevator_SendOff
from Game.FactoryGame.Interface.UI.HUDHelpers.HUDHelpers import Default__HUDHelpers
from Script.Engine import Actor
from Script.Engine import K2_GetActorLocation
from Script.MovieScene import MovieSceneSequenceLoopCount
from Game.FactoryGame.Buildable.Factory.SpaceElevator.Build_SpaceElevator import ExecuteUbergraph_Build_SpaceElevator.K2Node_CustomEvent_gamePhase
from Script.LevelSequence import SetBinding
from Script.Engine import GetOwner
from Script.FactoryGame import RemoveRepresentationOfActor
from Script.CoreUObject import Guid
from Script.AkAudio import AkComponent
from Script.FactoryGame import FGBuildableSpaceElevator

class Build_SpaceElevator(FGBuildableSpaceElevator):
    mSendOffSequence: Ptr[LevelSequenceActor]
    mMapText: FText = NSLOCTEXT("", "72AE51914F2104C8A4AF37A0D23FB3B3", "Space Elevator")
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
    mHologramClass = NewObject[FGSpaceElevatorHologram]()
    mDisplayName = NSLOCTEXT("", "B0AE60A44F6A0BBC2C2B84B14CB7DB6F", "Space Elevator")
    mDescription = NSLOCTEXT("", "C9D44CF643D9DC6F4A803D96A1F54FD0", "Requires deliveries of special Project Parts to complete Phases of Project Assembly.\r\nCompleting Phases in the Space Elevator will unlock new Tiers in the HUB Terminal.")
    MaxRenderDistance = -1
    mHighlightVector = Namespace(X=-2010, Y=0, Z=240)
    mFactoryTickFunction = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=True, bTickEvenWhenPaused=False)
    mPrimaryColor = Namespace(A=1, B=-1, G=-1, R=-1)
    mSecondaryColor = Namespace(A=1, B=-1, G=-1, R=-1)
    mDismantleEffectClassName = Namespace(AssetPathName='/Game/FactoryGame/Buildable/Factory/-Shared/BP_MaterialEffect_Dismantle.BP_MaterialEffect_Dismantle_C', SubPathString='')
    mBuildEffectClassName = Namespace(AssetPathName='/Game/FactoryGame/Buildable/Factory/SpaceElevator/BP_MaterialEffect_SpaceElevator.BP_MaterialEffect_SpaceElevator_C', SubPathString='')
    mHighlightParticleClassName = Namespace(AssetPathName='/Game/FactoryGame/Buildable/-Shared/Particle/NewBuildingPing.NewBuildingPing_C', SubPathString='')
    mHighlightParticleSystemTemplate = Namespace(AssetPath='/Game/FactoryGame/Buildable/-Shared/Particle/NewBuildingPing.NewBuildingPing')
    mShouldShowHighlight = True
    mCameraDistanceSq = 100000000376832
    mBuildingID = -1
    mInteractWidgetClass = NewObject[Widget_SpaceElevator]()
    mIsUseable = True
    PrimaryActorTick = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=True, bTickEvenWhenPaused=False)
    bAlwaysRelevant = True
    bReplicates = True
    RemoteRole = 1
    NetCullDistanceSquared = 5624999936
    RootComponent = Namespace(Mobility=0, ObjectClass='/Script/Engine.SceneComponent', ObjectFlags=2883617, ObjectName='RootComponent')
    
    def GetActorCompassViewDistance(self):
        ReturnValue = 4
    

    def SetActorCompassViewDistance(self):
        ReturnValue = 0
    

    def SetActorRepresentationText(self):
        self.FlushNetDormancy()
        # Label 10
        self.mMapText = newText
        ReturnValue = self.mMapText
    

    def UpdateRepresentation(self):
        ReturnValue = False
    

    def GetActorRepresentationColor(self):
        
        Text = None
        Graphics = None
        Default__HUDHelpers.GetFactoryGameDarkGray(self, Ref[Text], Ref[Graphics])
        ReturnValue = Graphics
    

    def GetActorRepresentationText(self):
        ReturnValue = self.mMapText
    

    def GetActorRepresentationTexture(self):
        ReturnValue = MapCompass_Icon_Spelevator
    

    def GetActorRepresentationType(self):
        ReturnValue = 8
    

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
        ReturnValue = 80000
    

    def GetActorFogOfWarRevealType(self):
        ReturnValue = 1
    

    def GetActorShouldShowOnMap(self):
        ReturnValue = True
    

    def GetRealActorLocation(self):
        ReturnValue: Vector = self.K2_GetActorLocation()
        ReturnValue_0: Vector = ReturnValue
    

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
        ExecuteUbergraph_Build_SpaceElevator.K2Node_Event_newColor = NewColor #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Build_SpaceElevator(258)
    

    def CamShake_01(self):
        self.ExecuteUbergraph_Build_SpaceElevator(263)
    

    def CamShake_02(self):
        self.ExecuteUbergraph_Build_SpaceElevator(839)
    

    def CamShake_03(self):
        self.ExecuteUbergraph_Build_SpaceElevator(844)
    

    def CamShake_04(self):
        self.ExecuteUbergraph_Build_SpaceElevator(849)
    

    def UpperlineVisible(self):
        self.ExecuteUbergraph_Build_SpaceElevator(854)
    

    def Event_StartSound(self):
        self.ExecuteUbergraph_Build_SpaceElevator(893)
    

    def ReceiveBeginPlay(self):
        self.ExecuteUbergraph_Build_SpaceElevator(1001)
    

    def OnPhaseChanged(self, gamePhase: uint8):
        ExecuteUbergraph_Build_SpaceElevator.K2Node_CustomEvent_gamePhase = gamePhase #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Build_SpaceElevator(1148)
    

    def PlayUpgradeSequence(self):
        self.ExecuteUbergraph_Build_SpaceElevator(1167)
    

    def Event_SE_SendOff(self):
        self.ExecuteUbergraph_Build_SpaceElevator(1498)
    

    def ReceiveDestroyed(self):
        self.ExecuteUbergraph_Build_SpaceElevator(1503)
    

    def ReceiveEndPlay(self):
        ExecuteUbergraph_Build_SpaceElevator.K2Node_Event_EndPlayReason = EndPlayReason #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Build_SpaceElevator(1724)
    

    def ExecuteUbergraph_Build_SpaceElevator(self):
        # Label 10
        ReturnValue: bool = self.HasAuthority()
        if not ReturnValue:
            goto('L1748')
        ReturnValue_0: Ptr[FGGamePhaseManager] = Default__FGGamePhaseManager.Get(self)
        OutputDelegate.BindUFunction(self, OnPhaseChanged)
        ReturnValue_0.mOnGamePhaseChanged.AddUnique(OutputDelegate)
        self.SM_SpaceElevator_MidPart_01.SetVisibility(True, False)
        self.SpaceElevator_Elevator_LOD0_static.SetVisibility(True, False)
        self.SM_SpaceElevator_MidPart_02.SetVisibility(True, False)
        # End
        # End
        ReturnValue_1: Vector = self.SpaceElevator_skl.GetSocketLocation("Root")
        Default__GameplayStatics.PlayWorldCameraShake(self, SpelevatorImpact_01, ReturnValue_1, 0, 10000, 1, 2, False)
        # End
        # Label 407
        ReturnValue_1 = self.SpaceElevator_skl.GetSocketLocation("Root")
        Default__GameplayStatics.PlayWorldCameraShake(self, SpelevatorImpact_02, ReturnValue_1, 0, 8000, 1, 2, False)
        # End
        # Label 551
        ReturnValue1: Vector = self.SpaceElevator_skl.GetSocketLocation("Root")
        Default__GameplayStatics.PlayWorldCameraShake(self, SpelevatorImpact_04, ReturnValue1, 0, 8000, 1, 2.5, False)
        # End
        # Label 695
        ReturnValue1 = self.SpaceElevator_skl.GetSocketLocation("Root")
        Default__GameplayStatics.PlayWorldCameraShake(self, SpelevatorImpact_03, ReturnValue1, 0, 8000, 1, 3, False)
        # End
        goto('L407')
        goto('L695')
        goto('L551')
        self.UpperLine.SetVisibility(True, False)
        # End
        ReturnValue_2: Ptr[Actor] = self.SpaceElevator_skl.GetOwner()
        ReturnValue1_0: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_SpaceElevator_StartUp_TestVersion, ReturnValue_2, True)
        # End
        self.ReceiveBeginPlay()
        ReturnValue_3: bool = self.AddAsRepresentation()
        goto('L10')
        # Label 1040
        ReturnValue_2 = self.SpaceElevator_skl.GetOwner()
        ReturnValue_4: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_SpaceElevator_SendOff, ReturnValue_2, True)
        # End
        self.PlayUpgradeSequence()
        # End
        
        OutActor = None
        ReturnValue_5: Ptr[LevelSequencePlayer] = Default__LevelSequencePlayer.CreateLevelSequencePlayer(self, SpaceElevatorSendOff, MovieSceneSequencePlaybackSettings(bAutoPlay = False, LoopCount = MovieSceneSequenceLoopCount(Value = 0), PlayRate = 1, StartTime = 0, bRandomStartTime = False, bRestoreState = False, bDisableMovementInput = False, bDisableLookAtInput = False, bHidePlayer = False, bHideHud = False, bDisableCameraCuts = False, bPauseAtEnd = False), Ref[OutActor])
        self.mSendOffSequence = OutActor
        Array: Const[List[Ptr[Actor]]] = [self]
        
        self.mSendOffSequence.SetBinding(MovieSceneObjectBindingID(SequenceID = 0, Space = 1, Guid = Guid(A = 1996000994, B = 1219085466, C = -68230497, D = -1298024804)), False, Ref[Array])
        Array1: List[Ptr[Actor]] = [self]
        self.mSendOffSequence.SetEventReceivers(Array1)
        ReturnValue_5.Play()
        # End
        goto('L1040')
        self.ReceiveDestroyed()
        ReturnValue1_1: Ptr[Actor] = self.SpaceElevator_skl.GetOwner()
        ReturnValue2: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Stop_SpaceElevator_StartUp_TestVersion, ReturnValue1_1, True)
        ReturnValue1_1 = self.SpaceElevator_skl.GetOwner()
        ReturnValue3: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Stop_SpaceElevator_SendOff, ReturnValue1_1, True)
        # End
        ReturnValue_6: bool = self.RemoveAsRepresentation()
    
