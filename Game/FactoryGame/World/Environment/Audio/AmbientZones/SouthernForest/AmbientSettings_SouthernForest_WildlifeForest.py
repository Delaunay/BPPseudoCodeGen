
from codegen.ue4_stub import *

from Script.FactoryGame import FGAmbientSettings

class AmbientSettings_SouthernForest_WildlifeForest(FGAmbientSettings):
    mOnEnterOuterVolumeEvent = Namespace(AssetPath='/Game/FactoryGame/World/Environment/Audio/AmbientZones/SouthernForest/Play_WildlifeForest_Outer.Play_WildlifeForest_Outer')
    mOnExitOuterVolumeEvent = Namespace(AssetPath='/Game/FactoryGame/World/Environment/Audio/AmbientZones/SouthernForest/Stop_WildlifeForest_Outer.Stop_WildlifeForest_Outer')
    mOnEnterInnerVolumeEvent = Namespace(AssetPath='/Game/FactoryGame/World/Environment/Audio/AmbientZones/SouthernForest/Play_WildlifeForest_Inner.Play_WildlifeForest_Inner')
    mOnExitInnerVolumeEvent = Namespace(AssetPath='/Game/FactoryGame/World/Environment/Audio/AmbientZones/SouthernForest/Stop_WildlifeForest_Inner.Stop_WildlifeForest_Inner')
    
