
from codegen.ue4_stub import *

from Script.FactoryGame import FGMapArea

class Area_RedBambooFields_1(FGMapArea):
    mDisplayName = NSLOCTEXT("", "2502A9594C39C006BC6FAD9E7DD6373B", "Red Bamboo Fields 1")
    mZoneType = NewObject[Zone_RedBambooFields]()
    
