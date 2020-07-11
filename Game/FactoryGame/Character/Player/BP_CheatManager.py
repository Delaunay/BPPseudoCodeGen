
from codegen.ue4_stub import *

from Script.FactoryGame import FGCheatManager

class BP_CheatManager(FGCheatManager):
    DebugCameraControllerClass = NewObject[BP_DebugCameraController]()
    
