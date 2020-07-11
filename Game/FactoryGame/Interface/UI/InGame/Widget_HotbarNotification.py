
from codegen.ue4_stub import *

from Game.FactoryGame.Interface.UI.InGame.Widget_HotbarNotification import ExecuteUbergraph_Widget_HotbarNotification
from Game.FactoryGame.Interface.UI.HUDHelpers.HUDHelpers import Default__HUDHelpers
from Script.UMG import UserWidget
from Script.UMG import WidgetAnimation

class Widget_HotbarNotification(UserWidget):
    HotbarPopUp: Ptr[WidgetAnimation]
    
    def GetDarkGrayColour(self):
        
        Text = None
        Graphics = None
        Default__HUDHelpers.GetFactoryGameDarkGray(self, Ref[Text], Ref[Graphics])
        ReturnValue = Text
    

    def WidgetAnimationEvt_HotbarPopUp_K2Node_WidgetAnimationEvent_0(self):
        self.ExecuteUbergraph_Widget_HotbarNotification(96)
    

    def WidgetAnimationEvt_HotbarPopUp_K2Node_WidgetAnimationEvent_1(self):
        self.ExecuteUbergraph_Widget_HotbarNotification(10)
    

    def ExecuteUbergraph_Widget_HotbarNotification(self):
        self.Overlay_0.SetVisibility(1)
        # End
        # Label 53
        self.Overlay_0.SetVisibility(3)
        # End
        goto('L53')
    
