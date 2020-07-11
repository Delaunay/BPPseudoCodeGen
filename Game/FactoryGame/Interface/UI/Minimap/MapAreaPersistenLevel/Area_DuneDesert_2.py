
from codegen.ue4_stub import *

from Script.FactoryGame import FGMapArea

class Area_DuneDesert_2(FGMapArea):
    mDisplayName = NSLOCTEXT("", "4FB9F63844434F31F639D0A231137B58", "DuneDesert_2")
    mZoneType = NewObject[Zone_Dune]()
    
