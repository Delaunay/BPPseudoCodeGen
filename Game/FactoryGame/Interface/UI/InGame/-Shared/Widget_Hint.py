
from codegen.ue4_stub import *

from Script.Engine import PlayerController
from Script.UMG import UserWidget
from Script.UMG import UMGSequencePlayer
from Script.UMG import PlayAnimation
from Script.UMG import SetRenderOpacity
from Script.UMG import WidgetAnimation
from Game.FactoryGame.Interface.UI.InGame.-Shared.Widget_Hint import ExecuteUbergraph_Widget_Hint
from Script.FactoryGame import FormatStringWithKeyNames
from Game.FactoryGame.Interface.UI.InGame.-Shared.Widget_Hint import ExecuteUbergraph_Widget_Hint.K2Node_Event_IsDesignTime
from Script.FactoryGame import Default__FGInputLibrary

class Widget_Hint(UserWidget):
    SpawnAnim: Ptr[WidgetAnimation]
    mHintKeyText: FText = NSLOCTEXT("", "E85EC53E476A3EA3FA64FCAF56D46589", "Key")
    mHintDescriptionText: FText = NSLOCTEXT("", "F56FF73E4FC1078A59E583804C3D7A7B", "Action")
    
    def PlaySpawnAnim(self):
        ReturnValue: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.SpawnAnim, 0, 1, 0, 1)
    

    def PreConstruct(self):
        ExecuteUbergraph_Widget_Hint.K2Node_Event_IsDesignTime = IsDesignTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_Hint(10)
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_Hint(105)
    

    def ExecuteUbergraph_Widget_Hint(self):
        self.mHintDescription.SetText(self.mHintDescriptionText)
        self.mHintKey.SetText(self.mHintKeyText)
        # End
        self.mActionContainer.SetRenderOpacity(0)
        self.mKeyContainer.SetRenderOpacity(0)
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_0: FText = Default__FGInputLibrary.FormatStringWithKeyNames(ReturnValue, self.mHintKeyText, True)
        self.mHintKey.SetText(ReturnValue_0)
    
