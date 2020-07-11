
from codegen.ue4_stub import *

from Script.Engine import Default__KismetSystemLibrary
from Script.FactoryGame import FGPopupWidgetContent
from Script.Engine import FCeil
from Script.Engine import K2_GetTimerRemainingTimeHandle
from Game.FactoryGame.Interface.UI.InGame.Widget_PopupContentResolutionTimer import ExecuteUbergraph_Widget_PopupContentResolutionTimer.K2Node_Event_title
from Script.Engine import FormatArgumentData
from Script.Engine import K2_SetTimerDelegate
from Game.FactoryGame.Interface.UI.InGame.Widget_PopupContentResolutionTimer import ExecuteUbergraph_Widget_PopupContentResolutionTimer.K2Node_Event_desc
from Script.Engine import Format
from Game.FactoryGame.Interface.UI.InGame.Widget_Popup import Widget_Popup
from Script.Engine import TimerHandle
from Game.FactoryGame.Interface.UI.InGame.Widget_PopupContentResolutionTimer import ExecuteUbergraph_Widget_PopupContentResolutionTimer
from Script.Engine import K2_ClearAndInvalidateTimerHandle
from Script.Engine import Default__KismetTextLibrary

class Widget_PopupContentResolutionTimer(FGPopupWidgetContent):
    mBody: FText
    TimerHandle: TimerHandle
    TimerDuration: float = 30
    
    def GetShouldOkayBeEnabled(self):
        ReturnValue = True
    

    def Get_TimerText(self):
        ReturnValue: float = Default__KismetSystemLibrary.K2_GetTimerRemainingTimeHandle(self, self.TimerHandle)
        ReturnValue_0: int32 = FCeil(ReturnValue)
        FormatArgumentData.ArgumentName = "time"
        FormatArgumentData.ArgumentValueType = 0
        FormatArgumentData.ArgumentValue = 
        FormatArgumentData.ArgumentValueInt = ReturnValue_0
        FormatArgumentData.ArgumentValueFloat = 0
        FormatArgumentData.ArgumentValueGender = 0
        Array: List[FormatArgumentData] = [FormatArgumentData]
        ReturnValue_1: FText = Default__KismetTextLibrary.Format(self.mBody, Array)
        ReturnValue_2: FText = ReturnValue_1
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_PopupContentResolutionTimer(57)
    

    def TriggerCancel(self):
        self.ExecuteUbergraph_Widget_PopupContentResolutionTimer(181)
    

    def SetOptionalTextElements(self):
        ExecuteUbergraph_Widget_PopupContentResolutionTimer.K2Node_Event_title = Title #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_PopupContentResolutionTimer.K2Node_Event_desc = Desc #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_PopupContentResolutionTimer(302)
    

    def Destruct(self):
        self.ExecuteUbergraph_Widget_PopupContentResolutionTimer(10)
    

    def ExecuteUbergraph_Widget_PopupContentResolutionTimer(self):
        
        Default__KismetSystemLibrary.K2_ClearAndInvalidateTimerHandle(self, Ref[self.TimerHandle])
        # End
        OutputDelegate.BindUFunction(self, TriggerCancel)
        ReturnValue: TimerHandle = Default__KismetSystemLibrary.K2_SetTimerDelegate(OutputDelegate, self.TimerDuration, False)
        self.TimerHandle = ReturnValue
        # End
        Popup: Ptr[Widget_Popup] = Cast[Widget_Popup](self.mPopupWidget)
        bSuccess: bool = Popup
        if not bSuccess:
            goto('L329')
        Popup.DoClosePopup(False)
        # End
        self.mBody = title
    
