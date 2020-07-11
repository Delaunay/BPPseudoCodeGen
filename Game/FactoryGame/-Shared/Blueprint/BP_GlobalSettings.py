
from codegen.ue4_stub import *

from Script.FactoryGame import FGGlobalSettings

class BP_GlobalSettings(FGGlobalSettings):
    mResourceSettings = NewObject[BP_ResourceSettings]()
    mFactorySettings = NewObject[BP_FactorySettings]()
    mDropPodSettings = NewObject[BP_DropPodSettings]()
    mHardDriveSettings = NewObject[BP_HardDriveSettings]()
    mEnvironmentSettings = NewObject[BP_EnvironmentSettings]()
    mSubsystemClasses = NewObject[BP_SubsystemClasses]()
    mSignSettings = NewObject[BP_SignSettings]()
    mGlobalSettingsClassName = Namespace(AssetPathName='/Game/FactoryGame/-Shared/Blueprint/BP_GlobalSettings.BP_GlobalSettings_C', SubPathString='')
    
