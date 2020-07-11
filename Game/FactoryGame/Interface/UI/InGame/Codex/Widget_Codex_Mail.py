
from codegen.ue4_stub import *

from Script.Engine import Conv_StringToText
from Script.Engine import EqualEqual_TextText
from Script.UMG import UserWidget
from Script.UMG import SetText
from Game.FactoryGame.Interface.UI.InGame.Codex.Widget_Codex_Mail import ExecuteUbergraph_Widget_Codex_Mail
from Script.Engine import Default__KismetTextLibrary

class Widget_Codex_Mail(UserWidget):
    mText: FText
    
    def Construct(self):
        self.ExecuteUbergraph_Widget_Codex_Mail(10)
    

    def ExecuteUbergraph_Widget_Codex_Mail(self):
        ReturnValue: FText = Default__KismetTextLibrary.Conv_StringToText("")
        
        ReturnValue_0: bool = Default__KismetTextLibrary.EqualEqual_TextText(Ref[self.mText], Ref[ReturnValue])
        if not ReturnValue_0:
            goto('L141')
        # End
        
        # Label 141
        self.RichTextBlock_0.SetText(Ref[self.mText])
    
