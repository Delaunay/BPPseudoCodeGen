
from codegen.ue4_stub import *

from Game.FactoryGame.Interface.UI.InGame.-Shared.Widget_StandardButton_Togglable import ExecuteUbergraph_Widget_StandardButton_Togglable.K2Node_Event_IsDesignTime
from Game.FactoryGame.Interface.UI.InGame.-Shared.Widget_StandardButton_Togglable import ExecuteUbergraph_Widget_StandardButton_Togglable
from Script.SlateCore import SlateBrush
from Game.FactoryGame.Interface.UI.InGame.-Shared.Widget_StandardButton_Togglable import ExecuteUbergraph_Widget_StandardButton_Togglable.K2Node_CustomEvent_mIsTrue
from Script.Engine import Not_PreBool
from Script.UMG import UserWidget

class Widget_StandardButton_Togglable(UserWidget):
    mTrueText: FText = NSLOCTEXT("", "D06DD00446AEB0155E7383B265D4E3AC", "True")
    mFalseText: FText = NSLOCTEXT("", "7095D59A49BA541D1878C08A290A9195", "False")
    mTrueIconBrush: SlateBrush
    mFalseIconBrush: SlateBrush
    mIsTrue: bool = True
    OnStateChanged: FMulticastScriptDelegate
    
    def SetButtonState(self, mIsTrue: bool):
        self.mIsTrue = mIsTrue
        Variable1: bool = self.mIsTrue
        
        switch = {
            False: self.mFalseText,
            True: self.mTrueText
        }
        self.Widget_StandardButton.SetText(switch.get(Variable1, None))
        Variable: bool = self.mIsTrue
        
        switch_0 = {
            False: self.mFalseIconBrush,
            True: self.mTrueIconBrush
        }
        self.Widget_StandardButton.SetIconBrush(switch_0.get(Variable, None))
    

    def PreConstruct(self):
        ExecuteUbergraph_Widget_StandardButton_Togglable.K2Node_Event_IsDesignTime = IsDesignTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_StandardButton_Togglable(38)
    

    def Init(self, mIsTrue: bool):
        ExecuteUbergraph_Widget_StandardButton_Togglable.K2Node_CustomEvent_mIsTrue = mIsTrue #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_StandardButton_Togglable(43)
    

    def BndEvt__Widget_StandardButton_K2Node_ComponentBoundEvent_0_OnClicked__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_StandardButton_Togglable(71)
    

    def ExecuteUbergraph_Widget_StandardButton_Togglable(self):
        # Label 10
        self.Init(self.mIsTrue)
        # End
        goto('L10')
        self.SetButtonState(mIsTrue)
        # End
        ReturnValue: bool = Not_PreBool(self.mIsTrue)
        self.SetButtonState(ReturnValue)
        self.OnStateChanged.ProcessMulticastDelegate(self.mIsTrue)
    

    def OnStateChanged__DelegateSignature(self, IsTrue: bool):
        pass
    
