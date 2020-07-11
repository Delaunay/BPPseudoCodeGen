
from codegen.ue4_stub import *

from Script.Engine import Conv_TextToString
from Script.FactoryGame import PlayNextDialogue
from Script.FactoryGame import GetSenderDefaultObject
from Script.FactoryGame import StartPlayback
from Game.FactoryGame.Interface.UI.Message.Widget_AudioMessage import ExecuteUbergraph_Widget_AudioMessage
from Script.Engine import Default__KismetSystemLibrary
from Script.FactoryGame import FGAudioMessage
from Script.UMG import PlayAnimation
from Script.UMG import Destruct
from Script.UMG import UnbindAllFromAnimationFinished
from Script.FactoryGame import FGMessageSender
from Script.FactoryGame import Default__FGMessageSender
from Script.Engine import Default__KismetTextLibrary
from Script.UMG import Construct
from Script.FactoryGame import AudioSubtitlePair
from Script.UMG import WidgetAnimation
from Game.FactoryGame.Interface.UI.HUDHelpers.HUDHelpers import Default__HUDHelpers
from Script.Engine import RandomIntegerInRange
from Script.UMG import UMGSequencePlayer
from Script.FactoryGame import GetCurrentDialogue
from Script.UMG import BindToAnimationFinished
from Script.Engine import IsValidClass
from Script.Engine import RandomFloatInRange

class Widget_AudioMessage(FGAudioMessage):
    IncomingAnimation: Ptr[WidgetAnimation]
    mSubtitleTimeMultiplier = 0.06499999761581421
    mSenderClass = NewObject[Sender_CEO]()
    
    def SetSenderInfo(self, inSender: TSubclassOf[FGMessageSender]):
        localSender = inSender
        ReturnValue2: Ptr[FGMessageSender] = Default__FGMessageSender.GetSenderDefaultObject(localSender)
        
        ReturnValue2.mSenderName = None
        ReturnValue1: FString = Default__KismetTextLibrary.Conv_TextToString(Ref[ReturnValue2.mSenderName])
        self.mSubtitleWidget.mSender.SetTitle(ReturnValue1)
        ReturnValue1_0: Ptr[FGMessageSender] = Default__FGMessageSender.GetSenderDefaultObject(localSender)
        
        ReturnValue1_0.mSenderMail = None
        ReturnValue: FString = Default__KismetTextLibrary.Conv_TextToString(Ref[ReturnValue1_0.mSenderMail])
        self.mSubtitleWidget.mSenderEmail2.SetTitle(ReturnValue)
        ReturnValue_0: Ptr[FGMessageSender] = Default__FGMessageSender.GetSenderDefaultObject(localSender)
        SlateBrush.ImageSize = self.mSubtitleWidget.SenderIcon.Brush.ImageSize
        SlateBrush.Margin = self.mSubtitleWidget.SenderIcon.Brush.Margin
        SlateBrush.TintColor = self.mSubtitleWidget.SenderIcon.Brush.TintColor
        SlateBrush.ResourceObject = ReturnValue_0.mTexture
        SlateBrush.DrawAs = self.mSubtitleWidget.SenderIcon.Brush.DrawAs
        SlateBrush.Tiling = self.mSubtitleWidget.SenderIcon.Brush.Tiling
        SlateBrush.Mirroring = self.mSubtitleWidget.SenderIcon.Brush.Mirroring
        
        SlateBrush = None
        self.mSubtitleWidget.SenderIcon.SetBrush(Ref[SlateBrush])
    

    def GetDarkGray(self):
        
        Text = None
        Graphics = None
        Default__HUDHelpers.GetFactoryGameDarkGray(self, Ref[Text], Ref[Graphics])
        ReturnValue = Graphics
    

    def PlayNextDialogue(self):
        self.ExecuteUbergraph_Widget_AudioMessage(25)
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_AudioMessage(306)
    

    def ShowContent(self):
        self.ExecuteUbergraph_Widget_AudioMessage(502)
    

    def Destruct(self):
        self.ExecuteUbergraph_Widget_AudioMessage(816)
    

    def ExecuteUbergraph_Widget_AudioMessage(self):
        # Label 10
        self.StartPlayback()
        # End
        self.PlayNextDialogue()
        ReturnValue: AudioSubtitlePair = self.GetCurrentDialogue()
        self.mSubtitleWidget.mText.SetText(ReturnValue.Subtitle)
        ReturnValue1: AudioSubtitlePair = self.GetCurrentDialogue()
        ReturnValue_0: bool = Default__KismetSystemLibrary.IsValidClass(ReturnValue1.SenderClass)
        if not ReturnValue_0:
            goto('L845')
        ReturnValue1 = self.GetCurrentDialogue()
        self.SetSenderInfo(ReturnValue1.SenderClass)
        # End
        self.Construct()
        ReturnValue_1: int32 = RandomIntegerInRange(1, 3)
        ReturnValue_2: float = RandomFloatInRange(1.399999976158142, 1.7999999523162842)
        ReturnValue1_0: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.IncomingAnimation, 0, ReturnValue_1, 0, ReturnValue_2)
        OutputDelegate.BindUFunction(self, ShowContent)
        self.BindToAnimationFinished(self.IncomingAnimation, OutputDelegate)
        # End
        self.mIncomingText.SetVisibility(2)
        self.mIncomingMessageOverlay.SetVisibility(2)
        self.mSubtitleWidget.mText.SetText(self.mAudioEvents[0].Subtitle)
        self.SetSenderInfo(self.mSenderClass)
        ReturnValue_3: Ptr[UMGSequencePlayer] = self.mSubtitleWidget.PlayAnimation(self.mSubtitleWidget.SpawnAnimation, 0, 1, 0, 1)
        self.Overlay_1.SetVisibility(4)
        goto('L10')
        self.Destruct()
        self.UnbindAllFromAnimationFinished(self.IncomingAnimation)
    
