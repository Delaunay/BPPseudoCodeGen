
from codegen.ue4_stub import *

from Script.AkAudio import PostAkEvent
from Script.Engine import Delay
from Script.Engine import K2_SetTimerDelegate
from Script.Engine import Pawn
from Script.Engine import LatentActionInfo
from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import PlayerController
from Script.Engine import FormatArgumentData
from Script.UMG import PlayAnimation
from Script.Engine import TimerHandle
from Script.FactoryGame import FGMessageBase
from Script.Engine import Default__KismetTextLibrary
from Game.FactoryGame.Interface.UI.Audio.Codex.Play_UI_CodexMessage_Blip import Play_UI_CodexMessage_Blip
from Script.Engine import Format
from Script.UMG import WidgetAnimation
from Script.AkAudio import Default__AkGameplayStatics
from Script.UMG import UserWidget
from Game.FactoryGame.Interface.UI.InGame.Widget_MessageNotifier import ExecuteUbergraph_Widget_MessageNotifier.K2Node_Event_IsDesignTime
from Script.UMG import GetOwningPlayerPawn
from Game.FactoryGame.Interface.UI.HUDHelpers.HUDHelpers import Default__HUDHelpers
from Game.FactoryGame.Interface.UI.InGame.Widget_MessageNotifier import ExecuteUbergraph_Widget_MessageNotifier
from Script.UMG import UMGSequencePlayer
from Script.AkAudio import AkComponent

class Widget_MessageNotifier(UserWidget):
    SpawnAnimation: Ptr[WidgetAnimation]
    mMessage: TSubclassOf[FGMessageBase]
    mTimerHandle: TimerHandle
    mText: FText = NSLOCTEXT("", "CAD24A63495F3BC7C4A0AFBBD333D96E", "No preview info available")
    mActive: bool
    mTimeToLive: float = 3
    
    def GetKeyForAction(self):
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        
        button = None
        Default__HUDHelpers.GetKeyNameForActionSimple(ReturnValue, "OpenCodex", self, Ref[button])
        keyText = button
    

    def PreConstruct(self):
        ExecuteUbergraph_Widget_MessageNotifier.K2Node_Event_IsDesignTime = IsDesignTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_MessageNotifier(30)
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_MessageNotifier(428)
    

    def RemoveNotifier(self):
        self.ExecuteUbergraph_Widget_MessageNotifier(648)
    

    def ExecuteUbergraph_Widget_MessageNotifier(self):
        goto(ComputedJump("EntryPoint"))
        self.RemoveFromParent()
        goto(ExecutionFlow.Pop())
        
        keyText = None
        self.GetKeyForAction(Ref[keyText])
        FormatArgumentData.ArgumentName = "KEY"
        FormatArgumentData.ArgumentValueType = 4
        FormatArgumentData.ArgumentValue = keyText
        FormatArgumentData.ArgumentValueInt = 0
        FormatArgumentData.ArgumentValueFloat = 0
        FormatArgumentData.ArgumentValueGender = 0
        Array: List[FormatArgumentData] = [FormatArgumentData]
        ReturnValue: FText = Default__KismetTextLibrary.Format("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 314, 'Value': 'Press {KEY} to open.'}", Array)
        self.mKeyShortcut.SetText(ReturnValue)
        goto(ExecutionFlow.Pop())
        ReturnValue_0: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.SpawnAnimation, 0, 1, 0, 1.2000000476837158)
        OutputDelegate.BindUFunction(self, RemoveNotifier)
        ReturnValue_1: TimerHandle = Default__KismetSystemLibrary.K2_SetTimerDelegate(OutputDelegate, self.mTimeToLive, False)
        ReturnValue_2: Ptr[Pawn] = self.GetOwningPlayerPawn()
        ReturnValue_3: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_UI_CodexMessage_Blip, ReturnValue_2, True)
        goto(ExecutionFlow.Pop())
        ReturnValue1: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.SpawnAnimation, 0, 1, 1, 1.7999999523162842)
        Default__KismetSystemLibrary.Delay(self, 1, LatentActionInfo(Linkage = 15, UUID = 618605932, ExecutionFunction = "ExecuteUbergraph_Widget_MessageNotifier", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
    
