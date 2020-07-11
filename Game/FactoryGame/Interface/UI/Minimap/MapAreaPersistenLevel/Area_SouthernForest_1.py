
from codegen.ue4_stub import *

from Script.FactoryGame import FGMapArea

class Area_SouthernForest_1(FGMapArea):
    mDisplayName = NSLOCTEXT("", "30CBC36C4EC82F6B616ED89F1ABF9DA5", "Southern Forest 1")
    mZoneType = NewObject[Zone_SouthernForest]()
    
