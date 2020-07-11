
from codegen.ue4_stub import *

from Script.Engine import Delay
from Game.FactoryGame.Interface.UI.Notifications.Widget_RestartNotification import ExecuteUbergraph_Widget_RestartNotification
from Script.Engine import LatentActionInfo
from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import GameStateBase
from Script.Engine import FormatArgumentData
from Script.UMG import PlayAnimation
from Game.FactoryGame.Interface.UI.Notifications.Widget_RestartNotification import ExecuteUbergraph_Widget_RestartNotification.K2Node_Event_IsDesignTime
from Script.Engine import Default__KismetTextLibrary
from Script.Engine import Default__GameplayStatics
from Script.FactoryGame import FGGameState
from Script.Engine import Format
from Script.Engine import MakeLiteralText
from Script.UMG import WidgetAnimation
from Game.FactoryGame.Interface.UI.Notifications.Widget_RestartNotification import ExecuteUbergraph_Widget_RestartNotification.K2Node_CustomEvent_timeLeft
from Script.UMG import UserWidget
from Script.UMG import UMGSequencePlayer
from Script.Engine import GetGameState
from Script.Engine import Round

class Widget_RestartNotification(UserWidget):
    SpawnAnim: Ptr[WidgetAnimation]
    mTimeLeftText: FText = NewObject[ServerRestartTable", "ServerRestartNotificationString")]()
    
    def GetTimeText(self, timeToRestart: float):
        ReturnValue: float = timeToRestart - 3600
        ReturnValue_0: bool = ReturnValue > 0
        if not ReturnValue_0:
            goto('L821')
        ReturnValue2: FText = Default__KismetSystemLibrary.MakeLiteralText(STRING_TABLE_ENTRY("StringTable /Game/FactoryGame/Interface/UI/ServerRestartTable.ServerRestartTable", "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 219, 'Value': 'HoursString'}")
        FormatArgumentData4.ArgumentName = "units"
        FormatArgumentData4.ArgumentValueType = 4
        FormatArgumentData4.ArgumentValue = ReturnValue2
        FormatArgumentData4.ArgumentValueInt = 0
        FormatArgumentData4.ArgumentValueFloat = 0
        FormatArgumentData4.ArgumentValueGender = 0
        ReturnValue1: float = timeToRestart / 3600
        # Label 467
        ReturnValue2_0: int32 = Round(ReturnValue1)
        FormatArgumentData5.ArgumentName = "time"
        FormatArgumentData5.ArgumentValueType = 0
        FormatArgumentData5.ArgumentValue = 
        FormatArgumentData5.ArgumentValueInt = ReturnValue2_0
        FormatArgumentData5.ArgumentValueFloat = 0
        FormatArgumentData5.ArgumentValueGender = 0
        Array2: List[FormatArgumentData] = [FormatArgumentData5, FormatArgumentData4]
        ReturnValue2_1: FText = Default__KismetTextLibrary.Format(self.mTimeLeftText, Array2)
        text = ReturnValue2_1
        # End
        # Label 821
        ReturnValue1_0: float = timeToRestart - 60
        ReturnValue1_1: bool = ReturnValue1_0 > 0
        if not ReturnValue1_1:
            goto('L1644')
        ReturnValue1_2: FText = Default__KismetSystemLibrary.MakeLiteralText(STRING_TABLE_ENTRY("StringTable /Game/FactoryGame/Interface/UI/ServerRestartTable.ServerRestartTable", "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 1040, 'Value': 'MinutesString'}")
        FormatArgumentData2.ArgumentName = "units"
        FormatArgumentData2.ArgumentValueType = 4
        FormatArgumentData2.ArgumentValue = ReturnValue1_2
        FormatArgumentData2.ArgumentValueInt = 0
        FormatArgumentData2.ArgumentValueFloat = 0
        FormatArgumentData2.ArgumentValueGender = 0
        ReturnValue_1: float = timeToRestart / 60
        ReturnValue1_3: int32 = Round(ReturnValue_1)
        FormatArgumentData3.ArgumentName = "time"
        FormatArgumentData3.ArgumentValueType = 0
        FormatArgumentData3.ArgumentValue = 
        FormatArgumentData3.ArgumentValueInt = ReturnValue1_3
        FormatArgumentData3.ArgumentValueFloat = 0
        FormatArgumentData3.ArgumentValueGender = 0
        Array1: List[FormatArgumentData] = [FormatArgumentData3, FormatArgumentData2]
        ReturnValue1_4: FText = Default__KismetTextLibrary.Format(self.mTimeLeftText, Array1)
        text = ReturnValue1_4
        # End
        # Label 1644
        ReturnValue_2: int32 = Round(timeToRestart)
        FormatArgumentData.ArgumentName = "time"
        FormatArgumentData.ArgumentValueType = 0
        FormatArgumentData.ArgumentValue = 
        FormatArgumentData.ArgumentValueInt = ReturnValue_2
        FormatArgumentData.ArgumentValueFloat = 0
        FormatArgumentData.ArgumentValueGender = 0
        ReturnValue_3: FText = Default__KismetSystemLibrary.MakeLiteralText(STRING_TABLE_ENTRY("StringTable /Game/FactoryGame/Interface/UI/ServerRestartTable.ServerRestartTable", "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 1998, 'Value': 'SecondsString'}")
        FormatArgumentData1.ArgumentName = "units"
        FormatArgumentData1.ArgumentValueType = 4
        FormatArgumentData1.ArgumentValue = ReturnValue_3
        FormatArgumentData1.ArgumentValueInt = 0
        FormatArgumentData1.ArgumentValueFloat = 0
        FormatArgumentData1.ArgumentValueGender = 0
        Array: List[FormatArgumentData] = [FormatArgumentData, FormatArgumentData1]
        ReturnValue_4: FText = Default__KismetTextLibrary.Format(self.mTimeLeftText, Array)
        text = ReturnValue_4
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_RestartNotification(279)
    

    def Destruct(self):
        self.ExecuteUbergraph_Widget_RestartNotification(284)
    

    def OnTimeLeftUpdated(self, timeLeft: float):
        ExecuteUbergraph_Widget_RestartNotification.K2Node_CustomEvent_timeLeft = timeLeft #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_RestartNotification(514)
    

    def PreConstruct(self):
        ExecuteUbergraph_Widget_RestartNotification.K2Node_Event_IsDesignTime = IsDesignTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_RestartNotification(596)
    

    def ExecuteUbergraph_Widget_RestartNotification(self):
        goto(ComputedJump("EntryPoint"))
        # Label 15
        ReturnValue: Ptr[GameStateBase] = Default__GameplayStatics.GetGameState(self)
        State: Ptr[FGGameState] = Cast[FGGameState](ReturnValue)
        bSuccess: bool = State
        if not bSuccess:
            goto('L202')
        OutputDelegate.BindUFunction(self, OnTimeLeftUpdated)
        State.mOnRestartTimeNotification.AddUnique(OutputDelegate)
        goto(ExecutionFlow.Pop())
        # Label 202
        Default__KismetSystemLibrary.Delay(self, 0.009999999776482582, LatentActionInfo(Linkage = 15, UUID = 1946865055, ExecutionFunction = "ExecuteUbergraph_Widget_RestartNotification", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        goto('L15')
        ReturnValue1: Ptr[GameStateBase] = Default__GameplayStatics.GetGameState(self)
        State1: Ptr[FGGameState] = Cast[FGGameState](ReturnValue1)
        bSuccess1: bool = State1
        if not bSuccess1:
           goto(ExecutionFlow.Pop())
        OutputDelegate.BindUFunction(self, OnTimeLeftUpdated)
        State1.mOnRestartTimeNotification.Remove(OutputDelegate)
        goto(ExecutionFlow.Pop())
        # Label 467
        ReturnValue_0: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.SpawnAnim, 0, 1, 2, 1)
        goto(ExecutionFlow.Pop())
        
        text = None
        self.GetTimeText(timeLeft, Ref[text])
        self.mTimeLeftLabel.SetText(text)
        goto('L467')
        self.mTimeLeftLabel.SetText(self.mTimeLeftText)
        goto(ExecutionFlow.Pop())
    
