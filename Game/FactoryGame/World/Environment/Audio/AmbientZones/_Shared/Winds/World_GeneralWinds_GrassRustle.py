
from codegen.ue4_stub import *

from Script.FactoryGame import FGAmbientSettings

class World_GeneralWinds_GrassRustle(FGAmbientSettings):
    mOnEnterOuterVolumeEvent = Namespace(AssetPath='/Game/FactoryGame/World/Environment/Audio/AmbientZones/_Shared/Winds/Play_Winds_GrassRustle_Mono_Outer.Play_Winds_GrassRustle_Mono_Outer')
    mOnExitOuterVolumeEvent = Namespace(AssetPath='/Game/FactoryGame/World/Environment/Audio/AmbientZones/_Shared/Winds/Stop_Winds_GrassRustle_Mono_Outer.Stop_Winds_GrassRustle_Mono_Outer')
    mOnEnterInnerVolumeEvent = Namespace(AssetPath='/Game/FactoryGame/World/Environment/Audio/AmbientZones/_Shared/Winds/Play_Ambience_Winds_GrassRustle_Quad.Play_Ambience_Winds_GrassRustle_Quad')
    mOnExitInnerVolumeEvent = Namespace(AssetPath='/Game/FactoryGame/World/Environment/Audio/AmbientZones/_Shared/Winds/Stop_Ambience_Winds_GrassRustle_Quad.Stop_Ambience_Winds_GrassRustle_Quad')
    
