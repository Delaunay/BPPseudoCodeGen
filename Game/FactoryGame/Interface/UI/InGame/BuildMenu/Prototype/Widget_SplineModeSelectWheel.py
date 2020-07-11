
from codegen.ue4_stub import *

from Script.Engine import Conv_TextToString
from Script.Engine import Conv_StringToName
from Script.FactoryGame import FGInteractWidget
from Script.Engine import Default__KismetArrayLibrary
from Game.FactoryGame.Interface.UI.InGame.BuildMenu.Prototype.Widget_SplineModeSelectWheel import ExecuteUbergraph_Widget_SplineModeSelectWheel
from Script.FactoryGame import EHologramSplinePathMode
from Script.FactoryGame import GetSupportedSplineModes
from Script.FactoryGame import SetActiveSplineMode
from Script.Engine import Default__KismetStringLibrary
from Script.FactoryGame import FGBuildGunStateBuild
from Script.Engine import Default__KismetTextLibrary

class Widget_SplineModeSelectWheel(FGInteractWidget):
    mBuildGunState: Ptr[FGBuildGunStateBuild]
    mSupportedSplineModes: List[uint8]
    mRestoreFocusWhenLost = True
    mDesiredHorizontalAlignment = 2
    mDesiredVerticalAlignment = 2
    mCallCustomTickOnConstruct = True
    
    def Construct(self):
        self.ExecuteUbergraph_Widget_SplineModeSelectWheel(1309)
    

    def Destruct(self):
        self.ExecuteUbergraph_Widget_SplineModeSelectWheel(1489)
    

    def ExecuteUbergraph_Widget_SplineModeSelectWheel(self):
        goto(ComputedJump("EntryPoint"))
        # Label 15
        ReturnValue: int32 = Variable + 1
        Variable: int32 = ReturnValue
        
        # Label 84
        ReturnValue_0: int32 = len(self.mSupportedSplineModes)
        ReturnValue_1: bool = Variable <= ReturnValue_0
        if not ReturnValue_1:
            goto('L1221')
        Variable_0: int32 = Variable
        ExecutionFlow.Push("L15")
        Variable_1: FText = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 247, 'Value': 'Noodle'}"
        Variable1: FText = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 311, 'Value': 'Conveyor 2D'}"
        Variable2: FText = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 380, 'Value': 'Path Find'}"
        Variable3: FText = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 447, 'Value': 'Vertical To Horizontal'}"
        Variable4: FText = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 527, 'Value': 'Vertical'}"
        Variable5: FText = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 593, 'Value': 'Straight Vertical'}"
        Variable6: FText = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 668, 'Value': 'Straight Horizontal'}"
        Variable7: FText = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 745, 'Value': 'Default'}"
        
        Item = None
        Item = self.mSupportedSplineModes[Variable_0]
        Variable_2: uint8 = Item
        
        switch = {
            0: Variable7,
            1: Variable6,
            2: Variable5,
            3: Variable4,
            4: Variable3,
            5: Variable2,
            6: Variable1,
            7: Variable_1
        }
        
        switch.get(Variable_2, None) = None
        ReturnValue_2: FString = Default__KismetTextLibrary.Conv_TextToString(Ref[switch.get(Variable_2, None)])
        ReturnValue_3: FName = Default__KismetStringLibrary.Conv_StringToName(ReturnValue_2)
        
        self.Widget_RadialMenu.Buttons = None
        ReturnValue_4: int32 = self.Widget_RadialMenu.Buttons.append(ReturnValue_3)
        goto(ExecutionFlow.Pop())
        # Label 1221
        self.Widget_RadialMenu.Create Radial Menu()
        goto(ExecutionFlow.Pop())
        # Label 1258
        Variable = 0
        Variable_0 = 0
        goto('L84')
        self.Widget_RadialMenu.mDescText = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 1351, 'Value': 'Select Spline Mode'}"
        ReturnValue_5: List[uint8] = self.mBuildGunState.GetSupportedSplineModes()
        self.mSupportedSplineModes = ReturnValue_5
        goto('L1258')
        
        Item1 = None
        Item1 = self.mSupportedSplineModes[self.Widget_RadialMenu.SelectedInt]
        self.mBuildGunState.SetActiveSplineMode(Item1)
        goto(ExecutionFlow.Pop())
    
