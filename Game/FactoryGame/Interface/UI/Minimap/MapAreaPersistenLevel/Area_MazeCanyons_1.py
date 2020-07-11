
from codegen.ue4_stub import *

from Script.FactoryGame import FGMapArea

class Area_MazeCanyons_1(FGMapArea):
    mDisplayName = NSLOCTEXT("", "563367D942F5047DE8B61EBB265017FA", "Maze Canyons 1")
    mZoneType = NewObject[Zone_MazeCanyons]()
    
