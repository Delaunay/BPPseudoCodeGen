
from codegen.ue4_stub import *

from Script.Engine import Texture
from Script.Engine import Texture2D
from Script.SlateCore import Margin
from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import Default__KismetArrayLibrary
from Game.FactoryGame.Buildable.Factory.TradingPost.Widget_SchematicRewardItem import Widget_SchematicRewardItem
from Script.FactoryGame import GetItemName
from Script.FactoryGame import GetBigIcon
from Script.Engine import IsValid
from Game.FactoryGame.Buildable.Factory.TradingPost.Widget_SchematicRewardItem import Construct
from Script.FactoryGame import FGBuildDescriptor
from Script.Engine import Default__KismetTextLibrary
from Script.Engine import Conv_StringToText
from Game.FactoryGame.Buildable.Factory.TradingPost.Widget_RewardProduct import ExecuteUbergraph_Widget_RewardProduct
from Script.Engine import EqualEqual_TextText
from Script.FactoryGame import Default__FGItemDescriptor
from Script.CoreUObject import Vector2D
from Script.SlateCore import SlateBrush
from Script.SlateCore import SlateColor
from Script.FactoryGame import ItemAmount
from Script.CoreUObject import LinearColor

class Widget_RewardProduct(Widget_SchematicRewardItem):
    mForcedCategoryIcon: Ptr[Texture]
    mProducts: List[ItemAmount] = [{'ItemClass': 'None', 'amount': 0}]
    
    def GetFirstProductItemClass(self):
        
        Item = None
        Item = self.mProducts[0]
        ItemClass = Item.ItemClass
    

    def IsValidRewardItem(self):
        IsValid = True
    

    def GetName(self):
        
        ItemClass = None
        self.GetFirstProductItemClass(Ref[ItemClass])
        ReturnValue: FText = Default__FGItemDescriptor.GetItemName(ItemClass)
        ReturnValue_0: FText = ReturnValue
    

    def GetIcon(self):
        
        ItemClass = None
        self.GetFirstProductItemClass(Ref[ItemClass])
        ReturnValue: Ptr[Texture2D] = Default__FGItemDescriptor.GetBigIcon(ItemClass)
        SlateBrush1.ImageSize = Vector2D(X = 128, Y = 128)
        SlateBrush1.Margin = Margin(Left = 0, Top = 0, Right = 0, Bottom = 0)
        SlateBrush1.TintColor = SlateColor(SpecifiedColor = LinearColor(R = 1, G = 1, B = 1, A = 1), ColorUseRule = 0)
        SlateBrush1.ResourceObject = ReturnValue
        SlateBrush1.DrawAs = 3
        SlateBrush1.Tiling = 0
        SlateBrush1.Mirroring = 0
        self.mBigIconBrush = SlateBrush1
        
        ItemClass = None
        self.GetFirstProductItemClass(Ref[ItemClass])
        
        ItemClass1 = None
        self.GetFirstProductItemClass(Ref[ItemClass1])
        ReturnValue = Default__FGItemDescriptor.GetBigIcon(ItemClass)
        Descriptor: TSubclassOf[FGBuildDescriptor] = ClassCast[FGBuildDescriptor](ItemClass1)
        bSuccess: bool = Descriptor
        SlateBrush.ImageSize = Vector2D(X = 256, Y = 256)
        SlateBrush.Margin = Margin(Left = 0, Top = 0, Right = 0, Bottom = 0)
        SlateBrush.TintColor = SlateColor(SpecifiedColor = LinearColor(R = 1, G = 1, B = 1, A = 1), ColorUseRule = 0)
        SlateBrush.ResourceObject = ReturnValue
        SlateBrush.DrawAs = 3
        SlateBrush.Tiling = 0
        SlateBrush.Mirroring = 0
        Variable: bool = bSuccess
        SlateBrush1.ImageSize = Vector2D(X = 128, Y = 128)
        SlateBrush1.Margin = Margin(Left = 0, Top = 0, Right = 0, Bottom = 0)
        SlateBrush1.TintColor = SlateColor(SpecifiedColor = LinearColor(R = 1, G = 1, B = 1, A = 1), ColorUseRule = 0)
        SlateBrush1.ResourceObject = ReturnValue
        SlateBrush1.DrawAs = 3
        SlateBrush1.Tiling = 0
        SlateBrush1.Mirroring = 0
        
        switch = {
            False: SlateBrush1,
            True: SlateBrush
        }
        ReturnValue_0: SlateBrush = switch.get(Variable, None)
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_RewardProduct(10)
    

    def ExecuteUbergraph_Widget_RewardProduct(self):
        self.Construct()
        
        ItemClass1 = None
        self.GetFirstProductItemClass(Ref[ItemClass1])
        self.SetCategoryTexture(ItemClass1)
        ReturnValue: FText = Default__KismetTextLibrary.Conv_StringToText("")
        
        self.mTitle = None
        ReturnValue_0: bool = Default__KismetTextLibrary.EqualEqual_TextText(Ref[self.mTitle], Ref[ReturnValue])
        if not ReturnValue_0:
            goto('L319')
        
        ItemClass = None
        self.GetFirstProductItemClass(Ref[ItemClass])
        ReturnValue_1: FText = Default__FGItemDescriptor.GetItemName(ItemClass)
        self.TextBlock_0.SetText(ReturnValue_1)
        # Label 319
        ReturnValue_2: SlateBrush = self.GetIcon()
        
        self.mRecipeIcon.SetBrush(Ref[ReturnValue_2])
        ReturnValue_3: bool = Default__KismetSystemLibrary.IsValid(self.mForcedCategoryIcon)
        if not ReturnValue_3:
            goto('L925')
        SlateBrush1.ImageSize = Vector2D(X = 20, Y = 20)
        SlateBrush1.Margin = self.mRewardCategoryIcon.Brush.Margin
        SlateBrush1.TintColor = self.mRewardCategoryIcon.Brush.TintColor
        SlateBrush1.ResourceObject = self.mForcedCategoryIcon
        SlateBrush1.DrawAs = self.mRewardCategoryIcon.Brush.DrawAs
        SlateBrush1.Tiling = self.mRewardCategoryIcon.Brush.Tiling
        SlateBrush1.Mirroring = self.mRewardCategoryIcon.Brush.Mirroring
        
        SlateBrush1 = None
        self.mRewardCategoryIcon.SetBrush(Ref[SlateBrush1])
        # End
        # Label 925
        SlateBrush.ImageSize = Vector2D(X = 20, Y = 20)
        SlateBrush.Margin = self.mRewardCategoryIcon.Brush.Margin
        SlateBrush.TintColor = self.mRewardCategoryIcon.Brush.TintColor
        SlateBrush.ResourceObject = self.mCategoryIconTexture
        SlateBrush.DrawAs = self.mRewardCategoryIcon.Brush.DrawAs
        SlateBrush.Tiling = self.mRewardCategoryIcon.Brush.Tiling
        SlateBrush.Mirroring = self.mRewardCategoryIcon.Brush.Mirroring
        
        SlateBrush = None
        self.mRewardCategoryIcon.SetBrush(Ref[SlateBrush])
    
