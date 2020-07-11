
from codegen.ue4_stub import *

from Script.Engine import Default__KismetInputLibrary
from Script.Engine import EqualEqual_ClassClass
from Script.Engine import InputEvent_IsShiftDown
from Script.Engine import Default__KismetSystemLibrary
from Game.FactoryGame.Character.Player.BP_PlayerState import BP_PlayerState
from Script.Engine import PlayerController
from Script.Engine import Default__KismetArrayLibrary
from Script.UMG import Handled
from Script.UMG import Unhandled
from Script.UMG import ESlateVisibility
from Script.Engine import IsValid
from Script.Engine import Conv_IntToText
from Script.UMG import Default__WidgetBlueprintLibrary
from Script.Engine import Default__KismetTextLibrary
from Game.FactoryGame.Interface.UI.InGame.BuildMenu.Prototype.Widget_BuildMenu_RightClickMenu import ExecuteUbergraph_Widget_BuildMenu_RightClickMenu
from Script.SlateCore import InputEvent
from Script.UMG import UserWidget
from Script.FactoryGame import FGRecipe
from Script.UMG import GetInputEventFromKeyEvent
from Script.UMG import EventReply

class Widget_BuildMenu_RightClickMenu(UserWidget):
    mPlayerState: Ptr[BP_PlayerState]
    mRecipe: TSubclassOf[FGRecipe]
    isHoldingShift: bool
    UpdateWindowWidgetOffset: FMulticastScriptDelegate
    hasRemoveToDoListBeenShown: bool
    
    def UpdateRemoveFromTodoListVisibility(self):
        
        NumberRecipes = None
        self.GetAmount(Ref[NumberRecipes])
        ReturnValue: bool = NumberRecipes <= 1
        self.mRemoveFromTodoList.SetIsDisabled(ReturnValue)
    

    def OnKeyUp(self):
        
        ReturnValue: InputEvent = Default__WidgetBlueprintLibrary.GetInputEventFromKeyEvent(Ref[InKeyEvent])
        
        ReturnValue_0: bool = Default__KismetInputLibrary.InputEvent_IsShiftDown(Ref[ReturnValue])
        if not ReturnValue_0:
            goto('L217')
        self.isHoldingShift = True
        ReturnValue_1: EventReply = Default__WidgetBlueprintLibrary.Handled()
        ReturnValue_2: EventReply = ReturnValue_1
        goto('L305')
        # Label 217
        self.isHoldingShift = False
        # Label 228
        ReturnValue_3: EventReply = Default__WidgetBlueprintLibrary.Unhandled()
        ReturnValue_2 = ReturnValue_3
    

    def OnKeyDown(self):
        
        ReturnValue: InputEvent = Default__WidgetBlueprintLibrary.GetInputEventFromKeyEvent(Ref[InKeyEvent])
        
        ReturnValue_0: bool = Default__KismetInputLibrary.InputEvent_IsShiftDown(Ref[ReturnValue])
        if not ReturnValue_0:
            goto('L217')
        self.isHoldingShift = True
        ReturnValue_1: EventReply = Default__WidgetBlueprintLibrary.Handled()
        ReturnValue_2: EventReply = ReturnValue_1
        goto('L294')
        # Label 217
        ReturnValue_3: EventReply = Default__WidgetBlueprintLibrary.Unhandled()
        ReturnValue_2 = ReturnValue_3
    

    def GetRemoveItemButtonVisibility(self):
        
        NumberRecipes = None
        self.GetAmount(Ref[NumberRecipes])
        ReturnValue: bool = NumberRecipes > 0
        if not ReturnValue:
            goto('L107')
        self.hasRemoveToDoListBeenShown = True
        ReturnValue_0: uint8 = 0
        goto('L196')
        # Label 107
        if not self.hasRemoveToDoListBeenShown:
            goto('L176')
        self.SetVisibility(1)
        self.RemoveFromParent()
        ReturnValue_0 = 1
        goto('L196')
        # Label 176
        ReturnValue_0 = 1
    

    def GetAmount(self):
        ExecutionFlow.Push("L607")
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(self.mPlayerState)
        if not ReturnValue:
           goto(ExecutionFlow.Pop())
        Variable: int32 = 0
        Variable_0: int32 = 0
        
        self.mPlayerState.mShoppingList = None
        # Label 112
        ReturnValue_0: int32 = len(self.mPlayerState.mShoppingList)
        ReturnValue_1: bool = Variable <= ReturnValue_0
        if not ReturnValue_1:
           goto(ExecutionFlow.Pop())
        Variable_0 = Variable
        ExecutionFlow.Push("L533")
        
        self.mPlayerState.mShoppingList = None
        Item = None
        Item = self.mPlayerState.mShoppingList[Variable_0]
        # Label 354
        ReturnValue_2: bool = EqualEqual_ClassClass(Item.Recipe_3_9675A43D4FEC0E33CE84EA9FCEF0E903, self.mRecipe)
        if not ReturnValue_2:
           goto(ExecutionFlow.Pop())
        
        self.mPlayerState.mShoppingList = None
        Item = None
        Item = self.mPlayerState.mShoppingList[Variable_0]
        NumberRecipes = Item.Amount_6_262F181A4A294617FCD1F496A451BA13
        # End
        # Label 533
        ReturnValue_3: int32 = Variable + 1
        # Label 575
        Variable = ReturnValue_3
        goto('L112')
    

    def GetNumberRecipesInShoppingList(self):
        ExecutionFlow.Push("L649")
        Variable: int32 = 0
        Variable_0: int32 = 0
        
        self.mPlayerState.mShoppingList = None
        # Label 51
        ReturnValue: int32 = len(self.mPlayerState.mShoppingList)
        ReturnValue_0: bool = Variable <= ReturnValue
        if not ReturnValue_0:
            goto('L547')
        Variable_0 = Variable
        ExecutionFlow.Push("L575")
        
        self.mPlayerState.mShoppingList = None
        Item = None
        Item = self.mPlayerState.mShoppingList[Variable_0]
        ReturnValue_1: bool = EqualEqual_ClassClass(Item.Recipe_3_9675A43D4FEC0E33CE84EA9FCEF0E903, self.mRecipe)
        if not ReturnValue_1:
           goto(ExecutionFlow.Pop())
        
        self.mPlayerState.mShoppingList = None
        Item = None
        # Label 354
        Item = self.mPlayerState.mShoppingList[Variable_0]
        ReturnValue_2: FText = Default__KismetTextLibrary.Conv_IntToText(Item.Amount_6_262F181A4A294617FCD1F496A451BA13, False, True, 1, 324)
        ReturnValue_3: FText = ReturnValue_2
        goto('L649')
        # Label 547
        ReturnValue_3 = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 567, 'Value': '0'}"
        goto('L649')
        # Label 575
        ReturnValue_4: int32 = Variable + 1
        Variable = ReturnValue_4
        goto('L51')
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_BuildMenu_RightClickMenu(29)
    

    def BndEvt__mAddToTodolistButton_K2Node_ComponentBoundEvent_1_OnClicked__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_BuildMenu_RightClickMenu(502)
    

    def BndEvt__mRemoveFromTodoList_K2Node_ComponentBoundEvent_2_OnClicked__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_BuildMenu_RightClickMenu(507)
    

    def ExecuteUbergraph_Widget_BuildMenu_RightClickMenu(self):
        # Label 10
        self.UpdateRemoveFromTodoListVisibility()
        # End
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        State: Ptr[BP_PlayerState] = Cast[BP_PlayerState](ReturnValue.PlayerState)
        bSuccess: bool = State
        if not bSuccess:
            goto('L512')
        self.mPlayerState = State
        goto('L10')
        # Label 178
        self.mPlayerState.AddRecipeToShoppingList(self.mRecipe, 10)
        # Label 228
        self.UpdateWindowWidgetOffset.ProcessMulticastDelegate()
        self.UpdateRemoveFromTodoListVisibility()
        # End
        # Label 266
        self.mPlayerState.RemoveRecipeFromShoppingList(self.mRecipe, 10)
        # Label 316
        self.UpdateWindowWidgetOffset.ProcessMulticastDelegate()
        self.UpdateRemoveFromTodoListVisibility()
        # End
        # Label 354
        if not self.isHoldingShift:
            goto('L373')
        goto('L178')
        # Label 373
        self.mPlayerState.AddRecipeToShoppingList(self.mRecipe, 1)
        goto('L228')
        # Label 428
        if not self.isHoldingShift:
            goto('L447')
        goto('L266')
        # Label 447
        self.mPlayerState.RemoveRecipeFromShoppingList(self.mRecipe, 1)
        goto('L316')
        goto('L354')
        goto('L428')
    

    def UpdateWindowWidgetOffset__DelegateSignature(self):
        pass
    
