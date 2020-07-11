
from codegen.ue4_stub import *

from Script.Engine import SetTextPropertyByName
from Script.Engine import Conv_TextToString
from Script.Engine import EqualEqual_ClassClass
from Script.Engine import SetClassPropertyByName
from Script.Engine import EqualEqual_ByteByte
from Script.Engine import GreaterEqual_IntInt
from Script.InputCore import Key
from Script.Engine import Default__KismetSystemLibrary
from Game.FactoryGame.Character.Player.BP_PlayerState import BP_PlayerState
from Script.Engine import PlayerController
from Script.Engine import SetStructurePropertyByName
from Script.Engine import Default__KismetArrayLibrary
from Script.Engine import FormatArgumentData
from Script.UMG import Unhandled
from Script.UMG import ESlateVisibility
from Game.FactoryGame.Interface.UI.InGame.ShoppingList.Widget_ShoppingListButton import ExecuteUbergraph_Widget_ShoppingListButton
from Script.Engine import IsValid
from Game.FactoryGame.Interface.UI.InGame.Widget_Tooltip import Widget_Tooltip
from Script.UMG import Default__WidgetBlueprintLibrary
from Script.Engine import Conv_IntToText
from Script.Engine import Default__KismetTextLibrary
from Script.Engine import IsInputKeyDown
from Script.Engine import SetBoolPropertyByName
from Script.Engine import BooleanOR
from Script.Engine import Conv_StringToInt
from Script.UMG import Widget
from Script.FactoryGame import Default__FGRecipe
from Script.Engine import Format
from Script.Engine import Default__KismetStringLibrary
from Script.UMG import WidgetAnimation
from Script.UMG import UserWidget
from Game.FactoryGame.Interface.UI.HUDHelpers.HUDHelpers import Default__HUDHelpers
from Script.FactoryGame import GetRecipeName
from Script.UMG import Create
from Script.FactoryGame import FGRecipe
from Script.SlateCore import SlateColor
from Game.FactoryGame.Interface.UI.InGame.ShoppingList.Widget_ShoppingListButton import ExecuteUbergraph_Widget_ShoppingListButton.K2Node_ComponentBoundEvent_Text
from Script.UMG import EventReply
from Game.FactoryGame.Interface.UI.InGame.ShoppingList.Widget_ShoppingListButton import ExecuteUbergraph_Widget_ShoppingListButton.K2Node_ComponentBoundEvent_CommitMethod

class Widget_ShoppingListButton(UserWidget):
    AfterShoppingListActive: Ptr[WidgetAnimation]
    mRecipe: TSubclassOf[FGRecipe]
    mPlayerState: Ptr[BP_PlayerState]
    OnShortcutRemapClicked: FMulticastScriptDelegate
    mParentIsHovered: bool
    mShouldPlayAnimation: bool
    
    def OnKeyDown(self):
        ReturnValue: EventReply = Default__WidgetBlueprintLibrary.Unhandled()
        ReturnValue_0: EventReply = ReturnValue
    

    def GetMinusVisibility(self):
        
        NumberRecipes = None
        self.GetAmount(Ref[NumberRecipes])
        ReturnValue: bool = GreaterEqual_IntInt(NumberRecipes, 1)
        if not ReturnValue:
            goto('L96')
        ReturnValue_0: uint8 = 4
        goto('L116')
        # Label 96
        ReturnValue_0 = 2
    

    def GetInputNumberTooltip(self):
        mTooltipDescriptionText = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 20, 'Value': 'Input a number to set the amount in your To-Do list.'}"
        ReturnValue: Ptr[Widget_Tooltip] = Default__WidgetBlueprintLibrary.Create(self, Widget_Tooltip, None)
        ItemAmount.ItemClass = None
        ItemAmount.amount = 0
        
        ItemAmount = None
        Default__KismetSystemLibrary.SetStructurePropertyByName(ReturnValue, "mItemDescriptor", Ref[ItemAmount])
        Default__KismetSystemLibrary.SetBoolPropertyByName(ReturnValue, "mIsManufacturingStat", True)
        
        Default__KismetSystemLibrary.SetTextPropertyByName(ReturnValue, "mDescriptionText", Ref[mTooltipDescriptionText])
        ReturnValue_0: FText = Default__FGRecipe.GetRecipeName(self.mRecipe)
        FormatArgumentData.ArgumentName = "A"
        FormatArgumentData.ArgumentValueType = 4
        FormatArgumentData.ArgumentValue = ReturnValue_0
        FormatArgumentData.ArgumentValueInt = 0
        FormatArgumentData.ArgumentValueFloat = 0
        FormatArgumentData.ArgumentValueGender = 0
        Array: List[FormatArgumentData] = [FormatArgumentData]
        ReturnValue_1: FText = Default__KismetTextLibrary.Format("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 714, 'Value': 'Add {A} to To-Do List'}", Array)
        
        Default__KismetSystemLibrary.SetTextPropertyByName(ReturnValue, "mTitleText", Ref[ReturnValue_1])
        ReturnValue_2: Ptr[Widget] = ReturnValue
    

    def GetButtonTooltip(self):
        mTooltipText = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 20, 'Value': 'Input a number to set amount in To-Do List.'}"
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_0: Ptr[Widget_Tooltip] = Default__WidgetBlueprintLibrary.Create(self, Widget_Tooltip, ReturnValue)
        ItemAmount.ItemClass = None
        ItemAmount.amount = 0
        
        ItemAmount = None
        Default__KismetSystemLibrary.SetStructurePropertyByName(ReturnValue_0, "mItemDescriptor", Ref[ItemAmount])
        Default__KismetSystemLibrary.SetClassPropertyByName(ReturnValue_0, "mRecipe", self.mRecipe)
        ReturnValue_1: Ptr[Widget] = ReturnValue_0
    

    def GetInputTextfieldVisibility(self):
        
        NumberRecipes = None
        self.GetAmount(Ref[NumberRecipes])
        ReturnValue: bool = NumberRecipes > 0
        if not ReturnValue:
            goto('L96')
        ReturnValue_0: uint8 = 0
        goto('L116')
        # Label 96
        ReturnValue_0 = 2
    

    def SetAmountText(self):
        
        NumberRecipes = None
        self.GetAmount(Ref[NumberRecipes])
        ReturnValue: FText = Default__KismetTextLibrary.Conv_IntToText(NumberRecipes, False, True, 1, 324)
        ReturnValue_0: FText = ReturnValue
    

    def GetHoverVisibility(self):
        if not self.mParentIsHovered:
            goto('L39')
        ReturnValue = 0
        goto('L59')
        # Label 39
        ReturnValue = 2
    

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
        Variable = ReturnValue_3
        goto('L112')
    

    def GetAmountRecipesInListColor(self):
        ReturnValue: bool = 0 > 0
        if not ReturnValue:
            goto('L131')
        
        TextWhite = None
        GraphicsWhite = None
        Default__HUDHelpers.GetFactoryGameWhite(self, Ref[TextWhite], Ref[GraphicsWhite])
        ReturnValue_0: SlateColor = TextWhite
        goto('L213')
        
        Text = None
        Graphics = None
        # Label 131
        Default__HUDHelpers.GetFactoryGameLightGray(self, Ref[Text], Ref[Graphics])
        ReturnValue_0 = Text
    

    def BndEvt__Remove1_K2Node_ComponentBoundEvent_2_OnButtonClickedEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_ShoppingListButton(10)
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_ShoppingListButton(576)
    

    def BndEvt__Add1_K2Node_ComponentBoundEvent_0_OnButtonClickedEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_ShoppingListButton(725)
    

    def BndEvt__mInputNumberToAdd_K2Node_ComponentBoundEvent_0_OnEditableTextBoxCommittedEvent__DelegateSignature(self, text: Const[Ref[FText]], CommitMethod: uint8):
        ExecuteUbergraph_Widget_ShoppingListButton.K2Node_ComponentBoundEvent_Text = text #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_ShoppingListButton.K2Node_ComponentBoundEvent_CommitMethod = CommitMethod #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_ShoppingListButton(1049)
    

    def ExecuteUbergraph_Widget_ShoppingListButton(self):
        ReturnValue2: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue1: bool = ReturnValue2.IsInputKeyDown(Key(KeyName = "RightShift"))
        ReturnValue2_0: bool = ReturnValue2.IsInputKeyDown(Key(KeyName = "LeftShift"))
        ReturnValue: bool = BooleanOR(ReturnValue2_0, ReturnValue1)
        if not ReturnValue:
            goto('L279')
        self.mPlayerState.RemoveRecipeFromShoppingList(self.mRecipe, 10)
        # End
        # Label 279
        self.mPlayerState.RemoveRecipeFromShoppingList(self.mRecipe, 1)
        # End
        # Label 334
        ReturnValue_0: bool = Default__KismetSystemLibrary.IsValid(self.mPlayerState)
        if not ReturnValue_0:
            goto('L1168')
        
        Text = None
        ReturnValue_1: FString = Default__KismetTextLibrary.Conv_TextToString(Ref[Text])
        ReturnValue_2: int32 = Default__KismetStringLibrary.Conv_StringToInt(ReturnValue_1)
        self.mPlayerState.SetNumRecipeInShoppingList(self.mRecipe, ReturnValue_2)
        # End
        ReturnValue_3: Ptr[PlayerController] = self.GetOwningPlayer()
        State: Ptr[BP_PlayerState] = Cast[BP_PlayerState](ReturnValue_3.PlayerState)
        bSuccess: bool = State
        if not bSuccess:
            goto('L1168')
        self.mPlayerState = State
        # End
        ReturnValue1_0: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_4: bool = ReturnValue1_0.IsInputKeyDown(Key(KeyName = "RightShift"))
        ReturnValue3: bool = ReturnValue1_0.IsInputKeyDown(Key(KeyName = "LeftShift"))
        ReturnValue1_1: bool = BooleanOR(ReturnValue3, ReturnValue_4)
        if not ReturnValue1_1:
            goto('L994')
        self.mPlayerState.AddRecipeToShoppingList(self.mRecipe, 10)
        # End
        # Label 994
        self.mPlayerState.AddRecipeToShoppingList(self.mRecipe, 1)
        # End
        ReturnValue_5: bool = EqualEqual_ByteByte(CommitMethod, 1)
        ReturnValue1_2: bool = EqualEqual_ByteByte(CommitMethod, 2)
        ReturnValue2_1: bool = BooleanOR(ReturnValue_5, ReturnValue1_2)
        if not ReturnValue2_1:
            goto('L1168')
        goto('L334')
    

    def OnShortcutRemapClicked__DelegateSignature(self, shortcutIndex: int32, newRecipe: TSubclassOf[FGRecipe]):
        pass
    
