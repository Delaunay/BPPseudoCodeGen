
from codegen.ue4_stub import *

from Game.FactoryGame.Interface.UI.InGame.Widget_RewardInventoryItems import ExecuteUbergraph_Widget_RewardInventoryItems.K2Node_Event_IsDesignTime
from Script.UMG import UserWidget
from Game.FactoryGame.Interface.UI.InGame.Widget_RewardInventoryItems import ExecuteUbergraph_Widget_RewardInventoryItems

class Widget_RewardInventoryItems(UserWidget):
    mText: FText = NSLOCTEXT("", "0DAEC2E6469B86A7134A5786EE25943A", "+6 Arms Slots")
    
    def PreConstruct(self):
        ExecuteUbergraph_Widget_RewardInventoryItems.K2Node_Event_IsDesignTime = IsDesignTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_RewardInventoryItems(10)
    

    def ExecuteUbergraph_Widget_RewardInventoryItems(self):
        self.mTextField.SetText(self.mText)
    
