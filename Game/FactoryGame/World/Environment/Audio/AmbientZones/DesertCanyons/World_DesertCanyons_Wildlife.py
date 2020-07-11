
from codegen.ue4_stub import *

from Script.FactoryGame import FGAmbientSettings

class World_DesertCanyons_Wildlife(FGAmbientSettings):
    mOnEnterOuterVolumeEvent = Namespace(AssetPath='/Game/FactoryGame/World/Environment/Audio/AmbientZones/DesertCanyons/Play_DesertCanyons_Wildlife_Outer.Play_DesertCanyons_Wildlife_Outer')
    mOnExitOuterVolumeEvent = Namespace(AssetPath='/Game/FactoryGame/World/Environment/Audio/AmbientZones/DesertCanyons/Stop_DesertCanyons_Wildlife_Outer.Stop_DesertCanyons_Wildlife_Outer')
    mOnEnterInnerVolumeEvent = Namespace(AssetPath='/Game/FactoryGame/World/Environment/Audio/AmbientZones/DesertCanyons/Play_DesertCanyons_Wildlife_Inner.Play_DesertCanyons_Wildlife_Inner')
    mOnExitInnerVolumeEvent = Namespace(AssetPath='/Game/FactoryGame/World/Environment/Audio/AmbientZones/DesertCanyons/Stop_DesertCanyons_Wildlife_Inner.Stop_DesertCanyons_Wildlife_Inner')
    
