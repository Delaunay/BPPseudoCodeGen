
from codegen.ue4_stub import *

from Game.FactoryGame.Interface.UI.InGame.Widget_NetworkErrorPopup import ExecuteUbergraph_Widget_NetworkErrorPopup.K2Node_CustomEvent_errorMsg
from Script.Engine import Delay
from Game.FactoryGame.Interface.UI.InGame.Widget_NetworkErrorPopup import ExecuteUbergraph_Widget_NetworkErrorPopup
from Script.Engine import Not_PreBool
from Script.Engine import LatentActionInfo
from Script.FactoryGame import FGGameNetworkErrorMsg
from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import PlayerController
from Game.FactoryGame.Interface.UI.InGame.Widget_NetworkErrorPopup import ExecuteUbergraph_Widget_NetworkErrorPopup.K2Node_CustomEvent_NewParam
from Script.FactoryGame import PopLatestNetworkError
from Script.Engine import GetGameInstance
from Script.Engine import Default__KismetTextLibrary
from Script.Engine import Conv_StringToText
from Script.Engine import Default__GameplayStatics
from Script.Engine import NotEqual_StrStr
from Script.Engine import Default__KismetStringLibrary
from Script.FactoryGame import GetLatestNetworkError
from Script.FactoryGame import Default__FGBlueprintFunctionLibrary
from Script.Engine import NotEqual_ByteByte
from Script.FactoryGame import FGGameInstance
from Script.UMG import UserWidget
from Game.FactoryGame.Interface.UI.InGame.Widget_NetworkErrorPopup import ExecuteUbergraph_Widget_NetworkErrorPopup.K2Node_CustomEvent_errorType
from Script.FactoryGame import AddPopupWithCloseDelegate
from Script.Engine import GameInstance

class Widget_NetworkErrorPopup(UserWidget):
    FGGameInstance: Ptr[FGGameInstance]
    mHasPopupOpen: bool
    LatestMessage: FGGameNetworkErrorMsg = Namespace(errorMsg='No errors', errorType=11)
    
    def CreatePopup(self, FGGameNetworkErrorMsg: Const[Ref[FGGameNetworkErrorMsg]]):
        ReturnValue: bool = Default__KismetStringLibrary.NotEqual_StrStr(FGGameNetworkErrorMsg.errorMsg, self.LatestMessage.errorMsg)
        ReturnValue_0: bool = NotEqual_ByteByte(FGGameNetworkErrorMsg.errorType, self.LatestMessage.errorType)
        ReturnValue_1: bool = ReturnValue_0 and ReturnValue
        if not ReturnValue_1:
            goto('L945')
        FGGameNetworkErrorMsg_0.errorType = FGGameNetworkErrorMsg.errorType
        FGGameNetworkErrorMsg_0.errorMsg = FGGameNetworkErrorMsg.errorMsg
        self.LatestMessage = FGGameNetworkErrorMsg_0
        ReturnValue_2: bool = Not_PreBool(self.mHasPopupOpen)
        if not ReturnValue_2:
            goto('L1207')
        CmpSuccess: bool = NotEqual_ByteByte(FGGameNetworkErrorMsg.errorType, 0)
        if not CmpSuccess:
            goto('L965')
        CmpSuccess = NotEqual_ByteByte(FGGameNetworkErrorMsg.errorType, 1)
        if not CmpSuccess:
            goto('L965')
        CmpSuccess = NotEqual_ByteByte(FGGameNetworkErrorMsg.errorType, 2)
        if not CmpSuccess:
            goto('L965')
        CmpSuccess = NotEqual_ByteByte(FGGameNetworkErrorMsg.errorType, 3)
        if not CmpSuccess:
            goto('L965')
        CmpSuccess = NotEqual_ByteByte(FGGameNetworkErrorMsg.errorType, 4)
        if not CmpSuccess:
            goto('L965')
        CmpSuccess = NotEqual_ByteByte(FGGameNetworkErrorMsg.errorType, 5)
        if not CmpSuccess:
            goto('L965')
        CmpSuccess = NotEqual_ByteByte(FGGameNetworkErrorMsg.errorType, 6)
        if not CmpSuccess:
            goto('L965')
        CmpSuccess = NotEqual_ByteByte(FGGameNetworkErrorMsg.errorType, 7)
        if not CmpSuccess:
            goto('L965')
        CmpSuccess = NotEqual_ByteByte(FGGameNetworkErrorMsg.errorType, 8)
        if not CmpSuccess:
            goto('L965')
        CmpSuccess = NotEqual_ByteByte(FGGameNetworkErrorMsg.errorType, 9)
        if not CmpSuccess:
            goto('L965')
        CmpSuccess = NotEqual_ByteByte(FGGameNetworkErrorMsg.errorType, 10)
        if not CmpSuccess:
            goto('L965')
        # End
        # Label 945
        self.OnPopupClosed(False)
        # End
        # Label 965
        ReturnValue_3: FText = Default__KismetTextLibrary.Conv_StringToText(FGGameNetworkErrorMsg.errorMsg)
        ReturnValue_4: Ptr[PlayerController] = self.GetOwningPlayer()
        OutputDelegate.BindUFunction(self, OnPopupClosed)
        
        OutputDelegate = None
        Default__FGBlueprintFunctionLibrary.AddPopupWithCloseDelegate(ReturnValue_4, "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 1122, 'Value': 'Network Error'}", ReturnValue_3, 0, None, None, Ref[OutputDelegate])
        self.mHasPopupOpen = True
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_NetworkErrorPopup(372)
    

    def mOnNetworkErrorRecieved_Event_0(self, errorType: uint8, errorMsg: FString):
        ExecuteUbergraph_Widget_NetworkErrorPopup.K2Node_CustomEvent_errorType = errorType #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_NetworkErrorPopup.K2Node_CustomEvent_errorMsg = errorMsg #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_NetworkErrorPopup(449)
    

    def CheckErrors(self):
        self.ExecuteUbergraph_Widget_NetworkErrorPopup(454)
    

    def OnPopupClosed(self, NewParam: bool):
        ExecuteUbergraph_Widget_NetworkErrorPopup.K2Node_CustomEvent_NewParam = NewParam #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_NetworkErrorPopup(590)
    

    def ExecuteUbergraph_Widget_NetworkErrorPopup(self):
        goto(ComputedJump("EntryPoint"))
        # Label 15
        self.LatestMessage = FGGameNetworkErrorMsg(errorType = 255, errorMsg = "No errors")
        FGGameNetworkErrorMsg.errorType = errorType
        FGGameNetworkErrorMsg.errorMsg = errorMsg
        
        FGGameNetworkErrorMsg = None
        self.CreatePopup(Ref[FGGameNetworkErrorMsg])
        goto(ExecutionFlow.Pop())
        ReturnValue: Ptr[GameInstance] = Default__GameplayStatics.GetGameInstance(self)
        Instance: Ptr[FGGameInstance] = Cast[FGGameInstance](ReturnValue)
        bSuccess: bool = Instance
        if not bSuccess:
           goto(ExecutionFlow.Pop())
        self.FGGameInstance = Instance
        OutputDelegate.BindUFunction(self, mOnNetworkErrorRecieved_Event_0)
        self.FGGameInstance.mOnNetworkErrorRecieved.AddUnique(OutputDelegate)
        self.CheckErrors()
        goto(ExecutionFlow.Pop())
        Default__KismetSystemLibrary.Delay(self, 0.20000000298023224, LatentActionInfo(Linkage = 156, UUID = 1893485943, ExecutionFunction = "ExecuteUbergraph_Widget_NetworkErrorPopup", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        goto('L15')
        
        msg = None
        ReturnValue_0: bool = self.FGGameInstance.GetLatestNetworkError(Ref[msg])
        if not ReturnValue_0:
           goto(ExecutionFlow.Pop())
        
        msg = None
        ReturnValue_0 = self.FGGameInstance.GetLatestNetworkError(Ref[msg])
        
        msg = None
        self.CreatePopup(Ref[msg])
        goto(ExecutionFlow.Pop())
        
        msg1 = None
        ReturnValue1: bool = self.FGGameInstance.GetLatestNetworkError(Ref[msg1])
        if not ReturnValue1:
           goto(ExecutionFlow.Pop())
        ReturnValue_1: bool = self.FGGameInstance.PopLatestNetworkError()
        self.mHasPopupOpen = False
        self.CheckErrors()
        goto(ExecutionFlow.Pop())
    
