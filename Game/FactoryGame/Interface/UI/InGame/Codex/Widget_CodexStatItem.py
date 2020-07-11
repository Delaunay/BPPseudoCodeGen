
from codegen.ue4_stub import *

from Game.FactoryGame.Interface.UI.InGame.Codex.Widget_CodexStatItem import ExecuteUbergraph_Widget_CodexStatItem
from Script.UMG import UserWidget

class Widget_CodexStatItem(UserWidget):
    mInfo: FText
    mValue: FText
    
    def Construct(self):
        self.ExecuteUbergraph_Widget_CodexStatItem(10)
    

    def ExecuteUbergraph_Widget_CodexStatItem(self):
        self.mInfoText.SetText(self.mInfo)
        self.mValueText.SetText(self.mValue)
    
