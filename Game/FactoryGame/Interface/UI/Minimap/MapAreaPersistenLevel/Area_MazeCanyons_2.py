
from codegen.ue4_stub import *

from Script.FactoryGame import FGMapArea

class Area_MazeCanyons_2(FGMapArea):
    mDisplayName = NSLOCTEXT("", "BB6827A34FE4F8E443ECDBB6303B5865", "Maze Canyons 2")
    mZoneType = NewObject[Zone_MazeCanyons]()
    
