
from codegen.ue4_stub import *

from Script.UMG import GetParent
from Script.UMG import GetChildIndex
from Script.InputCore import Key
from Script.FactoryGame import GetProducts
from Game.FactoryGame.Character.Player.BP_PlayerState import BP_PlayerState
from Script.Engine import PlayerController
from Script.Engine import Default__KismetArrayLibrary
from Script.UMG import IsPressed
from Script.UMG import ESlateVisibility
from Script.Engine import Conv_IntToText
from Script.Engine import Default__KismetTextLibrary
from Script.Engine import IsInputKeyDown
from Script.Engine import BooleanOR
from Script.FactoryGame import Default__FGRecipe
from Script.UMG import PanelWidget
from Script.UMG import UserWidget
from Game.FactoryGame.Interface.UI.InGame.ShoppingList.Widget_ShoppingListRecipeRow import ExecuteUbergraph_Widget_ShoppingListRecipeRow
from Game.FactoryGame.Interface.UI.HUDHelpers.HUDHelpers import Default__HUDHelpers
from Script.Engine import SelectColor
from Script.FactoryGame import GetRecipeName
from Script.FactoryGame import ItemAmount
from Game.FactoryGame.Interface.UI.InGame.ShoppingList.Widget_ShoppingList import Widget_ShoppingList
from Script.CoreUObject import LinearColor

class Widget_ShoppingListRecipeRow(UserWidget):
    mPlayerState: Ptr[BP_PlayerState]
    mShoppingListWidget: Ptr[Widget_ShoppingList]
    padding = Namespace(Bottom=2, Left=0, Right=0, Top=2)
    
    def GetShoppingListButtonVisibility(self):
        Variable: uint8 = 0
        Variable1: uint8 = 1
        Variable_0: bool = self.mShoppingListWidget.isShoppingListInteractive
        
        switch = {
            False: Variable1,
            True: Variable
        }
        ReturnValue = switch.get(Variable_0, None)
    

    def GetTextColor(self):
        
        TextWhite = None
        GraphicsWhite = None
        Default__HUDHelpers.GetFactoryGameWhite(self, Ref[TextWhite], Ref[GraphicsWhite])
        
        Text = None
        Graphics = None
        Default__HUDHelpers.GetFactoryGameDarkGray(self, Ref[Text], Ref[Graphics])
        Variable: bool = self.mShoppingListWidget.isShoppingListInteractive
        
        switch = {
            False: TextWhite,
            True: Text
        }
        ReturnValue = switch.get(Variable, None)
    

    def GetAddButtonIconColor(self):
        
        Text = None
        Graphics = None
        Default__HUDHelpers.GetFactoryGameDarkGray(self, Ref[Text], Ref[Graphics])
        ReturnValue: bool = self.mButtonAdd.IsHovered()
        
        TextWhite = None
        GraphicsWhite = None
        Default__HUDHelpers.GetFactoryGameWhite(self, Ref[TextWhite], Ref[GraphicsWhite])
        ReturnValue_0: LinearColor = SelectColor(GraphicsWhite, Graphics, ReturnValue)
        ReturnValue_1: LinearColor = ReturnValue_0
    

    def GetAddButtonColor(self):
        
        TextWhite = None
        GraphicsWhite = None
        Default__HUDHelpers.GetFactoryGameWhite(self, Ref[TextWhite], Ref[GraphicsWhite])
        ReturnValue: bool = self.mButtonAdd.IsPressed()
        ReturnValue_0: bool = self.mButtonAdd.IsHovered()
        
        Text = None
        Graphics = None
        Default__HUDHelpers.GetFactoryGameDarkGray(self, Ref[Text], Ref[Graphics])
        ReturnValue_1: bool = BooleanOR(ReturnValue_0, ReturnValue)
        ReturnValue_2: LinearColor = SelectColor(Graphics, GraphicsWhite, ReturnValue_1)
        ReturnValue_3: LinearColor = ReturnValue_2
    

    def GetRemoveButtonIconColor(self):
        
        Text = None
        Graphics = None
        Default__HUDHelpers.GetFactoryGameDarkGray(self, Ref[Text], Ref[Graphics])
        ReturnValue: bool = self.mButtonRemove.IsHovered()
        
        TextWhite = None
        GraphicsWhite = None
        Default__HUDHelpers.GetFactoryGameWhite(self, Ref[TextWhite], Ref[GraphicsWhite])
        ReturnValue_0: LinearColor = SelectColor(GraphicsWhite, Graphics, ReturnValue)
        ReturnValue_1: LinearColor = ReturnValue_0
    

    def GetRemoveButtonColor(self):
        
        TextWhite = None
        GraphicsWhite = None
        Default__HUDHelpers.GetFactoryGameWhite(self, Ref[TextWhite], Ref[GraphicsWhite])
        ReturnValue: bool = self.mButtonRemove.IsPressed()
        ReturnValue_0: bool = self.mButtonRemove.IsHovered()
        
        Text = None
        Graphics = None
        Default__HUDHelpers.GetFactoryGameDarkGray(self, Ref[Text], Ref[Graphics])
        ReturnValue_1: bool = BooleanOR(ReturnValue_0, ReturnValue)
        ReturnValue_2: LinearColor = SelectColor(Graphics, GraphicsWhite, ReturnValue_1)
        ReturnValue_3: LinearColor = ReturnValue_2
    

    def GetAmount(self):
        ReturnValue: Ptr[PanelWidget] = self.GetParent()
        ReturnValue_0: int32 = ReturnValue.GetChildIndex(self)
        
        self.mPlayerState.mShoppingList = None
        Item = None
        Item = self.mPlayerState.mShoppingList[ReturnValue_0]
        ReturnValue_1: List[ItemAmount] = Default__FGRecipe.GetProducts(Item.Recipe_3_9675A43D4FEC0E33CE84EA9FCEF0E903, False)
        
        Item1 = None
        Item1 = ReturnValue_1[0]
        ReturnValue_2: int32 = Item1.amount * Item.Amount_6_262F181A4A294617FCD1F496A451BA13
        mAmount = ReturnValue_2
    

    def GetRecipe(self):
        ReturnValue: Ptr[PanelWidget] = self.GetParent()
        ReturnValue_0: int32 = ReturnValue.GetChildIndex(self)
        
        self.mPlayerState.mShoppingList = None
        Item = None
        Item = self.mPlayerState.mShoppingList[ReturnValue_0]
        Recipe = Item.Recipe_3_9675A43D4FEC0E33CE84EA9FCEF0E903
    

    def GetTitleText(self):
        
        Recipe = None
        self.GetRecipe(Ref[Recipe])
        ReturnValue: FText = Default__FGRecipe.GetRecipeName(Recipe)
        ReturnValue_0: FText = ReturnValue
    

    def GetNumberText(self):
        
        mAmount = None
        self.GetAmount(Ref[mAmount])
        ReturnValue: FText = Default__KismetTextLibrary.Conv_IntToText(mAmount, False, True, 1, 324)
        ReturnValue_0: FText = ReturnValue
    

    def BndEvt__Button_1_K2Node_ComponentBoundEvent_1_OnButtonClickedEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_ShoppingListRecipeRow(458)
    

    def BndEvt__mButtonRemove_K2Node_ComponentBoundEvent_3_OnButtonClickedEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_ShoppingListRecipeRow(10)
    

    def ExecuteUbergraph_Widget_ShoppingListRecipeRow(self):
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_0: bool = ReturnValue.IsInputKeyDown(Key(KeyName = "RightShift"))
        ReturnValue1: bool = ReturnValue.IsInputKeyDown(Key(KeyName = "LeftShift"))
        ReturnValue_1: bool = BooleanOR(ReturnValue1, ReturnValue_0)
        if not ReturnValue_1:
            goto('L302')
        
        Recipe1 = None
        self.GetRecipe(Ref[Recipe1])
        self.mPlayerState.RemoveRecipeFromShoppingList(Recipe1, 10)
        # End
        
        Recipe2 = None
        # Label 302
        self.GetRecipe(Ref[Recipe2])
        self.mPlayerState.RemoveRecipeFromShoppingList(Recipe2, 1)
        # End
        
        Recipe = None
        # Label 380
        self.GetRecipe(Ref[Recipe])
        self.mPlayerState.AddRecipeToShoppingList(Recipe, 10)
        # End
        ReturnValue1_0: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue2: bool = ReturnValue1_0.IsInputKeyDown(Key(KeyName = "RightShift"))
        ReturnValue3: bool = ReturnValue1_0.IsInputKeyDown(Key(KeyName = "LeftShift"))
        ReturnValue1_1: bool = BooleanOR(ReturnValue3, ReturnValue2)
        if not ReturnValue1_1:
            goto('L677')
        goto('L380')
        
        Recipe3 = None
        # Label 677
        self.GetRecipe(Ref[Recipe3])
        self.mPlayerState.AddRecipeToShoppingList(Recipe3, 1)
    
