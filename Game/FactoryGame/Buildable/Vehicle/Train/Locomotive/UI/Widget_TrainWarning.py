
from codegen.ue4_stub import *

from Script.FactoryGame import GetSelfDrivingError
from Script.Engine import NotEqual_BoolBool
from Script.Engine import K2_SetTimerDelegate
from Script.Engine import Not_PreBool
from Script.Engine import Default__KismetSystemLibrary
from Script.UMG import PlayAnimation
from Script.Engine import TimerHandle
from Script.UMG import StopAnimation
from Script.Engine import NotEqual_TextText
from Script.Engine import Default__KismetTextLibrary
from Script.Engine import BooleanOR
from Game.FactoryGame.Buildable.Vehicle.Train.Locomotive.UI.Widget_TrainWarning import ExecuteUbergraph_Widget_TrainWarning
from Script.UMG import WidgetAnimation
from Script.Engine import NotEqual_ByteByte
from Script.UMG import UserWidget
from Script.FactoryGame import ESelfDrivingLocomotiveError
from Script.UMG import UMGSequencePlayer
from Script.UMG import IsAnimationPlaying
from Script.FactoryGame import FGTrain
from Game.FactoryGame.Buildable.Vehicle.Train.Locomotive.UI.Widget_TrainWarning import ExecuteUbergraph_Widget_TrainWarning.K2Node_CustomEvent_Train
from Script.Engine import K2_ClearAndInvalidateTimerHandle
from Script.Engine import PrintString
from Script.CoreUObject import LinearColor

class Widget_TrainWarning(UserWidget):
    WarningPulse: Ptr[WidgetAnimation]
    mTrain: Ptr[FGTrain]
    mUpdateTime: float = 1
    mCheckErrorsTimer: TimerHandle
    mCurrentWarning: uint8
    mForceWarning: bool
    mForcedWarningText: FText
    
    def ShouldForceWarning(self, ForceWarning: bool, WarningText: FText):
        ReturnValue: bool = NotEqual_BoolBool(ForceWarning, self.mForceWarning)
        
        ReturnValue_0: bool = Default__KismetTextLibrary.NotEqual_TextText(Ref[WarningText], Ref[self.mForcedWarningText])
        ReturnValue_1: bool = BooleanOR(ReturnValue, ReturnValue_0)
        if not ReturnValue_1:
            goto('L293')
        self.mForceWarning = ForceWarning
        self.mForcedWarningText = WarningText
        Default__KismetSystemLibrary.PrintString(self, "Warning", True, True, LinearColor(R = 1, G = 0.3777419924736023, B = 0, A = 1), 2)
        self.UpdateWarning()
    

    def UpdateWarning(self):
        if not self.mForceWarning:
            goto('L123')
        Default__KismetSystemLibrary.PrintString(self, "Hello", True, True, LinearColor(R = 0, G = 0.6600000262260437, B = 1, A = 1), 2)
        self.ShowWarning(self.mForcedWarningText)
        # End
        # Label 123
        ReturnValue: uint8 = self.mTrain.GetSelfDrivingError()
        self.mCurrentWarning = ReturnValue
        CmpSuccess: bool = NotEqual_ByteByte(self.mCurrentWarning, 0)
        if not CmpSuccess:
            goto('L475')
        CmpSuccess = NotEqual_ByteByte(self.mCurrentWarning, 1)
        if not CmpSuccess:
            goto('L494')
        CmpSuccess = NotEqual_ByteByte(self.mCurrentWarning, 2)
        if not CmpSuccess:
            goto('L588')
        CmpSuccess = NotEqual_ByteByte(self.mCurrentWarning, 3)
        if not CmpSuccess:
            goto('L664')
        CmpSuccess = NotEqual_ByteByte(self.mCurrentWarning, 4)
        if not CmpSuccess:
            goto('L744')
        CmpSuccess = NotEqual_ByteByte(self.mCurrentWarning, 5)
        if not CmpSuccess:
            goto('L835')
        # End
        # Label 475
        self.HideWarning()
        # End
        # Label 494
        WarningText = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 514, 'Value': 'No Power'}"
        # Label 560
        self.ShowWarning(WarningText)
        # End
        # Label 588
        WarningText = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 608, 'Value': 'No Time Table'}"
        goto('L560')
        # Label 664
        WarningText = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 684, 'Value': 'Invalid Next Stop'}"
        goto('L560')
        # Label 744
        WarningText = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 764, 'Value': 'Invalid Locomotive Placement'}"
        goto('L560')
        # Label 835
        WarningText = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 855, 'Value': 'Unable to reach next stop'}"
        goto('L560')
    

    def HideWarning(self):
        self.mWarning.SetVisibility(1)
        self.StopAnimation(self.WarningPulse)
    

    def ShowWarning(self, WarningText: FText):
        self.mWarningText.SetText(WarningText)
        self.mWarning.SetVisibility(0)
        ReturnValue: bool = self.IsAnimationPlaying(self.WarningPulse)
        ReturnValue_0: bool = Not_PreBool(ReturnValue)
        if not ReturnValue_0:
            goto('L201')
        ReturnValue_1: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.WarningPulse, 0, 0, 0, 1)
    

    def Init(self, Train: Ptr[FGTrain]):
        ExecuteUbergraph_Widget_TrainWarning.K2Node_CustomEvent_Train = Train #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_TrainWarning(10)
    

    def CheckErrors(self):
        self.ExecuteUbergraph_Widget_TrainWarning(167)
    

    def Destruct(self):
        self.ExecuteUbergraph_Widget_TrainWarning(288)
    

    def ExecuteUbergraph_Widget_TrainWarning(self):
        self.mTrain = Train
        self.CheckErrors()
        OutputDelegate.BindUFunction(self, CheckErrors)
        ReturnValue: TimerHandle = Default__KismetSystemLibrary.K2_SetTimerDelegate(OutputDelegate, self.mUpdateTime, True)
        self.mCheckErrorsTimer = ReturnValue
        # End
        ReturnValue_0: uint8 = self.mTrain.GetSelfDrivingError()
        ReturnValue_1: bool = NotEqual_ByteByte(self.mCurrentWarning, ReturnValue_0)
        if not ReturnValue_1:
            goto('L330')
        self.UpdateWarning()
        # End
        
        Default__KismetSystemLibrary.K2_ClearAndInvalidateTimerHandle(self, Ref[self.mCheckErrorsTimer])
    
