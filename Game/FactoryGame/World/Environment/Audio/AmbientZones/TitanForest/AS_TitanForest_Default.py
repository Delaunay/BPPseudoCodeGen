
from codegen.ue4_stub import *

from Script.FactoryGame import FGAmbientSettings

class AS_TitanForest_Default(FGAmbientSettings):
    mOnEnterOuterVolumeEvent = Namespace(AssetPath='/Game/FactoryGame/World/Environment/Audio/AmbientZones/TitanForest/Play_TitanForest_Default.Play_TitanForest_Default')
    mOnExitOuterVolumeEvent = Namespace(AssetPath='/Game/FactoryGame/World/Environment/Audio/AmbientZones/TitanForest/Stop_TitanForest_Default.Stop_TitanForest_Default')
    mOnEnterInnerVolumeEvent = Namespace(AssetPath='/Game/FactoryGame/World/Environment/Audio/AmbientZones/TitanForest/Play_TitanForest_Default_WildLife.Play_TitanForest_Default_WildLife')
    mOnExitInnerVolumeEvent = Namespace(AssetPath='/Game/FactoryGame/World/Environment/Audio/AmbientZones/TitanForest/Stop_TitanForest_Default_WildLife.Stop_TitanForest_Default_WildLife')
    mIgnoreListenerRotation = True
    
