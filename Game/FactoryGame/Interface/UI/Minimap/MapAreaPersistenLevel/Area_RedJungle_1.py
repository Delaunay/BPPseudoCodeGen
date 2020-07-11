
from codegen.ue4_stub import *

from Script.FactoryGame import FGMapArea

class Area_RedJungle_1(FGMapArea):
    mDisplayName = NSLOCTEXT("", "E1B662534AE424BE225E12AF6CAAE330", "Red Jungle 1")
    mZoneType = NewObject[Zone_RedJungle]()
    
