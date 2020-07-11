
from codegen.ue4_stub import *

from Script.FactoryGame import FGAmbientSettings

class AS_StagnantWater(FGAmbientSettings):
    mOnEnterOuterVolumeEvent = Namespace(AssetPath='/Game/FactoryGame/World/Environment/Audio/AmbientZones/_Shared/Lakes/Play_W_Water_Stagnant_Pond.Play_W_Water_Stagnant_Pond')
    mOnExitOuterVolumeEvent = Namespace(AssetPath='/Game/FactoryGame/World/Environment/Audio/AmbientZones/_Shared/Lakes/Stop_W_Water_Stagnant_Pond.Stop_W_Water_Stagnant_Pond')
    
