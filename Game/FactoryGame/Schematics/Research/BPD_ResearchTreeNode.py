
from codegen.ue4_stub import *

from Game.FactoryGame.Interface.UI.InGame.MAMTree.MAMTree_NodeData_Struct import MAMTree_NodeData_Struct
from Script.FactoryGame import FGResearchTreeNode

class BPD_ResearchTreeNode(FGResearchTreeNode):
    mNodeDataStruct: MAMTree_NodeData_Struct
    
