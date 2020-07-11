
from codegen.ue4_stub import *

from Script.FactoryGame import FGEquipmentDescriptor
from Script.Engine import EqualEqual_ClassClass
from Game.FactoryGame.Character.Player.BP_PlayerState import ExecuteUbergraph_BP_PlayerState.K2Node_Event_DeltaSeconds
from Game.FactoryGame.Character.Player.BP_PlayerState import ExecuteUbergraph_BP_PlayerState.K2Node_CustomEvent_Recipe2
from Game.FactoryGame.Character.Player.BP_PlayerState import ExecuteUbergraph_BP_PlayerState.K2Node_CustomEvent_ChatMessageIn
from Script.FactoryGame import FGPlayerState
from Script.Engine import Array_Set
from Script.Engine import Not_PreBool
from Script.Engine import HasAuthority
from Script.FactoryGame import GetProducts
from Game.FactoryGame.Character.Player.BP_PlayerState import BP_PlayerState
from Script.Engine import ReceiveTick
from Script.Engine import Default__KismetArrayLibrary
from Script.Engine import GameStateBase
from Script.Engine import ClassIsChildOf
from Game.FactoryGame.Character.Player.BP_PlayerState import ExecuteUbergraph_BP_PlayerState
from Script.FactoryGame import FGBuildDescriptor
from Script.Engine import EqualEqual_IntInt
from Game.FactoryGame.Character.Player.BP_PlayerState import ExecuteUbergraph_BP_PlayerState.K2Node_CustomEvent_Recipe1
from Script.Engine import Default__KismetTextLibrary
from Script.Engine import Conv_StringToText
from Script.Engine import Default__GameplayStatics
from Game.FactoryGame.Character.Player.BP_PlayerState import ExecuteUbergraph_BP_PlayerState.K2Node_CustomEvent_ItemDescriptor
from Script.Engine import FlushNetDormancy
from Game.FactoryGame.Character.Player.BP_PlayerState import ExecuteUbergraph_BP_PlayerState.K2Node_CustomEvent_NumRecipes
from Script.FactoryGame import Default__FGRecipe
from Game.FactoryGame.Character.Player.BP_PlayerState import ExecuteUbergraph_BP_PlayerState.K2Node_CustomEvent_NumRecipes1
from Game.FactoryGame.Character.Player.BP_PlayerState import ExecuteUbergraph_BP_PlayerState.K2Node_CustomEvent_Recipe
from Game.FactoryGame.Interface.UI.InGame.RecipeAmountStruct import RecipeAmountStruct
from Game.FactoryGame.Character.Player.BP_PlayerState import ExecuteUbergraph_BP_PlayerState.K2Node_CustomEvent_NumRecipes2
from Game.FactoryGame.Character.Player.BP_PlayerState import ExecuteUbergraph_BP_PlayerState.K2Node_CustomEvent_ChatSender
from Script.Engine import GetGameState
from Script.FactoryGame import ItemAmount
from Game.FactoryGame.Character.Player.BP_PlayerState import ExecuteUbergraph_BP_PlayerState.K2Node_CustomEvent_ChatMessageIn1
from Script.CoreUObject import LinearColor

class BP_PlayerState(FGPlayerState):
    ReceivedChatMessage: FMulticastScriptDelegate
    mSavedColorPickerColors: List[LinearColor]
    mShoppingList: List[RecipeAmountStruct]
    OnShoppingListUpdated: FMulticastScriptDelegate
    mLastSchematicTierInUI: int32
    mDefaultRecipeShortcuts = ['/Game/FactoryGame/Recipes/Buildings/Recipe_PowerPoleMk1.Recipe_PowerPoleMk1_C', '/Game/FactoryGame/Recipes/Buildings/Recipe_PowerLine.Recipe_PowerLine_C', '/Game/FactoryGame/Recipes/Buildings/Recipe_ConveyorBeltMk1.Recipe_ConveyorBeltMk1_C', '/Game/FactoryGame/Recipes/Buildings/Recipe_ConveyorPole.Recipe_ConveyorPole_C']
    mSlotNum = -1
    mTutorialSubsystemClass = NewObject[BP_TutorialSubsystem]()
    mNumArmSlots = 1
    PrimaryActorTick = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=False, bTickEvenWhenPaused=False)
    NetUpdateFrequency = 10
    
    def ClearShoppingList(self):
        self.FlushNetDormancy()
        Array: List[RecipeAmountStruct] = []
        self.mShoppingList = Array
        self.OnRep_mShoppingList()
    

    def ShoppingListUpdated(self):
        self.OnRep_mShoppingList()
    

    def OnRep_mShoppingList(self):
        self.OnShoppingListUpdated.ProcessMulticastDelegate()
    

    def GetShoppingListSortIndex(self, RecipeAmountStruct: Ref[RecipeAmountStruct]):
        ReturnValue: List[ItemAmount] = Default__FGRecipe.GetProducts(RecipeAmountStruct.Recipe_3_9675A43D4FEC0E33CE84EA9FCEF0E903, False)
        Variable: int32 = 1
        
        Item = None
        Item = ReturnValue[0]
        Variable1: int32 = 2
        ReturnValue_0: bool = ClassIsChildOf(Item.ItemClass, FGBuildDescriptor)
        ReturnValue1: bool = ClassIsChildOf(Item.ItemClass, FGEquipmentDescriptor)
        Variable_0: bool = ReturnValue1
        Variable1_0: bool = ReturnValue_0
        Variable2: int32 = 0
        
        switch = {
            False: Variable1,
            True: Variable
        }
        
        switch_0 = {
            False: switch.get(Variable_0, None),
            True: Variable2
        }
        ReturnValue_1: int32 = switch_0.get(Variable1_0, None)
    

    def SortShoppingList(self):
        ExecutionFlow.Push("L868")
        
        # Label 5
        ReturnValue: int32 = len(tempShoppingList)
        
        ReturnValue1: int32 = len(self.mShoppingList)
        ReturnValue_0: bool = ReturnValue1 != ReturnValue
        if not ReturnValue_0:
            goto('L645')
        ExecutionFlow.Push("L5")
        Variable: int32 = 0
        Variable_0: int32 = 0
        
        # Label 226
        ReturnValue2: int32 = len(self.mShoppingList)
        ReturnValue_1: bool = Variable <= ReturnValue2
        if not ReturnValue_1:
            goto('L697')
        Variable_0 = Variable
        ExecutionFlow.Push("L794")
        
        Item = None
        Item = self.mShoppingList[Variable_0]
        
        Item = None
        ReturnValue_2: int32 = self.GetShoppingListSortIndex(Ref[Item])
        ReturnValue_3: bool = EqualEqual_IntInt(currentSortIndex, ReturnValue_2)
        if not ReturnValue_3:
           goto(ExecutionFlow.Pop())
        
        Item = None
        Item = self.mShoppingList[Variable_0]
        
        Item = None
        ReturnValue_4: int32 = tempShoppingList.append(Item)
        # Label 644
        goto(ExecutionFlow.Pop())
        # Label 645
        self.FlushNetDormancy()
        self.mShoppingList = tempShoppingList
        self.OnRep_mShoppingList()
        goto(ExecutionFlow.Pop())
        # Label 697
        ReturnValue1_0: int32 = currentSortIndex + 1
        Variable_1: int32 = ReturnValue1_0
        currentSortIndex = Variable_1
        goto(ExecutionFlow.Pop())
        # Label 794
        ReturnValue_5: int32 = Variable + 1
        Variable = ReturnValue_5
        goto('L226')
    

    def SetNumRecipeInShoppingList(self, Recipe: TSubclassOf[FGRecipe], NumRecipes: int32):
        ExecutionFlow.Push("L1119")
        # Label 5
        mShoppingListArrayIndex = 0
        ReturnValue: bool = self.HasAuthority()
        if not ReturnValue:
            goto('L616')
        # Label 62
        mNumRecipesInput = NumRecipes
        Variable: bool = False
        Variable_0: int32 = 0
        Variable_1: int32 = 0
        # Label 146
        ReturnValue_0: bool = Not_PreBool(Variable)
        
        ReturnValue_1: int32 = len(self.mShoppingList)
        ReturnValue_2: bool = Variable_0 <= ReturnValue_1
        ReturnValue_3: bool = ReturnValue_0 and ReturnValue_2
        if not ReturnValue_3:
            goto('L653')
        Variable_1 = Variable_0
        ExecutionFlow.Push("L848")
        mShoppingListArrayIndex = Variable_1
        
        Item = None
        Item = self.mShoppingList[Variable_1]
        ReturnValue_4: bool = EqualEqual_ClassClass(Recipe, Item.Recipe_3_9675A43D4FEC0E33CE84EA9FCEF0E903)
        if not ReturnValue_4:
           goto(ExecutionFlow.Pop())
        ReturnValue_5: bool = mNumRecipesInput <= 0
        if not ReturnValue_5:
            goto('L922')
        
        self.mShoppingList.remove(mShoppingListArrayIndex)
        # Label 597
        self.ShoppingListUpdated()
        # End
        # Label 616
        self.Server_SetNumRecipesInShoppingList(Recipe, NumRecipes)
        goto('L62')
        # Label 653
        ReturnValue_6: bool = mNumRecipesInput > 0
        if not ReturnValue_6:
           goto(ExecutionFlow.Pop())
        # Label 697
        RecipeAmountStruct.Recipe_3_9675A43D4FEC0E33CE84EA9FCEF0E903 = Recipe
        # Label 725
        RecipeAmountStruct.Amount_6_262F181A4A294617FCD1F496A451BA13 = mNumRecipesInput
        
        RecipeAmountStruct = None
        ReturnValue_7: int32 = self.mShoppingList.append(RecipeAmountStruct)
        self.ShoppingListUpdated()
        # End
        # Label 848
        ReturnValue_8: int32 = Variable_0 + 1
        # Label 890
        Variable_0 = ReturnValue_8
        goto('L146')
        
        Item = None
        # Label 922
        Item = self.mShoppingList[Variable_1]
        RecipeAmountStruct1.Recipe_3_9675A43D4FEC0E33CE84EA9FCEF0E903 = Item.Recipe_3_9675A43D4FEC0E33CE84EA9FCEF0E903
        RecipeAmountStruct1.Amount_6_262F181A4A294617FCD1F496A451BA13 = mNumRecipesInput
        
        RecipeAmountStruct1 = None
        Default__KismetArrayLibrary.Array_Set(mShoppingListArrayIndex, False, Ref[self.mShoppingList], Ref[RecipeAmountStruct1])
        goto('L597')
    

    def PonderUpdatingShoppingList(self, InputPin: TSubclassOf[FGItemDescriptor]):
        ExecutionFlow.Push("L601")
        # Label 5
        Variable: int32 = 0
        Variable_0: int32 = 0
        
        # Label 51
        ReturnValue: int32 = len(self.mShoppingList)
        ReturnValue_0: bool = Variable <= ReturnValue
        if not ReturnValue_0:
           goto(ExecutionFlow.Pop())
        Variable_0 = Variable
        ExecutionFlow.Push("L527")
        
        Item = None
        Item = self.mShoppingList[Variable_0]
        ReturnValue_1: List[ItemAmount] = Default__FGRecipe.GetProducts(Item.Recipe_3_9675A43D4FEC0E33CE84EA9FCEF0E903, False)
        
        Item1 = None
        Item1 = ReturnValue_1[0]
        ReturnValue_2: bool = EqualEqual_ClassClass(Item1.ItemClass, InputPin)
        if not ReturnValue_2:
           goto(ExecutionFlow.Pop())
        
        Item = None
        Item = self.mShoppingList[Variable_0]
        self.RemoveRecipeFromShoppingList(Item.Recipe_3_9675A43D4FEC0E33CE84EA9FCEF0E903, 1)
        goto(ExecutionFlow.Pop())
        # Label 527
        ReturnValue_3: int32 = Variable + 1
        Variable = ReturnValue_3
        goto('L51')
    

    def AddRecipeToShoppingList(self, Recipe: TSubclassOf[FGRecipe], NumRecipes: int32):
        ExecutionFlow.Push("L964")
        # Label 5
        ReturnValue: bool = self.HasAuthority()
        if not ReturnValue:
            goto('L688')
        # Label 39
        Variable: bool = False
        Variable_0: int32 = 0
        Variable_1: int32 = 0
        # Label 96
        ReturnValue_0: bool = Not_PreBool(Variable)
        
        ReturnValue_1: int32 = len(self.mShoppingList)
        ReturnValue_2: bool = Variable_0 <= ReturnValue_1
        ReturnValue_3: bool = ReturnValue_0 and ReturnValue_2
        if not ReturnValue_3:
            goto('L725')
        Variable_1 = Variable_0
        ExecutionFlow.Push("L890")
        
        Item = None
        Item = self.mShoppingList[Variable_1]
        ReturnValue_4: bool = EqualEqual_ClassClass(Recipe, Item.Recipe_3_9675A43D4FEC0E33CE84EA9FCEF0E903)
        if not ReturnValue_4:
           goto(ExecutionFlow.Pop())
        
        Item = None
        Item = self.mShoppingList[Variable_1]
        ReturnValue_5: int32 = Item.Amount_6_262F181A4A294617FCD1F496A451BA13 + NumRecipes
        RecipeAmountStruct1.Recipe_3_9675A43D4FEC0E33CE84EA9FCEF0E903 = Item.Recipe_3_9675A43D4FEC0E33CE84EA9FCEF0E903
        RecipeAmountStruct1.Amount_6_262F181A4A294617FCD1F496A451BA13 = ReturnValue_5
        
        RecipeAmountStruct1 = None
        Default__KismetArrayLibrary.Array_Set(Variable_1, False, Ref[self.mShoppingList], Ref[RecipeAmountStruct1])
        self.ShoppingListUpdated()
        # End
        # Label 688
        self.Server_AddRecipeToShoppingList(Recipe, NumRecipes)
        goto('L39')
        # Label 725
        RecipeAmountStruct.Recipe_3_9675A43D4FEC0E33CE84EA9FCEF0E903 = Recipe
        RecipeAmountStruct.Amount_6_262F181A4A294617FCD1F496A451BA13 = NumRecipes
        
        RecipeAmountStruct = None
        ReturnValue_6: int32 = self.mShoppingList.append(RecipeAmountStruct)
        self.SortShoppingList()
        self.ShoppingListUpdated()
        # End
        # Label 890
        ReturnValue1: int32 = Variable_0 + 1
        Variable_0 = ReturnValue1
        goto('L96')
    

    def RemoveRecipeFromShoppingList(self, Recipe: TSubclassOf[FGRecipe], NumRecipes: int32):
        ExecutionFlow.Push("L979")
        # Label 5
        ReturnValue: bool = self.HasAuthority()
        if not ReturnValue:
            goto('L607')
        # Label 39
        Variable: bool = False
        Variable_0: int32 = 0
        Variable_1: int32 = 0
        # Label 96
        ReturnValue_0: bool = Not_PreBool(Variable)
        
        ReturnValue_1: int32 = len(self.mShoppingList)
        ReturnValue_2: bool = Variable_0 <= ReturnValue_1
        ReturnValue_3: bool = ReturnValue_0 and ReturnValue_2
        if not ReturnValue_3:
           goto(ExecutionFlow.Pop())
        Variable_1 = Variable_0
        ExecutionFlow.Push("L644")
        
        Item = None
        Item = self.mShoppingList[Variable_1]
        ReturnValue_4: bool = EqualEqual_ClassClass(Recipe, Item.Recipe_3_9675A43D4FEC0E33CE84EA9FCEF0E903)
        if not ReturnValue_4:
           goto(ExecutionFlow.Pop())
        
        Item = None
        Item = self.mShoppingList[Variable_1]
        ReturnValue_5: bool = Item.Amount_6_262F181A4A294617FCD1F496A451BA13 <= NumRecipes
        if not ReturnValue_5:
            goto('L718')
        
        self.mShoppingList.remove(Variable_1)
        self.ShoppingListUpdated()
        # End
        # Label 607
        self.Server_RemoveRecupeFromShoppingList(Recipe, NumRecipes)
        goto('L39')
        # Label 644
        ReturnValue_6: int32 = Variable_0 + 1
        Variable_0 = ReturnValue_6
        goto('L96')
        
        Item = None
        # Label 718
        Item = self.mShoppingList[Variable_1]
        ReturnValue_7: int32 = Item.Amount_6_262F181A4A294617FCD1F496A451BA13 - NumRecipes
        RecipeAmountStruct.Recipe_3_9675A43D4FEC0E33CE84EA9FCEF0E903 = Item.Recipe_3_9675A43D4FEC0E33CE84EA9FCEF0E903
        RecipeAmountStruct.Amount_6_262F181A4A294617FCD1F496A451BA13 = ReturnValue_7
        
        RecipeAmountStruct = None
        Default__KismetArrayLibrary.Array_Set(Variable_1, False, Ref[self.mShoppingList], Ref[RecipeAmountStruct])
        self.ShoppingListUpdated()
    

    def ReceiveBeginPlay(self):
        self.ExecuteUbergraph_BP_PlayerState(705)
    

    def BroadcastChatMessage(self, ChatMessageIn: FText):
        ExecuteUbergraph_BP_PlayerState.K2Node_CustomEvent_ChatMessageIn1 = ChatMessageIn #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_PlayerState(30)
    

    def ReceiveChatMessage(self, ChatMessageIn: FText, ChatSender: FText):
        ExecuteUbergraph_BP_PlayerState.K2Node_CustomEvent_ChatMessageIn = ChatMessageIn #  PERSISTENT_FRAME(
        ExecuteUbergraph_BP_PlayerState.K2Node_CustomEvent_ChatSender = ChatSender #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_PlayerState(667)
    

    def OnBuildableConstructed(self, itemDescriptor: TSubclassOf[FGItemDescriptor]):
        ExecuteUbergraph_BP_PlayerState.K2Node_CustomEvent_ItemDescriptor = itemDescriptor #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_PlayerState(748)
    

    def Server_AddRecipeToShoppingList(self, Recipe: TSubclassOf[FGRecipe], NumRecipes: int32):
        ExecuteUbergraph_BP_PlayerState.K2Node_CustomEvent_Recipe2 = Recipe #  PERSISTENT_FRAME(
        ExecuteUbergraph_BP_PlayerState.K2Node_CustomEvent_NumRecipes2 = NumRecipes #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_PlayerState(772)
    

    def Server_SetNumRecipesInShoppingList(self, Recipe: TSubclassOf[FGRecipe], NumRecipes: int32):
        ExecuteUbergraph_BP_PlayerState.K2Node_CustomEvent_Recipe1 = Recipe #  PERSISTENT_FRAME(
        ExecuteUbergraph_BP_PlayerState.K2Node_CustomEvent_NumRecipes1 = NumRecipes #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_PlayerState(805)
    

    def Server_RemoveRecupeFromShoppingList(self, Recipe: TSubclassOf[FGRecipe], NumRecipes: int32):
        ExecuteUbergraph_BP_PlayerState.K2Node_CustomEvent_Recipe = Recipe #  PERSISTENT_FRAME(
        ExecuteUbergraph_BP_PlayerState.K2Node_CustomEvent_NumRecipes = NumRecipes #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_PlayerState(838)
    

    def ReceiveTick(self):
        ExecuteUbergraph_BP_PlayerState.K2Node_Event_DeltaSeconds = DeltaSeconds #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_PlayerState(871)
    

    def Server_ClearShoppingList(self):
        self.ExecuteUbergraph_BP_PlayerState(891)
    

    def ExecuteUbergraph_BP_PlayerState(self):
        # Label 5
        goto(ComputedJump("EntryPoint"))
        # Label 15
        self.ClearShoppingList()
        goto(ExecutionFlow.Pop())
        Variable: int32 = 0
        Variable_0: int32 = 0
        # Label 76
        ReturnValue: Ptr[GameStateBase] = Default__GameplayStatics.GetGameState(self)
        
        ReturnValue.PlayerArray = None
        ReturnValue_0: int32 = len(ReturnValue.PlayerArray)
        ReturnValue_1: bool = Variable <= ReturnValue_0
        if not ReturnValue_1:
           goto(ExecutionFlow.Pop())
        Variable_0 = Variable
        ExecutionFlow.Push("L593")
        ReturnValue = Default__GameplayStatics.GetGameState(self)
        
        ReturnValue.PlayerArray = None
        Item = None
        Item = ReturnValue.PlayerArray[Variable_0]
        State: Ptr[BP_PlayerState] = Cast[BP_PlayerState](Item)
        bSuccess: bool = State
        if not bSuccess:
           goto(ExecutionFlow.Pop())
        ReturnValue_2: FText = Default__KismetTextLibrary.Conv_StringToText(self.PlayerName)
        State.ReceiveChatMessage(ChatMessageIn1, ReturnValue_2)
        goto(ExecutionFlow.Pop())
        # Label 593
        ReturnValue_3: int32 = Variable + 1
        Variable = ReturnValue_3
        goto('L76')
        self.ReceivedChatMessage.ProcessMulticastDelegate(ChatSender, ChatMessageIn)
        goto(ExecutionFlow.Pop())
        OutputDelegate.BindUFunction(self, OnBuildableConstructed)
        self.BuildableConstructedDelegate.AddUnique(OutputDelegate)
        goto(ExecutionFlow.Pop())
        self.PonderUpdatingShoppingList(ItemDescriptor)
        goto(ExecutionFlow.Pop())
        self.AddRecipeToShoppingList(Recipe2, NumRecipes2)
        goto(ExecutionFlow.Pop())
        self.SetNumRecipeInShoppingList(Recipe1, NumRecipes1)
        goto(ExecutionFlow.Pop())
        self.RemoveRecipeFromShoppingList(Recipe, NumRecipes)
        goto(ExecutionFlow.Pop())
        self.ReceiveTick(DeltaSeconds)
        # Label 890
        goto(ExecutionFlow.Pop())
        goto('L15')
    

    def OnShoppingListUpdated__DelegateSignature(self):
        pass
    

    def ReceivedChatMessage__DelegateSignature(self, ChatSender: FText, ChatMessage: FText):
        pass
    
