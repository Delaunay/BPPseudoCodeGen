
from codegen.ue4_stub import *

from Game.FactoryGame.Interface.UI.InGame.-Shared.Widget_LetterSpacedLetter import ExecuteUbergraph_Widget_LetterSpacedLetter
from Script.UMG import SetBrushTintColor
from Script.SlateCore import SlateFontInfo
from Script.UMG import SetFont
from Script.UMG import WidgetAnimation
from Game.FactoryGame.Interface.UI.InGame.-Shared.Widget_LetterSpacedLetter import ExecuteUbergraph_Widget_LetterSpacedLetter.K2Node_Event_IsDesignTime
from Script.UMG import UserWidget
from Script.CoreUObject import LinearColor

class Widget_LetterSpacedLetter(UserWidget):
    SpawnAnim: Ptr[WidgetAnimation]
    mText: FText
    mFont: SlateFontInfo = Namespace(FontMaterial={'$Empty': True}, FontObject={'$Empty': True}, OutlineSettings={'OutlineSize': 0, 'bSeparateFillAlpha': False, 'bApplyOutlineToDropShadows': True, 'OutlineMaterial': {'$Empty': True}, 'OutlineColor': {'R': 0, 'G': 0, 'B': 0, 'A': 1}}, Size=1, TypefaceFontName='None')
    mAnimColor: LinearColor = Namespace(A=1, B=0.05951099842786789, G=0.2917709946632385, R=0.7835379838943481)
    
    def SetTextAndFont(self, text: FText, Font: SlateFontInfo):
        self.mText = text
        self.mFont = Font
        self.mTextBlock.SetFont(self.mFont)
        self.mTextBlock.SetText(self.mText)
    

    def PreConstruct(self):
        ExecuteUbergraph_Widget_LetterSpacedLetter.K2Node_Event_IsDesignTime = IsDesignTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_LetterSpacedLetter(10)
    

    def ExecuteUbergraph_Widget_LetterSpacedLetter(self):
        self.SetTextAndFont(self.mText, self.mFont)
        SlateColor.SpecifiedColor = self.mAnimColor
        SlateColor.ColorUseRule = 0
        self.mOverlayBlock.SetBrushTintColor(SlateColor)
    
