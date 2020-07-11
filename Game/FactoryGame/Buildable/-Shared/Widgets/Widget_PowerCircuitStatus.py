
from codegen.ue4_stub import *

from Script.Engine import Default__KismetSystemLibrary
from Script.FactoryGame import GetPowerCircuit
from Script.Engine import FormatArgumentData
from Script.FactoryGame import FGPowerConnectionComponent
from Script.FactoryGame import GetCircuitID
from Script.Engine import Format
from Script.Engine import IsValid
from Script.FactoryGame import FGPowerCircuit
from Script.FactoryGame import FGPowerInfoComponent
from Script.FactoryGame import FGPowerCircuitWidget
from Script.Engine import Default__KismetTextLibrary

class Widget_PowerCircuitStatus(FGPowerCircuitWidget):
    mPowerInfo: Ptr[FGPowerInfoComponent]
    mPowerConnection: Ptr[FGPowerConnectionComponent]
    
    def IsConnectedVisibility(self):
        
        IsConnected = None
        self.IsConnected(Ref[IsConnected])
        if not IsConnected:
            goto('L62')
        ReturnValue = 3
        goto('L82')
        # Label 62
        ReturnValue = 1
    

    def IsConnected(self):
        ReturnValue: Ptr[FGPowerCircuit] = self.GetPowerCircuit()
        ReturnValue_0: bool = Default__KismetSystemLibrary.IsValid(ReturnValue)
        IsConnected = ReturnValue_0
    

    def GetCircuitText(self):
        mNotConnectedText = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 20, 'Value': 'NOT CONNECTED'}"
        
        IsConnected = None
        self.IsConnected(Ref[IsConnected])
        if not IsConnected:
            goto('L526')
        ReturnValue: Ptr[FGPowerCircuit] = self.GetPowerCircuit()
        ReturnValue_0: int32 = ReturnValue.GetCircuitID()
        FormatArgumentData.ArgumentName = "A"
        FormatArgumentData.ArgumentValueType = 0
        FormatArgumentData.ArgumentValue = 
        FormatArgumentData.ArgumentValueInt = ReturnValue_0
        FormatArgumentData.ArgumentValueFloat = 0
        FormatArgumentData.ArgumentValueGender = 0
        Array: List[FormatArgumentData] = [FormatArgumentData]
        ReturnValue_1: FText = Default__KismetTextLibrary.Format("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 434, 'Value': 'Circuit: {A}'}", Array)
        ReturnValue_2: FText = ReturnValue_1
        goto('L553')
        # Label 526
        ReturnValue_2 = mNotConnectedText
    
