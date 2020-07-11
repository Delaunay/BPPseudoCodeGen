
from codegen.ue4_stub import *

from Script.Engine import Default__KismetSystemLibrary
from Script.FactoryGame import OnExitOuterVolume
from Script.Engine import PrintString
from Script.FactoryGame import FGAmbientSettings
from Script.CoreUObject import LinearColor

class AS_Rivers_Big_Fast(FGAmbientSettings):
    mOnEnterOuterVolumeEvent = Namespace(AssetPath='/Game/FactoryGame/World/Environment/Audio/AmbientZones/_Shared/Rivers/Play_Env_Rivers_Big_Fast_Stereo.Play_Env_Rivers_Big_Fast_Stereo')
    mOnExitOuterVolumeEvent = Namespace(AssetPath='/Game/FactoryGame/World/Environment/Audio/AmbientZones/_Shared/Rivers/Stop_Env_Rivers_Fast_Stereo.Stop_Env_Rivers_Fast_Stereo')
    
    def OnExitOuterVolume(self):
        self.OnExitOuterVolume(ambientComponent)
        Default__KismetSystemLibrary.PrintString(ambientComponent, "Hello", True, True, LinearColor(R = 0, G = 0.6600000262260437, B = 1, A = 1), 2)
    
