
from codegen.ue4_stub import *

from Script.FactoryGame import FGMapArea

class Area_SouthernForest_2(FGMapArea):
    mDisplayName = NSLOCTEXT("", "75958B744A44279D702CEA96E2EA0484", "Southern Forest 2")
    mZoneType = NewObject[Zone_SouthernForest]()
    
