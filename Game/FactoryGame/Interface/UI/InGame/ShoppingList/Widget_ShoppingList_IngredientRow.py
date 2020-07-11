
from codegen.ue4_stub import *

from Script.UMG import GetParent
from Script.Engine import Texture2D
from Script.Engine import FClamp
from Script.Engine import Pawn
from Script.UMG import GetChildIndex
from Script.Engine import GreaterEqual_IntInt
from Script.Engine import Conv_IntToFloat
from Game.FactoryGame.Character.Player.BP_PlayerState import BP_PlayerState
from Script.Engine import FormatArgumentData
from Script.FactoryGame import GetItemName
from Script.UMG import ESlateVisibility
from Game.FactoryGame.Interface.UI.InGame.ShoppingList.Widget_ShoppingList_IngredientRow import ExecuteUbergraph_Widget_ShoppingList_IngredientRow.K2Node_Event_MyGeometry
from Script.Engine import Conv_IntToText
from Script.Engine import Default__KismetTextLibrary
from Script.FactoryGame import GetSmallIcon
from Script.UMG import Construct
from Script.UMG import Tick
from Script.Engine import Format
from Script.UMG import PanelWidget
from Game.FactoryGame.Interface.UI.InGame.ShoppingList.Widget_ShoppingList_IngredientRow import ExecuteUbergraph_Widget_ShoppingList_IngredientRow
from Script.UMG import UserWidget
from Script.UMG import GetOwningPlayerPawn
from Game.FactoryGame.Interface.UI.HUDHelpers.HUDHelpers import Default__HUDHelpers
from Script.Engine import SelectColor
from Script.FactoryGame import Default__FGItemDescriptor
from Script.SlateCore import SlateBrush
from Game.FactoryGame.Interface.UI.InGame.ShoppingList.Widget_ShoppingList import Widget_ShoppingList
from Game.FactoryGame.Interface.UI.InGame.ShoppingList.Widget_ShoppingList_IngredientRow import ExecuteUbergraph_Widget_ShoppingList_IngredientRow.K2Node_Event_InDeltaTime
from Script.CoreUObject import LinearColor

class Widget_ShoppingList_IngredientRow(UserWidget):
    mPlayerState: Ptr[BP_PlayerState]
    mShoppingListWidget: Ptr[Widget_ShoppingList]
    padding = Namespace(Bottom=6, Left=0, Right=0, Top=6)
    
    def GetProgressBarBorderColor(self):
        
        Text = None
        Graphics = None
        Default__HUDHelpers.GetFactoryGameDarkGray(self, Ref[Text], Ref[Graphics])
        
        TextWhite = None
        GraphicsWhite = None
        Default__HUDHelpers.GetFactoryGameWhite(self, Ref[TextWhite], Ref[GraphicsWhite])
        ReturnValue: LinearColor = SelectColor(Graphics, GraphicsWhite, self.mShoppingListWidget.isShoppingListInteractive)
        ReturnValue_0: LinearColor = ReturnValue
    

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
    

    def GetIconBGColor(self):
        
        numItems = None
        self.GetNumIngredientsOwned(Ref[numItems])
        
        Ingredient = None
        self.GetIngredient(Ref[Ingredient])
        ReturnValue: bool = GreaterEqual_IntInt(numItems, Ingredient.amount)
        ReturnValue_0: LinearColor = SelectColor(LinearColor(R = 0.6038280129432678, G = 0.5972020030021667, B = 0.5972020030021667, A = 0.5), LinearColor(R = 0.09530699998140335, G = 0.09530699998140335, B = 0.09530699998140335, A = 1), ReturnValue)
        ReturnValue_1: LinearColor = ReturnValue_0
    

    def GetBorderVisibility(self):
        Variable: uint8 = 1
        Variable1: uint8 = 3
        
        numItems = None
        self.GetNumIngredientsOwned(Ref[numItems])
        
        Ingredient = None
        self.GetIngredient(Ref[Ingredient])
        ReturnValue: bool = GreaterEqual_IntInt(numItems, Ingredient.amount)
        Variable_0: bool = ReturnValue
        
        switch = {
            False: Variable1,
            True: Variable
        }
        ReturnValue_0: uint8 = switch.get(Variable_0, None)
    

    def GetProgressBGColor(self):
        
        numItems = None
        self.GetNumIngredientsOwned(Ref[numItems])
        
        Ingredient = None
        self.GetIngredient(Ref[Ingredient])
        ReturnValue: bool = GreaterEqual_IntInt(numItems, Ingredient.amount)
        ReturnValue_0: LinearColor = SelectColor(LinearColor(R = 0.6038280129432678, G = 0.5972020030021667, B = 0.5972020030021667, A = 0.5), LinearColor(R = 0.09530699998140335, G = 0.09530699998140335, B = 0.09530699998140335, A = 1), ReturnValue)
        ReturnValue_1: LinearColor = ReturnValue_0
    

    def GetIconVisibility(self):
        Variable: uint8 = 2
        Variable1: uint8 = 3
        
        numItems = None
        self.GetNumIngredientsOwned(Ref[numItems])
        
        Ingredient = None
        self.GetIngredient(Ref[Ingredient])
        ReturnValue: bool = GreaterEqual_IntInt(numItems, Ingredient.amount)
        Variable_0: bool = ReturnValue
        
        switch = {
            False: Variable1,
            True: Variable
        }
        ReturnValue_0: uint8 = switch.get(Variable_0, None)
    

    def GetCheckboxVisibility(self):
        Variable: uint8 = 3
        Variable1: uint8 = 2
        
        numItems = None
        self.GetNumIngredientsOwned(Ref[numItems])
        
        Ingredient = None
        self.GetIngredient(Ref[Ingredient])
        ReturnValue: bool = GreaterEqual_IntInt(numItems, Ingredient.amount)
        Variable_0: bool = ReturnValue
        
        switch = {
            False: Variable1,
            True: Variable
        }
        ReturnValue_0: uint8 = switch.get(Variable_0, None)
    

    def GetProgressBarColor(self):
        
        numItems = None
        self.GetNumIngredientsOwned(Ref[numItems])
        
        Ingredient = None
        self.GetIngredient(Ref[Ingredient])
        ReturnValue: bool = GreaterEqual_IntInt(numItems, Ingredient.amount)
        if not ReturnValue:
            goto('L194')
        
        TextWhite = None
        GraphicsWhite = None
        Default__HUDHelpers.GetFactoryGameWhite(self, Ref[TextWhite], Ref[GraphicsWhite])
        ReturnValue_0: LinearColor = GraphicsWhite
        goto('L276')
        
        Text = None
        Graphics = None
        # Label 194
        Default__HUDHelpers.GetFactoryGameLightGray(self, Ref[Text], Ref[Graphics])
        ReturnValue_0 = Graphics
    

    def GetToDoListProgressBarPercentage(self):
        
        numItems = None
        self.GetNumIngredientsOwned(Ref[numItems])
        
        Ingredient = None
        self.GetIngredient(Ref[Ingredient])
        ReturnValue: float = Conv_IntToFloat(numItems)
        ReturnValue1: float = Conv_IntToFloat(Ingredient.amount)
        ReturnValue_0: float = ReturnValue / ReturnValue1
        ReturnValue_1: float = FClamp(ReturnValue_0, 0, 1)
        ReturnValue_2: float = ReturnValue_1
    

    def GetNumIngredientsOwned(self):
        
        Ingredient = None
        self.GetIngredient(Ref[Ingredient])
        ReturnValue: Ptr[Pawn] = self.GetOwningPlayerPawn()
        
        numItems = None
        Default__HUDHelpers.GetNumItemsFromPlayerInventory(ReturnValue, Ingredient.ItemClass, self, Ref[numItems])
        totalItems = numItems
        NumItems = totalItems
    

    def GetNumberIngredientsInInventoryText(self):
        
        numItems = None
        self.GetNumIngredientsOwned(Ref[numItems])
        ReturnValue: FText = Default__KismetTextLibrary.Conv_IntToText(numItems, False, True, 1, 324)
        FormatArgumentData.ArgumentName = "A"
        FormatArgumentData.ArgumentValueType = 4
        FormatArgumentData.ArgumentValue = ReturnValue
        FormatArgumentData.ArgumentValueInt = 0
        FormatArgumentData.ArgumentValueFloat = 0
        FormatArgumentData.ArgumentValueGender = 0
        Array: List[FormatArgumentData] = [FormatArgumentData]
        ReturnValue_0: FText = Default__KismetTextLibrary.Format("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 353, 'Value': '{A} / '}", Array)
        ReturnValue_1: FText = ReturnValue_0
    

    def GetIngredient(self):
        ReturnValue: Ptr[PanelWidget] = self.GetParent()
        ReturnValue_0: int32 = ReturnValue.GetChildIndex(self)
        ingredient = self.mShoppingListWidget.mTotalCost[ReturnValue_0]
    

    def GetIcon(self):
        
        Ingredient = None
        self.GetIngredient(Ref[Ingredient])
        ReturnValue: Ptr[Texture2D] = Default__FGItemDescriptor.GetSmallIcon(Ingredient.ItemClass)
        SlateBrush.ImageSize = self.mItemImageBrush.Brush.ImageSize
        SlateBrush.Margin = self.mItemImageBrush.Brush.Margin
        SlateBrush.TintColor = self.mItemImageBrush.Brush.TintColor
        SlateBrush.ResourceObject = ReturnValue
        SlateBrush.DrawAs = self.mItemImageBrush.Brush.DrawAs
        SlateBrush.Tiling = self.mItemImageBrush.Brush.Tiling
        SlateBrush.Mirroring = self.mItemImageBrush.Brush.Mirroring
        ReturnValue_0: SlateBrush = SlateBrush
    

    def GetIngredientTitleText(self):
        
        Ingredient = None
        self.GetIngredient(Ref[Ingredient])
        ReturnValue: FText = Default__FGItemDescriptor.GetItemName(Ingredient.ItemClass)
        ReturnValue_0: FText = ReturnValue
    

    def GetIngredientNumberText(self):
        
        Ingredient = None
        self.GetIngredient(Ref[Ingredient])
        ReturnValue: FText = Default__KismetTextLibrary.Conv_IntToText(Ingredient.amount, False, True, 1, 324)
        ReturnValue_0: FText = ReturnValue
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_ShoppingList_IngredientRow(25)
    

    def Tick(self):
        ExecuteUbergraph_Widget_ShoppingList_IngredientRow.K2Node_Event_MyGeometry = MyGeometry #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_ShoppingList_IngredientRow.K2Node_Event_InDeltaTime = InDeltaTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_ShoppingList_IngredientRow(30)
    

    def ExecuteUbergraph_Widget_ShoppingList_IngredientRow(self):
        # Label 10
        self.Construct()
        # End
        goto('L10')
        self.Tick(MyGeometry, InDeltaTime)
    
