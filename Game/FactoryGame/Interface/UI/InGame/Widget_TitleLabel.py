
from codegen.ue4_stub import *

from Script.UMG import UserWidget

class Widget_TitleLabel(UserWidget):
    mShouldShowColorPickerButton: bool
    mHeaderTitleText: FText
    
    def SetFicsItDriverText(self):
        pass
    

    def SetTitle(self, Title: FText):
        self.mHeaderTitleText = Title
    
