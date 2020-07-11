
from codegen.ue4_stub import *

from Script.FactoryGame import FGMapArea

class Area_GrassFields_2(FGMapArea):
    mDisplayName = NSLOCTEXT("", "E84CA98C4EF173057658708344E2FD7C", "Grass Fields 2")
    mZoneType = NewObject[Zone_GrassFields]()
    
