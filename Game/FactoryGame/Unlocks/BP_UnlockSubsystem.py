
from codegen.ue4_stub import *

from Script.FactoryGame import FGUnlockSubsystem

class BP_UnlockSubsystem(FGUnlockSubsystem):
    mMapUnlockedMessage = NewObject[Tutorial_Map]()
    mNumTotalInventorySlots = 16
    mNumTotalArmEquipmentSlots = 1
    bAlwaysRelevant = True
    bReplicates = True
    RemoteRole = 1
    
