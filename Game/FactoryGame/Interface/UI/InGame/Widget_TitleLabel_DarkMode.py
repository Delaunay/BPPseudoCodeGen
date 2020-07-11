
from codegen.ue4_stub import *

from Script.Engine import Conv_TextToString
from Script.Engine import Default__KismetTextLibrary
from Game.FactoryGame.Interface.UI.InGame.Widget_TitleLabel_DarkMode import ExecuteUbergraph_Widget_TitleLabel_DarkMode
from Game.FactoryGame.Interface.UI.InGame.Widget_TitleLabel_DarkMode import ExecuteUbergraph_Widget_TitleLabel_DarkMode.K2Node_Event_IsDesignTime
from Script.UMG import UserWidget

class Widget_TitleLabel_DarkMode(UserWidget):
    mShouldShowColorPickerButton: bool
    mHeaderTitleText: FText = NSLOCTEXT("", "A81785E047642BEED034E3A365F99E20", "Title Here")
    
    def SetFicsItDriverText(self):
        pass
    

    def SetTitle(self, Title: FText):
        
        ReturnValue: FString = Default__KismetTextLibrary.Conv_TextToString(Ref[Title])
        self.Widget_LetterSpacedText.SetTitle(ReturnValue)
    

    def PreConstruct(self):
        ExecuteUbergraph_Widget_TitleLabel_DarkMode.K2Node_Event_IsDesignTime = IsDesignTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_TitleLabel_DarkMode(38)
    

    def ExecuteUbergraph_Widget_TitleLabel_DarkMode(self):
        # Label 10
        self.SetTitle(self.mHeaderTitleText)
        # End
        goto('L10')
    
