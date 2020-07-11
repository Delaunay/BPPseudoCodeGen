
from codegen.ue4_stub import *

from Script.UMG import UserWidget

class Widget_Codex_MessageNotification(UserWidget):
    mText: FText
    
    def GetText(self):
        ReturnValue = self.mText
    
