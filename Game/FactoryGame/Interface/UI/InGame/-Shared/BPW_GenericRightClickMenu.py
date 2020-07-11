
from codegen.ue4_stub import *

from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import SetTextPropertyByName
from Script.Engine import SetStructurePropertyByName
from Script.UMG import AddChild
from Game.FactoryGame.Interface.UI.InGame.-Shared.Widget_StandardButton import Widget_StandardButton
from Script.Engine import Default__KismetArrayLibrary
from Script.UMG import UserWidget
from Script.UMG import Create
from Game.FactoryGame.Interface.UI.InGame.-Shared.BPW_GenericRightClickMenu import ExecuteUbergraph_BPW_GenericRightClickMenu.K2Node_Event_IsDesignTime
from Script.UMG import GetChildIndex
from Game.FactoryGame.Interface.UI.InGame.-Shared.StandardButton_Struct import StandardButton_Struct
from Script.UMG import PanelSlot
from Game.FactoryGame.Interface.UI.InGame.-Shared.BPW_GenericRightClickMenu import ExecuteUbergraph_BPW_GenericRightClickMenu
from Script.Engine import SetFloatPropertyByName
from Script.UMG import Default__WidgetBlueprintLibrary

class BPW_GenericRightClickMenu(UserWidget):
    mButtons: List[StandardButton_Struct]
    OnMenuButtonClicked: FMulticastScriptDelegate
    
    def OnClicked(self, ButtonWidget: Ptr[Widget_StandardButton]):
        ReturnValue: int32 = self.mButtonsContainer.GetChildIndex(ButtonWidget)
        self.OnMenuButtonClicked.ProcessMulticastDelegate(ReturnValue)
    

    def PreConstruct(self):
        ExecuteUbergraph_BPW_GenericRightClickMenu.K2Node_Event_IsDesignTime = IsDesignTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BPW_GenericRightClickMenu(857)
    

    def Destruct(self):
        self.ExecuteUbergraph_BPW_GenericRightClickMenu(862)
    

    def ExecuteUbergraph_BPW_GenericRightClickMenu(self):
        goto(ComputedJump("EntryPoint"))
        # Label 15
        self.OnMenuButtonClicked.Clear()
        goto(ExecutionFlow.Pop())
        # Label 26
        ExecutionFlow.Push("L593")
        ReturnValue: Ptr[Widget_StandardButton] = Default__WidgetBlueprintLibrary.Create(self, Widget_StandardButton, None)
        
        Item = None
        Item = self.mButtons[Variable]
        
        Item.Text_4_E8EE19824CB6399AF427C8B677E5F49E = None
        Default__KismetSystemLibrary.SetTextPropertyByName(ReturnValue, "mText", Ref[Item.Text_4_E8EE19824CB6399AF427C8B677E5F49E])
        
        Item = None
        Item = self.mButtons[Variable]
        
        Item.IconBrush_6_6BF4D8794D306ACEE50EA8B1767667C2 = None
        Default__KismetSystemLibrary.SetStructurePropertyByName(ReturnValue, "mIconBrush", Ref[Item.IconBrush_6_6BF4D8794D306ACEE50EA8B1767667C2])
        
        Item = None
        Item = self.mButtons[Variable]
        Default__KismetSystemLibrary.SetFloatPropertyByName(ReturnValue, "mIconHeight", Item.IconHeight_10_2FCF433D46FC80760CD5018CA8C45619)
        OutputDelegate.BindUFunction(self, OnClicked)
        ReturnValue.OnClickedIncludeSelf.AddUnique(OutputDelegate)
        ReturnValue_0: Ptr[PanelSlot] = self.mButtonsContainer.AddChild(ReturnValue)
        goto(ExecutionFlow.Pop())
        # Label 593
        ReturnValue_1: int32 = Variable + 1
        Variable: int32 = ReturnValue_1
        
        # Label 662
        ReturnValue_2: int32 = len(self.mButtons)
        ReturnValue_3: bool = Variable <= ReturnValue_2
        if not ReturnValue_3:
           goto(ExecutionFlow.Pop())
        Variable = Variable
        goto('L26')
        # Label 801
        Variable = 0
        goto('L662')
        # Label 829
        Variable = 0
        goto('L801')
        goto('L829')
        goto('L15')
    

    def OnMenuButtonClicked__DelegateSignature(self, ButtonIndex: int32):
        pass
    
