
from codegen.ue4_stub import *

from Script.FactoryGame import ECompassViewDistance
from Script.Engine import Default__KismetNodeHelperLibrary
from Script.UMG import GetChildrenCount
from Script.Engine import GreaterEqual_IntInt
from Script.Engine import Conv_ByteToInt
from Script.Engine import LatentActionInfo
from Script.UMG import Button
from Script.Engine import Default__KismetSystemLibrary
from Script.UMG import GetChildAt
from Script.UMG import Unhandled
from Script.UMG import ESlateVisibility
from Script.Engine import IsValid
from Script.Engine import GetValidValue
from Script.UMG import Default__WidgetBlueprintLibrary
from Script.Engine import EqualEqual_IntInt
from Game.FactoryGame.Interface.UI.Minimap.MapFilters.Widget_BeaconViewdistanceSlider import ExecuteUbergraph_Widget_BeaconViewdistanceSlider.K2Node_Event_MouseEvent
from Script.Engine import BooleanOR
from Script.UMG import Widget
from Game.FactoryGame.Interface.UI.Minimap.MapFilters.Widget_BeaconViewdistanceSlider import ExecuteUbergraph_Widget_BeaconViewdistanceSlider
from Script.UMG import Overlay
from Script.Engine import Conv_IntToByte
from Script.Engine import RetriggerableDelay
from Script.UMG import UserWidget
from Script.Engine import RandomIntegerInRange
from Script.UMG import TextBlock
from Game.FactoryGame.Interface.UI.Minimap.MapFilters.Widget_BeaconViewdistanceSlider import ExecuteUbergraph_Widget_BeaconViewdistanceSlider.K2Node_Event_IsDesignTime
from Script.UMG import SetStyle
from Script.UMG import EventReply
from Script.CoreUObject import LinearColor

class Widget_BeaconViewdistanceSlider(UserWidget):
    mSelectedLevel: int32
    mHoveredLevel: int32
    mLastHoveredLevel: int32 = -1
    mCeline1: bool
    mName: FText
    mCompassViewDistance: uint8 = ECompassViewDistance::CVD_Mid
    OnViewDistanceChanged: FMulticastScriptDelegate
    OnHovered: FMulticastScriptDelegate
    OnUnhovered: FMulticastScriptDelegate
    OnViewDistanceHovered: FMulticastScriptDelegate
    OnViewDistanceUnhovered: FMulticastScriptDelegate
    
    def GetTextFromIndex(self, index: int32):
        ExecutionFlow.Push("L523")
        ReturnValue: Ptr[Widget] = self.mContainer.GetChildAt(index)
        AsOverlay: Ptr[Overlay] = Cast[Overlay](ReturnValue)
        bSuccess: bool = AsOverlay
        if not bSuccess:
           goto(ExecutionFlow.Pop())
        Variable: int32 = 0
        # Label 154
        ReturnValue_0: int32 = AsOverlay.GetChildrenCount()
        ReturnValue_1: bool = Variable <= ReturnValue_0
        if not ReturnValue_1:
            goto('L422')
        ExecutionFlow.Push("L449")
        ReturnValue1: Ptr[Widget] = AsOverlay.GetChildAt(Variable)
        AsText: Ptr[TextBlock] = Cast[TextBlock](ReturnValue1)
        bSuccess1: bool = AsText
        if not bSuccess1:
           goto(ExecutionFlow.Pop())
        text = AsText
        success = True
        # End
        # Label 422
        text = None
        success = False
        # End
        # Label 449
        ReturnValue_2: int32 = Variable + 1
        Variable = ReturnValue_2
        goto('L154')
    

    def OnMouseMove(self):
        ExecutionFlow.Push("L1415")
        self.mHoveredLevel = -1
        ReturnValue: bool = self.mContainer.IsHovered()
        if not ReturnValue:
            goto('L602')
        Variable: int32 = 0
        # Label 111
        ReturnValue_0: int32 = self.mContainer.GetChildrenCount()
        ReturnValue_1: bool = Variable <= ReturnValue_0
        if not ReturnValue_1:
            goto('L623')
        ExecutionFlow.Push("L839")
        ReturnValue_2: Ptr[Widget] = self.mContainer.GetChildAt(Variable)
        ReturnValue_3: bool = Default__KismetSystemLibrary.IsValid(ReturnValue_2)
        if not ReturnValue_3:
           goto(ExecutionFlow.Pop())
        ExecutionFlow.Push("L1192")
        ExecutionFlow.Push("L913")
        ReturnValue_2 = self.mContainer.GetChildAt(Variable)
        ReturnValue1: bool = ReturnValue_2.IsHovered()
        if not ReturnValue1:
           goto(ExecutionFlow.Pop())
        self.mHoveredLevel = Variable
        ReturnValue_4: bool = self.mHoveredLevel != self.mLastHoveredLevel
        if not ReturnValue_4:
           goto(ExecutionFlow.Pop())
        self.mLastHoveredLevel = self.mHoveredLevel
        self.MyMemesWillGoOn()
        self.mWhereever.SetVisibility(1)
        goto(ExecutionFlow.Pop())
        # Label 602
        self.OnViewDistanceUnhovered.ProcessMulticastDelegate(self)
        goto(ExecutionFlow.Pop())
        # Label 623
        ReturnValue_5: uint8 = Conv_IntToByte(self.mHoveredLevel)
        ReturnValue_6: uint8 = Default__KismetNodeHelperLibrary.GetValidValue(ECompassViewDistance, ReturnValue_5)
        self.OnViewDistanceHovered.ProcessMulticastDelegate(self, ReturnValue_6)
        ReturnValue_7: EventReply = Default__WidgetBlueprintLibrary.Unhandled()
        ReturnValue_8: EventReply = ReturnValue_7
        goto('L1415')
        # Label 839
        ReturnValue_9: int32 = Variable + 1
        Variable = ReturnValue_9
        goto('L111')
        
        Text = None
        Success = None
        # Label 913
        self.GetTextFromIndex(Variable, Ref[Text], Ref[Success])
        if not Success:
           goto(ExecutionFlow.Pop())
        ReturnValue_10: bool = EqualEqual_IntInt(Variable, self.mHoveredLevel)
        
        Text = None
        Success = None
        self.GetTextFromIndex(Variable, Ref[Text], Ref[Success])
        Variable_0: uint8 = 2
        Variable1: uint8 = 3
        Variable_1: bool = ReturnValue_10
        
        switch = {
            False: Variable_0,
            True: Variable1
        }
        Text.SetVisibility(switch.get(Variable_1, None))
        goto(ExecutionFlow.Pop())
        
        Button = None
        Success = None
        # Label 1192
        self.GetButtonFromIndex(Variable, Ref[Button], Ref[Success])
        ReturnValue_11: bool = GreaterEqual_IntInt(self.mHoveredLevel, Variable)
        ReturnValue_12: bool = self.mHoveredLevel <= 0
        ReturnValue_13: bool = BooleanOR(ReturnValue_12, ReturnValue_11)
        ReturnValue_14: bool = ReturnValue_13 and Success
        self.SetButtonStyle(Button, ReturnValue_14, True)
        goto(ExecutionFlow.Pop())
    

    def GetButtonFromIndex(self, index: int32):
        ExecutionFlow.Push("L523")
        ReturnValue: Ptr[Widget] = self.mContainer.GetChildAt(index)
        AsOverlay: Ptr[Overlay] = Cast[Overlay](ReturnValue)
        bSuccess: bool = AsOverlay
        if not bSuccess:
           goto(ExecutionFlow.Pop())
        Variable: int32 = 0
        # Label 154
        ReturnValue_0: int32 = AsOverlay.GetChildrenCount()
        ReturnValue_1: bool = Variable <= ReturnValue_0
        if not ReturnValue_1:
            goto('L422')
        ExecutionFlow.Push("L449")
        ReturnValue1: Ptr[Widget] = AsOverlay.GetChildAt(Variable)
        AsButton: Ptr[Button] = Cast[Button](ReturnValue1)
        bSuccess1: bool = AsButton
        if not bSuccess1:
           goto(ExecutionFlow.Pop())
        Button = AsButton
        success = True
        # End
        # Label 422
        Button = None
        success = False
        # End
        # Label 449
        ReturnValue_2: int32 = Variable + 1
        Variable = ReturnValue_2
        goto('L154')
    

    def SetButtonStyle(self, Button: Ptr[Button], Selected: bool, Hovered: bool):
        Variable: LinearColor = LinearColor(R = 0.7835379838943481, G = 0.2917709946632385, B = 0.05951099842786789, A = 1)
        Variable1: LinearColor = LinearColor(R = 0.09530699998140335, G = 0.09530699998140335, B = 0.09530699998140335, A = 1)
        Variable2: LinearColor = LinearColor(R = 0, G = 0, B = 0, A = 0)
        Variable_0: bool = Hovered
        Variable1_0: bool = Selected
        
        switch = {
            False: Variable1,
            True: Variable
        }
        
        switch_0 = {
            False: Variable2,
            True: switch.get(Variable_0, None)
        }
        SlateColor.SpecifiedColor = switch_0.get(Variable1_0, None)
        SlateColor.ColorUseRule = 0
        SlateBrush.ImageSize = Button.WidgetStyle.Normal.ImageSize
        SlateBrush.Margin = Button.WidgetStyle.Normal.Margin
        SlateBrush.TintColor = SlateColor
        SlateBrush.ResourceObject = Button.WidgetStyle.Normal.ResourceObject
        SlateBrush.DrawAs = Button.WidgetStyle.Normal.DrawAs
        SlateBrush.Tiling = Button.WidgetStyle.Normal.Tiling
        SlateBrush.Mirroring = Button.WidgetStyle.Normal.Mirroring
        SlateBrush1.ImageSize = Button.WidgetStyle.Hovered.ImageSize
        SlateBrush1.Margin = Button.WidgetStyle.Hovered.Margin
        SlateBrush1.TintColor = Button.WidgetStyle.Hovered.TintColor
        SlateBrush1.ResourceObject = Button.WidgetStyle.Hovered.ResourceObject
        SlateBrush1.DrawAs = Button.WidgetStyle.Hovered.DrawAs
        SlateBrush1.Tiling = Button.WidgetStyle.Hovered.Tiling
        SlateBrush1.Mirroring = Button.WidgetStyle.Hovered.Mirroring
        ButtonStyle.Normal = SlateBrush
        ButtonStyle.Hovered = SlateBrush1
        ButtonStyle.Pressed = Button.WidgetStyle.Pressed
        ButtonStyle.Disabled = Button.WidgetStyle.Disabled
        ButtonStyle.NormalPadding = Button.WidgetStyle.NormalPadding
        ButtonStyle.PressedPadding = Button.WidgetStyle.PressedPadding
        ButtonStyle.PressedSlateSound = Button.WidgetStyle.PressedSlateSound
        ButtonStyle.HoveredSlateSound = Button.WidgetStyle.HoveredSlateSound
        
        ButtonStyle = None
        Button.SetStyle(Ref[ButtonStyle])
    

    def OnMouseLeave(self):
        ExecuteUbergraph_Widget_BeaconViewdistanceSlider.K2Node_Event_MouseEvent = MouseEvent #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_BeaconViewdistanceSlider(1005)
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_BeaconViewdistanceSlider(1020)
    

    def OnButtonClicked(self):
        self.ExecuteUbergraph_Widget_BeaconViewdistanceSlider(1446)
    

    def MyMemesWillGoOn(self):
        self.ExecuteUbergraph_Widget_BeaconViewdistanceSlider(1636)
    

    def PreConstruct(self):
        ExecuteUbergraph_Widget_BeaconViewdistanceSlider.K2Node_Event_IsDesignTime = IsDesignTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_BeaconViewdistanceSlider(1713)
    

    def UpdateSelectedLevel(self):
        self.ExecuteUbergraph_Widget_BeaconViewdistanceSlider(1759)
    

    def BndEvt__Widget_FilterButton_Row_K2Node_ComponentBoundEvent_0_OnHovered__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_BeaconViewdistanceSlider(1764)
    

    def BndEvt__Widget_FilterButton_Row_K2Node_ComponentBoundEvent_1_OnUnhovered__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_BeaconViewdistanceSlider(1785)
    

    def ExecuteUbergraph_Widget_BeaconViewdistanceSlider(self):
        goto(ComputedJump("EntryPoint"))
        ReturnValue: bool = self.IsHovered()
        if not ReturnValue:
            goto('L113')
        ReturnValue1: bool = EqualEqual_IntInt(self.mLastHoveredLevel, 1)
        if not ReturnValue1:
            goto('L125')
        self.mCeline1 = True
        goto(ExecutionFlow.Pop())
        # Label 113
        self.mCeline1 = False
        goto(ExecutionFlow.Pop())
        # Label 125
        if not self.mCeline1:
            goto('L309')
        ReturnValue_0: bool = EqualEqual_IntInt(self.mLastHoveredLevel, 3)
        if not ReturnValue_0:
            goto('L309')
        self.mWhereever.SetVisibility(0)
        ReturnValue_1: int32 = RandomIntegerInRange(8, 10)
        self.Widget_GenericParticleSpawner.CreateParticles(ReturnValue_1)
        goto(ExecutionFlow.Pop())
        # Label 309
        self.mCeline1 = False
        self.mWhereever.SetVisibility(1)
        goto(ExecutionFlow.Pop())
        # Label 359
        self.OnViewDistanceUnhovered.ProcessMulticastDelegate(self)
        goto(ExecutionFlow.Pop())
        # Label 380
        ExecutionFlow.Push("L833")
        ReturnValue_2: Ptr[Widget] = self.mContainer.GetChildAt(Variable1)
        ReturnValue_3: bool = Default__KismetSystemLibrary.IsValid(ReturnValue_2)
        if not ReturnValue_3:
           goto(ExecutionFlow.Pop())
        
        Button1 = None
        Success1 = None
        self.GetButtonFromIndex(Variable1, Ref[Button1], Ref[Success1])
        if not Success1:
           goto(ExecutionFlow.Pop())
        
        Text = None
        Success = None
        self.GetTextFromIndex(Variable1, Ref[Text], Ref[Success])
        if not Success:
            goto('L682')
        
        Text = None
        Success = None
        self.GetTextFromIndex(Variable1, Ref[Text], Ref[Success])
        Text.SetVisibility(2)
        # Label 682
        ReturnValue_4: bool = Variable1 <= self.mSelectedLevel
        
        Button1 = None
        Success1 = None
        self.GetButtonFromIndex(Variable1, Ref[Button1], Ref[Success1])
        self.SetButtonStyle(Button1, ReturnValue_4, False)
        self.mWhereever.SetVisibility(1)
        goto(ExecutionFlow.Pop())
        # Label 833
        ReturnValue_5: int32 = Variable1 + 1
        Variable1: int32 = ReturnValue_5
        # Label 902
        ReturnValue1_0: int32 = self.mContainer.GetChildrenCount()
        ReturnValue1_1: bool = Variable1 <= ReturnValue1_0
        if not ReturnValue1_1:
           goto(ExecutionFlow.Pop())
        goto('L380')
        self.UpdateSelectedLevel()
        goto(ExecutionFlow.Pop())
        ReturnValue_6: int32 = Conv_ByteToInt(self.mCompassViewDistance)
        self.mSelectedLevel = ReturnValue_6
        self.UpdateSelectedLevel()
        Variable: int32 = 0
        # Label 1121
        ReturnValue_7: int32 = self.mContainer.GetChildrenCount()
        ReturnValue_8: int32 = ReturnValue_7 - 1
        ReturnValue2: bool = Variable <= ReturnValue_8
        if not ReturnValue2:
           goto(ExecutionFlow.Pop())
        ExecutionFlow.Push("L1372")
        OutputDelegate.BindUFunction(self, OnButtonClicked)
        
        Button = None
        Success = None
        self.GetButtonFromIndex(Variable, Ref[Button], Ref[Success])
        Button.OnClicked.AddUnique(OutputDelegate)
        goto(ExecutionFlow.Pop())
        # Label 1372
        ReturnValue1_2: int32 = Variable + 1
        Variable = ReturnValue1_2
        goto('L1121')
        self.mSelectedLevel = self.mHoveredLevel
        ReturnValue_9: uint8 = Conv_IntToByte(self.mSelectedLevel)
        ReturnValue_10: uint8 = Default__KismetNodeHelperLibrary.GetValidValue(ECompassViewDistance, ReturnValue_9)
        self.OnViewDistanceChanged.ProcessMulticastDelegate(self, ReturnValue_10)
        goto(ExecutionFlow.Pop())
        # Label 1608
        Variable1 = 0
        goto('L902')
        Default__KismetSystemLibrary.RetriggerableDelay(self, 2, LatentActionInfo(Linkage = 15, UUID = 202746167, ExecutionFunction = "ExecuteUbergraph_Widget_BeaconViewdistanceSlider", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        self.Widget_FilterButton_Row.SetTitle(self.mName)
        goto(ExecutionFlow.Pop())
        goto('L1608')
        self.OnHovered.ProcessMulticastDelegate(self)
        goto(ExecutionFlow.Pop())
        self.OnUnhovered.ProcessMulticastDelegate(self)
        goto('L359')
    

    def OnViewDistanceUnhovered__DelegateSignature(self, Instigator: Ptr[Widget_BeaconViewdistanceSlider]):
        pass
    

    def OnViewDistanceHovered__DelegateSignature(self, Instigator: Ptr[Widget_BeaconViewdistanceSlider], viewDistance: uint8):
        pass
    

    def OnUnhovered__DelegateSignature(self, Instigator: Ptr[Widget_BeaconViewdistanceSlider]):
        pass
    

    def OnHovered__DelegateSignature(self, Instigator: Ptr[Widget_BeaconViewdistanceSlider]):
        pass
    

    def OnViewDistanceChanged__DelegateSignature(self, Instigator: Ptr[Widget_BeaconViewdistanceSlider], NewViewDistance: uint8):
        pass
    
