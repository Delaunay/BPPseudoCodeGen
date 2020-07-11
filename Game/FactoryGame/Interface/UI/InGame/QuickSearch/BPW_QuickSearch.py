
from codegen.ue4_stub import *

from Script.Engine import Texture2D
from Script.FactoryGame import FGCharacterPlayer
from Script.InputCore import Key
from Script.UMG import AddChild
from Script.Engine import Default__KismetSystemLibrary
from Script.FactoryGame import GetProducts
from Script.UMG import GetChildAt
from Script.Engine import FormatArgumentData
from Script.UMG import ESlateVisibility
from Script.Engine import TimerHandle
from Script.Engine import Array_Append
from Script.Engine import Contains
from Script.Engine import EqualEqual_IntInt
from Script.Engine import Default__KismetTextLibrary
from Script.FactoryGame import GetSmallIcon
from Script.Engine import NotEqual_StrStr
from Script.FactoryGame import GetAllAvailableRecipes
from Script.Engine import Default__KismetStringLibrary
from Script.Engine import RetriggerableDelay
from Game.FactoryGame.Interface.UI.HUDHelpers.HUDHelpers import Default__HUDHelpers
from Script.UMG import Create
from Script.FactoryGame import FGBuildGun
from Script.Engine import GetGameState
from Script.Engine import Clamp
from Script.Engine import Array_Clear
from Script.FactoryGame import FGResourceDescriptor
from Script.Engine import SetClassPropertyByName
from Script.Engine import SetObjectPropertyByName
from Script.Engine import Pawn
from Script.Engine import GreaterEqual_IntInt
from Script.UMG import GetChildrenCount
from Game.FactoryGame.Interface.UI.InGame.QuickSearch.BPW_QuickSearch import ExecuteUbergraph_BPW_QuickSearch
from Script.Engine import Default__KismetArrayLibrary
from Script.Engine import GameStateBase
from Game.FactoryGame.Interface.UI.InGame.QuickSearch.BPW_QuickSearch import ExecuteUbergraph_BPW_QuickSearch.K2Node_ComponentBoundEvent_Text
from Script.FactoryGame import SetDefaultFocusWidget
from Script.FactoryGame import FGVehicleDescriptor
from Script.FactoryGame import FGInteractWidget
from Script.FactoryGame import Default__FGRecipeManager
from Script.FactoryGame import GotoBuildState
from Script.FactoryGame import Default__FGRecipe
from Script.Engine import GetKey
from Script.FactoryGame import FindRecipesByProduct
from Script.Engine import NotEqual_ByteByte
from Script.Engine import EqualEqual_KeyKey
from Game.FactoryGame.Interface.UI.HUDHelpers.BPHUDHelpers import Default__BPHUDHelpers
from Script.FactoryGame import Default__FGItemDescriptor
from Script.FactoryGame import FGRecipe
from Script.FactoryGame import ItemAmount
from Script.FactoryGame import IsBuildGunEquipped
from Script.UMG import EventReply
from Script.FactoryGame import FGBuildingDescriptor
from Script.UMG import SetUserFocus
from Script.Engine import SetTextPropertyByName
from Script.Engine import Array_Contains
from Script.UMG import PanelSlot
from Script.FactoryGame import SetKeyboardFocusAndSelectAllText
from Script.Engine import LatentActionInfo
from Script.FactoryGame import Get
from Script.Engine import PlayerController
from Script.UMG import Unhandled
from Script.UMG import Default__WidgetBlueprintLibrary
from Script.Engine import Replace
from Script.Engine import Default__GameplayStatics
from Script.FactoryGame import ToggleBuildGun
from Script.Engine import Format
from Game.FactoryGame.Interface.UI.InGame.-Shared.Widget_ListButton import Widget_ListButton
from Script.FactoryGame import Default__FGBlueprintFunctionLibrary
from Game.FactoryGame.Interface.UI.InGame.QuickSearch.BPW_QuickSearch import ExecuteUbergraph_BPW_QuickSearch.K2Node_ComponentBoundEvent_Text1
from Game.FactoryGame.Interface.UI.InGame.Codex.Widget_Codex_Container import Widget_Codex_Container
from Script.FactoryGame import FGItemDescriptor
from Game.FactoryGame.Interface.UI.InGame.BP_GameUI import BP_GameUI
from Script.FactoryGame import EvaluateMathExpression
from Script.Engine import Default__KismetInputLibrary
from Script.Engine import Conv_TextToString
from Script.Engine import Not_PreBool
from Script.FactoryGame import GetItemName
from Script.UMG import Widget
from Script.Engine import Array_AddUnique
from Script.FactoryGame import GetBuildGun
from Script.UMG import GetOwningPlayerPawn
from Script.FactoryGame import FGRecipeManager
from Game.FactoryGame.Interface.UI.InGame.QuickSearch.BPW_QuickSearch import ExecuteUbergraph_BPW_QuickSearch.K2Node_ComponentBoundEvent_CommitMethod

class BPW_QuickSearch(FGInteractWidget):
    mBuildings: List[TSubclassOf[FGItemDescriptor]]
    mParts: List[TSubclassOf[FGItemDescriptor]]
    mProducts: List[TSubclassOf[FGItemDescriptor]]
    mSearchDelayHandle: TimerHandle
    mSearchWords: FString
    mSearchResults: List[TSubclassOf[FGItemDescriptor]]
    mSelectedIndex: int32
    mMaxAmountOfResults: int32 = 10
    mMathSymbols: List[FString] = ['+', '-', '*', '/', '(', ')', '^', '%']
    mUseKeyboard = True
    mUseMouse = True
    mCaptureInput = True
    mDesiredHorizontalAlignment = 2
    mDesiredVerticalAlignment = 2
    mCustomTickRate = 0.10000000149011612
    mCallCustomTickOnConstruct = True
    
    def OpenQuickSearch(self):
        self.SetDefaultFocusWidget(self.mSearchField)
        self.SetupDefaultFocus()
        self.SetInputMode()
        self.InitAllRecipes()
        self.mSearchField.SetKeyboardFocusAndSelectAllText()
        self.CreateSearchResultList(self.mSearchWords)
    

    def CloseQuickSearch(self):
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        
        gameUI = None
        Default__HUDHelpers.GetFGGameUI(ReturnValue, self, Ref[gameUI])
        UI: Ptr[BP_GameUI] = Cast[BP_GameUI](gameUI)
        bSuccess: bool = UI
        if not bSuccess:
            goto('L194')
        UI.ResetInput()
    

    def SetQuickSearchVisibility(self, IsVisibile: bool):
        Variable: bool = IsVisibile
        Variable_0: uint8 = 0
        # Label 39
        Variable1: uint8 = 1
        
        switch = {
            False: Variable1,
            True: Variable_0
        }
        self.SetVisibility(switch.get(Variable, None))
        if not IsVisibile:
            goto('L159')
        self.OpenQuickSearch()
        # End
        # Label 159
        self.CloseQuickSearch()
    

    def GenerateMathAnswer(self, mSearchWords: FString):
        ReturnValue: bool = self.IsMathExpression(mSearchWords)
        if not ReturnValue:
            goto('L561')
        self.mMathResult.SetVisibility(0)
        ReturnValue_0: FString = Default__KismetStringLibrary.Replace(mSearchWords, ",", ".", 1)
        
        Result = None
        ReturnValue_1: bool = Default__FGBlueprintFunctionLibrary.EvaluateMathExpression(ReturnValue_0, Ref[Result])
        if not ReturnValue_1:
            goto('L604')
        FormatArgumentData.ArgumentName = "Answer"
        FormatArgumentData.ArgumentValueType = 4
        FormatArgumentData.ArgumentValue = Result
        FormatArgumentData.ArgumentValueInt = 0
        FormatArgumentData.ArgumentValueFloat = 0
        FormatArgumentData.ArgumentValueGender = 0
        Array: List[FormatArgumentData] = [FormatArgumentData]
        ReturnValue_2: FText = Default__KismetTextLibrary.Format("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 490, 'Value': '={Answer}'}", Array)
        self.mMathResult.SetText(ReturnValue_2)
        # End
        # Label 561
        self.mMathResult.SetVisibility(1)
        # End
        # Label 604
        self.mMathResult.SetText("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 641, 'Value': '= ?'}")
    

    def IsMathExpression(self, mSearchWords: FString):
        ExecutionFlow.Push("L431")
        Variable: int32 = 0
        Variable_0: int32 = 0
        
        # Label 51
        ReturnValue: int32 = len(self.mMathSymbols)
        ReturnValue_0: bool = Variable <= ReturnValue
        if not ReturnValue_0:
            goto('L341')
        Variable_0 = Variable
        ExecutionFlow.Push("L357")
        
        Item = None
        # Label 194
        Item = self.mMathSymbols[Variable_0]
        ReturnValue_1: bool = Default__KismetStringLibrary.Contains(mSearchWords, Item, False, False)
        if not ReturnValue_1:
           goto(ExecutionFlow.Pop())
        ReturnValue_2: bool = True
        goto('L431')
        # Label 341
        ReturnValue_2 = False
        goto('L431')
        # Label 357
        ReturnValue_3: int32 = Variable + 1
        Variable = ReturnValue_3
        goto('L51')
    

    def OnPartSelected(self, product: TSubclassOf[FGItemDescriptor]):
        self.SetQuickSearchVisibility(False)
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        # Label 39
        ReturnValue_0: Ptr[Widget_Codex_Container] = Default__WidgetBlueprintLibrary.Create(self, Widget_Codex_Container, ReturnValue)
        Default__KismetSystemLibrary.SetClassPropertyByName(ReturnValue_0, "mOpenOnRecipe", product)
        ReturnValue1: Ptr[PlayerController] = self.GetOwningPlayer()
        Default__BPHUDHelpers.PushStackWidget(ReturnValue1, ReturnValue_0, self)
    

    def OnBuildingSelected(self, product: TSubclassOf[FGItemDescriptor]):
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_0: Ptr[FGRecipeManager] = Default__FGRecipeManager.Get(ReturnValue)
        ReturnValue_1: List[TSubclassOf[FGRecipe]] = ReturnValue_0.FindRecipesByProduct(product)
        ReturnValue_2: Ptr[Pawn] = self.GetOwningPlayerPawn()
        Player: Ptr[FGCharacterPlayer] = Cast[FGCharacterPlayer](ReturnValue_2)
        bSuccess: bool = Player
        if not bSuccess:
            goto('L484')
        ReturnValue_3: bool = Player.IsBuildGunEquipped()
        if not ReturnValue_3:
            goto('L447')
        
        Item = None
        # Label 289
        Item = ReturnValue_1[0]
        ReturnValue_4: Ptr[FGBuildGun] = Player.GetBuildGun()
        # Label 386
        ReturnValue_4.GotoBuildState(Item)
        self.SetQuickSearchVisibility(False)
        # End
        # Label 447
        Player.ToggleBuildGun()
        goto('L289')
    

    def OnIndexClicked(self, index: int32, ListButton: Ptr[Widget_ListButton]):
        self.SetSelectedIndex(index)
        
        Item = None
        Item = self.mSearchResults[index]
        SelectedProduct = Item
        
        ReturnValue1: bool = Default__KismetArrayLibrary.Array_Contains(Ref[self.mBuildings], Ref[SelectedProduct])
        if not ReturnValue1:
            goto('L203')
        self.OnBuildingSelected(SelectedProduct)
        # End
        
        # Label 203
        ReturnValue: bool = Default__KismetArrayLibrary.Array_Contains(Ref[self.mProducts], Ref[SelectedProduct])
        if not ReturnValue:
            goto('L300')
        self.OnPartSelected(SelectedProduct)
    

    def SetSelectedIndex(self, NewSelectedIndex: int32):
        ReturnValue1: int32 = self.mSearchResultsContainer.GetChildrenCount()
        ReturnValue: bool = self.mSelectedIndex <= ReturnValue1
        if not ReturnValue:
            goto('L265')
        ReturnValue1_0: Ptr[Widget] = self.mSearchResultsContainer.GetChildAt(self.mSelectedIndex)
        Button1: Ptr[Widget_ListButton] = Cast[Widget_ListButton](ReturnValue1_0)
        bSuccess1: bool = Button1
        if not bSuccess1:
            goto('L265')
        Button1.mIsSelected = False
        # Label 265
        ReturnValue_0: int32 = self.mSearchResultsContainer.GetChildrenCount()
        ReturnValue_1: int32 = ReturnValue_0 - 1
        # Label 357
        ReturnValue_2: int32 = Clamp(NewSelectedIndex, 0, ReturnValue_1)
        self.mSelectedIndex = ReturnValue_2
        ReturnValue_3: Ptr[Widget] = self.mSearchResultsContainer.GetChildAt(self.mSelectedIndex)
        Button: Ptr[Widget_ListButton] = Cast[Widget_ListButton](ReturnValue_3)
        bSuccess: bool = Button
        if not bSuccess:
            goto('L598')
        Button.mIsSelected = True
    

    def OnKeyUp(self):
        
        ReturnValue: Key = Default__KismetInputLibrary.GetKey(Ref[InKeyEvent])
        ReturnValue3: bool = Default__KismetInputLibrary.EqualEqual_KeyKey(ReturnValue, Key(KeyName = "Up"))
        if not ReturnValue3:
            goto('L286')
        ReturnValue_0: int32 = self.mSelectedIndex - 1
        self.SetSelectedIndex(ReturnValue_0)
        ReturnValue1: Ptr[PlayerController] = self.GetOwningPlayer()
        self.mSearchField.SetUserFocus(ReturnValue1)
        goto('L1000')
        
        # Label 286
        ReturnValue = Default__KismetInputLibrary.GetKey(Ref[InKeyEvent])
        ReturnValue2: bool = Default__KismetInputLibrary.EqualEqual_KeyKey(ReturnValue, Key(KeyName = "Down"))
        if not ReturnValue2:
            goto('L572')
        ReturnValue_1: int32 = self.mSelectedIndex + 1
        self.SetSelectedIndex(ReturnValue_1)
        ReturnValue_2: Ptr[PlayerController] = self.GetOwningPlayer()
        self.mSearchField.SetUserFocus(ReturnValue_2)
        goto('L1000')
        
        # Label 572
        ReturnValue = Default__KismetInputLibrary.GetKey(Ref[InKeyEvent])
        ReturnValue1_0: bool = Default__KismetInputLibrary.EqualEqual_KeyKey(ReturnValue, Key(KeyName = "Enter"))
        if not ReturnValue1_0:
            goto('L752')
        self.OnIndexClicked(self.mSelectedIndex, None)
        goto('L1000')
        
        # Label 752
        ReturnValue = Default__KismetInputLibrary.GetKey(Ref[InKeyEvent])
        ReturnValue_3: bool = Default__KismetInputLibrary.EqualEqual_KeyKey(ReturnValue, Key(KeyName = "Escape"))
        if not ReturnValue_3:
            goto('L923')
        self.SetQuickSearchVisibility(False)
        goto('L1000')
        # Label 923
        ReturnValue_4: EventReply = Default__WidgetBlueprintLibrary.Unhandled()
        ReturnValue_5: EventReply = ReturnValue_4
    

    def CreateSearchResultList(self, SearchWords: FString):
        ExecutionFlow.Push("L997")
        self.mSearchResultsContainer.ClearChildren()
        self.GenerateMathAnswer(SearchWords)
        self.GenerateSearchResults(SearchWords)
        Variable: int32 = 0
        Variable_0: int32 = 0
        
        # Label 133
        ReturnValue: int32 = len(self.mSearchResults)
        ReturnValue_0: bool = Variable <= ReturnValue
        if not ReturnValue_0:
           goto(ExecutionFlow.Pop())
        Variable_0 = Variable
        ExecutionFlow.Push("L923")
        ReturnValue_1: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_2: Ptr[Widget_ListButton] = Default__WidgetBlueprintLibrary.Create(self, Widget_ListButton, ReturnValue_1)
        
        Item = None
        # Label 357
        Item = self.mSearchResults[Variable_0]
        ReturnValue_3: Ptr[Texture2D] = Default__FGItemDescriptor.GetSmallIcon(Item)
        Default__KismetSystemLibrary.SetObjectPropertyByName(ReturnValue_2, "mIcon", ReturnValue_3)
        
        Item = None
        Item = self.mSearchResults[Variable_0]
        ReturnValue_4: FText = Default__FGItemDescriptor.GetItemName(Item)
        
        Default__KismetSystemLibrary.SetTextPropertyByName(ReturnValue_2, "mTitle", Ref[ReturnValue_4])
        ReturnValue_5: Ptr[PanelSlot] = self.mSearchResultsContainer.AddChild(ReturnValue_2)
        OutputDelegate.BindUFunction(self, OnIndexClicked)
        ReturnValue_2.OnClicked.AddUnique(OutputDelegate)
        ReturnValue_6: bool = EqualEqual_IntInt(Variable_0, 0)
        if not ReturnValue_6:
           goto(ExecutionFlow.Pop())
        ReturnValue_2.mIsSelected = True
        self.SetSelectedIndex(0)
        goto(ExecutionFlow.Pop())
        # Label 923
        ReturnValue_7: int32 = Variable + 1
        Variable = ReturnValue_7
        goto('L133')
    

    def GenerateSearchResults(self, SearchWords: FString):
        ExecutionFlow.Push("L978")
        
        Default__KismetArrayLibrary.Array_Clear(Ref[self.mSearchResults])
        ReturnValue: bool = Default__KismetStringLibrary.NotEqual_StrStr(SearchWords, "")
        if not ReturnValue:
           goto(ExecutionFlow.Pop())
        Variable: bool = False
        Variable_0: int32 = 0
        Variable_1: int32 = 0
        # Label 166
        ReturnValue_0: bool = Not_PreBool(Variable)
        
        ReturnValue_1: int32 = len(self.mProducts)
        ReturnValue_2: bool = Variable_0 <= ReturnValue_1
        ReturnValue_3: bool = ReturnValue_0 and ReturnValue_2
        if not ReturnValue_3:
            goto('L872')
        Variable_1 = Variable_0
        ExecutionFlow.Push("L904")
        
        Item = None
        Item = self.mProducts[Variable_1]
        localProduct = Item
        ReturnValue_4: FText = Default__FGItemDescriptor.GetItemName(localProduct)
        
        ReturnValue_5: FString = Default__KismetTextLibrary.Conv_TextToString(Ref[ReturnValue_4])
        # Label 572
        ReturnValue_6: bool = Default__BPHUDHelpers.DoesTextContainSearchWords(ReturnValue_5, SearchWords, True, self)
        if not ReturnValue_6:
           goto(ExecutionFlow.Pop())
        
        ReturnValue_7: int32 = LocalSearchResults.append(localProduct)
        ReturnValue_8: int32 = LocalResultCounter + 1
        Variable_2: int32 = ReturnValue_8
        LocalResultCounter = Variable_2
        ReturnValue_9: bool = GreaterEqual_IntInt(Variable_2, self.mMaxAmountOfResults)
        if not ReturnValue_9:
           goto(ExecutionFlow.Pop())
        Variable = True
        goto(ExecutionFlow.Pop())
        # Label 872
        self.mSearchResults = LocalSearchResults
        # End
        # Label 904
        ReturnValue1: int32 = Variable_0 + 1
        Variable_0 = ReturnValue1
        goto('L166')
    

    def InitAllRecipes(self):
        ExecutionFlow.Push("L1579")
        ReturnValue: Ptr[GameStateBase] = Default__GameplayStatics.GetGameState(self)
        ReturnValue_0: Ptr[FGRecipeManager] = Default__FGRecipeManager.Get(ReturnValue)
        recipes: List[TSubclassOf[FGRecipe]] = []
        
        ReturnValue_0.GetAllAvailableRecipes(Ref[recipes])
        Variable: int32 = 0
        Variable1: int32 = 0
        
        # Label 197
        ReturnValue_1: int32 = len(recipes)
        ReturnValue_2: bool = Variable <= ReturnValue_1
        if not ReturnValue_2:
            goto('L930')
        Variable1 = Variable
        ExecutionFlow.Push("L1066")
        Variable1_0: int32 = 0
        Variable_0: int32 = 0
        
        Item = None
        # Label 386
        Item = recipes[Variable1]
        ReturnValue_3: List[ItemAmount] = Default__FGRecipe.GetProducts(Item, False)
        
        ReturnValue1: int32 = len(ReturnValue_3)
        ReturnValue1_0: bool = Variable1_0 <= ReturnValue1
        if not ReturnValue1_0:
           goto(ExecutionFlow.Pop())
        Variable_0 = Variable1_0
        ExecutionFlow.Push("L1140")
        
        Item = None
        Item = recipes[Variable1]
        ReturnValue_3 = Default__FGRecipe.GetProducts(Item, False)
        
        Item1 = None
        Item1 = ReturnValue_3[Variable_0]
        LocalClass = Item1.ItemClass
        Descriptor: TSubclassOf[FGResourceDescriptor] = ClassCast[FGResourceDescriptor](LocalClass)
        bSuccess: bool = Descriptor
        if not bSuccess:
            goto('L1214')
        goto(ExecutionFlow.Pop())
        # Label 930
        self.mBuildings = LocalBuildings
        self.mParts = LocalParts
        self.mProducts = LocalBuildings
        
        Default__KismetArrayLibrary.Array_Append(Ref[self.mProducts], Ref[LocalParts])
        # End
        # Label 1066
        ReturnValue_4: int32 = Variable + 1
        Variable = ReturnValue_4
        goto('L197')
        # Label 1140
        ReturnValue1_1: int32 = Variable1_0 + 1
        Variable1_0 = ReturnValue1_1
        goto('L386')
        # Label 1214
        Descriptor_0: TSubclassOf[FGBuildingDescriptor] = ClassCast[FGBuildingDescriptor](LocalClass)
        bSuccess2: bool = Descriptor_0
        if not bSuccess2:
            goto('L1362')
        
        ReturnValue1_2: int32 = Default__KismetArrayLibrary.Array_AddUnique(Ref[LocalBuildings], Ref[LocalClass])
        goto(ExecutionFlow.Pop())
        # Label 1362
        Descriptor_1: TSubclassOf[FGVehicleDescriptor] = ClassCast[FGVehicleDescriptor](LocalClass)
        bSuccess1: bool = Descriptor_1
        if not bSuccess1:
            goto('L1510')
        
        ReturnValue_5: int32 = Default__KismetArrayLibrary.Array_AddUnique(Ref[LocalBuildings], Ref[LocalClass])
        goto(ExecutionFlow.Pop())
        
        # Label 1510
        ReturnValue2: int32 = Default__KismetArrayLibrary.Array_AddUnique(Ref[LocalParts], Ref[LocalClass])
        goto(ExecutionFlow.Pop())
    

    def BndEvt__mCloseButton_K2Node_ComponentBoundEvent_2_OnButtonClickedEvent__DelegateSignature(self):
        self.ExecuteUbergraph_BPW_QuickSearch(116)
    

    def BndEvt__FGEditableText_357_K2Node_ComponentBoundEvent_3_OnEditableTextChangedEvent__DelegateSignature(self, text: Const[Ref[FText]]):
        ExecuteUbergraph_BPW_QuickSearch.K2Node_ComponentBoundEvent_Text1 = text #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BPW_QuickSearch(198)
    

    def BndEvt__FGEditableText_357_K2Node_ComponentBoundEvent_4_OnEditableTextCommittedEvent__DelegateSignature(self, text: Const[Ref[FText]], CommitMethod: uint8):
        ExecuteUbergraph_BPW_QuickSearch.K2Node_ComponentBoundEvent_Text = text #  PERSISTENT_FRAME(
        ExecuteUbergraph_BPW_QuickSearch.K2Node_ComponentBoundEvent_CommitMethod = CommitMethod #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BPW_QuickSearch(289)
    

    def ExecuteUbergraph_BPW_QuickSearch(self):
        goto(ComputedJump("EntryPoint"))
        self.CreateSearchResultList(self.mSearchWords)
        goto(ExecutionFlow.Pop())
        # Label 39
        Default__KismetSystemLibrary.RetriggerableDelay(self, 0.10000000149011612, LatentActionInfo(Linkage = 15, UUID = 1717044286, ExecutionFunction = "ExecuteUbergraph_BPW_QuickSearch", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        self.SetQuickSearchVisibility(False)
        goto(ExecutionFlow.Pop())
        # Label 132
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        self.mSearchField.SetUserFocus(ReturnValue)
        # Label 197
        goto(ExecutionFlow.Pop())
        
        Text1 = None
        ReturnValue_0: FString = Default__KismetTextLibrary.Conv_TextToString(Ref[Text1])
        self.mSearchWords = ReturnValue_0
        goto('L39')
        # Label 289
        CmpSuccess: bool = NotEqual_ByteByte(CommitMethod, 1)
        if not CmpSuccess:
            goto('L132')
        goto(ExecutionFlow.Pop())
    
