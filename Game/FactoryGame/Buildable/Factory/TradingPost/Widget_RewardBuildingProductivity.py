
from codegen.ue4_stub import *

from Game.FactoryGame.Buildable.Factory.TradingPost.Widget_RewardBuildingProductivity import ExecuteUbergraph_Widget_RewardBuildingProductivity
from Game.FactoryGame.Buildable.Factory.TradingPost.Widget_SchematicRewardItem import Construct
from Script.SlateCore import SlateBrush
from Game.FactoryGame.Buildable.Factory.TradingPost.Widget_SchematicRewardItem import Widget_SchematicRewardItem

class Widget_RewardBuildingProductivity(Widget_SchematicRewardItem):
    mProductivityBrush: SlateBrush = Namespace(DrawAs=3, ImageSize={'X': 64, 'Y': 64}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$AssetPath': '/Game/FactoryGame/Interface/UI/Assets/Shared/ThumbsUp_64.ThumbsUp_64'}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    mCategoryIconTexture = Namespace(AssetPath='/Game/FactoryGame/Buildable/Factory/TradingPost/UI/RecipeIcons/Recipe_Icon_Upgrade.Recipe_Icon_Upgrade')
    mBigIconBrush = Namespace(DrawAs=3, ImageSize={'X': 256, 'Y': 256}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$AssetPath': '/Game/FactoryGame/Interface/UI/Assets/Shared/ThumbsUp_256.ThumbsUp_256'}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    mTitle = NSLOCTEXT("", "A7BDFFD74E09A9B367FE69AD205D368F", "Productivity Display")
    mDescription = NSLOCTEXT("", "1B763E334EB824D22A0884B8C4598E95", "With this upgrade you can see the efficiency of each building")
    Visibility = ESlateVisibility::Collapsed
    
    def IsValidRewardItem(self):
        IsValid = True
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_RewardBuildingProductivity(10)
    

    def ExecuteUbergraph_Widget_RewardBuildingProductivity(self):
        self.Construct()
        
        self.mRecipeIcon.SetBrush(Ref[self.mProductivityBrush])
    
