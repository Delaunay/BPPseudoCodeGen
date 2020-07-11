
from codegen.ue4_stub import *

from Script.FactoryGame import FGMapArea

class Area_WesternDuneForest_2(FGMapArea):
    mDisplayName = NSLOCTEXT("", "0213101041F7B55E0D1884BC8B41535B", "Western Dune Forest 2")
    mZoneType = NewObject[Zone_WesternDuneForest]()
    
