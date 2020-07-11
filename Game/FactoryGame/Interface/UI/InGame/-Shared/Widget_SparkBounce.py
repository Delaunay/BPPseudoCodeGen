
from codegen.ue4_stub import *

from Script.UMG import UMGSequencePlayer
from Script.UMG import PlayAnimation
from Game.FactoryGame.Interface.UI.InGame.-Shared.Widget_SparkBounce import ExecuteUbergraph_Widget_SparkBounce
from Script.UMG import BindToAnimationFinished
from Script.UMG import WidgetAnimation
from Script.UMG import UserWidget

class Widget_SparkBounce(UserWidget):
    SpawnAnim: Ptr[WidgetAnimation]
    
    def Construct(self):
        self.ExecuteUbergraph_Widget_SparkBounce(29)
    

    def OnAnimFinished(self):
        self.ExecuteUbergraph_Widget_SparkBounce(131)
    

    def ExecuteUbergraph_Widget_SparkBounce(self):
        # Label 10
        self.RemoveFromParent()
        # End
        ReturnValue: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.SpawnAnim, 0, 1, 0, 1)
        OutputDelegate.BindUFunction(self, OnAnimFinished)
        self.BindToAnimationFinished(self.SpawnAnim, OutputDelegate)
        # End
        goto('L10')
    
