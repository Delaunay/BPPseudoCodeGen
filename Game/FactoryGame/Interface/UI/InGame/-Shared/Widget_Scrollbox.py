
from codegen.ue4_stub import *

from Script.UMG import HasAnyChildren
from Game.FactoryGame.Interface.UI.InGame.-Shared.Widget_Scrollbox import ExecuteUbergraph_Widget_Scrollbox
from Script.UMG import UserWidget

class Widget_Scrollbox(UserWidget):
    
    
    def Construct(self):
        self.ExecuteUbergraph_Widget_Scrollbox(10)
    

    def ExecuteUbergraph_Widget_Scrollbox(self):
        ReturnValue: bool = self.mScrollableContent.HasAnyChildren()
        if not ReturnValue:
            goto('L101')
        self.SetVisibility(0)
        # End
        # Label 101
        self.SetVisibility(2)
    
