
from codegen.ue4_stub import *

from Script.FactoryGame import FGAmbientSettings

class Zone_Savanna_Wildlife_Cricket(FGAmbientSettings):
    mOnEnterOuterVolumeEvent = Namespace(AssetPath='/Game/FactoryGame/World/Environment/Audio/AmbientZones/_Shared/Wild/Play_Wildlife_CricketLoop_St_Outer.Play_Wildlife_CricketLoop_St_Outer')
    mOnExitOuterVolumeEvent = Namespace(AssetPath='/Game/FactoryGame/World/Environment/Audio/AmbientZones/_Shared/Wild/Stop_Wildlife_CricketLoop_St_Outer.Stop_Wildlife_CricketLoop_St_Outer')
    mOnEnterInnerVolumeEvent = Namespace(AssetPath='/Game/FactoryGame/World/Environment/Audio/AmbientZones/_Shared/Wild/Play_Wildlife_CricketLoop_St_Inner.Play_Wildlife_CricketLoop_St_Inner')
    mOnExitInnerVolumeEvent = Namespace(AssetPath='/Game/FactoryGame/World/Environment/Audio/AmbientZones/_Shared/Wild/Stop_Wildlife_CricketLoop_St_Inner.Stop_Wildlife_CricketLoop_St_Inner')
    
