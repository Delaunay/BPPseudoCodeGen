
from codegen.ue4_stub import *

from Script.FactoryGame import FGAmbientSettings

class AS_TitanForest_Forest_Clear_MC(FGAmbientSettings):
    mOnEnterOuterVolumeEvent = Namespace(AssetPath='/Game/FactoryGame/World/Environment/Audio/AmbientZones/TitanForest/Play_TitanForest_Dawn_chorus_Stereo.Play_TitanForest_Dawn_chorus_Stereo')
    mOnExitOuterVolumeEvent = Namespace(AssetPath='/Game/FactoryGame/World/Environment/Audio/AmbientZones/TitanForest/Stop_TitanForest_Dawn_chorus_Stereo.Stop_TitanForest_Dawn_chorus_Stereo')
    mOnEnterInnerVolumeEvent = Namespace(AssetPath='/Game/FactoryGame/World/Environment/Audio/AmbientZones/TitanForest/Play_TitanForest_Dawn_chorus_MC.Play_TitanForest_Dawn_chorus_MC')
    mOnExitInnerVolumeEvent = Namespace(AssetPath='/Game/FactoryGame/World/Environment/Audio/AmbientZones/TitanForest/Stop_TitanForest_Dawn_chorus_MC.Stop_TitanForest_Dawn_chorus_MC')
    mIgnoreListenerRotation = True
    
