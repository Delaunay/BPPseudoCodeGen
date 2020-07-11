
from codegen.ue4_stub import *

from Script.FactoryGame import FGEquipmentDescriptor
from Script.Engine import Texture2D
from Script.FactoryGame import FGResourceDescriptor
from Game.FactoryGame.Unlocks.RewardData.RewardData_Item import RewardData_Item
from Script.Engine import SetClassPropertyByName
from Game.FactoryGame.Buildable.Factory.TradingPost.Widget_RewardProduct import Widget_RewardProduct
from Script.Engine import SetObjectPropertyByName
from Script.FactoryGame import GetRecipesToUnlock
from Game.FactoryGame.Unlocks.RewardData.RewardData_Building import RewardData_Building
from Script.FactoryGame import GetProducts
from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import Default__KismetArrayLibrary
from Script.Engine import Set_Add
from Script.FactoryGame import GetItemName
from Script.FactoryGame import FGUnlockRecipe
from Script.UMG import Default__WidgetBlueprintLibrary
from Script.Engine import ClassIsChildOf
from Game.FactoryGame.Unlocks.RewardData.RewardData_Vehicle import RewardData_Vehicle
from Script.FactoryGame import GetSmallIcon
from Script.FactoryGame import FGVehicleDescriptor
from Script.FactoryGame import Default__FGRecipe
from Game.FactoryGame.Unlocks.RewardData.RewardData_Decor import RewardData_Decor
from Script.Engine import SetArrayPropertyByName
from Game.FactoryGame.Unlocks.RewardData.RewardData_Resource import RewardData_Resource
from Game.FactoryGame.Unlocks.RewardData.RewardData_Equipment import RewardData_Equipment
from Script.FactoryGame import Default__FGItemDescriptor
from Script.UMG import Create
from Script.FactoryGame import FGRecipe
from Script.Engine import Default__BlueprintSetLibrary
from Script.FactoryGame import ItemAmount
from Script.FactoryGame import FGDecorDescriptor
from Script.FactoryGame import FGBuildingDescriptor

class BP_UnlockRecipe(FGUnlockRecipe):
    
    
    def GetUnlockDataStruct(self):
        ExecutionFlow.Push("L1289")
        Variable: int32 = 0
        Variable1: int32 = 0
        # Label 51
        ReturnValue: List[TSubclassOf[FGRecipe]] = self.GetRecipesToUnlock()
        
        ReturnValue_0: int32 = len(ReturnValue)
        ReturnValue_1: bool = Variable <= ReturnValue_0
        if not ReturnValue_1:
            goto('L1109')
        Variable1 = Variable
        ExecutionFlow.Push("L1141")
        Variable1_0: int32 = 0
        Variable_0: int32 = 0
        # Label 268
        ReturnValue = self.GetRecipesToUnlock()
        
        Item = None
        Item = ReturnValue[Variable1]
        ReturnValue_2: List[ItemAmount] = Default__FGRecipe.GetProducts(Item, False)
        
        ReturnValue1: int32 = len(ReturnValue_2)
        ReturnValue1_0: bool = Variable1_0 <= ReturnValue1
        if not ReturnValue1_0:
           goto(ExecutionFlow.Pop())
        Variable_0 = Variable1_0
        ExecutionFlow.Push("L1215")
        ReturnValue = self.GetRecipesToUnlock()
        
        Item = None
        Item = ReturnValue[Variable1]
        ReturnValue_2 = Default__FGRecipe.GetProducts(Item, False)
        
        Item1 = None
        Item1 = ReturnValue_2[Variable_0]
        ReturnValue_3: Ptr[Texture2D] = Default__FGItemDescriptor.GetSmallIcon(Item1.ItemClass)
        ReturnValue_4: FText = Default__FGItemDescriptor.GetItemName(Item1.ItemClass)
        FUnlockDataStruct.UnlockName_2_490383D6421D4A92D86E1F835769488A = ReturnValue_4
        FUnlockDataStruct.UnlockIcon_9_3E3B124C41C68907A6EB9FAD36C04BC4 = ReturnValue_3
        FUnlockDataStruct.UnlockAmount_13_F32234CC46ECA4C99973A28AA05BE30E = 0
        FUnlockDataStruct.UnlockStructIndex_34_716E881C402D058998F7CDA17E1E4BF2 = Variable1
        FUnlockDataStruct.Unlock_29_06E6D017481991B0E94072A4F21FCC03 = self
        
        FUnlockDataStruct = None
        ReturnValue_5: int32 = localUnlockDataStruct.append(FUnlockDataStruct)
        goto(ExecutionFlow.Pop())
        # Label 1109
        UnlockDataStruct = localUnlockDataStruct
        # End
        # Label 1141
        ReturnValue_6: int32 = Variable + 1
        Variable = ReturnValue_6
        goto('L51')
        # Label 1215
        ReturnValue1_1: int32 = Variable1_0 + 1
        Variable1_0 = ReturnValue1_1
        goto('L268')
    

    def GetStingerWidgetRewardData(self):
        ExecutionFlow.Push("L1032")
        Variable: int32 = 0
        Variable_0: int32 = 0
        # Label 51
        ReturnValue: List[TSubclassOf[FGRecipe]] = self.GetRecipesToUnlock()
        
        ReturnValue_0: int32 = len(ReturnValue)
        ReturnValue_1: bool = Variable <= ReturnValue_0
        if not ReturnValue_1:
            goto('L852')
        Variable_0 = Variable
        ExecutionFlow.Push("L884")
        Variable1: int32 = 0
        Variable1_0: int32 = 0
        # Label 268
        ReturnValue = self.GetRecipesToUnlock()
        
        Item = None
        Item = ReturnValue[Variable_0]
        ReturnValue_2: List[ItemAmount] = Default__FGRecipe.GetProducts(Item, False)
        
        ReturnValue1: int32 = len(ReturnValue_2)
        ReturnValue1_0: bool = Variable1 <= ReturnValue1
        if not ReturnValue1_0:
           goto(ExecutionFlow.Pop())
        Variable1_0 = Variable1
        ExecutionFlow.Push("L958")
        ReturnValue = self.GetRecipesToUnlock()
        
        Item = None
        Item = ReturnValue[Variable_0]
        ReturnValue_2 = Default__FGRecipe.GetProducts(Item, False)
        
        Item1 = None
        Item1 = ReturnValue_2[Variable1_0]
        
        RewardData = None
        self.GetRewardTypeFromItemDescriptor(Item1.ItemClass, Ref[RewardData])
        
        RewardData = None
        Default__BlueprintSetLibrary.Set_Add(Ref[LocalStingerWidgetRewardData], Ref[RewardData])
        goto(ExecutionFlow.Pop())
        # Label 852
        StingerRewardTypes = LocalStingerWidgetRewardData
        # End
        # Label 884
        ReturnValue_3: int32 = Variable + 1
        Variable = ReturnValue_3
        goto('L51')
        # Label 958
        ReturnValue1_1: int32 = Variable1 + 1
        Variable1 = ReturnValue1_1
        goto('L268')
    

    def GetUnlockRewardWidgets(self):
        ExecutionFlow.Push("L794")
        Variable: int32 = 0
        Variable_0: int32 = 0
        # Label 51
        ReturnValue: List[TSubclassOf[FGRecipe]] = self.GetRecipesToUnlock()
        
        ReturnValue_0: int32 = len(ReturnValue)
        ReturnValue_1: bool = Variable <= ReturnValue_0
        if not ReturnValue_1:
            goto('L688')
        Variable_0 = Variable
        ExecutionFlow.Push("L720")
        ReturnValue_2: Ptr[Widget_RewardProduct] = Default__WidgetBlueprintLibrary.Create(self, Widget_RewardProduct, OwningPlayer)
        ReturnValue = self.GetRecipesToUnlock()
        
        Item = None
        Item = ReturnValue[Variable_0]
        ReturnValue_3: List[ItemAmount] = Default__FGRecipe.GetProducts(Item, False)
        
        Default__KismetArrayLibrary.SetArrayPropertyByName(ReturnValue_2, "mProducts", Ref[ReturnValue_3])
        Default__KismetSystemLibrary.SetClassPropertyByName(ReturnValue_2, "mSchematicClass", SchematicClass)
        Default__KismetSystemLibrary.SetObjectPropertyByName(ReturnValue_2, "mTradingPostWidget", TradingPostWidget)
        
        ReturnValue_4: int32 = RewardWidgets.append(ReturnValue_2)
        goto(ExecutionFlow.Pop())
        # Label 688
        Widgets = RewardWidgets
        # End
        # Label 720
        ReturnValue_5: int32 = Variable + 1
        Variable = ReturnValue_5
        goto('L51')
    

    def GetRewardTypeFromItemDescriptor(self, ItemDescriptorClass: TSubclassOf[FGItemDescriptor]):
        ReturnValue4: bool = ClassIsChildOf(ItemDescriptorClass, FGDecorDescriptor)
        if not ReturnValue4:
            goto('L76')
        RewardData = RewardData_Decor
        # End
        # Label 76
        ReturnValue3: bool = ClassIsChildOf(ItemDescriptorClass, FGVehicleDescriptor)
        if not ReturnValue3:
            goto('L152')
        RewardData = RewardData_Vehicle
        # End
        # Label 152
        ReturnValue2: bool = ClassIsChildOf(ItemDescriptorClass, FGEquipmentDescriptor)
        if not ReturnValue2:
            goto('L228')
        RewardData = RewardData_Equipment
        # End
        # Label 228
        ReturnValue1: bool = ClassIsChildOf(ItemDescriptorClass, FGResourceDescriptor)
        if not ReturnValue1:
            goto('L304')
        RewardData = RewardData_Resource
        # End
        # Label 304
        ReturnValue: bool = ClassIsChildOf(ItemDescriptorClass, FGBuildingDescriptor)
        if not ReturnValue:
            goto('L380')
        RewardData = RewardData_Building
        # End
        # Label 380
        RewardData = RewardData_Item
    
