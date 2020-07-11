
from codegen.ue4_stub import *

from Script.FactoryGame import FGMapArea

class Area_NorthernForest_1(FGMapArea):
    mDisplayName = NSLOCTEXT("", "D5DF2C384BF0285273385CBB3CEC377A", "Northern Forest 1")
    mZoneType = NewObject[Zone_NorthernForest]()
    
