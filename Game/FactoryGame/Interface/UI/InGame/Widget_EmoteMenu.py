
from codegen.ue4_stub import *

from Game.FactoryGame.Interface.UI.InGame.Widget_EmoteMenu import ExecuteUbergraph_Widget_EmoteMenu.K2Node_Event_InDeltaTime
from Script.Engine import PlayerController
from Script.UMG import Construct
from Script.FactoryGame import FGInteractWidget
from Game.FactoryGame.Interface.UI.InGame.Widget_EmoteMenu import ExecuteUbergraph_Widget_EmoteMenu
from Game.FactoryGame.Interface.UI.InGame.Widget_EmoteMenu import ExecuteUbergraph_Widget_EmoteMenu.K2Node_Event_MyGeometry

class Widget_EmoteMenu(FGInteractWidget):
    ShowEmote: FMulticastScriptDelegate
    mRestoreFocusWhenLost = True
    mDesiredHorizontalAlignment = 2
    mDesiredVerticalAlignment = 2
    mCallCustomTickOnConstruct = True
    
    def Construct(self):
        self.ExecuteUbergraph_Widget_EmoteMenu(10)
    

    def Destruct(self):
        self.ExecuteUbergraph_Widget_EmoteMenu(127)
    

    def Tick(self):
        ExecuteUbergraph_Widget_EmoteMenu.K2Node_Event_MyGeometry = MyGeometry #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_EmoteMenu.K2Node_Event_InDeltaTime = InDeltaTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_EmoteMenu(243)
    

    def ExecuteUbergraph_Widget_EmoteMenu(self):
        self.Construct()
        self.Widget_RadialMenu.Generate Radial Menu()
        # End
        # Label 61
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue.SetIgnoreLookInput(True)
        # End
        self.ShowEmote.ProcessMulticastDelegate(self.Widget_RadialMenu.SelectedInt)
        ReturnValue1: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue1.SetIgnoreLookInput(False)
        # End
        ReturnValue2: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_0: bool = ReturnValue2.IsLookInputIgnored()
        if not ReturnValue_0:
            goto('L61')
    

    def ShowEmote__DelegateSignature(self, EmoteIndex: int32):
        pass
    
