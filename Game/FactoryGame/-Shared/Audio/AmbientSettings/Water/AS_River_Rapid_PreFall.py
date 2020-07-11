
from codegen.ue4_stub import *

from Script.FactoryGame import FGAmbientSettings

class AS_River_Rapid_PreFall(FGAmbientSettings):
    mOnEnterOuterVolumeEvent = Namespace(AssetPath='/Game/FactoryGame/World/Environment/Audio/AmbientZones/_Shared/Rivers/Play_W_Water_River_Wavy_Moving.Play_W_Water_River_Wavy_Moving')
    mOnExitOuterVolumeEvent = Namespace(AssetPath='/Game/FactoryGame/World/Environment/Audio/AmbientZones/_Shared/Rivers/Stop_W_Water_River_Wavy_Moving.Stop_W_Water_River_Wavy_Moving')
    
