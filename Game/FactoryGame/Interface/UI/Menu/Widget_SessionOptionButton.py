
from codegen.ue4_stub import *

from Script.UMG import SetUserFocus
from Script.AkAudio import PostAkEvent
from Script.UMG import SetKeyboardFocus
from Game.FactoryGame.Interface.UI.Menu.Widget_SessionOptionButton import ExecuteUbergraph_Widget_SessionOptionButton
from Script.SlateCore import FontOutlineSettings
from Script.Engine import PlayerController
from Script.UMG import Handled
from Script.UMG import IsPressed
from Script.UMG import ESlateVisibility
from Game.FactoryGame.Interface.UI.Audio.MainMenu.Play_UI_MainMenu_MouseOver import Play_UI_MainMenu_MouseOver
from Script.UMG import Default__WidgetBlueprintLibrary
from Script.Engine import BooleanOR
from Script.SlateCore import SlateFontInfo
from Script.CoreUObject import LinearColor
from Script.FactoryGame import FGButtonWidget
from Script.UMG import SetFont
from Script.AkAudio import Default__AkGameplayStatics
from Game.FactoryGame.Interface.UI.HUDHelpers.HUDHelpers import Default__HUDHelpers
from Game.FactoryGame.Interface.UI.Audio.MainMenu.Play_UI_MainMenu_Click import Play_UI_MainMenu_Click
from Script.SlateCore import SlateBrush
from Script.SlateCore import SlateColor
from Script.AkAudio import AkComponent
from Script.UMG import EventReply
from Game.FactoryGame.Interface.Font.DescriptionText import DescriptionText

class Widget_SessionOptionButton(FGButtonWidget):
    OnClicked: FMulticastScriptDelegate
    mText: FText
    mBrush: SlateBrush
    isLoadButton: bool
    
    def GetLoadButtonVisibility(self):
        if not self.isLoadButton:
            goto('L39')
        ReturnValue = 0
        goto('L59')
        # Label 39
        ReturnValue = 2
    

    def SetFontForButton(self):
        loadFont = SlateFontInfo(FontObject = DescriptionText, FontMaterial = None, OutlineSettings = FontOutlineSettings(OutlineSize = 0, bSeparateFillAlpha = False, bApplyOutlineToDropShadows = False, OutlineMaterial = None, OutlineColor = LinearColor(R = 0, G = 0, B = 0, A = 1)), TypefaceFontName = "Default", Size = 16)
        saveFont = SlateFontInfo(FontObject = DescriptionText, FontMaterial = None, OutlineSettings = FontOutlineSettings(OutlineSize = 0, bSeparateFillAlpha = False, bApplyOutlineToDropShadows = False, OutlineMaterial = None, OutlineColor = LinearColor(R = 0, G = 0, B = 0, A = 1)), TypefaceFontName = "Default", Size = 10)
        if not self.isLoadButton:
            goto('L292')
        self.mButtonText.SetFont(loadFont)
        # End
        # Label 292
        self.mButtonText.SetFont(saveFont)
    

    def GetIconColor(self):
        ReturnValue1: bool = self.MenuButton.IsHovered()
        ReturnValue: bool = self.isLoadButton and ReturnValue1
        if not ReturnValue:
            goto('L185')
        
        Orange = None
        OrangeText = None
        Default__HUDHelpers.GetFactoryGameOrange(self, Ref[Orange], Ref[OrangeText])
        ReturnValue_0: LinearColor = Orange
        goto('L414')
        # Label 185
        ReturnValue_1: bool = self.MenuButton.IsHovered()
        if not ReturnValue_1:
            goto('L332')
        
        Text = None
        Graphics = None
        Default__HUDHelpers.GetFactoryGameDarkGray(self, Ref[Text], Ref[Graphics])
        ReturnValue_0 = Graphics
        goto('L414')
        
        TextWhite = None
        GraphicsWhite = None
        # Label 332
        Default__HUDHelpers.GetFactoryGameWhite(self, Ref[TextWhite], Ref[GraphicsWhite])
        ReturnValue_0 = GraphicsWhite
    

    def GetButtonBorderColor(self):
        ReturnValue1: bool = self.MenuButton.IsHovered()
        ReturnValue: bool = self.isLoadButton and ReturnValue1
        if not ReturnValue:
            goto('L185')
        
        Orange = None
        OrangeText = None
        Default__HUDHelpers.GetFactoryGameOrange(self, Ref[Orange], Ref[OrangeText])
        ReturnValue_0: LinearColor = Orange
        goto('L414')
        # Label 185
        ReturnValue_1: bool = self.MenuButton.IsHovered()
        if not ReturnValue_1:
            goto('L332')
        
        Text = None
        Graphics = None
        Default__HUDHelpers.GetFactoryGameDarkGray(self, Ref[Text], Ref[Graphics])
        ReturnValue_0 = Graphics
        goto('L414')
        
        TextWhite = None
        GraphicsWhite = None
        # Label 332
        Default__HUDHelpers.GetFactoryGameWhite(self, Ref[TextWhite], Ref[GraphicsWhite])
        ReturnValue_0 = GraphicsWhite
    

    def GetDeleteButtonColor(self):
        ReturnValue: bool = self.MenuButton.IsHovered()
        ReturnValue_0: bool = self.MenuButton.IsPressed()
        ReturnValue_1: bool = BooleanOR(ReturnValue, ReturnValue_0)
        if not ReturnValue_1:
            goto('L227')
        
        TextWhite = None
        GraphicsWhite = None
        Default__HUDHelpers.GetFactoryGameWhite(self, Ref[TextWhite], Ref[GraphicsWhite])
        ReturnValue_2: LinearColor = GraphicsWhite
        goto('L309')
        
        Text = None
        Graphics = None
        # Label 227
        Default__HUDHelpers.GetFactoryGameDarkGray(self, Ref[Text], Ref[Graphics])
        ReturnValue_2 = Graphics
    

    def GetButtonStyle(self):
        ReturnValue: bool = self.MenuButton.IsHovered()
        if not ReturnValue:
            goto('L85')
        ReturnValue_0: uint8 = 0
        goto('L105')
        # Label 85
        ReturnValue_0 = 2
    

    def GetTextColor(self):
        ReturnValue1: bool = self.MenuButton.IsHovered()
        ReturnValue: bool = self.isLoadButton and ReturnValue1
        if not ReturnValue:
            goto('L185')
        
        Orange = None
        OrangeText = None
        Default__HUDHelpers.GetFactoryGameOrange(self, Ref[Orange], Ref[OrangeText])
        ReturnValue_0: SlateColor = OrangeText
        goto('L414')
        # Label 185
        ReturnValue_1: bool = self.MenuButton.IsHovered()
        if not ReturnValue_1:
            goto('L332')
        
        Text = None
        Graphics = None
        Default__HUDHelpers.GetFactoryGameDarkGray(self, Ref[Text], Ref[Graphics])
        ReturnValue_0 = Text
        goto('L414')
        
        TextWhite = None
        GraphicsWhite = None
        # Label 332
        Default__HUDHelpers.GetFactoryGameWhite(self, Ref[TextWhite], Ref[GraphicsWhite])
        ReturnValue_0 = TextWhite
    

    def GetLoadButtonColor(self):
        ReturnValue: bool = self.MenuButton.IsHovered()
        ReturnValue_0: bool = self.MenuButton.IsPressed()
        ReturnValue_1: bool = BooleanOR(ReturnValue, ReturnValue_0)
        if not ReturnValue_1:
            goto('L227')
        
        TextWhite = None
        GraphicsWhite = None
        Default__HUDHelpers.GetFactoryGameWhite(self, Ref[TextWhite], Ref[GraphicsWhite])
        ReturnValue_2: LinearColor = GraphicsWhite
        goto('L309')
        
        Orange = None
        OrangeText = None
        # Label 227
        Default__HUDHelpers.GetFactoryGameOrange(self, Ref[Orange], Ref[OrangeText])
        ReturnValue_2 = Orange
    

    def SetFocused(self):
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        self.MenuButton.SetUserFocus(ReturnValue)
        self.MenuButton.SetKeyboardFocus()
    

    def OnFocusReceived(self):
        ReturnValue: EventReply = Default__WidgetBlueprintLibrary.Handled()
        ReturnValue_0: EventReply = ReturnValue
    

    def HideButton(self):
        self.MenuButton.SetVisibility(2)
    

    def BndEvt__Button_0_K2Node_ComponentBoundEvent_0_OnButtonClickedEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_SessionOptionButton(100)
    

    def Destruct(self):
        self.ExecuteUbergraph_Widget_SessionOptionButton(228)
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_SessionOptionButton(233)
    

    def BndEvt__MenuButton_K2Node_ComponentBoundEvent_1_OnButtonHoverEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_SessionOptionButton(252)
    

    def ExecuteUbergraph_Widget_SessionOptionButton(self):
        # Label 10
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_0: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_UI_MainMenu_MouseOver, ReturnValue, True)
        # End
        self.OnClicked.ProcessMulticastDelegate()
        ReturnValue1: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue1_0: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_UI_MainMenu_Click, ReturnValue1, True)
        # End
        # Label 209
        self.HideButton()
        # End
        goto('L209')
        self.SetFontForButton()
        # End
        goto('L10')
    

    def OnClicked__DelegateSignature(self):
        pass
    
