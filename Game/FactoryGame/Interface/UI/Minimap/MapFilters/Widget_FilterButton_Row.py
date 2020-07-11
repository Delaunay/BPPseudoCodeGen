
from codegen.ue4_stub import *

from Game.FactoryGame.Interface.UI.Minimap.MapFilters.Widget_FilterButton_Row import ExecuteUbergraph_Widget_FilterButton_Row
from Script.Engine import TimerHandle
from Game.FactoryGame.Interface.UI.Minimap.MapFilters.Widget_FilterButton_Row import ExecuteUbergraph_Widget_FilterButton_Row.K2Node_Event_IsDesignTime
from Script.UMG import SetWidthOverride
from Script.UMG import UserWidget

class Widget_FilterButton_Row(UserWidget):
    mFilterText: FText = NSLOCTEXT("", "33F4C47A4511F6D2E8BB7995BAF75218", "ohfailafwiszfihzwfizsf")
    mIsSelected: bool
    NewVar_0: TimerHandle
    OnClicked: FMulticastScriptDelegate
    OnPressed: FMulticastScriptDelegate
    OnHovered: FMulticastScriptDelegate
    OnUnhovered: FMulticastScriptDelegate
    mFilterOptionWidth: float = 120
    
    def SetTitle(self, Title: FText):
        self.mFilterText = Title
        self.mFilterName.SetText(self.mFilterText)
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_FilterButton_Row(10)
    

    def BndEvt__mFilterRowButton_K2Node_ComponentBoundEvent_0_OnButtonClickedEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_FilterButton_Row(15)
    

    def BndEvt__mFilterRowButton_K2Node_ComponentBoundEvent_1_OnButtonPressedEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_FilterButton_Row(39)
    

    def BndEvt__mFilterRowButton_K2Node_ComponentBoundEvent_2_OnButtonHoverEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_FilterButton_Row(63)
    

    def BndEvt__mFilterRowButton_K2Node_ComponentBoundEvent_3_OnButtonHoverEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_FilterButton_Row(87)
    

    def PreConstruct(self):
        ExecuteUbergraph_Widget_FilterButton_Row.K2Node_Event_IsDesignTime = IsDesignTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_FilterButton_Row(111)
    

    def ExecuteUbergraph_Widget_FilterButton_Row(self):
        # End
        self.OnClicked.ProcessMulticastDelegate()
        # End
        self.OnPressed.ProcessMulticastDelegate()
        # End
        self.OnHovered.ProcessMulticastDelegate()
        # End
        self.OnUnhovered.ProcessMulticastDelegate()
        # End
        self.SetTitle(self.mFilterText)
        self.mOptionSizeBox.SetWidthOverride(self.mFilterOptionWidth)
    

    def OnUnhovered__DelegateSignature(self):
        pass
    

    def OnHovered__DelegateSignature(self):
        pass
    

    def OnPressed__DelegateSignature(self):
        pass
    

    def OnClicked__DelegateSignature(self):
        pass
    
