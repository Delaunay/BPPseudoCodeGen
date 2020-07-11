
from codegen.ue4_stub import *

from Script.FactoryGame import FGAmbientSettings

class World_GeneralWinds_AnimatedWind(FGAmbientSettings):
    mOnEnterInnerVolumeEvent = Namespace(AssetPath='/Game/FactoryGame/World/Environment/Audio/AmbientZones/_Shared/Winds/Play_Ambience_AnimatedWind_Stereo.Play_Ambience_AnimatedWind_Stereo')
    mOnExitInnerVolumeEvent = Namespace(AssetPath='/Game/FactoryGame/World/Environment/Audio/AmbientZones/_Shared/Winds/Stop_Ambience_AnimatedWind_Stereo.Stop_Ambience_AnimatedWind_Stereo')
    
