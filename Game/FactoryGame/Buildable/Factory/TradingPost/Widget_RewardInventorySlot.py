
from codegen.ue4_stub import *

from Script.Engine import Conv_StringToText
from Game.FactoryGame.Buildable.Factory.TradingPost.Widget_SchematicRewardItem import Widget_SchematicRewardItem
from Script.Engine import Conv_IntToString
from Script.SlateCore import SlateBrush
from Script.Engine import Default__KismetStringLibrary
from Game.FactoryGame.-Shared.Blueprint.BP_SchematicHelper import Default__BP_SchematicHelper
from Game.FactoryGame.Buildable.Factory.TradingPost.Widget_RewardInventorySlot import ExecuteUbergraph_Widget_RewardInventorySlot
from Script.Engine import Concat_StrStr
from Game.FactoryGame.Buildable.Factory.TradingPost.Widget_SchematicRewardItem import Construct
from Script.Engine import Default__KismetTextLibrary

class Widget_RewardInventorySlot(Widget_SchematicRewardItem):
    mInventorySlotBrush: SlateBrush = Namespace(DrawAs=3, ImageSize={'X': 256, 'Y': 256}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$AssetPath': '/Game/FactoryGame/Interface/UI/Assets/Shared/ThumbsUp_256.ThumbsUp_256'}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    mCategoryIconTexture = Namespace(AssetPath='/Game/FactoryGame/Buildable/Factory/TradingPost/UI/RecipeIcons/Recipe_Icon_Upgrade.Recipe_Icon_Upgrade')
    mBigIconBrush = Namespace(DrawAs=3, ImageSize={'X': 256, 'Y': 256}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$AssetPath': '/Game/FactoryGame/Interface/UI/Assets/Shared/ThumbsUp_256.ThumbsUp_256'}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    mTitle = NSLOCTEXT("", "4C3B58FB4648103148D31FB0D3FCEBD1", "Inventory Slot")
    mDescription = NSLOCTEXT("", "81C7F2A0496E4AB15640EF9936B7743E", "This reward will give you an inventory slot")
    Visibility = ESlateVisibility::Collapsed
    
    def IsValidRewardItem(self):
        IsValid = True
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_RewardInventorySlot(10)
    

    def ExecuteUbergraph_Widget_RewardInventorySlot(self):
        self.Construct()
        
        self.mRecipeIcon.SetBrush(Ref[self.mInventorySlotBrush])
        
        numSlots = None
        Default__BP_SchematicHelper.GetNumInventorySlotsUnlocked(self.mSchematicClass, self, Ref[numSlots])
        ReturnValue: FString = Default__KismetStringLibrary.Conv_IntToString(numSlots)
        ReturnValue_0: FString = Default__KismetStringLibrary.Concat_StrStr("+", ReturnValue)
        ReturnValue1: FString = Default__KismetStringLibrary.Concat_StrStr(ReturnValue_0, " Inventory Slots")
        ReturnValue_1: FText = Default__KismetTextLibrary.Conv_StringToText(ReturnValue1)
        self.mTitle = ReturnValue_1
    
