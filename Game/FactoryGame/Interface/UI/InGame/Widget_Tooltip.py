
from codegen.ue4_stub import *

from Script.Engine import SetTextPropertyByName
from Script.FactoryGame import FGResourceDescriptor
from Script.Engine import Delay
from Script.Engine import SetClassPropertyByName
from Script.UMG import PanelSlot
from Script.UMG import AddChild
from Script.Engine import Not_PreBool
from Script.Engine import LatentActionInfo
from Script.Engine import Default__KismetSystemLibrary
from Script.FactoryGame import Get
from Script.Engine import PlayerController
from Script.Engine import Default__KismetArrayLibrary
from Script.Engine import FormatArgumentData
from Script.FactoryGame import GetItemName
from Script.UMG import PlayAnimation
from Game.FactoryGame.Interface.UI.InGame.Widget_Tooltip import ExecuteUbergraph_Widget_Tooltip
from Script.UMG import Default__WidgetBlueprintLibrary
from Script.Engine import Default__KismetTextLibrary
from Script.Engine import Conv_StringToText
from Script.FactoryGame import FGVehicleDescriptor
from Script.Engine import SetBoolPropertyByName
from Script.Engine import BooleanOR
from Script.FactoryGame import Default__FGRecipeManager
from Script.FactoryGame import Default__FGRecipe
from Script.Engine import Format
from Script.Engine import Default__KismetStringLibrary
from Script.UMG import WidgetAnimation
from Script.Engine import Conv_IntToString
from Script.FactoryGame import FindRecipesByProduct
from Script.FactoryGame import GetItemDescription
from Script.UMG import UserWidget
from Game.FactoryGame.Interface.UI.InGame.Widget_TooltipRecipe import Widget_TooltipRecipe
from Script.UMG import UMGSequencePlayer
from Script.FactoryGame import GetRecipeName
from Script.FactoryGame import Default__FGItemDescriptor
from Script.UMG import Create
from Script.FactoryGame import FGRecipe
from Script.FactoryGame import ItemAmount
from Script.FactoryGame import FGRecipeManager
from Script.Engine import IsValidClass
from Script.Engine import Concat_StrStr
from Script.FactoryGame import FGBuildingDescriptor

class Widget_Tooltip(UserWidget):
    SpawnAnim: Ptr[WidgetAnimation]
    mItemDescriptor: ItemAmount
    mRecipe: TSubclassOf[FGRecipe]
    mIsManufacturingStat: bool
    mDescriptionText: FText
    mTitleText: FText
    
    def GetItemDescription(self):
        ReturnValue1: bool = Default__KismetSystemLibrary.IsValidClass(self.mItemDescriptor.ItemClass)
        if not ReturnValue1:
            goto('L174')
        ReturnValue: FText = Default__FGItemDescriptor.GetItemDescription(self.mItemDescriptor.ItemClass)
        ReturnValue_0: FText = ReturnValue
        goto('L340')
        # Label 174
        ReturnValue_1: bool = Default__KismetSystemLibrary.IsValidClass(self.mRecipe)
        if not ReturnValue_1:
            goto('L313')
        ReturnValue_0 = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 259, 'Value': 'Save the necessary ingredients for this recipe.'}"
        goto('L340')
        # Label 313
        ReturnValue_0 = self.mDescriptionText
    

    def GetItemName(self):
        ReturnValue1: bool = Default__KismetSystemLibrary.IsValidClass(self.mItemDescriptor.ItemClass)
        if not ReturnValue1:
            goto('L174')
        ReturnValue: FText = Default__FGItemDescriptor.GetItemName(self.mItemDescriptor.ItemClass)
        ReturnValue_0: FText = ReturnValue
        goto('L685')
        # Label 174
        ReturnValue_1: bool = Default__KismetSystemLibrary.IsValidClass(self.mRecipe)
        if not ReturnValue_1:
            goto('L658')
        ReturnValue_2: FText = Default__FGRecipe.GetRecipeName(self.mRecipe)
        FormatArgumentData.ArgumentName = "X"
        FormatArgumentData.ArgumentValueType = 4
        FormatArgumentData.ArgumentValue = ReturnValue_2
        FormatArgumentData.ArgumentValueInt = 0
        FormatArgumentData.ArgumentValueFloat = 0
        FormatArgumentData.ArgumentValueGender = 0
        Array: List[FormatArgumentData] = [FormatArgumentData]
        ReturnValue_3: FText = Default__KismetTextLibrary.Format("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 557, 'Value': 'Add {X} to To-Do List'}", Array)
        ReturnValue_0 = ReturnValue_3
        goto('L685')
        # Label 658
        ReturnValue_0 = self.mTitleText
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_Tooltip(1675)
    

    def ExecuteUbergraph_Widget_Tooltip(self):
        goto(ComputedJump("EntryPoint"))
        ReturnValue: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.SpawnAnim, 0, 1, 0, 1)
        ReturnValue_0: bool = Default__KismetSystemLibrary.IsValidClass(self.mItemDescriptor.ItemClass)
        Descriptor: TSubclassOf[FGResourceDescriptor] = ClassCast[FGResourceDescriptor](self.mItemDescriptor.ItemClass)
        bSuccess2: bool = Descriptor
        ReturnValue_1: bool = Not_PreBool(bSuccess2)
        ReturnValue_2: bool = ReturnValue_0 and ReturnValue_1
        if not ReturnValue_2:
           goto(ExecutionFlow.Pop())
        ReturnValue_3: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_4: Ptr[FGRecipeManager] = Default__FGRecipeManager.Get(ReturnValue_3)
        ReturnValue_5: List[TSubclassOf[FGRecipe]] = ReturnValue_4.FindRecipesByProduct(self.mItemDescriptor.ItemClass)
        Variable: int32 = 0
        Variable_0: int32 = 0
        
        # Label 461
        ReturnValue_6: int32 = len(ReturnValue_5)
        ReturnValue_7: bool = Variable <= ReturnValue_6
        if not ReturnValue_7:
           goto(ExecutionFlow.Pop())
        Variable_0 = Variable
        ExecutionFlow.Push("L1601")
        ReturnValue1: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_8: Ptr[Widget_TooltipRecipe] = Default__WidgetBlueprintLibrary.Create(self, Widget_TooltipRecipe, ReturnValue1)
        
        Item = None
        # Label 685
        Item = ReturnValue_5[Variable_0]
        Default__KismetSystemLibrary.SetClassPropertyByName(ReturnValue_8, "mRecipe", Item)
        Variable_1: FText = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 827, 'Value': 'Standard Recipe: '}"
        ReturnValue_9: FString = Default__KismetStringLibrary.Conv_IntToString(Variable_0)
        ReturnValue_10: FString = Default__KismetStringLibrary.Concat_StrStr("Alternate Recipe ", ReturnValue_9)
        ReturnValue1_0: FString = Default__KismetStringLibrary.Concat_StrStr(ReturnValue_10, ":")
        ReturnValue_11: FText = Default__KismetTextLibrary.Conv_StringToText(ReturnValue1_0)
        ReturnValue_12: bool = Variable_0 > 0
        Variable_2: bool = ReturnValue_12
        
        switch = {
            False: Variable_1,
            True: ReturnValue_11
        }
        
        switch.get(Variable_2, None) = None
        Default__KismetSystemLibrary.SetTextPropertyByName(ReturnValue_8, "mRecipeNameText", Ref[switch.get(Variable_2, None)])
        Descriptor_0: TSubclassOf[FGVehicleDescriptor] = ClassCast[FGVehicleDescriptor](self.mItemDescriptor.ItemClass)
        bSuccess: bool = Descriptor_0
        Descriptor_1: TSubclassOf[FGBuildingDescriptor] = ClassCast[FGBuildingDescriptor](self.mItemDescriptor.ItemClass)
        bSuccess1: bool = Descriptor_1
        ReturnValue_13: bool = BooleanOR(bSuccess1, bSuccess)
        Default__KismetSystemLibrary.SetBoolPropertyByName(ReturnValue_8, "HideProductionInfo", ReturnValue_13)
        ReturnValue_14: Ptr[PanelSlot] = self.mRecipesContainer.AddChild(ReturnValue_8)
        goto(ExecutionFlow.Pop())
        # Label 1601
        ReturnValue_15: int32 = Variable + 1
        Variable = ReturnValue_15
        goto('L461')
        self.mRecipesContainer.ClearChildren()
        self.ToolTipContent.SetVisibility(4)
        Default__KismetSystemLibrary.Delay(self, 0.5, LatentActionInfo(Linkage = 15, UUID = 1492738409, ExecutionFunction = "ExecuteUbergraph_Widget_Tooltip", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
    
