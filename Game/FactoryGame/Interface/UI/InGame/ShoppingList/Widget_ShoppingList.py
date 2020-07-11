
from codegen.ue4_stub import *

from Script.UMG import RemoveChildAt
from Script.Engine import Conv_TextToString
from Script.Engine import Delay
from Script.FactoryGame import FGCharacterPlayer
from Script.Engine import SetObjectPropertyByName
from Script.Engine import Pawn
from Script.Engine import GreaterEqual_IntInt
from Script.UMG import GetChildrenCount
from Script.UMG import AddChildToVerticalBox
from Script.FactoryGame import Default__FGInventoryLibrary
from Script.Engine import Not_PreBool
from Script.Engine import LatentActionInfo
from Script.Engine import Default__KismetSystemLibrary
from Game.FactoryGame.Character.Player.BP_PlayerState import BP_PlayerState
from Script.Engine import PlayerController
from Script.Engine import Default__KismetArrayLibrary
from Script.FactoryGame import ConsolidateItemsAmount
from Script.Engine import K2_GetPawn
from Script.FactoryGame import GetItemName
from Script.UMG import ESlateVisibility
from Game.FactoryGame.Interface.UI.InGame.ShoppingList.Widget_ShoppingListRecipeRow import Widget_ShoppingListRecipeRow
from Script.FactoryGame import GetInventory
from Script.FactoryGame import GetIngredients
from Script.FactoryGame import FGInventoryComponent
from Script.UMG import Default__WidgetBlueprintLibrary
from Game.FactoryGame.Interface.UI.InGame.ShoppingList.Widget_ShoppingList import ExecuteUbergraph_Widget_ShoppingList
from Script.Engine import Default__KismetTextLibrary
from Script.Engine import Conv_StringToText
from Script.FactoryGame import GetNumItems
from Script.FactoryGame import Default__FGRecipe
from Game.FactoryGame.Interface.UI.InGame.ShoppingList.Widget_ShoppingList_IngredientRow import Widget_ShoppingList_IngredientRow
from Script.Engine import SelectString
from Script.UMG import SetScrollBarVisibility
from Script.Engine import Default__KismetStringLibrary
from Script.Engine import Conv_IntToString
from Script.UMG import UserWidget
from Script.UMG import VerticalBoxSlot
from Script.FactoryGame import GetRecipeName
from Script.UMG import HasAnyChildren
from Script.UMG import Create
from Script.FactoryGame import Default__FGItemDescriptor
from Script.Engine import Min
from Script.FactoryGame import ItemAmount
from Game.FactoryGame.Character.Player.BP_PlayerController import BP_PlayerController
from Script.Engine import Array_Clear
from Script.Engine import IsValidClass
from Script.Engine import Concat_StrStr

class Widget_ShoppingList(UserWidget):
    mTotalCost: List[ItemAmount]
    isShoppingListInteractive: bool
    
    def GetClearListButtonVisibility(self):
        Variable: uint8 = 1
        Variable1: uint8 = 0
        Variable2: uint8 = 1
        ReturnValue: bool = self.mShoppingListRecipeContainer.HasAnyChildren()
        Variable1_0: bool = self.isShoppingListInteractive
        ReturnValue_0: bool = Not_PreBool(ReturnValue)
        ReturnValue_1: bool = self.isShoppingListInteractive and ReturnValue_0
        Variable_0: bool = ReturnValue_1
        
        switch = {
            False: Variable1,
            True: Variable
        }
        
        switch_0 = {
            False: Variable2,
            True: switch.get(Variable_0, None)
        }
        ReturnValue_2: uint8 = switch_0.get(Variable1_0, None)
    

    def GetInteractiveBoxVisibility(self):
        Variable: uint8 = 0
        Variable1: uint8 = 1
        Variable_0: bool = self.isShoppingListInteractive
        
        switch = {
            False: Variable1,
            True: Variable
        }
        self.Widget_Scrollbox.mScrollBox.SetScrollBarVisibility(switch.get(Variable_0, None))
        Variable2: uint8 = 1
        Variable3: uint8 = 3
        Variable4: uint8 = 1
        ReturnValue: bool = self.mShoppingListRecipeContainer.HasAnyChildren()
        ReturnValue_0: bool = Not_PreBool(ReturnValue)
        ReturnValue_1: bool = self.isShoppingListInteractive and ReturnValue_0
        Variable1_0: bool = ReturnValue_1
        Variable2_0: bool = self.isShoppingListInteractive
        
        switch_0 = {
            False: Variable3,
            True: Variable2
        }
        
        switch_1 = {
            False: Variable4,
            True: switch_0.get(Variable1_0, None)
        }
        ReturnValue_2: uint8 = switch_1.get(Variable2_0, None)
    

    def GetDivVisibility(self):
        ReturnValue: int32 = self.mShoppingListIngredientContainer.GetChildrenCount()
        ReturnValue_0: bool = ReturnValue > 0
        if not ReturnValue_0:
            goto('L123')
        ReturnValue_1: uint8 = 0
        goto('L143')
        # Label 123
        ReturnValue_1 = 2
    

    def MatchWidgetWithIngredients(self):
        ExecutionFlow.Push("L358")
        
        # Label 5
        ReturnValue: int32 = len(self.mTotalCost)
        ReturnValue_0: int32 = self.mShoppingListIngredientContainer.GetChildrenCount()
        ReturnValue_1: bool = ReturnValue != ReturnValue_0
        if not ReturnValue_1:
           goto(ExecutionFlow.Pop())
        ExecutionFlow.Push("L5")
        
        ReturnValue = len(self.mTotalCost)
        ReturnValue_0 = self.mShoppingListIngredientContainer.GetChildrenCount()
        ReturnValue_2: bool = ReturnValue > ReturnValue_0
        if not ReturnValue_2:
            goto('L343')
        self.AddIngredientRow()
        goto(ExecutionFlow.Pop())
        # Label 343
        self.RemoveIngredientRow()
        goto(ExecutionFlow.Pop())
    

    def CalculateIngredients(self):
        ExecutionFlow.Push("L1316")
        
        # Label 5
        Default__KismetArrayLibrary.Array_Clear(Ref[self.mTotalCost])
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        State: Ptr[BP_PlayerState] = Cast[BP_PlayerState](ReturnValue.PlayerState)
        bSuccess: bool = State
        if not bSuccess:
           goto(ExecutionFlow.Pop())
        Variable: int32 = 0
        Variable_0: int32 = 0
        
        State.mShoppingList = None
        # Label 213
        ReturnValue_0: int32 = len(State.mShoppingList)
        ReturnValue_1: bool = Variable <= ReturnValue_0
        if not ReturnValue_1:
            goto('L1126')
        Variable_0 = Variable
        ExecutionFlow.Push("L1168")
        Variable1: int32 = 0
        Variable1_0: int32 = 0
        
        State.mShoppingList = None
        Item = None
        # Label 424
        Item = State.mShoppingList[Variable_0]
        ReturnValue_2: List[ItemAmount] = Default__FGRecipe.GetIngredients(Item.Recipe_3_9675A43D4FEC0E33CE84EA9FCEF0E903)
        
        ReturnValue1: int32 = len(ReturnValue_2)
        ReturnValue1_0: bool = Variable1 <= ReturnValue1
        if not ReturnValue1_0:
           goto(ExecutionFlow.Pop())
        Variable1_0 = Variable1
        ExecutionFlow.Push("L1242")
        
        State.mShoppingList = None
        Item = None
        Item = State.mShoppingList[Variable_0]
        ReturnValue_2 = Default__FGRecipe.GetIngredients(Item.Recipe_3_9675A43D4FEC0E33CE84EA9FCEF0E903)
        
        Item1 = None
        Item1 = ReturnValue_2[Variable1_0]
        ReturnValue_3: int32 = Item1.amount * Item.Amount_6_262F181A4A294617FCD1F496A451BA13
        ItemAmount.ItemClass = Item1.ItemClass
        ItemAmount.amount = ReturnValue_3
        
        ItemAmount = None
        ReturnValue_4: int32 = self.mTotalCost.append(ItemAmount)
        goto(ExecutionFlow.Pop())
        
        # Label 1126
        Default__FGInventoryLibrary.ConsolidateItemsAmount(Ref[self.mTotalCost])
        goto(ExecutionFlow.Pop())
        # Label 1168
        ReturnValue_5: int32 = Variable + 1
        Variable = ReturnValue_5
        goto('L213')
        # Label 1242
        ReturnValue1_1: int32 = Variable1 + 1
        Variable1 = ReturnValue1_1
        goto('L424')
    

    def RemoveIngredientRow(self):
        ReturnValue: int32 = self.mShoppingListIngredientContainer.GetChildrenCount()
        ReturnValue_0: int32 = ReturnValue - 1
        ReturnValue_1: int32 = Min(ReturnValue_0, 0)
        ReturnValue_2: bool = self.mShoppingListIngredientContainer.RemoveChildAt(ReturnValue_1)
    

    def AddIngredientRow(self):
        ReturnValue1: Ptr[PlayerController] = self.GetOwningPlayer()
        State: Ptr[BP_PlayerState] = Cast[BP_PlayerState](ReturnValue1.PlayerState)
        bSuccess: bool = State
        if not bSuccess:
            goto('L379')
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_0: Ptr[Widget_ShoppingList_IngredientRow] = Default__WidgetBlueprintLibrary.Create(self, Widget_ShoppingList_IngredientRow, ReturnValue)
        Default__KismetSystemLibrary.SetObjectPropertyByName(ReturnValue_0, "mPlayerState", State)
        Default__KismetSystemLibrary.SetObjectPropertyByName(ReturnValue_0, "mShoppingListWidget", self)
        ReturnValue_1: Ptr[VerticalBoxSlot] = self.mShoppingListIngredientContainer.AddChildToVerticalBox(ReturnValue_0)
    

    def RemoveRecipeRow(self):
        ReturnValue: int32 = self.mShoppingListRecipeContainer.GetChildrenCount()
        ReturnValue_0: int32 = ReturnValue - 1
        ReturnValue_1: int32 = Min(ReturnValue_0, 0)
        ReturnValue_2: bool = self.mShoppingListRecipeContainer.RemoveChildAt(ReturnValue_1)
    

    def AddRecipeRow(self):
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        State: Ptr[BP_PlayerState] = Cast[BP_PlayerState](ReturnValue.PlayerState)
        bSuccess: bool = State
        if not bSuccess:
            goto('L379')
        ReturnValue1: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_0: Ptr[Widget_ShoppingListRecipeRow] = Default__WidgetBlueprintLibrary.Create(self, Widget_ShoppingListRecipeRow, ReturnValue1)
        Default__KismetSystemLibrary.SetObjectPropertyByName(ReturnValue_0, "mPlayerState", State)
        Default__KismetSystemLibrary.SetObjectPropertyByName(ReturnValue_0, "mShoppingListWidget", self)
        ReturnValue_1: Ptr[VerticalBoxSlot] = self.mShoppingListRecipeContainer.AddChildToVerticalBox(ReturnValue_0)
    

    def MatchWidgetsWithRecipes(self):
        ExecutionFlow.Push("L523")
        # Label 5
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        State: Ptr[BP_PlayerState] = Cast[BP_PlayerState](ReturnValue.PlayerState)
        bSuccess: bool = State
        if not bSuccess:
           goto(ExecutionFlow.Pop())
        # Label 126
        ReturnValue_0: int32 = self.mShoppingListRecipeContainer.GetChildrenCount()
        
        State.mShoppingList = None
        ReturnValue_1: int32 = len(State.mShoppingList)
        ReturnValue_2: bool = ReturnValue_1 != ReturnValue_0
        if not ReturnValue_2:
           goto(ExecutionFlow.Pop())
        ExecutionFlow.Push("L126")
        ReturnValue_0 = self.mShoppingListRecipeContainer.GetChildrenCount()
        
        State.mShoppingList = None
        ReturnValue_1 = len(State.mShoppingList)
        ReturnValue_3: bool = ReturnValue_1 > ReturnValue_0
        if not ReturnValue_3:
            goto('L508')
        self.AddRecipeRow()
        goto(ExecutionFlow.Pop())
        # Label 508
        self.RemoveRecipeRow()
        goto(ExecutionFlow.Pop())
    

    def Get ShoppingListText(self):
        ExecutionFlow.Push("L3848")
        # Label 5
        ReturnValue1: Ptr[PlayerController] = self.GetOwningPlayer()
        State: Ptr[BP_PlayerState] = Cast[BP_PlayerState](ReturnValue1.PlayerState)
        bSuccess2: bool = State
        if not bSuccess2:
            goto('L2026')
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        Controller: Ptr[BP_PlayerController] = Cast[BP_PlayerController](ReturnValue)
        bSuccess: bool = Controller
        if not bSuccess:
            goto('L2026')
        ReturnValue_0: Ptr[Pawn] = Controller.K2_GetPawn()
        Player: Ptr[FGCharacterPlayer] = Cast[FGCharacterPlayer](ReturnValue_0)
        bSuccess1: bool = Player
        if not bSuccess1:
            goto('L2026')
        localPawn = Player
        
        State.mShoppingList = None
        ReturnValue1_0: int32 = len(State.mShoppingList)
        ReturnValue_1: bool = ReturnValue1_0 > 0
        if not ReturnValue_1:
            goto('L2026')
        Variable1: int32 = 0
        Variable2: int32 = 0
        
        State.mShoppingList = None
        # Label 548
        ReturnValue3: int32 = len(State.mShoppingList)
        ReturnValue2: bool = Variable1 <= ReturnValue3
        if not ReturnValue2:
            goto('L2051')
        Variable2 = Variable1
        ExecutionFlow.Push("L3700")
        ReturnValue8: FString = Default__KismetStringLibrary.Concat_StrStr(finalString, "
")
        
        State.mShoppingList = None
        Item1 = None
        Item1 = State.mShoppingList[Variable2]
        ReturnValue2_0: FString = Default__KismetStringLibrary.Conv_IntToString(Item1.Amount_6_262F181A4A294617FCD1F496A451BA13)
        ReturnValue9: FString = Default__KismetStringLibrary.Concat_StrStr(ReturnValue8, ReturnValue2_0)
        ReturnValue10: FString = Default__KismetStringLibrary.Concat_StrStr(ReturnValue9, "x ")
        ReturnValue_2: FText = Default__FGRecipe.GetRecipeName(Item1.Recipe_3_9675A43D4FEC0E33CE84EA9FCEF0E903)
        
        ReturnValue1_1: FString = Default__KismetTextLibrary.Conv_TextToString(Ref[ReturnValue_2])
        ReturnValue11: FString = Default__KismetStringLibrary.Concat_StrStr(ReturnValue10, ReturnValue1_1)
        finalString = ReturnValue11
        Variable: int32 = 0
        Variable_0: int32 = 0
        
        State.mShoppingList = None
        Item1 = None
        # Label 1324
        Item1 = State.mShoppingList[Variable2]
        ReturnValue_3: List[ItemAmount] = Default__FGRecipe.GetIngredients(Item1.Recipe_3_9675A43D4FEC0E33CE84EA9FCEF0E903)
        
        ReturnValue2_1: int32 = len(ReturnValue_3)
        ReturnValue1_2: bool = Variable <= ReturnValue2_1
        if not ReturnValue1_2:
           goto(ExecutionFlow.Pop())
        Variable_0 = Variable
        ExecutionFlow.Push("L3774")
        
        State.mShoppingList = None
        Item1 = None
        Item1 = State.mShoppingList[Variable2]
        ReturnValue_3 = Default__FGRecipe.GetIngredients(Item1.Recipe_3_9675A43D4FEC0E33CE84EA9FCEF0E903)
        
        Item2 = None
        Item2 = ReturnValue_3[Variable_0]
        ReturnValue_4: int32 = Item2.amount * Item1.Amount_6_262F181A4A294617FCD1F496A451BA13
        ItemAmount.ItemClass = Item2.ItemClass
        ItemAmount.amount = ReturnValue_4
        
        ItemAmount = None
        ReturnValue_5: int32 = totalCost.append(ItemAmount)
        goto(ExecutionFlow.Pop())
        # Label 2026
        ReturnValue_6: FText = 
        goto('L3848')
        
        # Label 2051
        Default__FGInventoryLibrary.ConsolidateItemsAmount(Ref[totalCost])
        ReturnValue4: FString = Default__KismetStringLibrary.Concat_StrStr(finalString, "
---------------------------")
        finalString = ReturnValue4
        Variable2_0: int32 = 0
        Variable1_0: int32 = 0
        
        # Label 2255
        ReturnValue_7: int32 = len(totalCost)
        ReturnValue_8: bool = Variable2_0 <= ReturnValue_7
        if not ReturnValue_8:
            goto('L3609')
        Variable1_0 = Variable2_0
        ExecutionFlow.Push("L3535")
        
        Item = None
        Item = totalCost[Variable1_0]
        ReturnValue_9: bool = Default__KismetSystemLibrary.IsValidClass(Item.ItemClass)
        if not ReturnValue_9:
           goto(ExecutionFlow.Pop())
        ReturnValue_10: Ptr[FGInventoryComponent] = localPawn.GetInventory()
        ReturnValue_11: FString = Default__KismetStringLibrary.Concat_StrStr(finalString, "
")
        
        Item = None
        Item = totalCost[Variable1_0]
        ReturnValue_12: FString = Default__KismetStringLibrary.Conv_IntToString(Item.amount)
        ReturnValue_13: int32 = ReturnValue_10.GetNumItems(Item.ItemClass)
        ReturnValue_14: bool = GreaterEqual_IntInt(ReturnValue_13, Item.amount)
        ReturnValue1_3: FString = Default__KismetStringLibrary.Conv_IntToString(ReturnValue_13)
        ReturnValue_15: FString = SelectString("[X] ", "[   ] ", ReturnValue_14)
        ReturnValue_16: FText = Default__FGItemDescriptor.GetItemName(Item.ItemClass)
        ReturnValue1_4: FString = Default__KismetStringLibrary.Concat_StrStr(ReturnValue_11, ReturnValue_15)
        
        ReturnValue_17: FString = Default__KismetTextLibrary.Conv_TextToString(Ref[ReturnValue_16])
        ReturnValue2_2: FString = Default__KismetStringLibrary.Concat_StrStr(ReturnValue1_4, ReturnValue1_3)
        ReturnValue3_0: FString = Default__KismetStringLibrary.Concat_StrStr(ReturnValue2_2, "/")
        ReturnValue5: FString = Default__KismetStringLibrary.Concat_StrStr(ReturnValue3_0, ReturnValue_12)
        ReturnValue6: FString = Default__KismetStringLibrary.Concat_StrStr(ReturnValue5, " ")
        ReturnValue7: FString = Default__KismetStringLibrary.Concat_StrStr(ReturnValue6, ReturnValue_17)
        finalString = ReturnValue7
        goto(ExecutionFlow.Pop())
        # Label 3535
        ReturnValue2_3: int32 = Variable2_0 + 1
        Variable2_0 = ReturnValue2_3
        goto('L2255')
        # Label 3609
        ReturnValue_18: FText = Default__KismetTextLibrary.Conv_StringToText(finalString)
        ReturnValue_6 = ReturnValue_18
        goto('L3848')
        # Label 3700
        ReturnValue1_5: int32 = Variable1 + 1
        Variable1 = ReturnValue1_5
        goto('L548')
        # Label 3774
        ReturnValue_19: int32 = Variable + 1
        Variable = ReturnValue_19
        goto('L1324')
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_ShoppingList(454)
    

    def UpdateShoppingListRows(self):
        self.ExecuteUbergraph_Widget_ShoppingList(502)
    

    def BndEvt__Widget_StandardButton_K2Node_ComponentBoundEvent_0_OnClicked__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_ShoppingList(15)
    

    def ExecuteUbergraph_Widget_ShoppingList(self):
        # Label 5
        goto(ComputedJump("EntryPoint"))
        ReturnValue1: Ptr[PlayerController] = self.GetOwningPlayer()
        State1: Ptr[BP_PlayerState] = Cast[BP_PlayerState](ReturnValue1.PlayerState)
        bSuccess1: bool = State1
        # Label 126
        if not bSuccess1:
           goto(ExecutionFlow.Pop())
        State1.Server_ClearShoppingList()
        goto(ExecutionFlow.Pop())
        # Label 173
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        State: Ptr[BP_PlayerState] = Cast[BP_PlayerState](ReturnValue.PlayerState)
        bSuccess: bool = State
        if not bSuccess:
            goto('L377')
        OutputDelegate.BindUFunction(self, UpdateShoppingListRows)
        State.OnShoppingListUpdated.AddUnique(OutputDelegate)
        self.UpdateShoppingListRows()
        goto(ExecutionFlow.Pop())
        # Label 377
        Default__KismetSystemLibrary.Delay(self, 0.20000000298023224, LatentActionInfo(Linkage = 173, UUID = 984691511, ExecutionFunction = "ExecuteUbergraph_Widget_ShoppingList", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        goto('L173')
        # Label 459
        self.MatchWidgetsWithRecipes()
        self.CalculateIngredients()
        self.MatchWidgetWithIngredients()
        goto(ExecutionFlow.Pop())
        goto('L459')
    
