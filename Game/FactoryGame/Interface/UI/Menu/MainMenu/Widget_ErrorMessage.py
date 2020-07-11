
from codegen.ue4_stub import *

from Script.Engine import Default__KismetSystemLibrary
from Game.FactoryGame.Interface.UI.Menu.MainMenu.Widget_ErrorMessage import ExecuteUbergraph_Widget_ErrorMessage.K2Node_Event_IsDesignTime
from Game.FactoryGame.Interface.UI.Menu.MainMenu.Widget_ErrorMessage import ExecuteUbergraph_Widget_ErrorMessage
from Script.Engine import QuitGame
from Script.UMG import UserWidget

class Widget_ErrorMessage(UserWidget):
    mOnClicked: FMulticastScriptDelegate
    mButtonText: FText
    mErrorMessage: FText
    mWillCauseExit: bool
    
    def SetBody(self, text: FText):
        self.mErrorMessage = text
    

    def SetButtonText(self, text: FText):
        self.mButtonText = text
        self.Widget_StandardButton.ButtonText.SetText(self.mButtonText)
    

    def BndEvt__Widget_StandardButton_K2Node_ComponentBoundEvent_0_OnClicked__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_ErrorMessage(34)
    

    def PreConstruct(self):
        ExecuteUbergraph_Widget_ErrorMessage.K2Node_Event_IsDesignTime = IsDesignTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_ErrorMessage(90)
    

    def ExecuteUbergraph_Widget_ErrorMessage(self):
        # Label 10
        self.mOnClicked.ProcessMulticastDelegate()
        # End
        if not self.mWillCauseExit:
            goto('L10')
        Default__KismetSystemLibrary.QuitGame(self, None, 0, False)
        # End
        self.Widget_StandardButton.mText = self.mButtonText
    

    def mOnClicked__DelegateSignature(self):
        pass
    
