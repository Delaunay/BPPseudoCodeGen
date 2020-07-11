
from codegen.ue4_stub import *

from Script.FactoryGame import FGAmbientSettings

class Waterfall_Large_Body(FGAmbientSettings):
    mOnEnterOuterVolumeEvent = Namespace(AssetPath='/Game/FactoryGame/World/Environment/Audio/AmbientZones/_Shared/Waterfalls/Play_A_Waterfall_Large.Play_A_Waterfall_Large')
    mOnExitOuterVolumeEvent = Namespace(AssetPath='/Game/FactoryGame/World/Environment/Audio/AmbientZones/_Shared/Waterfalls/Stop_A_Waterfall_Large.Stop_A_Waterfall_Large')
    
