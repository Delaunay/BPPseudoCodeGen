
from codegen.ue4_stub import *

from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import SetTextPropertyByName
from Script.Engine import PlayerController
from Script.UMG import AddChild
from Game.FactoryGame.Interface.UI.InGame.Widget_TutorialInfo import ExecuteUbergraph_Widget_TutorialInfo
from Script.Engine import Default__KismetArrayLibrary
from Script.UMG import UMGSequencePlayer
from Script.UMG import Create
from Script.UMG import PlayAnimation
from Game.FactoryGame.Interface.UI.InGame.Widget_TutorialHint import Widget_TutorialHint
from Script.UMG import WidgetAnimation
from Script.UMG import PanelSlot
from Script.UMG import Default__WidgetBlueprintLibrary
from Script.FactoryGame import FormatStringWithKeyNames
from Script.UMG import UserWidget
from Script.FactoryGame import Default__FGInputLibrary

class Widget_TutorialInfo(UserWidget):
    SpawnAnim: Ptr[WidgetAnimation]
    mTitle: FText
    mHints: List[FText]
    
    def Construct(self):
        self.ExecuteUbergraph_Widget_TutorialInfo(677)
    

    def ExecuteUbergraph_Widget_TutorialInfo(self):
        goto(ComputedJump("EntryPoint"))
        # Label 15
        ExecutionFlow.Push("L372")
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_0: Ptr[Widget_TutorialHint] = Default__WidgetBlueprintLibrary.Create(self, Widget_TutorialHint, ReturnValue)
        ReturnValue = self.GetOwningPlayer()
        
        Item = None
        Item = self.mHints[Variable]
        ReturnValue_1: FText = Default__FGInputLibrary.FormatStringWithKeyNames(ReturnValue, Item, True)
        
        Default__KismetSystemLibrary.SetTextPropertyByName(ReturnValue_0, "mText", Ref[ReturnValue_1])
        ReturnValue_2: Ptr[PanelSlot] = self.mBox.AddChild(ReturnValue_0)
        goto(ExecutionFlow.Pop())
        # Label 372
        ReturnValue_3: int32 = Variable + 1
        Variable: int32 = ReturnValue_3
        
        # Label 441
        ReturnValue_4: int32 = len(self.mHints)
        ReturnValue_5: bool = Variable <= ReturnValue_4
        if not ReturnValue_5:
           goto(ExecutionFlow.Pop())
        Variable = Variable
        goto('L15')
        # Label 580
        ReturnValue_6: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.SpawnAnim, 0, 1, 0, 1)
        Variable = 0
        Variable = 0
        goto('L441')
        goto('L580')
    
