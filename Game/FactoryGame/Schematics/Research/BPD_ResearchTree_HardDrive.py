
from codegen.ue4_stub import *

from Script.FactoryGame import FGResearchTree

class BPD_ResearchTree_HardDrive(FGResearchTree):
    mPreUnlockDisplayName = NSLOCTEXT("", "A8CD7C8845D0DE9E07F1B6836E9DD932", "Hard Drive")
    mDisplayName = NSLOCTEXT("", "FC25E10849DAFA58724BF4927CD707B4", "Hard Drive")
    mPreUnlockDescription = NSLOCTEXT("", "31B92F394E9F3A04E6EE4C8A71F8E376", "Multiple FICSIT property shipments have been... misplaced on the planet MASSAGE-2(AB)b. Retrieval of resources and potential production data is recommended.")
    mPostUnlockDescription = NSLOCTEXT("", "28FECDE046232FC174325384F21D3D8C", "These misplaced FICSIT hard-drivers hold valuable data on alternative resource production. Examination to salvage their content is highly recommended. ")
    mResearchTreeIcon = Namespace(DrawAs=3, ImageSize={'X': 256, 'Y': 256}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$AssetPath': '/Game/FactoryGame/Resource/Environment/CrashSites/UI/HardDrive_256.HardDrive_256'}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    mUnlockDependencies = [{'$ObjectClass': '/Game/FactoryGame/AvailabilityDependencies/BP_ItemPickedUpDependency.BP_ItemPickedUpDependency_C', '$ObjectFlags': 2621481, '$ObjectName': 'BP_ItemPickedUpDependency_C_0', 'mItems': ['/Game/FactoryGame/Resource/Environment/CrashSites/Desc_HardDrive.Desc_HardDrive_C']}]
    
