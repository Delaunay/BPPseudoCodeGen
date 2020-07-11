
from codegen.ue4_stub import *

from Script.UMG import SetBackgroundColor
from Script.UMG import GetParent
from Script.Engine import Texture
from Script.UMG import CanvasPanelSlot
from Game.FactoryGame.Interface.UI.InGame.-Shared.Widget_SlidingTabs_Button import ExecuteUbergraph_Widget_SlidingTabs_Button
from Script.Engine import Delay
from Script.UMG import SetPadding
from Script.UMG import GetChildIndex
from Script.UMG import OverlaySlot
from Script.UMG import Default__WidgetLayoutLibrary
from Script.UMG import SlotAsCanvasSlot
from Script.UMG import SlotAsOverlaySlot
from Script.UMG import SetZOrder
from Script.Engine import Not_PreBool
from Script.Engine import LatentActionInfo
from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import Default__KismetArrayLibrary
from Script.UMG import SetRenderTranslation
from Script.UMG import ESlateVisibility
from Script.UMG import HasChild
from Script.Engine import IsValid
from Script.UMG import SetColorAndOpacity
from Script.Engine import EqualEqual_IntInt
from Game.FactoryGame.Interface.UI.InGame.-Shared.Widget_SlidingTabs import Widget_SlidingTabs
from Script.UMG import CanvasPanel
from Script.UMG import Widget
from Script.UMG import PanelWidget
from Script.UMG import UserWidget
from Game.FactoryGame.Interface.UI.InGame.-Shared.Widget_SlidingTabs_Button import ExecuteUbergraph_Widget_SlidingTabs_Button.K2Node_Event_IsDesignTime
from Script.CoreUObject import Vector2D
from Script.SlateCore import SlateColor
from Script.UMG import SetStyle
from Script.CoreUObject import LinearColor

class Widget_SlidingTabs_Button(UserWidget):
    OnClicked: FMulticastScriptDelegate
    mTargetWidget: Ptr[Widget]
    mSlidingTabsWidget: Ptr[Widget_SlidingTabs]
    mIcon: Ptr[Texture]
    mTitle: FText = NSLOCTEXT("", "50B082804314BD6AB4D2C7A72EB53A02", "Title")
    TextNormalColor: SlateColor = Namespace(ColorUseRule=0, SpecifiedColor={'R': 1, 'G': 1, 'B': 1, 'A': 1})
    mTargetIndex: int32
    OnHovered: FMulticastScriptDelegate
    OnUnhovered: FMulticastScriptDelegate
    IsActive: bool
    mOverrideButtonFunction: bool
    IsBackgroundVisible: bool
    
    def SetBackgroundVisibility(self, visible: bool):
        self.IsBackgroundVisible = visible
        Variable2: LinearColor = LinearColor(R = 1, G = 1, B = 1, A = 1)
        Variable3: LinearColor = LinearColor(R = 0, G = 0, B = 0, A = 0)
        Variable3_0: bool = self.IsBackgroundVisible
        
        switch = {
            False: Variable3,
            True: Variable2
        }
        self.mButton.SetBackgroundColor(switch.get(Variable3_0, None))
        Variable: uint8 = 3
        Variable1: uint8 = 1
        Variable2_0: bool = self.IsBackgroundVisible
        
        switch_0 = {
            False: Variable1,
            True: Variable
        }
        self.mShadows.SetVisibility(switch_0.get(Variable2_0, None))
        Variable_0: Vector2D = Vector2D(X = 0, Y = 0)
        Variable1_0: Vector2D = Vector2D(X = 0, Y = -3)
        Variable1_1: bool = self.IsBackgroundVisible
        
        switch_1 = {
            False: Variable1_0,
            True: Variable_0
        }
        self.SetRenderTranslation(switch_1.get(Variable1_1, None))
        Margin.Left = 7
        Margin.Top = 0
        Margin.Right = 7
        Margin.Bottom = 0
        Margin1.Left = 12
        Margin1.Top = 0
        Margin1.Right = 12
        Margin1.Bottom = 0
        Variable_1: bool = self.IsBackgroundVisible
        ReturnValue: Ptr[OverlaySlot] = Default__WidgetLayoutLibrary.SlotAsOverlaySlot(self.mContent)
        
        switch_2 = {
            False: Margin,
            True: Margin1
        }
        ReturnValue.SetPadding(switch_2.get(Variable_1, None))
    

    def SetIcon(self, Texture: Const[Ptr[Texture]]):
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(Texture)
        if not ReturnValue:
            goto('L602')
        self.mIcon = Texture
        SlateBrush.ImageSize = self.mIconObject.Brush.ImageSize
        SlateBrush.Margin = self.mIconObject.Brush.Margin
        SlateBrush.TintColor = self.mIconObject.Brush.TintColor
        SlateBrush.ResourceObject = self.mIcon
        SlateBrush.DrawAs = self.mIconObject.Brush.DrawAs
        SlateBrush.Tiling = self.mIconObject.Brush.Tiling
        SlateBrush.Mirroring = self.mIconObject.Brush.Mirroring
        
        SlateBrush = None
        self.mIconObject.SetBrush(Ref[SlateBrush])
        self.mIconContainer.SetVisibility(3)
        # End
        # Label 602
        self.mIconContainer.SetVisibility(1)
    

    def SetTitle(self, mTitle: FText):
        self.mTitle = mTitle
        self.mTitleObject.SetText(self.mTitle)
    

    def SetActive(self, IsActive: bool):
        self.IsActive = IsActive
        Variable2: LinearColor = LinearColor(R = 0.09530699998140335, G = 0.09530699998140335, B = 0.09530699998140335, A = 1)
        Variable3: LinearColor = LinearColor(R = 0.1875, G = 0.1875, B = 0.1875, A = 1)
        Variable2_0: bool = self.IsActive
        
        switch = {
            False: Variable3,
            True: Variable2
        }
        SlateColor2.SpecifiedColor = switch.get(Variable2_0, None)
        SlateColor2.ColorUseRule = 0
        SlateBrush.ImageSize = self.mButton.WidgetStyle.Normal.ImageSize
        SlateBrush.Margin = self.mButton.WidgetStyle.Normal.Margin
        SlateBrush.TintColor = SlateColor2
        SlateBrush.ResourceObject = self.mButton.WidgetStyle.Normal.ResourceObject
        SlateBrush.DrawAs = self.mButton.WidgetStyle.Normal.DrawAs
        SlateBrush.Tiling = self.mButton.WidgetStyle.Normal.Tiling
        SlateBrush.Mirroring = self.mButton.WidgetStyle.Normal.Mirroring
        ButtonStyle.Normal = SlateBrush
        ButtonStyle.Hovered = self.mButton.WidgetStyle.Hovered
        ButtonStyle.Pressed = self.mButton.WidgetStyle.Pressed
        ButtonStyle.Disabled = self.mButton.WidgetStyle.Disabled
        ButtonStyle.NormalPadding = self.mButton.WidgetStyle.NormalPadding
        ButtonStyle.PressedPadding = self.mButton.WidgetStyle.PressedPadding
        ButtonStyle.PressedSlateSound = self.mButton.WidgetStyle.PressedSlateSound
        ButtonStyle.HoveredSlateSound = self.mButton.WidgetStyle.HoveredSlateSound
        
        ButtonStyle = None
        self.mButton.SetStyle(Ref[ButtonStyle])
        Variable: LinearColor = LinearColor(R = 1, G = 1, B = 1, A = 1)
        Variable1: LinearColor = LinearColor(R = 1, G = 1, B = 1, A = 1)
        Variable1_0: bool = self.IsActive
        
        switch_0 = {
            False: Variable1,
            True: Variable
        }
        SlateColor1.SpecifiedColor = switch_0.get(Variable1_0, None)
        SlateColor1.ColorUseRule = 0
        self.TextNormalColor = SlateColor1
        SlateColor.SpecifiedColor = LinearColor(R = 1, G = 1, B = 1, A = 1)
        SlateColor.ColorUseRule = 0
        ReturnValue: bool = self.IsHovered()
        Variable_0: bool = ReturnValue
        
        switch_1 = {
            False: self.TextNormalColor,
            True: SlateColor
        }
        self.mTitleObject.SetColorAndOpacity(switch_1.get(Variable_0, None))
        ReturnValue_0: Ptr[PanelWidget] = self.GetParent()
        Panel: Ptr[CanvasPanel] = Cast[CanvasPanel](ReturnValue_0)
        bSuccess: bool = Panel
        if not bSuccess:
            goto('L2120')
        Variable_1: int32 = 10
        Variable3_0: bool = self.IsActive
        ReturnValue_1: Ptr[CanvasPanelSlot] = Default__WidgetLayoutLibrary.SlotAsCanvasSlot(self)
        ReturnValue_2: int32 = Panel.GetChildIndex(self)
        ReturnValue_3: int32 = ReturnValue_2 * -1
        
        switch_2 = {
            False: ReturnValue_3,
            True: Variable_1
        }
        ReturnValue_1.SetZOrder(switch_2.get(Variable3_0, None))
        # Label 2120
        if not self.IsActive:
            goto('L2153')
        self.StartAutoScroll()
        # End
        # Label 2153
        self.Widget_AutoScrollingContainer.StopAutoScroll()
    

    def BndEvt__Button_0_K2Node_ComponentBoundEvent_0_OnButtonClickedEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_SlidingTabs_Button(901)
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_SlidingTabs_Button(906)
    

    def PreConstruct(self):
        ExecuteUbergraph_Widget_SlidingTabs_Button.K2Node_Event_IsDesignTime = IsDesignTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_SlidingTabs_Button(911)
    

    def BndEvt__mButton_K2Node_ComponentBoundEvent_1_OnButtonHoverEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_SlidingTabs_Button(958)
    

    def BndEvt__mButton_K2Node_ComponentBoundEvent_2_OnButtonHoverEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_SlidingTabs_Button(1110)
    

    def StartAutoScroll(self):
        self.ExecuteUbergraph_Widget_SlidingTabs_Button(1172)
    

    def ExecuteUbergraph_Widget_SlidingTabs_Button(self):
        goto(ComputedJump("EntryPoint"))
        ReturnValue2: bool = Default__KismetSystemLibrary.IsValid(self.mSlidingTabsWidget)
        if not ReturnValue2:
            goto('L187')
        ReturnValue: bool = EqualEqual_IntInt(self.mTargetIndex, self.mSlidingTabsWidget.mActiveIndex)
        if not ReturnValue:
           goto(ExecutionFlow.Pop())
        self.Widget_AutoScrollingContainer.StartAutoScroll()
        goto(ExecutionFlow.Pop())
        # Label 187
        self.Widget_AutoScrollingContainer.StartAutoScroll()
        goto(ExecutionFlow.Pop())
        # Label 224
        ReturnValue_0: bool = Not_PreBool(self.IsActive)
        if not ReturnValue_0:
           goto(ExecutionFlow.Pop())
        ReturnValue1: bool = Not_PreBool(self.mOverrideButtonFunction)
        if not ReturnValue1:
            goto('L685')
        ReturnValue_1: bool = Default__KismetSystemLibrary.IsValid(self.mSlidingTabsWidget)
        if not ReturnValue_1:
           goto(ExecutionFlow.Pop())
        ReturnValue3: bool = Default__KismetSystemLibrary.IsValid(self.mSlidingTabsWidget.mHorizontalBox)
        if not ReturnValue3:
           goto(ExecutionFlow.Pop())
        ReturnValue_2: bool = self.mSlidingTabsWidget.mHorizontalBox.HasChild(self.mTargetWidget)
        if not ReturnValue_2:
            goto('L706')
        ReturnValue_3: int32 = self.mSlidingTabsWidget.mHorizontalBox.GetChildIndex(self.mTargetWidget)
        self.mSlidingTabsWidget.SetActiveIndex(ReturnValue_3, True)
        # Label 664
        self.OnClicked.ProcessMulticastDelegate(self)
        goto(ExecutionFlow.Pop())
        # Label 685
        self.OnClicked.ProcessMulticastDelegate(self)
        goto(ExecutionFlow.Pop())
        # Label 706
        self.mSlidingTabsWidget.SetActiveIndex(self.mTargetIndex, True)
        goto('L664')
        # Label 757
        ReturnValue1_0: bool = Default__KismetSystemLibrary.IsValid(self.mSlidingTabsWidget)
        if not ReturnValue1_0:
           goto(ExecutionFlow.Pop())
        
        self.mSlidingTabsWidget.mButtons = None
        self = None
        ReturnValue_4: int32 = self.mSlidingTabsWidget.mButtons.append(self)
        goto(ExecutionFlow.Pop())
        goto('L224')
        goto('L757')
        self.SetTitle(self.mTitle)
        self.SetIcon(self.mIcon)
        goto(ExecutionFlow.Pop())
        SlateColor.SpecifiedColor = LinearColor(R = 1, G = 1, B = 1, A = 1)
        SlateColor.ColorUseRule = 0
        self.mTitleObject.SetColorAndOpacity(SlateColor)
        self.OnHovered.ProcessMulticastDelegate(self)
        goto(ExecutionFlow.Pop())
        self.mTitleObject.SetColorAndOpacity(self.TextNormalColor)
        self.OnUnhovered.ProcessMulticastDelegate(self)
        goto(ExecutionFlow.Pop())
        Default__KismetSystemLibrary.Delay(self, 0.10000000149011612, LatentActionInfo(Linkage = 15, UUID = 1598510957, ExecutionFunction = "ExecuteUbergraph_Widget_SlidingTabs_Button", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
    

    def OnUnhovered__DelegateSignature(self, Instigator: Ptr[Widget_SlidingTabs_Button]):
        pass
    

    def OnHovered__DelegateSignature(self, Instigator: Ptr[Widget_SlidingTabs_Button]):
        pass
    

    def OnClicked__DelegateSignature(self, Instigator: Ptr[Widget_SlidingTabs_Button]):
        pass
    
