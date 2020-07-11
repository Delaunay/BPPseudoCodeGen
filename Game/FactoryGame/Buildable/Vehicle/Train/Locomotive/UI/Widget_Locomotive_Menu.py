
from codegen.ue4_stub import *

from Script.Engine import Delay
from Script.Engine import K2_SetTimerDelegate
from Script.FactoryGame import GetTargetConsumption
from Script.FactoryGame import FGPowerInfoComponent
from Script.FactoryGame import HasPower
from Script.Engine import Not_PreBool
from Game.FactoryGame.Buildable.Vehicle.Train.Locomotive.UI.Widget_Locomotive_Menu import ExecuteUbergraph_Widget_Locomotive_Menu.K2Node_CustomEvent_state
from Script.Engine import LatentActionInfo
from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import PlayerController
from Script.FactoryGame import GetDockingState
from Script.FactoryGame import OnEscapePressed
from Script.Engine import Conv_FloatToText
from Script.Engine import TimerHandle
from Game.FactoryGame.Buildable.Vehicle.Train.Locomotive.UI.Widget_Locomotive_Menu import ExecuteUbergraph_Widget_Locomotive_Menu.K2Node_CustomEvent_mName
from Script.Engine import IsValid
from Script.UMG import Destruct
from Script.FactoryGame import CmS2KmH
from Game.FactoryGame.Buildable.Vehicle.Train.Locomotive.UI.Widget_Locomotive_Menu import ExecuteUbergraph_Widget_Locomotive_Menu.K2Node_ComponentBoundEvent_SelfDrivingEnabled
from Script.Engine import Default__KismetTextLibrary
from Script.FactoryGame import GetTrainName
from Script.FactoryGame import FGInteractWidget
from Game.FactoryGame.Buildable.Vehicle.Train.Locomotive.UI.Widget_Locomotive_Menu import ExecuteUbergraph_Widget_Locomotive_Menu
from Script.FactoryGame import GetTrain
from Script.FactoryGame import FGLocomotiveMovementComponent
from Script.FactoryGame import IsSelfDrivingEnabled
from Script.FactoryGame import GetLocomotiveMovementComponent
from Script.FactoryGame import Default__FGBlueprintFunctionLibrary
from Script.FactoryGame import FGLocomotive
from Game.FactoryGame.Interface.UI.HUDHelpers.BPHUDHelpers import Default__BPHUDHelpers
from Script.Engine import Abs
from Script.FactoryGame import FGTrain
from Script.FactoryGame import ETrainDockingState
from Script.Engine import K2_ClearAndInvalidateTimerHandle
from Script.FactoryGame import GetForwardSpeed
from Script.FactoryGame import GetPowerInfo

class Widget_Locomotive_Menu(FGInteractWidget):
    FGLocomotive: Ptr[FGLocomotive]
    mUpdateStatsTimer: TimerHandle
    mTrain: Ptr[FGTrain]
    OnClose: FMulticastScriptDelegate
    OnTrainNameChanged: FMulticastScriptDelegate
    mFakeHasPower: bool = True
    mUseMouse = True
    mRestoreFocusWhenLost = True
    mDesiredHorizontalAlignment = 2
    mDesiredVerticalAlignment = 2
    mCallCustomTickOnConstruct = True
    
    def UpdatePowerStatus(self):
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(self.FGLocomotive)
        if not ReturnValue:
            goto('L317')
        ReturnValue_0: Ptr[FGPowerInfoComponent] = self.FGLocomotive.GetPowerInfo()
        ReturnValue_1: bool = ReturnValue_0.HasPower()
        LocalHasPower = ReturnValue_1
        # Label 168
        ReturnValue_2: bool = Not_PreBool(LocalHasPower)
        self.Widget_TrainStats.Widget_TrainWarning.ShouldForceWarning(ReturnValue_2, "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 265, 'Value': 'No Power'}")
        # End
        # Label 317
        LocalHasPower = self.mFakeHasPower
        goto('L168')
    

    def GetLocomotiveSpeed(self, Locomotive: Ptr[FGLocomotive]):
        ReturnValue: Ptr[FGLocomotiveMovementComponent] = Locomotive.GetLocomotiveMovementComponent()
        ReturnValue_0: float = ReturnValue.GetForwardSpeed()
        ReturnValue_1: float = Default__FGBlueprintFunctionLibrary.CmS2KmH(ReturnValue_0)
        ReturnValue_2: float = Abs(ReturnValue_1)
        ReturnValue_3: FText = Default__KismetTextLibrary.Conv_FloatToText(ReturnValue_2, 0, False, True, 1, 324, 0, 0)
        self.Widget_TrainStats.mTrainSpeedText.SetText(ReturnValue_3)
    

    def GetPowerConsumption(self, Locomotive: Ptr[FGLocomotive]):
        ReturnValue: Ptr[FGPowerInfoComponent] = Locomotive.GetPowerInfo()
        ReturnValue_0: float = ReturnValue.GetTargetConsumption()
        ReturnValue_1: FText = Default__KismetTextLibrary.Conv_FloatToText(ReturnValue_0, 0, False, True, 1, 324, 0, 0)
        self.Widget_TrainStats.mTrainPowerConsumptionText.SetText(ReturnValue_1)
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_Locomotive_Menu(912)
    

    def Init(self):
        self.ExecuteUbergraph_Widget_Locomotive_Menu(1061)
    

    def Destruct(self):
        self.ExecuteUbergraph_Widget_Locomotive_Menu(1156)
    

    def UpdateLocomotiveStats(self):
        self.ExecuteUbergraph_Widget_Locomotive_Menu(1213)
    

    def OnEscapePressed(self):
        self.ExecuteUbergraph_Widget_Locomotive_Menu(1445)
    

    def OnNameChanged(self, mName: FText):
        ExecuteUbergraph_Widget_Locomotive_Menu.K2Node_CustomEvent_mName = mName #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_Locomotive_Menu(1450)
    

    def BndEvt__Widget_TrainStats_K2Node_ComponentBoundEvent_1_OnAutopilotChanged__DelegateSignature(self, SelfDrivingEnabled: bool):
        ExecuteUbergraph_Widget_Locomotive_Menu.K2Node_ComponentBoundEvent_SelfDrivingEnabled = SelfDrivingEnabled #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_Locomotive_Menu(1603)
    

    def BndEvt__Widget_TrainStats_K2Node_ComponentBoundEvent_0_OnDockClicked__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_Locomotive_Menu(1737)
    

    def OnDockingStateChanged(self, State: uint8):
        ExecuteUbergraph_Widget_Locomotive_Menu.K2Node_CustomEvent_state = State #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_Locomotive_Menu(1862)
    

    def ExecuteUbergraph_Widget_Locomotive_Menu(self):
        goto(ComputedJump("EntryPoint"))
        # Label 15
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(self.FGLocomotive)
        if not ReturnValue:
            goto('L802')
        ReturnValue_0: Ptr[FGTrain] = self.FGLocomotive.GetTrain()
        self.mTrain = ReturnValue_0
        # Label 141
        self.Widget_Train_TimeTable.Init(self.mTrain)
        OutputDelegate1.BindUFunction(self, OnEscapePressed)
        self.Widget_Window_DarkMode.OnClose.AddUnique(OutputDelegate1)
        OutputDelegate3.BindUFunction(self, OnNameChanged)
        self.Widget_TrainStats.OnNameChanged.AddUnique(OutputDelegate3)
        OutputDelegate2.BindUFunction(self, UpdateLocomotiveStats)
        ReturnValue_1: TimerHandle = Default__KismetSystemLibrary.K2_SetTimerDelegate(OutputDelegate2, 0.20000000298023224, True)
        self.mUpdateStatsTimer = ReturnValue_1
        ReturnValue_2: FText = self.mTrain.GetTrainName()
        self.Widget_TrainStats.SetTitle(ReturnValue_2)
        self.Widget_TrainStats.Widget_TrainWarning.Init(self.mTrain)
        ReturnValue_3: uint8 = self.mTrain.GetDockingState()
        ReturnValue_4: bool = self.mTrain.IsSelfDrivingEnabled()
        self.Widget_TrainStats.Init(ReturnValue_4, ReturnValue_3)
        OutputDelegate.BindUFunction(self, OnDockingStateChanged)
        self.mTrain.mOnDockingStateChanged.AddUnique(OutputDelegate)
        goto(ExecutionFlow.Pop())
        # Label 802
        Default__KismetSystemLibrary.Delay(self, 0.10000000149011612, LatentActionInfo(Linkage = 15, UUID = -57680593, ExecutionFunction = "ExecuteUbergraph_Widget_Locomotive_Menu", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        # Label 879
        self.mTrain.mOnDockingStateChanged.Clear()
        goto(ExecutionFlow.Pop())
        ReturnValue2: bool = Default__KismetSystemLibrary.IsValid(self.mTrain)
        if not ReturnValue2:
            goto('L15')
        self.mTrain = self.mTrain
        self.Widget_TrainStats.mAddidtionalStatsContainer.SetVisibility(1)
        goto('L141')
        AsFGLocomotive: Ptr[FGLocomotive] = Cast[FGLocomotive](self.mInteractObject)
        bSuccess: bool = AsFGLocomotive
        if not bSuccess:
           goto(ExecutionFlow.Pop())
        self.FGLocomotive = AsFGLocomotive
        goto(ExecutionFlow.Pop())
        self.Destruct()
        
        Default__KismetSystemLibrary.K2_ClearAndInvalidateTimerHandle(self, Ref[self.mUpdateStatsTimer])
        goto('L879')
        self.UpdatePowerStatus()
        ReturnValue3: bool = Default__KismetSystemLibrary.IsValid(self.FGLocomotive)
        if not ReturnValue3:
           goto(ExecutionFlow.Pop())
        self.GetLocomotiveSpeed(self.FGLocomotive)
        self.GetPowerConsumption(self.FGLocomotive)
        goto(ExecutionFlow.Pop())
        # Label 1335
        ReturnValue1: bool = Default__KismetSystemLibrary.IsValid(self.FGLocomotive)
        if not ReturnValue1:
            goto('L1411')
        self.OnEscapePressed()
        goto(ExecutionFlow.Pop())
        # Label 1411
        self.OnClose.ProcessMulticastDelegate()
        self.RemoveFromParent()
        goto(ExecutionFlow.Pop())
        goto('L1335')
        ReturnValue_5: Ptr[PlayerController] = self.GetOwningPlayer()
        
        RCO = None
        Default__BPHUDHelpers.GetDefaultRCO(ReturnValue_5, self, Ref[RCO])
        RCO.Server_SetTrainName(self.mTrain, mName)
        self.OnTrainNameChanged.ProcessMulticastDelegate()
        goto(ExecutionFlow.Pop())
        ReturnValue1_0: Ptr[PlayerController] = self.GetOwningPlayer()
        
        RCO1 = None
        Default__BPHUDHelpers.GetDefaultRCO(ReturnValue1_0, self, Ref[RCO1])
        RCO1.Server_SetTrainSelfDrivingEnabled(self.mTrain, SelfDrivingEnabled)
        goto(ExecutionFlow.Pop())
        ReturnValue2_0: Ptr[PlayerController] = self.GetOwningPlayer()
        
        RCO2 = None
        Default__BPHUDHelpers.GetDefaultRCO(ReturnValue2_0, self, Ref[RCO2])
        RCO2.Server_DockTrain(self.mTrain)
        goto(ExecutionFlow.Pop())
        self.Widget_TrainStats.UpdateDockingButton(state)
        goto(ExecutionFlow.Pop())
    

    def OnTrainNameChanged__DelegateSignature(self):
        pass
    

    def OnClose__DelegateSignature(self):
        pass
    
