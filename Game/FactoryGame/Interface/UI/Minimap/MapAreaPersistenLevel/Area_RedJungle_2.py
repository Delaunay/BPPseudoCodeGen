
from codegen.ue4_stub import *

from Script.FactoryGame import FGMapArea

class Area_RedJungle_2(FGMapArea):
    mDisplayName = NSLOCTEXT("", "F7105F594285FB8F76DF19BD06601B36", "Red Jungle 2")
    mZoneType = NewObject[Zone_RedJungle]()
    
