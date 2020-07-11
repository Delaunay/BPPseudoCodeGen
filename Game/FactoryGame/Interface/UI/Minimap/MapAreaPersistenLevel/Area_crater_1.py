
from codegen.ue4_stub import *

from Script.FactoryGame import FGMapArea

class Area_crater_1(FGMapArea):
    mDisplayName = NSLOCTEXT("", "6EB7B2D447272CC0A08126B3C62FDF3D", "Crater 1")
    mZoneType = NewObject[Zone_CraterLakes]()
    
