
from codegen.ue4_stub import *

from Script.FactoryGame import FGMapArea

class Area_LakeForest_1(FGMapArea):
    mDisplayName = NSLOCTEXT("", "B5B7F1AF4C9984503352C5B5E3AE26AD", "Lake Forest 1")
    mZoneType = NewObject[Zone_LakeForest]()
    
