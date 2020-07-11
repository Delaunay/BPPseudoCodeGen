
from codegen.ue4_stub import *

from Script.Engine import Default__KismetInputLibrary
from Script.Engine import Conv_TextToString
from Script.AkAudio import PostAkEvent
from Game.FactoryGame.Interface.UI.Menu.PauseMenu.Widget_GiveFeedback import ExecuteUbergraph_Widget_GiveFeedback.K2Node_ComponentBoundEvent_Text
from Script.InputCore import Key
from Script.Engine import GreaterEqual_IntInt
from Script.Engine import TextIsEmpty
from Game.FactoryGame.Interface.UI.Menu.PauseMenu.Widget_GiveFeedback import ExecuteUbergraph_Widget_GiveFeedback
from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import PlayerController
from Script.Engine import Default__KismetArrayLibrary
from Script.UMG import Handled
from Script.UMG import SetText
from Game.FactoryGame.Interface.UI.Menu.PauseMenu.Widget_GiveFeedback import ExecuteUbergraph_Widget_GiveFeedback.K2Node_CustomEvent_mConfirmBool
from Script.Engine import Len
from Script.UMG import AddOption
from Script.UMG import Default__WidgetBlueprintLibrary
from Script.Engine import EqualEqual_StrStr
from Script.Engine import Contains
from Script.Engine import Default__KismetTextLibrary
from Script.UMG import GetSelectedOption
from Script.FactoryGame import FGInteractWidget
from Script.FactoryGame import Default__FGNetworkLibrary
from Script.FactoryGame import GetInteractWidgetStack
from Script.UMG import GetText
from Script.Engine import Default__KismetStringLibrary
from Script.FactoryGame import SubmitFeedback
from Script.Engine import GetKey
from Script.FactoryGame import Default__FGBlueprintFunctionLibrary
from Script.AkAudio import Default__AkGameplayStatics
from Script.Engine import EqualEqual_KeyKey
from Script.Engine import LaunchURL
from Game.FactoryGame.Interface.UI.HUDHelpers.HUDHelpers import Default__HUDHelpers
from Game.FactoryGame.Interface.UI.Audio.MainMenu.Play_UI_MainMenu_Click import Play_UI_MainMenu_Click
from Script.FactoryGame import AddPopupWithCloseDelegate
from Game.FactoryGame.Interface.UI.Menu.PauseMenu.Widget_GiveFeedback import ExecuteUbergraph_Widget_GiveFeedback.K2Node_ComponentBoundEvent_SelectedOption
from Script.AkAudio import AkComponent
from Script.UMG import SetSelectedOption
from Script.UMG import EventReply

class Widget_GiveFeedback(FGInteractWidget):
    mIsSatisfactoryArray: List[FString] = ['Yes.', 'Literally, Yes.']
    mTypeFeedbackArray: List[FString] = ['Bug Report', 'Level Feedback']
    mUseKeyboard = True
    mUseMouse = True
    mCaptureInput = True
    mRestoreFocusWhenLost = True
    mDesiredHorizontalAlignment = 2
    mDesiredVerticalAlignment = 2
    mCallCustomTickOnConstruct = True
    
    def PopulateTypeFeedbackOptions(self):
        ExecutionFlow.Push("L387")
        Variable: int32 = 0
        Variable_0: int32 = 0
        
        # Label 51
        ReturnValue: int32 = len(self.mTypeFeedbackArray)
        ReturnValue_0: bool = Variable <= ReturnValue
        if not ReturnValue_0:
           goto(ExecutionFlow.Pop())
        Variable_0 = Variable
        ExecutionFlow.Push("L313")
        
        Item = None
        Item = self.mTypeFeedbackArray[Variable_0]
        self.mTypeFeedbackSelect.mDropdownBox.AddOption(Item)
        goto(ExecutionFlow.Pop())
        # Label 313
        ReturnValue_1: int32 = Variable + 1
        Variable = ReturnValue_1
        goto('L51')
    

    def PopulateSatisfactorySelectOptions(self):
        ExecutionFlow.Push("L505")
        Variable: int32 = 0
        Variable_0: int32 = 0
        
        # Label 51
        ReturnValue: int32 = len(self.mIsSatisfactoryArray)
        ReturnValue_0: bool = Variable <= ReturnValue
        if not ReturnValue_0:
           goto(ExecutionFlow.Pop())
        Variable_0 = Variable
        ExecutionFlow.Push("L431")
        
        Item1 = None
        Item1 = self.mIsSatisfactoryArray[Variable_0]
        self.mIsSatisfactorySelect.mDropdownBox.AddOption(Item1)
        
        Item = None
        Item = self.mIsSatisfactoryArray[0]
        self.mIsSatisfactorySelect.mDropdownBox.SetSelectedOption(Item)
        goto(ExecutionFlow.Pop())
        # Label 431
        ReturnValue_1: int32 = Variable + 1
        Variable = ReturnValue_1
        goto('L51')
    

    def OnKeyDown(self):
        
        ReturnValue: Key = Default__KismetInputLibrary.GetKey(Ref[InKeyEvent])
        ReturnValue_0: bool = Default__KismetInputLibrary.EqualEqual_KeyKey(ReturnValue, Key(KeyName = "Escape"))
        if not ReturnValue_0:
            goto('L752')
        ReturnValue_1: Ptr[PlayerController] = self.GetOwningPlayer()
        
        gameUI = None
        Default__HUDHelpers.GetFGGameUI(ReturnValue_1, self, Ref[gameUI])
        ReturnValue1: List[Ptr[FGInteractWidget]] = gameUI.GetInteractWidgetStack()
        
        ReturnValue1_0: int32 = len(ReturnValue1) - 1
        ReturnValue_2: bool = GreaterEqual_IntInt(ReturnValue1_0, 0)
        if not ReturnValue_2:
            goto('L829')
        # Label 387
        ReturnValue_1 = self.GetOwningPlayer()
        
        gameUI = None
        Default__HUDHelpers.GetFGGameUI(ReturnValue_1, self, Ref[gameUI])
        ReturnValue_3: List[Ptr[FGInteractWidget]] = gameUI.GetInteractWidgetStack()
        
        ReturnValue_4: int32 = len(ReturnValue_3) - 1
        
        Item = None
        Item = ReturnValue_3[ReturnValue_4]
        Item.OnEscapePressed()
        ReturnValue1_1: EventReply = Default__WidgetBlueprintLibrary.Handled()
        ReturnValue_5: EventReply = ReturnValue1_1
        goto('L829')
        # Label 752
        ReturnValue_6: EventReply = Default__WidgetBlueprintLibrary.Handled()
        ReturnValue_5 = ReturnValue_6
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_GiveFeedback(729)
    

    def BndEvt__Widget_Window_K2Node_ComponentBoundEvent_0_OnClose__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_GiveFeedback(891)
    

    def CloseFeedback(self):
        self.ExecuteUbergraph_Widget_GiveFeedback(942)
    

    def BndEvt__THANKSDUDE_K2Node_ComponentBoundEvent_147_OnClicked__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_GiveFeedback(947)
    

    def BndEvt__mTypeFeedbackSelect_K2Node_ComponentBoundEvent_1_onSelectionChanged__DelegateSignature(self, SelectedOption: FString):
        ExecuteUbergraph_Widget_GiveFeedback.K2Node_ComponentBoundEvent_SelectedOption = SelectedOption #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_GiveFeedback(962)
    

    def BndEvt__Details_text_K2Node_ComponentBoundEvent_4_OnMultiLineEditableTextChangedEvent__DelegateSignature(self, text: Const[Ref[FText]]):
        ExecuteUbergraph_Widget_GiveFeedback.K2Node_ComponentBoundEvent_Text = text #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_GiveFeedback(1305)
    

    def BndEvt__Widget_StandardButton_K2Node_ComponentBoundEvent_5_OnClicked__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_GiveFeedback(1589)
    

    def BndEvt__Widget_StandardButton_K2Node_ComponentBoundEvent_6_OnClicked__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_GiveFeedback(1667)
    

    def SendFeedbackAfterConfirm(self, mConfirmBool: bool):
        ExecuteUbergraph_Widget_GiveFeedback.K2Node_CustomEvent_mConfirmBool = mConfirmBool #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_GiveFeedback(1672)
    

    def BndEvt__Button_0_K2Node_ComponentBoundEvent_2_OnButtonClickedEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_GiveFeedback(15)
    

    def ExecuteUbergraph_Widget_GiveFeedback(self):
        goto(ComputedJump("EntryPoint"))
        # Label 15
        ReturnValue2: Ptr[PlayerController] = self.GetOwningPlayer()
        OutputDelegate1.BindUFunction(self, SendFeedbackAfterConfirm)
        
        OutputDelegate1 = None
        Default__FGBlueprintFunctionLibrary.AddPopupWithCloseDelegate(ReturnValue2, "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 104, 'Value': 'Thanks for your feedback!'}", "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 169, 'Value': "We're gonna work even harder now. <3"}", 0, None, None, Ref[OutputDelegate1])
        goto(ExecutionFlow.Pop())
        # Label 258
        if not False:
           goto(ExecutionFlow.Pop())
        Variable: bool = True
        goto(ExecutionFlow.Pop())
        # Label 272
        if not Variable:
            goto('L287')
        goto(ExecutionFlow.Pop())
        # Label 287
        Variable = True
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_0: FText = self.Details_text.GetText()
        
        ReturnValue_1: FString = Default__KismetTextLibrary.Conv_TextToString(Ref[ReturnValue_0])
        # Label 431
        ReturnValue_2: FString = self.mIsSatisfactorySelect.mDropdownBox.GetSelectedOption()
        ReturnValue_3: bool = Default__KismetStringLibrary.Contains(ReturnValue_2, "Yes", False, False)
        UserFeedbackFrontEndData.isSatisfactory = ReturnValue_3
        UserFeedbackFrontEndData.typeOfFeedback = "Level Feedback"
        UserFeedbackFrontEndData.Body = ReturnValue_1
        ReturnValue_4: bool = Default__FGNetworkLibrary.SubmitFeedback(UserFeedbackFrontEndData, ReturnValue)
        goto(ExecutionFlow.Pop())
        self.PopulateSatisfactorySelectOptions()
        self.PopulateTypeFeedbackOptions()
        self.mTypeFeedbackSelect.mDropdownBox.SetSelectedOption("Level Feedbck")
        OutputDelegate.BindUFunction(self, OnEscapePressed)
        self.Widget_Window_DarkMode.OnClose.AddUnique(OutputDelegate)
        goto(ExecutionFlow.Pop())
        # Label 891
        self.OnEscapePressed()
        goto(ExecutionFlow.Pop())
        # Label 906
        ExecutionFlow.Push("L272")
        if not Variable_0:
            goto('L926')
        goto(ExecutionFlow.Pop())
        # Label 926
        Variable_0: bool = True
        goto('L258')
        goto('L891')
        self.OnEscapePressed()
        goto(ExecutionFlow.Pop())
        ReturnValue1: FText = self.Details_text.GetText()
        
        ReturnValue_5: bool = Default__KismetTextLibrary.TextIsEmpty(Ref[ReturnValue1])
        ReturnValue_6: bool = Default__KismetStringLibrary.EqualEqual_StrStr(SelectedOption, "Bug Report")
        ReturnValue_7: bool = ReturnValue_6 and ReturnValue_5
        if not ReturnValue_7:
            goto('L1270')
        ReturnValue2_0: FText = self.Details_text.GetText()
        self.Details_text.SetText(ReturnValue2_0)
        goto(ExecutionFlow.Pop())
        # Label 1270
        self.Details_text.SetText()
        goto(ExecutionFlow.Pop())
        
        Text = None
        ReturnValue1_0: FString = Default__KismetTextLibrary.Conv_TextToString(Ref[Text])
        ReturnValue_8: int32 = Default__KismetStringLibrary.Len(ReturnValue1_0)
        ReturnValue_9: bool = ReturnValue_8 > 10
        self.mConfirmButton.SetIsEnabled(ReturnValue_9)
        goto(ExecutionFlow.Pop())
        # Label 1503
        ReturnValue1_1: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_10: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_UI_MainMenu_Click, ReturnValue1_1, True)
        goto(ExecutionFlow.Pop())
        Default__KismetSystemLibrary.LaunchURL("https://questions.satisfactorygame.com/")
        goto('L1503')
        goto('L15')
        goto('L906')
    
