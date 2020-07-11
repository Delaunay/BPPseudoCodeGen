
from codegen.ue4_stub import *

from Script.UMG import SetUserFocus
from Script.Engine import Conv_TextToString
from Script.AkAudio import PostAkEvent
from Script.UMG import SetKeyboardFocus
from Script.Engine import Not_PreBool
from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import PlayerController
from Script.UMG import ESlateVisibility
from Game.FactoryGame.Interface.UI.Audio.MainMenu.Play_UI_MainMenu_MouseOver import Play_UI_MainMenu_MouseOver
from Script.Engine import IsValid
from Script.Engine import EqualEqual_StrStr
from Script.UMG import SetColorAndOpacity
from Script.UMG import SetHeightOverride
from Script.Engine import Default__KismetTextLibrary
from Script.FactoryGame import FGButtonWidget
from Script.UMG import GetText
from Script.Engine import Default__KismetStringLibrary
from Game.FactoryGame.Interface.UI.InGame.-Shared.Widget_StandardButton import ExecuteUbergraph_Widget_StandardButton
from Script.AkAudio import Default__AkGameplayStatics
from Script.UMG import SetWidthOverride
from Game.FactoryGame.Interface.UI.InGame.-Shared.Widget_StandardButton import ExecuteUbergraph_Widget_StandardButton.K2Node_Event_IsDesignTime
from Game.FactoryGame.Interface.UI.Audio.MainMenu.Play_UI_MainMenu_Click import Play_UI_MainMenu_Click
from Script.SlateCore import SlateBrush
from Script.UMG import SetStyle
from Script.AkAudio import AkComponent
from Script.CoreUObject import LinearColor

class Widget_StandardButton(FGButtonWidget):
    mText: FText
    OnClicked: FMulticastScriptDelegate
    mIconBrush: SlateBrush = Namespace(DrawAs=3, ImageSize={'X': 8, 'Y': 8}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$Empty': True}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    mIconWidth: float = 24
    mIconHeight: float = 24
    mIsDisabled: bool
    OnClickedIncludeSelf: FMulticastScriptDelegate
    
    def Cleanup(self):
        self.OnClicked.Clear()
        # Label 10
        self.OnClickedIncludeSelf.Clear()
    

    def SetIsDisabled(self, mIsDisabled: bool):
        self.mIsDisabled = mIsDisabled
        Variable2: LinearColor = LinearColor(R = 0.030612999573349953, G = 0.030612999573349953, B = 0.03125, A = 1)
        Variable3: LinearColor = LinearColor(R = 0.13286800682544708, G = 0.13286800682544708, B = 0.13563300669193268, A = 1)
        Variable2_0: bool = self.mIsDisabled
        
        switch = {
            False: Variable3,
            True: Variable2
        }
        SlateColor.SpecifiedColor = switch.get(Variable2_0, None)
        SlateColor.ColorUseRule = 0
        SlateBrush.ImageSize = self.mButton.WidgetStyle.Normal.ImageSize
        SlateBrush.Margin = self.mButton.WidgetStyle.Normal.Margin
        SlateBrush.TintColor = SlateColor
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
        Variable: LinearColor = LinearColor(R = 0.13286800682544708, G = 0.13286800682544708, B = 0.13563300669193268, A = 1)
        Variable1: LinearColor = LinearColor(R = 0.9796140193939209, G = 0.9796140193939209, B = 1, A = 1)
        Variable1_0: bool = self.mIsDisabled
        
        switch_0 = {
            False: Variable1,
            True: Variable
        }
        SlateColor1.SpecifiedColor = switch_0.get(Variable1_0, None)
        SlateColor1.ColorUseRule = 0
        self.ButtonText.SetColorAndOpacity(SlateColor1)
        Variable = LinearColor(R = 0.13286800682544708, G = 0.13286800682544708, B = 0.13563300669193268, A = 1)
        Variable1 = LinearColor(R = 0.9796140193939209, G = 0.9796140193939209, B = 1, A = 1)
        Variable1_0 = self.mIsDisabled
        
        switch_1 = {
            False: Variable1,
            True: Variable
        }
        self.Icon.SetColorAndOpacity(switch_1.get(Variable1_0, None))
        Variable_0: uint8 = 3
        Variable1_1: uint8 = 0
        Variable_1: bool = self.mIsDisabled
        
        switch_2 = {
            False: Variable1_1,
            True: Variable_0
        }
        self.mButton.SetVisibility(switch_2.get(Variable_1, None))
    

    def SetIconSize(self):
        self.mIconSizeBox.SetHeightOverride(self.mIconHeight)
        self.mIconSizeBox.SetWidthOverride(self.mIconWidth)
    

    def SetIconBrush(self, mIconBrush: SlateBrush):
        self.mIconBrush = mIconBrush
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(self.mIconBrush.ResourceObject)
        if not ReturnValue:
            goto('L189')
        self.IconContainer.SetVisibility(3)
        
        self.Icon.SetBrush(Ref[self.mIconBrush])
        # End
        # Label 189
        self.IconContainer.SetVisibility(1)
    

    def SetText(self, mText: FText):
        self.mText = mText
        
        ReturnValue: FString = Default__KismetTextLibrary.Conv_TextToString(Ref[mText])
        ReturnValue_0: bool = Default__KismetStringLibrary.EqualEqual_StrStr(ReturnValue, "")
        ReturnValue_1: FText = self.ButtonText.GetText()
        
        # Label 189
        ReturnValue1: FString = Default__KismetTextLibrary.Conv_TextToString(Ref[ReturnValue_1])
        ReturnValue1_0: bool = Default__KismetStringLibrary.EqualEqual_StrStr(ReturnValue1, "")
        ReturnValue_2: bool = ReturnValue1_0 and ReturnValue_0
        ReturnValue_3: bool = Not_PreBool(ReturnValue_2)
        if not ReturnValue_3:
            goto('L470')
        self.ButtonText.SetVisibility(3)
        self.ButtonText.SetText(mText)
        # End
        # Label 470
        self.ButtonText.SetVisibility(1)
    

    def SetFocused(self):
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        self.mButton.SetUserFocus(ReturnValue)
        self.mButton.SetKeyboardFocus()
    

    def PreConstruct(self):
        ExecuteUbergraph_Widget_StandardButton.K2Node_Event_IsDesignTime = IsDesignTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_StandardButton(29)
    

    def BndEvt__MarkAsReadButton_K2Node_ComponentBoundEvent_0_OnButtonClickedEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_StandardButton(94)
    

    def BndEvt__mButton_K2Node_ComponentBoundEvent_1_OnButtonHoverEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_StandardButton(223)
    

    def Destruct(self):
        self.ExecuteUbergraph_Widget_StandardButton(313)
    

    def ExecuteUbergraph_Widget_StandardButton(self):
        # Label 10
        self.Cleanup()
        # End
        self.SetText(self.mText)
        self.SetIconBrush(self.mIconBrush)
        self.SetIconSize()
        # End
        self.OnClicked.ProcessMulticastDelegate()
        self.OnClickedIncludeSelf.ProcessMulticastDelegate(self)
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_0: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_UI_MainMenu_Click, ReturnValue, True)
        # End
        ReturnValue1: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue1_0: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_UI_MainMenu_MouseOver, ReturnValue1, True)
        # End
        goto('L10')
    

    def OnClickedIncludeSelf__DelegateSignature(self, ButtonWidget: Ptr[Widget_StandardButton]):
        pass
    

    def OnClicked__DelegateSignature(self):
        pass
    
