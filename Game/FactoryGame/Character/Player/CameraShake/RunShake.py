
from codegen.ue4_stub import *

from Script.Engine import CameraShake

class RunShake(CameraShake):
    bSingleInstance = True
    AnimScale = 1.25
    Anim = Namespace(AssetPath='/Game/FactoryGame/Character/Player/CameraShake/Sprint_01_CameraAnim.Sprint_01_CameraAnim')
    
