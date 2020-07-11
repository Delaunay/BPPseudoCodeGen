
from codegen.ue4_stub import *

from Script.FactoryGame import FGStingerWidgetRewardData
from Game.FactoryGame.Interface.UI.Assets.Shared.Map_Icon import Map_Icon
from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import SetTextPropertyByName
from Script.UMG import Create
from Script.Engine import SetClassPropertyByName
from Script.Engine import SetObjectPropertyByName
from Game.FactoryGame.Unlocks.FUnlockDataStruct import FUnlockDataStruct
from Script.UMG import Default__WidgetBlueprintLibrary
from Game.FactoryGame.Buildable.Factory.TradingPost.Widget_RewardMap import Widget_RewardMap
from Script.FactoryGame import FGUnlockMap
from Script.UMG import UserWidget
from Game.FactoryGame.Unlocks.RewardData.RewardData_GeneralUpgrade import RewardData_GeneralUpgrade

class BP_UnlockMap(FGUnlockMap):
    
    
    def GetUnlockDataStruct(self):
        FUnlockDataStruct.UnlockName_2_490383D6421D4A92D86E1F835769488A = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 29, 'Value': 'Map'}"
        FUnlockDataStruct.UnlockIcon_9_3E3B124C41C68907A6EB9FAD36C04BC4 = Map_Icon
        FUnlockDataStruct.UnlockAmount_13_F32234CC46ECA4C99973A28AA05BE30E = 0
        FUnlockDataStruct.UnlockStructIndex_34_716E881C402D058998F7CDA17E1E4BF2 = 0
        FUnlockDataStruct.Unlock_29_06E6D017481991B0E94072A4F21FCC03 = self
        Array: List[FUnlockDataStruct] = [FUnlockDataStruct]
        UnlockDataStruct = Array
    

    def GetStingerWidgetRewardData(self):
        Set: Set[TSubclassOf[FGStingerWidgetRewardData]] = [RewardData_GeneralUpgrade]
        StingerRewardTypes = Set
    

    def GetUnlockRewardWidgets(self):
        ReturnValue: Ptr[Widget_RewardMap] = Default__WidgetBlueprintLibrary.Create(self, Widget_RewardMap, OwningPlayer)
        Default__KismetSystemLibrary.SetClassPropertyByName(ReturnValue, "mSchematicClass", SchematicClass)
        Default__KismetSystemLibrary.SetObjectPropertyByName(ReturnValue, "mTradingPostWidget", TradingPostWidget)
        Variable1: Const[FText] = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 207, 'Value': 'Map'}"
        
        Default__KismetSystemLibrary.SetTextPropertyByName(ReturnValue, "mTitle", Ref[Variable1])
        Variable: Const[FText] = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 331, 'Value': 'This reward will give you a map that you can access whenever you want'}"
        
        Default__KismetSystemLibrary.SetTextPropertyByName(ReturnValue, "mDescription", Ref[Variable])
        Array: List[Ptr[UserWidget]] = [ReturnValue]
        Widgets = Array
    
