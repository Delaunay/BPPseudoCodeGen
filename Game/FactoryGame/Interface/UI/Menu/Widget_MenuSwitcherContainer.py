
from codegen.ue4_stub import *

from Script.Engine import Default__KismetSystemLibrary
from Script.UMG import GetChildAt
from Script.UMG import UMGSequencePlayer
from Script.UMG import HasAnyChildren
from Script.UMG import Widget
from Script.UMG import PlayAnimation
from Game.FactoryGame.Interface.UI.Menu.BP_MenuBase import BP_MenuBase
from Script.UMG import WidgetSwitcher
from Script.UMG import StopAnimation
from Script.Engine import IsValid
from Script.UMG import SetRenderOpacity
from Script.UMG import WidgetAnimation
from Game.FactoryGame.Interface.UI.Menu.Widget_MenuSwitcherContainer import ExecuteUbergraph_Widget_MenuSwitcherContainer.K2Node_CustomEvent_Widget
from Game.FactoryGame.Interface.UI.Menu.Widget_MenuSwitcherContainer import ExecuteUbergraph_Widget_MenuSwitcherContainer
from Script.Engine import Not_PreBool
from Script.UMG import UserWidget

class Widget_MenuSwitcherContainer(UserWidget):
    HideSwitcher: Ptr[WidgetAnimation]
    mSwitcherWidget: Ptr[WidgetSwitcher]
    mPreviousWidget: Ptr[Widget]
    PlayBackgroundAnim: bool
    OnWidgetSet: FMulticastScriptDelegate
    
    def GetFirstChildOfSwitcher(self, SwitcherWidget: Ptr[PanelWidget]):
        ReturnValue: bool = SwitcherWidget.HasAnyChildren()
        if not ReturnValue:
            goto('L122')
        ReturnValue_0: Ptr[Widget] = SwitcherWidget.GetChildAt(0)
        Child = ReturnValue_0
    

    def SetSwitcherWidget(self):
        ReturnValue: Ptr[Widget] = self.mSwitcherWidgetSlot.GetChildAt(0)
        Switcher: Ptr[WidgetSwitcher] = Cast[WidgetSwitcher](ReturnValue)
        bSuccess: bool = Switcher
        if not bSuccess:
            goto('L164')
        self.mSwitcherWidget = Switcher
        Widget Switcher = self.mSwitcherWidget
    

    def SetNoneActive(self):
        self.ExecuteUbergraph_Widget_MenuSwitcherContainer(558)
    

    def SetActiveWidget(self, Widget: Ptr[Widget]):
        ExecuteUbergraph_Widget_MenuSwitcherContainer.K2Node_CustomEvent_Widget = Widget #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_MenuSwitcherContainer(817)
    

    def WidgetAnimationEvt_HideSwitcher_K2Node_WidgetAnimationEvent_0(self):
        self.ExecuteUbergraph_Widget_MenuSwitcherContainer(10)
    

    def ExecuteUbergraph_Widget_MenuSwitcherContainer(self):
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(self.mSwitcherWidget)
        if not ReturnValue:
            goto('L822')
        self.mSwitcherWidget.SetActiveWidgetIndex(0)
        ReturnValue_0: bool = self.mSwitcherWidget.HasAnyChildren()
        if not ReturnValue_0:
            goto('L243')
        ReturnValue_1: Ptr[Widget] = self.mSwitcherWidget.GetChildAt(0)
        self.mPreviousWidget = ReturnValue_1
        # End
        # Label 243
        self.mPreviousWidget = None
        # End
        # Label 259
        self.PlayBackgroundAnim = True
        # Label 270
        Base1.SpawnAnim(self.PlayBackgroundAnim)
        # Label 315
        self.mSwitcherWidget.SetActiveWidget(Widget)
        self.mPreviousWidget = Widget
        self.OnWidgetSet.ProcessMulticastDelegate(True)
        # End
        # Label 404
        Base: Ptr[BP_MenuBase] = Cast[BP_MenuBase](self.mPreviousWidget)
        bSuccess: bool = Base
        if not bSuccess:
            goto('L259')
        ReturnValue_2: bool = Not_PreBool(Base.UsesSubmenuBackground)
        self.PlayBackgroundAnim = ReturnValue_2
        goto('L270')
        ReturnValue_3: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.HideSwitcher, 0, 1, 0, 1)
        self.OnWidgetSet.ProcessMulticastDelegate(False)
        # End
        # Label 629
        self.SetRenderOpacity(1)
        ReturnValue1: bool = Default__KismetSystemLibrary.IsValid(self.mSwitcherWidget)
        if not ReturnValue1:
            goto('L822')
        Base1: Ptr[BP_MenuBase] = Cast[BP_MenuBase](Widget)
        bSuccess1: bool = Base1
        if not bSuccess1:
            goto('L315')
        goto('L404')
        # Label 793
        self.StopAnimation(self.HideSwitcher)
        goto('L629')
        goto('L793')
    

    def OnWidgetSet__DelegateSignature(self, mHasChangedActiveWidget: bool):
        pass
    
