
from codegen.ue4_stub import *

from Script.FactoryGame import FGResearchManager

class BP_ResearchManager(FGResearchManager):
    bAlwaysRelevant = True
    bReplicates = True
    RemoteRole = 1
    
