
from codegen.ue4_stub import *

from Game.FactoryGame.Buildable.Factory.SpaceElevator.Widget_SpaceElevator_TierInfo import ExecuteUbergraph_Widget_SpaceElevator_TierInfo
from Game.FactoryGame.Buildable.Factory.SpaceElevator.Widget_SpaceElevator_TierInfo import ExecuteUbergraph_Widget_SpaceElevator_TierInfo.K2Node_Event_IsDesignTime
from Script.UMG import UserWidget

class Widget_SpaceElevator_TierInfo(UserWidget):
    mText: FText = NSLOCTEXT("", "43F49C524A75BDABC0B623B427BC074D", "Milestones Tier 1")
    
    def PreConstruct(self):
        ExecuteUbergraph_Widget_SpaceElevator_TierInfo.K2Node_Event_IsDesignTime = IsDesignTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_SpaceElevator_TierInfo(10)
    

    def ExecuteUbergraph_Widget_SpaceElevator_TierInfo(self):
        self.TierText.SetText(self.mText)
    
