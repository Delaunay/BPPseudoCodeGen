
from codegen.ue4_stub import *

from Script.FactoryGame import FGMapArea

class Area_Swamp_1(FGMapArea):
    mDisplayName = NSLOCTEXT("", "03C059644ABE9C512445F58FA84E8218", "Swamp 1")
    mZoneType = NewObject[Zone_Swamp]()
    
