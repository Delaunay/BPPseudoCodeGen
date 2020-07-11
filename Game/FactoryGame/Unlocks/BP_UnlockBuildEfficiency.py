
from codegen.ue4_stub import *

from Script.FactoryGame import FGStingerWidgetRewardData
from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import SetTextPropertyByName
from Script.FactoryGame import FGUnlockBuildEfficiency
from Script.UMG import Create
from Game.FactoryGame.Unlocks.RewardData.RewardData_GeneralUpgrade import RewardData_GeneralUpgrade
from Script.Engine import SetClassPropertyByName
from Game.FactoryGame.Interface.UI.Assets.Shared.ThumbsUp_64 import ThumbsUp_64
from Script.Engine import SetObjectPropertyByName
from Game.FactoryGame.Unlocks.FUnlockDataStruct import FUnlockDataStruct
from Script.UMG import Default__WidgetBlueprintLibrary
from Script.UMG import UserWidget
from Game.FactoryGame.Buildable.Factory.TradingPost.Widget_RewardBuildingProductivity import Widget_RewardBuildingProductivity

class BP_UnlockBuildEfficiency(FGUnlockBuildEfficiency):
    
    
    def GetUnlockDataStruct(self):
        FUnlockDataStruct.UnlockName_2_490383D6421D4A92D86E1F835769488A = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 29, 'Value': 'Building Efficiency Stat'}"
        FUnlockDataStruct.UnlockIcon_9_3E3B124C41C68907A6EB9FAD36C04BC4 = ThumbsUp_64
        FUnlockDataStruct.UnlockAmount_13_F32234CC46ECA4C99973A28AA05BE30E = 0
        FUnlockDataStruct.UnlockStructIndex_34_716E881C402D058998F7CDA17E1E4BF2 = 0
        FUnlockDataStruct.Unlock_29_06E6D017481991B0E94072A4F21FCC03 = self
        Array: List[FUnlockDataStruct] = [FUnlockDataStruct]
        UnlockDataStruct = Array
    

    def GetStingerWidgetRewardData(self):
        Set: Set[TSubclassOf[FGStingerWidgetRewardData]] = [RewardData_GeneralUpgrade]
        StingerRewardTypes = Set
    

    def GetUnlockRewardWidgets(self):
        ReturnValue: Ptr[Widget_RewardBuildingProductivity] = Default__WidgetBlueprintLibrary.Create(self, Widget_RewardBuildingProductivity, OwningPlayer)
        Default__KismetSystemLibrary.SetClassPropertyByName(ReturnValue, "mSchematicClass", SchematicClass)
        Default__KismetSystemLibrary.SetObjectPropertyByName(ReturnValue, "mTradingPostWidget", TradingPostWidget)
        Variable1: Const[FText] = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 207, 'Value': 'Productivity Display'}"
        
        Default__KismetSystemLibrary.SetTextPropertyByName(ReturnValue, "mTitle", Ref[Variable1])
        Variable: Const[FText] = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 348, 'Value': 'With this upgrade you can see the efficiency of each building'}"
        
        Default__KismetSystemLibrary.SetTextPropertyByName(ReturnValue, "mDescription", Ref[Variable])
        Array: List[Ptr[UserWidget]] = [ReturnValue]
        Widgets = Array
    
