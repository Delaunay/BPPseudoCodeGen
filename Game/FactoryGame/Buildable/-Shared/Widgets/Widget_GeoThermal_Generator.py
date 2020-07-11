
from codegen.ue4_stub import *

from Script.Engine import Default__KismetSystemLibrary
from Script.FactoryGame import GetPowerCircuit
from Script.FactoryGame import IsFuseTriggered
from Game.FactoryGame.Interface.UI.InGame.Widget_UseableBase import Destruct
from Script.FactoryGame import GetFuelAmount
from Script.UMG import ESlateVisibility
from Script.FactoryGame import FGBuildableGeneratorFuel
from Script.FactoryGame import IsConnected
from Game.FactoryGame.Interface.UI.InGame.Widget_UseableBase import Construct
from Script.FactoryGame import Init
from Game.FactoryGame.Interface.UI.InGame.Widget_UseableBase import Widget_UseableBase
from Script.Engine import IsValid
from Game.FactoryGame.Buildable.-Shared.Widgets.Widget_GeoThermal_Generator import ExecuteUbergraph_Widget_GeoThermal_Generator
from Script.FactoryGame import FGPowerCircuit
from Script.FactoryGame import FGPowerInfoComponent
from Script.FactoryGame import GetPowerInfo

class Widget_GeoThermal_Generator(Widget_UseableBase):
    mGenerator: Ptr[FGBuildableGeneratorFuel]
    mShouldOpenInventory = True
    mUseKeyboard = True
    mUseMouse = True
    mCaptureInput = True
    mRestoreFocusWhenLost = True
    mInputToPassThrough = ['Use']
    mDesiredHorizontalAlignment = 2
    mDesiredVerticalAlignment = 2
    mUseGamepadCursor = True
    mCallCustomTickOnConstruct = True
    
    def GetFuseVisibility(self):
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(self.mPowerCircuitGraph)
        if not ReturnValue:
            goto('L339')
        ReturnValue_0: Ptr[FGPowerCircuit] = self.mPowerCircuitGraph.mPowerInfo.GetPowerCircuit()
        ReturnValue1: bool = Default__KismetSystemLibrary.IsValid(ReturnValue_0)
        if not ReturnValue1:
            goto('L339')
        ReturnValue_0 = self.mPowerCircuitGraph.mPowerInfo.GetPowerCircuit()
        ReturnValue_1: bool = ReturnValue_0.IsFuseTriggered()
        if not ReturnValue_1:
            goto('L339')
        ReturnValue_2: uint8 = 4
        goto('L359')
        # Label 339
        ReturnValue_2 = 1
    

    def OnGetPowerCircuit(self):
        ReturnValue: Ptr[FGPowerInfoComponent] = self.mGenerator.GetPowerInfo()
        ReturnValue_0: bool = Default__KismetSystemLibrary.IsValid(ReturnValue)
        if not ReturnValue_0:
            goto('L215')
        ReturnValue = self.mGenerator.GetPowerInfo()
        ReturnValue_1: Ptr[FGPowerCircuit] = ReturnValue.GetPowerCircuit()
        ReturnValue_2: Ptr[FGPowerCircuit] = ReturnValue_1
        goto('L226')
        # Label 215
        ReturnValue_2 = None
    

    def IsConnected(self):
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(self.mGenerator)
        if not ReturnValue:
            goto('L173')
        ReturnValue_0: Ptr[FGPowerInfoComponent] = self.mGenerator.GetPowerInfo()
        ReturnValue_1: bool = ReturnValue_0.IsConnected()
        IsConnected = ReturnValue_1
        # End
        # Label 173
        IsConnected = False
    

    def Cleanup(self):
        self.Widget_Window_DarkMode.OnClose.Clear()
    

    def GetBurnProgressPercent(self):
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(self.mGenerator)
        if not ReturnValue:
            goto('L142')
        ReturnValue_0: float = self.mGenerator.GetFuelAmount()
        ReturnValue_1: float = ReturnValue_0
    

    def Init(self):
        self.ExecuteUbergraph_Widget_GeoThermal_Generator(259)
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_GeoThermal_Generator(274)
    

    def Destruct(self):
        self.ExecuteUbergraph_Widget_GeoThermal_Generator(289)
    

    def ExecuteUbergraph_Widget_GeoThermal_Generator(self):
        # Label 10
        self.mConnectionWarning.UpdateWarning("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 47, 'Value': 'EARLY ACCESS WARNING:\r\nMenu does not work as intended. \r\n\r\nDoes produce power, check power pole instead.'}")
        OutputDelegate.BindUFunction(self, OnEscapePressed)
        self.Widget_Window_DarkMode.OnClose.AddUnique(OutputDelegate)
        # End
        self.Init()
        # End
        self.Construct()
        goto('L10')
        self.Destruct()
        self.Cleanup()
    
