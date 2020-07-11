
from codegen.ue4_stub import *

from Script.FactoryGame import FGMapArea

class Area_crater_2(FGMapArea):
    mDisplayName = NSLOCTEXT("", "C70E90EE4C134FBA4061EEB62CADF25A", "Crater 2")
    mZoneType = NewObject[Zone_CraterLakes]()
    
