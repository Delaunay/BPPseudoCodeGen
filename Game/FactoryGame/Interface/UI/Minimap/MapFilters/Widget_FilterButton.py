
from codegen.ue4_stub import *

from Game.FactoryGame.Interface.UI.Minimap.MapFilters.Widget_FilterButton import ExecuteUbergraph_Widget_FilterButton.K2Node_ComponentBoundEvent_IsChecked
from Game.FactoryGame.Interface.UI.Minimap.MapFilters.Widget_FilterButton import ExecuteUbergraph_Widget_FilterButton.K2Node_Event_IsDesignTime
from Game.FactoryGame.Interface.UI.Minimap.MapFilters.Widget_FilterButton import ExecuteUbergraph_Widget_FilterButton.K2Node_ComponentBoundEvent_IsChecked1
from Game.FactoryGame.Interface.UI.Minimap.MapFilters.Widget_FilterButton import ExecuteUbergraph_Widget_FilterButton
from Script.UMG import UserWidget

class Widget_FilterButton(UserWidget):
    mName: FText = NSLOCTEXT("", "32CD6B0B43F5C6587AD265A1CD61B64F", "Filter")
    OnHovered: FMulticastScriptDelegate
    OnUnhovered: FMulticastScriptDelegate
    mShowOnCompass: bool
    mShowOnMap: bool
    mShowOnMapChanged: FMulticastScriptDelegate
    mShowOnCompassChanged: FMulticastScriptDelegate
    
    def SetTitle(self, mName: FText):
        self.mName = mName
        self.Widget_FilterButton_Row.SetTitle(self.mName)
    

    def PreConstruct(self):
        ExecuteUbergraph_Widget_FilterButton.K2Node_Event_IsDesignTime = IsDesignTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_FilterButton(10)
    

    def BndEvt__mShowOnCompassCheckbox_K2Node_ComponentBoundEvent_0_OnCheckChanged__DelegateSignature(self, IsChecked: bool):
        ExecuteUbergraph_Widget_FilterButton.K2Node_ComponentBoundEvent_IsChecked1 = IsChecked #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_FilterButton(38)
    

    def BndEvt__mShowOnMapCheckbox_K2Node_ComponentBoundEvent_1_OnCheckChanged__DelegateSignature(self, IsChecked: bool):
        ExecuteUbergraph_Widget_FilterButton.K2Node_ComponentBoundEvent_IsChecked = IsChecked #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_FilterButton(146)
    

    def BndEvt__Widget_FilterButton_Row_K2Node_ComponentBoundEvent_2_OnHovered__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_FilterButton(254)
    

    def BndEvt__Widget_FilterButton_Row_K2Node_ComponentBoundEvent_3_OnUnhovered__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_FilterButton(279)
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_FilterButton(304)
    

    def ExecuteUbergraph_Widget_FilterButton(self):
        self.SetTitle(self.mName)
        # End
        
        IsChecked = None
        self.mShowOnCompassCheckbox.SetChecked(IsChecked1, False, Ref[IsChecked])
        self.mShowOnCompass = IsChecked
        self.mShowOnCompassChanged.ProcessMulticastDelegate(self, self.mShowOnCompass)
        # End
        
        IsChecked1 = None
        self.mShowOnMapCheckbox.SetChecked(IsChecked, False, Ref[IsChecked1])
        self.mShowOnMap = IsChecked1
        self.mShowOnMapChanged.ProcessMulticastDelegate(self, self.mShowOnMap)
        # End
        self.OnHovered.ProcessMulticastDelegate(self)
        # End
        self.OnUnhovered.ProcessMulticastDelegate(self)
        # End
        
        IsChecked2 = None
        self.mShowOnMapCheckbox.SetChecked(self.mShowOnMap, False, Ref[IsChecked2])
        
        IsChecked3 = None
        self.mShowOnCompassCheckbox.SetChecked(self.mShowOnCompass, False, Ref[IsChecked3])
    

    def mShowOnCompassChanged__DelegateSignature(self, Instigator: Ptr[Widget_FilterButton], ShowOnCompass: bool):
        pass
    

    def mShowOnMapChanged__DelegateSignature(self, Instigator: Ptr[Widget_FilterButton], ShowOnMap: bool):
        pass
    

    def OnUnhovered__DelegateSignature(self, Instigator: Ptr[Widget_FilterButton]):
        pass
    

    def OnHovered__DelegateSignature(self, Instigator: Ptr[Widget_FilterButton]):
        pass
    
