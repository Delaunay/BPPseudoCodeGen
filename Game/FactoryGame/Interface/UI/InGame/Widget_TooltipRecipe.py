
from codegen.ue4_stub import *

from Script.UMG import PanelSlot
from Script.UMG import AddChild
from Script.FactoryGame import Default__FGInventoryLibrary
from Script.Engine import TextIsEmpty
from Script.Engine import Not_PreBool
from Script.FactoryGame import GetProducts
from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import PlayerController
from Script.Engine import Default__KismetArrayLibrary
from Script.Engine import FormatArgumentData
from Script.UMG import ESlateVisibility
from Script.Engine import Conv_FloatToText
from Game.FactoryGame.Interface.UI.InGame.Widget_CostSlotWrapper import Widget_CostSlotWrapper
from Script.FactoryGame import GetIngredients
from Script.UMG import Default__WidgetBlueprintLibrary
from Script.UMG import SetColorAndOpacity
from Script.Engine import Default__KismetTextLibrary
from Script.FactoryGame import GetAmountConvertedFromItemAmount
from Script.FactoryGame import Default__FGRecipe
from Script.Engine import Format
from Game.FactoryGame.Interface.UI.InGame.Widget_TooltipRecipe import ExecuteUbergraph_Widget_TooltipRecipe
from Script.UMG import UserWidget
from Game.FactoryGame.Interface.UI.HUDHelpers.HUDHelpers import Default__HUDHelpers
from Game.FactoryGame.Interface.UI.InGame.Widget_TooltipRecipe import ExecuteUbergraph_Widget_TooltipRecipe.K2Node_Event_IsDesignTime
from Script.UMG import Create
from Script.FactoryGame import GetManufacturingDuration
from Script.FactoryGame import FGRecipe
from Script.FactoryGame import ItemAmount
from Script.Engine import IsValidClass

class Widget_TooltipRecipe(UserWidget):
    mRecipe: TSubclassOf[FGRecipe]
    mRecipeNameText: FText
    HideProductionInfo: bool
    
    def OnUnhovered(self):
        
        Orange = None
        OrangeText = None
        Default__HUDHelpers.GetFactoryGameOrange(self, Ref[Orange], Ref[OrangeText])
        self.mProductionTime.SetColorAndOpacity(OrangeText)
    

    def OnHovered(self):
        
        TextWhite = None
        GraphicsWhite = None
        Default__HUDHelpers.GetFactoryGameWhite(self, Ref[TextWhite], Ref[GraphicsWhite])
        self.mProductionTime.SetColorAndOpacity(TextWhite)
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_TooltipRecipe(1353)
    

    def PreConstruct(self):
        ExecuteUbergraph_Widget_TooltipRecipe.K2Node_Event_IsDesignTime = IsDesignTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_TooltipRecipe(2359)
    

    def ExecuteUbergraph_Widget_TooltipRecipe(self):
        goto(ComputedJump("EntryPoint"))
        # Label 15
        ReturnValue: int32 = Variable + 1
        Variable: int32 = ReturnValue
        # Label 84
        ReturnValue_0: List[ItemAmount] = Default__FGRecipe.GetIngredients(self.mRecipe)
        
        ReturnValue_1: int32 = len(ReturnValue_0)
        ReturnValue_2: bool = Variable <= ReturnValue_1
        if not ReturnValue_2:
            goto('L634')
        Variable_0: int32 = Variable
        ExecutionFlow.Push("L15")
        ReturnValue_3: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_4: Ptr[Widget_CostSlotWrapper] = Default__WidgetBlueprintLibrary.Create(self, Widget_CostSlotWrapper, ReturnValue_3)
        ReturnValue_0 = Default__FGRecipe.GetIngredients(self.mRecipe)
        
        Item = None
        Item = ReturnValue_0[Variable_0]
        ReturnValue_4.Setup CostIcon(None, Item, None, 0, 0, True, False, False)
        ReturnValue_4.mSmallSlot = True
        ReturnValue_5: Ptr[PanelSlot] = self.mIngredientsContainer.AddChild(ReturnValue_4)
        goto(ExecutionFlow.Pop())
        # Label 634
        Variable1: int32 = 0
        Variable1_0: int32 = 0
        # Label 680
        ReturnValue1: List[ItemAmount] = Default__FGRecipe.GetProducts(self.mRecipe, False)
        
        ReturnValue1_0: int32 = len(ReturnValue1)
        ReturnValue1_1: bool = Variable1 <= ReturnValue1_0
        if not ReturnValue1_1:
           goto(ExecutionFlow.Pop())
        Variable1_0 = Variable1
        ExecutionFlow.Push("L1228")
        ReturnValue1_2: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue1_3: Ptr[Widget_CostSlotWrapper] = Default__WidgetBlueprintLibrary.Create(self, Widget_CostSlotWrapper, ReturnValue1_2)
        ReturnValue1 = Default__FGRecipe.GetProducts(self.mRecipe, False)
        
        Item1 = None
        Item1 = ReturnValue1[Variable1_0]
        ReturnValue1_3.Setup CostIcon(None, Item1, None, 0, 0, True, False, False)
        ReturnValue1_3.mSmallSlot = True
        ReturnValue1_4: Ptr[PanelSlot] = self.mProductsContainer.AddChild(ReturnValue1_3)
        goto(ExecutionFlow.Pop())
        # Label 1228
        ReturnValue1_5: int32 = Variable1 + 1
        Variable1 = ReturnValue1_5
        goto('L680')
        # Label 1302
        Variable = 0
        Variable_0 = 0
        goto('L84')
        self.mIngredientsContainer.ClearChildren()
        ReturnValue_6: bool = Default__KismetSystemLibrary.IsValidClass(self.mRecipe)
        if not ReturnValue_6:
           goto(ExecutionFlow.Pop())
        
        ReturnValue_7: bool = Default__KismetTextLibrary.TextIsEmpty(Ref[self.mRecipeNameText])
        ReturnValue_8: bool = Not_PreBool(ReturnValue_7)
        if not ReturnValue_8:
            goto('L1627')
        self.mRecipeNameLabel.SetText(self.mRecipeNameText)
        self.mRecipeNameLabel.SetVisibility(0)
        # Label 1627
        ReturnValue_9: List[ItemAmount] = Default__FGRecipe.GetProducts(self.mRecipe, False)
        ReturnValue_10: float = Default__FGRecipe.GetManufacturingDuration(self.mRecipe)
        
        ReturnValue_9[0] = None
        itemClass = None
        amountConverted = None
        Default__FGInventoryLibrary.GetAmountConvertedFromItemAmount(Ref[ReturnValue_9[0]], Ref[itemClass], Ref[amountConverted])
        ReturnValue_11: float = ReturnValue_10 / amountConverted
        ReturnValue1_6: float = 60 / ReturnValue_11
        ReturnValue_12: FText = Default__KismetTextLibrary.Conv_FloatToText(ReturnValue1_6, 0, False, True, 1, 324, 0, 3)
        FormatArgumentData.ArgumentName = "time"
        FormatArgumentData.ArgumentValueType = 4
        FormatArgumentData.ArgumentValue = ReturnValue_12
        FormatArgumentData.ArgumentValueInt = 0
        FormatArgumentData.ArgumentValueFloat = 0
        FormatArgumentData.ArgumentValueGender = 0
        Array: List[FormatArgumentData] = [FormatArgumentData]
        ReturnValue_13: FText = Default__KismetTextLibrary.Format("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 2244, 'Value': '{time} per minute'}", Array)
        self.mProductionTime.SetText(ReturnValue_13)
        goto('L1302')
        Variable_1: uint8 = 3
        Variable1_1: uint8 = 1
        Variable_2: bool = self.HideProductionInfo
        
        switch = {
            False: Variable_1,
            True: Variable1_1
        }
        self.mProductionInfoContainer.SetVisibility(switch.get(Variable_2, None))
        goto(ExecutionFlow.Pop())
    
