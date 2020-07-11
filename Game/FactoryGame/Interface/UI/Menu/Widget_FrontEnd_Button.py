
from codegen.ue4_stub import *

from Script.UMG import SetUserFocus
from Script.UMG import GetParent
from Script.UMG import SetKeyboardFocus
from Script.AkAudio import PostAkEvent
from Script.UMG import WidgetSwitcher
from Game.FactoryGame.Interface.UI.Menu.Widget_FrontEnd_Button import Widget_FrontEnd_Button
from Script.UMG import GetChildrenCount
from Script.Engine import Not_PreBool
from Game.FactoryGame.Interface.UI.Menu.Widget_MenuSwitcherContainer import Widget_MenuSwitcherContainer
from Script.Engine import Default__KismetSystemLibrary
from Game.FactoryGame.Interface.UI.Menu.Widget_FrontEnd_Button import ExecuteUbergraph_Widget_FrontEnd_Button.K2Node_Event_IsDesignTime
from Script.UMG import GetChildAt
from Script.Engine import PlayerController
from Script.UMG import Handled
from Game.FactoryGame.Interface.UI.Audio.MainMenu.Play_UI_MainMenu_MouseOver import Play_UI_MainMenu_MouseOver
from Script.Engine import IsValid
from Script.UMG import Default__WidgetBlueprintLibrary
from Script.UMG import SetBrushSize
from Game.FactoryGame.Interface.UI.Menu.Widget_FrontEnd_Button import ExecuteUbergraph_Widget_FrontEnd_Button
from Script.Engine import BooleanOR
from Script.UMG import Widget
from Script.UMG import PanelWidget
from Script.FactoryGame import FGButtonWidget
from Script.UMG import WidgetAnimation
from Script.UMG import SetFont
from Script.AkAudio import Default__AkGameplayStatics
from Script.Engine import NotEqual_ObjectObject
from Game.FactoryGame.Interface.UI.HUDHelpers.HUDHelpers import Default__HUDHelpers
from Game.FactoryGame.Interface.UI.Menu.Widget_FrontEnd_Button import ExecuteUbergraph_Widget_FrontEnd_Button.K2Node_CustomEvent_IsSelected
from Script.CoreUObject import Vector2D
from Script.SlateCore import SlateColor
from Script.UMG import SetStyle
from Script.AkAudio import AkComponent
from Script.UMG import EventReply
from Script.CoreUObject import LinearColor

class Widget_FrontEnd_Button(FGButtonWidget):
    ani_HideSaveName: Ptr[WidgetAnimation]
    ani_ShowSaveName: Ptr[WidgetAnimation]
    OnClicked: FMulticastScriptDelegate
    mDisplayName: FText = NSLOCTEXT("", "3FAF8E794A7B558F72717EAC45B94339", "Working as somewhat intended")
    IsFocused: bool
    isSelected: bool
    IsBigButton: bool
    FontSize: int32
    mMenuSwitcherContainer_DEPRECATED: Ptr[Widget_MenuSwitcherContainer]
    mSwitcherWidget: Ptr[WidgetSwitcher]
    mTargetWidget: Ptr[Widget]
    mParentList: Ptr[PanelWidget]
    mUseTransparentBackground: bool = True
    OnHovered: FMulticastScriptDelegate
    OnUnhovered: FMulticastScriptDelegate
    bIsFocusable = True
    
    def SetTitle(self, mDisplayName: FText):
        self.mDisplayName = mDisplayName
        self.Title.SetText(self.mDisplayName)
    

    def SetActiveWidgetInSwitcher(self):
        ReturnValue1: bool = Default__KismetSystemLibrary.IsValid(self.mTargetWidget)
        if not ReturnValue1:
            goto('L306')
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(self.mSwitcherWidget)
        if not ReturnValue:
            goto('L306')
        Variable: Ptr[Widget] = None
        Variable_0: bool = self.isSelected
        
        switch = {
            False: self.mTargetWidget,
            True: Variable
        }
        self.mSwitcherWidget.SetActiveWidget(switch.get(Variable_0, None))
        ReturnValue_0: bool = Not_PreBool(self.isSelected)
        self.SetSelected(ReturnValue_0)
        # End
    

    def ClearListOfSelections(self):
        ExecutionFlow.Push("L618")
        ReturnValue1: bool = Default__KismetSystemLibrary.IsValid(self.mParentList)
        if not ReturnValue1:
            goto('L419')
        LocalParent = self.mParentList
        # Label 89
        Variable: int32 = 0
        # Label 112
        ReturnValue: int32 = LocalParent.GetChildrenCount()
        ReturnValue_0: bool = Variable <= ReturnValue
        if not ReturnValue_0:
           goto(ExecutionFlow.Pop())
        ExecutionFlow.Push("L544")
        ReturnValue_1: Ptr[Widget] = LocalParent.GetChildAt(Variable)
        Button: Ptr[Widget_FrontEnd_Button] = Cast[Widget_FrontEnd_Button](ReturnValue_1)
        bSuccess: bool = Button
        if not bSuccess:
           goto(ExecutionFlow.Pop())
        ReturnValue_2: bool = NotEqual_ObjectObject(Button, self)
        if not ReturnValue_2:
           goto(ExecutionFlow.Pop())
        # Label 381
        Button.SetSelected(False)
        goto(ExecutionFlow.Pop())
        # Label 419
        ReturnValue_3: Ptr[PanelWidget] = self.GetParent()
        ReturnValue_4: bool = Default__KismetSystemLibrary.IsValid(ReturnValue_3)
        if not ReturnValue_4:
           goto(ExecutionFlow.Pop())
        ReturnValue_3 = self.GetParent()
        LocalParent = ReturnValue_3
        goto('L89')
        # Label 544
        ReturnValue_5: int32 = Variable + 1
        Variable = ReturnValue_5
        goto('L112')
    

    def GetButtonTextColor(self):
        ReturnValue: bool = self.mFrontEndButton.IsHovered()
        ReturnValue_0: bool = BooleanOR(ReturnValue, self.IsFocused)
        if not ReturnValue_0:
            goto('L185')
        
        TextWhite = None
        GraphicsWhite = None
        Default__HUDHelpers.GetFactoryGameWhite(self, Ref[TextWhite], Ref[GraphicsWhite])
        ReturnValue_1: SlateColor = TextWhite
        goto('L267')
        
        Text = None
        Graphics = None
        # Label 185
        Default__HUDHelpers.GetFactoryGameDarkGray(self, Ref[Text], Ref[Graphics])
        ReturnValue_1 = Text
    

    def GetButtonColor(self):
        ReturnValue: bool = self.mFrontEndButton.IsHovered()
        ReturnValue_0: bool = BooleanOR(ReturnValue, self.IsFocused)
        if not ReturnValue_0:
            goto('L155')
        ReturnValue_1: LinearColor = LinearColor(R = 0.7835379838943481, G = 0.2917709946632385, B = 0.057805001735687256, A = 1)
        goto('L381')
        # Label 155
        if not self.isSelected:
            goto('L226')
        ReturnValue_1 = LinearColor(R = 0.13286800682544708, G = 0.13286800682544708, B = 0.13563300669193268, A = 1)
        goto('L381')
        # Label 226
        LinearColor.R = 0
        LinearColor.G = 0
        LinearColor.B = 0
        LinearColor.A = 0
        ReturnValue_1 = LinearColor
    

    def SetFocused(self):
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        self.mFrontEndButton.SetUserFocus(ReturnValue)
        self.mFrontEndButton.SetKeyboardFocus()
        self.IsFocused = True
    

    def OnFocusReceived(self):
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        self.mFrontEndButton.SetUserFocus(ReturnValue)
        ReturnValue_0: EventReply = Default__WidgetBlueprintLibrary.Handled()
        ReturnValue_1: EventReply = ReturnValue_0
    

    def ShowButton(self):
        self.mFrontEndButton.SetVisibility(0)
    

    def HideButton(self):
        self.mFrontEndButton.SetVisibility(1)
    

    def GetButtonText(self):
        ReturnValue = self.mDisplayName
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_FrontEnd_Button(2524)
    

    def Destruct(self):
        self.ExecuteUbergraph_Widget_FrontEnd_Button(2529)
    

    def BndEvt__Button_0_K2Node_ComponentBoundEvent_0_OnButtonClickedEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_FrontEnd_Button(2534)
    

    def BndEvt__PauseMenuButton_K2Node_ComponentBoundEvent_1_OnButtonHoverEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_FrontEnd_Button(2567)
    

    def PreConstruct(self):
        ExecuteUbergraph_Widget_FrontEnd_Button.K2Node_Event_IsDesignTime = IsDesignTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_FrontEnd_Button(2676)
    

    def SetSelected(self, isSelected: bool):
        ExecuteUbergraph_Widget_FrontEnd_Button.K2Node_CustomEvent_IsSelected = isSelected #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_FrontEnd_Button(4472)
    

    def BndEvt__mFrontEndButton_K2Node_ComponentBoundEvent_2_OnButtonHoverEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_FrontEnd_Button(4496)
    

    def ExecuteUbergraph_Widget_FrontEnd_Button(self):
        # Label 10
        self.OnUnhovered.ProcessMulticastDelegate()
        # End
        # Label 34
        if not self.isSelected:
            goto('L1176')
        
        Text = None
        Graphics = None
        Default__HUDHelpers.GetFactoryGameDarkGray(self, Ref[Text], Ref[Graphics])
        SlateBrush.ImageSize = self.mFrontEndButton.WidgetStyle.Normal.ImageSize
        SlateBrush.Margin = self.mFrontEndButton.WidgetStyle.Normal.Margin
        SlateBrush.TintColor = Text
        SlateBrush.ResourceObject = self.mFrontEndButton.WidgetStyle.Normal.ResourceObject
        SlateBrush.DrawAs = self.mFrontEndButton.WidgetStyle.Normal.DrawAs
        SlateBrush.Tiling = self.mFrontEndButton.WidgetStyle.Normal.Tiling
        SlateBrush.Mirroring = self.mFrontEndButton.WidgetStyle.Normal.Mirroring
        ButtonStyle.Normal = SlateBrush
        ButtonStyle.Hovered = self.mFrontEndButton.WidgetStyle.Hovered
        ButtonStyle.Pressed = self.mFrontEndButton.WidgetStyle.Pressed
        ButtonStyle.Disabled = self.mFrontEndButton.WidgetStyle.Disabled
        ButtonStyle.NormalPadding = self.mFrontEndButton.WidgetStyle.NormalPadding
        ButtonStyle.PressedPadding = self.mFrontEndButton.WidgetStyle.PressedPadding
        ButtonStyle.PressedSlateSound = self.mFrontEndButton.WidgetStyle.PressedSlateSound
        ButtonStyle.HoveredSlateSound = self.mFrontEndButton.WidgetStyle.HoveredSlateSound
        
        ButtonStyle = None
        self.mFrontEndButton.SetStyle(Ref[ButtonStyle])
        self.Pointer.SetVisibility(0)
        # End
        # Label 1176
        Variable: LinearColor = LinearColor(R = 0, G = 0, B = 0, A = 0)
        Variable1: LinearColor = LinearColor(R = 0.09530699998140335, G = 0.09530699998140335, B = 0.09530699998140335, A = 1)
        Variable_0: bool = self.mUseTransparentBackground
        
        switch = {
            False: Variable1,
            True: Variable
        }
        SlateColor.SpecifiedColor = switch.get(Variable_0, None)
        SlateColor.ColorUseRule = 0
        SlateBrush1.ImageSize = self.mFrontEndButton.WidgetStyle.Normal.ImageSize
        SlateBrush1.Margin = self.mFrontEndButton.WidgetStyle.Normal.Margin
        SlateBrush1.TintColor = SlateColor
        SlateBrush1.ResourceObject = self.mFrontEndButton.WidgetStyle.Normal.ResourceObject
        SlateBrush1.DrawAs = self.mFrontEndButton.WidgetStyle.Normal.DrawAs
        SlateBrush1.Tiling = self.mFrontEndButton.WidgetStyle.Normal.Tiling
        SlateBrush1.Mirroring = self.mFrontEndButton.WidgetStyle.Normal.Mirroring
        ButtonStyle1.Normal = SlateBrush1
        ButtonStyle1.Hovered = self.mFrontEndButton.WidgetStyle.Hovered
        ButtonStyle1.Pressed = self.mFrontEndButton.WidgetStyle.Pressed
        ButtonStyle1.Disabled = self.mFrontEndButton.WidgetStyle.Disabled
        ButtonStyle1.NormalPadding = self.mFrontEndButton.WidgetStyle.NormalPadding
        ButtonStyle1.PressedPadding = self.mFrontEndButton.WidgetStyle.PressedPadding
        ButtonStyle1.PressedSlateSound = self.mFrontEndButton.WidgetStyle.PressedSlateSound
        ButtonStyle1.HoveredSlateSound = self.mFrontEndButton.WidgetStyle.HoveredSlateSound
        
        ButtonStyle1 = None
        self.mFrontEndButton.SetStyle(Ref[ButtonStyle1])
        self.Pointer.SetVisibility(1)
        # End
        # Label 2481
        self.OnClicked.ProcessMulticastDelegate()
        # End
        # Label 2505
        self.HideButton()
        # End
        # End
        goto('L2505')
        self.SetActiveWidgetInSwitcher()
        self.ClearListOfSelections()
        goto('L2481')
        self.OnHovered.ProcessMulticastDelegate()
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_0: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_UI_MainMenu_MouseOver, ReturnValue, True)
        # End
        if not self.IsBigButton:
            goto('L4388')
        self.Pointer.SetBrushSize(Vector2D(X = 30, Y = 30))
        self.FontSize = 25
        # Label 2769
        SlateFontInfo.FontObject = self.Title.Font.FontObject
        SlateFontInfo.FontMaterial = self.Title.Font.FontMaterial
        SlateFontInfo.OutlineSettings = self.Title.Font.OutlineSettings
        SlateFontInfo.TypefaceFontName = self.Title.Font.TypefaceFontName
        SlateFontInfo.Size = self.FontSize
        self.Title.SetFont(SlateFontInfo)
        self.SetTitle(self.mDisplayName)
        Variable2: LinearColor = LinearColor(R = 0, G = 0, B = 0, A = 0)
        Variable3: LinearColor = LinearColor(R = 0.09530699998140335, G = 0.09530699998140335, B = 0.09530699998140335, A = 1)
        Variable1_0: bool = self.mUseTransparentBackground
        
        switch_0 = {
            False: Variable3,
            True: Variable2
        }
        SlateColor1.SpecifiedColor = switch_0.get(Variable1_0, None)
        SlateColor1.ColorUseRule = 0
        SlateBrush2.ImageSize = self.mFrontEndButton.WidgetStyle.Normal.ImageSize
        SlateBrush2.Margin = self.mFrontEndButton.WidgetStyle.Normal.Margin
        SlateBrush2.TintColor = SlateColor1
        SlateBrush2.ResourceObject = self.mFrontEndButton.WidgetStyle.Normal.ResourceObject
        SlateBrush2.DrawAs = self.mFrontEndButton.WidgetStyle.Normal.DrawAs
        SlateBrush2.Tiling = self.mFrontEndButton.WidgetStyle.Normal.Tiling
        SlateBrush2.Mirroring = self.mFrontEndButton.WidgetStyle.Normal.Mirroring
        ButtonStyle2.Normal = SlateBrush2
        ButtonStyle2.Hovered = self.mFrontEndButton.WidgetStyle.Hovered
        ButtonStyle2.Pressed = self.mFrontEndButton.WidgetStyle.Pressed
        ButtonStyle2.Disabled = self.mFrontEndButton.WidgetStyle.Disabled
        ButtonStyle2.NormalPadding = self.mFrontEndButton.WidgetStyle.NormalPadding
        ButtonStyle2.PressedPadding = self.mFrontEndButton.WidgetStyle.PressedPadding
        ButtonStyle2.PressedSlateSound = self.mFrontEndButton.WidgetStyle.PressedSlateSound
        ButtonStyle2.HoveredSlateSound = self.mFrontEndButton.WidgetStyle.HoveredSlateSound
        
        ButtonStyle2 = None
        self.mFrontEndButton.SetStyle(Ref[ButtonStyle2])
        # End
        # Label 4388
        self.Pointer.SetBrushSize(Vector2D(X = 20, Y = 20))
        self.FontSize = 15
        goto('L2769')
        self.isSelected = IsSelected
        goto('L34')
        goto('L10')
    

    def OnUnhovered__DelegateSignature(self):
        pass
    

    def OnHovered__DelegateSignature(self):
        pass
    

    def OnClicked__DelegateSignature(self):
        pass
    
