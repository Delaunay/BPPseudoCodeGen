
from codegen.ue4_stub import *

from Script.Engine import Default__KismetSystemLibrary
from Script.FactoryGame import FGPopupWidgetContent
from Script.Engine import Default__KismetTextLibrary
from Script.Engine import Default__GameplayStatics
from Script.Engine import FormatArgumentData
from Script.Engine import GetGameInstance
from Script.FactoryGame import EJoinSessionState
from Script.FactoryGame import GetCurrentJoinSessionState
from Script.Engine import Format
from Game.FactoryGame.Interface.UI.Widget_JoinSessionPopup import ExecuteUbergraph_Widget_JoinSessionPopup.K2Node_CustomEvent_newState
from Script.Engine import Conv_ByteToInt
from Script.Engine import GameInstance
from Script.Engine import Subtract_ByteByte
from Script.Engine import Conv_IntToByte
from Script.FactoryGame import FGGameInstance
from Game.FactoryGame.Interface.UI.Widget_JoinSessionPopup import ExecuteUbergraph_Widget_JoinSessionPopup
from Script.Engine import MakeLiteralInt
from Script.Engine import MakeLiteralByte

class Widget_JoinSessionPopup(FGPopupWidgetContent):
    
    
    def GetShouldOkayBeEnabled(self):
        ReturnValue = False
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_JoinSessionPopup(10)
    

    def Destruct(self):
        self.ExecuteUbergraph_Widget_JoinSessionPopup(274)
    

    def OnJoinSessionStateUpdated(self, newState: uint8):
        ExecuteUbergraph_Widget_JoinSessionPopup.K2Node_CustomEvent_newState = newState #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_JoinSessionPopup(465)
    

    def ExecuteUbergraph_Widget_JoinSessionPopup(self):
        ReturnValue: Ptr[GameInstance] = Default__GameplayStatics.GetGameInstance(self)
        Instance: Ptr[FGGameInstance] = Cast[FGGameInstance](ReturnValue)
        bSuccess: bool = Instance
        if not bSuccess:
            goto('L2109')
        OutputDelegate.BindUFunction(self, OnJoinSessionStateUpdated)
        Instance.mOnJoinSessionStateUpdated.AddUnique(OutputDelegate)
        ReturnValue_0: uint8 = Instance.GetCurrentJoinSessionState()
        self.OnJoinSessionStateUpdated(ReturnValue_0)
        # End
        ReturnValue1: Ptr[GameInstance] = Default__GameplayStatics.GetGameInstance(self)
        Instance1: Ptr[FGGameInstance] = Cast[FGGameInstance](ReturnValue1)
        bSuccess1: bool = Instance1
        if not bSuccess1:
            goto('L2109')
        OutputDelegate.BindUFunction(self, OnJoinSessionStateUpdated)
        Instance1.mOnJoinSessionStateUpdated.Remove(OutputDelegate)
        # End
        Variable: FText = STRING_TABLE_ENTRY("StringTable /Game/FactoryGame/Interface/UI/Menu/NetworkMessages.NetworkMessages", "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 562, 'Value': 'ConnectingToHost'}"
        Variable1: FText = STRING_TABLE_ENTRY("StringTable /Game/FactoryGame/Interface/UI/Menu/NetworkMessages.NetworkMessages", "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 677, 'Value': 'DestroyingOldSession'}"
        Variable2: FText = STRING_TABLE_ENTRY("StringTable /Game/FactoryGame/Interface/UI/Menu/NetworkMessages.NetworkMessages", "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 796, 'Value': 'QueryingHostId'}"
        Variable3: FText = STRING_TABLE_ENTRY("StringTable /Game/FactoryGame/Interface/UI/Menu/NetworkMessages.NetworkMessages", "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 909, 'Value': 'WaitingForLogin'}"
        ReturnValue_1: int32 = Default__KismetSystemLibrary.MakeLiteralInt(5)
        Variable4: FText = 
        ReturnValue_2: uint8 = Conv_IntToByte(ReturnValue_1)
        ReturnValue_3: uint8 = Subtract_ByteByte(ReturnValue_2, 1)
        ReturnValue_4: int32 = Conv_ByteToInt(ReturnValue_3)
        FormatArgumentData.ArgumentName = "MaxStep"
        FormatArgumentData.ArgumentValueType = 0
        FormatArgumentData.ArgumentValue = 
        FormatArgumentData.ArgumentValueInt = ReturnValue_4
        FormatArgumentData.ArgumentValueFloat = 0
        FormatArgumentData.ArgumentValueGender = 0
        Variable_0: uint8 = newState
        FormatArgumentData1.ArgumentName = "Message"
        FormatArgumentData1.ArgumentValueType = 4
        
        switch = {
            0: Variable4,
            1: Variable3,
            2: Variable2,
            3: Variable1,
            4: Variable
        }
        FormatArgumentData1.ArgumentValue = switch.get(Variable_0, None)
        FormatArgumentData1.ArgumentValueInt = 0
        FormatArgumentData1.ArgumentValueFloat = 0
        FormatArgumentData1.ArgumentValueGender = 0
        ReturnValue_5: uint8 = Default__KismetSystemLibrary.MakeLiteralByte(newState)
        ReturnValue1_0: int32 = Conv_ByteToInt(ReturnValue_5)
        FormatArgumentData2.ArgumentName = "Step"
        FormatArgumentData2.ArgumentValueType = 0
        FormatArgumentData2.ArgumentValue = 
        FormatArgumentData2.ArgumentValueInt = ReturnValue1_0
        FormatArgumentData2.ArgumentValueFloat = 0
        FormatArgumentData2.ArgumentValueGender = 0
        Array: List[FormatArgumentData] = [FormatArgumentData1, FormatArgumentData2, FormatArgumentData]
        ReturnValue_6: FText = Default__KismetTextLibrary.Format("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 1990, 'Value': '{Message} {Step}/{MaxStep}'}", Array)
        self.mTextBody.SetText(ReturnValue_6)
    
