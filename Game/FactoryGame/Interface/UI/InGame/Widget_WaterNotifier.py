
from codegen.ue4_stub import *

from Script.Engine import Default__KismetSystemLibrary
from Script.UMG import GetOwningPlayerPawn
from Script.Engine import Conv_TextToString
from Script.AkAudio import PostAkEvent
from Script.UMG import UserWidget
from Script.UMG import UMGSequencePlayer
from Game.FactoryGame.Interface.UI.Audio.Codex.Play_UI_CodexMessage_Blip import Play_UI_CodexMessage_Blip
from Script.UMG import PlayAnimation
from Game.FactoryGame.Interface.UI.InGame.Widget_WaterNotifier import ExecuteUbergraph_Widget_WaterNotifier
from Script.Engine import K2_SetTimerDelegate
from Script.Engine import Delay
from Script.Engine import TimerHandle
from Script.Engine import Pawn
from Script.AkAudio import AkComponent
from Script.UMG import WidgetAnimation
from Script.AkAudio import Default__AkGameplayStatics
from Script.Engine import LatentActionInfo
from Script.Engine import Default__KismetTextLibrary

class Widget_WaterNotifier(UserWidget):
    SpawnAnimation: Ptr[WidgetAnimation]
    mTimerHandle: TimerHandle
    mText: FText = NSLOCTEXT("", "D81E1B2D422AFFBDC8E861A3541BF7E3", "No preview info available")
    mActive: bool
    mTimeToLive: float = 7
    mTitleMessageText: FText
    
    def SetTitleText(self, messageText: FText):
        self.mTitleMessageText = messageText
        
        ReturnValue: FString = Default__KismetTextLibrary.Conv_TextToString(Ref[self.mTitleMessageText])
        self.Widget_LetterSpacedText.SetTitle(ReturnValue)
    

    def SetMessageText(self, messageText: FText):
        self.mText = messageText
        self.mMessageText.SetText(self.mText)
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_WaterNotifier(77)
    

    def RemoveNotifier(self):
        self.ExecuteUbergraph_Widget_WaterNotifier(301)
    

    def ExecuteUbergraph_Widget_WaterNotifier(self):
        goto(ComputedJump("EntryPoint"))
        self.RemoveFromParent()
        goto(ExecutionFlow.Pop())
        # Label 30
        self.SetMessageText(self.mText)
        self.SetTitleText(self.mTitleMessageText)
        goto(ExecutionFlow.Pop())
        ReturnValue: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.SpawnAnimation, 0, 1, 0, 0.800000011920929)
        OutputDelegate.BindUFunction(self, RemoveNotifier)
        ReturnValue_0: TimerHandle = Default__KismetSystemLibrary.K2_SetTimerDelegate(OutputDelegate, self.mTimeToLive, False)
        ReturnValue_1: Ptr[Pawn] = self.GetOwningPlayerPawn()
        ReturnValue_2: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_UI_CodexMessage_Blip, ReturnValue_1, True)
        goto('L30')
        ReturnValue1: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.SpawnAnimation, 0, 1, 1, 1)
        Default__KismetSystemLibrary.Delay(self, 1, LatentActionInfo(Linkage = 15, UUID = 342720649, ExecutionFunction = "ExecuteUbergraph_Widget_WaterNotifier", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
    
