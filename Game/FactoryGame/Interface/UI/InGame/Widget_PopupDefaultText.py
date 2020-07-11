
from codegen.ue4_stub import *

from Game.FactoryGame.Interface.UI.InGame.Widget_PopupDefaultText import ExecuteUbergraph_Widget_PopupDefaultText
from Script.UMG import UserWidget

class Widget_PopupDefaultText(UserWidget):
    mBody: FText
    
    def Construct(self):
        self.ExecuteUbergraph_Widget_PopupDefaultText(10)
    

    def ExecuteUbergraph_Widget_PopupDefaultText(self):
        self.mText.SetText(self.mBody)
    
