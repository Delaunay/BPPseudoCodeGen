
from codegen.ue4_stub import *

from Game.FactoryGame.Interface.UI.InGame.BuildMenu.Prototype.BPW_AddHotbarPreset_Button import ExecuteUbergraph_BPW_AddHotbarPreset_Button
from Script.UMG import UserWidget

class BPW_AddHotbarPreset_Button(UserWidget):
    OnAddHotbarPresetClicked: FMulticastScriptDelegate
    
    def BndEvt__BPW_BuildMenuButton_Base_K2Node_ComponentBoundEvent_0_OnButtonClicked__DelegateSignature(self):
        self.ExecuteUbergraph_BPW_AddHotbarPreset_Button(34)
    

    def ExecuteUbergraph_BPW_AddHotbarPreset_Button(self):
        # Label 10
        self.OnAddHotbarPresetClicked.ProcessMulticastDelegate()
        # End
        goto('L10')
    

    def OnAddHotbarPresetClicked__DelegateSignature(self):
        pass
    
