
from codegen.ue4_stub import *

from Script.FactoryGame import FGAmbientSettings

class Zone_Savanna_Wildlife(FGAmbientSettings):
    mOnEnterOuterVolumeEvent = Namespace(AssetPath='/Game/FactoryGame/World/Environment/Audio/AmbientZones/Savanna/Play_Zone_Savanna_Wildlife_Outer.Play_Zone_Savanna_Wildlife_Outer')
    mOnExitOuterVolumeEvent = Namespace(AssetPath='/Game/FactoryGame/World/Environment/Audio/AmbientZones/Savanna/Stop_Zone_Savanna_Wildlife_Outer.Stop_Zone_Savanna_Wildlife_Outer')
    mOnEnterInnerVolumeEvent = Namespace(AssetPath='/Game/FactoryGame/World/Environment/Audio/AmbientZones/Savanna/Play_Zone_Savanna_Wildlife_Inner.Play_Zone_Savanna_Wildlife_Inner')
    mOnExitInnerVolumeEvent = Namespace(AssetPath='/Game/FactoryGame/World/Environment/Audio/AmbientZones/Savanna/Stop_Zone_Savanna_Wildlife_Inner.Stop_Zone_Savanna_Wildlife_Inner')
    
