
from codegen.ue4_stub import *

from Game.FactoryGame.Interface.UI.InGame.BPW_AutosaveNotification import ExecuteUbergraph_BPW_AutosaveNotification
from Script.Engine import Delay
from Script.Engine import K2_SetTimerDelegate
from Script.Engine import Not_PreBool
from Script.Engine import LatentActionInfo
from Script.Engine import Default__KismetSystemLibrary
from Script.UMG import SetRenderTranslation
from Script.UMG import PlayAnimation
from Script.Engine import FormatArgumentData
from Game.FactoryGame.Interface.UI.InGame.BPW_AutosaveNotification import ExecuteUbergraph_BPW_AutosaveNotification.K2Node_CustomEvent_Delay
from Script.Engine import Conv_FloatToText
from Script.Engine import TimerHandle
from Script.UMG import StopAnimation
from Script.Engine import Default__KismetTextLibrary
from Script.Engine import Format
from Script.UMG import WidgetAnimation
from Script.UMG import UserWidget
from Script.UMG import UMGSequencePlayer
from Script.CoreUObject import Vector2D
from Script.Engine import K2_ClearAndInvalidateTimerHandle

class BPW_AutosaveNotification(UserWidget):
    animWarningBlink: Ptr[WidgetAnimation]
    animShowNotification: Ptr[WidgetAnimation]
    animSpinnerSpin: Ptr[WidgetAnimation]
    animAutosaveFinished: Ptr[WidgetAnimation]
    animAutosaveStart: Ptr[WidgetAnimation]
    animAutosaveInProgress: Ptr[WidgetAnimation]
    mAutosaveUpdateTimer: TimerHandle
    mTimeUntilAutosave: float
    mAutosaveFinished: bool
    
    def SetupTimeUntilAutosave(self, Time: float):
        self.mTimeUntilAutosave = Time
        self.UpdateAutosaveTimerText()
        OutputDelegate.BindUFunction(self, UpdateAutosaveTimerText)
        ReturnValue: TimerHandle = Default__KismetSystemLibrary.K2_SetTimerDelegate(OutputDelegate, 1, True)
        self.mAutosaveUpdateTimer = ReturnValue
    

    def OnAutosaveFinished(self):
        self.mAutosaveFinished = True
        self.mInProgress.SetRenderTranslation(Vector2D(X = 0, Y = 30))
        self.mWarning.SetRenderTranslation(Vector2D(X = 0, Y = 30))
        ReturnValue: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.animAutosaveFinished, 0, 1, 0, 1)
        self.mAutosaveText.SetTitle("AUTOSAVE COMPLETE!")
        self.mMessageText.SetText("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 262, 'Value': 'Save completed'}")
        self.CloseNotificationDelayed(4)
    

    def OnAutosaveInProgress(self):
        ReturnValue: bool = Not_PreBool(self.mAutosaveFinished)
        if not ReturnValue:
            goto('L353')
        ReturnValue1: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.animAutosaveInProgress, 0, 1, 0, 1)
        ReturnValue_0: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.animSpinnerSpin, 0, 0, 0, 1)
        self.StopAnimation(self.animWarningBlink)
        self.mWarning.SetRenderTranslation(Vector2D(X = 0, Y = 30))
        self.mAutosaveText.SetTitle("AUTOSAVE IN PROGRESS...")
        self.mMessageText.SetText("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 308, 'Value': 'Saving'}")
    

    def OnAutosaveStarting(self, TimeUntilAutosave: float):
        self.mAutosaveFinished = False
        self.mAutosaveText.SetTitle("AUTOSAVE STARTING...")
        ReturnValue2: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.animAutosaveStart, 0, 1, 0, 1)
        ReturnValue1: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.animShowNotification, 0, 1, 0, 1)
        ReturnValue: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.animWarningBlink, 0, 0, 0, 1)
        self.mAutosaveComplete.SetRenderTranslation(Vector2D(X = 0, Y = 30))
        self.SetupTimeUntilAutosave(TimeUntilAutosave)
    

    def Construct(self):
        self.ExecuteUbergraph_BPW_AutosaveNotification(801)
    

    def UpdateAutosaveTimerText(self):
        self.ExecuteUbergraph_BPW_AutosaveNotification(105)
    

    def CloseNotificationDelayed(self, Delay: float):
        ExecuteUbergraph_BPW_AutosaveNotification.K2Node_CustomEvent_Delay = Delay #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BPW_AutosaveNotification(802)
    

    def ExecuteUbergraph_BPW_AutosaveNotification(self):
        goto(ComputedJump("EntryPoint"))
        ReturnValue: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.animShowNotification, 0, 1, 1, 1)
        goto(ExecutionFlow.Pop())
        
        # Label 62
        Default__KismetSystemLibrary.K2_ClearAndInvalidateTimerHandle(self, Ref[self.mAutosaveUpdateTimer])
        goto(ExecutionFlow.Pop())
        ReturnValue_0: bool = Not_PreBool(self.mAutosaveFinished)
        if not ReturnValue_0:
            goto('L62')
        ReturnValue_1: FText = Default__KismetTextLibrary.Conv_FloatToText(self.mTimeUntilAutosave, 0, False, True, 1, 324, 0, 3)
        FormatArgumentData.ArgumentName = "time"
        FormatArgumentData.ArgumentValueType = 4
        FormatArgumentData.ArgumentValue = ReturnValue_1
        FormatArgumentData.ArgumentValueInt = 0
        FormatArgumentData.ArgumentValueFloat = 0
        FormatArgumentData.ArgumentValueGender = 0
        Array: List[FormatArgumentData] = [FormatArgumentData]
        ReturnValue_2: FText = Default__KismetTextLibrary.Format("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 493, 'Value': 'Autosave in {time}'}", Array)
        self.mMessageText.SetText(ReturnValue_2)
        ReturnValue_3: float = self.mTimeUntilAutosave - 1
        Variable: float = ReturnValue_3
        self.mTimeUntilAutosave = Variable
        ReturnValue_4: bool = self.mTimeUntilAutosave <= 0
        if not ReturnValue_4:
           goto(ExecutionFlow.Pop())
        
        Default__KismetSystemLibrary.K2_ClearAndInvalidateTimerHandle(self, Ref[self.mAutosaveUpdateTimer])
        self.OnAutosaveInProgress()
        goto(ExecutionFlow.Pop())
        goto(ExecutionFlow.Pop())
        Default__KismetSystemLibrary.Delay(self, Delay, LatentActionInfo(Linkage = 15, UUID = -511997260, ExecutionFunction = "ExecuteUbergraph_BPW_AutosaveNotification", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
    
