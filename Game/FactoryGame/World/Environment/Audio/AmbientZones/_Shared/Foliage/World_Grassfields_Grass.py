
from codegen.ue4_stub import *

from Script.FactoryGame import FGAmbientSettings

class World_Grassfields_Grass(FGAmbientSettings):
    mOnEnterOuterVolumeEvent = Namespace(AssetPath='/Game/FactoryGame/World/Environment/Audio/AmbientZones/_Shared/Foliage/Play_Zone_GrassFields_Grass_Stereo_Outer.Play_Zone_GrassFields_Grass_Stereo_Outer')
    mOnExitOuterVolumeEvent = Namespace(AssetPath='/Game/FactoryGame/World/Environment/Audio/AmbientZones/_Shared/Foliage/Stop_Zone_GrassFields_Grass_Stereo_Outer.Stop_Zone_GrassFields_Grass_Stereo_Outer')
    mOnEnterInnerVolumeEvent = Namespace(AssetPath='/Game/FactoryGame/World/Environment/Audio/AmbientZones/_Shared/Foliage/Play_Zone_GrassFields_Grass_Quad.Play_Zone_GrassFields_Grass_Quad')
    mOnExitInnerVolumeEvent = Namespace(AssetPath='/Game/FactoryGame/World/Environment/Audio/AmbientZones/_Shared/Foliage/Stop_Zone_GrassFields_Grass_Quad.Stop_Zone_GrassFields_Grass_Quad')
    
