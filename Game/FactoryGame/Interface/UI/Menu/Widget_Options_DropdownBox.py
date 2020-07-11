
from codegen.ue4_stub import *

from Script.UMG import GetOptionCount
from Game.FactoryGame.Interface.UI.Menu.Widget_Options_DropdownBox import ExecuteUbergraph_Widget_Options_DropdownBox.K2Node_Event_IsDesignTime
from Script.Engine import PlayerController
from Script.AkAudio import PostAkEvent
from Script.Engine import Default__KismetArrayLibrary
from Game.FactoryGame.Interface.UI.Menu.Widget_Options_DropdownBox import ExecuteUbergraph_Widget_Options_DropdownBox.K2Node_ComponentBoundEvent_SelectedItem
from Game.FactoryGame.Interface.UI.Menu.Widget_OptionValueController import Widget_OptionValueController
from Game.FactoryGame.Interface.UI.Audio.MainMenu.Play_UI_MainMenu_MouseOver import Play_UI_MainMenu_MouseOver
from Script.UMG import SetColorAndOpacity
from Game.FactoryGame.Interface.UI.Menu.Widget_Options_DropdownBox import ExecuteUbergraph_Widget_Options_DropdownBox.K2Node_ComponentBoundEvent_SelectionType
from Script.UMG import AddOption
from Script.Engine import GreaterEqual_IntInt
from Game.FactoryGame.Interface.UI.Menu.Widget_Options_DropdownBox import ExecuteUbergraph_Widget_Options_DropdownBox
from Script.AkAudio import AkComponent
from Game.FactoryGame.Interface.UI.Audio.MainMenu.Play_UI_MainMenu_DialBoxDropDown import Play_UI_MainMenu_DialBoxDropDown
from Script.AkAudio import Default__AkGameplayStatics
from Script.UMG import SetSelectedOption
from Script.UMG import ClearOptions

class Widget_Options_DropdownBox(Widget_OptionValueController):
    OnSelectionChanged: FMulticastScriptDelegate
    mOptions: List[FString]
    mDefaultSelectedIndex: int32
    
    def SetDropdownColor(self, Color: LinearColor):
        LocalColor = Color
        SlateColor.SpecifiedColor = LocalColor
        SlateColor.ColorUseRule = self.mDropdownBox.WidgetStyle.ComboButtonStyle.ButtonStyle.Normal.TintColor.ColorUseRule
        SlateColor1.SpecifiedColor = LocalColor
        SlateColor1.ColorUseRule = self.mDropdownBox.WidgetStyle.ComboButtonStyle.ButtonStyle.Pressed.TintColor.ColorUseRule
        SlateBrush.ImageSize = self.mDropdownBox.WidgetStyle.ComboButtonStyle.ButtonStyle.Normal.ImageSize
        SlateBrush.Margin = self.mDropdownBox.WidgetStyle.ComboButtonStyle.ButtonStyle.Normal.Margin
        SlateBrush.TintColor = SlateColor
        SlateBrush.ResourceObject = self.mDropdownBox.WidgetStyle.ComboButtonStyle.ButtonStyle.Normal.ResourceObject
        SlateBrush.DrawAs = self.mDropdownBox.WidgetStyle.ComboButtonStyle.ButtonStyle.Normal.DrawAs
        SlateBrush.Tiling = self.mDropdownBox.WidgetStyle.ComboButtonStyle.ButtonStyle.Normal.Tiling
        SlateBrush.Mirroring = self.mDropdownBox.WidgetStyle.ComboButtonStyle.ButtonStyle.Normal.Mirroring
        SlateBrush1.ImageSize = self.mDropdownBox.WidgetStyle.ComboButtonStyle.ButtonStyle.Pressed.ImageSize
        SlateBrush1.Margin = self.mDropdownBox.WidgetStyle.ComboButtonStyle.ButtonStyle.Pressed.Margin
        SlateBrush1.TintColor = SlateColor1
        SlateBrush1.ResourceObject = self.mDropdownBox.WidgetStyle.ComboButtonStyle.ButtonStyle.Pressed.ResourceObject
        SlateBrush1.DrawAs = self.mDropdownBox.WidgetStyle.ComboButtonStyle.ButtonStyle.Pressed.DrawAs
        SlateBrush1.Tiling = self.mDropdownBox.WidgetStyle.ComboButtonStyle.ButtonStyle.Pressed.Tiling
        SlateBrush1.Mirroring = self.mDropdownBox.WidgetStyle.ComboButtonStyle.ButtonStyle.Pressed.Mirroring
        SlateColor2.SpecifiedColor = LocalColor
        SlateColor2.ColorUseRule = self.mDropdownBox.WidgetStyle.ComboButtonStyle.ButtonStyle.Hovered.TintColor.ColorUseRule
        SlateBrush2.ImageSize = self.mDropdownBox.WidgetStyle.ComboButtonStyle.ButtonStyle.Hovered.ImageSize
        SlateBrush2.Margin = self.mDropdownBox.WidgetStyle.ComboButtonStyle.ButtonStyle.Hovered.Margin
        SlateBrush2.TintColor = SlateColor2
        SlateBrush2.ResourceObject = self.mDropdownBox.WidgetStyle.ComboButtonStyle.ButtonStyle.Hovered.ResourceObject
        SlateBrush2.DrawAs = self.mDropdownBox.WidgetStyle.ComboButtonStyle.ButtonStyle.Hovered.DrawAs
        SlateBrush2.Tiling = self.mDropdownBox.WidgetStyle.ComboButtonStyle.ButtonStyle.Hovered.Tiling
        SlateBrush2.Mirroring = self.mDropdownBox.WidgetStyle.ComboButtonStyle.ButtonStyle.Hovered.Mirroring
        ButtonStyle.Normal = SlateBrush
        ButtonStyle.Hovered = SlateBrush2
        ButtonStyle.Pressed = SlateBrush1
        ButtonStyle.Disabled = self.mDropdownBox.WidgetStyle.ComboButtonStyle.ButtonStyle.Disabled
        ButtonStyle.NormalPadding = self.mDropdownBox.WidgetStyle.ComboButtonStyle.ButtonStyle.NormalPadding
        ButtonStyle.PressedPadding = self.mDropdownBox.WidgetStyle.ComboButtonStyle.ButtonStyle.PressedPadding
        ButtonStyle.PressedSlateSound = self.mDropdownBox.WidgetStyle.ComboButtonStyle.ButtonStyle.PressedSlateSound
        ButtonStyle.HoveredSlateSound = self.mDropdownBox.WidgetStyle.ComboButtonStyle.ButtonStyle.HoveredSlateSound
        ComboButtonStyle.ButtonStyle = ButtonStyle
        ComboButtonStyle.DownArrowImage = self.mDropdownBox.WidgetStyle.ComboButtonStyle.DownArrowImage
        ComboButtonStyle.MenuBorderBrush = self.mDropdownBox.WidgetStyle.ComboButtonStyle.MenuBorderBrush
        ComboButtonStyle.MenuBorderPadding = self.mDropdownBox.WidgetStyle.ComboButtonStyle.MenuBorderPadding
        ComboBoxStyle.ComboButtonStyle = ComboButtonStyle
        ComboBoxStyle.PressedSlateSound = self.mDropdownBox.WidgetStyle.PressedSlateSound
        ComboBoxStyle.SelectionChangeSlateSound = self.mDropdownBox.WidgetStyle.SelectionChangeSlateSound
        self.mDropdownBox.WidgetStyle = ComboBoxStyle
    

    def IsValidIndex(self, index: int32):
        ReturnValue: bool = GreaterEqual_IntInt(index, 0)
        ReturnValue_0: int32 = self.mDropdownBox.GetOptionCount()
        ReturnValue_1: bool = index <= ReturnValue_0
        ReturnValue_2: bool = ReturnValue and ReturnValue_1
        Valid = ReturnValue_2
    

    def BndEvt__mDropDownButton_K2Node_ComponentBoundEvent_172_OnButtonClickedEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_Options_DropdownBox(455)
    

    def BndEvt__mDropdownBox_K2Node_ComponentBoundEvent_2_OnOpeningEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_Options_DropdownBox(570)
    

    def BndEvt__mFakeButton_K2Node_ComponentBoundEvent_3_OnButtonHoverEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_Options_DropdownBox(661)
    

    def BndEvt__mDropdownBox_K2Node_ComponentBoundEvent_0_OnSelectionChangedEvent__DelegateSignature(self, SelectedItem: FString, SelectionType: uint8):
        ExecuteUbergraph_Widget_Options_DropdownBox.K2Node_ComponentBoundEvent_SelectedItem = SelectedItem #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_Options_DropdownBox.K2Node_ComponentBoundEvent_SelectionType = SelectionType #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_Options_DropdownBox(666)
    

    def PreConstruct(self):
        ExecuteUbergraph_Widget_Options_DropdownBox.K2Node_Event_IsDesignTime = IsDesignTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_Options_DropdownBox(695)
    

    def OnRowHovered(self):
        self.ExecuteUbergraph_Widget_Options_DropdownBox(835)
    

    def OnRowUnhovered(self):
        self.ExecuteUbergraph_Widget_Options_DropdownBox(900)
    

    def ExecuteUbergraph_Widget_Options_DropdownBox(self):
        goto(ComputedJump("EntryPoint"))
        # Label 15
        ExecutionFlow.Push("L121")
        
        Item = None
        Item = self.mOptions[Variable]
        self.mDropdownBox.AddOption(Item)
        goto(ExecutionFlow.Pop())
        # Label 121
        ReturnValue: int32 = Variable + 1
        Variable: int32 = ReturnValue
        
        # Label 190
        ReturnValue1: int32 = len(self.mOptions)
        ReturnValue_0: bool = Variable <= ReturnValue1
        if not ReturnValue_0:
            goto('L333')
        Variable = Variable
        goto('L15')
        
        valid = None
        # Label 333
        self.IsValidIndex(self.mDefaultSelectedIndex, Ref[valid])
        if not valid:
           goto(ExecutionFlow.Pop())
        self.mDropdownBox.SetSelectedOption(self.mOptions[self.mDefaultSelectedIndex])
        goto(ExecutionFlow.Pop())
        # Label 427
        Variable = 0
        goto('L190')
        goto(ExecutionFlow.Pop())
        # Label 456
        ReturnValue_1: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_2: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_UI_MainMenu_DialBoxDropDown, ReturnValue_1, True)
        goto(ExecutionFlow.Pop())
        # Label 542
        Variable = 0
        goto('L427')
        goto('L456')
        # Label 575
        ReturnValue1_0: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue1_1: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_UI_MainMenu_MouseOver, ReturnValue1_0, True)
        goto(ExecutionFlow.Pop())
        goto('L575')
        self.OnSelectionChanged.ProcessMulticastDelegate(SelectedItem)
        goto(ExecutionFlow.Pop())
        self.mDropdownBox.ClearOptions()
        
        ReturnValue_3: int32 = len(self.mOptions)
        ReturnValue_4: bool = ReturnValue_3 > 0
        if not ReturnValue_4:
           goto(ExecutionFlow.Pop())
        goto('L542')
        self.SetDropdownColor(self.mHoveredColor)
        self.mCaret.SetColorAndOpacity(self.mHoveredColor)
        goto(ExecutionFlow.Pop())
        self.SetDropdownColor(self.mUnhoveredColor)
        self.mCaret.SetColorAndOpacity(self.mUnhoveredColor)
        goto(ExecutionFlow.Pop())
    

    def onSelectionChanged__DelegateSignature(self, SelectedOption: FString):
        pass
    
