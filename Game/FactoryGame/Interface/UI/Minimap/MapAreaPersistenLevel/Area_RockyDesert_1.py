
from codegen.ue4_stub import *

from Script.FactoryGame import FGMapArea

class Area_RockyDesert_1(FGMapArea):
    mDisplayName = NSLOCTEXT("", "6CFAD2594FA4A76136AD0CA7311397C1", "Rocky desert 1")
    mZoneType = NewObject[Zone_RockyDesert]()
    
