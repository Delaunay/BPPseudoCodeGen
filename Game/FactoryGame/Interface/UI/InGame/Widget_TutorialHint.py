
from codegen.ue4_stub import *

from Script.UMG import UMGSequencePlayer
from Script.UMG import PlayAnimation
from Game.FactoryGame.Interface.UI.InGame.Widget_TutorialHint import ExecuteUbergraph_Widget_TutorialHint
from Script.UMG import WidgetAnimation
from Script.UMG import UserWidget

class Widget_TutorialHint(UserWidget):
    AniConstruct: Ptr[WidgetAnimation]
    mText: FText
    padding = Namespace(Bottom=0, Left=0, Right=0, Top=8)
    
    def Construct(self):
        self.ExecuteUbergraph_Widget_TutorialHint(61)
    

    def ExecuteUbergraph_Widget_TutorialHint(self):
        # Label 10
        ReturnValue: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.AniConstruct, 0, 1, 0, 1)
        # End
        goto('L10')
    
