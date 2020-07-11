
from codegen.ue4_stub import *

from Script.FactoryGame import FGMapArea

class Area_Savanna_1(FGMapArea):
    mDisplayName = NSLOCTEXT("", "686FDD014F15C17B67E02BAA53678183", "Savanna 1")
    mZoneType = NewObject[Zone_RockyDesert]()
    
