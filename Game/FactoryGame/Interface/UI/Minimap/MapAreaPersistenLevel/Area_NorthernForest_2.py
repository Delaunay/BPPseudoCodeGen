
from codegen.ue4_stub import *

from Script.FactoryGame import FGMapArea

class Area_NorthernForest_2(FGMapArea):
    mDisplayName = NSLOCTEXT("", "77D066804AF690E8F95E709EF3C091F0", "Northern Forest 2")
    mZoneType = NewObject[Zone_NorthernForest]()
    
