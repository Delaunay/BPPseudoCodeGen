
from codegen.ue4_stub import *

from Script.FactoryGame import FGMapArea

class Area_GrassFields_3(FGMapArea):
    mDisplayName = NSLOCTEXT("", "D259CEA6447521A990214FA0FA8C1C52", "Grass Fields 3")
    mZoneType = NewObject[Zone_GrassFields]()
    
