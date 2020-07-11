
from codegen.ue4_stub import *

from Script.FactoryGame import FGMapArea

class Area_Savanna_2(FGMapArea):
    mDisplayName = NSLOCTEXT("", "7108C6594E569A0CC151FE9E4F974AF0", "Savanna 2")
    mZoneType = NewObject[Zone_RockyDesert]()
    
