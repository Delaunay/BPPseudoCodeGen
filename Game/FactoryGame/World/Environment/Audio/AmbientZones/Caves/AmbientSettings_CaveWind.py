
from codegen.ue4_stub import *

from Script.FactoryGame import FGAmbientSettings

class AmbientSettings_CaveWind(FGAmbientSettings):
    mOnEnterOuterVolumeEvent = Namespace(AssetPath='/Game/FactoryGame/World/Environment/Audio/AmbientZones/Caves/Play_Winds_CaveWind_Stereo_Outer.Play_Winds_CaveWind_Stereo_Outer')
    mOnExitOuterVolumeEvent = Namespace(AssetPath='/Game/FactoryGame/World/Environment/Audio/AmbientZones/Caves/Stop_Winds_CaveWind_Stereo_Outer.Stop_Winds_CaveWind_Stereo_Outer')
    mOnEnterInnerVolumeEvent = Namespace(AssetPath='/Game/FactoryGame/World/Environment/Audio/AmbientZones/Caves/Play_Winds_CaveWind_Stereo_Inner.Play_Winds_CaveWind_Stereo_Inner')
    mOnExitInnerVolumeEvent = Namespace(AssetPath='/Game/FactoryGame/World/Environment/Audio/AmbientZones/Caves/Stop_Winds_CaveWind_Stereo_Inner.Stop_Winds_CaveWind_Stereo_Inner')
    
