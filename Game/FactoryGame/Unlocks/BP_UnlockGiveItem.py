
from codegen.ue4_stub import *

from Script.FactoryGame import FGUnlockGiveItem
from Script.Engine import Texture2D
from Script.Engine import Default__KismetArrayLibrary
from Script.FactoryGame import Default__FGItemDescriptor
from Script.FactoryGame import GetItemName
from Script.FactoryGame import GetItemsToGive
from Script.FactoryGame import ItemAmount
from Script.FactoryGame import GetSmallIcon

class BP_UnlockGiveItem(FGUnlockGiveItem):
    
    
    def GetStingerWidgetRewardData(self):
        StingerRewardTypes = Set[ClassProperty /Game/FactoryGame/Unlocks/BP_UnlockGiveItem.BP_UnlockGiveItem_C:GetStingerWidgetRewardData.StingerRewardTypes.StingerRewardTypes]([])
    

    def GetUnlockRewardWidgets(self):
        Widgets = List[ObjectProperty /Game/FactoryGame/Unlocks/BP_UnlockGiveItem.BP_UnlockGiveItem_C:GetUnlockRewardWidgets.Widgets.Widgets]([])
    

    def GetUnlockDataStruct(self):
        ExecutionFlow.Push("L773")
        Variable: int32 = 0
        Variable_0: int32 = 0
        # Label 51
        ReturnValue: List[ItemAmount] = self.GetItemsToGive()
        
        ReturnValue_0: int32 = len(ReturnValue)
        ReturnValue_1: bool = Variable <= ReturnValue_0
        if not ReturnValue_1:
            goto('L667')
        Variable_0 = Variable
        ExecutionFlow.Push("L699")
        ReturnValue = self.GetItemsToGive()
        
        Item = None
        Item = ReturnValue[Variable_0]
        ReturnValue_2: Ptr[Texture2D] = Default__FGItemDescriptor.GetSmallIcon(Item.ItemClass)
        ReturnValue_3: FText = Default__FGItemDescriptor.GetItemName(Item.ItemClass)
        FUnlockDataStruct.UnlockName_2_490383D6421D4A92D86E1F835769488A = ReturnValue_3
        FUnlockDataStruct.UnlockIcon_9_3E3B124C41C68907A6EB9FAD36C04BC4 = ReturnValue_2
        FUnlockDataStruct.UnlockAmount_13_F32234CC46ECA4C99973A28AA05BE30E = Item.amount
        FUnlockDataStruct.UnlockStructIndex_34_716E881C402D058998F7CDA17E1E4BF2 = 0
        FUnlockDataStruct.Unlock_29_06E6D017481991B0E94072A4F21FCC03 = self
        
        FUnlockDataStruct = None
        ReturnValue_4: int32 = localUnlockDataStruct.append(FUnlockDataStruct)
        goto(ExecutionFlow.Pop())
        # Label 667
        UnlockDataStruct = localUnlockDataStruct
        # End
        # Label 699
        ReturnValue_5: int32 = Variable + 1
        Variable = ReturnValue_5
        goto('L51')
    

    def IsRepeatPurchasesAllowed(self):
        ReturnValue = True
    
