
from codegen.ue4_stub import *

from Script.FactoryGame import FGAmbientSettings

class World_AbyssCliffs_Debris(FGAmbientSettings):
    mOnEnterOuterVolumeEvent = Namespace(AssetPath='/Game/FactoryGame/World/Environment/Audio/AmbientZones/AbyssCliffs/Play_Zone_AbyssCliffs_Rocks_OS_Mono_Outer.Play_Zone_AbyssCliffs_Rocks_OS_Mono_Outer')
    mOnExitOuterVolumeEvent = Namespace(AssetPath='/Game/FactoryGame/World/Environment/Audio/AmbientZones/AbyssCliffs/Stop_Zone_AbyssCliffs_Rocks_OS_Mono_Outer.Stop_Zone_AbyssCliffs_Rocks_OS_Mono_Outer')
    mOnEnterInnerVolumeEvent = Namespace(AssetPath='/Game/FactoryGame/World/Environment/Audio/AmbientZones/AbyssCliffs/Play_AbyssCliffs_Debris_Inner.Play_AbyssCliffs_Debris_Inner')
    mOnExitInnerVolumeEvent = Namespace(AssetPath='/Game/FactoryGame/World/Environment/Audio/AmbientZones/AbyssCliffs/Stop_AbyssCliffs_Debris_Inner.Stop_AbyssCliffs_Debris_Inner')
    
