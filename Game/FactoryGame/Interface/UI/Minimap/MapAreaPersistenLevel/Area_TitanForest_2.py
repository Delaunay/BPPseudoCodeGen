
from codegen.ue4_stub import *

from Script.FactoryGame import FGMapArea

class Area_TitanForest_2(FGMapArea):
    mDisplayName = NSLOCTEXT("", "64A753A84E450757578780B64D0EA7AC", "Titan Forest 2")
    mZoneType = NewObject[Zone_TitanForest]()
    
