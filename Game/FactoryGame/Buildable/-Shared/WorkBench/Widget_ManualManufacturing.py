
from codegen.ue4_stub import *

from Script.FactoryGame import GetCurrentFatigue
from Script.FactoryGame import FGCharacterPlayer
from Game.FactoryGame.Buildable.-Shared.WorkBench.Widget_ManualManufacturing import ExecuteUbergraph_Widget_ManualManufacturing.K2Node_CustomEvent_dt
from Script.UMG import GetChildIndex
from Script.UMG import OverlaySlot
from Script.InputCore import Key
from Game.FactoryGame.Interface.UI.InGame.Widget_RecipeButton import Widget_RecipeButton
from Script.UMG import AddChild
from Script.Engine import Array_Set
from Script.FactoryGame import GetCollapsedItemCategories
from Script.FactoryGame import GetProducts
from Script.Engine import Default__KismetSystemLibrary
from Script.UMG import GetChildAt
from Script.Engine import NotEqual_ClassClass
from Script.Engine import Array_Find
from Game.FactoryGame.Buildable.-Shared.WorkBench.ItemCategoryRecipeStruct import ItemCategoryRecipeStruct
from Script.Engine import FormatArgumentData
from Script.UMG import ESlateVisibility
from Game.FactoryGame.Buildable.Factory.WorkBench.Audio.Rework_Click.Play_Switch_AnvilType import Play_Switch_AnvilType
from Game.FactoryGame.Interface.UI.InGame.Widget_CostSlot import Widget_CostSlot
from Script.Engine import TimerHandle
from Script.UMG import StopAnimation
from Script.FactoryGame import GetIngredients
from Script.Engine import IsValid
from Script.UMG import SetPercent
from Script.Engine import Conv_IntToText
from Script.UMG import SetColorAndOpacity
from Script.UMG import Destruct
from Script.Engine import EqualEqual_IntInt
from Script.Engine import Default__KismetTextLibrary
from Game.FactoryGame.Buildable.-Shared.WorkBench.Widget_ManualManufacturing import ExecuteUbergraph_Widget_ManualManufacturing.K2Node_CustomEvent_mNewRecipe
from Script.Engine import Conv_StringToText
from Script.UMG import SetFillColorAndOpacity
from Script.Engine import NotEqual_FloatFloat
from Script.UMG import Construct
from Game.FactoryGame.Buildable.-Shared.WorkBench.Widget_ManualManufacturing import ExecuteUbergraph_Widget_ManualManufacturing.K2Node_Event_InDeltaTime
from Script.Engine import NotEqual_IgnoreCase_TextText
from Script.FactoryGame import GetCategoriesWithAffordableRecipes
from Script.Engine import Conv_BoolToString
from Script.Engine import Default__KismetStringLibrary
from Script.Engine import RetriggerableDelay
from Script.UMG import UserWidget
from Script.Engine import NotEqual_ObjectObject
from Game.FactoryGame.Interface.UI.HUDHelpers.HUDHelpers import Default__HUDHelpers
from Script.UMG import Create
from Script.FactoryGame import GetManufacturingDuration
from Script.FactoryGame import GetItemCategory
from Script.Engine import GetGameState
from Script.FactoryGame import InventoryItem
from Script.Engine import Round
from Game.FactoryGame.Character.Player.BP_PlayerController import BP_PlayerController
from Script.Engine import K2_ClearAndInvalidateTimerHandle
from Script.Engine import GetComponentsByClass
from Script.CoreUObject import LinearColor
from Script.FactoryGame import OnReleasedButton
from Script.Engine import EqualEqual_ClassClass
from Script.Engine import NotEqual_BoolBool
from Script.Engine import SetClassPropertyByName
from Script.FactoryGame import MakeInventoryStack
from Game.FactoryGame.Buildable.-Shared.WorkBench.Widget_ManualManufacturing import ExecuteUbergraph_Widget_ManualManufacturing.K2Node_ComponentBoundEvent_Text
from Script.FactoryGame import FGWorkBench
from Script.Engine import FClamp
from Script.AkAudio import SetActorRTPCValue
from Script.Engine import SetObjectPropertyByName
from Script.Engine import Pawn
from Script.UMG import GetChildrenCount
from Script.FactoryGame import GetManufacturingProgress
from Game.FactoryGame.Buildable.Factory.WorkBench.Audio.Rework_Click.Play_WorkBench_Nani import Play_WorkBench_Nani
from Script.FactoryGame import SetItemCategoryCollapsed
from Script.Engine import SetStructurePropertyByName
from Script.Engine import Default__KismetArrayLibrary
from Script.Engine import GameStateBase
from Script.UMG import SetRenderTranslation
from Script.FactoryGame import GetInventory
from Script.Engine import GetObjectClass
from Script.CoreUObject import Object
from Script.FactoryGame import FGInventoryComponent
from Script.FactoryGame import Default__FGRecipeManager
from Script.FactoryGame import GetCurrentRecipe
from Script.FactoryGame import Default__FGRecipe
from Game.FactoryGame.Character.Player.Char_Player import Char_Player
from Game.FactoryGame.Buildable.-Shared.WorkBench.Widget_ManualManufacturing import ExecuteUbergraph_Widget_ManualManufacturing.K2Node_CustomEvent_ProduceSpeed
from Script.FactoryGame import Default__FGItemCategory
from Game.FactoryGame.Buildable.-Shared.WorkBench.Widget_ManualManufacturing_Container import Widget_ManualManufacturing_Container
from Game.FactoryGame.Buildable.-Shared.WorkBench.Widget_ManualManufacturing import ExecuteUbergraph_Widget_ManualManufacturing
from Script.Engine import GetKey
from Script.AkAudio import Default__AkGameplayStatics
from Script.UMG import WrapBoxSlot
from Script.Engine import EqualEqual_KeyKey
from Script.FactoryGame import SetWorkBenchUser
from Game.FactoryGame.Interface.UI.HUDHelpers.BPHUDHelpers import Default__BPHUDHelpers
from Script.FactoryGame import SetOnlyShowAffordableRecipes
from Script.FactoryGame import Default__FGItemDescriptor
from Script.FactoryGame import FGRecipe
from Script.FactoryGame import GetAvailableRecipesForProducer
from Script.FactoryGame import ItemAmount
from Script.AkAudio import AkComponent
from Script.Engine import PrintString
from Script.UMG import EventReply
from Script.UMG import SetUserFocus
from Script.Engine import SetTextPropertyByName
from Script.FactoryGame import Produce
from Script.AkAudio import PostAkEvent
from Game.FactoryGame.Buildable.Factory.WorkBench.Audio.Stop_F_WorkBench import Stop_F_WorkBench
from Script.Engine import Delay
from Script.Engine import K2_SetTimerDelegate
from Script.UMG import GetEndTime
from Script.Engine import Array_Contains
from Script.FactoryGame import FGPlayerState
from Game.FactoryGame.Buildable.Factory.WorkBench.Audio.Play_F_WorkBench import Play_F_WorkBench
from Script.UMG import PanelSlot
from Script.FactoryGame import Default__FGInventoryLibrary
from Script.FactoryGame import HasEnoughSpaceForStack
from Script.Engine import Conv_IntToFloat
from Script.Engine import LatentActionInfo
from Script.FactoryGame import GetCategoryName
from Script.AkAudio import SetSwitch
from Script.FactoryGame import Get
from Script.Engine import PlayerController
from Script.UMG import PlayAnimation
from Script.UMG import Unhandled
from Game.FactoryGame.Buildable.-Shared.WorkBench.BP_ManualManufacturingComponent import BP_ManualManufacturingComponent
from Game.FactoryGame.Buildable.-Shared.WorkBench.Widget_ManualManufacturing import ExecuteUbergraph_Widget_ManualManufacturing.K2Node_CustomEvent_Instigator
from Script.Engine import EqualEqual_StriStri
from Script.UMG import Default__WidgetBlueprintLibrary
from Script.FactoryGame import GetAllWidgetsOfClassInHierarchy
from Script.UMG import AddChildToWrapBox
from Script.Engine import CurveFloat
from Script.Engine import SetBoolPropertyByName
from Script.Engine import Default__GameplayStatics
from Script.FactoryGame import GetManualManufacturingDuration
from Game.FactoryGame.Interface.UI.Audio.Overclocking.Play_UI_OverClock_Tick import Play_UI_OverClock_Tick
from Script.Engine import Format
from Game.FactoryGame.Interface.UI.InGame.-Shared.Widget_Smoke import Widget_Smoke
from Script.FactoryGame import CanProduce
from Script.FactoryGame import SetRecipe
from Script.FactoryGame import Default__FGBlueprintFunctionLibrary
from Game.FactoryGame.Resource.ItemCategories.Cat_Other import Cat_Other
from Script.FactoryGame import GetRemoteCallObjectOfClass
from Script.Engine import RandomIntegerInRange
from Script.Engine import NearlyEqual_FloatFloat
from Script.FactoryGame import GetRecipeName
from Script.CoreUObject import Vector2D
from Script.FactoryGame import SetupManufacturingButton
from Script.FactoryGame import InventoryStack
from Game.FactoryGame.Character.Player.BP_RemoteCallObject import BP_RemoteCallObject
from Script.Engine import Default__KismetInputLibrary
from Script.Engine import RandomFloatInRange
from Script.Engine import Conv_TextToString
from Game.FactoryGame.Buildable.-Shared.WorkBench.Widget_ManualManufacturing import ExecuteUbergraph_Widget_ManualManufacturing.K2Node_ComponentBoundEvent_IsChecked
from Script.FactoryGame import GetOnlyShowAffordableRecipes
from Script.FactoryGame import FGItemCategory
from Script.FactoryGame import GetManufacturingSpeed
from Game.FactoryGame.Buildable.-Shared.WorkBench.Widget_ManualManufacturing import Widget_ManualManufacturing
from Script.Engine import Not_PreBool
from Script.UMG import GetRenderOpacity
from Script.FactoryGame import GetItemName
from Script.FactoryGame import IsProducing
from Script.Engine import GetWorldDeltaSeconds
from Game.FactoryGame.Interface.UI.Assets.Shared.Widget_CraftBench_Category import Widget_CraftBench_Category
from Game.FactoryGame.Buildable.-Shared.WorkBench.Widget_ManualManufacturing import ExecuteUbergraph_Widget_ManualManufacturing.K2Node_Event_MyGeometry
from Script.Engine import BooleanOR
from Script.UMG import Tick
from Script.UMG import Widget
from Script.FactoryGame import MakeInventoryItem
from Script.UMG import WidgetAnimation
from Script.UMG import GetOwningPlayerPawn
from Game.FactoryGame.Widget_SmallCostslot import Widget_SmallCostSlot
from Script.Engine import Actor
from Script.Engine import EqualEqual_TextText
from Script.UMG import UMGSequencePlayer
from Script.UMG import IsAnimationPlaying
from Script.FactoryGame import FGRecipeManager
from Script.UMG import SetRenderOpacity
from Script.Engine import IsValidClass
from Script.Engine import GetFloatValue
from Script.UMG import AddChildToOverlay

class Widget_ManualManufacturing(UserWidget):
    AddedToInventoryPulse: Ptr[WidgetAnimation]
    HideAddedToInventory: Ptr[WidgetAnimation]
    LEDAnim: Ptr[WidgetAnimation]
    ButtonGlow: Ptr[WidgetAnimation]
    OutputPulse: Ptr[WidgetAnimation]
    GlowPanelFade: Ptr[WidgetAnimation]
    NANI?: Ptr[WidgetAnimation]
    SuperClickAnim: Ptr[WidgetAnimation]
    ShakeCostSlotAnim: Ptr[WidgetAnimation]
    mManualManufacturerComponent: Ptr[FGWorkBench]
    isWorkingAtWorkbench: bool
    mCurrentRecipe: TSubclassOf[FGRecipe]
    mInteractObject: Ptr[Object]
    IsProducing: bool
    mProgressBarCurve: Ptr[CurveFloat] = Namespace(AssetPath='/Game/FactoryGame/Buildable/-Shared/Curves/TestCurve.TestCurve')
    mProgressBarEndCurve: Ptr[CurveFloat]
    ProgressbarStep: int32 = -1
    Manufacturing_Container: Ptr[Widget_ManualManufacturing_Container]
    mHoldTimer: TimerHandle
    LastClickTime: float
    ClickCounter: int32
    InGameTime: float
    GlowFadeStop: bool
    GlowMin: float = -0.25
    ShakeActive: bool
    ShakeIntesity: float
    mGlowRTPC: float
    mIsHolding: bool
    DelayActive: bool = True
    DelayCounter: int32
    mWarningMessageTimerHandle: TimerHandle
    mDelayHandle: TimerHandle
    DelayTime: float = 0.10000000149011612
    AddedToInventoryBuffer: int32
    mCategorizedRecipes: List[ItemCategoryRecipeStruct]
    mCurrentCategoryWidget: Ptr[Widget_CraftBench_Category]
    OnRelevantClassesUpdated: FMulticastScriptDelegate
    
    def UpdateRelevantClasses(self):
        ExecutionFlow.Push("L1072")
        Variable: int32 = 0
        Variable_0: int32 = 0
        # Label 51
        ReturnValue: List[ItemAmount] = Default__FGRecipe.GetIngredients(self.mCurrentRecipe)
        
        # Label 110
        ReturnValue1: int32 = len(ReturnValue)
        ReturnValue1_0: bool = Variable <= ReturnValue1
        if not ReturnValue1_0:
            goto('L449')
        Variable_0 = Variable
        ExecutionFlow.Push("L924")
        ReturnValue = Default__FGRecipe.GetIngredients(self.mCurrentRecipe)
        
        Item1 = None
        Item1 = ReturnValue[Variable_0]
        
        Item1.ItemClass = None
        ReturnValue1_1: int32 = LocalRelevantClasses.append(Item1.ItemClass)
        goto(ExecutionFlow.Pop())
        # Label 449
        Variable1: int32 = 0
        Variable1_0: int32 = 0
        # Label 495
        ReturnValue_0: List[ItemAmount] = Default__FGRecipe.GetProducts(self.mCurrentRecipe, False)
        
        ReturnValue_1: int32 = len(ReturnValue_0)
        ReturnValue_2: bool = Variable1 <= ReturnValue_1
        if not ReturnValue_2:
            goto('L895')
        Variable1_0 = Variable1
        ExecutionFlow.Push("L998")
        ReturnValue_0 = Default__FGRecipe.GetProducts(self.mCurrentRecipe, False)
        
        Item = None
        Item = ReturnValue_0[Variable1_0]
        
        Item.ItemClass = None
        ReturnValue_3: int32 = LocalRelevantClasses.append(Item.ItemClass)
        goto(ExecutionFlow.Pop())
        # Label 895
        self.OnRelevantClassesUpdated.ProcessMulticastDelegate(Ref[LocalRelevantClasses])
        goto(ExecutionFlow.Pop())
        # Label 924
        ReturnValue_4: int32 = Variable + 1
        Variable = ReturnValue_4
        goto('L51')
        # Label 998
        ReturnValue1_2: int32 = Variable1 + 1
        Variable1 = ReturnValue1_2
        goto('L495')
    

    def OnMouseButtonDown(self):
        self.Widget_UI_ParticleManager.CreateParticle()
        ReturnValue: EventReply = Default__WidgetBlueprintLibrary.Unhandled()
        ReturnValue_0: EventReply = ReturnValue
    

    def UpdateAffordableCategories(self):
        ExecutionFlow.Push("L795")
        ReturnValue: TSubclassOf[FGWorkBench] = Default__GameplayStatics.GetObjectClass(self.mManualManufacturerComponent)
        ReturnValue_0: Ptr[Pawn] = self.GetOwningPlayerPawn()
        Player: Ptr[FGCharacterPlayer] = Cast[FGCharacterPlayer](ReturnValue_0)
        bSuccess: bool = Player
        ReturnValue_1: List[TSubclassOf[FGItemCategory]] = Default__FGBlueprintFunctionLibrary.GetCategoriesWithAffordableRecipes(Player, ReturnValue)
        AffordableRecipes = ReturnValue_1
        Variable: int32 = 0
        Variable_0: int32 = 0
        
        # Label 282
        ReturnValue_2: int32 = len(self.mCategorizedRecipes)
        ReturnValue_3: bool = Variable <= ReturnValue_2
        if not ReturnValue_3:
           goto(ExecutionFlow.Pop())
        Variable_0 = Variable
        ExecutionFlow.Push("L721")
        ReturnValue_4: Ptr[Widget] = self.mPhase0ScrollBox.GetChildAt(Variable_0)
        Category: Ptr[Widget_CraftBench_Category] = Cast[Widget_CraftBench_Category](ReturnValue_4)
        bSuccess1: bool = Category
        if not bSuccess1:
           goto(ExecutionFlow.Pop())
        
        Item = None
        Item = self.mCategorizedRecipes[Variable_0]
        
        Item.Category_5_48CE2A3C41089DC1E5DE39909CF17792 = None
        ReturnValue_5: bool = Default__KismetArrayLibrary.Array_Contains(Ref[AffordableRecipes], Ref[Item.Category_5_48CE2A3C41089DC1E5DE39909CF17792])
        Category.SetHasAffordableRecipes(ReturnValue_5)
        goto(ExecutionFlow.Pop())
        # Label 721
        ReturnValue_6: int32 = Variable + 1
        Variable = ReturnValue_6
        goto('L282')
    

    def GetCategoryWidgetFromRecipe(self, Recipe: TSubclassOf[FGRecipe]):
        ExecutionFlow.Push("L1021")
        LocalIndex = -1
        Variable: bool = False
        Variable_0: int32 = 0
        Variable_1: int32 = 0
        # Label 85
        ReturnValue: bool = Not_PreBool(Variable)
        
        ReturnValue_0: int32 = len(self.mCategorizedRecipes)
        ReturnValue_1: bool = Variable_0 <= ReturnValue_0
        # Label 211
        ReturnValue_2: bool = ReturnValue and ReturnValue_1
        if not ReturnValue_2:
            goto('L625')
        Variable_1 = Variable_0
        ExecutionFlow.Push("L947")
        ReturnValue_3: List[ItemAmount] = Default__FGRecipe.GetProducts(Recipe, False)
        
        Item = None
        # Label 355
        Item = ReturnValue_3[0]
        ReturnValue_4: TSubclassOf[FGItemCategory] = Default__FGItemDescriptor.GetItemCategory(Item.ItemClass)
        
        Item1 = None
        # Label 470
        Item1 = self.mCategorizedRecipes[Variable_1]
        ReturnValue_5: bool = EqualEqual_ClassClass(Item1.Category_5_48CE2A3C41089DC1E5DE39909CF17792, ReturnValue_4)
        if not ReturnValue_5:
           goto(ExecutionFlow.Pop())
        # Label 586
        LocalIndex = Variable_1
        Variable = True
        goto(ExecutionFlow.Pop())
        # Label 625
        Variable_2: Ptr[Widget_CraftBench_Category] = None
        Variable1: Ptr[Widget] = None
        ReturnValue_6: Ptr[Widget] = self.mPhase0ScrollBox.GetChildAt(LocalIndex)
        ReturnValue_7: bool = LocalIndex != -1
        Variable_3: bool = ReturnValue_7
        
        switch = {
            False: Variable1,
            True: ReturnValue_6
        }
        Category: Ptr[Widget_CraftBench_Category] = Cast[Widget_CraftBench_Category](switch.get(Variable_3, None))
        bSuccess: bool = Category
        Variable1_0: bool = bSuccess
        
        switch_0 = {
            False: Variable_2,
            True: Category
        }
        ReturnValue_8: Ptr[Widget_CraftBench_Category] = switch_0.get(Variable1_0, None)
        goto('L1021')
        # Label 947
        ReturnValue_9: int32 = Variable_0 + 1
        Variable_0 = ReturnValue_9
        goto('L85')
    

    def AddUniqueRecipe(self, CategorizedRecipes: Ref[List[ItemCategoryRecipeStruct]], Recipe: TSubclassOf[FGRecipe]):
        ExecutionFlow.Push("L1422")
        ReturnValue: List[ItemAmount] = Default__FGRecipe.GetProducts(Recipe, False)
        
        Item = None
        Item = ReturnValue[0]
        ReturnValue_0: TSubclassOf[FGItemCategory] = Default__FGItemDescriptor.GetItemCategory(Item.ItemClass)
        ReturnValue_1: bool = Default__KismetSystemLibrary.IsValidClass(ReturnValue_0)
        if not ReturnValue_1:
            goto('L1132')
        ReturnValue = Default__FGRecipe.GetProducts(Recipe, False)
        
        Item = None
        Item = ReturnValue[0]
        ReturnValue_0 = Default__FGItemDescriptor.GetItemCategory(Item.ItemClass)
        LocalCategory = ReturnValue_0
        # Label 439
        Variable: bool = False
        Variable_0: int32 = 0
        Variable_1: int32 = 0
        # Label 496
        ReturnValue_2: bool = Not_PreBool(Variable)
        
        ReturnValue_3: int32 = len(CategorizedRecipes)
        ReturnValue_4: bool = Variable_0 <= ReturnValue_3
        ReturnValue_5: bool = ReturnValue_2 and ReturnValue_4
        # Label 660
        if not ReturnValue_5:
            goto('L1156')
        Variable_1 = Variable_0
        ExecutionFlow.Push("L1348")
        
        Item1 = None
        Item1 = CategorizedRecipes[Variable_1]
        ReturnValue_6: bool = EqualEqual_ClassClass(LocalCategory, Item1.Category_5_48CE2A3C41089DC1E5DE39909CF17792)
        if not ReturnValue_6:
           goto(ExecutionFlow.Pop())
        
        Item1 = None
        Item1 = CategorizedRecipes[Variable_1]
        localRecipeArray = Item1.Recipes_6_5C2C7BF54D78A483A81B2785C2CF7736
        
        ReturnValue1: int32 = localRecipeArray.append(Recipe)
        ItemCategoryRecipeStruct.Category_5_48CE2A3C41089DC1E5DE39909CF17792 = LocalCategory
        ItemCategoryRecipeStruct.Recipes_6_5C2C7BF54D78A483A81B2785C2CF7736 = localRecipeArray
        
        ItemCategoryRecipeStruct = None
        Default__KismetArrayLibrary.Array_Set(Variable_1, False, Ref[CategorizedRecipes], Ref[ItemCategoryRecipeStruct])
        RecipeExists = True
        Variable = True
        # Label 1131
        goto(ExecutionFlow.Pop())
        # Label 1132
        LocalCategory = Cat_Other
        goto('L439')
        # Label 1156
        ReturnValue1_0: bool = Not_PreBool(RecipeExists)
        if not ReturnValue1_0:
           goto(ExecutionFlow.Pop())
        Array: List[TSubclassOf[FGRecipe]] = [Recipe]
        ItemCategoryRecipeStruct1.Category_5_48CE2A3C41089DC1E5DE39909CF17792 = LocalCategory
        ItemCategoryRecipeStruct1.Recipes_6_5C2C7BF54D78A483A81B2785C2CF7736 = Array
        
        ItemCategoryRecipeStruct1 = None
        # Label 1279
        ReturnValue_7: int32 = CategorizedRecipes.append(ItemCategoryRecipeStruct1)
        goto(ExecutionFlow.Pop())
        # Label 1348
        ReturnValue_8: int32 = Variable_0 + 1
        Variable_0 = ReturnValue_8
        goto('L496')
    

    def ClearAndHideSearchResults(self):
        self.mSearchResultsBox.ClearChildren()
        self.mPhase0ScrollBox.SetVisibility(4)
    

    def OnSearchCreateResults(self, text: FText):
        ExecutionFlow.Push("L1290")
        localSearchResult = text
        ReturnValue: FText = Default__KismetTextLibrary.Conv_StringToText("")
        
        ReturnValue_0: bool = Default__KismetTextLibrary.NotEqual_IgnoreCase_TextText(Ref[localSearchResult], Ref[ReturnValue])
        if not ReturnValue_0:
            goto('L1201')
        self.mPhase0ScrollBox.SetVisibility(1)
        self.mSearchResultsBox.ClearChildren()
        Variable: int32 = 0
        Variable_0: int32 = 0
        
        AvailableRecipes = None
        # Label 278
        self.GetAvailableRecipes(Ref[AvailableRecipes])
        
        AvailableRecipes = None
        ReturnValue_1: int32 = len(AvailableRecipes)
        ReturnValue_2: bool = Variable <= ReturnValue_1
        if not ReturnValue_2:
           goto(ExecutionFlow.Pop())
        Variable_0 = Variable
        ExecutionFlow.Push("L1216")
        
        AvailableRecipes = None
        self.GetAvailableRecipes(Ref[AvailableRecipes])
        
        AvailableRecipes = None
        Item = None
        Item = AvailableRecipes[Variable_0]
        localRecipe = Item
        ReturnValue_3: bool = Default__KismetSystemLibrary.IsValidClass(localRecipe)
        if not ReturnValue_3:
           goto(ExecutionFlow.Pop())
        ReturnValue_4: FText = Default__FGRecipe.GetRecipeName(localRecipe)
        
        ReturnValue_5: FString = Default__KismetTextLibrary.Conv_TextToString(Ref[ReturnValue_4])
        
        ReturnValue1: FString = Default__KismetTextLibrary.Conv_TextToString(Ref[localSearchResult])
        ReturnValue_6: bool = Default__BPHUDHelpers.DoesTextContainSearchWords(ReturnValue_5, ReturnValue1, True, self)
        ReturnValue_7: bool = Default__KismetStringLibrary.EqualEqual_StriStri(ReturnValue1, "")
        ReturnValue_8: bool = BooleanOR(ReturnValue_6, ReturnValue_7)
        if not ReturnValue_8:
           goto(ExecutionFlow.Pop())
        ReturnValue_9: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_10: Ptr[Widget_RecipeButton] = Default__WidgetBlueprintLibrary.Create(self, Widget_RecipeButton, ReturnValue_9)
        Default__KismetSystemLibrary.SetClassPropertyByName(ReturnValue_10, "mRecipeClass", localRecipe)
        Default__KismetSystemLibrary.SetObjectPropertyByName(ReturnValue_10, "Workbench", self)
        ReturnValue_11: Ptr[PanelSlot] = self.mSearchResultsBox.AddChild(ReturnValue_10)
        goto(ExecutionFlow.Pop())
        # Label 1201
        self.ClearAndHideSearchResults()
        goto(ExecutionFlow.Pop())
        # Label 1216
        ReturnValue_12: int32 = Variable + 1
        Variable = ReturnValue_12
        goto('L278')
    

    def ShowOnlyAffordableRecipes(self, OnlyShowAffordable: bool):
        ExecutionFlow.Push("L1279")
        ExecutionFlow.Push("L702")
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(self.mPhase0ScrollBox)
        if not ReturnValue:
           goto(ExecutionFlow.Pop())
        Variable1: int32 = 0
        # Label 94
        ReturnValue_0: int32 = self.mPhase0ScrollBox.GetChildrenCount()
        ReturnValue_1: bool = Variable1 <= ReturnValue_0
        if not ReturnValue_1:
           goto(ExecutionFlow.Pop())
        ExecutionFlow.Push("L1131")
        ReturnValue_2: Ptr[Widget] = self.mPhase0ScrollBox.GetChildAt(Variable1)
        Category: Ptr[Widget_CraftBench_Category] = Cast[Widget_CraftBench_Category](ReturnValue_2)
        bSuccess: bool = Category
        if not bSuccess:
           goto(ExecutionFlow.Pop())
        Category.mHideIfUnaffordable = OnlyShowAffordable
        Variable2: int32 = 0
        # Label 387
        ReturnValue1: int32 = Category.mContentVertical.GetChildrenCount()
        ReturnValue2: bool = Variable2 <= ReturnValue1
        if not ReturnValue2:
           goto(ExecutionFlow.Pop())
        ExecutionFlow.Push("L1205")
        ReturnValue1_0: Ptr[Widget] = Category.mContentVertical.GetChildAt(Variable2)
        # Label 585
        Button: Ptr[Widget_RecipeButton] = Cast[Widget_RecipeButton](ReturnValue1_0)
        bSuccess1: bool = Button
        if not bSuccess1:
           goto(ExecutionFlow.Pop())
        # Label 660
        Button.mHideIfUnaffordable = OnlyShowAffordable
        goto(ExecutionFlow.Pop())
        # Label 702
        ReturnValue1_1: bool = Default__KismetSystemLibrary.IsValid(self.mSearchResultsBox)
        if not ReturnValue1_1:
           goto(ExecutionFlow.Pop())
        Variable: int32 = 0
        # Label 786
        ReturnValue2_0: int32 = self.mSearchResultsBox.GetChildrenCount()
        ReturnValue1_2: bool = Variable <= ReturnValue2_0
        if not ReturnValue1_2:
           goto(ExecutionFlow.Pop())
        ExecutionFlow.Push("L1057")
        ReturnValue2_1: Ptr[Widget] = self.mSearchResultsBox.GetChildAt(Variable)
        Button1: Ptr[Widget_RecipeButton] = Cast[Widget_RecipeButton](ReturnValue2_1)
        bSuccess2: bool = Button1
        if not bSuccess2:
           goto(ExecutionFlow.Pop())
        Button1.mHideIfUnaffordable = OnlyShowAffordable
        goto(ExecutionFlow.Pop())
        # Label 1057
        ReturnValue_3: int32 = Variable + 1
        Variable = ReturnValue_3
        goto('L786')
        # Label 1131
        ReturnValue1_3: int32 = Variable1 + 1
        Variable1 = ReturnValue1_3
        goto('L94')
        # Label 1205
        ReturnValue2_2: int32 = Variable2 + 1
        Variable2 = ReturnValue2_2
        goto('L387')
    

    def SpaceBarOverride(self):
        if not self.mCraftButton.IsEnabled:
            goto('L211')
        OutputDelegate.BindUFunction(self, StopCraftingOverride)
        ReturnValue: TimerHandle = Default__KismetSystemLibrary.K2_SetTimerDelegate(OutputDelegate, 1, False)
        ReturnValue_0: Ptr[PlayerController] = self.GetOwningPlayer()
        self.mCraftButton.mButton.SetUserFocus(ReturnValue_0)
    

    def StopCraftingOverride(self):
        self.mCraftButton.OnReleasedButton()
        self.mCraftButton.SimulateRelease()
        self.EndProducing()
    

    def OnPreviewKeyDown(self):
        
        ReturnValue: Key = Default__KismetInputLibrary.GetKey(Ref[InKeyEvent])
        ReturnValue_0: bool = Default__KismetInputLibrary.EqualEqual_KeyKey(ReturnValue, Key(KeyName = "SpaceBar"))
        if not ReturnValue_0:
            goto('L165')
        self.SpaceBarOverride()
        # Label 165
        ReturnValue_1: EventReply = Default__WidgetBlueprintLibrary.Unhandled()
        ReturnValue_2: EventReply = ReturnValue_1
    

    def CreateCategoryHeader(self, InScrollbox: Ptr[PanelWidget], Name: FText, mIsCollapsed: bool):
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_0: Ptr[Widget_CraftBench_Category] = Default__WidgetBlueprintLibrary.Create(self, Widget_CraftBench_Category, ReturnValue)
        
        # Label 85
        Default__KismetSystemLibrary.SetTextPropertyByName(ReturnValue_0, "mText", Ref[Name])
        Default__KismetSystemLibrary.SetBoolPropertyByName(ReturnValue_0, "mIsCollapsed", mIsCollapsed)
        # Label 211
        ReturnValue_1: Ptr[PanelSlot] = InScrollbox.AddChild(ReturnValue_0)
        Category Widget = ReturnValue_0
    

    def UpdateLeds(self):
        Variable4: uint8 = 0
        Variable5: uint8 = 2
        ReturnValue2: bool = self.DelayCounter > 0
        # Label 74
        Variable2: bool = ReturnValue2
        
        switch = {
            False: Variable5,
            True: Variable4
        }
        self.mLED_On_1L.SetVisibility(switch.get(Variable2, None))
        
        switch_0 = {
            False: Variable5,
            True: Variable4
        }
        self.mLED_On_1R.SetVisibility(switch_0.get(Variable2, None))
        Variable2_0: uint8 = 0
        Variable3: uint8 = 2
        ReturnValue1: bool = self.DelayCounter > 1
        Variable1: bool = ReturnValue1
        
        switch_1 = {
            False: Variable3,
            True: Variable2_0
        }
        self.mLED_On_2R.SetVisibility(switch_1.get(Variable1, None))
        
        switch_2 = {
            False: Variable3,
            True: Variable2_0
        }
        self.mLED_On_2L.SetVisibility(switch_2.get(Variable1, None))
        Variable: uint8 = 0
        Variable1_0: uint8 = 2
        ReturnValue: bool = self.DelayCounter > 2
        Variable_0: bool = ReturnValue
        
        switch_3 = {
            False: Variable1_0,
            True: Variable
        }
        self.mLED_On_3L.SetVisibility(switch_3.get(Variable_0, None))
        
        switch_4 = {
            False: Variable1_0,
            True: Variable
        }
        self.mLED_On_3R.SetVisibility(switch_4.get(Variable_0, None))
    

    def UpdateWarningWidget(self):
        ExecutionFlow.Push("L1532")
        ReturnValue: bool = Default__KismetSystemLibrary.IsValidClass(self.mCurrentRecipe)
        if not ReturnValue:
            goto('L1060')
        ReturnValue_0: Ptr[Pawn] = self.GetOwningPlayerPawn()
        # Label 90
        Player: Ptr[FGCharacterPlayer] = Cast[FGCharacterPlayer](ReturnValue_0)
        bSuccess: bool = Player
        if not bSuccess:
           goto(ExecutionFlow.Pop())
        # Label 165
        ReturnValue_1: List[ItemAmount] = Default__FGRecipe.GetProducts(self.mCurrentRecipe, False)
        
        Item = None
        Item = ReturnValue_1[0]
        ReturnValue_2: Ptr[FGInventoryComponent] = Player.GetInventory()
        ReturnValue_3: InventoryItem = Default__FGInventoryLibrary.MakeInventoryItem(Item.ItemClass)
        ReturnValue_4: InventoryStack = Default__FGInventoryLibrary.MakeInventoryStack(Item.amount, ReturnValue_3)
        
        ReturnValue_5: bool = ReturnValue_2.HasEnoughSpaceForStack(Ref[ReturnValue_4])
        if not ReturnValue_5:
            goto('L1177')
        Variable: int32 = 0
        Variable_0: int32 = 0
        # Label 578
        ReturnValue_6: List[ItemAmount] = Default__FGRecipe.GetIngredients(self.mCurrentRecipe)
        
        ReturnValue_7: int32 = len(ReturnValue_6)
        ReturnValue1: bool = Variable <= ReturnValue_7
        if not ReturnValue1:
            goto('L1297')
        Variable_0 = Variable
        ExecutionFlow.Push("L1458")
        ReturnValue_6 = Default__FGRecipe.GetIngredients(self.mCurrentRecipe)
        
        Item1 = None
        Item1 = ReturnValue_6[Variable_0]
        ReturnValue1_0: Ptr[Pawn] = self.GetOwningPlayerPawn()
        
        numItems = None
        Default__HUDHelpers.GetNumItemsFromPlayerInventory(ReturnValue1_0, Item1.ItemClass, self, Ref[numItems])
        ReturnValue_8: bool = numItems <= Item1.amount
        if not ReturnValue_8:
           goto(ExecutionFlow.Pop())
        LocalCantAfford = True
        goto(ExecutionFlow.Pop())
        # Label 1060
        self.Widget_Manufacturing_Warning.UpdateWarning("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 1097, 'Value': 'Select Recipe in the List on the Left...'}")
        goto(ExecutionFlow.Pop())
        # Label 1177
        self.Widget_Manufacturing_Warning.UpdateWarning("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 1214, 'Value': 'Not Enough Space in Inventory'}")
        self.GetCraftButtonFeedback()
        goto(ExecutionFlow.Pop())
        # Label 1297
        if not LocalCantAfford:
            goto('L1407')
        self.Widget_Manufacturing_Warning.UpdateWarning("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 1348, 'Value': "Can't afford Recipe"}")
        goto(ExecutionFlow.Pop())
        # Label 1407
        self.Widget_Manufacturing_Warning.HideWarning()
        self.GetCraftButtonFeedback()
        goto(ExecutionFlow.Pop())
        # Label 1458
        ReturnValue_9: int32 = Variable + 1
        Variable = ReturnValue_9
        goto('L578')
    

    def GetCalculatedCurve(self):
        EnableShake = True
        ReturnValue1: bool = Default__KismetSystemLibrary.IsValid(self.mManualManufacturerComponent)
        if not ReturnValue1:
            goto('L2343')
        if not True:
            goto('L2150')
        ReturnValue: bool = self.mManualManufacturerComponent.IsProducing()
        if not ReturnValue:
            goto('L2291')
        ReturnValue_0: bool = Default__KismetSystemLibrary.IsValid(self.mProgressBarEndCurve)
        ReturnValue_1: float = self.mManualManufacturerComponent.GetManufacturingProgress()
        ReturnValue_2: float = self.mManualManufacturerComponent.GetManufacturingSpeed()
        # Label 289
        ReturnValue_3: float = Default__FGRecipe.GetManufacturingDuration(self.mCurrentRecipe)
        ReturnValue_4: float = ReturnValue_3 / ReturnValue_2
        ReturnValue_5: float = ReturnValue_1 * ReturnValue_4
        ReturnValue_6: float = ReturnValue_5 - 0.5
        ReturnValue_7: int32 = Round(ReturnValue_6)
        ReturnValue_8: float = Conv_IntToFloat(ReturnValue_7)
        ReturnValue1_0: float = ReturnValue_4 - ReturnValue_8
        ReturnValue_9: bool = ReturnValue1_0 > 1
        ReturnValue_10: bool = Not_PreBool(ReturnValue_9)
        ReturnValue_11: bool = ReturnValue_0 and ReturnValue_10
        EndCurve = ReturnValue_11
        ReturnValue_1 = self.mManualManufacturerComponent.GetManufacturingProgress()
        ReturnValue_2 = self.mManualManufacturerComponent.GetManufacturingSpeed()
        ReturnValue_3 = Default__FGRecipe.GetManufacturingDuration(self.mCurrentRecipe)
        ReturnValue_4 = ReturnValue_3 / ReturnValue_2
        ReturnValue_5 = ReturnValue_1 * ReturnValue_4
        ReturnValue_6 = ReturnValue_5 - 0.5
        ReturnValue_7 = Round(ReturnValue_6)
        ReturnValue_12: bool = self.ProgressbarStep <= ReturnValue_7
        if not ReturnValue_12:
            goto('L1475')
        ReturnValue_1 = self.mManualManufacturerComponent.GetManufacturingProgress()
        ReturnValue_2 = self.mManualManufacturerComponent.GetManufacturingSpeed()
        ReturnValue_3 = Default__FGRecipe.GetManufacturingDuration(self.mCurrentRecipe)
        ReturnValue_4 = ReturnValue_3 / ReturnValue_2
        ReturnValue_5 = ReturnValue_1 * ReturnValue_4
        ReturnValue_6 = ReturnValue_5 - 0.5
        ReturnValue_7 = Round(ReturnValue_6)
        self.ProgressbarStep = ReturnValue_7
        self.OnCraftingProgressbarAnimationLoop()
        # Label 1475
        if not EndCurve:
            goto('L2319')
        CurrentCurve = self.mProgressBarEndCurve
        # Label 1508
        ReturnValue_1 = self.mManualManufacturerComponent.GetManufacturingProgress()
        ReturnValue_2 = self.mManualManufacturerComponent.GetManufacturingSpeed()
        ReturnValue_3 = Default__FGRecipe.GetManufacturingDuration(self.mCurrentRecipe)
        ReturnValue_4 = ReturnValue_3 / ReturnValue_2
        ReturnValue_5 = ReturnValue_1 * ReturnValue_4
        ReturnValue_6 = ReturnValue_5 - 0.5
        ReturnValue_7 = Round(ReturnValue_6)
        ReturnValue1_1: float = Conv_IntToFloat(ReturnValue_7)
        ReturnValue1_2: float = ReturnValue1_1 / ReturnValue_4
        ReturnValue2: float = ReturnValue_5 - ReturnValue1_1
        ReturnValue1_3: float = CurrentCurve.GetFloatValue(ReturnValue2)
        ReturnValue2_0: float = ReturnValue1_3 / ReturnValue_4
        ReturnValue_13: float = ReturnValue2_0 + ReturnValue1_2
        Output = ReturnValue_13
        # End
        # Label 2150
        ReturnValue1_4: float = self.mManualManufacturerComponent.GetManufacturingProgress()
        ReturnValue_14: float = self.mProgressBarCurve.GetFloatValue(ReturnValue1_4)
        Output = ReturnValue_14
        # End
        # Label 2291
        self.ProgressbarStep = -1
        # End
        # Label 2319
        CurrentCurve = self.mProgressBarCurve
        goto('L1508')
    

    def ShowCurrentOutput(self):
        ReturnValue: bool = Default__KismetSystemLibrary.IsValidClass(self.mCurrentRecipe)
        # Label 51
        if not ReturnValue:
            goto('L90')
        ReturnValue_0: uint8 = 0
        # Label 85
        goto('L110')
        # Label 90
        ReturnValue_0 = 2
    

    def UpdateProductionStats(self):
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(self.mManualManufacturerComponent)
        # Label 51
        if not ReturnValue:
            goto('L533')
        ReturnValue_0: float = self.mManualManufacturerComponent.GetCurrentFatigue()
        ReturnValue_1: float = self.mManualManufacturerComponent.GetManufacturingSpeed()
        # Label 165
        ReturnValue_2: float = ReturnValue_1 * ReturnValue_0
        # Label 211
        ReturnValue_3: float = Default__FGRecipe.GetManualManufacturingDuration(self.mCurrentRecipe)
        ReturnValue_4: float = ReturnValue_3 / ReturnValue_2
        ReturnValue1: float = ReturnValue_4 / 0.25
        ReturnValue_5: int32 = Round(ReturnValue1)
        ReturnValue_6: FText = Default__KismetTextLibrary.Conv_IntToText(ReturnValue_5, False, True, 1, 324)
        self.Widget_SmallManufacturingScreen.CraftAmount.SetText(ReturnValue_6)
    

    def UpdateProgressBar(self):
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(self.mManualManufacturerComponent)
        # Label 51
        if not ReturnValue:
            goto('L484')
        ReturnValue_0: TSubclassOf[FGRecipe] = self.mManualManufacturerComponent.GetCurrentRecipe()
        ReturnValue_1: bool = Default__KismetSystemLibrary.IsValidClass(ReturnValue_0)
        if not ReturnValue_1:
            goto('L484')
        OldPercent = self.Widget_SmallManufacturingScreen.Widget_ProgressBar.mProgressBar.Percent
        # Label 265
        ReturnValue_2: float = self.mManualManufacturerComponent.GetManufacturingProgress()
        NewPercent = ReturnValue_2
        ReturnValue_3: bool = NotEqual_FloatFloat(OldPercent, NewPercent)
        if not ReturnValue_3:
            goto('L565')
        self.Widget_SmallManufacturingScreen.Widget_ProgressBar.mProgressBar.SetPercent(NewPercent)
        # End
        # Label 484
        self.Widget_SmallManufacturingScreen.Widget_ProgressBar.mProgressBar.SetPercent(0)
    

    def GetCraftButtonFeedback(self):
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(self.mManualManufacturerComponent)
        # Label 51
        if not ReturnValue:
            goto('L302')
        ReturnValue_0: Ptr[FGInventoryComponent] = self.mManualManufacturerComponent.GetInventory()
        ReturnValue_1: TSubclassOf[FGRecipe] = self.mManualManufacturerComponent.GetCurrentRecipe()
        ReturnValue_2: bool = self.mManualManufacturerComponent.CanProduce(ReturnValue_1, ReturnValue_0)
        if not ReturnValue_2:
            goto('L265')
        self.mCraftButton.SetEnabled(True)
        # End
        # Label 265
        self.mCraftButton.SetEnabled(False)
    

    def CloseVehicle(self):
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(None)
        if not ReturnValue:
            goto('L356')
        ReturnValue_0: Ptr[Pawn] = self.GetOwningPlayerPawn()
        Player: Ptr[FGCharacterPlayer] = Cast[FGCharacterPlayer](ReturnValue_0)
        bSuccess1: bool = Player
        if not bSuccess1:
            goto('L356')
        ReturnValue_1: Ptr[PlayerController] = self.GetOwningPlayer()
        Controller: Ptr[BP_PlayerController] = Cast[BP_PlayerController](ReturnValue_1)
        bSuccess: bool = Controller
        if not bSuccess:
            goto('L356')
        ReturnValue_2: Ptr[BP_RemoteCallObject] = Controller.GetRemoteCallObjectOfClass(BP_RemoteCallObject)
        ReturnValue_2.ServerCloseVehicleTrunk(None, Player)
    

    def GetInfoboxVisibility(self):
        ReturnValue: bool = Default__KismetSystemLibrary.IsValidClass(self.mCurrentRecipe)
        # Label 51
        if not ReturnValue:
            goto('L90')
        ReturnValue_0: uint8 = 0
        # Label 85
        goto('L110')
        # Label 90
        ReturnValue_0 = 2
    

    def GetCraftingFeedbackVisibility(self):
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(self.mManualManufacturerComponent)
        # Label 51
        if not ReturnValue:
            goto('L146')
        ReturnValue_0: bool = self.mManualManufacturerComponent.IsProducing()
        if not ReturnValue_0:
            goto('L146')
        ReturnValue_1: uint8 = 0
        goto('L166')
        # Label 146
        ReturnValue_1 = 2
    

    def SetWorkingAtWorkbenchOnServer(self, FGPlayerController: Ptr[FGPlayerController]):
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        Controller: Ptr[BP_PlayerController] = Cast[BP_PlayerController](ReturnValue)
        bSuccess: bool = Controller
        if not bSuccess:
            goto('L208')
        ReturnValue_0: Ptr[BP_RemoteCallObject] = Controller.GetRemoteCallObjectOfClass(BP_RemoteCallObject)
        ReturnValue_0.ServerSetWorkingAtBench(FGPlayerController, self.mManualManufacturerComponent)
    

    def OnCraftCompleted(self):
        self.GetCraftButtonFeedback()
        ReturnValue2: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.AddedToInventoryPulse, 0, 1, 0, 1)
        ReturnValue1: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.OutputPulse, 0, 1, 0, 1)
        self.FadeBar()
        ReturnValue: int32 = RandomIntegerInRange(12, 20)
        self.Widget_SparkParticles.CreateSparks(ReturnValue)
        ReturnValue_0: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.ButtonGlow, 0, 1, 0, 1)
        self.ShowAddedToInventory()
    

    def CreateInfoBox(self, mRecipe: TSubclassOf[FGRecipe]):
        ExecutionFlow.Push("L1637")
        localRecipe = mRecipe
        self.InputVBox.ClearChildren()
        
        Text = None
        Graphics = None
        Default__HUDHelpers.GetFactoryGameDarkGray(self, Ref[Text], Ref[Graphics])
        self.Widget_SmallManufacturingScreen.Widget_ProgressBar.mProgressBar.SetFillColorAndOpacity(Graphics)
        ReturnValue: bool = Default__KismetSystemLibrary.IsValidClass(localRecipe)
        if not ReturnValue:
           goto(ExecutionFlow.Pop())
        Variable: int32 = 0
        Variable_0: int32 = 0
        # Label 307
        ReturnValue_0: List[ItemAmount] = Default__FGRecipe.GetIngredients(localRecipe)
        
        ReturnValue_1: int32 = len(ReturnValue_0)
        ReturnValue_2: bool = Variable <= ReturnValue_1
        if not ReturnValue_2:
            goto('L995')
        Variable_0 = Variable
        ExecutionFlow.Push("L1563")
        ReturnValue_0 = Default__FGRecipe.GetIngredients(localRecipe)
        
        Item = None
        Item = ReturnValue_0[Variable_0]
        localCost = Item
        ReturnValue_3: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_4: Ptr[Widget_SmallCostSlot] = Default__WidgetBlueprintLibrary.Create(self, Widget_SmallCostSlot, ReturnValue_3)
        
        Default__KismetSystemLibrary.SetStructurePropertyByName(ReturnValue_4, "mCost", Ref[localCost])
        ReturnValue_4.Widget_CostSlotWrapper.Setup CostIcon(None, localCost, None, Variable_0, 0, True, False, False)
        ReturnValue_4.Widget_CostSlotWrapper.mForceEmptyAnim = True
        ReturnValue_5: Ptr[WrapBoxSlot] = self.InputVBox.AddChildToWrapBox(ReturnValue_4)
        goto(ExecutionFlow.Pop())
        # Label 995
        ReturnValue_6: List[ItemAmount] = Default__FGRecipe.GetProducts(self.mCurrentRecipe, True)
        
        Item1 = None
        Item1 = ReturnValue_6[0]
        self.Widget_CostSlotWrapper.Setup CostIcon(None, Item1, None, 0, 0, False, False, False)
        ReturnValue_7: FText = Default__FGRecipe.GetRecipeName(self.mCurrentRecipe)
        self.Widget_SmallManufacturingScreen.mName.SetText(ReturnValue_7)
        ReturnValue_8: int32 = self.InputVBox.GetChildrenCount()
        ReturnValue_9: bool = EqualEqual_IntInt(ReturnValue_8, 4)
        if not ReturnValue_9:
           goto(ExecutionFlow.Pop())
        ReturnValue_10: Ptr[Widget] = self.InputVBox.GetChildAt(3)
        Slot: Ptr[Widget_CostSlot] = Cast[Widget_CostSlot](ReturnValue_10)
        bSuccess: bool = Slot
        Slot.mDividerBottom.SetVisibility(1)
        goto(ExecutionFlow.Pop())
        # Label 1563
        ReturnValue_11: int32 = Variable + 1
        Variable = ReturnValue_11
        goto('L307')
    

    def Cleanup(self):
        self.SetWorkingAtWorkbenchOnServer(None)
        ReturnValue: Ptr[Pawn] = self.GetOwningPlayerPawn()
        Player: Ptr[Char_Player] = Cast[Char_Player](ReturnValue)
        bSuccess1: bool = Player
        if not bSuccess1:
            goto('L289')
        Player.EventFire.Clear()
        # Label 146
        Component: Ptr[BP_ManualManufacturingComponent] = Cast[BP_ManualManufacturingComponent](self.mManualManufacturerComponent)
        bSuccess: bool = Component
        # Label 211
        if not bSuccess:
            goto('L289')
        OutputDelegate.BindUFunction(self, OnCraftCompleted)
        Component.OnCraftCompleted.Remove(OutputDelegate)
    

    def GetAvailableRecipes(self):
        ReturnValue: Ptr[GameStateBase] = Default__GameplayStatics.GetGameState(self)
        ReturnValue_0: Ptr[FGRecipeManager] = Default__FGRecipeManager.Get(ReturnValue)
        # Label 94
        ReturnValue_1: bool = Default__KismetSystemLibrary.IsValid(ReturnValue_0)
        if not ReturnValue_1:
            goto('L513')
        ReturnValue_2: TSubclassOf[FGWorkBench] = Default__GameplayStatics.GetObjectClass(self.mManualManufacturerComponent)
        ReturnValue_3: bool = Default__KismetSystemLibrary.IsValidClass(ReturnValue_2)
        if not ReturnValue_3:
            goto('L513')
        ReturnValue = Default__GameplayStatics.GetGameState(self)
        ReturnValue_2 = Default__GameplayStatics.GetObjectClass(self.mManualManufacturerComponent)
        ReturnValue_0 = Default__FGRecipeManager.Get(ReturnValue)
        recipes: List[TSubclassOf[FGRecipe]] = []
        
        ReturnValue_0.GetAvailableRecipesForProducer(ReturnValue_2, Ref[recipes])
        AvailableRecipes = recipes
        # End
        # Label 513
        Default__KismetSystemLibrary.PrintString(self, "No available recipes", True, True, LinearColor(R = 0, G = 0.6600000262260437, B = 1, A = 1), 2)
        AvailableRecipes = List[ClassProperty /Game/FactoryGame/Buildable/-Shared/WorkBench/Widget_ManualManufacturing.Widget_ManualManufacturing_C:GetAvailableRecipes.AvailableRecipes.AvailableRecipes]([])
    

    def SetSelectedRecipe(self, mRecipe: TSubclassOf[FGRecipe]):
        ReturnValue: bool = NotEqual_ClassClass(self.mCurrentRecipe, mRecipe)
        if not ReturnValue:
            goto('L818')
        ReturnValue_0: Ptr[Widget_CraftBench_Category] = self.GetCategoryWidgetFromRecipe(mRecipe)
        # Label 85
        LocalNewCategoryWidget = ReturnValue_0
        ReturnValue_1: bool = Default__KismetSystemLibrary.IsValid(self.mCurrentCategoryWidget)
        ReturnValue_2: FString = Default__KismetStringLibrary.Conv_BoolToString(ReturnValue_1)
        Default__KismetSystemLibrary.PrintString(self, ReturnValue_2, True, True, LinearColor(R = 0, G = 0.6600000262260437, B = 1, A = 1), 2)
        ReturnValue_3: bool = NotEqual_ObjectObject(self.mCurrentCategoryWidget, LocalNewCategoryWidget)
        if not ReturnValue_3:
            goto('L598')
        ReturnValue1: bool = Default__KismetSystemLibrary.IsValid(self.mCurrentCategoryWidget)
        if not ReturnValue1:
            goto('L598')
        ReturnValue_4: Ptr[Widget] = self.mCurrentCategoryWidget.mContentVertical.GetChildAt(0)
        Button: Ptr[Widget_RecipeButton] = Cast[Widget_RecipeButton](ReturnValue_4)
        bSuccess: bool = Button
        if not bSuccess:
            goto('L598')
        Button.ClearButtonSelection()
        # Label 598
        self.mCurrentRecipe = mRecipe
        self.mCurrentCategoryWidget = LocalNewCategoryWidget
        self.mManualManufacturerComponent.SetRecipe(self.mCurrentRecipe)
        self.CreateInfoBox(self.mCurrentRecipe)
        self.GetCraftButtonFeedback()
        self.screen.SetVisibility(0)
        self.Widget_Manufacturing_Warning.SetVisibility(2)
        self.HideAddedToInventoryEvent()
        self.UpdateRelevantClasses()
    

    def InitRecipeList(self):
        ExecutionFlow.Push("L1929")
        StartIndex = -1
        Variable: int32 = 0
        # Label 51
        Variable2: int32 = 0
        
        AvailableRecipes = None
        # Label 74
        self.GetAvailableRecipes(Ref[AvailableRecipes])
        
        AvailableRecipes = None
        ReturnValue2: int32 = len(AvailableRecipes)
        ReturnValue2_0: bool = Variable <= ReturnValue2
        if not ReturnValue2_0:
            goto('L355')
        # Label 208
        Variable2 = Variable
        ExecutionFlow.Push("L1781")
        
        AvailableRecipes = None
        self.GetAvailableRecipes(Ref[AvailableRecipes])
        
        AvailableRecipes = None
        Item2 = None
        Item2 = AvailableRecipes[Variable2]
        
        self.AddUniqueRecipe(Item2, Ref[self.mCategorizedRecipes])
        goto(ExecutionFlow.Pop())
        # Label 355
        Variable1: int32 = 0
        Variable_0: int32 = 0
        
        # Label 401
        ReturnValue: int32 = len(self.mCategorizedRecipes)
        ReturnValue_0: bool = Variable1 <= ReturnValue
        if not ReturnValue_0:
           goto(ExecutionFlow.Pop())
        Variable_0 = Variable1
        ExecutionFlow.Push("L1707")
        Variable2_0: int32 = 0
        Variable1_0: int32 = 0
        
        Item = None
        # Label 586
        Item = self.mCategorizedRecipes[Variable_0]
        
        Item.Recipes_6_5C2C7BF54D78A483A81B2785C2CF7736 = None
        ReturnValue1: int32 = len(Item.Recipes_6_5C2C7BF54D78A483A81B2785C2CF7736)
        ReturnValue1_0: bool = Variable2_0 <= ReturnValue1
        if not ReturnValue1_0:
           goto(ExecutionFlow.Pop())
        Variable1_0 = Variable2_0
        ExecutionFlow.Push("L1855")
        ReturnValue_1: bool = EqualEqual_IntInt(Variable1_0, 0)
        if not ReturnValue_1:
            goto('L1331')
        ReturnValue_2: Ptr[PlayerController] = self.GetOwningPlayer()
        State: Ptr[FGPlayerState] = Cast[FGPlayerState](ReturnValue_2.PlayerState)
        bSuccess: bool = State
        ReturnValue_3: List[TSubclassOf[FGItemCategory]] = State.GetCollapsedItemCategories()
        
        Item = None
        Item = self.mCategorizedRecipes[Variable_0]
        
        Item.Category_5_48CE2A3C41089DC1E5DE39909CF17792 = None
        ReturnValue_4: bool = Default__KismetArrayLibrary.Array_Contains(Ref[ReturnValue_3], Ref[Item.Category_5_48CE2A3C41089DC1E5DE39909CF17792])
        ReturnValue_5: FText = Default__FGItemCategory.GetCategoryName(Item.Category_5_48CE2A3C41089DC1E5DE39909CF17792)
        
        Widget = None
        self.CreateCategoryHeader(self.mPhase0ScrollBox, ReturnValue_5, ReturnValue_4, Ref[Widget])
        CurrentCategory = Widget
        OutputDelegate.BindUFunction(self, OnCategoryClicked)
        # Label 1290
        CurrentCategory.OnClicked.AddUnique(OutputDelegate)
        # Label 1331
        ReturnValue1_1: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_6: Ptr[Widget_RecipeButton] = Default__WidgetBlueprintLibrary.Create(self, Widget_RecipeButton, ReturnValue1_1)
        
        Item = None
        Item = self.mCategorizedRecipes[Variable_0]
        
        Item.Recipes_6_5C2C7BF54D78A483A81B2785C2CF7736 = None
        Item1 = None
        # Label 1475
        Item1 = Item.Recipes_6_5C2C7BF54D78A483A81B2785C2CF7736[Variable1_0]
        Default__KismetSystemLibrary.SetClassPropertyByName(ReturnValue_6, "mRecipeClass", Item1)
        Default__KismetSystemLibrary.SetObjectPropertyByName(ReturnValue_6, "Workbench", self)
        CurrentCategory.AddChildToContentVertical(ReturnValue_6)
        goto(ExecutionFlow.Pop())
        # Label 1707
        ReturnValue1_2: int32 = Variable1 + 1
        Variable1 = ReturnValue1_2
        goto('L401')
        # Label 1781
        ReturnValue_7: int32 = Variable + 1
        Variable = ReturnValue_7
        goto('L74')
        # Label 1855
        ReturnValue2_1: int32 = Variable2_0 + 1
        Variable2_0 = ReturnValue2_1
        goto('L586')
    

    def Destruct(self):
        self.ExecuteUbergraph_Widget_ManualManufacturing(4413)
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_ManualManufacturing(5439)
    

    def SetupProductionMode(self):
        self.ExecuteUbergraph_Widget_ManualManufacturing(5479)
    

    def OnNewRecipeSet(self, mNewRecipe: TSubclassOf[FGRecipe]):
        ExecuteUbergraph_Widget_ManualManufacturing.K2Node_CustomEvent_mNewRecipe = mNewRecipe #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_ManualManufacturing(5946)
    

    def Init(self):
        self.ExecuteUbergraph_Widget_ManualManufacturing(6641)
    

    def StartProducing(self, dt: float):
        ExecuteUbergraph_Widget_ManualManufacturing.K2Node_CustomEvent_dt = dt #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_ManualManufacturing(6658)
    

    def EndProducing(self):
        self.ExecuteUbergraph_Widget_ManualManufacturing(7192)
    

    def Tick(self):
        ExecuteUbergraph_Widget_ManualManufacturing.K2Node_Event_MyGeometry = MyGeometry #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_ManualManufacturing.K2Node_Event_InDeltaTime = InDeltaTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_ManualManufacturing(7402)
    

    def OnCraftingProgressbarAnimationLoop(self):
        self.ExecuteUbergraph_Widget_ManualManufacturing(7658)
    

    def StopSuperClick(self):
        self.ExecuteUbergraph_Widget_ManualManufacturing(7735)
    

    def StartSuperClick(self):
        self.ExecuteUbergraph_Widget_ManualManufacturing(7812)
    

    def IncreaseGlow(self):
        self.ExecuteUbergraph_Widget_ManualManufacturing(8986)
    

    def DecreseGlow(self):
        self.ExecuteUbergraph_Widget_ManualManufacturing(8991)
    

    def Shake(self):
        self.ExecuteUbergraph_Widget_ManualManufacturing(9600)
    

    def EmptyBar(self):
        self.ExecuteUbergraph_Widget_ManualManufacturing(9616)
    

    def FadeBar(self):
        self.ExecuteUbergraph_Widget_ManualManufacturing(9784)
    

    def WarningMessageCheck(self):
        self.ExecuteUbergraph_Widget_ManualManufacturing(10033)
    

    def ProductionStartupDelay(self, ProduceSpeed: float):
        ExecuteUbergraph_Widget_ManualManufacturing.K2Node_CustomEvent_ProduceSpeed = ProduceSpeed #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_ManualManufacturing(10048)
    

    def PlayLEDSound(self):
        self.ExecuteUbergraph_Widget_ManualManufacturing(10395)
    

    def ShowAddedToInventory(self):
        self.ExecuteUbergraph_Widget_ManualManufacturing(10400)
    

    def HideAddedToInventoryEvent(self):
        self.ExecuteUbergraph_Widget_ManualManufacturing(11924)
    

    def BndEvt__Button_0_K2Node_ComponentBoundEvent_0_OnButtonClickedEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_ManualManufacturing(11985)
    

    def BndEvt__mOnlyShowAffordableCheckbox_K2Node_ComponentBoundEvent_3_OnCheckChanged__DelegateSignature(self, IsChecked: bool):
        ExecuteUbergraph_Widget_ManualManufacturing.K2Node_ComponentBoundEvent_IsChecked = IsChecked #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_ManualManufacturing(12119)
    

    def BndEvt__mSearchbar_K2Node_ComponentBoundEvent_4_OnTextChanged__DelegateSignature(self, text: FText):
        ExecuteUbergraph_Widget_ManualManufacturing.K2Node_ComponentBoundEvent_Text = text #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_ManualManufacturing(12202)
    

    def InitOnlyShowAffordable(self):
        self.ExecuteUbergraph_Widget_ManualManufacturing(12399)
    

    def OnCategoryClicked(self, Instigator: Ptr[Widget_CraftBench_Category]):
        ExecuteUbergraph_Widget_ManualManufacturing.K2Node_CustomEvent_Instigator = Instigator #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_ManualManufacturing(12740)
    

    def ExecuteUbergraph_Widget_ManualManufacturing(self):
        goto(ComputedJump("EntryPoint"))
        ReturnValue1: bool = Default__KismetSystemLibrary.IsValid(self.Manufacturing_Container)
        if not ReturnValue1:
            goto('L170')
        ReturnValue2: Ptr[UMGSequencePlayer] = self.Manufacturing_Container.PlayAnimation(self.Manufacturing_Container.ShakeAnim, 0, 1, 0, 1)
        # Label 170
        ReturnValue2_0: Ptr[Pawn] = self.GetOwningPlayerPawn()
        ReturnValue: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_UI_OverClock_Tick, ReturnValue2_0, True)
        goto(ExecutionFlow.Pop())
        self.StopAnimation(self.SuperClickAnim)
        self.SuperClickContainer.SetVisibility(2)
        ReturnValue3: bool = Default__KismetSystemLibrary.IsValid(self.Manufacturing_Container)
        if not ReturnValue3:
            goto('L470')
        self.Manufacturing_Container.StopAnimation(self.Manufacturing_Container.ShakeAnim)
        self.Manufacturing_Container.mLoopingSmoke = False
        # Label 470
        self.ClickCounter = 0
        ReturnValue4: Ptr[PlayerController] = self.GetOwningPlayer()
        Default__AkGameplayStatics.SetSwitch("WorkBench_ClinkSound", "Normal", ReturnValue4)
        goto(ExecutionFlow.Pop())
        # Label 585
        ReturnValue_0: bool = Default__KismetSystemLibrary.IsValidClass(self.mCurrentRecipe)
        if not ReturnValue_0:
           goto(ExecutionFlow.Pop())
        if not self.ShakeActive:
            goto('L1398')
        # Label 660
        ReturnValue1_0: float = self.GlowingPanel.ColorAndOpacity.A + 0.009999999776482582
        ReturnValue_1: float = FClamp(ReturnValue1_0, 0, 0.8500000238418579)
        LinearColor.R = 1
        LinearColor.G = ReturnValue_1
        LinearColor.B = ReturnValue_1
        LinearColor.A = ReturnValue_1
        self.GlowingPanel.SetColorAndOpacity(LinearColor)
        ReturnValue1_0 = self.GlowingPanel.ColorAndOpacity.A + 0.009999999776482582
        ReturnValue_1 = FClamp(ReturnValue1_0, 0, 0.8500000238418579)
        self.GlowingPanelGlow.SetRenderOpacity(ReturnValue_1)
        ReturnValue2_1: float = self.ShakeIntesity + 0.009999999776482582
        self.ShakeIntesity = ReturnValue2_1
        ReturnValue4_0: Ptr[Pawn] = self.GetOwningPlayerPawn()
        Default__AkGameplayStatics.SetActorRTPCValue("RTPC_WorkBench_Glow", self.ShakeIntesity, 0, ReturnValue4_0)
        
        ReturnValue_2 = None
        # Label 1279
        Default__KismetSystemLibrary.K2_ClearAndInvalidateTimerHandle(self, Ref[ReturnValue_2])
        Default__KismetSystemLibrary.RetriggerableDelay(self, 0.5, LatentActionInfo(Linkage = 1417, UUID = 301632169, ExecutionFunction = "ExecuteUbergraph_Widget_ManualManufacturing", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        # Label 1398
        self.Shake()
        goto('L660')
        OutputDelegate.BindUFunction(self, DecreseGlow)
        ReturnValue_2: TimerHandle = Default__KismetSystemLibrary.K2_SetTimerDelegate(OutputDelegate, 0.05000000074505806, True)
        ReturnValue1_1: bool = self.GlowingPanel.ColorAndOpacity.A > 0.699999988079071
        if not ReturnValue1_1:
           goto(ExecutionFlow.Pop())
        ReturnValue2_2: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_3: Ptr[Widget_Smoke] = Default__WidgetBlueprintLibrary.Create(self, Widget_Smoke, ReturnValue2_2)
        ReturnValue_4: Ptr[OverlaySlot] = self.SmokeContainerLeft.AddChildToOverlay(ReturnValue_3)
        ReturnValue3_0: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue1_2: Ptr[Widget_Smoke] = Default__WidgetBlueprintLibrary.Create(self, Widget_Smoke, ReturnValue3_0)
        ReturnValue1_3: Ptr[OverlaySlot] = self.SmokeContainerRight.AddChildToOverlay(ReturnValue1_2)
        goto(ExecutionFlow.Pop())
        ExecutionFlow.Push("L2080")
        ReturnValue_5: float = self.Widget_SmallManufacturingScreen.Widget_ProgressBar.mFadeBar.GetRenderOpacity()
        ReturnValue5: float = ReturnValue_5 - 0.5
        self.Widget_SmallManufacturingScreen.Widget_ProgressBar.mFadeBar.SetRenderOpacity(ReturnValue5)
        goto(ExecutionFlow.Pop())
        # Label 2080
        ReturnValue1_4: float = self.Widget_SmallManufacturingScreen.Widget_ProgressBar.mFadeBar.GetRenderOpacity()
        ReturnValue3_1: bool = ReturnValue1_4 > 0
        if not ReturnValue3_1:
            goto('L2299')
        Default__KismetSystemLibrary.Delay(self, 0.029999999329447746, LatentActionInfo(Linkage = 1853, UUID = -51595640, ExecutionFunction = "ExecuteUbergraph_Widget_ManualManufacturing", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        # Label 2299
        self.Widget_SmallManufacturingScreen.Widget_ProgressBar.mFadeBar.SetVisibility(2)
        goto(ExecutionFlow.Pop())
        ExecutionFlow.Push("L2698")
        ReturnValue2_3: float = self.ShakeIntesity - 0.75
        ReturnValue1_5: float = FClamp(ReturnValue2_3, 0, 1)
        ReturnValue_6: float = ReturnValue1_5 * -1
        ReturnValue_7: float = RandomFloatInRange(ReturnValue_6, ReturnValue1_5)
        ReturnValue1_6: float = RandomFloatInRange(ReturnValue_6, ReturnValue1_5)
        ReturnValue_8: Vector2D = Vector2D(ReturnValue1_6, ReturnValue_7)
        self.PanelContainer.SetRenderTranslation(ReturnValue_8)
        goto(ExecutionFlow.Pop())
        # Label 2698
        if not self.ShakeActive:
           goto(ExecutionFlow.Pop())
        Default__KismetSystemLibrary.Delay(self, 0.03999999910593033, LatentActionInfo(Linkage = 2382, UUID = 598363269, ExecutionFunction = "ExecuteUbergraph_Widget_ManualManufacturing", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        ExecutionFlow.Push("L2984")
        ReturnValue4_1: float = self.Widget_SmallManufacturingScreen.Widget_ProgressBar.mFadeBar.Percent - 0.10000000149011612
        self.Widget_SmallManufacturingScreen.Widget_ProgressBar.mFadeBar.SetPercent(ReturnValue4_1)
        goto(ExecutionFlow.Pop())
        # Label 2984
        ReturnValue2_4: bool = self.Widget_SmallManufacturingScreen.Widget_ProgressBar.mProgressBar.Percent > 0
        if not ReturnValue2_4:
            goto('L3175')
        Default__KismetSystemLibrary.Delay(self, 0.029999999329447746, LatentActionInfo(Linkage = 2785, UUID = -156032864, ExecutionFunction = "ExecuteUbergraph_Widget_ManualManufacturing", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        # Label 3175
        self.Widget_SmallManufacturingScreen.Widget_ProgressBar.mFadeBar.SetVisibility(2)
        goto(ExecutionFlow.Pop())
        # Label 3258
        ReturnValue2_5: bool = Default__KismetSystemLibrary.IsValid(self.mManualManufacturerComponent)
        if not ReturnValue2_5:
            goto('L3533')
        self.GetCraftButtonFeedback()
        LinearColor2.R = 1
        LinearColor2.G = self.GlowMin
        LinearColor2.B = self.GlowMin
        LinearColor2.A = self.GlowMin
        self.GlowingPanel.SetColorAndOpacity(LinearColor2)
        self.InitOnlyShowAffordable()
        goto(ExecutionFlow.Pop())
        # Label 3533
        Default__KismetSystemLibrary.Delay(self, 0.10000000149011612, LatentActionInfo(Linkage = 3258, UUID = 1134313916, ExecutionFunction = "ExecuteUbergraph_Widget_ManualManufacturing", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        if not self.mIsHolding:
           goto(ExecutionFlow.Pop())
        self.DelayActive = False
        goto(ExecutionFlow.Pop())
        ReturnValue3_2: float = self.mAddedToInventoryBox.GetRenderOpacity()
        ReturnValue1_7: bool = NearlyEqual_FloatFloat(ReturnValue3_2, 1, 9.999999974752427e-07)
        if not ReturnValue1_7:
           goto(ExecutionFlow.Pop())
        ReturnValue4_2: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.HideAddedToInventory, 0, 1, 0, 1)
        ReturnValue_9: float = self.HideAddedToInventory.GetEndTime()
        Default__KismetSystemLibrary.Delay(self, ReturnValue_9, LatentActionInfo(Linkage = 3908, UUID = 221561800, ExecutionFunction = "ExecuteUbergraph_Widget_ManualManufacturing", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        ReturnValue2_6: float = self.mAddedToInventoryBox.GetRenderOpacity()
        ReturnValue_10: bool = NearlyEqual_FloatFloat(ReturnValue2_6, 0, 9.999999974752427e-07)
        if not ReturnValue_10:
           goto(ExecutionFlow.Pop())
        self.AddedToInventoryBuffer = 0
        goto(ExecutionFlow.Pop())
        # Label 4031
        Variable: bool = True
        goto(ExecutionFlow.Pop())
        
        # Label 4043
        Default__KismetSystemLibrary.K2_ClearAndInvalidateTimerHandle(self, Ref[ReturnValue_2])
        self.ShakeActive = False
        goto(ExecutionFlow.Pop())
        # Label 4097
        Variable = True
        goto(ExecutionFlow.Pop())
        # Label 4109
        if not Variable:
           goto(ExecutionFlow.Pop())
        # Label 4119
        ReturnValue10: Ptr[PlayerController] = self.GetOwningPlayer()
        State: Ptr[FGPlayerState] = Cast[FGPlayerState](ReturnValue10.PlayerState)
        bSuccess6: bool = State
        if not bSuccess6:
           goto(ExecutionFlow.Pop())
        State.SetOnlyShowAffordableRecipes(self.mOnlyShowAffordableCheckbox.mIsChecked)
        goto(ExecutionFlow.Pop())
        # Label 4304
        Variable = False
        goto(ExecutionFlow.Pop())
        # Label 4316
        ExecutionFlow.Push("L4109")
        # Label 4321
        ExecutionFlow.Push("L4366")
        if not Variable1:
            goto('L4341')
        goto(ExecutionFlow.Pop())
        # Label 4341
        Variable1: bool = True
        if not False:
           goto(ExecutionFlow.Pop())
        Variable1_0: bool = True
        goto(ExecutionFlow.Pop())
        # Label 4366
        if not Variable1_0:
            goto('L4381')
        goto(ExecutionFlow.Pop())
        # Label 4381
        Variable1_0 = True
        if not True:
            goto('L4031')
        goto('L4304')
        # Label 4403
        ExecutionFlow.Push("L4097")
        goto('L4321')
        self.Destruct()
        self.Cleanup()
        ReturnValue8: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue6: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Stop_F_WorkBench, ReturnValue8, True)
        goto(ExecutionFlow.Pop())
        # Label 4523
        ReturnValue_11: Ptr[Pawn] = self.GetOwningPlayerPawn()
        Player: Ptr[FGCharacterPlayer] = Cast[FGCharacterPlayer](ReturnValue_11)
        bSuccess: bool = Player
        if not bSuccess:
           goto(ExecutionFlow.Pop())
        ReturnValue_12: TSubclassOf[FGRecipe] = self.mManualManufacturerComponent.GetCurrentRecipe()
        self.mCurrentRecipe = ReturnValue_12
        self.CreateInfoBox(self.mCurrentRecipe)
        self.SetupProductionMode()
        ReturnValue_13: int32 = self.mPhase0ScrollBox.GetChildrenCount()
        ReturnValue_14: bool = ReturnValue_13 > 0
        if not ReturnValue_14:
           goto(ExecutionFlow.Pop())
        ReturnValue1_8: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_15: Ptr[Widget] = self.mPhase0ScrollBox.GetChildAt(0)
        ReturnValue_15.SetUserFocus(ReturnValue1_8)
        self.mManualManufacturerComponent.SetupManufacturingButton(self.mCraftButton)
        OutputDelegate3.BindUFunction(self, ProductionStartupDelay)
        self.mCraftButton.OnManufacturePressed.AddUnique(OutputDelegate3)
        OutputDelegate2.BindUFunction(self, EndProducing)
        self.mCraftButton.mButton.OnReleased.AddUnique(OutputDelegate2)
        ReturnValue3_3: bool = Default__KismetSystemLibrary.IsValidClass(self.mCurrentRecipe)
        if not ReturnValue3_3:
            goto('L5397')
        self.screen.SetVisibility(0)
        self.mCraftButton.SetEnabled(True)
        # Label 5253
        self.UpdateWarningWidget()
        OutputDelegate4.BindUFunction(self, WarningMessageCheck)
        ReturnValue1_9: TimerHandle = Default__KismetSystemLibrary.K2_SetTimerDelegate(OutputDelegate4, 0.10000000149011612, True)
        self.mWarningMessageTimerHandle = ReturnValue1_9
        self.UpdateRelevantClasses()
        goto(ExecutionFlow.Pop())
        # Label 5397
        self.mCraftButton.SetEnabled(False)
        goto('L5253')
        self.Construct()
        self.isWorkingAtWorkbench = True
        goto('L3258')
        # Label 5465
        if not False:
           goto(ExecutionFlow.Pop())
        Variable_0: bool = True
        goto(ExecutionFlow.Pop())
        ReturnValue_16: Ptr[PlayerController] = self.GetOwningPlayer()
        Controller: Ptr[BP_PlayerController] = Cast[BP_PlayerController](ReturnValue_16)
        bSuccess1: bool = Controller
        self.SetWorkingAtWorkbenchOnServer(Controller)
        ReturnValue1_10: Ptr[Pawn] = self.GetOwningPlayerPawn()
        Player1: Ptr[FGCharacterPlayer] = Cast[FGCharacterPlayer](ReturnValue1_10)
        bSuccess3: bool = Player1
        self.mManualManufacturerComponent.SetWorkBenchUser(Player1)
        goto(ExecutionFlow.Pop())
        # Label 5718
        ReturnValue_17: bool = Default__KismetSystemLibrary.IsValid(self.mManualManufacturerComponent)
        if not ReturnValue_17:
            goto('L4523')
        self.InitRecipeList()
        goto('L4523')
        # Label 5802
        Component: Ptr[BP_ManualManufacturingComponent] = Cast[BP_ManualManufacturingComponent](self.mManualManufacturerComponent)
        bSuccess2: bool = Component
        if not bSuccess2:
           goto(ExecutionFlow.Pop())
        OutputDelegate1.BindUFunction(self, OnCraftCompleted)
        Component.OnCraftCompleted.AddUnique(OutputDelegate1)
        goto('L5718')
        self.GetCraftButtonFeedback()
        self.mCurrentRecipe = mNewRecipe
        self.CreateInfoBox(self.mCurrentRecipe)
        goto(ExecutionFlow.Pop())
        # Label 6003
        AsActor: Ptr[Actor] = Cast[Actor](self.mInteractObject)
        bSuccess4: bool = AsActor
        if not bSuccess4:
           goto(ExecutionFlow.Pop())
        ReturnValue_18: List[Ptr[BP_ManualManufacturingComponent]] = AsActor.GetComponentsByClass(BP_ManualManufacturingComponent)
        
        foundWidgets = None
        self = None
        ReturnValue_19: int32 = Default__KismetArrayLibrary.Array_Find(Ref[foundWidgets], Ref[self])
        
        Item = None
        Item = ReturnValue_18[ReturnValue_19]
        self.mManualManufacturerComponent = Item
        goto('L5802')
        # Label 6280
        Component1: Ptr[BP_ManualManufacturingComponent] = Cast[BP_ManualManufacturingComponent](self.mInteractObject)
        bSuccess5: bool = Component1
        if not bSuccess5:
            goto('L6383')
        self.mManualManufacturerComponent = Component1
        goto('L5802')
        # Label 6383
        ReturnValue_20: TSubclassOf[Widget_ManualManufacturing] = Default__GameplayStatics.GetObjectClass(self)
        foundWidgets: List[Ptr[Widget_ManualManufacturing]] = []
        
        Default__FGBlueprintFunctionLibrary.GetAllWidgetsOfClassInHierarchy(self, ReturnValue_20, Ref[foundWidgets])
        goto('L6003')
        # Label 6493
        ExecutionFlow.Push("L6529")
        if not Variable_1:
            goto('L6513')
        goto(ExecutionFlow.Pop())
        # Label 6513
        Variable_1: bool = True
        goto('L5465')
        # Label 6529
        if not Variable_0:
            goto('L6544')
        goto(ExecutionFlow.Pop())
        # Label 6544
        Variable_0 = True
        ReturnValue6_0: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue4_3: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_F_WorkBench, ReturnValue6_0, True)
        goto(ExecutionFlow.Pop())
        goto('L6280')
        # Label 6646
        Variable_1 = True
        goto(ExecutionFlow.Pop())
        ReturnValue5_0: bool = Default__KismetSystemLibrary.IsValid(self.mManualManufacturerComponent)
        if not ReturnValue5_0:
           goto(ExecutionFlow.Pop())
        self.mManualManufacturerComponent.Produce(dt)
        ReturnValue_21: Ptr[FGInventoryComponent] = self.mManualManufacturerComponent.GetInventory()
        ReturnValue1_11: TSubclassOf[FGRecipe] = self.mManualManufacturerComponent.GetCurrentRecipe()
        ReturnValue_22: bool = self.mManualManufacturerComponent.CanProduce(ReturnValue1_11, ReturnValue_21)
        ReturnValue1_12: bool = Not_PreBool(ReturnValue_22)
        if not ReturnValue1_12:
            goto('L7076')
        self.GetCraftButtonFeedback()
        self.UpdateLeds()
        ReturnValue5_1: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue3_4: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Stop_F_WorkBench, ReturnValue5_1, True)
        # Label 7060
        Variable_0 = False
        goto('L6646')
        # Label 7076
        self.IncreaseGlow()
        self.StartSuperClick()
        ReturnValue_23: int32 = RandomIntegerInRange(1, 2)
        self.Widget_SparkParticles.CreateSparks(ReturnValue_23)
        goto('L6493')
        self.StopAnimation(self.LEDAnim)
        self.DelayActive = True
        self.mIsHolding = False
        self.DelayCounter = 0
        
        Default__KismetSystemLibrary.K2_ClearAndInvalidateTimerHandle(self, Ref[self.mHoldTimer])
        self.UpdateLeds()
        ReturnValue7: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue5_2: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Stop_F_WorkBench, ReturnValue7, True)
        goto('L7060')
        self.Tick(MyGeometry, InDeltaTime)
        ReturnValue1_13: bool = Default__KismetSystemLibrary.IsValidClass(self.mCurrentRecipe)
        if not ReturnValue1_13:
           goto(ExecutionFlow.Pop())
        self.UpdateProgressBar()
        self.UpdateProductionStats()
        ReturnValue_24: float = Default__GameplayStatics.GetWorldDeltaSeconds(self)
        ReturnValue_25: float = self.InGameTime + ReturnValue_24
        self.InGameTime = ReturnValue_25
        self.UpdateAffordableCategories()
        goto(ExecutionFlow.Pop())
        Default__KismetSystemLibrary.Delay(self, 0.5, LatentActionInfo(Linkage = 15, UUID = -835234522, ExecutionFunction = "ExecuteUbergraph_Widget_ManualManufacturing", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        Default__KismetSystemLibrary.RetriggerableDelay(self, 0.30000001192092896, LatentActionInfo(Linkage = 252, UUID = -10937367, ExecutionFunction = "ExecuteUbergraph_Widget_ManualManufacturing", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        ReturnValue2_7: bool = Default__KismetSystemLibrary.IsValidClass(self.mCurrentRecipe)
        if not ReturnValue2_7:
           goto(ExecutionFlow.Pop())
        ReturnValue_26: float = self.InGameTime - self.LastClickTime
        ReturnValue_27: bool = ReturnValue_26 <= 0.07999999821186066
        if not ReturnValue_27:
            goto('L8864')
        ReturnValue_28: int32 = self.ClickCounter + 1
        self.ClickCounter = ReturnValue_28
        ReturnValue_29: bool = self.IsAnimationPlaying(self.SuperClickAnim)
        ReturnValue_30: bool = Not_PreBool(ReturnValue_29)
        ReturnValue2_8: bool = self.ClickCounter > 3
        ReturnValue_31: bool = ReturnValue_30 and ReturnValue2_8
        ReturnValue4_4: bool = self.ShakeIntesity > 1.5
        ReturnValue1_14: bool = ReturnValue_31 and ReturnValue4_4
        if not ReturnValue1_14:
            goto('L8741')
        self.SuperClickContainer.SetVisibility(3)
        ReturnValue4_5: bool = Default__KismetSystemLibrary.IsValid(self.Manufacturing_Container)
        if not ReturnValue4_5:
            goto('L8481')
        self.Manufacturing_Container.LoopSmoke()
        ReturnValue5_3: Ptr[UMGSequencePlayer] = self.Manufacturing_Container.PlayAnimation(self.Manufacturing_Container.ShakeAnim, 0, 0, 0, 1)
        # Label 8481
        ReturnValue_32: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.SuperClickAnim, 0, 0, 0, 1)
        ReturnValue1_15: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.NANI?, 0, 1, 0, 1)
        ReturnValue6_1: Ptr[Pawn] = self.GetOwningPlayerPawn()
        ReturnValue2_9: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_WorkBench_Nani, ReturnValue6_1, True)
        ReturnValue6_1 = self.GetOwningPlayerPawn()
        Default__AkGameplayStatics.SetSwitch("WorkBench_ClinkSound", "Nani", ReturnValue6_1)
        # Label 8741
        self.LastClickTime = self.InGameTime
        self.StopSuperClick()
        ReturnValue3_5: Ptr[Pawn] = self.GetOwningPlayerPawn()
        ReturnValue1_16: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_Switch_AnvilType, ReturnValue3_5, True)
        goto(ExecutionFlow.Pop())
        # Label 8864
        ReturnValue1_17: bool = self.ClickCounter > 3
        if not ReturnValue1_17:
            goto('L8741')
        ReturnValue1_18: int32 = self.ClickCounter + 1
        self.ClickCounter = ReturnValue1_18
        goto('L8741')
        goto('L585')
        ReturnValue1_19: float = self.GlowingPanel.ColorAndOpacity.A - 0.019999999552965164
        LinearColor1.R = 1
        LinearColor1.G = ReturnValue1_19
        LinearColor1.B = ReturnValue1_19
        LinearColor1.A = ReturnValue1_19
        self.GlowingPanel.SetColorAndOpacity(LinearColor1)
        ReturnValue1_19 = self.GlowingPanel.ColorAndOpacity.A - 0.019999999552965164
        self.GlowingPanelGlow.SetRenderOpacity(ReturnValue1_19)
        ReturnValue3_6: float = self.ShakeIntesity - 0.019999999552965164
        self.ShakeIntesity = ReturnValue3_6
        ReturnValue5_4: Ptr[Pawn] = self.GetOwningPlayerPawn()
        Default__AkGameplayStatics.SetActorRTPCValue("RTPC_WorkBench_Glow", self.ShakeIntesity, 0, ReturnValue5_4)
        ReturnValue_33: bool = self.GlowingPanel.ColorAndOpacity.A > self.GlowMin
        if not ReturnValue_33:
            goto('L4043')
        goto(ExecutionFlow.Pop())
        self.ShakeActive = True
        goto('L2698')
        self.Widget_SmallManufacturingScreen.Widget_ProgressBar.mFadeBar.SetPercent(1.5)
        self.Widget_SmallManufacturingScreen.Widget_ProgressBar.mFadeBar.SetVisibility(0)
        goto('L2984')
        self.Widget_SmallManufacturingScreen.Widget_ProgressBar.mFadeBar.SetPercent(1)
        self.Widget_SmallManufacturingScreen.Widget_ProgressBar.mFadeBar.SetVisibility(0)
        self.Widget_SmallManufacturingScreen.Widget_ProgressBar.mFadeBar.SetRenderOpacity(1.2000000476837158)
        goto('L2080')
        self.UpdateWarningWidget()
        goto(ExecutionFlow.Pop())
        if not self.DelayActive:
            goto('L10285')
        ReturnValue2_10: bool = Not_PreBool(self.mIsHolding)
        if not ReturnValue2_10:
           goto(ExecutionFlow.Pop())
        self.mIsHolding = True
        ReturnValue_34: float = 1 / self.DelayTime
        ReturnValue3_7: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.LEDAnim, 0, 1, 0, ReturnValue_34)
        Default__KismetSystemLibrary.Delay(self, self.DelayTime, LatentActionInfo(Linkage = 3610, UUID = 1202827613, ExecutionFunction = "ExecuteUbergraph_Widget_ManualManufacturing", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        # Label 10285
        self.StartProducing(ProduceSpeed)
        goto(ExecutionFlow.Pop())
        # Label 10309
        ReturnValue9: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue7_0: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_UI_OverClock_Tick, ReturnValue9, True)
        goto(ExecutionFlow.Pop())
        goto('L10309')
        self.StopAnimation(self.HideAddedToInventory)
        ReturnValue_35: List[ItemAmount] = Default__FGRecipe.GetProducts(self.mCurrentRecipe, False)
        ReturnValue2_11: int32 = self.AddedToInventoryBuffer + ReturnValue_35[0].amount
        self.AddedToInventoryBuffer = ReturnValue2_11
        FormatArgumentData.ArgumentName = "Amount"
        FormatArgumentData.ArgumentValueType = 0
        FormatArgumentData.ArgumentValue = 
        FormatArgumentData.ArgumentValueInt = self.AddedToInventoryBuffer
        FormatArgumentData.ArgumentValueFloat = 0
        FormatArgumentData.ArgumentValueGender = 0
        ReturnValue_35 = Default__FGRecipe.GetProducts(self.mCurrentRecipe, False)
        ReturnValue_36: FText = Default__FGItemDescriptor.GetItemName(ReturnValue_35[0].ItemClass)
        FormatArgumentData1.ArgumentName = "Name"
        FormatArgumentData1.ArgumentValueType = 4
        FormatArgumentData1.ArgumentValue = ReturnValue_36
        FormatArgumentData1.ArgumentValueInt = 0
        FormatArgumentData1.ArgumentValueFloat = 0
        FormatArgumentData1.ArgumentValueGender = 0
        Array: List[FormatArgumentData] = [FormatArgumentData, FormatArgumentData1]
        ReturnValue_37: FText = Default__KismetTextLibrary.Format("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 11162, 'Value': '+{Amount} {Name}'}", Array)
        self.mAddedToInventoryText.SetText(ReturnValue_37)
        ReturnValue7_1: Ptr[Pawn] = self.GetOwningPlayerPawn()
        ReturnValue1_20: List[ItemAmount] = Default__FGRecipe.GetProducts(self.mCurrentRecipe, False)
        
        numItems = None
        Default__HUDHelpers.GetNumItemsFromPlayerInventory(ReturnValue7_1, ReturnValue1_20[0].ItemClass, self, Ref[numItems])
        FormatArgumentData2.ArgumentName = "TotalAmount"
        FormatArgumentData2.ArgumentValueType = 0
        FormatArgumentData2.ArgumentValue = 
        FormatArgumentData2.ArgumentValueInt = numItems
        FormatArgumentData2.ArgumentValueFloat = 0
        FormatArgumentData2.ArgumentValueGender = 0
        Array1: List[FormatArgumentData] = [FormatArgumentData2]
        ReturnValue1_21: FText = Default__KismetTextLibrary.Format("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 11696, 'Value': '({TotalAmount} Total)'}", Array1)
        self.mTotalInInventoryText.SetText(ReturnValue1_21)
        self.mAddedToInventoryBox.SetRenderOpacity(1)
        Default__KismetSystemLibrary.RetriggerableDelay(self, 1, LatentActionInfo(Linkage = 3632, UUID = 1587283515, ExecutionFunction = "ExecuteUbergraph_Widget_ManualManufacturing", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        self.AddedToInventoryBuffer = 0
        self.mAddedToInventoryBox.SetRenderOpacity(0)
        goto(ExecutionFlow.Pop())
        ReturnValue3_8: bool = Not_PreBool(self.mOnlyShowAffordableCheckbox.mIsChecked)
        
        IsChecked = None
        self.mOnlyShowAffordableCheckbox.SetChecked(ReturnValue3_8, False, Ref[IsChecked])
        self.ShowOnlyAffordableRecipes(IsChecked)
        goto('L4119')
        
        IsChecked1 = None
        self.mOnlyShowAffordableCheckbox.SetChecked(IsChecked, False, Ref[IsChecked1])
        self.ShowOnlyAffordableRecipes(IsChecked1)
        goto('L4316')
        ReturnValue_38: FText = Default__KismetTextLibrary.Conv_StringToText(" ")
        
        Text = None
        ReturnValue_39: bool = Default__KismetTextLibrary.EqualEqual_TextText(Ref[Text], Ref[ReturnValue_38])
        if not ReturnValue_39:
            goto('L12330')
        goto(ExecutionFlow.Pop())
        # Label 12330
        self.OnSearchCreateResults(Text)
        self.ShowOnlyAffordableRecipes(self.mOnlyShowAffordableCheckbox.mIsChecked)
        goto(ExecutionFlow.Pop())
        ExecutionFlow.Push("L12409")
        goto('L4403')
        # Label 12409
        ReturnValue11: Ptr[PlayerController] = self.GetOwningPlayer()
        State1: Ptr[FGPlayerState] = Cast[FGPlayerState](ReturnValue11.PlayerState)
        bSuccess7: bool = State1
        if not bSuccess7:
           goto(ExecutionFlow.Pop())
        ReturnValue_40: bool = State1.GetOnlyShowAffordableRecipes()
        ReturnValue_41: bool = NotEqual_BoolBool(self.mOnlyShowAffordableCheckbox.mIsChecked, ReturnValue_40)
        if not ReturnValue_41:
           goto(ExecutionFlow.Pop())
        ReturnValue_40 = State1.GetOnlyShowAffordableRecipes()
        
        IsChecked2 = None
        self.mOnlyShowAffordableCheckbox.SetChecked(ReturnValue_40, True, Ref[IsChecked2])
        goto(ExecutionFlow.Pop())
        ReturnValue12: Ptr[PlayerController] = self.GetOwningPlayer()
        State2: Ptr[FGPlayerState] = Cast[FGPlayerState](ReturnValue12.PlayerState)
        bSuccess8: bool = State2
        if not bSuccess8:
           goto(ExecutionFlow.Pop())
        ReturnValue_42: int32 = self.mPhase0ScrollBox.GetChildIndex(Instigator)
        
        Item1 = None
        Item1 = self.mCategorizedRecipes[ReturnValue_42]
        State2.SetItemCategoryCollapsed(Item1.Category_5_48CE2A3C41089DC1E5DE39909CF17792, Instigator.mIsCollapsed)
        goto(ExecutionFlow.Pop())
    

    def OnRelevantClassesUpdated__DelegateSignature(self, relevantClasses: Ref[List[TSubclassOf[FGItemDescriptor]]]):
        pass
    
