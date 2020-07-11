
from codegen.ue4_stub import *

from Script.FactoryGame import FGMapArea

class Area_LakeForest_2(FGMapArea):
    mDisplayName = NSLOCTEXT("", "FCF01F9A478555E93684F3BB2377056B", "Lake Forest 2")
    mZoneType = NewObject[Zone_LakeForest]()
    
