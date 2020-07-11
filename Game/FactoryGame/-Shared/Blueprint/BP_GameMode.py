
from codegen.ue4_stub import *

from Game.FactoryGame.-Shared.Blueprint.BP_GameModeBase import BP_GameModeBase

class BP_GameMode(BP_GameModeBase):
    mLastAutosaveId = 255
    mDefaultRemoteCallObjectsClassNames = [{'AssetPathName': '/Game/FactoryGame/Character/Player/BP_RemoteCallObject.BP_RemoteCallObject_C', 'SubPathString': ''}]
    mServerRestartTimeHours = 24
    mSkipTutorialInPIE = True
    GameSessionClass = NewObject[FGGameSession]()
    GameStateClass = NewObject[BP_GameState]()
    PlayerControllerClass = NewObject[BP_PlayerController]()
    PlayerStateClass = NewObject[BP_PlayerState]()
    HUDClass = NewObject[BP_HUD]()
    DefaultPawnClass = NewObject[Char_Player]()
    PrimaryActorTick = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=False, bStartWithTickEnabled=True, bTickEvenWhenPaused=False)
    
