
from codegen.ue4_stub import *

from Script.FactoryGame import FGMapArea

class Area_DesertCanyons_1(FGMapArea):
    mDisplayName = NSLOCTEXT("", "BD2DA5E541A430B111AE6F8E44D5CAAA", "Desert Canyons 1")
    mZoneType = NewObject[Zone_DesertCanyon]()
    
