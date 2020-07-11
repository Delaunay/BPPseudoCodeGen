
from codegen.ue4_stub import *

from Script.FactoryGame import FGMapArea

class Area_EasternDuneForest_1(FGMapArea):
    mDisplayName = NSLOCTEXT("", "D6DC3FBA41D9E20DA426DFB512C60FAB", "Eastern Dune Forest 1")
    mZoneType = NewObject[Zone_EasternDuneForest]()
    
