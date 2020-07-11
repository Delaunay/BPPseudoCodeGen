
from codegen.ue4_stub import *

from Script.FactoryGame import FGMapArea

class Area_DuneDesert_1(FGMapArea):
    mDisplayName = NSLOCTEXT("", "E504A7284D0B3D7FFE9493827A6F0789", "DuneDesert_1")
    mZoneType = NewObject[Zone_Dune]()
    
