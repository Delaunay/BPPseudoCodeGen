
from codegen.ue4_stub import *

from Script.FactoryGame import FGAmbientSettings

class Rivers_Thick_Calm(FGAmbientSettings):
    mOnEnterOuterVolumeEvent = Namespace(AssetPath='/Game/FactoryGame/World/Environment/Audio/AmbientZones/_Shared/Rivers/Play_Env_Rivers_Thick_Stereo.Play_Env_Rivers_Thick_Stereo')
    mOnExitOuterVolumeEvent = Namespace(AssetPath='/Game/FactoryGame/World/Environment/Audio/AmbientZones/_Shared/Rivers/Stop_Env_Rivers_Thick_Stereo.Stop_Env_Rivers_Thick_Stereo')
    
