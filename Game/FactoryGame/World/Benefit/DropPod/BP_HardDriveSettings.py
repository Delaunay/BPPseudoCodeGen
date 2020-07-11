
from codegen.ue4_stub import *

from Script.FactoryGame import FGHardDriveSettings

class BP_HardDriveSettings(FGHardDriveSettings):
    mUniqueItemCount = 3
    mFallbackReturnItem = Namespace(ItemClass='/Game/FactoryGame/Resource/Environment/CrashSites/Desc_HardDrive.Desc_HardDrive_C', amount=1)
    mHardDriveResearchSchematic = NewObject[Research_HardDrive_0]()
    
