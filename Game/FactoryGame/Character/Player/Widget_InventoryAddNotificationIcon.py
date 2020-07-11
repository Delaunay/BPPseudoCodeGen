
from codegen.ue4_stub import *

from Script.UMG import UMGSequencePlayer
from Game.FactoryGame.Character.Player.Widget_InventoryAddNotificationIcon import ExecuteUbergraph_Widget_InventoryAddNotificationIcon
from Script.UMG import PlayAnimation
from Script.UMG import WidgetAnimation
from Script.UMG import UserWidget

class Widget_InventoryAddNotificationIcon(UserWidget):
    IconAnimation: Ptr[WidgetAnimation]
    
    def Animate Icon(self):
        self.ExecuteUbergraph_Widget_InventoryAddNotificationIcon(10)
    

    def ExecuteUbergraph_Widget_InventoryAddNotificationIcon(self):
        ReturnValue: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.IconAnimation, 0, 1, 0, 0.30000001192092896)
    
