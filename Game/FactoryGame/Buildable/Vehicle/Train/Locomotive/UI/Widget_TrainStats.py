
from codegen.ue4_stub import *

from Game.FactoryGame.Buildable.Vehicle.Train.Locomotive.UI.Widget_TrainStats import ExecuteUbergraph_Widget_TrainStats.K2Node_ComponentBoundEvent_CommitMethod
from Game.FactoryGame.Buildable.Vehicle.Train.Locomotive.UI.Widget_TrainStats import ExecuteUbergraph_Widget_TrainStats.K2Node_CustomEvent_SelfDrivingEnabled
from Script.Engine import BooleanOR
from Script.UMG import ESlateVisibility
from Script.UMG import SetText
from Game.FactoryGame.Buildable.Vehicle.Train.Locomotive.UI.Widget_TrainStats import ExecuteUbergraph_Widget_TrainStats.K2Node_ComponentBoundEvent_IsTrue
from Script.Engine import EqualEqual_ByteByte
from Game.FactoryGame.Buildable.Vehicle.Train.Locomotive.UI.Widget_TrainStats import ExecuteUbergraph_Widget_TrainStats
from Game.FactoryGame.Buildable.Vehicle.Train.Locomotive.UI.Widget_TrainStats import ExecuteUbergraph_Widget_TrainStats.K2Node_Event_IsDesignTime
from Game.FactoryGame.Buildable.Vehicle.Train.Locomotive.UI.Widget_TrainStats import ExecuteUbergraph_Widget_TrainStats.K2Node_CustomEvent_DockingState
from Script.UMG import SetRenderOpacity
from Script.FactoryGame import ETrainDockingState
from Game.FactoryGame.Buildable.Vehicle.Train.Locomotive.UI.Widget_TrainStats import ExecuteUbergraph_Widget_TrainStats.K2Node_ComponentBoundEvent_Text
from Script.UMG import PreConstruct
from Script.UMG import UserWidget

class Widget_TrainStats(UserWidget):
    mTrainName: FText
    OnNameChanged: FMulticastScriptDelegate
    mSelfDrivingEnabled: bool
    OnAutopilotChanged: FMulticastScriptDelegate
    OnDockClicked: FMulticastScriptDelegate
    
    def UpdateDockingButton(self, State: uint8):
        Variable3: uint8 = 3
        Variable4: uint8 = 0
        Variable5: uint8 = 3
        Variable2: uint8 = State
        
        switch = {
            0: Variable5,
            1: Variable4,
            2: Variable3
        }
        self.mDockingButton.SetVisibility(switch.get(Variable2, None))
        Variable: float = 0.5
        Variable1: float = 1
        Variable2_0: float = 0.5
        Variable1_0: uint8 = State
        
        switch_0 = {
            0: Variable2_0,
            1: Variable1,
            2: Variable
        }
        self.mDockingButton.SetRenderOpacity(switch_0.get(Variable1_0, None))
        Variable_0: FText = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 411, 'Value': 'Docking...'}"
        Variable1_1: FText = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 479, 'Value': 'Dock'}"
        Variable2_1: FText = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 541, 'Value': 'Cannot Dock outside of Station'}"
        Variable_1: uint8 = State
        
        switch_1 = {
            0: Variable2_1,
            1: Variable1_1,
            2: Variable_0
        }
        self.mDockingButton.SetText(switch_1.get(Variable_1, None))
    

    def SetTitle(self, mTrainName: FText):
        self.mTrainName = mTrainName
        self.mTrainNameInputBox.SetText(self.mTrainName)
    

    def BndEvt__mTrainNameInputBox_K2Node_ComponentBoundEvent_1_OnEditableTextCommittedEvent__DelegateSignature(self, text: Const[Ref[FText]], CommitMethod: uint8):
        ExecuteUbergraph_Widget_TrainStats.K2Node_ComponentBoundEvent_Text = text #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_TrainStats.K2Node_ComponentBoundEvent_CommitMethod = CommitMethod #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_TrainStats(34)
    

    def PreConstruct(self):
        ExecuteUbergraph_Widget_TrainStats.K2Node_Event_IsDesignTime = IsDesignTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_TrainStats(204)
    

    def Destruct(self):
        self.ExecuteUbergraph_Widget_TrainStats(251)
    

    def Init(self, SelfDrivingEnabled: bool, DockingState: uint8):
        ExecuteUbergraph_Widget_TrainStats.K2Node_CustomEvent_SelfDrivingEnabled = SelfDrivingEnabled #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_TrainStats.K2Node_CustomEvent_DockingState = DockingState #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_TrainStats(283)
    

    def BndEvt__Widget_StandardButton_Togglable_K2Node_ComponentBoundEvent_2_OnStateChanged__DelegateSignature(self, IsTrue: bool):
        ExecuteUbergraph_Widget_TrainStats.K2Node_ComponentBoundEvent_IsTrue = IsTrue #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_TrainStats(375)
    

    def BndEvt__Widget_StandardButton_K2Node_ComponentBoundEvent_3_OnClicked__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_TrainStats(408)
    

    def ExecuteUbergraph_Widget_TrainStats(self):
        # Label 10
        self.OnDockClicked.ProcessMulticastDelegate()
        # End
        ReturnValue: bool = EqualEqual_ByteByte(CommitMethod, 1)
        ReturnValue1: bool = EqualEqual_ByteByte(CommitMethod, 2)
        ReturnValue_0: bool = BooleanOR(ReturnValue, ReturnValue1)
        if not ReturnValue_0:
            goto('L413')
        self.SetTitle(Text)
        self.OnNameChanged.ProcessMulticastDelegate(self.mTrainName)
        # End
        self.PreConstruct(IsDesignTime)
        self.SetTitle(self.mTrainName)
        # End
        self.mTrainName = self.mTrainName
        # End
        self.mSelfDrivingEnabled = SelfDrivingEnabled
        self.mAutopilotButton.Init(self.mSelfDrivingEnabled)
        self.UpdateDockingButton(DockingState)
        # End
        self.OnAutopilotChanged.ProcessMulticastDelegate(IsTrue)
        # End
        goto('L10')
    

    def OnDockClicked__DelegateSignature(self):
        pass
    

    def OnAutopilotChanged__DelegateSignature(self, SelfDrivingEnabled: bool):
        pass
    

    def OnNameChanged__DelegateSignature(self, mName: FText):
        pass
    
