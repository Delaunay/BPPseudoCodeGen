
from codegen.ue4_stub import *

from Script.FactoryGame import FGMapArea

class Area_AbyssCliffs_1(FGMapArea):
    mDisplayName = NSLOCTEXT("", "7542F00F48F8AD0758091B805BE5411A", "Abyss Cliffs 1")
    mZoneType = NewObject[Zone_AbyssCliffs]()
    
