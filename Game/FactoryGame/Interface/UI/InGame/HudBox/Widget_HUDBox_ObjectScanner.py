
from codegen.ue4_stub import *

from Script.Engine import Default__KismetSystemLibrary
from Game.FactoryGame.Interface.UI.InGame.HudBox.Widget_HUDBox_ObjectScanner import ExecuteUbergraph_Widget_HUDBox_ObjectScanner.K2Node_Event_MyGeometry
from Script.FactoryGame import HasValidCurrentDetails
from Script.Engine import IsValid
from Script.FactoryGame import GetCurrentDetails
from Game.FactoryGame.Interface.UI.InGame.HudBox.Widget_HUDBox_Equipment_Parent import Widget_HUDBox_Equipment_Parent
from Script.FactoryGame import ScannableDetails
from Game.FactoryGame.Interface.UI.InGame.HudBox.Widget_HUDBox_ObjectScanner import ExecuteUbergraph_Widget_HUDBox_ObjectScanner.K2Node_Event_InDeltaTime
from Script.FactoryGame import FGObjectScanner
from Game.FactoryGame.Interface.UI.InGame.HudBox.Widget_HUDBox_ObjectScanner import ExecuteUbergraph_Widget_HUDBox_ObjectScanner

class Widget_HUDBox_ObjectScanner(Widget_HUDBox_Equipment_Parent):
    mScanner: Ptr[FGObjectScanner]
    bHasScriptImplementedTick = True
    
    def Construct(self):
        self.ExecuteUbergraph_Widget_HUDBox_ObjectScanner(283)
    

    def Tick(self):
        ExecuteUbergraph_Widget_HUDBox_ObjectScanner.K2Node_Event_MyGeometry = MyGeometry #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_HUDBox_ObjectScanner.K2Node_Event_InDeltaTime = InDeltaTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_HUDBox_ObjectScanner(386)
    

    def ExecuteUbergraph_Widget_HUDBox_ObjectScanner(self):
        # Label 10
        self.mScanningText.SetText()
        # End
        # Label 53
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(self.mScanner)
        if not ReturnValue:
            goto('L391')
        ReturnValue_0: bool = self.mScanner.HasValidCurrentDetails()
        if not ReturnValue_0:
            goto('L10')
        ReturnValue_1: ScannableDetails = self.mScanner.GetCurrentDetails()
        self.mScanningText.SetText(ReturnValue_1.DisplayText)
        # End
        Scanner: Ptr[FGObjectScanner] = Cast[FGObjectScanner](self.mEquipment)
        bSuccess: bool = Scanner
        if not bSuccess:
            goto('L391')
        self.mScanner = Scanner
        # End
        goto('L53')
    
