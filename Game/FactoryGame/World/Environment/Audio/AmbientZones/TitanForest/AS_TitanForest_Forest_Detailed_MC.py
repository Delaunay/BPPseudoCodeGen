
from codegen.ue4_stub import *

from Script.FactoryGame import FGAmbientSettings

class AS_TitanForest_Forest_Detailed_MC(FGAmbientSettings):
    mOnEnterOuterVolumeEvent = Namespace(AssetPath='/Game/FactoryGame/World/Environment/Audio/AmbientZones/TitanForest/Play_TitanForest_Tropic_Birds_Drops_Stereo.Play_TitanForest_Tropic_Birds_Drops_Stereo')
    mOnExitOuterVolumeEvent = Namespace(AssetPath='/Game/FactoryGame/World/Environment/Audio/AmbientZones/TitanForest/Stop_TitanForest_Tropic_Birds_Drops_Stereo.Stop_TitanForest_Tropic_Birds_Drops_Stereo')
    mOnEnterInnerVolumeEvent = Namespace(AssetPath='/Game/FactoryGame/World/Environment/Audio/AmbientZones/TitanForest/Play_TitanForest_Tropic_Birds_Drops_MC.Play_TitanForest_Tropic_Birds_Drops_MC')
    mOnExitInnerVolumeEvent = Namespace(AssetPath='/Game/FactoryGame/World/Environment/Audio/AmbientZones/TitanForest/Stop_TitanForest_Tropic_Birds_Drops_MC.Stop_TitanForest_Tropic_Birds_Drops_MC')
    mIgnoreListenerRotation = True
    
