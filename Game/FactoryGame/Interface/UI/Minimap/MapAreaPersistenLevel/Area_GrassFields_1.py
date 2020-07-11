
from codegen.ue4_stub import *

from Script.FactoryGame import FGMapArea

class Area_GrassFields_1(FGMapArea):
    mDisplayName = NSLOCTEXT("", "A51C8F6949E95F7811F7DA93F5F2CC8D", "Grass Fields 1")
    mZoneType = NewObject[Zone_GrassFields]()
    
