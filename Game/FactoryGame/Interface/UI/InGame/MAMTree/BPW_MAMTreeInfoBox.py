
from codegen.ue4_stub import *

from Script.UMG import UMGSequencePlayer
from Script.UMG import PlayAnimation
from Script.UMG import WidgetAnimation
from Game.FactoryGame.Interface.UI.InGame.MAMTree.BPW_MAMTreeInfoBox import ExecuteUbergraph_BPW_MAMTreeInfoBox
from Script.UMG import UserWidget

class BPW_MAMTreeInfoBox(UserWidget):
    SpawnAnim: Ptr[WidgetAnimation]
    
    def Construct(self):
        self.ExecuteUbergraph_BPW_MAMTreeInfoBox(61)
    

    def ExecuteUbergraph_BPW_MAMTreeInfoBox(self):
        # Label 10
        ReturnValue: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.SpawnAnim, 0, 1, 0, 1)
        # End
        goto('L10')
    
