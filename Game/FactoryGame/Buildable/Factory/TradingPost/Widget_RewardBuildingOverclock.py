
from codegen.ue4_stub import *

from Game.FactoryGame.Buildable.Factory.TradingPost.Widget_SchematicRewardItem import Construct
from Game.FactoryGame.Buildable.Factory.TradingPost.Widget_RewardBuildingOverclock import ExecuteUbergraph_Widget_RewardBuildingOverclock
from Script.SlateCore import SlateBrush
from Game.FactoryGame.Buildable.Factory.TradingPost.Widget_SchematicRewardItem import Widget_SchematicRewardItem

class Widget_RewardBuildingOverclock(Widget_SchematicRewardItem):
    mOverclockBrush: SlateBrush = Namespace(DrawAs=3, ImageSize={'X': 256, 'Y': 256}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$AssetPath': '/Game/FactoryGame/Interface/UI/Assets/Shared/Overclock_Icon.Overclock_Icon'}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    mCategoryIconTexture = Namespace(AssetPath='/Game/FactoryGame/Buildable/Factory/TradingPost/UI/RecipeIcons/Recipe_Icon_Upgrade.Recipe_Icon_Upgrade')
    mBigIconBrush = Namespace(DrawAs=3, ImageSize={'X': 256, 'Y': 256}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$AssetPath': '/Game/FactoryGame/Interface/UI/Assets/Shared/Overclock_Icon.Overclock_Icon'}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    mTitle = NSLOCTEXT("", "99C432064763578191DA96BD300357FB", "Overclock buildings")
    mDescription = NSLOCTEXT("", "9E0B73424D508EAC7898B69FF4CDAA45", "This upgrade unlocks new functionality that lets you overclock your factory buildings.")
    Visibility = ESlateVisibility::Collapsed
    
    def IsValidRewardItem(self):
        IsValid = True
    

    def GetName(self):
        ReturnValue = self.mTitle
    

    def GetIcon(self):
        ReturnValue = self.mOverclockBrush
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_RewardBuildingOverclock(10)
    

    def ExecuteUbergraph_Widget_RewardBuildingOverclock(self):
        self.Construct()
        
        self.mRecipeIcon.SetBrush(Ref[self.mOverclockBrush])
    
