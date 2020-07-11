
from codegen.ue4_stub import *

from Script.LevelSequence import LevelSequenceActor
from Script.Engine import SetVisibility
from Game.FactoryGame.Buildable.Factory.SpaceElevator.Animation.SpaceElevatorActivate import SpaceElevatorActivate
from Script.Engine import SetPosition
from Game.FactoryGame.Buildable.Factory.-Shared.BP_MaterialEffect_Build import OnEnded
from Script.LevelSequence import SetEventReceivers
from Script.MovieScene import Play
from Script.MovieScene import MovieSceneSequencePlaybackSettings
from Game.FactoryGame.Buildable.Factory.SpaceElevator.BP_MaterialEffect_SpaceElevator import ExecuteUbergraph_BP_MaterialEffect_SpaceElevator
from Script.MovieScene import MovieSceneObjectBindingID
from Script.LevelSequence import LevelSequencePlayer
from Script.LevelSequence import Default__LevelSequencePlayer
from Game.FactoryGame.Buildable.Factory.-Shared.BP_MaterialEffect_Build import BP_MaterialEffect_Build
from Script.LevelSequence import CreateLevelSequencePlayer
from Game.FactoryGame.Buildable.Factory.SpaceElevator.Build_SpaceElevator import Build_SpaceElevator
from Script.Engine import Actor
from Script.MovieScene import MovieSceneSequenceLoopCount
from Script.LevelSequence import SetBinding
from Script.Engine import GetOwner
from Script.CoreUObject import Guid
from Script.FactoryGame import FGBuildableSpaceElevator
from Game.FactoryGame.Buildable.Factory.-Shared.BP_MaterialEffect_Build import OnStarted

class BP_MaterialEffect_SpaceElevator(BP_MaterialEffect_Build):
    mSpaceElevatorSequence_0: Ptr[LevelSequenceActor]
    mAutoDestroy = True
    PrimaryComponentTick = Namespace(EndTickGroup=0, TickGroup=2, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=False, bTickEvenWhenPaused=False)
    bAutoActivate = True
    
    def OnEnded(self):
        self.ExecuteUbergraph_BP_MaterialEffect_SpaceElevator(496)
    

    def OnStarted(self):
        self.ExecuteUbergraph_BP_MaterialEffect_SpaceElevator(511)
    

    def ExecuteUbergraph_BP_MaterialEffect_SpaceElevator(self):
        # Label 10
        ReturnValue: Ptr[Actor] = self.GetOwner()
        Elevator: Ptr[FGBuildableSpaceElevator] = Cast[FGBuildableSpaceElevator](ReturnValue)
        bSuccess: bool = Elevator
        if not bSuccess:
            goto('L935')
        
        OutActor = None
        ReturnValue_0: Ptr[LevelSequencePlayer] = Default__LevelSequencePlayer.CreateLevelSequencePlayer(self, SpaceElevatorActivate, MovieSceneSequencePlaybackSettings(bAutoPlay = False, LoopCount = MovieSceneSequenceLoopCount(Value = 0), PlayRate = 1, StartTime = 0, bRandomStartTime = False, bRestoreState = False, bDisableMovementInput = False, bDisableLookAtInput = False, bHidePlayer = False, bHideHud = False, bDisableCameraCuts = False, bPauseAtEnd = False), Ref[OutActor])
        self.mSpaceElevatorSequence_0 = OutActor
        ReturnValue1: Ptr[Actor] = self.GetOwner()
        Array1: Const[List[Ptr[Actor]]] = [ReturnValue1]
        
        self.mSpaceElevatorSequence_0.SetBinding(MovieSceneObjectBindingID(SequenceID = 0, Space = 1, Guid = Guid(A = -1492792065, B = 1217100001, C = -2126895984, D = -1709368131)), False, Ref[Array1])
        ReturnValue1 = self.GetOwner()
        Array: List[Ptr[Actor]] = [ReturnValue1]
        self.mSpaceElevatorSequence_0.SetEventReceivers(Array)
        ReturnValue_0.Play()
        # End
        self.OnEnded()
        goto('L10')
        self.OnStarted()
        ReturnValue2: Ptr[Actor] = self.GetOwner()
        Elevator1: Ptr[FGBuildableSpaceElevator] = Cast[FGBuildableSpaceElevator](ReturnValue2)
        bSuccess1: bool = Elevator1
        if not bSuccess1:
            goto('L935')
        Elevator_0: Ptr[Build_SpaceElevator] = Cast[Build_SpaceElevator](Elevator1)
        bSuccess2: bool = Elevator_0
        if not bSuccess2:
            goto('L935')
        Elevator_0.SpaceElevator_skl.SetPosition(0, False)
        Elevator_0.SpaceElevator_arm02.SetPosition(0, False)
        Elevator_0.SpaceElevator_arm03.SetPosition(0, False)
        Elevator_0.UpperLine.SetVisibility(False, False)
    
