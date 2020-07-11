
from codegen.ue4_stub import *

from Script.Engine import Default__KismetSystemLibrary
from Game.FactoryGame.Interface.UI.HUDHelpers.HUDHelpers import Default__HUDHelpers
from Script.UMG import UserWidget
from Script.UMG import IsVisible
from Script.UMG import UMGSequencePlayer
from Script.UMG import PlayAnimation
from Script.UMG import ESlateVisibility
from Script.CoreUObject import Object
from Script.Engine import IsValid
from Script.UMG import WidgetAnimation
from Game.FactoryGame.Buildable.Factory.TradingPost.Widget_TradingPost_RecipeInfoBox import ExecuteUbergraph_Widget_TradingPost_RecipeInfoBox

class Widget_TradingPost_RecipeInfoBox(UserWidget):
    CategoryFade: Ptr[WidgetAnimation]
    IconFade: Ptr[WidgetAnimation]
    IconGlowAnim: Ptr[WidgetAnimation]
    mCategoryIconImage: Ptr[Object]
    
    def GetLightGrayColor(self):
        
        Text = None
        Graphics = None
        Default__HUDHelpers.GetFactoryGameLightGray(self, Ref[Text], Ref[Graphics])
        ReturnValue = Graphics
    

    def GetLightGrayText(self):
        
        Text = None
        Graphics = None
        Default__HUDHelpers.GetFactoryGameLightGray(self, Ref[Text], Ref[Graphics])
        ReturnValue = Text
    

    def GetCategoryIcon(self):
        SlateBrush.ImageSize = self.mCategoryIcon.Brush.ImageSize
        SlateBrush.Margin = self.mCategoryIcon.Brush.Margin
        SlateBrush.TintColor = self.mCategoryIcon.Brush.TintColor
        SlateBrush.ResourceObject = self.mCategoryIconImage
        SlateBrush.DrawAs = self.mCategoryIcon.Brush.DrawAs
        SlateBrush.Tiling = self.mCategoryIcon.Brush.Tiling
        SlateBrush.Mirroring = self.mCategoryIcon.Brush.Mirroring
        ReturnValue = SlateBrush
    

    def Get_Divider_Visibility_0(self):
        ReturnValue: bool = self.mCategoryIcon.IsVisible()
        if not ReturnValue:
            goto('L81')
        ReturnValue_0: uint8 = 0
        goto('L101')
        # Label 81
        ReturnValue_0 = 2
    

    def Get_mIcon_Visibility_0(self):
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(self.mIcon.Brush.ResourceObject)
        if not ReturnValue:
            goto('L121')
        ReturnValue_0: uint8 = 0
        goto('L141')
        # Label 121
        ReturnValue_0 = 2
    

    def SetItemTitle(self, Title: FText):
        self.mProductTitleText.SetText(Title)
    

    def SetItemDescriptionText(self, Description: FText):
        self.mProductDescriptionText.SetText(Description)
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_TradingPost_RecipeInfoBox(61)
    

    def ExecuteUbergraph_Widget_TradingPost_RecipeInfoBox(self):
        # Label 10
        ReturnValue: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.IconGlowAnim, 0, 0, 0, 1)
        # End
        goto('L10')
    
