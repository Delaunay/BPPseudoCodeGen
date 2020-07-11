
from codegen.ue4_stub import *

from Script.FactoryGame import FGMapArea

class Area_Swamp_2(FGMapArea):
    mDisplayName = NSLOCTEXT("", "1C98EF4546ADBAF7AA80FCB143265A1F", "Swamp 2")
    mZoneType = NewObject[Zone_Swamp]()
    
