
from codegen.ue4_stub import *

from Game.FactoryGame.Interface.UI.InGame.MAMTree.BPW_MAMTree_Ingame import ExecuteUbergraph_BPW_MAMTree_Ingame.K2Node_Event_IsDesignTime
from Game.FactoryGame.Interface.UI.InGame.MAMTree.BPW_MAMTree_Ingame import ExecuteUbergraph_BPW_MAMTree_Ingame
from Game.FactoryGame.Interface.UI.InGame.MAMTree.Widget_MAMTree_Grid import Widget_MAMTree_Grid

class BPW_MAMTree_Ingame(Widget_MAMTree_Grid):
    mMAMState: bool
    
    def PreConstruct(self):
        ExecuteUbergraph_BPW_MAMTree_Ingame.K2Node_Event_IsDesignTime = IsDesignTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BPW_MAMTree_Ingame(10)
    

    def ExecuteUbergraph_BPW_MAMTree_Ingame(self):
        self.SetupCavases(self.mGridCanvas, self.mNodeCanvas, self.mRoads)
    
