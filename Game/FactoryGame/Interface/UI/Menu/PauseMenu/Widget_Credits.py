
from codegen.ue4_stub import *

from Script.UMG import UMGSequencePlayer
from Script.UMG import PlayAnimation
from Script.UMG import IsAnimationPlaying
from Game.FactoryGame.Interface.UI.Menu.BP_MenuBase import BP_MenuBase
from Game.FactoryGame.Interface.UI.Menu.BP_MenuBase import Construct
from Script.UMG import BindToAnimationFinished
from Game.FactoryGame.Interface.UI.Menu.BP_MenuBase import OnMenuEnter
from Game.FactoryGame.Interface.UI.Menu.BP_MenuBase import OnEscape
from Game.FactoryGame.Interface.UI.Menu.PauseMenu.Widget_Credits import ExecuteUbergraph_Widget_Credits.K2Node_Event_prevMenu
from Game.FactoryGame.Interface.UI.Menu.PauseMenu.Widget_Credits import ExecuteUbergraph_Widget_Credits
from Script.UMG import WidgetAnimation

class Widget_Credits(BP_MenuBase):
    CreditsTextAnim: Ptr[WidgetAnimation]
    OnBackClicked: FMulticastScriptDelegate
    UsesSubmenuBackground = True
    
    def OnEscape(self):
        self.ExecuteUbergraph_Widget_Credits(95)
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_Credits(100)
    

    def OnMenuEnter(self):
        ExecuteUbergraph_Widget_Credits.K2Node_Event_prevMenu = prevMenu #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_Credits(214)
    

    def ExecuteUbergraph_Widget_Credits(self):
        # Label 10
        ReturnValue: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.CreditsTextAnim, 0, 1, 0, 0.800000011920929)
        # End
        # Label 61
        self.OnEscape()
        self.OnBackClicked.ProcessMulticastDelegate()
        # End
        goto('L61')
        self.Construct()
        ReturnValue_0: bool = self.IsAnimationPlaying(self.CreditsTextAnim)
        if not ReturnValue_0:
            goto('L158')
        # End
        # Label 158
        OutputDelegate.BindUFunction(self, OnEscape)
        self.BindToAnimationFinished(self.CreditsTextAnim, OutputDelegate)
        # End
        self.OnMenuEnter(prevMenu)
        goto('L10')
    

    def OnBackClicked__DelegateSignature(self):
        pass
    
