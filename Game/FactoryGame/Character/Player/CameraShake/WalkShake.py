
from codegen.ue4_stub import *

from Script.Engine import CameraShake

class WalkShake(CameraShake):
    bSingleInstance = True
    AnimScale = 2
    Anim = Namespace(AssetPath='/Game/FactoryGame/Character/Player/CameraShake/Run_01_CameraAnim.Run_01_CameraAnim')
    
