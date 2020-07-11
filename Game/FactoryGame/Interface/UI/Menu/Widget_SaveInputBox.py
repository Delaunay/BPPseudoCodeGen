
from codegen.ue4_stub import *

from Script.Engine import Default__KismetSystemLibrary
from Script.UMG import SetUserFocus
from Script.Engine import PlayerController
from Game.FactoryGame.Interface.UI.Menu.Widget_SaveInputBox import ExecuteUbergraph_Widget_SaveInputBox
from Script.CoreUObject import LinearColor
from Script.Engine import K2_SetTimerDelegate
from Script.Engine import TimerHandle
from Script.UMG import SetStyle
from Game.FactoryGame.Interface.UI.Menu.Widget_SaveInputBox import ExecuteUbergraph_Widget_SaveInputBox.K2Node_ComponentBoundEvent_Text
from Game.FactoryGame.Interface.UI.Menu.Widget_SaveInputBox import ExecuteUbergraph_Widget_SaveInputBox.K2Node_ComponentBoundEvent_Text1
from Script.Engine import K2_ClearAndInvalidateTimerHandle
from Script.UMG import HasUserFocusedDescendants
from Script.UMG import UserWidget
from Game.FactoryGame.Interface.UI.Menu.Widget_SaveInputBox import ExecuteUbergraph_Widget_SaveInputBox.K2Node_ComponentBoundEvent_CommitMethod

class Widget_SaveInputBox(UserWidget):
    OnTextChanged: FMulticastScriptDelegate
    OnTextCommited: FMulticastScriptDelegate
    mFocusCheckerTimerHandle: TimerHandle
    OnFocused: FMulticastScriptDelegate
    OnUnfocused: FMulticastScriptDelegate
    
    def SetButtonColor(self, Color: SlateColor):
        SlateBrush.ImageSize = self.Button_0.WidgetStyle.Normal.ImageSize
        SlateBrush.Margin = self.Button_0.WidgetStyle.Normal.Margin
        SlateBrush.TintColor = Color
        SlateBrush.ResourceObject = self.Button_0.WidgetStyle.Normal.ResourceObject
        SlateBrush.DrawAs = self.Button_0.WidgetStyle.Normal.DrawAs
        SlateBrush.Tiling = self.Button_0.WidgetStyle.Normal.Tiling
        SlateBrush.Mirroring = self.Button_0.WidgetStyle.Normal.Mirroring
        ButtonStyle.Normal = SlateBrush
        ButtonStyle.Hovered = self.Button_0.WidgetStyle.Hovered
        ButtonStyle.Pressed = self.Button_0.WidgetStyle.Pressed
        ButtonStyle.Disabled = self.Button_0.WidgetStyle.Disabled
        ButtonStyle.NormalPadding = self.Button_0.WidgetStyle.NormalPadding
        ButtonStyle.PressedPadding = self.Button_0.WidgetStyle.PressedPadding
        ButtonStyle.PressedSlateSound = self.Button_0.WidgetStyle.PressedSlateSound
        ButtonStyle.HoveredSlateSound = self.Button_0.WidgetStyle.HoveredSlateSound
        
        ButtonStyle = None
        self.Button_0.SetStyle(Ref[ButtonStyle])
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_SaveInputBox(470)
    

    def BndEvt__Button_0_K2Node_ComponentBoundEvent_0_OnButtonClickedEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_SaveInputBox(590)
    

    def BndEvt__mSaveInputBox_K2Node_ComponentBoundEvent_1_OnEditableTextBoxChangedEvent__DelegateSignature(self, text: Const[Ref[FText]]):
        ExecuteUbergraph_Widget_SaveInputBox.K2Node_ComponentBoundEvent_Text1 = text #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_SaveInputBox(660)
    

    def BndEvt__mSaveInputBox_K2Node_ComponentBoundEvent_2_OnEditableTextBoxCommittedEvent__DelegateSignature(self, text: Const[Ref[FText]], CommitMethod: uint8):
        ExecuteUbergraph_Widget_SaveInputBox.K2Node_ComponentBoundEvent_Text = text #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_SaveInputBox.K2Node_ComponentBoundEvent_CommitMethod = CommitMethod #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_SaveInputBox(693)
    

    def CheckUserFocus(self):
        self.ExecuteUbergraph_Widget_SaveInputBox(735)
    

    def Destruct(self):
        self.ExecuteUbergraph_Widget_SaveInputBox(740)
    

    def ExecuteUbergraph_Widget_SaveInputBox(self):
        # Label 10
        self.OnFocused.ProcessMulticastDelegate()
        # End
        # Label 34
        Variable: bool = False
        SlateColor.SpecifiedColor = LinearColor(R = 0.09530699998140335, G = 0.09530699998140335, B = 0.09530699998140335, A = 1)
        SlateColor.ColorUseRule = 0
        self.SetButtonColor(SlateColor)
        goto('L10')
        # Label 163
        if not Variable:
            goto('L182')
        # End
        # Label 182
        Variable = True
        SlateColor1.SpecifiedColor = LinearColor(R = 0, G = 0, B = 0, A = 0)
        SlateColor1.ColorUseRule = 0
        self.SetButtonColor(SlateColor1)
        self.OnUnfocused.ProcessMulticastDelegate()
        # End
        # Label 330
        ReturnValue1: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue: bool = self.mSaveInputBox.HasUserFocusedDescendants(ReturnValue1)
        if not ReturnValue:
            goto('L438')
        if not Variable1:
            goto('L454')
        # End
        # Label 438
        Variable1: bool = False
        goto('L163')
        # Label 454
        Variable1 = True
        goto('L34')
        OutputDelegate.BindUFunction(self, CheckUserFocus)
        ReturnValue_0: TimerHandle = Default__KismetSystemLibrary.K2_SetTimerDelegate(OutputDelegate, 0.10000000149011612, True)
        self.mFocusCheckerTimerHandle = ReturnValue_0
        # End
        ReturnValue_1: Ptr[PlayerController] = self.GetOwningPlayer()
        self.mSaveInputBox.SetUserFocus(ReturnValue_1)
        # End
        self.OnTextChanged.ProcessMulticastDelegate(Text1)
        # End
        self.OnTextCommited.ProcessMulticastDelegate(Text, CommitMethod)
        # End
        goto('L330')
        
        Default__KismetSystemLibrary.K2_ClearAndInvalidateTimerHandle(self, Ref[self.mFocusCheckerTimerHandle])
    

    def OnUnfocused__DelegateSignature(self):
        pass
    

    def OnFocused__DelegateSignature(self):
        pass
    

    def OnTextCommited__DelegateSignature(self, text: FText, CommitMethod: uint8):
        pass
    

    def OnTextChanged__DelegateSignature(self, text: FText):
        pass
    
