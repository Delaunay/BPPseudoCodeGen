
from codegen.ue4_stub import *

from Script.FactoryGame import FGAmbientSettings

class AbyssDrone(FGAmbientSettings):
    mOnEnterOuterVolumeEvent = Namespace(AssetPath='/Game/FactoryGame/World/Environment/Audio/AmbientZones/AbyssCliffs/Play_AbyssDrone_Inner.Play_AbyssDrone_Inner')
    mOnExitOuterVolumeEvent = Namespace(AssetPath='/Game/FactoryGame/World/Environment/Audio/AmbientZones/AbyssCliffs/Stop_AbyssDrone_Inner.Stop_AbyssDrone_Inner')
    
