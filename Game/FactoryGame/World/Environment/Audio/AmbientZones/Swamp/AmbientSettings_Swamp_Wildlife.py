
from codegen.ue4_stub import *

from Script.FactoryGame import FGAmbientSettings

class AmbientSettings_Swamp_Wildlife(FGAmbientSettings):
    mOnEnterOuterVolumeEvent = Namespace(AssetPath='/Game/FactoryGame/World/Environment/Audio/AmbientZones/Swamp/Play_Zone_Swamp_Wildlife_Outer.Play_Zone_Swamp_Wildlife_Outer')
    mOnExitOuterVolumeEvent = Namespace(AssetPath='/Game/FactoryGame/World/Environment/Audio/AmbientZones/Swamp/Stop_Zone_Swamp_Wildlife_Outer.Stop_Zone_Swamp_Wildlife_Outer')
    mOnEnterInnerVolumeEvent = Namespace(AssetPath='/Game/FactoryGame/World/Environment/Audio/AmbientZones/Swamp/Play_Zone_Swamp_Wildlife_Inner.Play_Zone_Swamp_Wildlife_Inner')
    mOnExitInnerVolumeEvent = Namespace(AssetPath='/Game/FactoryGame/World/Environment/Audio/AmbientZones/Swamp/Stop_Zone_Swamp_Wildlife_Inner.Stop_Zone_Swamp_Wildlife_Inner')
    
