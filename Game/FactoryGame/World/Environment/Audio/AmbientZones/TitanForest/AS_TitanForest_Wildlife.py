
from codegen.ue4_stub import *

from Script.FactoryGame import FGAmbientSettings

class AS_TitanForest_Wildlife(FGAmbientSettings):
    mOnEnterOuterVolumeEvent = Namespace(AssetPath='/Game/FactoryGame/World/Environment/Audio/AmbientZones/TitanForest/Play_Zone_TitanForest_Wildlife_Outer.Play_Zone_TitanForest_Wildlife_Outer')
    mOnExitOuterVolumeEvent = Namespace(AssetPath='/Game/FactoryGame/World/Environment/Audio/AmbientZones/TitanForest/Stop_Zone_TitanForest_WildlifeLoop_Quad_Outer.Stop_Zone_TitanForest_WildlifeLoop_Quad_Outer')
    mOnEnterInnerVolumeEvent = Namespace(AssetPath='/Game/FactoryGame/World/Environment/Audio/AmbientZones/TitanForest/Play_Zone_TitanForest_Wildlife_Inner.Play_Zone_TitanForest_Wildlife_Inner')
    mOnExitInnerVolumeEvent = Namespace(AssetPath='/Game/FactoryGame/World/Environment/Audio/AmbientZones/TitanForest/Stop_Zone_TitanForest_WildlifeLoop_Quad_Inner.Stop_Zone_TitanForest_WildlifeLoop_Quad_Inner')
    
