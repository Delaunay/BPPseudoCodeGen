
from codegen.ue4_stub import *

from Script.MovieScene import PlayToFrame
from Script.MediaAssets import Close
from Script.MediaAssets import Play
from Script.FactoryGame import FGCharacterPlayer
from Script.MovieScene import GetEndTime
from Script.LevelSequence import SetEventReceivers
from Script.Engine import Default__KismetSystemLibrary
from Game.FactoryGame.Buildable.Factory.TradingPost.BP_StartingPod import ExecuteUbergraph_BP_StartingPod.K2Node_Event_byCharacter1
from Script.Engine import IsValid
from Script.FactoryGame import IntroDone
from Script.Engine import FlushNetDormancy
from Game.FactoryGame.-Shared.Audio.Music.JannikReuterberg.Resume_Music import Resume_Music
from Script.LevelSequence import CreateLevelSequencePlayer
from Game.FactoryGame.Interface.UI.HUDHelpers.HUDHelpers import Default__HUDHelpers
from Script.AkAudio import SetGlobalRTPCValue
from Script.CoreUObject import Guid
from Script.CoreUObject import LinearColor
from Script.FactoryGame import FGPlayerController
from Script.Engine import Controller
from Script.Engine import Pawn
from Game.FactoryGame.Buildable.Factory.TradingPost.BP_StartingPod import ExecuteUbergraph_BP_StartingPod.K2Node_Event_gameVersion
from Game.FactoryGame.Cinematics.DropPod.Sequence.DropPod_Intro_01 import DropPod_Intro_01
from Script.MovieScene import Play
from Game.FactoryGame.Cinematics.DropPod.Audio.Play_Cinematic_DropPod import Play_Cinematic_DropPod
from Script.Engine import HUD
from Script.MediaAssets import MediaPlayer
from Script.Engine import SkeletalMesh
from Script.CoreUObject import Object
from Script.Engine import GetHUD
from Script.MovieScene import MovieSceneObjectBindingID
from Game.FactoryGame.Character.Player.Char_Player import Char_Player
from Game.FactoryGame.Buildable.Factory.TradingPost.BP_StartingPod import ExecuteUbergraph_BP_StartingPod.K2Node_Event_gameVersion1
from Script.FactoryGame import FGActorRepresentationManager
from Script.AkAudio import Default__AkGameplayStatics
from Script.MovieScene import MovieSceneSequenceLoopCount
from Script.LevelSequence import SetBinding
from Script.AkAudio import AkComponent
from Script.FactoryGame import Default__FGTutorialIntroManager
from Script.CoreUObject import QualifiedFrameTime
from Script.Engine import PrintString
from Script.AkAudio import PostAkEvent
from Script.FactoryGame import CreateAndAddNewRepresentation
from Game.FactoryGame.-Shared.Audio.Music.JannikReuterberg.Pause_Music import Pause_Music
from Game.Movies.Satisfactory_Intro_01 import Satisfactory_Intro_01
from Script.Engine import LatentActionInfo
from Script.Engine import HasAuthority
from Script.FactoryGame import Get
from Script.Engine import GetController
from Script.FactoryGame import SetCanSkipTutorialIntro
from Script.Engine import LoadAsset
from Game.FactoryGame.Buildable.Factory.TradingPost.BP_StartingPod import ExecuteUbergraph_BP_StartingPod.K2Node_Event_saveVersion1
from Script.LevelSequence import LevelSequencePlayer
from Script.FactoryGame import Default__FGBlueprintFunctionLibrary
from Game.FactoryGame.Buildable.Factory.TradingPost.BP_StartingPod import ExecuteUbergraph_BP_StartingPod.K2Node_Event_saveVersion3
from Script.FactoryGame import GetRemoteCallObjectOfClass
from Game.FactoryGame.Buildable.Factory.TradingPost.BP_StartingPod import ExecuteUbergraph_BP_StartingPod.K2Node_Event_saveVersion2
from Script.FactoryGame import RemoveRepresentationOfActor
from Game.FactoryGame.Buildable.Factory.TradingPost.BP_StartingPod import ExecuteUbergraph_BP_StartingPod.K2Node_Event_gameVersion2
from Game.FactoryGame.Character.Player.BP_RemoteCallObject import BP_RemoteCallObject
from Script.FactoryGame import ShowOutline
from Script.LevelSequence import LevelSequenceActor
from Game.FactoryGame.Buildable.Factory.TradingPost.BP_StartingPod import ExecuteUbergraph_BP_StartingPod.K2Node_Event_saveVersion
from Script.FactoryGame import SetPartialPumpiMode
from Script.FactoryGame import GetCachedPlayer
from Game.FactoryGame.Buildable.Factory.TradingPost.BP_StartingPod import ExecuteUbergraph_BP_StartingPod.K2Node_Event_byCharacter
from Game.FactoryGame.Buildable.Factory.TradingPost.BP_StartingPod import ExecuteUbergraph_BP_StartingPod.K2Node_Event_newColor
from Game.FactoryGame.Buildable.Factory.TradingPost.BP_StartingPod import ExecuteUbergraph_BP_StartingPod.K2Node_Event_DeltaSeconds
from Script.MovieScene import MovieSceneSequencePlaybackSettings
from Script.Engine import ReceiveTick
from Game.FactoryGame.Buildable.Factory.TradingPost.BP_StartingPod import ExecuteUbergraph_BP_StartingPod.K2Node_Event_gameVersion3
from Script.Engine import K2_GetPawn
from Script.FactoryGame import FGTutorialIntroManager
from Game.FactoryGame.Cinematics.DropPod.Audio.Stop_Cinematic_DropPod import Stop_Cinematic_DropPod
from Script.FactoryGame import Default__FGActorRepresentationManager
from Script.FactoryGame import HideOutline
from Game.FactoryGame.-Shared.Audio.Blueprints.BP_MusicManager import BP_MusicManager
from Script.LevelSequence import GetSequencePlayer
from Game.FactoryGame.Interface.UI.Assets.Map.MapCompass_Icon_pod import MapCompass_Icon_pod
from Script.LevelSequence import Default__LevelSequencePlayer
from Script.CoreUObject import Vector
from Game.FactoryGame.Buildable.Factory.TradingPost.BP_StartingPod import ExecuteUbergraph_BP_StartingPod
from Script.FactoryGame import FGHUD
from Script.Engine import Actor
from Script.MediaAssets import OpenSource
from Script.Engine import K2_GetActorLocation
from Game.FactoryGame.Buildable.Factory.TradingPost.BP_StartingPod import ExecuteUbergraph_BP_StartingPod.K2Node_CustomEvent_Loaded
from Script.Engine import BreakQualifiedFrameTime
from Script.FactoryGame import FGStartingPod
from Script.MediaAssets import SetLooping

class BP_StartingPod(FGStartingPod):
    mCachedPC: Ptr[FGPlayerController]
    mStartingSequence: Ptr[LevelSequenceActor]
    mVideoPlayer: Ptr[MediaPlayer] = Namespace(AssetPath='/Game/Cinematics/Cutscenes/Intro_01/CutScenePlayer.CutScenePlayer')
    mMusicManager: Ptr[BP_MusicManager]
    mMapText: FText = NSLOCTEXT("", "5D4CDB9C43CDE82CE2C6E3A884BDE4EB", "Starting Pod")
    SkeletalMeshPtr: TSoftObjectPtr[SkeletalMesh] = NewObject[DropPod_skl]()
    mDismantleStacks = [{'Item': {'ItemClass': '/Game/FactoryGame/Resource/Parts/HUBParts/Desc_HUBParts.Desc_HUBParts_C', 'ItemState': {'ActorPtr': {'$Empty': True}}}, 'NumItems': 1}]
    mDropPodMesh = Namespace(AnimClass='/Game/FactoryGame/Buildable/Factory/DropPod/Anim_DropPod.Anim_DropPod_C', AnimationData={'AnimToPlay': {'$AssetPath': '/Game/FactoryGame/Buildable/Factory/DropPod/Animation/DropPodIdle_01.DropPodIdle_01'}, 'bSavedLooping': False, 'bSavedPlaying': False, 'SavedPosition': 0, 'SavedPlayRate': 1}, AttachParent={'$ObjectClass': '/Script/Engine.SceneComponent', '$ObjectFlags': 2883617, '$ObjectName': 'DefaultSceneRoot'}, BodyInstance={'ObjectType': 0, 'CollisionEnabled': 0, 'SleepFamily': 'ESleepFamily::Normal', 'DOFMode': 0, 'bUseCCD': False, 'bNotifyRigidBodyCollision': False, 'bSimulatePhysics': False, 'bOverrideMass': False, 'bEnableGravity': False, 'bAutoWeld': False, 'bStartAwake': True, 'bGenerateWakeEvents': False, 'bUpdateMassWhenScaleChanges': False, 'bLockTranslation': True, 'bLockRotation': True, 'bLockXTranslation': False, 'bLockYTranslation': False, 'bLockZTranslation': False, 'bLockXRotation': False, 'bLockYRotation': False, 'bLockZRotation': False, 'bOverrideMaxAngularVelocity': False, 'bOverrideMaxDepenetrationVelocity': False, 'bOverrideWalkableSlopeOnInstance': False, 'bInterpolateWhenSubStepping': True, 'CollisionProfileName': 'NoCollision', 'CollisionResponses': {'ResponseArray': [{'Channel': 'WorldStatic', 'Response': 0}, {'Channel': 'WorldDynamic', 'Response': 0}, {'Channel': 'Pawn', 'Response': 0}, {'Channel': 'Visibility', 'Response': 0}, {'Channel': 'Camera', 'Response': 0}, {'Channel': 'PhysicsBody', 'Response': 0}, {'Channel': 'Vehicle', 'Response': 0}, {'Channel': 'Destructible', 'Response': 0}, {'Channel': 'Projectile', 'Response': 0}, {'Channel': 'Resource', 'Response': 0}]}, 'MaxDepenetrationVelocity': 0, 'MassInKgOverride': 100, 'LinearDamping': 0.009999999776482582, 'AngularDamping': 0, 'CustomDOFPlaneNormal': {'X': 0, 'Y': 0, 'Z': 0}, 'COMNudge': {'X': 0, 'Y': 0, 'Z': 0}, 'MassScale': 1, 'InertiaTensorScale': {'X': 1, 'Y': 1, 'Z': 1}, 'WalkableSlopeOverride': {'WalkableSlopeBehavior': 0, 'WalkableSlopeAngle': 0}, 'PhysMaterialOverride': {'$Empty': True}, 'MaxAngularVelocity': 3600, 'CustomSleepThresholdMultiplier': 1, 'StabilizationThresholdMultiplier': 1, 'PhysicsBlendWeight': 0, 'PositionSolverIterationCount': 8, 'VelocitySolverIterationCount': 1}, ClothingSimulationFactory='/Script/ClothingSystemRuntime.ClothingSimulationFactoryNv', ObjectClass='/Script/Engine.SkeletalMeshComponent', ObjectFlags=2883617, ObjectName='DropPod Mesh', bComponentUseFixedSkelBounds=True, bEnableUpdateRateOptimizations=False, mFOV=90)
    PrimaryActorTick = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=True, bTickEvenWhenPaused=False)
    bReplicates = True
    InputPriority = 100
    RootComponent = Namespace(ObjectClass='/Script/Engine.SceneComponent', ObjectFlags=2883617, ObjectName='DefaultSceneRoot')
    
    def GatherDependencies(self):
        dependentObjects: List[Ptr[Object]] = List[ObjectProperty /Game/FactoryGame/Buildable/Factory/TradingPost/BP_StartingPod.BP_StartingPod_C:GatherDependencies.out_dependentObjects.out_dependentObjects]([])
    

    def NeedTransform(self):
        ReturnValue = True
    

    def ShouldSave(self):
        ReturnValue = True
    

    def GetActorCompassViewDistance(self):
        ReturnValue = 4
    

    def SetActorCompassViewDistance(self):
        ReturnValue = 0
    

    def SetActorRepresentationText(self):
        self.FlushNetDormancy()
        self.mMapText = newText
        ReturnValue = self.mMapText
    

    def UpdateRepresentation(self):
        ReturnValue = False
    

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
        ReturnValue = self.mMapText
    

    def GetActorRepresentationTexture(self):
        ReturnValue = MapCompass_Icon_pod
    

    def GetActorRepresentationType(self):
        ReturnValue = 9
    

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
    

    def OnLoaded_8586F6D040F0FFE03962849F398DB59A(self, Loaded: Ptr[Object]):
        ExecuteUbergraph_BP_StartingPod.K2Node_CustomEvent_Loaded = Loaded #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_StartingPod(3784)
    

    def PostLoadGame(self):
        ExecuteUbergraph_BP_StartingPod.K2Node_Event_saveVersion3 = SaveVersion #  PERSISTENT_FRAME(
        ExecuteUbergraph_BP_StartingPod.K2Node_Event_gameVersion3 = GameVersion #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_StartingPod(1313)
    

    def PostSaveGame(self):
        ExecuteUbergraph_BP_StartingPod.K2Node_Event_saveVersion2 = SaveVersion #  PERSISTENT_FRAME(
        ExecuteUbergraph_BP_StartingPod.K2Node_Event_gameVersion2 = GameVersion #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_StartingPod(1314)
    

    def PreLoadGame(self):
        ExecuteUbergraph_BP_StartingPod.K2Node_Event_saveVersion1 = SaveVersion #  PERSISTENT_FRAME(
        ExecuteUbergraph_BP_StartingPod.K2Node_Event_gameVersion1 = GameVersion #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_StartingPod(1315)
    

    def PreSaveGame(self):
        ExecuteUbergraph_BP_StartingPod.K2Node_Event_saveVersion = SaveVersion #  PERSISTENT_FRAME(
        ExecuteUbergraph_BP_StartingPod.K2Node_Event_gameVersion = GameVersion #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_StartingPod(1316)
    

    def SetActorRepresentationColor(self):
        ExecuteUbergraph_BP_StartingPod.K2Node_Event_newColor = NewColor #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_StartingPod(1317)
    

    def StartIsLookedAtForDismantle(self):
        ExecuteUbergraph_BP_StartingPod.K2Node_Event_byCharacter1 = byCharacter #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_StartingPod(1318)
    

    def StopIsLookedAtForDismantle(self):
        ExecuteUbergraph_BP_StartingPod.K2Node_Event_byCharacter = byCharacter #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_StartingPod(1362)
    

    def ReceiveTick(self):
        ExecuteUbergraph_BP_StartingPod.K2Node_Event_DeltaSeconds = DeltaSeconds #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_StartingPod(1404)
    

    def SetupPodForOwner(self):
        self.ExecuteUbergraph_BP_StartingPod(1622)
    

    def SetupPodForObserver(self):
        self.ExecuteUbergraph_BP_StartingPod(1898)
    

    def EndCinematic(self):
        self.ExecuteUbergraph_BP_StartingPod(1948)
    

    def StartMovie(self):
        self.ExecuteUbergraph_BP_StartingPod(3346)
    

    def AK_StopDucking(self):
        self.ExecuteUbergraph_BP_StartingPod(3351)
    

    def AK_HalveDucking(self):
        self.ExecuteUbergraph_BP_StartingPod(3407)
    

    def ReceiveDestroyed(self):
        self.ExecuteUbergraph_BP_StartingPod(3576)
    

    def StartCinematic(self):
        self.ExecuteUbergraph_BP_StartingPod(3581)
    

    def OnPlayerSkipIntroSequence(self):
        self.ExecuteUbergraph_BP_StartingPod(3620)
    

    def AllowSkipIntro(self):
        self.ExecuteUbergraph_BP_StartingPod(3625)
    

    def BlockSkipIntro(self):
        self.ExecuteUbergraph_BP_StartingPod(3702)
    

    def ReceiveBeginPlay(self):
        self.ExecuteUbergraph_BP_StartingPod(3779)
    

    def ExecuteUbergraph_BP_StartingPod(self):
        goto(ComputedJump("EntryPoint"))
        # Label 15
        self.mDropPodMesh.SetSkeletalMesh(None, True)
        ReturnValue: bool = self.RemoveAsRepresentation()
        goto(ExecutionFlow.Pop())
        # Label 78
        if not Variable:
            goto('L93')
        goto(ExecutionFlow.Pop())
        # Label 93
        Variable: bool = True
        self.SetupPodForObserver()
        goto(ExecutionFlow.Pop())
        # Label 119
        Variable = True
        goto(ExecutionFlow.Pop())
        # Label 131
        if not Variable1:
            goto('L146')
        # Label 145
        goto(ExecutionFlow.Pop())
        # Label 146
        Variable1: bool = True
        self.SetupPodForOwner()
        goto(ExecutionFlow.Pop())
        # Label 172
        Variable_0: bool = True
        if not False:
           goto(ExecutionFlow.Pop())
        goto('L119')
        # Label 190
        if not Variable_0:
            goto('L172')
        goto(ExecutionFlow.Pop())
        # Label 205
        Variable1 = True
        goto(ExecutionFlow.Pop())
        # Label 217
        ExecutionFlow.Push("L78")
        goto('L190')
        # Label 227
        self.SetOwner(self.mCachedPC)
        ReturnValue_0: Ptr[HUD] = self.mCachedPC.GetHUD()
        AsFGHUD: Ptr[FGHUD] = Cast[FGHUD](ReturnValue_0)
        bSuccess1: bool = AsFGHUD
        if not bSuccess1:
           goto(ExecutionFlow.Pop())
        AsFGHUD.SetPartialPumpiMode(True)
        
        OutActor = None
        ReturnValue_1: Ptr[LevelSequencePlayer] = Default__LevelSequencePlayer.CreateLevelSequencePlayer(self, DropPod_Intro_01, MovieSceneSequencePlaybackSettings(bAutoPlay = False, LoopCount = MovieSceneSequenceLoopCount(Value = 0), PlayRate = 1, StartTime = 0, bRandomStartTime = False, bRestoreState = False, bDisableMovementInput = False, bDisableLookAtInput = False, bHidePlayer = False, bHideHud = False, bDisableCameraCuts = False, bPauseAtEnd = False), Ref[OutActor])
        self.mStartingSequence = OutActor
        ReturnValue2: Ptr[FGCharacterPlayer] = self.GetCachedPlayer()
        Array: Const[List[Ptr[Actor]]] = [ReturnValue2]
        
        self.mStartingSequence.SetBinding(MovieSceneObjectBindingID(SequenceID = 0, Space = 1, Guid = Guid(A = -23011956, B = 1216166386, C = 1237473951, D = -1146401488)), False, Ref[Array])
        Array1: Const[List[Ptr[Actor]]] = [self]
        
        self.mStartingSequence.SetBinding(MovieSceneObjectBindingID(SequenceID = 0, Space = 1, Guid = Guid(A = 1348593567, B = 1263814946, C = -1937319039, D = -1440609462)), False, Ref[Array1])
        ReturnValue3: Ptr[FGCharacterPlayer] = self.GetCachedPlayer()
        Array2: List[Ptr[Actor]] = [self, ReturnValue3]
        self.mStartingSequence.SetEventReceivers(Array2)
        ReturnValue_1.Play()
        self.EnableInput(self.mCachedPC)
        ReturnValue1: bool = self.mVideoPlayer.OpenSource(Satisfactory_Intro_01)
        ReturnValue1_0: bool = self.mVideoPlayer.Play()
        ReturnValue1_1: bool = self.mVideoPlayer.SetLooping(False)
        Default__AkGameplayStatics.SetGlobalRTPCValue("StartSequence_Duck_Ambient", 1, 0)
        ReturnValue2_0: Ptr[Pawn] = self.mCachedPC.K2_GetPawn()
        ReturnValue3_0: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Pause_Music, ReturnValue2_0, True)
        ReturnValue_2: Ptr[Pawn] = self.mCachedPC.K2_GetPawn()
        ReturnValue1_2: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_Cinematic_DropPod, ReturnValue_2, True)
        goto(ExecutionFlow.Pop())
        goto(ExecutionFlow.Pop())
        goto(ExecutionFlow.Pop())
        goto(ExecutionFlow.Pop())
        goto(ExecutionFlow.Pop())
        goto(ExecutionFlow.Pop())
        Default__FGBlueprintFunctionLibrary.ShowOutline(self.mDropPodMesh, 254)
        goto(ExecutionFlow.Pop())
        Default__FGBlueprintFunctionLibrary.HideOutline(self.mDropPodMesh)
        goto(ExecutionFlow.Pop())
        self.ReceiveTick(DeltaSeconds)
        ReturnValue_3: Ptr[FGCharacterPlayer] = self.GetCachedPlayer()
        ReturnValue_4: bool = Default__KismetSystemLibrary.IsValid(ReturnValue_3)
        if not ReturnValue_4:
           goto(ExecutionFlow.Pop())
        ReturnValue_3 = self.GetCachedPlayer()
        ReturnValue_5: bool = ReturnValue_3.IsLocallyControlled()
        if not ReturnValue_5:
            goto('L217')
        ExecutionFlow.Push("L131")
        if not Variable1_0:
            goto('L1604')
        goto(ExecutionFlow.Pop())
        # Label 1604
        Variable1_0: bool = True
        if not False:
           goto(ExecutionFlow.Pop())
        goto('L205')
        self.Plane.SetCollisionEnabled(0)
        ReturnValue4: Ptr[FGCharacterPlayer] = self.GetCachedPlayer()
        ReturnValue4.CharacterMovement.GravityScale = 0
        ReturnValue1_3: Ptr[FGCharacterPlayer] = self.GetCachedPlayer()
        ReturnValue_6: Ptr[Controller] = ReturnValue1_3.GetController()
        Controller: Ptr[FGPlayerController] = Cast[FGPlayerController](ReturnValue_6)
        bSuccess: bool = Controller
        self.mCachedPC = Controller
        goto('L227')
        self.mDropPodMesh.SetCollisionProfileName("BlockAll")
        goto(ExecutionFlow.Pop())
        ReturnValue5: Ptr[FGCharacterPlayer] = self.GetCachedPlayer()
        ReturnValue5.CharacterMovement.GravityScale = 1
        ReturnValue_7: Ptr[FGTutorialIntroManager] = Default__FGTutorialIntroManager.Get(self)
        ReturnValue_7.IntroDone()
        ReturnValue_8: Ptr[BP_RemoteCallObject] = self.mCachedPC.GetRemoteCallObjectOfClass(BP_RemoteCallObject)
        ReturnValue_7 = Default__FGTutorialIntroManager.Get(self)
        ReturnValue_8.Server_UpdateTutorial(1, ReturnValue_7)
        self.mDropPodMesh.SetCollisionProfileName("BlockAll")
        self.mVideoPlayer.Close()
        self.DisableInput(self.mCachedPC)
        self.NewBuildingPing.SetActive(True, False)
        ReturnValue_9: bool = self.AddAsRepresentation()
        ReturnValue_10: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Resume_Music, self.mCachedPC, True)
        self.SetOwner(None)
        goto(ExecutionFlow.Pop())
        # Label 2494
        ReturnValue_11: bool = self.mVideoPlayer.SetLooping(False)
        Default__KismetSystemLibrary.PrintString(self, "startmovie", True, True, LinearColor(R = 0, G = 0.6600000262260437, B = 1, A = 1), 2)
        goto(ExecutionFlow.Pop())
        # Label 2624
        ReturnValue_12: Ptr[LevelSequencePlayer] = self.mStartingSequence.GetSequencePlayer()
        ReturnValue_13: QualifiedFrameTime = ReturnValue_12.GetEndTime()
        
        Frame = None
        FrameRate = None
        SubFrame = None
        BreakQualifiedFrameTime(Ref[ReturnValue_13], Ref[Frame], Ref[FrameRate], Ref[SubFrame])
        ReturnValue_14: float = SubFrame - 0
        FrameTime.FrameNumber = Frame
        FrameTime.SubFrame = ReturnValue_14
        ReturnValue_12.PlayToFrame(FrameTime)
        self.EndCinematic()
        ReturnValue3_1: Ptr[Pawn] = self.mCachedPC.K2_GetPawn()
        Player: Ptr[Char_Player] = Cast[Char_Player](ReturnValue3_1)
        bSuccess2: bool = Player
        if not bSuccess2:
           goto(ExecutionFlow.Pop())
        Player.SkipIntro()
        Default__AkGameplayStatics.SetGlobalRTPCValue("StartSequence_Duck_Ambient", 0, 1000)
        ReturnValue1_4: Ptr[Pawn] = self.mCachedPC.K2_GetPawn()
        ReturnValue2_1: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Stop_Cinematic_DropPod, ReturnValue1_4, True)
        goto(ExecutionFlow.Pop())
        # Label 3243
        ReturnValue_15: bool = self.mVideoPlayer.Play()
        goto('L2494')
        # Label 3290
        ReturnValue_16: bool = self.mVideoPlayer.OpenSource(Satisfactory_Intro_01)
        goto('L3243')
        goto('L3290')
        Default__AkGameplayStatics.SetGlobalRTPCValue("StartSequence_Duck_Ambient", 0, 6000)
        goto(ExecutionFlow.Pop())
        Default__AkGameplayStatics.SetGlobalRTPCValue("StartSequence_Duck_Ambient", 0.30000001192092896, 1000)
        goto(ExecutionFlow.Pop())
        # Label 3463
        OutputDelegate.BindUFunction(self, OnLoaded_8586F6D040F0FFE03962849F398DB59A)
        Default__KismetSystemLibrary.LoadAsset(self, self.SkeletalMeshPtr, OutputDelegate, LatentActionInfo(Linkage = -1, UUID = -1030975351, ExecutionFunction = "ExecuteUbergraph_BP_StartingPod", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        goto('L15')
        self.Plane.SetCollisionEnabled(3)
        goto(ExecutionFlow.Pop())
        goto('L2624')
        ReturnValue1_5: Ptr[FGTutorialIntroManager] = Default__FGTutorialIntroManager.Get(self)
        ReturnValue1_5.SetCanSkipTutorialIntro(True)
        goto(ExecutionFlow.Pop())
        ReturnValue2_2: Ptr[FGTutorialIntroManager] = Default__FGTutorialIntroManager.Get(self)
        ReturnValue2_2.SetCanSkipTutorialIntro(False)
        goto(ExecutionFlow.Pop())
        goto('L3463')
        Variable_1: Ptr[Object] = Loaded
        Mesh: Ptr[SkeletalMesh] = Cast[SkeletalMesh](Variable_1)
        bSuccess3: bool = Mesh
        if not bSuccess3:
           goto(ExecutionFlow.Pop())
        self.mDropPodMesh.SetSkeletalMesh(Mesh, True)
        goto(ExecutionFlow.Pop())
    
