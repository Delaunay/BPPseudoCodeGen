
from codegen.ue4_stub import *

from Script.Engine import Default__KismetSystemLibrary
from Game.FactoryGame.Interface.UI.InGame.-Shared.Struct_KeybindingHint import Struct_KeybindingHint
from Script.Engine import SetTextPropertyByName
from Script.Engine import PlayerController
from Script.UMG import AddChild
from Script.UMG import GetChildAt
from Script.Engine import Default__KismetArrayLibrary
from Script.UMG import UserWidget
from Script.Engine import Delay
from Script.UMG import Create
from Script.UMG import Widget
from Game.FactoryGame.Interface.UI.InGame.-Shared.Widget_Hint import Widget_Hint
from Game.FactoryGame.Interface.UI.InGame.-Shared.Widget_HintContainer import ExecuteUbergraph_Widget_HintContainer
from Script.UMG import GetChildrenCount
from Script.UMG import PanelSlot
from Script.UMG import Default__WidgetBlueprintLibrary
from Script.Engine import LatentActionInfo
from Game.FactoryGame.Interface.UI.InGame.-Shared.Widget_HintContainer import ExecuteUbergraph_Widget_HintContainer.K2Node_Event_IsDesignTime

class Widget_HintContainer(UserWidget):
    mKeyBindingHints: List[Struct_KeybindingHint]
    mShowKeybindingsOnConstruct: bool = True
    
    def SetKeybindingHints(self, mKeyBindingHints: Ref[List[Struct_KeybindingHint]]):
        ExecutionFlow.Push("L885")
        self.mKeyBindingHints = mKeyBindingHints
        
        ReturnValue: int32 = len(self.mKeyBindingHints)
        ReturnValue_0: bool = ReturnValue > 0
        if not ReturnValue_0:
            goto('L779')
        self.SetVisibility(3)
        self.mHintContainer.ClearChildren()
        Variable: int32 = 0
        Variable_0: int32 = 0
        
        # Label 237
        ReturnValue1: int32 = len(self.mKeyBindingHints)
        ReturnValue_1: bool = Variable <= ReturnValue1
        if not ReturnValue_1:
            goto('L796')
        Variable_0 = Variable
        ExecutionFlow.Push("L811")
        ReturnValue_2: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_3: Ptr[Widget_Hint] = Default__WidgetBlueprintLibrary.Create(self, Widget_Hint, ReturnValue_2)
        
        Item = None
        Item = self.mKeyBindingHints[Variable_0]
        
        Item.KeyBinding_5_6C26EF9041BC54531A02F2B5B7DC3464 = None
        Default__KismetSystemLibrary.SetTextPropertyByName(ReturnValue_3, "mHintKeyText", Ref[Item.KeyBinding_5_6C26EF9041BC54531A02F2B5B7DC3464])
        
        Item = None
        Item = self.mKeyBindingHints[Variable_0]
        
        Item.Action_3_8CED3F9B4A70C1822B95758560DE8695 = None
        Default__KismetSystemLibrary.SetTextPropertyByName(ReturnValue_3, "mHintDescriptionText", Ref[Item.Action_3_8CED3F9B4A70C1822B95758560DE8695])
        ReturnValue_4: Ptr[PanelSlot] = self.mHintContainer.AddChild(ReturnValue_3)
        goto(ExecutionFlow.Pop())
        # Label 779
        self.SetVisibility(1)
        goto(ExecutionFlow.Pop())
        # Label 796
        self.AnimateHints()
        goto(ExecutionFlow.Pop())
        # Label 811
        ReturnValue_5: int32 = Variable + 1
        Variable = ReturnValue_5
        goto('L237')
    

    def PreConstruct(self):
        ExecuteUbergraph_Widget_HintContainer.K2Node_Event_IsDesignTime = IsDesignTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_HintContainer(469)
    

    def AnimateHints(self):
        self.ExecuteUbergraph_Widget_HintContainer(503)
    

    def ExecuteUbergraph_Widget_HintContainer(self):
        goto(ComputedJump("EntryPoint"))
        ExecutionFlow.Push("L183")
        ReturnValue: Ptr[Widget] = self.mHintContainer.GetChildAt(Variable)
        Hint: Ptr[Widget_Hint] = Cast[Widget_Hint](ReturnValue)
        bSuccess: bool = Hint
        if not bSuccess:
           goto(ExecutionFlow.Pop())
        Hint.PlaySpawnAnim()
        goto(ExecutionFlow.Pop())
        # Label 183
        ReturnValue_0: int32 = Variable + 1
        Variable: int32 = ReturnValue_0
        # Label 252
        ReturnValue_1: int32 = self.mHintContainer.GetChildrenCount()
        ReturnValue_2: int32 = ReturnValue_1 - 1
        ReturnValue_3: bool = Variable <= ReturnValue_2
        if not ReturnValue_3:
           goto(ExecutionFlow.Pop())
        Default__KismetSystemLibrary.Delay(self, 0.05000000074505806, LatentActionInfo(Linkage = 15, UUID = -348465805, ExecutionFunction = "ExecuteUbergraph_Widget_HintContainer", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        if not self.mShowKeybindingsOnConstruct:
           goto(ExecutionFlow.Pop())
        
        self.SetKeybindingHints(Ref[self.mKeyBindingHints])
        goto(ExecutionFlow.Pop())
        Variable = 0
        goto('L252')
    
