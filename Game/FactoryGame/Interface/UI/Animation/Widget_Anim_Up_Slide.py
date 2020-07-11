
from codegen.ue4_stub import *

from Script.UMG import UMGSequencePlayer
from Script.UMG import PlayAnimation
from Script.UMG import WidgetAnimation
from Game.FactoryGame.Interface.UI.Animation.Widget_Anim_Up_Slide import ExecuteUbergraph_Widget_Anim_Up_Slide
from Script.UMG import UserWidget

class Widget_Anim_Up_Slide(UserWidget):
    EnableAnim: Ptr[WidgetAnimation]
    CloseAnimStarted: bool
    
    def Construct(self):
        self.ExecuteUbergraph_Widget_Anim_Up_Slide(26)
    

    def CloseAnim(self):
        self.ExecuteUbergraph_Widget_Anim_Up_Slide(77)
    

    def Destruct(self):
        self.ExecuteUbergraph_Widget_Anim_Up_Slide(139)
    

    def ExecuteUbergraph_Widget_Anim_Up_Slide(self):
        # Label 10
        self.CloseAnimStarted = False
        # End
        ReturnValue: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.EnableAnim, 0, 1, 0, 1)
        # End
        self.CloseAnimStarted = True
        ReturnValue1: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.EnableAnim, 0, 1, 1, 1)
        # End
        goto('L10')
    
