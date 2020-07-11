
from codegen.ue4_stub import *

from Script.FactoryGame import FGStingerWidgetRewardData
from Script.Engine import SetTextPropertyByName
from Script.Engine import Texture2D
from Script.FactoryGame import FGResourceDescriptor
from Script.Engine import SetClassPropertyByName
from Game.FactoryGame.Buildable.Factory.TradingPost.Widget_RewardProduct import Widget_RewardProduct
from Script.Engine import SetObjectPropertyByName
from Script.Engine import Default__KismetSystemLibrary
from Game.FactoryGame.Unlocks.RewardData.RewardData_ScannableResource import RewardData_ScannableResource
from Script.Engine import Default__KismetArrayLibrary
from Script.Engine import FormatArgumentData
from Script.FactoryGame import GetItemName
from Script.FactoryGame import GetBigIcon
from Script.UMG import Default__WidgetBlueprintLibrary
from Script.FactoryGame import FGUnlockScannableResource
from Game.FactoryGame.Buildable.Factory.TradingPost.UI.RecipeIcons.Recipe_Icon_Scanner import Recipe_Icon_Scanner
from Script.FactoryGame import GetResourcesToAddToScanner
from Script.Engine import Default__KismetTextLibrary
from Script.Engine import Format
from Script.Engine import SetArrayPropertyByName
from Script.FactoryGame import Default__FGItemDescriptor
from Script.UMG import Create
from Script.FactoryGame import ItemAmount

class BP_UnlockScannableResource(FGUnlockScannableResource):
    
    
    def GetUnlockDataStruct(self):
        ExecutionFlow.Push("L1082")
        Variable: int32 = 0
        Variable_0: int32 = 0
        # Label 51
        ReturnValue: List[TSubclassOf[FGResourceDescriptor]] = self.GetResourcesToAddToScanner()
        
        ReturnValue_0: int32 = len(ReturnValue)
        ReturnValue_1: bool = Variable <= ReturnValue_0
        if not ReturnValue_1:
            goto('L976')
        Variable_0 = Variable
        ExecutionFlow.Push("L1008")
        ReturnValue = self.GetResourcesToAddToScanner()
        
        Item = None
        Item = ReturnValue[Variable_0]
        ReturnValue_2: FText = Default__FGItemDescriptor.GetItemName(Item)
        FormatArgumentData.ArgumentName = "item"
        FormatArgumentData.ArgumentValueType = 4
        FormatArgumentData.ArgumentValue = ReturnValue_2
        FormatArgumentData.ArgumentValueInt = 0
        FormatArgumentData.ArgumentValueFloat = 0
        FormatArgumentData.ArgumentValueGender = 0
        Array: List[FormatArgumentData] = [FormatArgumentData]
        ReturnValue_3: Ptr[Texture2D] = Default__FGItemDescriptor.GetBigIcon(Item)
        ReturnValue_4: FText = Default__KismetTextLibrary.Format("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 681, 'Value': 'Scannable Resource: {item}'}", Array)
        FUnlockDataStruct.UnlockName_2_490383D6421D4A92D86E1F835769488A = ReturnValue_4
        FUnlockDataStruct.UnlockIcon_9_3E3B124C41C68907A6EB9FAD36C04BC4 = ReturnValue_3
        FUnlockDataStruct.UnlockAmount_13_F32234CC46ECA4C99973A28AA05BE30E = 0
        FUnlockDataStruct.UnlockStructIndex_34_716E881C402D058998F7CDA17E1E4BF2 = Variable_0
        FUnlockDataStruct.Unlock_29_06E6D017481991B0E94072A4F21FCC03 = self
        
        FUnlockDataStruct = None
        ReturnValue_5: int32 = localUnlockDataStruct.append(FUnlockDataStruct)
        goto(ExecutionFlow.Pop())
        # Label 976
        UnlockDataStruct = localUnlockDataStruct
        # End
        # Label 1008
        ReturnValue_6: int32 = Variable + 1
        Variable = ReturnValue_6
        goto('L51')
    

    def GetStingerWidgetRewardData(self):
        Set: Set[TSubclassOf[FGStingerWidgetRewardData]] = [RewardData_ScannableResource]
        StingerRewardTypes = Set
    

    def GetUnlockRewardWidgets(self):
        ExecutionFlow.Push("L1993")
        Variable: int32 = 0
        Variable_0: int32 = 0
        # Label 51
        ReturnValue: List[TSubclassOf[FGResourceDescriptor]] = self.GetResourcesToAddToScanner()
        
        ReturnValue_0: int32 = len(ReturnValue)
        ReturnValue_1: bool = Variable <= ReturnValue_0
        if not ReturnValue_1:
            goto('L1887')
        Variable_0 = Variable
        ExecutionFlow.Push("L1919")
        ReturnValue_2: Ptr[Widget_RewardProduct] = Default__WidgetBlueprintLibrary.Create(self, Widget_RewardProduct, OwningPlayer)
        Default__KismetSystemLibrary.SetObjectPropertyByName(ReturnValue_2, "mForcedCategoryIcon", Recipe_Icon_Scanner)
        ReturnValue = self.GetResourcesToAddToScanner()
        
        Item = None
        Item = ReturnValue[Variable_0]
        ItemAmount.ItemClass = Item
        ItemAmount.amount = 0
        Array: List[ItemAmount] = [ItemAmount]
        
        Default__KismetArrayLibrary.SetArrayPropertyByName(ReturnValue_2, "mProducts", Ref[Array])
        Default__KismetSystemLibrary.SetClassPropertyByName(ReturnValue_2, "mSchematicClass", SchematicClass)
        Default__KismetSystemLibrary.SetObjectPropertyByName(ReturnValue_2, "mTradingPostWidget", TradingPostWidget)
        ReturnValue = self.GetResourcesToAddToScanner()
        
        Item = None
        Item = ReturnValue[Variable_0]
        ReturnValue_3: FText = Default__FGItemDescriptor.GetItemName(Item)
        FormatArgumentData.ArgumentName = "Item"
        FormatArgumentData.ArgumentValueType = 4
        FormatArgumentData.ArgumentValue = ReturnValue_3
        FormatArgumentData.ArgumentValueInt = 0
        FormatArgumentData.ArgumentValueFloat = 0
        FormatArgumentData.ArgumentValueGender = 0
        Array1: List[FormatArgumentData] = [FormatArgumentData]
        ReturnValue_4: FText = Default__KismetTextLibrary.Format("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 1110, 'Value': 'Scanner Update: {Item}'}", Array1)
        
        Default__KismetSystemLibrary.SetTextPropertyByName(ReturnValue_2, "mTitle", Ref[ReturnValue_4])
        ReturnValue = self.GetResourcesToAddToScanner()
        
        Item = None
        Item = ReturnValue[Variable_0]
        ReturnValue_3 = Default__FGItemDescriptor.GetItemName(Item)
        FormatArgumentData1.ArgumentName = "Item"
        FormatArgumentData1.ArgumentValueType = 4
        FormatArgumentData1.ArgumentValue = ReturnValue_3
        FormatArgumentData1.ArgumentValueInt = 0
        FormatArgumentData1.ArgumentValueFloat = 0
        FormatArgumentData1.ArgumentValueGender = 0
        Array2: List[FormatArgumentData] = [FormatArgumentData1]
        ReturnValue1: FText = Default__KismetTextLibrary.Format("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 1651, 'Value': 'Allows you to scan for {Item} with the Resource Scanner.'}", Array2)
        
        Default__KismetSystemLibrary.SetTextPropertyByName(ReturnValue_2, "mDescription", Ref[ReturnValue1])
        
        ReturnValue_5: int32 = RewardWidgets.append(ReturnValue_2)
        goto(ExecutionFlow.Pop())
        # Label 1887
        Widgets = RewardWidgets
        # End
        # Label 1919
        ReturnValue_6: int32 = Variable + 1
        Variable = ReturnValue_6
        goto('L51')
    
