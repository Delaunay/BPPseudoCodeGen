
from codegen.ue4_stub import *

from Game.FactoryGame.Interface.UI.Menu.Graphics.Credits.Widget_Credit_Trademark import ExecuteUbergraph_Widget_Credit_Trademark.K2Node_Event_IsDesignTime
from Script.UMG import UserWidget
from Script.Engine import Texture2D
from Script.UMG import ESlateVisibility
from Script.UMG import SetText
from Game.FactoryGame.Interface.UI.Menu.Graphics.Credits.ECreditType import ECreditType
from Game.FactoryGame.Interface.UI.Menu.Graphics.Credits.wWise_White import wWise_White
from Script.Engine import NotEqual_ByteByte
from Game.FactoryGame.Interface.UI.Menu.Graphics.Credits.Widget_Credit_Trademark import ExecuteUbergraph_Widget_Credit_Trademark
from Script.Engine import TextIsEmpty
from Script.Engine import Default__KismetTextLibrary
from Game.FactoryGame.Interface.UI.Menu.Graphics.Credits.Unreal_Engine_White import Unreal_Engine_White

class Widget_Credit_Trademark(UserWidget):
    NewVar_0: Ptr[Texture2D]
    mCreditType: uint8 = 1
    mTrademarkText: FText
    
    def ShowHideText(self):
        Variable: uint8 = 2
        Variable1: uint8 = 3
        
        ReturnValue: bool = Default__KismetTextLibrary.TextIsEmpty(Ref[self.mTrademarkText])
        Variable_0: bool = ReturnValue
        
        switch = {
            False: Variable1,
            True: Variable
        }
        self.mCreditsText.SetVisibility(switch.get(Variable_0, None))
    

    def SetText(self, mText: FText):
        self.mTrademarkText = mText
        
        self.mCreditsText.SetText(Ref[self.mTrademarkText])
    

    def PreConstruct(self):
        ExecuteUbergraph_Widget_Credit_Trademark.K2Node_Event_IsDesignTime = IsDesignTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_Credit_Trademark(29)
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_Credit_Trademark(1305)
    

    def ExecuteUbergraph_Widget_Credit_Trademark(self):
        # Label 10
        self.ShowHideText()
        # End
        CmpSuccess: bool = NotEqual_ByteByte(self.mCreditType, 0)
        if not CmpSuccess:
            goto('L124')
        CmpSuccess = NotEqual_ByteByte(self.mCreditType, 1)
        if not CmpSuccess:
            goto('L604')
        # End
        # Label 124
        SlateBrush.ImageSize = self.mIconBrush.Brush.ImageSize
        SlateBrush.Margin = self.mIconBrush.Brush.Margin
        SlateBrush.TintColor = self.mIconBrush.Brush.TintColor
        SlateBrush.ResourceObject = Unreal_Engine_White
        SlateBrush.DrawAs = self.mIconBrush.Brush.DrawAs
        SlateBrush.Tiling = self.mIconBrush.Brush.Tiling
        SlateBrush.Mirroring = self.mIconBrush.Brush.Mirroring
        
        SlateBrush = None
        self.mIconBrush.SetBrush(Ref[SlateBrush])
        # End
        # Label 604
        SlateBrush1.ImageSize = self.mIconBrush.Brush.ImageSize
        SlateBrush1.Margin = self.mIconBrush.Brush.Margin
        SlateBrush1.TintColor = self.mIconBrush.Brush.TintColor
        SlateBrush1.ResourceObject = wWise_White
        SlateBrush1.DrawAs = self.mIconBrush.Brush.DrawAs
        SlateBrush1.Tiling = self.mIconBrush.Brush.Tiling
        SlateBrush1.Mirroring = self.mIconBrush.Brush.Mirroring
        
        SlateBrush1 = None
        self.mIconBrush.SetBrush(Ref[SlateBrush1])
        self.SetText("{'Instruction': 'EX_UnicodeStringConst', 'InstOffsetFromTop': 1094, 'Value': '<SmallText>Powered by Wwise © 2006 – 2019 Audiokinetic Inc. All rights reserved.</>'}")
        # End
        goto('L10')
    
