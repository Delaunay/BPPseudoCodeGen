
from codegen.ue4_stub import *

from Game.FactoryGame.Buildable.Factory.ResourceSinkShop.UI.Widget_Bookmark_Button import ExecuteUbergraph_Widget_Bookmark_Button
from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import PrintString
from Script.UMG import UserWidget
from Script.CoreUObject import LinearColor

class Widget_Bookmark_Button(UserWidget):
    OnBookmarkButtonClicked: FMulticastScriptDelegate
    
    def BndEvt__mBookmarkButton_K2Node_ComponentBoundEvent_0_OnButtonClickedEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_Bookmark_Button(106)
    

    def ExecuteUbergraph_Widget_Bookmark_Button(self):
        # Label 10
        Default__KismetSystemLibrary.PrintString(self, "Add to wishlist", True, True, LinearColor(R = 1, G = 0.077845998108387, B = 0.7202000021934509, A = 1), 2)
        # End
        goto('L10')
    

    def OnBookmarkButtonClicked__DelegateSignature(self):
        pass
    
