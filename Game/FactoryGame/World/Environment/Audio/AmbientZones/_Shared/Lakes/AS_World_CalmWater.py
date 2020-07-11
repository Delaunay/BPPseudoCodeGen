
from codegen.ue4_stub import *

from Script.FactoryGame import FGAmbientSettings

class AS_World_CalmWater(FGAmbientSettings):
    mOnEnterOuterVolumeEvent = Namespace(AssetPath='/Game/FactoryGame/World/Environment/Audio/AmbientZones/_Shared/Lakes/Play_A_Water_Calm_Stereo.Play_A_Water_Calm_Stereo')
    mOnExitOuterVolumeEvent = Namespace(AssetPath='/Game/FactoryGame/World/Environment/Audio/AmbientZones/_Shared/Lakes/Stop_A_Water_Calm_Stereo.Stop_A_Water_Calm_Stereo')
    
