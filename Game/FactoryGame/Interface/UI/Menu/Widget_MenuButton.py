
from codegen.ue4_stub import *

from Script.UMG import SetUserFocus
from Script.UMG import GetParent
from Script.UMG import SetKeyboardFocus
from Script.UMG import WidgetSwitcher
from Script.UMG import GetChildIndex
from Script.Engine import Not_PreBool
from Game.FactoryGame.Interface.UI.Menu.Widget_MenuButton import ExecuteUbergraph_Widget_MenuButton
from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import PlayerController
from Script.Engine import Default__KismetArrayLibrary
from Script.Engine import IsValid
from Script.FactoryGame import GetAllWidgetsOfClassInHierarchy
from Script.Engine import EqualEqual_IntInt
from Script.UMG import PanelWidget
from Script.FactoryGame import FGButtonWidget
from Script.FactoryGame import Default__FGBlueprintFunctionLibrary
from Game.FactoryGame.Interface.UI.HUDHelpers.HUDHelpers import Default__HUDHelpers
from Script.Engine import SelectColor
from Script.SlateCore import SlateBrush
from Script.CoreUObject import LinearColor

class Widget_MenuButton(FGButtonWidget):
    OnClicked: FMulticastScriptDelegate
    mText: FText
    mBrush: SlateBrush
    mIndexAsChild: int32
    mCachedTabSwitcher: Ptr[WidgetSwitcher]
    OnClickedAsTabSwitcher: FMulticastScriptDelegate
    bIsFocusable = True
    
    def GetHoverColor(self):
        ReturnValue: bool = self.MenuButton.IsHovered()
        if not ReturnValue:
            goto('L303')
        
        TextWhite2 = None
        GraphicsWhite2 = None
        Default__HUDHelpers.GetFactoryGameWhite(self, Ref[TextWhite2], Ref[GraphicsWhite2])
        
        Text = None
        Graphics = None
        Default__HUDHelpers.GetFactoryGameDarkGray(self, Ref[Text], Ref[Graphics])
        ReturnValue = self.MenuButton.IsHovered()
        ReturnValue1: LinearColor = SelectColor(Graphics, GraphicsWhite2, ReturnValue)
        ReturnValue_0: LinearColor = ReturnValue1
        goto('L707')
        # Label 303
        ReturnValue_1: bool = Default__KismetSystemLibrary.IsValid(self.mCachedTabSwitcher)
        if not ReturnValue_1:
            goto('L625')
        
        TextWhite1 = None
        GraphicsWhite1 = None
        Default__HUDHelpers.GetFactoryGameWhite(self, Ref[TextWhite1], Ref[GraphicsWhite1])
        
        Orange = None
        OrangeText = None
        Default__HUDHelpers.GetFactoryGameOrange(self, Ref[Orange], Ref[OrangeText])
        ReturnValue_2: bool = EqualEqual_IntInt(self.mCachedTabSwitcher.ActiveWidgetIndex, self.mIndexAsChild)
        ReturnValue_3: LinearColor = SelectColor(Orange, GraphicsWhite1, ReturnValue_2)
        ReturnValue_0 = ReturnValue_3
        # Label 620
        goto('L707')
        
        TextWhite = None
        GraphicsWhite = None
        # Label 625
        Default__HUDHelpers.GetFactoryGameWhite(self, Ref[TextWhite], Ref[GraphicsWhite])
        ReturnValue_0 = GraphicsWhite
    

    def GetButtonColor(self):
        ReturnValue: bool = self.MenuButton.IsHovered()
        if not ReturnValue:
            goto('L303')
        
        Text = None
        Graphics = None
        Default__HUDHelpers.GetFactoryGameDarkGray(self, Ref[Text], Ref[Graphics])
        
        TextWhite1 = None
        GraphicsWhite1 = None
        Default__HUDHelpers.GetFactoryGameWhite(self, Ref[TextWhite1], Ref[GraphicsWhite1])
        ReturnValue = self.MenuButton.IsHovered()
        ReturnValue1: LinearColor = SelectColor(Graphics, GraphicsWhite1, ReturnValue)
        ReturnValue_0: LinearColor = ReturnValue1
        goto('L620')
        # Label 303
        ReturnValue_1: bool = Default__KismetSystemLibrary.IsValid(self.mCachedTabSwitcher)
        if not ReturnValue_1:
            goto('L620')
        
        TextWhite = None
        GraphicsWhite = None
        Default__HUDHelpers.GetFactoryGameWhite(self, Ref[TextWhite], Ref[GraphicsWhite])
        
        Orange = None
        OrangeText = None
        Default__HUDHelpers.GetFactoryGameOrange(self, Ref[Orange], Ref[OrangeText])
        ReturnValue_2: bool = EqualEqual_IntInt(self.mCachedTabSwitcher.ActiveWidgetIndex, self.mIndexAsChild)
        ReturnValue_3: LinearColor = SelectColor(Orange, GraphicsWhite, ReturnValue_2)
        ReturnValue_0 = ReturnValue_3
    

    def SetFocused(self):
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        self.MenuButton.SetUserFocus(ReturnValue)
        self.MenuButton.SetKeyboardFocus()
    

    def OnFocusReceived(self):
        pass
    

    def HideButton(self):
        self.MenuButton.SetVisibility(2)
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_MenuButton(699)
    

    def BndEvt__Button_0_K2Node_ComponentBoundEvent_0_OnButtonClickedEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_MenuButton(766)
    

    def Destruct(self):
        self.ExecuteUbergraph_Widget_MenuButton(846)
    

    def OnThisMenuButtonClicked(self):
        self.ExecuteUbergraph_Widget_MenuButton(851)
    

    def ExecuteUbergraph_Widget_MenuButton(self):
        goto(ComputedJump("EntryPoint"))
        # Label 15
        ExecutionFlow.Push("L110")
        
        foundWidgets = None
        Item = None
        Item = foundWidgets[Variable]
        self.mCachedTabSwitcher = Item
        Variable: bool = True
        goto(ExecutionFlow.Pop())
        # Label 110
        ReturnValue: int32 = Variable_0 + 1
        Variable_0: int32 = ReturnValue
        # Label 179
        ReturnValue_0: bool = Not_PreBool(Variable)
        
        foundWidgets = None
        ReturnValue_1: int32 = len(foundWidgets)
        ReturnValue_2: bool = Variable_0 <= ReturnValue_1
        ReturnValue_3: bool = ReturnValue_0 and ReturnValue_2
        if not ReturnValue_3:
            goto('L389')
        Variable = Variable_0
        goto('L15')
        # Label 389
        OutputDelegate.BindUFunction(self, OnThisMenuButtonClicked)
        self.OnClickedAsTabSwitcher.AddUnique(OutputDelegate)
        ReturnValue_4: Ptr[PanelWidget] = self.GetParent()
        ReturnValue_5: int32 = ReturnValue_4.GetChildIndex(self)
        self.mIndexAsChild = ReturnValue_5
        goto(ExecutionFlow.Pop())
        # Label 530
        ReturnValue_6: bool = Default__KismetSystemLibrary.IsValid(self.mCachedTabSwitcher)
        if not ReturnValue_6:
           goto(ExecutionFlow.Pop())
        self.mCachedTabSwitcher.SetActiveWidgetIndex(self.mIndexAsChild)
        goto(ExecutionFlow.Pop())
        # Label 637
        Variable = False
        Variable_0 = 0
        Variable = 0
        goto('L179')
        foundWidgets: List[Ptr[WidgetSwitcher]] = []
        
        Default__FGBlueprintFunctionLibrary.GetAllWidgetsOfClassInHierarchy(self, WidgetSwitcher, Ref[foundWidgets])
        goto('L637')
        self.mCachedTabSwitcher.SetActiveWidgetIndex(self.mIndexAsChild)
        self.OnClicked.ProcessMulticastDelegate()
        goto(ExecutionFlow.Pop())
        # Label 831
        self.HideButton()
        goto(ExecutionFlow.Pop())
        goto('L831')
        goto('L530')
    

    def OnClickedAsTabSwitcher__DelegateSignature(self):
        pass
    

    def OnClicked__DelegateSignature(self):
        pass
    
