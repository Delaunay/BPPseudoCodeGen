
from codegen.ue4_stub import *

from Script.FactoryGame import FGAmbientSettings

class AS_World_SeaAtmos(FGAmbientSettings):
    mOnEnterOuterVolumeEvent = Namespace(AssetPath='/Game/FactoryGame/World/Environment/Audio/AmbientZones/_Shared/Lakes/Play_A_SeaAtmos_Mono_Outer.Play_A_SeaAtmos_Mono_Outer')
    mOnExitOuterVolumeEvent = Namespace(AssetPath='/Game/FactoryGame/World/Environment/Audio/AmbientZones/_Shared/Lakes/Stop_A_SeaAtmos_Mono_Outer.Stop_A_SeaAtmos_Mono_Outer')
    mOnEnterInnerVolumeEvent = Namespace(AssetPath='/Game/FactoryGame/World/Environment/Audio/AmbientZones/_Shared/Lakes/Play_A_SeaAtmos_Quad_Inner.Play_A_SeaAtmos_Quad_Inner')
    mOnExitInnerVolumeEvent = Namespace(AssetPath='/Game/FactoryGame/World/Environment/Audio/AmbientZones/_Shared/Lakes/Stop_A_SeaAtmos_Quad_Inner.Stop_A_SeaAtmos_Quad_Inner')
    
