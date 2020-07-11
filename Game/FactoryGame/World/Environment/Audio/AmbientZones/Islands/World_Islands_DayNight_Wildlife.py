
from codegen.ue4_stub import *

from Script.FactoryGame import FGAmbientSettings

class World_Islands_DayNight_Wildlife(FGAmbientSettings):
    mOnEnterOuterVolumeEvent = Namespace(AssetPath='/Game/FactoryGame/World/Environment/Audio/AmbientZones/Islands/Play_Islands_Wildlife_Outer.Play_Islands_Wildlife_Outer')
    mOnExitOuterVolumeEvent = Namespace(AssetPath='/Game/FactoryGame/World/Environment/Audio/AmbientZones/Islands/Stop_Islands_Wildlife_Outer.Stop_Islands_Wildlife_Outer')
    mOnEnterInnerVolumeEvent = Namespace(AssetPath='/Game/FactoryGame/World/Environment/Audio/AmbientZones/Islands/Play_Islands_Wildlife_Inner.Play_Islands_Wildlife_Inner')
    mOnExitInnerVolumeEvent = Namespace(AssetPath='/Game/FactoryGame/World/Environment/Audio/AmbientZones/Islands/Stop_Islands_Wildlife_Inner.Stop_Islands_Wildlife_Inner')
    
