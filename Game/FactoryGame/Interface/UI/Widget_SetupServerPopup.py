
from codegen.ue4_stub import *

from Script.Engine import Default__KismetSystemLibrary
from Script.FactoryGame import FGPopupWidgetContent
from Script.FactoryGame import ECreateSessionState
from Script.Engine import MakeLiteralByte
from Game.FactoryGame.Interface.UI.Widget_SetupServerPopup import ExecuteUbergraph_Widget_SetupServerPopup.K2Node_CustomEvent_newState
from Script.Engine import Default__KismetTextLibrary
from Script.Engine import FormatArgumentData
from Script.Engine import Format
from Script.FactoryGame import FGLocalPlayer
from Game.FactoryGame.Interface.UI.Widget_SetupServerPopup import ExecuteUbergraph_Widget_SetupServerPopup
from Script.Engine import Conv_ByteToInt
from Script.Engine import Subtract_ByteByte
from Script.Engine import Conv_IntToByte
from Script.FactoryGame import GetCurrentCreateSessionState
from Script.Engine import MakeLiteralInt
from Script.Engine import LocalPlayer

class Widget_SetupServerPopup(FGPopupWidgetContent):
    
    
    def GetShouldOkayBeEnabled(self):
        ReturnValue = False
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_SetupServerPopup(10)
    

    def Destruct(self):
        self.ExecuteUbergraph_Widget_SetupServerPopup(255)
    

    def OnCreateSessionStateChanged(self, newState: uint8):
        ExecuteUbergraph_Widget_SetupServerPopup.K2Node_CustomEvent_newState = newState #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_SetupServerPopup(427)
    

    def ExecuteUbergraph_Widget_SetupServerPopup(self):
        ReturnValue: Ptr[LocalPlayer] = self.GetOwningLocalPlayer()
        Player: Ptr[FGLocalPlayer] = Cast[FGLocalPlayer](ReturnValue)
        bSuccess: bool = Player
        if not bSuccess:
            goto('L2204')
        OutputDelegate.BindUFunction(self, OnCreateSessionStateChanged)
        Player.mOnCreateSessionStateChanged.AddUnique(OutputDelegate)
        ReturnValue_0: uint8 = Player.GetCurrentCreateSessionState()
        self.OnCreateSessionStateChanged(ReturnValue_0)
        # End
        ReturnValue1: Ptr[LocalPlayer] = self.GetOwningLocalPlayer()
        Player1: Ptr[FGLocalPlayer] = Cast[FGLocalPlayer](ReturnValue1)
        bSuccess1: bool = Player1
        if not bSuccess1:
            goto('L2204')
        OutputDelegate.BindUFunction(self, OnCreateSessionStateChanged)
        Player1.mOnCreateSessionStateChanged.Remove(OutputDelegate)
        # End
        Variable: FText = STRING_TABLE_ENTRY("StringTable /Game/FactoryGame/Interface/UI/Menu/NetworkMessages.NetworkMessages", "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 524, 'Value': 'WaitingForLogin'}"
        Variable1: FText = STRING_TABLE_ENTRY("StringTable /Game/FactoryGame/Interface/UI/Menu/NetworkMessages.NetworkMessages", "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 638, 'Value': 'WaitingForPresence'}"
        Variable2: FText = STRING_TABLE_ENTRY("StringTable /Game/FactoryGame/Interface/UI/Menu/NetworkMessages.NetworkMessages", "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 755, 'Value': 'UpdatingPresence'}"
        Variable3: FText = STRING_TABLE_ENTRY("StringTable /Game/FactoryGame/Interface/UI/Menu/NetworkMessages.NetworkMessages", "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 870, 'Value': 'DestroyingOldSession'}"
        Variable4: FText = STRING_TABLE_ENTRY("StringTable /Game/FactoryGame/Interface/UI/Menu/NetworkMessages.NetworkMessages", "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 989, 'Value': 'CreatingSession'}"
        Variable5: FText = 
        ReturnValue_1: int32 = Default__KismetSystemLibrary.MakeLiteralInt(6)
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
            0: Variable5,
            1: Variable4,
            2: Variable3,
            3: Variable2,
            4: Variable1,
            5: Variable
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
        ReturnValue_6: FText = Default__KismetTextLibrary.Format("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 2085, 'Value': '{Message} {Step}/{MaxStep}'}", Array)
        self.mTextBody.SetText(ReturnValue_6)
    
