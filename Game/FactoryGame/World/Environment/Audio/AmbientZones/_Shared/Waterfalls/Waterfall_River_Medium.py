
from codegen.ue4_stub import *

from Script.FactoryGame import FGAmbientSettings

class Waterfall_River_Medium(FGAmbientSettings):
    mOnEnterOuterVolumeEvent = Namespace(AssetPath='/Game/FactoryGame/World/Environment/Audio/AmbientZones/_Shared/Waterfalls/Play_W_Water_Waterfall_Pouring.Play_W_Water_Waterfall_Pouring')
    mOnExitOuterVolumeEvent = Namespace(AssetPath='/Game/FactoryGame/World/Environment/Audio/AmbientZones/_Shared/Waterfalls/Stop_W_Water_Waterfall_Pouring.Stop_W_Water_Waterfall_Pouring')
    
