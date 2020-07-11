
from codegen.ue4_stub import *

from Game.FactoryGame.Buildable.Factory.TradingPost.Widget_SchematicRewardItem import Construct
from Game.FactoryGame.Buildable.Factory.TradingPost.Widget_RewardMap import ExecuteUbergraph_Widget_RewardMap
from Script.SlateCore import SlateBrush
from Game.FactoryGame.Buildable.Factory.TradingPost.Widget_SchematicRewardItem import Widget_SchematicRewardItem

class Widget_RewardMap(Widget_SchematicRewardItem):
    mMapBrush: SlateBrush = Namespace(DrawAs=3, ImageSize={'X': 256, 'Y': 256}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$AssetPath': '/Game/FactoryGame/Interface/UI/Assets/Shared/Map_Icon.Map_Icon'}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    mCategoryIconTexture = Namespace(AssetPath='/Game/FactoryGame/Buildable/Factory/TradingPost/UI/RecipeIcons/Recipe_Icon_Map.Recipe_Icon_Map')
    mBigIconBrush = Namespace(DrawAs=3, ImageSize={'X': 256, 'Y': 256}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$AssetPath': '/Game/FactoryGame/Interface/UI/Assets/Shared/Map_Icon.Map_Icon'}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    mTitle = NSLOCTEXT("", "E40B5E024B6710195C0EB5820F99D370", "Map")
    mDescription = NSLOCTEXT("", "9EC093CF4E57F12A9446B2AA5995D35D", "This reward will give you a map that you can access whenever you want")
    Visibility = ESlateVisibility::Collapsed
    
    def GetName(self):
        ReturnValue = self.mTitle
    

    def GetIcon(self):
        ReturnValue = self.mMapBrush
    

    def IsValidRewardItem(self):
        IsValid = True
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_RewardMap(10)
    

    def ExecuteUbergraph_Widget_RewardMap(self):
        self.Construct()
        
        self.mRecipeIcon.SetBrush(Ref[self.mMapBrush])
    
