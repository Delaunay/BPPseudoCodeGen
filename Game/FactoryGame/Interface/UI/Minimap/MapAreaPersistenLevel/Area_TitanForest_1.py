
from codegen.ue4_stub import *

from Script.FactoryGame import FGMapArea

class Area_TitanForest_1(FGMapArea):
    mDisplayName = NSLOCTEXT("", "40F0D55344C809E5ED761E9CF3D2E9EE", "Titan Forest 1")
    mZoneType = NewObject[Zone_TitanForest]()
    
