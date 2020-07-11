
from codegen.ue4_stub import *

from Script.FactoryGame import FGMapArea

class Area_DesertCanyons_2(FGMapArea):
    mDisplayName = NSLOCTEXT("", "28C4F32C4EB9A76291E69D8982C0A608", "Desert Canyons 2")
    mZoneType = NewObject[Zone_DesertCanyon]()
    
