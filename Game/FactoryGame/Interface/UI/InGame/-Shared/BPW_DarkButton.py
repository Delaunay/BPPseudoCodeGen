
from codegen.ue4_stub import *

from Script.Engine import Texture2D
from Game.FactoryGame.Interface.UI.InGame.-Shared.BPW_DarkButton import ExecuteUbergraph_BPW_DarkButton
from Script.UMG import SetPadding
from Script.UMG import OverlaySlot
from Script.UMG import Default__WidgetLayoutLibrary
from Script.UMG import SlotAsOverlaySlot
from Game.FactoryGame.Interface.UI.Assets.Shared.TXUI_DarkButton import TXUI_DarkButton
from Script.UMG import ESlateVisibility
from Script.CoreUObject import Object
from Script.UMG import SetColorAndOpacity
from Script.Engine import Default__KismetTextLibrary
from Game.FactoryGame.Interface.UI.Assets.Shared.LED_off import LED_off
from Script.Engine import TextToUpper
from Script.CoreUObject import LinearColor
from Script.UMG import UserWidget
from Script.UMG import SetStyle
from Game.FactoryGame.Interface.UI.Assets.Shared.LED_Blue_on import LED_Blue_on
from Game.FactoryGame.Interface.UI.Assets.Shared.TXUI_DarkButton_Selected import TXUI_DarkButton_Selected
from Game.FactoryGame.Interface.UI.InGame.-Shared.BPW_DarkButton import ExecuteUbergraph_BPW_DarkButton.K2Node_Event_IsDesignTime

class BPW_DarkButton(UserWidget):
    mText: FText = NSLOCTEXT("", "555913004F794CA00EA509A3977AB631", "Full Pipe Network")
    mIsSelected: bool
    OnClicked: FMulticastScriptDelegate
    mIsDisabled: bool
    
    def SetIsDisabled(self, IsDisabled: bool):
        self.mIsDisabled = IsDisabled
        Variable: uint8 = 3
        Variable1: uint8 = 4
        Variable1_0: bool = self.mIsDisabled
        
        switch = {
            False: Variable1,
            True: Variable
        }
        self.SetVisibility(switch.get(Variable1_0, None))
        Variable_0: LinearColor = LinearColor(R = 0.13286800682544708, G = 0.13286800682544708, B = 0.13563300669193268, A = 1)
        Variable1_1: LinearColor = LinearColor(R = 0.6038280129432678, G = 0.5972020030021667, B = 0.5972020030021667, A = 1)
        Variable_1: bool = self.mIsDisabled
        
        switch_0 = {
            False: Variable1_1,
            True: Variable_0
        }
        SlateColor.SpecifiedColor = switch_0.get(Variable_1, None)
        SlateColor.ColorUseRule = 0
        self.mTextObject.SetColorAndOpacity(SlateColor)
    

    def SetIsSelected(self, mIsSelected: bool):
        self.mIsSelected = mIsSelected
        Variable2: Ptr[Object] = LED_Blue_on
        Variable3: Ptr[Object] = LED_off
        Variable2_0: bool = self.mIsSelected
        SlateBrush2.ImageSize = self.mLed.Brush.ImageSize
        SlateBrush2.Margin = self.mLed.Brush.Margin
        SlateBrush2.TintColor = self.mLed.Brush.TintColor
        
        switch = {
            False: Variable3,
            True: Variable2
        }
        SlateBrush2.ResourceObject = switch.get(Variable2_0, None)
        SlateBrush2.DrawAs = self.mLed.Brush.DrawAs
        SlateBrush2.Tiling = self.mLed.Brush.Tiling
        SlateBrush2.Mirroring = self.mLed.Brush.Mirroring
        
        SlateBrush2 = None
        self.mLed.SetBrush(Ref[SlateBrush2])
        Variable: Ptr[Texture2D] = TXUI_DarkButton_Selected
        Variable1: Ptr[Texture2D] = TXUI_DarkButton
        Variable1_0: bool = self.mIsSelected
        
        switch_0 = {
            False: Variable1,
            True: Variable
        }
        mButtonTexture = switch_0.get(Variable1_0, None)
        SlateBrush.ImageSize = self.mButton.WidgetStyle.Hovered.ImageSize
        SlateBrush.Margin = self.mButton.WidgetStyle.Hovered.Margin
        SlateBrush.TintColor = self.mButton.WidgetStyle.Hovered.TintColor
        SlateBrush.ResourceObject = mButtonTexture
        SlateBrush.DrawAs = self.mButton.WidgetStyle.Hovered.DrawAs
        SlateBrush.Tiling = self.mButton.WidgetStyle.Hovered.Tiling
        SlateBrush.Mirroring = self.mButton.WidgetStyle.Hovered.Mirroring
        SlateBrush1.ImageSize = self.mButton.WidgetStyle.Normal.ImageSize
        SlateBrush1.Margin = self.mButton.WidgetStyle.Normal.Margin
        SlateBrush1.TintColor = self.mButton.WidgetStyle.Normal.TintColor
        SlateBrush1.ResourceObject = mButtonTexture
        SlateBrush1.DrawAs = self.mButton.WidgetStyle.Normal.DrawAs
        SlateBrush1.Tiling = self.mButton.WidgetStyle.Normal.Tiling
        SlateBrush1.Mirroring = self.mButton.WidgetStyle.Normal.Mirroring
        ButtonStyle.Normal = SlateBrush1
        ButtonStyle.Hovered = SlateBrush
        ButtonStyle.Pressed = self.mButton.WidgetStyle.Pressed
        ButtonStyle.Disabled = self.mButton.WidgetStyle.Disabled
        ButtonStyle.NormalPadding = self.mButton.WidgetStyle.NormalPadding
        ButtonStyle.PressedPadding = self.mButton.WidgetStyle.PressedPadding
        ButtonStyle.PressedSlateSound = self.mButton.WidgetStyle.PressedSlateSound
        ButtonStyle.HoveredSlateSound = self.mButton.WidgetStyle.HoveredSlateSound
        
        ButtonStyle = None
        self.mButton.SetStyle(Ref[ButtonStyle])
        Variable_0: float = 2
        Variable1_1: float = 0
        Variable_1: bool = self.mIsSelected
        ReturnValue: Ptr[OverlaySlot] = Default__WidgetLayoutLibrary.SlotAsOverlaySlot(self.mContainer)
        
        switch_1 = {
            False: Variable1_1,
            True: Variable_0
        }
        ReturnValue_0: float = switch_1.get(Variable_1, None) * -1
        Margin.Left = 0
        
        switch_2 = {
            False: Variable1_1,
            True: Variable_0
        }
        Margin.Top = switch_2.get(Variable_1, None)
        Margin.Right = 0
        Margin.Bottom = ReturnValue_0
        ReturnValue.SetPadding(Margin)
    

    def SetText(self, mText: FText):
        self.mText = mText
        
        ReturnValue: FText = Default__KismetTextLibrary.TextToUpper(Ref[self.mText])
        self.mTextObject.SetText(ReturnValue)
    

    def PreConstruct(self):
        ExecuteUbergraph_BPW_DarkButton.K2Node_Event_IsDesignTime = IsDesignTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BPW_DarkButton(34)
    

    def BndEvt__mButton_K2Node_ComponentBoundEvent_0_OnButtonClickedEvent__DelegateSignature(self):
        self.ExecuteUbergraph_BPW_DarkButton(62)
    

    def ExecuteUbergraph_BPW_DarkButton(self):
        # Label 10
        self.OnClicked.ProcessMulticastDelegate()
        # End
        self.SetText(self.mText)
        # End
        goto('L10')
    

    def OnClicked__DelegateSignature(self):
        pass
    
