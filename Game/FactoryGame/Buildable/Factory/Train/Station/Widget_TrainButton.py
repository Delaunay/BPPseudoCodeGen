
from codegen.ue4_stub import *

from Script.Engine import Default__KismetSystemLibrary
from Script.FactoryGame import GetTimeTable
from Script.Engine import K2_ClearAndInvalidateTimerHandle
from Script.Engine import Default__KismetArrayLibrary
from Script.FactoryGame import GetCurrentStop
from Script.FactoryGame import GetStationName
from Script.Engine import K2_SetTimerDelegate
from Script.FactoryGame import TimeTableStop
from Script.FactoryGame import FGTrain
from Script.FactoryGame import FGRailroadTimeTable
from Script.Engine import TimerHandle
from Script.Engine import IsValid
from Game.FactoryGame.Buildable.Factory.Train.Station.Widget_TrainButton import ExecuteUbergraph_Widget_TrainButton
from Script.FactoryGame import GetStops
from Script.UMG import SetColorAndOpacity
from Game.FactoryGame.Buildable.Factory.Train.Station.Widget_TrainButton import ExecuteUbergraph_Widget_TrainButton.K2Node_Event_IsDesignTime
from Script.UMG import UserWidget
from Script.CoreUObject import LinearColor

class Widget_TrainButton(UserWidget):
    OnClicked: FMulticastScriptDelegate
    mTrainObject: Ptr[FGTrain]
    mTitle: FText = NSLOCTEXT("", "7CCE33D54D422546A8BA37B76AFD0F01", "Locomotive")
    CheckNextStopTimer: TimerHandle
    
    def SetTitle(self, mTitle: FText):
        self.mTitle = mTitle
        self.mTitleObject.SetText(self.mTitle)
    

    def PreConstruct(self):
        ExecuteUbergraph_Widget_TrainButton.K2Node_Event_IsDesignTime = IsDesignTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_TrainButton(10)
    

    def BndEvt__mButton_K2Node_ComponentBoundEvent_0_OnButtonClickedEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_TrainButton(38)
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_TrainButton(63)
    

    def CheckNextStop(self):
        self.ExecuteUbergraph_Widget_TrainButton(242)
    

    def Destruct(self):
        self.ExecuteUbergraph_Widget_TrainButton(700)
    

    def BndEvt__mButton_K2Node_ComponentBoundEvent_1_OnButtonHoverEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_TrainButton(747)
    

    def BndEvt__mButton_K2Node_ComponentBoundEvent_2_OnButtonHoverEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_TrainButton(924)
    

    def ExecuteUbergraph_Widget_TrainButton(self):
        self.SetTitle(self.mTitle)
        # End
        self.OnClicked.ProcessMulticastDelegate(self)
        # End
        self.Widget_TrainWarning.Init(self.mTrainObject)
        self.CheckNextStop()
        OutputDelegate.BindUFunction(self, CheckNextStop)
        ReturnValue: TimerHandle = Default__KismetSystemLibrary.K2_SetTimerDelegate(OutputDelegate, 1, True)
        self.CheckNextStopTimer = ReturnValue
        # End
        ReturnValue_0: Ptr[FGRailroadTimeTable] = self.mTrainObject.GetTimeTable()
        ReturnValue_1: bool = Default__KismetSystemLibrary.IsValid(ReturnValue_0)
        if not ReturnValue_1:
            goto('L657')
        self.mNextStopContainer.SetVisibility(3)
        stops: List[TimeTableStop] = []
        
        ReturnValue_0.GetStops(Ref[stops])
        ReturnValue_2: int32 = ReturnValue_0.GetCurrentStop()
        
        Item = None
        Item = stops[ReturnValue_2]
        ReturnValue_3: FText = Item.Station.GetStationName()
        self.mNextStopText.SetText(ReturnValue_3)
        # End
        # Label 657
        self.mNextStopContainer.SetVisibility(1)
        # End
        
        Default__KismetSystemLibrary.K2_ClearAndInvalidateTimerHandle(self, Ref[self.CheckNextStopTimer])
        # End
        SlateColor1.SpecifiedColor = LinearColor(R = 1, G = 1, B = 1, A = 1)
        SlateColor1.ColorUseRule = 0
        self.mNextStopTitle.SetColorAndOpacity(SlateColor1)
        self.mNextStopText.SetColorAndOpacity(SlateColor1)
        # End
        SlateColor.SpecifiedColor = LinearColor(R = 0.6038280129432678, G = 0.5972020030021667, B = 0.5972020030021667, A = 1)
        SlateColor.ColorUseRule = 0
        self.mNextStopTitle.SetColorAndOpacity(SlateColor)
        self.mNextStopText.SetColorAndOpacity(SlateColor)
    

    def OnClicked__DelegateSignature(self, Button: Ptr[Widget_TrainButton]):
        pass
    
