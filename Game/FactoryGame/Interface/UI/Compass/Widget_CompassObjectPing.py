
from codegen.ue4_stub import *

from Game.FactoryGame.Interface.UI.Compass.Widget_CompassObjectPing import ExecuteUbergraph_Widget_CompassObjectPing
from Script.FactoryGame import GetActorRepresentation
from Script.UMG import CanvasPanelSlot
from Script.FactoryGame import FGCompassObjectWidget
from Script.FactoryGame import FGActorRepresentation
from Script.UMG import Default__WidgetLayoutLibrary
from Script.UMG import SlotAsCanvasSlot
from Script.UMG import SetZOrder

class Widget_CompassObjectPing(FGCompassObjectWidget):
    
    
    def Construct(self):
        self.ExecuteUbergraph_Widget_CompassObjectPing(10)
    

    def ExecuteUbergraph_Widget_CompassObjectPing(self):
        ReturnValue: Ptr[FGActorRepresentation] = self.GetActorRepresentation()
        self.Widget_MapCompass_Icon.UpdateActor(ReturnValue, True)
        ReturnValue_0: Ptr[CanvasPanelSlot] = Default__WidgetLayoutLibrary.SlotAsCanvasSlot(self)
        ReturnValue_0.SetZOrder(200)
    
