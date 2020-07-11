
from codegen.ue4_stub import *

from Game.FactoryGame.Interface.UI.Assets.Shared.Widget_Label import ExecuteUbergraph_Widget_Label.K2Node_Event_IsDesignTime
from Script.UMG import UserWidget
from Game.FactoryGame.Interface.UI.Assets.Shared.Widget_Label import ExecuteUbergraph_Widget_Label

class Widget_Label(UserWidget):
    mLabelText: FText
    
    def SetLabelText(self, LabelText: FText):
        self.mLabelText = LabelText
        self.mLabelTextblock.SetText(self.mLabelText)
    

    def PreConstruct(self):
        ExecuteUbergraph_Widget_Label.K2Node_Event_IsDesignTime = IsDesignTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_Label(38)
    

    def ExecuteUbergraph_Widget_Label(self):
        # Label 10
        self.SetLabelText(self.mLabelText)
        # End
        goto('L10')
    
