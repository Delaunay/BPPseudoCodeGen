
from codegen.ue4_stub import *

from Script.UMG import UMGSequencePlayer
from Script.UMG import PlayAnimation
from Script.UMG import ESlateVisibility
from Game.FactoryGame.Interface.UI.InGame.ActorDetails.Widget_ActorDetails_Container import ExecuteUbergraph_Widget_ActorDetails_Container.K2Node_Event_IsDesignTime
from Game.FactoryGame.Interface.UI.InGame.ActorDetails.Widget_ActorDetails_Container import ExecuteUbergraph_Widget_ActorDetails_Container
from Script.UMG import WidgetAnimation
from Script.UMG import UserWidget

class Widget_ActorDetails_Container(UserWidget):
    SpawnAnim: Ptr[WidgetAnimation]
    mTitle: FText = NSLOCTEXT("", "1B33AA404DCBAA5DEDF2AA82C489C0E8", "Name Here")
    ShowPointer: bool = True
    
    def SetShowPointer(self, ShowPointer: bool):
        self.ShowPointer = ShowPointer
        Variable: bool = self.ShowPointer
        Variable_0: uint8 = 3
        Variable1: uint8 = 1
        
        switch = {
            False: Variable1,
            True: Variable_0
        }
        self.mPointer.SetVisibility(switch.get(Variable, None))
    

    def SetTitle(self, mTitle: FText):
        self.mTitle = mTitle
        self.mTitleObject.SetText(self.mTitle)
    

    def PreConstruct(self):
        ExecuteUbergraph_Widget_ActorDetails_Container.K2Node_Event_IsDesignTime = IsDesignTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_ActorDetails_Container(38)
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_ActorDetails_Container(66)
    

    def ExecuteUbergraph_Widget_ActorDetails_Container(self):
        # Label 10
        self.SetShowPointer(self.ShowPointer)
        # End
        self.SetTitle(self.mTitle)
        goto('L10')
        ReturnValue: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.SpawnAnim, 0, 1, 0, 1)
    
