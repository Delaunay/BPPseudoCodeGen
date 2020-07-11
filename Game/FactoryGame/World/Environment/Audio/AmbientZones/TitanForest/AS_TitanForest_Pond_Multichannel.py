
from codegen.ue4_stub import *

from Script.FactoryGame import FGAmbientSettings

class AS_TitanForest_Pond_Multichannel(FGAmbientSettings):
    mOnEnterOuterVolumeEvent = Namespace(AssetPath='/Game/FactoryGame/World/Environment/Audio/AmbientZones/TitanForest/Play_TitanForest_WaterBirdInsects_Stereo.Play_TitanForest_WaterBirdInsects_Stereo')
    mOnExitOuterVolumeEvent = Namespace(AssetPath='/Game/FactoryGame/World/Environment/Audio/AmbientZones/TitanForest/Stop_TitanForest_WaterBirdInsects_Stereo.Stop_TitanForest_WaterBirdInsects_Stereo')
    mOnEnterInnerVolumeEvent = Namespace(AssetPath='/Game/FactoryGame/World/Environment/Audio/AmbientZones/TitanForest/Play_TitanForest_WaterBirdInsects_MC.Play_TitanForest_WaterBirdInsects_MC')
    mOnExitInnerVolumeEvent = Namespace(AssetPath='/Game/FactoryGame/World/Environment/Audio/AmbientZones/TitanForest/Stop_TitanForest_WaterBirdInsects_MC.Stop_TitanForest_WaterBirdInsects_MC')
    mIgnoreListenerRotation = True
    
