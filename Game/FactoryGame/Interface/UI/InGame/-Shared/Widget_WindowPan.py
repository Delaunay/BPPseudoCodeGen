
from codegen.ue4_stub import *

from Game.FactoryGame.Interface.UI.InGame.-Shared.Widget_WindowPan import ExecuteUbergraph_Widget_WindowPan.K2Node_Event_InDeltaTime
from Script.UMG import UserWidget
from Game.FactoryGame.Interface.UI.InGame.-Shared.Widget_WindowPan import ExecuteUbergraph_Widget_WindowPan
from Game.FactoryGame.Interface.UI.InGame.-Shared.Widget_WindowPan import ExecuteUbergraph_Widget_WindowPan.K2Node_Event_MyGeometry

class Widget_WindowPan(UserWidget):
    Pan_Multiplier: float = 50
    Shadow_Multiplier: float = 0.5
    
    def Tick(self):
        ExecuteUbergraph_Widget_WindowPan.K2Node_Event_MyGeometry = MyGeometry #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_WindowPan.K2Node_Event_InDeltaTime = InDeltaTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_WindowPan(10)
    

    def ExecuteUbergraph_Widget_WindowPan(self):
        pass
    
