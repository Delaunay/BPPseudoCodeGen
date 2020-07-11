
from codegen.ue4_stub import *

from Script.FactoryGame import FGStingerWidgetRewardData
from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import SetTextPropertyByName
from Script.UMG import UserWidget
from Script.FactoryGame import FGUnlockArmEquipmentSlot
from Script.Engine import FormatArgumentData
from Script.UMG import Create
from Script.Engine import SetClassPropertyByName
from Game.FactoryGame.Interface.UI.Assets.Shared.ThumbsUp_64 import ThumbsUp_64
from Script.Engine import Format
from Script.FactoryGame import GetNumArmEquipmentSlotsToUnlock
from Script.Engine import SetObjectPropertyByName
from Game.FactoryGame.Unlocks.FUnlockDataStruct import FUnlockDataStruct
from Script.UMG import Default__WidgetBlueprintLibrary
from Game.FactoryGame.Buildable.Factory.TradingPost.Widget_RewardArmEquipmentSlot import Widget_RewardArmEquipmentSlot
from Script.Engine import Default__KismetTextLibrary
from Game.FactoryGame.Unlocks.RewardData.RewardData_GeneralUpgrade import RewardData_GeneralUpgrade

class BP_UnlockArmEquipmentSlot(FGUnlockArmEquipmentSlot):
    
    
    def GetUnlockDataStruct(self):
        ReturnValue: int32 = self.GetNumArmEquipmentSlotsToUnlock()
        ReturnValue1: int32 = self.GetNumArmEquipmentSlotsToUnlock()
        ReturnValue_0: bool = ReturnValue1 > 1
        FormatArgumentData.ArgumentName = "amount"
        FormatArgumentData.ArgumentValueType = 0
        FormatArgumentData.ArgumentValue = 
        FormatArgumentData.ArgumentValueInt = ReturnValue1
        FormatArgumentData.ArgumentValueFloat = 0
        FormatArgumentData.ArgumentValueGender = 0
        Variable: bool = ReturnValue_0
        Array: List[FormatArgumentData] = [FormatArgumentData]
        ReturnValue_1: FText = Default__KismetTextLibrary.Format("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 370, 'Value': '{amount} Hand Slot'}", Array)
        FormatArgumentData1.ArgumentName = "text"
        FormatArgumentData1.ArgumentValueType = 4
        FormatArgumentData1.ArgumentValue = ReturnValue_1
        FormatArgumentData1.ArgumentValueInt = 0
        FormatArgumentData1.ArgumentValueFloat = 0
        FormatArgumentData1.ArgumentValueGender = 0
        Array1: List[FormatArgumentData] = [FormatArgumentData1]
        ReturnValue1_0: FText = Default__KismetTextLibrary.Format("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 698, 'Value': '{text}s'}", Array1)
        
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
        ReturnValue: Ptr[Widget_RewardArmEquipmentSlot] = Default__WidgetBlueprintLibrary.Create(self, Widget_RewardArmEquipmentSlot, OwningPlayer)
        Default__KismetSystemLibrary.SetClassPropertyByName(ReturnValue, "mSchematicClass", SchematicClass)
        Default__KismetSystemLibrary.SetObjectPropertyByName(ReturnValue, "mTradingPostWidget", TradingPostWidget)
        Variable1: Const[FText] = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 207, 'Value': 'Hand Slot'}"
        
        Default__KismetSystemLibrary.SetTextPropertyByName(ReturnValue, "mTitle", Ref[Variable1])
        Variable: Const[FText] = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 337, 'Value': 'Upgrades the Toolbelt with an extra Hand Equipment Slot, providing easier access to multiple tools and weapons.'}"
        
        Default__KismetSystemLibrary.SetTextPropertyByName(ReturnValue, "mDescription", Ref[Variable])
        Array: List[Ptr[UserWidget]] = [ReturnValue]
        Widgets = Array
    
