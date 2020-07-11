
from codegen.ue4_stub import *

from Script.UMG import PlayAnimation
from Script.UMG import UserWidget
from Script.UMG import UMGSequencePlayer

class Widget_Train_TimeTable_AvilableStations(UserWidget):
    mIsVisible: bool
    
    def SetIsVisible(self, mIsVisible: bool):
        self.mIsVisible = mIsVisible
        if not self.mIsVisible:
            goto('L188')
        self.SetVisibility(0)
        ReturnValue: Ptr[UMGSequencePlayer] = self.Widget_Window_DarkMode.Widget_Anim_Up_Slide.PlayAnimation(self.Widget_Window_DarkMode.Widget_Anim_Up_Slide.EnableAnim, 0, 1, 0, 1)
        # End
        # Label 188
        self.SetVisibility(2)
    
