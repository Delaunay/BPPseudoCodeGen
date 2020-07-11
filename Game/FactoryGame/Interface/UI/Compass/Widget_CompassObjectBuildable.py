
from codegen.ue4_stub import *

from Script.Engine import Default__KismetSystemLibrary
from Game.FactoryGame.Interface.UI.Compass.Widget_CompassObjectBuildable import ExecuteUbergraph_Widget_CompassObjectBuildable
from Script.UMG import UMGSequencePlayer
from Script.UMG import CanvasPanelSlot
from Script.UMG import PlayAnimation
from Script.FactoryGame import FGCompassObjectWidget
from Script.FactoryGame import OnCompassObjectUpdated
from Script.UMG import EUMGSequencePlayMode
from Game.FactoryGame.Interface.UI.Compass.Widget_CompassObjectBuildable import ExecuteUbergraph_Widget_CompassObjectBuildable.K2Node_Event_centered
from Script.Engine import IsValid
from Script.UMG import Default__WidgetLayoutLibrary
from Script.UMG import SlotAsCanvasSlot
from Script.UMG import SetZOrder

class Widget_CompassObjectBuildable(FGCompassObjectWidget):
    mPositionOffset = Namespace(X=0, Y=-2)
    mShouldFadeInEdges = True
    
    def Construct(self):
        self.ExecuteUbergraph_Widget_CompassObjectBuildable(10)
    

    def OnCompassObjectUpdated(self):
        self.ExecuteUbergraph_Widget_CompassObjectBuildable(61)
    

    def OnObjectCentered(self):
        ExecuteUbergraph_Widget_CompassObjectBuildable.K2Node_Event_centered = centered #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_CompassObjectBuildable(122)
    

    def ExecuteUbergraph_Widget_CompassObjectBuildable(self):
        self.Widget_MapCompass_Icon.UpdateActor(self.mActorRepresentation, True)
        # End
        self.OnCompassObjectUpdated()
        self.Widget_MapCompass_Icon.UpdateActor(self.mActorRepresentation, True)
        # End
        ReturnValue: Ptr[CanvasPanelSlot] = Default__WidgetLayoutLibrary.SlotAsCanvasSlot(self)
        ReturnValue_0: bool = Default__KismetSystemLibrary.IsValid(ReturnValue)
        if not ReturnValue_0:
            goto('L423')
        Variable: bool = centered
        ReturnValue = Default__WidgetLayoutLibrary.SlotAsCanvasSlot(self)
        Variable_0: int32 = 0
        Variable1: int32 = 1
        
        switch = {
            False: Variable_0,
            True: Variable1
        }
        ReturnValue.SetZOrder(switch.get(Variable, None))
        # Label 423
        Variable_1: uint8 = 0
        Variable1_0: uint8 = 1
        Variable1_1: bool = centered
        
        switch_0 = {
            False: Variable1_0,
            True: Variable_1
        }
        ReturnValue_1: Ptr[UMGSequencePlayer] = self.Widget_MapCompass_Icon.PlayAnimation(self.Widget_MapCompass_Icon.ShowDescription, 0, 1, switch_0.get(Variable1_1, None), 1)
    
