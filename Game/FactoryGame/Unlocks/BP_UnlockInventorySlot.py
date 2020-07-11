
from codegen.ue4_stub import *

from Script.FactoryGame import FGStingerWidgetRewardData
from Script.FactoryGame import GetNumInventorySlotsToUnlock
from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import SetTextPropertyByName
from Script.UMG import UserWidget
from Script.Engine import FormatArgumentData
from Game.FactoryGame.Buildable.Factory.TradingPost.Widget_RewardInventorySlot import Widget_RewardInventorySlot
from Script.UMG import Create
from Script.Engine import SetClassPropertyByName
from Script.FactoryGame import FGUnlockInventorySlot
from Game.FactoryGame.Interface.UI.Assets.Shared.ThumbsUp_64 import ThumbsUp_64
from Script.Engine import Format
from Script.Engine import SetObjectPropertyByName
from Game.FactoryGame.Unlocks.FUnlockDataStruct import FUnlockDataStruct
from Script.UMG import Default__WidgetBlueprintLibrary
from Script.Engine import Default__KismetTextLibrary
from Game.FactoryGame.Unlocks.RewardData.RewardData_GeneralUpgrade import RewardData_GeneralUpgrade

class BP_UnlockInventorySlot(FGUnlockInventorySlot):
    
    
    def GetUnlockDataStruct(self):
        ReturnValue: int32 = self.GetNumInventorySlotsToUnlock()
        ReturnValue1: int32 = self.GetNumInventorySlotsToUnlock()
        FormatArgumentData.ArgumentName = "amount"
        FormatArgumentData.ArgumentValueType = 0
        FormatArgumentData.ArgumentValue = 
        FormatArgumentData.ArgumentValueInt = ReturnValue1
        FormatArgumentData.ArgumentValueFloat = 0
        FormatArgumentData.ArgumentValueGender = 0
        ReturnValue_0: bool = ReturnValue1 > 1
        Array: List[FormatArgumentData] = [FormatArgumentData]
        Variable: bool = ReturnValue_0
        ReturnValue_1: FText = Default__KismetTextLibrary.Format("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 370, 'Value': '{amount} Inventory Slot'}", Array)
        FormatArgumentData1.ArgumentName = "text"
        FormatArgumentData1.ArgumentValueType = 4
        FormatArgumentData1.ArgumentValue = ReturnValue_1
        FormatArgumentData1.ArgumentValueInt = 0
        FormatArgumentData1.ArgumentValueFloat = 0
        FormatArgumentData1.ArgumentValueGender = 0
        Array1: List[FormatArgumentData] = [FormatArgumentData1]
        ReturnValue1_0: FText = Default__KismetTextLibrary.Format("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 703, 'Value': '{text}s'}", Array1)
        
        switch = {
            False: ReturnValue_1,
            True: ReturnValue1_0
        }
        FUnlockDataStruct.UnlockName_2_490383D6421D4A92D86E1F835769488A = switch.get(Variable, None)
        FUnlockDataStruct.UnlockIcon_9_3E3B124C41C68907A6EB9FAD36C04BC4 = ThumbsUp_64
        FUnlockDataStruct.UnlockAmount_13_F32234CC46ECA4C99973A28AA05BE30E = ReturnValue
        FUnlockDataStruct.UnlockStructIndex_34_716E881C402D058998F7CDA17E1E4BF2 = 0
        FUnlockDataStruct.Unlock_29_06E6D017481991B0E94072A4F21FCC03 = self
        Array2: List[FUnlockDataStruct] = [FUnlockDataStruct]
        UnlockDataStruct = Array2
    

    def GetStingerWidgetRewardData(self):
        Set: Set[TSubclassOf[FGStingerWidgetRewardData]] = [RewardData_GeneralUpgrade]
        StingerRewardTypes = Set
    

    def GetUnlockRewardWidgets(self):
        ReturnValue: Ptr[Widget_RewardInventorySlot] = Default__WidgetBlueprintLibrary.Create(self, Widget_RewardInventorySlot, OwningPlayer)
        Default__KismetSystemLibrary.SetClassPropertyByName(ReturnValue, "mSchematicClass", SchematicClass)
        Default__KismetSystemLibrary.SetObjectPropertyByName(ReturnValue, "mTradingPostWidget", TradingPostWidget)
        Variable1: Const[FText] = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 207, 'Value': 'Inventory Slots'}"
        
        Default__KismetSystemLibrary.SetTextPropertyByName(ReturnValue, "mTitle", Ref[Variable1])
        Variable: Const[FText] = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 343, 'Value': 'Upgrades the Pocket Dimension with extra Inventory Slots.'}"
        
        Default__KismetSystemLibrary.SetTextPropertyByName(ReturnValue, "mDescription", Ref[Variable])
        Array: List[Ptr[UserWidget]] = [ReturnValue]
        Widgets = Array
    
