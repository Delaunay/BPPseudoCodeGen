
from codegen.ue4_stub import *

from Script.FactoryGame import FGEquipmentChild

class EquipChild_JumpingStilts(FGEquipmentChild):
    mAttachSocket = jumpingstilt_rSocket
    bOnlyRelevantToOwner = True
    bNetUseOwnerRelevancy = True
    bReplicates = True
    RemoteRole = 1
    
