
from codegen.ue4_stub import *

from Script.Engine import SetTextPropertyByName
from Script.Engine import Conv_TextToString
from Script.Engine import Texture2D
from Game.FactoryGame.Interface.UI.InGame.Codex.Widget_Codex_Message import ExecuteUbergraph_Widget_Codex_Message.K2Node_CustomEvent_contentClass
from Script.FactoryGame import GetSenderDefaultObject
from Script.UMG import PanelSlot
from Script.UMG import AddChild
from Script.Engine import Default__KismetSystemLibrary
from Script.FactoryGame import FGAudioMessage
from Script.Engine import PlayerController
from Script.Engine import Default__KismetArrayLibrary
from Script.Engine import FormatArgumentData
from Script.UMG import ESlateVisibility
from Script.Engine import IsValid
from Script.UMG import Default__WidgetBlueprintLibrary
from Game.FactoryGame.Interface.UI.InGame.Codex.Widget_Codex_Message import ExecuteUbergraph_Widget_Codex_Message
from Script.FactoryGame import FGMessageBase
from Game.FactoryGame.Interface.UI.InGame.Codex.Widget_Codex_Mail import Widget_Codex_Mail
from Script.Engine import Default__KismetTextLibrary
from Script.FactoryGame import FGMessageSender
from Script.FactoryGame import Default__FGMessageSender
from Script.Engine import Conv_StringToText
from Game.FactoryGame.Interface.UI.Message.Widget_AudioMessage import Widget_AudioMessage
from Script.Engine import Format
from Script.Engine import Default__KismetStringLibrary
from Script.UMG import UserWidget
from Script.FactoryGame import GetMessageDefaultObject
from Game.FactoryGame.Interface.UI.HUDHelpers.HUDHelpers import Default__HUDHelpers
from Script.Engine import EqualEqual_TextText
from Script.UMG import Create
from Script.FactoryGame import Default__FGMessageBase
from Script.Engine import Concat_StrStr

class Widget_Codex_Message(UserWidget):
    mImages: List[Ptr[Texture2D]]
    mImageIndex: int32
    IsAudioMessage: bool
    CurrentAudioTranscript: Ptr[Widget_Codex_Mail]
    mCurrentAudioMessage: TSubclassOf[FGAudioMessage]
    
    def ClearMessage(self):
        self.mMessageSlot.ClearChildren()
        self.mFromName.SetText()
        self.mFromMail.SetText()
        self.mToName.SetText()
        self.mToMail.SetText()
        self.mSubject.SetText()
        self.mAttachedFileName.SetText()
        self.mMessageInfo.SetVisibility(1)
    

    def GenerateAudioMessage(self, inClass: TSubclassOf[FGAudioMessage]):
        ExecutionFlow.Push("L1392")
        Variable: int32 = 0
        Variable_0: int32 = 0
        # Label 51
        ReturnValue: Ptr[FGAudioMessage] = Default__FGMessageBase.GetMessageDefaultObject(inClass)
        
        ReturnValue.mAudioEvents = None
        ReturnValue_0: int32 = len(ReturnValue.mAudioEvents)
        ReturnValue_1: bool = Variable <= ReturnValue_0
        if not ReturnValue_1:
            goto('L562')
        Variable_0 = Variable
        ExecutionFlow.Push("L594")
        ReturnValue_2: FText = Default__KismetTextLibrary.Conv_StringToText("")
        
        ReturnValue_3: bool = Default__KismetTextLibrary.EqualEqual_TextText(Ref[Full Text], Ref[ReturnValue_2])
        if not ReturnValue_3:
            goto('L668')
        ReturnValue = Default__FGMessageBase.GetMessageDefaultObject(inClass)
        
        ReturnValue.mAudioEvents = None
        Item = None
        Item = ReturnValue.mAudioEvents[Variable_0]
        Full Text = Item.Subtitle
        goto(ExecutionFlow.Pop())
        # Label 562
        text = Full Text
        # End
        # Label 594
        ReturnValue_4: int32 = Variable + 1
        Variable = ReturnValue_4
        goto('L51')
        # Label 668
        ReturnValue = Default__FGMessageBase.GetMessageDefaultObject(inClass)
        
        ReturnValue.mAudioEvents = None
        Item = None
        Item = ReturnValue.mAudioEvents[Variable_0]
        FormatArgumentData.ArgumentName = "Added Text"
        FormatArgumentData.ArgumentValueType = 4
        FormatArgumentData.ArgumentValue = Item.Subtitle
        FormatArgumentData.ArgumentValueInt = 0
        FormatArgumentData.ArgumentValueFloat = 0
        FormatArgumentData.ArgumentValueGender = 0
        FormatArgumentData1.ArgumentName = "Full Text"
        FormatArgumentData1.ArgumentValueType = 4
        FormatArgumentData1.ArgumentValue = Full Text
        FormatArgumentData1.ArgumentValueInt = 0
        FormatArgumentData1.ArgumentValueFloat = 0
        FormatArgumentData1.ArgumentValueGender = 0
        Array: List[FormatArgumentData] = [FormatArgumentData1, FormatArgumentData]
        ReturnValue_5: FText = Default__KismetTextLibrary.Format("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 1282, 'Value': '{Full Text}\r\n<br></>\r\n{Added Text}'}", Array)
        Full Text = ReturnValue_5
        goto(ExecutionFlow.Pop())
    

    def GetAttachedFilesVisibility(self):
        if not self.IsAudioMessage:
            goto('L39')
        ReturnValue = 0
        goto('L59')
        # Label 39
        ReturnValue = 1
    

    def GetScrollButtonVisibility(self):
        Variable: uint8 = 4
        Variable1: uint8 = 1
        
        ReturnValue: int32 = len(self.mImages)
        ReturnValue_0: bool = ReturnValue > 1
        Variable_0: bool = ReturnValue_0
        
        switch = {
            False: Variable1,
            True: Variable
        }
        ReturnValue_1: uint8 = switch.get(Variable_0, None)
    

    def SetupImage(self):
        
        ReturnValue: int32 = len(self.mImages)
        # Label 59
        ReturnValue_0: bool = ReturnValue > 0
        if not ReturnValue_0:
            goto('L212')
        
        Item = None
        Item = self.mImages[self.mImageIndex]
        self.mImage.SetBrushFromTexture(Item, False)
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_Codex_Message(1775)
    

    def AddContent(self, contentClass: TSubclassOf[UserWidget]):
        ExecuteUbergraph_Widget_Codex_Message.K2Node_CustomEvent_contentClass = contentClass #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_Codex_Message(1794)
    

    def BndEvt__mScrollButton_K2Node_ComponentBoundEvent_40_OnClicked__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_Codex_Message(2313)
    

    def BndEvt__Button_0_K2Node_ComponentBoundEvent_0_OnButtonClickedEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_Codex_Message(2604)
    

    def ExecuteUbergraph_Widget_Codex_Message(self):
        
        Text = None
        # Label 10
        self.GenerateAudioMessage(self.mCurrentAudioMessage, Ref[Text])
        ReturnValue1: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue1_0: Ptr[Widget_Codex_Mail] = Default__WidgetBlueprintLibrary.Create(self, Widget_Codex_Mail, ReturnValue1)
        
        Text = None
        Default__KismetSystemLibrary.SetTextPropertyByName(ReturnValue1_0, "mText", Ref[Text])
        self.CurrentAudioTranscript = ReturnValue1_0
        ReturnValue1_1: Ptr[PanelSlot] = self.mMessageSlot.AddChild(self.CurrentAudioTranscript)
        self.IsAudioMessage = True
        # Label 271
        self.mImageIndex = 0
        self.SetupImage()
        ReturnValue: Ptr[FGMessageBase] = Default__FGMessageBase.GetMessageDefaultObject(Base)
        ReturnValue_0: Ptr[FGMessageSender] = Default__FGMessageSender.GetSenderDefaultObject(ReturnValue.mSenderClass)
        ReturnValue_1: bool = Default__KismetSystemLibrary.IsValid(ReturnValue_0)
        if not ReturnValue_1:
            goto('L2857')
        ReturnValue = Default__FGMessageBase.GetMessageDefaultObject(Base)
        ReturnValue_0 = Default__FGMessageSender.GetSenderDefaultObject(ReturnValue.mSenderClass)
        self.mFromName.SetText(ReturnValue_0.mSenderName)
        ReturnValue = Default__FGMessageBase.GetMessageDefaultObject(Base)
        ReturnValue_0 = Default__FGMessageSender.GetSenderDefaultObject(ReturnValue.mSenderClass)
        
        ReturnValue_0.mSenderMail = None
        ReturnValue1_2: FString = Default__KismetTextLibrary.Conv_TextToString(Ref[ReturnValue_0.mSenderMail])
        ReturnValue1_3: FString = Default__KismetStringLibrary.Concat_StrStr(" - ", ReturnValue1_2)
        ReturnValue1_4: FText = Default__KismetTextLibrary.Conv_StringToText(ReturnValue1_3)
        self.mFromMail.SetText(ReturnValue1_4)
        self.mToName.SetText("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 1098, 'Value': 'Employee'}")
        ReturnValue2: FString = Default__KismetStringLibrary.Concat_StrStr(" - ", "employee.05192.83.3845.710.8.192b@ficsit.biz")
        ReturnValue2_0: FText = Default__KismetTextLibrary.Conv_StringToText(ReturnValue2)
        self.mToMail.SetText(ReturnValue2_0)
        ReturnValue = Default__FGMessageBase.GetMessageDefaultObject(Base)
        self.mSubject.SetText(ReturnValue.mTitle)
        ReturnValue = Default__FGMessageBase.GetMessageDefaultObject(Base)
        
        ReturnValue.mTitle = None
        ReturnValue_2: FString = Default__KismetTextLibrary.Conv_TextToString(Ref[ReturnValue.mTitle])
        ReturnValue_3: FString = Default__KismetStringLibrary.Concat_StrStr(ReturnValue_2, ".flac")
        ReturnValue_4: FText = Default__KismetTextLibrary.Conv_StringToText(ReturnValue_3)
        self.mAttachedFileName.SetText(ReturnValue_4)
        # End
        self.ClearMessage()
        # End
        self.mMessageInfo.SetVisibility(4)
        self.mCurrentAudioMessage = None
        self.mMessageSlot.ClearChildren()
        Base: TSubclassOf[FGMessageBase] = ClassCast[FGMessageBase](contentClass)
        bSuccess1: bool = Base
        if not bSuccess1:
            goto('L2857')
        ReturnValue1_5: Ptr[FGMessageBase] = Default__FGMessageBase.GetMessageDefaultObject(Base)
        self.mImages = ReturnValue1_5.mImages
        Message: TSubclassOf[Widget_AudioMessage] = ClassCast[Widget_AudioMessage](contentClass)
        bSuccess: bool = Message
        if not bSuccess:
            goto('L2161')
        self.mCurrentAudioMessage = Message
        goto('L10')
        # Label 2161
        ReturnValue_5: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_6: Ptr[UserWidget] = Default__WidgetBlueprintLibrary.Create(self, contentClass, ReturnValue_5)
        ReturnValue_7: Ptr[PanelSlot] = self.mMessageSlot.AddChild(ReturnValue_6)
        self.IsAudioMessage = False
        goto('L271')
        ReturnValue_8: int32 = self.mImageIndex + 1
        Variable: int32 = ReturnValue_8
        self.mImageIndex = Variable
        
        ReturnValue_9: int32 = len(self.mImages)
        ReturnValue_10: int32 = ReturnValue_9 - 1
        ReturnValue_11: bool = Variable > ReturnValue_10
        if not ReturnValue_11:
            goto('L2585')
        self.mImageIndex = 0
        # Label 2585
        self.SetupImage()
        # End
        if not self.IsAudioMessage:
            goto('L2857')
        ReturnValue2_1: Ptr[PlayerController] = self.GetOwningPlayer()
        
        gameUI = None
        Default__HUDHelpers.GetFGGameUI(ReturnValue2_1, self, Ref[gameUI])
        gameUI.PlayAudioMessage(self.mCurrentAudioMessage)
        ReturnValue2_1 = self.GetOwningPlayer()
        
        gameUI = None
        Default__HUDHelpers.GetFGGameUI(ReturnValue2_1, self, Ref[gameUI])
        gameUI.PopAllWidgets()
    
