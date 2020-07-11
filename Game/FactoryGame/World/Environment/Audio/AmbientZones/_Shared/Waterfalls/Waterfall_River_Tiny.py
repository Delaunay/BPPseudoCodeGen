
from codegen.ue4_stub import *

from Script.FactoryGame import FGAmbientSettings

class Waterfall_River_Tiny(FGAmbientSettings):
    mOnEnterOuterVolumeEvent = Namespace(AssetPath='/Game/FactoryGame/World/Environment/Audio/AmbientZones/_Shared/Waterfalls/Play_W_WaterFall_Small_Bottom.Play_W_WaterFall_Small_Bottom')
    mOnExitOuterVolumeEvent = Namespace(AssetPath='/Game/FactoryGame/World/Environment/Audio/AmbientZones/_Shared/Waterfalls/Stop_W_WaterFall_Small_Bottom.Stop_W_WaterFall_Small_Bottom')
    
