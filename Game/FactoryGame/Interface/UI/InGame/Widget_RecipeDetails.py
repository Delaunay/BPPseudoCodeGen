
from codegen.ue4_stub import *

from Script.UMG import AddChildToHorizontalBox
from Game.FactoryGame.Interface.UI.InGame.Widget_RecipeDetails import ExecuteUbergraph_Widget_RecipeDetails
from Script.Engine import PlayerController
from Script.Engine import Default__KismetArrayLibrary
from Script.UMG import Create
from Script.FactoryGame import FGRecipe
from Script.FactoryGame import Default__FGRecipe
from Game.FactoryGame.Interface.UI.InGame.Widget_CostSlotWrapper import Widget_CostSlotWrapper
from Script.FactoryGame import ItemAmount
from Script.FactoryGame import GetIngredients
from Script.UMG import HorizontalBoxSlot
from Script.UMG import Default__WidgetBlueprintLibrary
from Script.UMG import UserWidget

class Widget_RecipeDetails(UserWidget):
    mRecipe: TSubclassOf[FGRecipe]
    localClearText: FText
    
    def Construct(self):
        self.ExecuteUbergraph_Widget_RecipeDetails(625)
    

    def ExecuteUbergraph_Widget_RecipeDetails(self):
        goto(ComputedJump("EntryPoint"))
        # Label 15
        Variable: int32 = 0
        # Label 38
        ReturnValue: List[ItemAmount] = Default__FGRecipe.GetIngredients(self.mRecipe)
        
        ReturnValue_0: int32 = len(ReturnValue)
        ReturnValue_1: bool = Variable_0 <= ReturnValue_0
        if not ReturnValue_1:
           goto(ExecutionFlow.Pop())
        Variable = Variable_0
        ExecutionFlow.Push("L551")
        ReturnValue_2: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_3: Ptr[Widget_CostSlotWrapper] = Default__WidgetBlueprintLibrary.Create(self, Widget_CostSlotWrapper, ReturnValue_2)
        ReturnValue = Default__FGRecipe.GetIngredients(self.mRecipe)
        
        Item = None
        Item = ReturnValue[Variable]
        ReturnValue_3.Setup CostIcon(None, Item, None, 0, 0, False, False, False)
        ReturnValue_4: Ptr[HorizontalBoxSlot] = self.HorizontalBox_101.AddChildToHorizontalBox(ReturnValue_3)
        goto(ExecutionFlow.Pop())
        # Label 551
        ReturnValue_5: int32 = Variable_0 + 1
        Variable_0: int32 = ReturnValue_5
        goto('L38')
        Variable_0 = 0
        goto('L15')
    
