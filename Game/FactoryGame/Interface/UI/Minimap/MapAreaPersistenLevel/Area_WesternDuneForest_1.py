
from codegen.ue4_stub import *

from Script.FactoryGame import FGMapArea

class Area_WesternDuneForest_1(FGMapArea):
    mDisplayName = NSLOCTEXT("", "B48B1F0B439791590CE55CABFC25045D", "Western Dune Forest 1")
    mZoneType = NewObject[Zone_WesternDuneForest]()
    
