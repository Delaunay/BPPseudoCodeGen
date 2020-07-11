
from codegen.ue4_stub import *

from Script.FactoryGame import FGGameMode

class BP_GameModeBase(FGGameMode):
    mLastAutosaveId = 255
    mDefaultRemoteCallObjectsClassNames = [{'AssetPathName': '/Game/FactoryGame/Character/Player/BP_RemoteCallObject.BP_RemoteCallObject_C', 'SubPathString': ''}]
    mServerRestartTimeHours = 24
    mSkipTutorialInPIE = True
    InactivePlayerStateLifeSpan = 300
    GameStateClass = NewObject[GameState]()
    PlayerStateClass = NewObject[PlayerState]()
    HUDClass = NewObject[HUD]()
    DefaultPawnClass = NewObject[DefaultPawn]()
    PrimaryActorTick = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=False, bStartWithTickEnabled=True, bTickEvenWhenPaused=False)
    
