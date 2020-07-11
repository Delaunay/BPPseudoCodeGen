
from codegen.ue4_stub import *

from Script.FactoryGame import FGAmbientSettings

class World_AbyssCliffs_DayNight_Wildlife(FGAmbientSettings):
    mOnEnterOuterVolumeEvent = Namespace(AssetPath='/Game/FactoryGame/World/Environment/Audio/AmbientZones/AbyssCliffs/Play_DayNight_Wildlife_Outer.Play_DayNight_Wildlife_Outer')
    mOnExitOuterVolumeEvent = Namespace(AssetPath='/Game/FactoryGame/World/Environment/Audio/AmbientZones/AbyssCliffs/Stop_DayNight_Wildlife_Outer.Stop_DayNight_Wildlife_Outer')
    mOnEnterInnerVolumeEvent = Namespace(AssetPath='/Game/FactoryGame/World/Environment/Audio/AmbientZones/AbyssCliffs/Play_DayNight_Wildlife_Inner.Play_DayNight_Wildlife_Inner')
    mOnExitInnerVolumeEvent = Namespace(AssetPath='/Game/FactoryGame/World/Environment/Audio/AmbientZones/AbyssCliffs/Stop_DayNight_Wildlife_Inner.Stop_DayNight_Wildlife_Inner')
    
