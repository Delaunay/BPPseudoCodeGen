
from codegen.ue4_stub import *

from Game.FactoryGame.-Shared.Blueprint.BP_GameModeBase import BP_GameModeBase

class BP_GameModeMenu(BP_GameModeBase):
    mLastAutosaveId = 255
    mDefaultRemoteCallObjectsClassNames = [{'AssetPathName': '/Game/FactoryGame/Character/Player/BP_RemoteCallObject.BP_RemoteCallObject_C', 'SubPathString': ''}]
    mServerRestartTimeHours = 24
    mSkipTutorialInPIE = True
    mIsMainMenu = True
    GameSessionClass = NewObject[FGGameSession]()
    PlayerControllerClass = NewObject[FGPlayerControllerBase]()
    HUDClass = NewObject[BP_MenuHUD]()
    PrimaryActorTick = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=False, bStartWithTickEnabled=True, bTickEvenWhenPaused=False)
    
