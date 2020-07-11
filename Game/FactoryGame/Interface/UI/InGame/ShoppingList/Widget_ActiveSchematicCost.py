
from codegen.ue4_stub import *

from Script.UMG import GetParent
from Script.Engine import Texture2D
from Script.Engine import EqualEqual_ClassClass
from Script.FactoryGame import GetActiveSchematic
from Script.Engine import K2_SetTimerDelegate
from Script.FactoryGame import GetCost
from Script.UMG import GetChildIndex
from Script.Engine import GreaterEqual_IntInt
from Game.FactoryGame.Interface.UI.InGame.ShoppingList.Widget_ActiveSchematicContainer import Widget_ActiveSchematicContainer
from Script.Engine import Default__KismetSystemLibrary
from Game.FactoryGame.Character.Player.BP_PlayerState import BP_PlayerState
from Script.FactoryGame import Get
from Game.FactoryGame.Interface.UI.InGame.ShoppingList.Widget_ActiveSchematicCost import ExecuteUbergraph_Widget_ActiveSchematicCost
from Script.Engine import Default__KismetArrayLibrary
from Script.Engine import GameStateBase
from Script.UMG import ESlateVisibility
from Script.Engine import TimerHandle
from Script.Engine import IsValid
from Script.FactoryGame import GetSmallIcon
from Script.Engine import Default__GameplayStatics
from Script.FactoryGame import GetPaidOffCostFor
from Script.UMG import PanelWidget
from Script.FactoryGame import FGSchematic
from Script.Engine import K2_ClearAndInvalidateTimerHandle
from Script.UMG import UserWidget
from Script.FactoryGame import FGSchematicManager
from Script.FactoryGame import Default__FGItemDescriptor
from Script.Engine import GetGameState
from Script.FactoryGame import Default__FGSchematic
from Script.FactoryGame import ItemAmount
from Script.FactoryGame import Default__FGSchematicManager
from Script.Engine import IsValidClass

class Widget_ActiveSchematicCost(UserWidget):
    mPlayerState: Ptr[BP_PlayerState]
    mActiveSchematicContainer: Ptr[Widget_ActiveSchematicContainer]
    mUpdateHandle: TimerHandle
    padding = Namespace(Bottom=4, Left=4, Right=4, Top=4)
    
    def GetNumIngredientsPaidOff(self):
        ExecutionFlow.Push("L1284")
        ReturnValue: Ptr[GameStateBase] = Default__GameplayStatics.GetGameState(self)
        ReturnValue_0: Ptr[FGSchematicManager] = Default__FGSchematicManager.Get(ReturnValue)
        ReturnValue_1: bool = Default__KismetSystemLibrary.IsValid(ReturnValue_0)
        if not ReturnValue_1:
            goto('L1182')
        Variable: int32 = 0
        Variable_0: int32 = 0
        # Label 210
        ReturnValue = Default__GameplayStatics.GetGameState(self)
        ReturnValue_0 = Default__FGSchematicManager.Get(ReturnValue)
        ReturnValue_2: TSubclassOf[FGSchematic] = ReturnValue_0.GetActiveSchematic()
        ReturnValue_3: List[ItemAmount] = ReturnValue_0.GetPaidOffCostFor(ReturnValue_2)
        
        ReturnValue_4: int32 = len(ReturnValue_3)
        ReturnValue_5: bool = Variable <= ReturnValue_4
        if not ReturnValue_5:
           goto(ExecutionFlow.Pop())
        Variable_0 = Variable
        ExecutionFlow.Push("L1210")
        
        Ingredient = None
        self.GetIngredient(Ref[Ingredient])
        ReturnValue = Default__GameplayStatics.GetGameState(self)
        ReturnValue_0 = Default__FGSchematicManager.Get(ReturnValue)
        ReturnValue_2 = ReturnValue_0.GetActiveSchematic()
        ReturnValue_3 = ReturnValue_0.GetPaidOffCostFor(ReturnValue_2)
        
        Item = None
        Item = ReturnValue_3[Variable_0]
        ReturnValue_6: bool = EqualEqual_ClassClass(Item.ItemClass, Ingredient.ItemClass)
        if not ReturnValue_6:
           goto(ExecutionFlow.Pop())
        ReturnValue = Default__GameplayStatics.GetGameState(self)
        ReturnValue_0 = Default__FGSchematicManager.Get(ReturnValue)
        ReturnValue_2 = ReturnValue_0.GetActiveSchematic()
        ReturnValue_3 = ReturnValue_0.GetPaidOffCostFor(ReturnValue_2)
        
        Item = None
        Item = ReturnValue_3[Variable_0]
        NumItems = Item.amount
        # End
        # Label 1182
        NumItems = 0
        # End
        # Label 1210
        ReturnValue_7: int32 = Variable + 1
        Variable = ReturnValue_7
        goto('L210')
    

    def GetIngredient(self):
        ReturnValue: Ptr[GameStateBase] = Default__GameplayStatics.GetGameState(self)
        ReturnValue_0: Ptr[FGSchematicManager] = Default__FGSchematicManager.Get(ReturnValue)
        ReturnValue_1: bool = Default__KismetSystemLibrary.IsValid(ReturnValue_0)
        if not ReturnValue_1:
            goto('L717')
        ReturnValue = Default__GameplayStatics.GetGameState(self)
        ReturnValue_0 = Default__FGSchematicManager.Get(ReturnValue)
        ReturnValue_2: TSubclassOf[FGSchematic] = ReturnValue_0.GetActiveSchematic()
        ReturnValue_3: bool = Default__KismetSystemLibrary.IsValidClass(ReturnValue_2)
        if not ReturnValue_3:
            goto('L760')
        ReturnValue_4: Ptr[PanelWidget] = self.GetParent()
        ReturnValue = Default__GameplayStatics.GetGameState(self)
        ReturnValue_5: int32 = ReturnValue_4.GetChildIndex(self)
        ReturnValue_0 = Default__FGSchematicManager.Get(ReturnValue)
        ReturnValue_2 = ReturnValue_0.GetActiveSchematic()
        ReturnValue_6: List[ItemAmount] = Default__FGSchematic.GetCost(ReturnValue_2)
        
        Item = None
        Item = ReturnValue_6[ReturnValue_5]
        ingredient = Item
        # End
        # Label 717
        ingredient = ItemAmount(ItemClass = None, amount = 0)
        # End
        # Label 760
        ingredient = ItemAmount(ItemClass = None, amount = 0)
    

    def UpdateTimer(self):
        self.ExecuteUbergraph_Widget_ActiveSchematicCost(10)
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_ActiveSchematicCost(504)
    

    def Destruct(self):
        self.ExecuteUbergraph_Widget_ActiveSchematicCost(624)
    

    def ExecuteUbergraph_Widget_ActiveSchematicCost(self):
        
        Ingredient1 = None
        self.GetIngredient(Ref[Ingredient1])
        
        Ingredient2 = None
        self.GetIngredient(Ref[Ingredient2])
        
        NumItems = None
        self.GetNumIngredientsPaidOff(Ref[NumItems])
        ReturnValue: Ptr[Texture2D] = Default__FGItemDescriptor.GetSmallIcon(Ingredient2.ItemClass)
        self.Widget_CostSlotWrapper.Setup CostIcon(ReturnValue, Ingredient1, None, 0, NumItems, False, False, False)
        
        Ingredient = None
        self.GetIngredient(Ref[Ingredient])
        Variable: uint8 = 3
        Variable1: uint8 = 1
        
        NumItems1 = None
        self.GetNumIngredientsPaidOff(Ref[NumItems1])
        ReturnValue_0: bool = GreaterEqual_IntInt(NumItems1, Ingredient.amount)
        Variable_0: bool = ReturnValue_0
        
        switch = {
            False: Variable1,
            True: Variable
        }
        self.mMilestonePaidOff.SetVisibility(switch.get(Variable_0, None))
        # End
        
        # Label 457
        Default__KismetSystemLibrary.K2_ClearAndInvalidateTimerHandle(self, Ref[self.mUpdateHandle])
        # End
        OutputDelegate.BindUFunction(self, UpdateTimer)
        ReturnValue_1: TimerHandle = Default__KismetSystemLibrary.K2_SetTimerDelegate(OutputDelegate, 0.10000000149011612, True)
        self.mUpdateHandle = ReturnValue_1
        # End
        goto('L457')
    
