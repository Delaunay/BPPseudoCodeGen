
from codegen.ue4_stub import *

from Script.Engine import Delay
from Script.UMG import SetPadding
from Script.UMG import OverlaySlot
from Game.FactoryGame.Interface.UI.Menu.Widget_FrontEnd_Button import Widget_FrontEnd_Button
from Script.UMG import GetChildrenCount
from Game.FactoryGame.Interface.UI.InGame.-Shared.Widget_Scrollbox import Widget_Scrollbox
from Script.UMG import Default__WidgetLayoutLibrary
from Script.SlateCore import Margin
from Script.UMG import SlotAsOverlaySlot
from Script.Engine import LatentActionInfo
from Script.Engine import Default__KismetSystemLibrary
from Script.UMG import GetChildAt
from Script.Engine import Default__KismetArrayLibrary
from Script.UMG import PlayAnimation
from Script.UMG import ESlateVisibility
from Script.Engine import IsValid
from Game.FactoryGame.Interface.UI.Menu.Widget_SubMenuBackground import ExecuteUbergraph_Widget_SubMenuBackground.K2Node_Event_IsDesignTime
from Script.UMG import Widget
from Script.UMG import PanelWidget
from Script.UMG import WidgetAnimation
from Script.UMG import UserWidget
from Script.UMG import UMGSequencePlayer
from Script.UMG import HasAnyChildren
from Game.FactoryGame.Interface.UI.Menu.Widget_SubMenuBackground import ExecuteUbergraph_Widget_SubMenuBackground
from Game.FactoryGame.Interface.UI.Menu.Widget_SubMenuBackground import ExecuteUbergraph_Widget_SubMenuBackground.K2Node_CustomEvent_OverwritePanelWIdget
from Script.UMG import SetRenderOpacity
from Script.Engine import Array_Clear

class Widget_SubMenuBackground(UserWidget):
    ListItemSpawn: Ptr[WidgetAnimation]
    SpawnAnim: Ptr[WidgetAnimation]
    mShowBackground: bool = True
    mContentPadding: Margin = Namespace(Bottom=0, Left=0, Right=0, Top=150)
    mListItems: List[Ptr[UserWidget]]
    
    def OnSpawnAnim(self, OverwritePanelWIdget: Ptr[PanelWidget]):
        ExecutionFlow.Push("L1387")
        
        Default__KismetArrayLibrary.Array_Clear(Ref[self.mListItems])
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(OverwritePanelWIdget)
        if not ReturnValue:
            goto('L492')
        LocalPanelWidget = OverwritePanelWIdget
        # Label 130
        Variable: int32 = 0
        # Label 153
        ReturnValue_0: int32 = LocalPanelWidget.GetChildrenCount()
        ReturnValue_1: bool = Variable <= ReturnValue_0
        if not ReturnValue_1:
            goto('L1298')
        ExecutionFlow.Push("L1313")
        ReturnValue_2: Ptr[Widget] = LocalPanelWidget.GetChildAt(Variable)
        Widget: Ptr[UserWidget] = Cast[UserWidget](ReturnValue_2)
        bSuccess: bool = Widget
        if not bSuccess:
           goto(ExecutionFlow.Pop())
        Widget.SetRenderOpacity(0)
        
        ReturnValue_3: int32 = self.mListItems.append(Widget)
        goto(ExecutionFlow.Pop())
        # Label 492
        ReturnValue1: bool = self.mContent.HasAnyChildren()
        if not ReturnValue1:
           goto(ExecutionFlow.Pop())
        ReturnValue2: Ptr[Widget] = self.mContent.GetChildAt(0)
        Widget_0: Ptr[PanelWidget] = Cast[PanelWidget](ReturnValue2)
        bSuccess3: bool = Widget_0
        if not bSuccess3:
            goto('L694')
        LocalPanelWidget = Widget_0
        # Label 689
        goto('L130')
        # Label 694
        ReturnValue2 = self.mContent.GetChildAt(0)
        Scrollbox: Ptr[Widget_Scrollbox] = Cast[Widget_Scrollbox](ReturnValue2)
        bSuccess2: bool = Scrollbox
        if not bSuccess2:
            goto('L1070')
        ReturnValue_4: bool = Scrollbox.mScrollableContent.HasAnyChildren()
        if not ReturnValue_4:
            goto('L1070')
        ReturnValue3: Ptr[Widget] = Scrollbox.mScrollableContent.GetChildAt(0)
        Widget1: Ptr[PanelWidget] = Cast[PanelWidget](ReturnValue3)
        bSuccess4: bool = Widget1
        if not bSuccess4:
            goto('L1070')
        LocalPanelWidget = Widget1
        goto('L130')
        # Label 1070
        ReturnValue1_0: Ptr[Widget] = self.mContent.GetChildAt(0)
        Widget1_0: Ptr[UserWidget] = Cast[UserWidget](ReturnValue1_0)
        bSuccess1: bool = Widget1_0
        if not bSuccess1:
           goto(ExecutionFlow.Pop())
        Widget1_0.SetRenderOpacity(0)
        ReturnValue_5: Ptr[UMGSequencePlayer] = Widget1_0.PlayAnimation(self.ListItemSpawn, 0, 1, 0, 1)
        goto(ExecutionFlow.Pop())
        # Label 1298
        self.OnListSpawnAnim()
        goto(ExecutionFlow.Pop())
        # Label 1313
        ReturnValue_6: int32 = Variable + 1
        Variable = ReturnValue_6
        goto('L153')
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_SubMenuBackground(879)
    

    def PlayListSpawnAnim(self, OverwritePanelWIdget: Ptr[PanelWidget]):
        ExecuteUbergraph_Widget_SubMenuBackground.K2Node_CustomEvent_OverwritePanelWIdget = OverwritePanelWIdget #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_SubMenuBackground(1176)
    

    def PreConstruct(self):
        ExecuteUbergraph_Widget_SubMenuBackground.K2Node_Event_IsDesignTime = IsDesignTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_SubMenuBackground(1251)
    

    def OnListSpawnAnim(self):
        self.ExecuteUbergraph_Widget_SubMenuBackground(1344)
    

    def PlayBackgroundSpawnAnim(self):
        self.ExecuteUbergraph_Widget_SubMenuBackground(1372)
    

    def ExecuteUbergraph_Widget_SubMenuBackground(self):
        goto(ComputedJump("EntryPoint"))
        ExecutionFlow.Push("L148")
        
        Item = None
        Item = self.mListItems[Variable]
        ReturnValue1: Ptr[UMGSequencePlayer] = Item.PlayAnimation(self.ListItemSpawn, 0, 1, 0, 1)
        goto(ExecutionFlow.Pop())
        # Label 148
        ReturnValue1_0: int32 = Variable + 1
        Variable: int32 = ReturnValue1_0
        
        # Label 217
        ReturnValue: int32 = len(self.mListItems)
        ReturnValue_0: int32 = ReturnValue - 1
        ReturnValue_1: bool = Variable <= ReturnValue_0
        if not ReturnValue_1:
           goto(ExecutionFlow.Pop())
        Default__KismetSystemLibrary.Delay(self, 0.05000000074505806, LatentActionInfo(Linkage = 15, UUID = -962210269, ExecutionFunction = "ExecuteUbergraph_Widget_SubMenuBackground", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        # Label 443
        ExecutionFlow.Push("L620")
        
        Item1 = None
        Item1 = self.mListItems[Variable_0]
        Button: Ptr[Widget_FrontEnd_Button] = Cast[Widget_FrontEnd_Button](Item1)
        bSuccess: bool = Button
        if not bSuccess:
           goto(ExecutionFlow.Pop())
        Button.SetSelected(False)
        goto(ExecutionFlow.Pop())
        # Label 620
        ReturnValue_2: int32 = Variable_0 + 1
        Variable_0: int32 = ReturnValue_2
        
        # Label 689
        ReturnValue1_1: int32 = len(self.mListItems)
        ReturnValue_3: bool = Variable_0 <= ReturnValue1_1
        if not ReturnValue_3:
           goto(ExecutionFlow.Pop())
        Variable_0 = Variable_0
        goto('L443')
        # Label 828
        Variable_0 = 0
        Variable_0 = 0
        goto('L689')
        Variable_1: uint8 = 0
        Variable1: uint8 = 2
        Variable1_0: bool = self.mShowBackground
        
        switch = {
            False: Variable1,
            True: Variable_1
        }
        self.mBackgroundContainer.SetVisibility(switch.get(Variable1_0, None))
        Variable2: uint8 = 3
        Variable3: uint8 = 2
        Variable_2: bool = self.mShowBackground
        
        switch_0 = {
            False: Variable3,
            True: Variable2
        }
        self.mGradientContainer.SetVisibility(switch_0.get(Variable_2, None))
        goto(ExecutionFlow.Pop())
        self.OnSpawnAnim(OverwritePanelWIdget)
        goto('L828')
        # Label 1204
        ReturnValue_4: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.SpawnAnim, 0, 1, 0, 1)
        goto(ExecutionFlow.Pop())
        ReturnValue_5: Ptr[OverlaySlot] = Default__WidgetLayoutLibrary.SlotAsOverlaySlot(self.mContent)
        ReturnValue_5.SetPadding(self.mContentPadding)
        goto(ExecutionFlow.Pop())
        Variable = 0
        goto('L217')
        goto('L1204')
    
