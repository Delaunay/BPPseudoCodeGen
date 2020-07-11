
from codegen.ue4_stub import *

from Script.Engine import Conv_TextToString
from Script.UMG import HasMouseCapture
from Game.FactoryGame.Interface.UI.Menu.Widget_InputBox import ExecuteUbergraph_Widget_InputBox.K2Node_Event_InFocusEvent
from Script.Engine import EqualEqual_ByteByte
from Game.FactoryGame.Interface.UI.Menu.Widget_InputBox import ExecuteUbergraph_Widget_InputBox.K2Node_ComponentBoundEvent_Text
from Game.FactoryGame.Interface.UI.Menu.Widget_InputBox import ExecuteUbergraph_Widget_InputBox.K2Node_ComponentBoundEvent_Text1
from Game.FactoryGame.Interface.UI.Assets.BuildMenu.Cross import Cross
from Script.UMG import Handled
from Script.UMG import Unhandled
from Script.UMG import SetText
from Game.FactoryGame.Interface.UI.Menu.Widget_InputBox import ExecuteUbergraph_Widget_InputBox.K2Node_Event_MyGeometry
from Script.Engine import Len
from Game.FactoryGame.Interface.UI.Menu.Widget_InputBox import ExecuteUbergraph_Widget_InputBox.K2Node_ComponentBoundEvent_CommitMethod
from Script.UMG import Default__WidgetBlueprintLibrary
from Script.UMG import SetColorAndOpacity
from Script.Engine import Default__KismetTextLibrary
from Script.Engine import BooleanOR
from Script.UMG import Construct
from Game.FactoryGame.Interface.UI.Assets.Shared.SearchIcon import SearchIcon
from Game.FactoryGame.Interface.UI.Menu.Widget_InputBox import ExecuteUbergraph_Widget_InputBox.K2Node_Event_InDeltaTime
from Game.FactoryGame.Interface.UI.Menu.Widget_InputBox import ExecuteUbergraph_Widget_InputBox
from Game.FactoryGame.Interface.UI.Menu.Widget_InputBox import ExecuteUbergraph_Widget_InputBox.K2Node_Event_IsDesignTime
from Script.UMG import GetText
from Script.Engine import Default__KismetStringLibrary
from Script.UMG import UserWidget
from Game.FactoryGame.Interface.UI.HUDHelpers.HUDHelpers import Default__HUDHelpers
from Script.UMG import EventReply

class Widget_InputBox(UserWidget):
    OnTextChanged: FMulticastScriptDelegate
    OnTextComitted: FMulticastScriptDelegate
    mPreviewText: FText
    isSearchbar: bool = True
    OnClearTextClicked: FMulticastScriptDelegate
    mInputHandled: bool = True
    OnInputBoxFocusReceived: FMulticastScriptDelegate
    OnInputBoxFocusLost: FMulticastScriptDelegate
    
    def OnFocusReceived(self):
        self.OnInputBoxFocusReceived.ProcessMulticastDelegate(InFocusEvent)
        ReturnValue: EventReply = Default__WidgetBlueprintLibrary.Unhandled()
        ReturnValue_0: EventReply = ReturnValue
    

    def OnKeyUp(self):
        ReturnValue: EventReply = Default__WidgetBlueprintLibrary.Unhandled()
        ReturnValue_0: EventReply = Default__WidgetBlueprintLibrary.Handled()
        Variable: bool = self.mInputHandled
        
        switch = {
            False: ReturnValue,
            True: ReturnValue_0
        }
        ReturnValue_1: EventReply = switch.get(Variable, None)
    

    def CheckSearchbarLength(self):
        if not self.isSearchbar:
            goto('L235')
        ReturnValue: FText = self.mInputBox.GetText()
        
        ReturnValue_0: FString = Default__KismetTextLibrary.Conv_TextToString(Ref[ReturnValue])
        ReturnValue_1: int32 = Default__KismetStringLibrary.Len(ReturnValue_0)
        ReturnValue_2: bool = ReturnValue_1 > 0
        SearchbarContainsText = ReturnValue_2
    

    def SetSearchbarStyle(self):
        if not self.isSearchbar:
            goto('L57')
        self.mSearchbarIconSizebox.SetVisibility(0)
        # End
        # Label 57
        self.mSearchbarIconSizebox.SetVisibility(1)
    

    def SetInputboxStyle(self, IsHovered: bool):
        if not IsHovered:
            goto('L405')
        
        Text = None
        Graphics = None
        Default__HUDHelpers.GetFactoryGameDarkGray(self, Ref[Text], Ref[Graphics])
        self.mIconImageSwitcher.mImageObject.SetColorAndOpacity(Graphics)
        
        Text2 = None
        Graphics2 = None
        Default__HUDHelpers.GetFactoryGameDarkGray(self, Ref[Text2], Ref[Graphics2])
        self.HintText.SetColorAndOpacity(Text2)
        
        Text1 = None
        Graphics1 = None
        Default__HUDHelpers.GetFactoryGameDarkGray(self, Ref[Text1], Ref[Graphics1])
        self.InputText.SetColorAndOpacity(Text1)
        self.mBorder.SetVisibility(3)
        self.mBG.SetVisibility(2)
        # End
        
        Text = None
        Graphics = None
        # Label 405
        Default__HUDHelpers.GetFactoryGameLightGray(self, Ref[Text], Ref[Graphics])
        self.mIconImageSwitcher.mImageObject.SetColorAndOpacity(Graphics)
        
        Text1 = None
        Graphics1 = None
        Default__HUDHelpers.GetFactoryGameLightGray(self, Ref[Text1], Ref[Graphics1])
        self.HintText.SetColorAndOpacity(Text1)
        
        TextWhite = None
        GraphicsWhite = None
        Default__HUDHelpers.GetFactoryGameWhite(self, Ref[TextWhite], Ref[GraphicsWhite])
        self.InputText.SetColorAndOpacity(TextWhite)
        self.mBorder.SetVisibility(2)
        self.mBG.SetVisibility(3)
    

    def ShowHintText(self):
        ReturnValue: bool = self.mInputBox.HasMouseCapture()
        ReturnValue_0: FText = self.mInputBox.GetText()
        
        ReturnValue_1: FString = Default__KismetTextLibrary.Conv_TextToString(Ref[ReturnValue_0])
        ReturnValue_2: int32 = Default__KismetStringLibrary.Len(ReturnValue_1)
        ReturnValue_3: bool = ReturnValue_2 > 0
        ReturnValue_4: bool = BooleanOR(ReturnValue_3, ReturnValue)
        if not ReturnValue_4:
            goto('L339')
        self.HintText.SetVisibility(1)
        # End
        # Label 339
        self.HintText.SetVisibility(3)
    

    def BndEvt__mInputBox_K2Node_ComponentBoundEvent_0_OnEditableTextChangedEvent__DelegateSignature(self, text: Const[Ref[FText]]):
        ExecuteUbergraph_Widget_InputBox.K2Node_ComponentBoundEvent_Text1 = text #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_InputBox(244)
    

    def BndEvt__mInputBox_K2Node_ComponentBoundEvent_0_OnEditableTextCommittedEvent__DelegateSignature(self, text: Const[Ref[FText]], CommitMethod: uint8):
        ExecuteUbergraph_Widget_InputBox.K2Node_ComponentBoundEvent_Text = text #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_InputBox.K2Node_ComponentBoundEvent_CommitMethod = CommitMethod #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_InputBox(43)
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_InputBox(626)
    

    def Tick(self):
        ExecuteUbergraph_Widget_InputBox.K2Node_Event_MyGeometry = MyGeometry #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_InputBox.K2Node_Event_InDeltaTime = InDeltaTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_InputBox(655)
    

    def BndEvt__mHover_K2Node_ComponentBoundEvent_1_OnButtonHoverEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_InputBox(754)
    

    def BndEvt__mHover_K2Node_ComponentBoundEvent_2_OnButtonHoverEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_InputBox(828)
    

    def PreConstruct(self):
        ExecuteUbergraph_Widget_InputBox.K2Node_Event_IsDesignTime = IsDesignTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_InputBox(833)
    

    def BndEvt__mSearchButton_K2Node_ComponentBoundEvent_5_OnButtonClickedEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_InputBox(867)
    

    def OnFocusLost(self):
        ExecuteUbergraph_Widget_InputBox.K2Node_Event_InFocusEvent = InFocusEvent #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_InputBox(10)
    

    def ExecuteUbergraph_Widget_InputBox(self):
        self.OnInputBoxFocusLost.ProcessMulticastDelegate(InFocusEvent)
        # End
        ReturnValue: bool = EqualEqual_ByteByte(CommitMethod, 1)
        ReturnValue1: bool = EqualEqual_ByteByte(CommitMethod, 0)
        ReturnValue_0: bool = BooleanOR(ReturnValue, ReturnValue1)
        if not ReturnValue_0:
            goto('L957')
        self.InputText.SetText(Text)
        self.OnTextComitted.ProcessMulticastDelegate(Text, CommitMethod)
        # End
        self.OnTextChanged.ProcessMulticastDelegate(Text1)
        self.InputText.SetText(Text1)
        self.ShowHintText()
        
        SearchbarContainsText1 = None
        self.CheckSearchbarLength(Ref[SearchbarContainsText1])
        if not SearchbarContainsText1:
            goto('L387')
        if not Variable:
            goto('L516')
        # End
        # Label 387
        Variable: bool = False
        if not Variable1:
            goto('L417')
        # End
        # Label 417
        Variable1: bool = True
        self.mIconImageSwitcher.SwitchImage(SearchIcon)
        self.mClearSearchButton.SetVisibility(3)
        # End
        # Label 516
        Variable = True
        Variable1 = False
        self.mIconImageSwitcher.SwitchImage(Cross)
        self.mClearSearchButton.SetVisibility(0)
        # End
        self.Construct()
        self.ShowHintText()
        # End
        ReturnValue_1: bool = self.mInputBox.HasMouseCapture()
        if not ReturnValue_1:
            goto('L957')
        self.HintText.SetVisibility(1)
        # End
        # Label 754
        ReturnValue_2: bool = self.mHover.IsHovered()
        self.SetInputboxStyle(ReturnValue_2)
        # End
        goto('L754')
        self.SetSearchbarStyle()
        self.SetInputboxStyle(False)
        # End
        
        SearchbarContainsText = None
        self.CheckSearchbarLength(Ref[SearchbarContainsText])
        if not SearchbarContainsText:
            goto('L957')
        self.mInputBox.SetText()
        self.OnClearTextClicked.ProcessMulticastDelegate()
    

    def OnInputBoxFocusLost__DelegateSignature(self, FocusEvent: FocusEvent):
        pass
    

    def OnInputBoxFocusReceived__DelegateSignature(self, FocusEvent: FocusEvent):
        pass
    

    def OnClearTextClicked__DelegateSignature(self):
        pass
    

    def OnTextComitted__DelegateSignature(self, text: FText, CommitMethod: uint8):
        pass
    

    def OnTextChanged__DelegateSignature(self, text: FText):
        pass
    
