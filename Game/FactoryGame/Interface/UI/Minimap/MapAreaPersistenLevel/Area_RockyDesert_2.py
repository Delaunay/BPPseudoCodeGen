
from codegen.ue4_stub import *

from Script.FactoryGame import FGMapArea

class Area_RockyDesert_2(FGMapArea):
    mDisplayName = NSLOCTEXT("", "C17944AB465C17F39232988B381EA786", "Rocky desert 2")
    mZoneType = NewObject[Zone_RockyDesert]()
    
