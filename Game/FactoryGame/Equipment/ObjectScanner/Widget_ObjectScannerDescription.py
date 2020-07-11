
from codegen.ue4_stub import *

from Script.Engine import Default__KismetSystemLibrary
from Script.UMG import UMGSequencePlayer
from Script.UMG import PlayAnimation
from Game.FactoryGame.Equipment.ObjectScanner.Widget_ObjectScannerDescription import ExecuteUbergraph_Widget_ObjectScannerDescription
from Game.FactoryGame.Equipment.ObjectScanner.Widget_ObjectScannerMenuItem import Widget_ObjectScannerMenuItem
from Script.Engine import IsValid
from Script.UMG import WidgetAnimation
from Script.UMG import UserWidget

class Widget_ObjectScannerDescription(UserWidget):
    AniConstruct: Ptr[WidgetAnimation]
    mSelectedItem: Ptr[Widget_ObjectScannerMenuItem]
    
    def Get_mDescription_Text_0(self):
        Variable: FText = 
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(self.mSelectedItem)
        Variable_0: bool = ReturnValue
        
        switch = {
            False: Variable,
            True: self.mSelectedItem.mDescription
        }
        ReturnValue_0: FText = switch.get(Variable_0, None)
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_ObjectScannerDescription(61)
    

    def ExecuteUbergraph_Widget_ObjectScannerDescription(self):
        # Label 10
        ReturnValue: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.AniConstruct, 0, 1, 0, 1)
        # End
        goto('L10')
    
