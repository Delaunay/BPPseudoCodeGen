
from codegen.ue4_stub import *

from Script.FactoryGame import FGAmbientSettings

class AS_TitanForest_River(FGAmbientSettings):
    mOnEnterOuterVolumeEvent = Namespace(AssetPath='/Game/FactoryGame/World/Environment/Audio/AmbientZones/_Shared/Lakes/Play_Env_Rivers_Faster_Stereo.Play_Env_Rivers_Faster_Stereo')
    mOnExitOuterVolumeEvent = Namespace(AssetPath='/Game/FactoryGame/World/Environment/Audio/AmbientZones/_Shared/Lakes/Stop_Env_Rivers_Faster_Stereo.Stop_Env_Rivers_Faster_Stereo')
    mIgnoreListenerRotation = True
    
