
from codegen.ue4_stub import *

from Script.Engine import PlayerController
from Game.FactoryGame.Interface.UI.InGame.Widget_FicsitLogoSplash import ExecuteUbergraph_Widget_FicsitLogoSplash
from Script.Engine import GetPlayerName
from Script.UMG import UMGSequencePlayer
from Script.UMG import PlayAnimation
from Script.UMG import WidgetAnimation
from Script.UMG import UserWidget

class Widget_FicsitLogoSplash(UserWidget):
    SpawnAnim: Ptr[WidgetAnimation]
    Visibility = ESlateVisibility::Collapsed
    
    def ShowLogo(self):
        self.ExecuteUbergraph_Widget_FicsitLogoSplash(10)
    

    def ExecuteUbergraph_Widget_FicsitLogoSplash(self):
        ReturnValue: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.SpawnAnim, 0, 1, 2, 1)
        ReturnValue_0: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_1: FString = ReturnValue_0.PlayerState.GetPlayerName()
        self.mName.SetTitle(ReturnValue_1)
    
