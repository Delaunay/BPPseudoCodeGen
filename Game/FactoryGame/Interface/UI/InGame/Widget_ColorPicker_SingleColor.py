
from codegen.ue4_stub import *

from Game.FactoryGame.Interface.UI.InGame.Widget_ColorPicker_SingleColor import ExecuteUbergraph_Widget_ColorPicker_SingleColor
from Game.FactoryGame.Interface.UI.InGame.Widget_ColorPicker_SingleColor import ExecuteUbergraph_Widget_ColorPicker_SingleColor.K2Node_Event_IsDesignTime
from Script.UMG import UserWidget
from Script.CoreUObject import LinearColor

class Widget_ColorPicker_SingleColor(UserWidget):
    OnClose: FMulticastScriptDelegate
    StartColor: LinearColor
    
    def SetupStartColor(self, Color: LinearColor):
        self.Widget_ColorPicker_Module.SetupColorAndSliders(Color)
    

    def PreConstruct(self):
        ExecuteUbergraph_Widget_ColorPicker_SingleColor.K2Node_Event_IsDesignTime = IsDesignTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_ColorPicker_SingleColor(29)
    

    def BndEvt__mEditPresetAccept_K2Node_ComponentBoundEvent_0_OnClicked__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_ColorPicker_SingleColor(57)
    

    def BndEvt__mEditPresetCanel_K2Node_ComponentBoundEvent_1_OnClicked__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_ColorPicker_SingleColor(126)
    

    def ExecuteUbergraph_Widget_ColorPicker_SingleColor(self):
        # Label 10
        self.RemoveFromParent()
        # End
        self.SetupStartColor(self.StartColor)
        # End
        self.OnClose.ProcessMulticastDelegate(self.Widget_ColorPicker_Module.CurrentColor)
        self.RemoveFromParent()
        # End
        self.OnClose.ProcessMulticastDelegate(self.Widget_ColorPicker_Module.StartColor)
        goto('L10')
    

    def OnClose__DelegateSignature(self, Color: LinearColor):
        pass
    
