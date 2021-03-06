﻿
from codegen.ue4_stub import *

from Script.FactoryGame import FGAmbientSettings

class Zone_WesternDuneForest_Rare(FGAmbientSettings):
    mOnEnterOuterVolumeEvent = Namespace(AssetPath='/Game/FactoryGame/World/Environment/Audio/AmbientZones/_Shared/Wild/Play_Zone_WesternDuneForest_Rare_Mono_Outer.Play_Zone_WesternDuneForest_Rare_Mono_Outer')
    mOnExitOuterVolumeEvent = Namespace(AssetPath='/Game/FactoryGame/World/Environment/Audio/AmbientZones/_Shared/Wild/Stop_Zone_WesternDuneForest_Rare_Mono_Outer.Stop_Zone_WesternDuneForest_Rare_Mono_Outer')
    mOnEnterInnerVolumeEvent = Namespace(AssetPath='/Game/FactoryGame/World/Environment/Audio/AmbientZones/_Shared/Wild/Play_WDForest_Rare_Quad_Inner.Play_WDForest_Rare_Quad_Inner')
    mOnExitInnerVolumeEvent = Namespace(AssetPath='/Game/FactoryGame/World/Environment/Audio/AmbientZones/_Shared/Wild/Stop_WDForest_Rare_Quad_Inner.Stop_WDForest_Rare_Quad_Inner')
    
