
from codegen.ue4_stub import *

from Script.Engine import Texture2D
from Game.FactoryGame.Buildable.-Shared.Widgets.Widget_Manufacturing import ExecuteUbergraph_Widget_Manufacturing.K2Node_CustomEvent_Instigator
from Script.UMG import GetChildIndex
from Script.FactoryGame import EResourceForm
from Game.FactoryGame.Buildable.-Shared.Widgets.Widget_ManufacturingIOSlot import Widget_ManufacturingIOSlot
from Script.Engine import Array_Set
from Script.FactoryGame import GetCollapsedItemCategories
from Script.Engine import FTrunc
from Script.FactoryGame import GetProducts
from Script.Engine import Default__KismetSystemLibrary
from Script.UMG import GetChildAt
from Script.Engine import NotEqual_ClassClass
from Game.FactoryGame.Buildable.-Shared.WorkBench.ItemCategoryRecipeStruct import ItemCategoryRecipeStruct
from Script.Engine import FormatArgumentData
from Script.UMG import ESlateVisibility
from Script.UMG import SetText
from Game.FactoryGame.Interface.UI.InGame.Widget_UseableBase import Construct
from Script.Engine import Array_Append
from Game.FactoryGame.Buildable.-Shared.Widgets.Widget_Manufacturing import ExecuteUbergraph_Widget_Manufacturing.K2Node_Event_MyGeometry
from Script.FactoryGame import GetIngredients
from Script.Engine import IsValid
from Script.UMG import SetPercent
from Script.FactoryGame import GetAvailableRecipes
from Script.Engine import Conv_IntToText
from Script.Engine import EqualEqual_IntInt
from Script.Engine import Default__KismetTextLibrary
from Script.UMG import SetFillColorAndOpacity
from Script.FactoryGame import Init
from Script.Engine import Default__KismetStringLibrary
from Game.FactoryGame.Interface.UI.HUDHelpers.HUDHelpers import Default__HUDHelpers
from Game.FactoryGame.Interface.UI.InGame.Widget_UseableBase import Destruct
from Script.UMG import Create
from Script.FactoryGame import GetItemCategory
from Game.FactoryGame.Interface.UI.InGame.Widget_ManufacturingButton import Widget_ManufacturingButton
from Game.FactoryGame.Buildable.-Shared.Widgets.Widget_Manufacturing import ExecuteUbergraph_Widget_Manufacturing.K2Node_CustomEvent_replicationDetailActorOwner
from Script.FactoryGame import GetCanChangePotential
from Script.Engine import Array_Clear
from Script.FactoryGame import Default__FGUnlockSubsystem
from Script.CoreUObject import LinearColor
from Script.UMG import RemoveChildAt
from Script.Engine import EqualEqual_ClassClass
from Script.Engine import SetClassPropertyByName
from Script.FactoryGame import FGPlayerController
from Script.Engine import EqualEqual_ByteByte
from Script.Engine import SetObjectPropertyByName
from Game.FactoryGame.Buildable.-Shared.Widgets.Widget_Manufacturing import ExecuteUbergraph_Widget_Manufacturing.K2Node_CustomEvent_owningWidget
from Script.FactoryGame import FGBuildable
from Script.UMG import AddChildToVerticalBox
from Script.UMG import GetChildrenCount
from Script.FactoryGame import SetItemCategoryCollapsed
from Game.FactoryGame.Interface.UI.InGame.Widget_RecipeDetails import Widget_RecipeDetails
from Script.Engine import Default__KismetArrayLibrary
from Script.UMG import SetHorizontalAlignment
from Script.FactoryGame import FGInventoryComponent
from Game.FactoryGame.Buildable.-Shared.Widgets.Widget_Manufacturing import ExecuteUbergraph_Widget_Manufacturing.K2Node_CustomEvent_NewRecipe
from Script.FactoryGame import GetAmountConvertedFromItemAmount
from Script.FactoryGame import GetIsBuildingOverclockUnlocked
from Script.FactoryGame import GetCurrentRecipe
from Script.FactoryGame import Default__FGRecipe
from Script.FactoryGame import Default__FGItemCategory
from Script.Engine import Array_RemoveItem
from Script.Engine import NotEqual_ByteByte
from Script.UMG import WrapBoxSlot
from Script.FactoryGame import GetProducingPowerConsumption
from Game.FactoryGame.Buildable.-Shared.Widgets.Widget_Manufacturing import ExecuteUbergraph_Widget_Manufacturing.K2Node_ComponentBoundEvent_ButtonIndex
from Script.UMG import VerticalBoxSlot
from Script.Engine import Conv_StringToFloat
from Script.FactoryGame import Default__FGItemDescriptor
from Script.FactoryGame import FGRecipe
from Game.FactoryGame.Buildable.-Shared.Widgets.Widget_ManufacturingStat import Widget_ManufacturingStat
from Script.FactoryGame import ItemAmount
from Script.Engine import SetTextPropertyByName
from Script.Engine import Array_Contains
from Script.FactoryGame import FGPlayerState
from Script.FactoryGame import Default__FGInventoryLibrary
from Game.FactoryGame.Buildable.-Shared.Widgets.Widget_Manufacturing import ExecuteUbergraph_Widget_Manufacturing
from Script.FactoryGame import GetCategoryName
from Script.Engine import HasAuthority
from Script.FactoryGame import Get
from Script.FactoryGame import GetProductionSuffixFromFormType
from Script.Engine import PlayerController
from Script.UMG import PlayAnimation
from Script.Engine import Conv_FloatToText
from Script.FactoryGame import GetForm
from Script.UMG import Default__WidgetBlueprintLibrary
from Game.FactoryGame.Resource.Environment.Crystal.Desc_CrystalShard import Desc_CrystalShard
from Script.FactoryGame import IsProductionPaused
from Script.Engine import SetFloatPropertyByName
from Script.UMG import AddChildToWrapBox
from Script.Engine import CurveFloat
from Script.Engine import SetBoolPropertyByName
from Script.Engine import Format
from Game.FactoryGame.Interface.UI.InGame.Widget_UseableBase import Widget_UseableBase
from Script.FactoryGame import GetRemoteCallObjectOfClass
from Script.FactoryGame import GetRecipeName
from Script.FactoryGame import FGItemDescriptor
from Script.FactoryGame import GetOutputInventory
from Game.FactoryGame.Character.Player.BP_RemoteCallObject import BP_RemoteCallObject
from Script.Engine import Conv_TextToString
from Script.FactoryGame import FGItemCategory
from Script.FactoryGame import FGBuildableManufacturer
from Game.FactoryGame.Buildable.-Shared.Widgets.Widget_Manufacturing import ExecuteUbergraph_Widget_Manufacturing.K2Node_Event_InDeltaTime
from Script.Engine import Not_PreBool
from Script.FactoryGame import GetItemName
from Script.FactoryGame import GetBigIcon
from Game.FactoryGame.Interface.UI.InGame.Widget_CostSlotWrapper import Widget_CostSlotWrapper
from Game.FactoryGame.Interface.UI.Assets.Shared.Widget_CraftBench_Category import Widget_CraftBench_Category
from Script.FactoryGame import FGBuildableFactory
from Script.Engine import BooleanOR
from Script.UMG import Tick
from Script.UMG import Widget
from Script.FactoryGame import FGUnlockSubsystem
from Script.FactoryGame import GetItemDescription
from Game.FactoryGame.Buildable.-Shared.Widgets.Widget_Manufacturing import ExecuteUbergraph_Widget_Manufacturing.K2Node_CustomEvent_owningWidget1
from Script.Engine import SelectColor
from Script.FactoryGame import GetProductivity
from Script.UMG import UMGSequencePlayer
from Script.Engine import Array_IsValidIndex
from Script.Engine import Min
from Script.UMG import SetRenderOpacity
from Script.Engine import IsValidClass

class Widget_Manufacturing(Widget_UseableBase):
    mBuildableManufacturer: Ptr[FGBuildableManufacturer]
    mActivatedRecipe: TSubclassOf[FGRecipe]
    mHoveredRecipe: TSubclassOf[FGRecipe]
    mFactory: Ptr[FGBuildableFactory]
    mProgressCurve: Ptr[CurveFloat] = Namespace(AssetPath='/Game/FactoryGame/Buildable/-Shared/Curves/TestCurve.TestCurve')
    mIOSlots: List[Ptr[Widget_ManufacturingIOSlot]]
    mRelevantItems: List[TSubclassOf[FGItemDescriptor]]
    mCategorizedRecipes: List[ItemCategoryRecipeStruct]
    NewVar_0_0: FText
    mHoverWidget: Ptr[Widget_RecipeDetails]
    mShouldOpenInventory = True
    mUseMouse = True
    mCaptureInput = True
    mRestoreFocusWhenLost = True
    mDesiredHorizontalAlignment = 2
    mDesiredVerticalAlignment = 2
    mCallCustomTickOnConstruct = True
    bHasScriptImplementedTick = True
    
    def GetCylceProducedAndNameText(self, Recipe: TSubclassOf[FGRecipe]):
        ReturnValue: List[ItemAmount] = Default__FGRecipe.GetProducts(Recipe, False)
        ReturnValue_0: FText = Default__FGRecipe.GetRecipeName(Recipe)
        
        Item = None
        Item = ReturnValue[1]
        FormatArgumentData.ArgumentName = "B"
        FormatArgumentData.ArgumentValueType = 4
        FormatArgumentData.ArgumentValue = ReturnValue_0
        FormatArgumentData.ArgumentValueInt = 0
        FormatArgumentData.ArgumentValueFloat = 0
        FormatArgumentData.ArgumentValueGender = 0
        
        Item = None
        itemClass = None
        amountConverted = None
        Default__FGInventoryLibrary.GetAmountConvertedFromItemAmount(Ref[Item], Ref[itemClass], Ref[amountConverted])
        
        itemAmount = None
        self.GetItemAmount(Recipe, Ref[itemAmount])
        FormatArgumentData1.ArgumentName = "A"
        FormatArgumentData1.ArgumentValueType = 2
        FormatArgumentData1.ArgumentValue = 
        FormatArgumentData1.ArgumentValueInt = 0
        FormatArgumentData1.ArgumentValueFloat = amountConverted
        FormatArgumentData1.ArgumentValueGender = 0
        
        itemAmount = None
        itemClass1 = None
        amountConverted1 = None
        Default__FGInventoryLibrary.GetAmountConvertedFromItemAmount(Ref[itemAmount], Ref[itemClass1], Ref[amountConverted1])
        ReturnValue_1: FText = Default__FGItemDescriptor.GetItemName(itemClass)
        FormatArgumentData2.ArgumentName = "A"
        FormatArgumentData2.ArgumentValueType = 2
        FormatArgumentData2.ArgumentValue = 
        FormatArgumentData2.ArgumentValueInt = 0
        # Label 876
        FormatArgumentData2.ArgumentValueFloat = amountConverted1
        FormatArgumentData2.ArgumentValueGender = 0
        FormatArgumentData3.ArgumentName = "B"
        FormatArgumentData3.ArgumentValueType = 4
        FormatArgumentData3.ArgumentValue = ReturnValue_1
        FormatArgumentData3.ArgumentValueInt = 0
        FormatArgumentData3.ArgumentValueFloat = 0
        FormatArgumentData3.ArgumentValueGender = 0
        ReturnValue_2: uint8 = Default__FGItemDescriptor.GetForm(itemClass1)
        ReturnValue1: uint8 = Default__FGItemDescriptor.GetForm(itemClass)
        ReturnValue_3: bool = NotEqual_ByteByte(ReturnValue_2, 1)
        ReturnValue1_0: bool = NotEqual_ByteByte(ReturnValue1, 1)
        ReturnValue_4: FText = Default__FGInventoryLibrary.GetProductionSuffixFromFormType(ReturnValue_2)
        FormatArgumentData4.ArgumentName = "suffix"
        # Label 1403
        FormatArgumentData4.ArgumentValueType = 4
        FormatArgumentData4.ArgumentValue = ReturnValue_4
        FormatArgumentData4.ArgumentValueInt = 0
        FormatArgumentData4.ArgumentValueFloat = 0
        FormatArgumentData4.ArgumentValueGender = 0
        Variable1: bool = ReturnValue_3
        Array: List[FormatArgumentData] = [FormatArgumentData4]
        ReturnValue_5: FText = Default__KismetTextLibrary.Format("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 1651, 'Value': '{suffix} '}", Array)
        Variable: FText = 
        Variable1_0: FText = 
        FormatArgumentData5.ArgumentName = "Suffix"
        FormatArgumentData5.ArgumentValueType = 4
        
        switch = {
            False: Variable,
            True: ReturnValue_5
        }
        FormatArgumentData5.ArgumentValue = switch.get(Variable1, None)
        FormatArgumentData5.ArgumentValueInt = 0
        FormatArgumentData5.ArgumentValueFloat = 0
        FormatArgumentData5.ArgumentValueGender = 0
        Array1: List[FormatArgumentData] = [FormatArgumentData2, FormatArgumentData5, FormatArgumentData]
        ReturnValue1_1: List[ItemAmount] = Default__FGRecipe.GetProducts(Recipe, False)
        ReturnValue1_2: FText = Default__KismetTextLibrary.Format("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 2134, 'Value': '{A} {Suffix}{B}'}", Array1)
        
        ReturnValue_6: int32 = len(ReturnValue1_1)
        FormatArgumentData6.ArgumentName = "a"
        FormatArgumentData6.ArgumentValueType = 4
        FormatArgumentData6.ArgumentValue = ReturnValue1_2
        FormatArgumentData6.ArgumentValueInt = 0
        FormatArgumentData6.ArgumentValueFloat = 0
        FormatArgumentData6.ArgumentValueGender = 0
        ReturnValue_7: bool = ReturnValue_6 > 1
        Variable_0: bool = ReturnValue_7
        Variable2: bool = ReturnValue1_0
        Array2: List[FormatArgumentData] = [FormatArgumentData(ArgumentName = "", ArgumentValueType = 0, ArgumentValue = , ArgumentValueInt = 0, ArgumentValueFloat = 0, ArgumentValueGender = 0)]
        ReturnValue2: FText = Default__KismetTextLibrary.Format("{'Instruction': 'EX_UnicodeStringConst', 'InstOffsetFromTop': 2610, 'Value': 'm³'}", Array2)
        FormatArgumentData7.ArgumentName = "Suffix"
        FormatArgumentData7.ArgumentValueType = 4
        
        switch_0 = {
            False: Variable1_0,
            True: ReturnValue2
        }
        FormatArgumentData7.ArgumentValue = switch_0.get(Variable2, None)
        FormatArgumentData7.ArgumentValueInt = 0
        FormatArgumentData7.ArgumentValueFloat = 0
        FormatArgumentData7.ArgumentValueGender = 0
        Array3: List[FormatArgumentData] = [FormatArgumentData1, FormatArgumentData7, FormatArgumentData3]
        ReturnValue3: FText = Default__KismetTextLibrary.Format("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 2989, 'Value': '{A} {Suffix}{B}'}", Array3)
        FormatArgumentData8.ArgumentName = "b"
        FormatArgumentData8.ArgumentValueType = 4
        FormatArgumentData8.ArgumentValue = ReturnValue3
        FormatArgumentData8.ArgumentValueInt = 0
        FormatArgumentData8.ArgumentValueFloat = 0
        FormatArgumentData8.ArgumentValueGender = 0
        Array4: List[FormatArgumentData] = [FormatArgumentData6, FormatArgumentData8]
        ReturnValue4: FText = Default__KismetTextLibrary.Format("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 3320, 'Value': '{a},\r\n{b}'}", Array4)
        
        switch_1 = {
            False: ReturnValue1_2,
            True: ReturnValue4
        }
        ReturnValue_8: FText = switch_1.get(Variable_0, None)
    

    def CreateCategoryHeader(self, Container: Ptr[PanelWidget], CategoryName: FText, IsCollapsed: bool):
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_0: Ptr[Widget_CraftBench_Category] = Default__WidgetBlueprintLibrary.Create(self, Widget_CraftBench_Category, ReturnValue)
        
        Default__KismetSystemLibrary.SetTextPropertyByName(ReturnValue_0, "mText", Ref[CategoryName])
        Default__KismetSystemLibrary.SetBoolPropertyByName(ReturnValue_0, "mIsCollapsed", IsCollapsed)
        ReturnValue_1: Ptr[VerticalBoxSlot] = self.mVertBox.AddChildToVerticalBox(ReturnValue_0)
        ReturnValue_1.SetHorizontalAlignment(0)
        Category Widget = ReturnValue_0
    

    def AddUniqueRecipe(self, CategorizedRecipes: Ref[List[ItemCategoryRecipeStruct]], Recipe: TSubclassOf[FGRecipe]):
        ExecutionFlow.Push("L1312")
        # Label 5
        ReturnValue: List[ItemAmount] = Default__FGRecipe.GetProducts(Recipe, False)
        ReturnValue_0: TSubclassOf[FGItemCategory] = Default__FGItemDescriptor.GetItemCategory(ReturnValue[0].ItemClass)
        ReturnValue_1: bool = Default__KismetSystemLibrary.IsValidClass(ReturnValue_0)
        if not ReturnValue_1:
            goto('L1034')
        ReturnValue = Default__FGRecipe.GetProducts(Recipe, False)
        ReturnValue_0 = Default__FGItemDescriptor.GetItemCategory(ReturnValue[0].ItemClass)
        localItemCategory = ReturnValue_0
        Variable: bool = False
        Variable_0: int32 = 0
        Variable_1: int32 = 0
        # Label 398
        ReturnValue_2: bool = Not_PreBool(Variable)
        
        ReturnValue_3: int32 = len(CategorizedRecipes)
        ReturnValue_4: bool = Variable_0 <= ReturnValue_3
        ReturnValue_5: bool = ReturnValue_2 and ReturnValue_4
        if not ReturnValue_5:
            goto('L1046')
        Variable_1 = Variable_0
        ExecutionFlow.Push("L1238")
        
        Item = None
        Item = CategorizedRecipes[Variable_1]
        ReturnValue_6: bool = EqualEqual_ClassClass(localItemCategory, Item.Category_5_48CE2A3C41089DC1E5DE39909CF17792)
        if not ReturnValue_6:
           goto(ExecutionFlow.Pop())
        
        Item = None
        # Label 724
        Item = CategorizedRecipes[Variable_1]
        localRecipeArray = Item.Recipes_6_5C2C7BF54D78A483A81B2785C2CF7736
        
        ReturnValue1: int32 = localRecipeArray.append(Recipe)
        ItemCategoryRecipeStruct1.Category_5_48CE2A3C41089DC1E5DE39909CF17792 = localItemCategory
        ItemCategoryRecipeStruct1.Recipes_6_5C2C7BF54D78A483A81B2785C2CF7736 = localRecipeArray
        
        ItemCategoryRecipeStruct1 = None
        Default__KismetArrayLibrary.Array_Set(Variable_1, False, Ref[CategorizedRecipes], Ref[ItemCategoryRecipeStruct1])
        localRecipeExists = True
        Variable = True
        goto(ExecutionFlow.Pop())
        # Label 1034
        localItemCategory = None
        goto(ExecutionFlow.Pop())
        # Label 1046
        ReturnValue1_0: bool = Not_PreBool(localRecipeExists)
        if not ReturnValue1_0:
           goto(ExecutionFlow.Pop())
        Array: List[TSubclassOf[FGRecipe]] = [Recipe]
        ItemCategoryRecipeStruct.Category_5_48CE2A3C41089DC1E5DE39909CF17792 = localItemCategory
        ItemCategoryRecipeStruct.Recipes_6_5C2C7BF54D78A483A81B2785C2CF7736 = Array
        
        ItemCategoryRecipeStruct = None
        ReturnValue_7: int32 = CategorizedRecipes.append(ItemCategoryRecipeStruct)
        goto(ExecutionFlow.Pop())
        # Label 1238
        ReturnValue_8: int32 = Variable_0 + 1
        Variable_0 = ReturnValue_8
        goto('L398')
    

    def GenerateOutputSlots(self):
        ExecutionFlow.Push("L1152")
        # Label 5
        Variable: int32 = 0
        Variable_0: int32 = 0
        # Label 51
        ReturnValue: List[ItemAmount] = Default__FGRecipe.GetProducts(self.mActivatedRecipe, False)
        
        # Label 111
        ReturnValue_0: int32 = len(ReturnValue)
        ReturnValue_1: bool = Variable <= ReturnValue_0
        if not ReturnValue_1:
            goto('L982')
        Variable_0 = Variable
        ExecutionFlow.Push("L1078")
        ReturnValue = Default__FGRecipe.GetProducts(self.mActivatedRecipe, False)
        
        Item = None
        Item = ReturnValue[Variable_0]
        LocalItemClass = Item.ItemClass
        LocalIndex = Variable_0
        Variable_1: FText = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 448, 'Value': 'Fluid'}"
        Variable1: FText = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 511, 'Value': 'Output'}"
        # Label 555
        ReturnValue_2: uint8 = Default__FGItemDescriptor.GetForm(LocalItemClass)
        ReturnValue_3: bool = EqualEqual_ByteByte(ReturnValue_2, 2)
        Variable1_0: bool = ReturnValue_3
        Variable_2: bool = ReturnValue_3
        ReturnValue_4: Ptr[FGInventoryComponent] = self.mBuildableManufacturer.GetOutputInventory()
        
        switch = {
            False: Variable1,
            True: Variable_1
        }
        Struct.Title_3_16865392480E04744923368E818FDF9E = switch.get(Variable_2, None)
        Struct.InventoryComponent_6_670B318B4DE9249E98B040BFD46013A9 = ReturnValue_4
        Struct.InventorySlotIndex_10_ECF91A0C4E759F6F2FC3768CE0512AB9 = LocalIndex
        
        switch_0 = {
            False: SolidOutputs,
            True: LiquidOutputs
        }
        
        switch_0.get(Variable1_0, None) = None
        Struct = None
        ReturnValue_5: int32 = switch_0.get(Variable1_0, None).append(Struct)
        goto(ExecutionFlow.Pop())
        
        # Label 982
        Default__KismetArrayLibrary.Array_Append(Ref[SolidOutputs], Ref[LiquidOutputs])
        
        self.Widget_Output_Slot.GenerateOutputSlots(Ref[SolidOutputs])
        goto(ExecutionFlow.Pop())
        # Label 1078
        ReturnValue_6: int32 = Variable + 1
        Variable = ReturnValue_6
        goto('L51')
    

    def SetActivatedRecipe(self, mActivatedRecipe: TSubclassOf[FGRecipe]):
        ExecutionFlow.Push("L1403")
        # Label 5
        self.mActivatedRecipe = mActivatedRecipe
        
        Default__KismetArrayLibrary.Array_Clear(Ref[self.mRelevantItems])
        Variable: int32 = 0
        Variable1: int32 = 0
        # Label 111
        ReturnValue: List[ItemAmount] = Default__FGRecipe.GetIngredients(self.mActivatedRecipe)
        
        ReturnValue1: int32 = len(ReturnValue)
        ReturnValue1_0: bool = Variable <= ReturnValue1
        if not ReturnValue1_0:
            goto('L509')
        Variable1 = Variable
        ExecutionFlow.Push("L1255")
        ReturnValue = Default__FGRecipe.GetIngredients(self.mActivatedRecipe)
        
        Item1 = None
        Item1 = ReturnValue[Variable1]
        
        Item1.ItemClass = None
        ReturnValue2: int32 = self.mRelevantItems.append(Item1.ItemClass)
        goto(ExecutionFlow.Pop())
        # Label 509
        Variable1_0: int32 = 0
        Variable_0: int32 = 0
        # Label 555
        ReturnValue_0: List[ItemAmount] = Default__FGRecipe.GetProducts(self.mActivatedRecipe, False)
        
        ReturnValue_1: int32 = len(ReturnValue_0)
        ReturnValue_2: bool = Variable1_0 <= ReturnValue_1
        if not ReturnValue_2:
            goto('L955')
        Variable_0 = Variable1_0
        ExecutionFlow.Push("L1329")
        ReturnValue_0 = Default__FGRecipe.GetProducts(self.mActivatedRecipe, False)
        
        Item = None
        Item = ReturnValue_0[Variable_0]
        
        Item.ItemClass = None
        ReturnValue1_1: int32 = self.mRelevantItems.append(Item.ItemClass)
        goto(ExecutionFlow.Pop())
        # Label 955
        ReturnValue_3: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_4: Ptr[FGUnlockSubsystem] = Default__FGUnlockSubsystem.Get(ReturnValue_3)
        ReturnValue_5: bool = ReturnValue_4.GetIsBuildingOverclockUnlocked()
        if not ReturnValue_5:
            goto('L1173')
        Variable_1: Const[TSubclassOf[FGItemDescriptor]] = Desc_CrystalShard
        
        ReturnValue_6: int32 = self.mRelevantItems.append(Variable_1)
        
        # Label 1173
        self.Widget_Window_DarkMode.SetupRelevantInventory(Ref[self.mRelevantItems])
        self.Widget_Overclock.SetDefaultProductionSpeed()
        goto(ExecutionFlow.Pop())
        # Label 1255
        ReturnValue_7: int32 = Variable + 1
        Variable = ReturnValue_7
        goto('L111')
        # Label 1329
        ReturnValue1_2: int32 = Variable1_0 + 1
        Variable1_0 = ReturnValue1_2
        goto('L555')
    

    def ReconstructIOSlots(self):
        ExecutionFlow.Push("L361")
        # Label 5
        Variable: int32 = 0
        Variable_0: int32 = 0
        
        # Label 51
        ReturnValue: int32 = len(self.mIOSlots)
        ReturnValue_0: bool = Variable <= ReturnValue
        if not ReturnValue_0:
           goto(ExecutionFlow.Pop())
        Variable_0 = Variable
        ExecutionFlow.Push("L287")
        
        Item = None
        Item = self.mIOSlots[Variable_0]
        Item.ConstructFromManufacturingWidget(self)
        goto(ExecutionFlow.Pop())
        # Label 287
        ReturnValue_1: int32 = Variable + 1
        Variable = ReturnValue_1
        goto('L51')
    

    def DropInventorySlotStack(self):
        ExecutionFlow.Push("L1349")
        # Label 5
        ExecutionFlow.Push("L475")
        # Label 10
        Variable1: bool = False
        Variable: int32 = 0
        Variable1_0: int32 = 0
        # Label 67
        ReturnValue1: bool = Not_PreBool(Variable1)
        
        ReturnValue1_0: int32 = len(self.mIOSlots)
        ReturnValue1_1: bool = Variable <= ReturnValue1_0
        ReturnValue1_2: bool = ReturnValue1 and ReturnValue1_1
        if not ReturnValue1_2:
            goto('L499')
        Variable1_0 = Variable
        ExecutionFlow.Push("L1275")
        
        Item1 = None
        Item1 = self.mIOSlots[Variable1_0]
        
        Result1 = None
        Item1.Widget_CostSlotWrapper.Widget_InventorySlot.DropOntoInventorySlot(InventorySlot, Ref[Result1])
        LocalResult = Result1
        if not LocalResult:
           goto(ExecutionFlow.Pop())
        Variable1 = True
        goto(ExecutionFlow.Pop())
        # Label 475
        WasStackMoved = LocalResult
        # End
        # Label 499
        if not LocalResult:
            goto('L514')
        goto(ExecutionFlow.Pop())
        
        Slots = None
        # Label 514
        self.Widget_Overclock.GetUnlockedOverclockSlots(Ref[Slots])
        Variable_0: bool = False
        Variable1_1: int32 = 0
        Variable_1: int32 = 0
        # Label 616
        ReturnValue: bool = Not_PreBool(Variable_0)
        
        Slots = None
        ReturnValue_0: int32 = len(Slots)
        ReturnValue_1: bool = Variable1_1 <= ReturnValue_0
        ReturnValue_2: bool = ReturnValue and ReturnValue_1
        if not ReturnValue_2:
            goto('L1255')
        Variable_1 = Variable1_1
        ExecutionFlow.Push("L1181")
        Variable1_2: bool = True
        
        Slots = None
        Item = None
        Item = Slots[Variable_1]
        
        slotHasItems = None
        Item.CheckSlotHasItems(Ref[slotHasItems])
        ReturnValue2: bool = Not_PreBool(slotHasItems)
        Variable2: bool = True
        
        switch = {
            False: Variable2,
            True: ReturnValue2
        }
        if not switch.get(Variable1_2, None):
           goto(ExecutionFlow.Pop())
        
        Slots = None
        Item = None
        Item = Slots[Variable_1]
        
        Result = None
        Item.DropOntoInventorySlot(InventorySlot, Ref[Result])
        if not Result:
           goto(ExecutionFlow.Pop())
        Variable_2: bool = True
        Variable_0 = True
        goto(ExecutionFlow.Pop())
        # Label 1181
        ReturnValue1_3: int32 = Variable1_1 + 1
        Variable1_1 = ReturnValue1_3
        goto('L616')
        # Label 1255
        LocalResult = Variable_2
        goto(ExecutionFlow.Pop())
        # Label 1275
        ReturnValue_3: int32 = Variable + 1
        Variable = ReturnValue_3
        goto('L67')
    

    def UpdateWindowText(self):
        AsFGBuildable: Ptr[FGBuildable] = Cast[FGBuildable](self.mInteractObject)
        bSuccess: bool = AsFGBuildable
        if not bSuccess:
            goto('L146')
        self.Widget_Window_DarkMode.SetTitle(AsFGBuildable.mDisplayName)
    

    def GetItemAmount(self, Recipe: TSubclassOf[FGRecipe]):
        ReturnValue: bool = Default__KismetSystemLibrary.IsValidClass(Recipe)
        # Label 51
        if not ReturnValue:
            goto('L207')
        ReturnValue_0: List[ItemAmount] = Default__FGRecipe.GetProducts(Recipe, False)
        
        Item = None
        Item = ReturnValue_0[0]
        ItemAmount = Item
    

    def GetManufacturingWarningVisibility(self, buildableManufacturer: Ptr[FGBuildableManufacturer]):
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(buildableManufacturer)
        # Label 51
        if not ReturnValue:
            goto('L368')
        ReturnValue_0: bool = buildableManufacturer.HasPower()
        # Label 111
        ReturnValue_1: bool = Not_PreBool(ReturnValue_0)
        ReturnValue_2: bool = buildableManufacturer.IsProductionPaused()
        ReturnValue_3: bool = BooleanOR(ReturnValue_2, ReturnValue_1)
        Variable: uint8 = 3
        Variable_0: bool = ReturnValue_3
        Variable1: uint8 = 1
        
        switch = {
            False: Variable1,
            True: Variable
        }
        # Label 279
        self.Widget_Manufacturing_Warning.SetVisibility(switch.get(Variable_0, None))
    

    def UpdateProductionStats(self):
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(self.mBuildableManufacturer)
        # Label 51
        if not ReturnValue:
            goto('L724')
        ReturnValue_0: bool = Default__KismetSystemLibrary.IsValidClass(self.mActivatedRecipe)
        if not ReturnValue_0:
            goto('L724')
        ReturnValue_1: List[ItemAmount] = Default__FGRecipe.GetProducts(self.mActivatedRecipe, False)
        
        ReturnValue_2: int32 = len(ReturnValue_1)
        ReturnValue_3: bool = ReturnValue_2 > 1
        if not ReturnValue_3:
            goto('L448')
        ReturnValue_1 = Default__FGRecipe.GetProducts(self.mActivatedRecipe, False)
        
        Item = None
        Item = ReturnValue_1[1]
        LocalSecondAmount = Item.amount
        # Label 448
        ReturnValue_4: float = self.mBuildableManufacturer.GetProductivity()
        ReturnValue_5: float = self.mBuildableManufacturer.GetProductionCycleTime()
        ReturnValue_6: float = self.mBuildableManufacturer.GetProducingPowerConsumption()
        
        itemAmount = None
        self.GetItemAmount(self.mActivatedRecipe, Ref[itemAmount])
        self.Widget_Output_Slot.UpdateProductionStats(itemAmount.amount, ReturnValue_5, ReturnValue_6, ReturnValue_4, LocalSecondAmount)
    

    def UpdateOutputSlotInfo(self, Recipe: TSubclassOf[FGRecipe]):
        ReturnValue: FText = self.GetCylceProducedAndNameText(Recipe)
        self.Widget_Output_Slot.mRecipeName.SetText(ReturnValue)
        self.GenerateOutputSlots()
        
        itemAmount = None
        self.GetItemAmount(Recipe, Ref[itemAmount])
        self.Widget_Output_Slot.mItemDescriptor = itemAmount.ItemClass
        ReturnValue1: List[ItemAmount] = Default__FGRecipe.GetProducts(Recipe, False)
        
        ReturnValue_0: int32 = len(ReturnValue1)
        ReturnValue_1: bool = ReturnValue_0 > 1
        if not ReturnValue_1:
            goto('L707')
        ReturnValue_2: List[ItemAmount] = Default__FGRecipe.GetProducts(Recipe, False)
        
        Item = None
        Item = ReturnValue_2[1]
        ReturnValue1 = Default__FGRecipe.GetProducts(Recipe, False)
        
        ReturnValue_0 = len(ReturnValue1)
        ReturnValue_1 = ReturnValue_0 > 1
        self.Widget_Output_Slot.SetShowSecondPartsPerMin(ReturnValue_1, Item.ItemClass)
        # End
        # Label 707
        self.Widget_Output_Slot.SetShowSecondPartsPerMin(False, None)
    

    def UpdateProductivityPercentage(self):
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(self.mBuildableManufacturer)
        # Label 51
        if not ReturnValue:
            goto('L1233')
        ReturnValue1: float = self.mFactory.GetProductionProgress()
        self.Widget_Output_Slot.mProgressBar.mProgressBar.SetPercent(ReturnValue1)
        ReturnValue_0: bool = self.mBuildableManufacturer.IsProductionPaused()
        ReturnValue_1: bool = self.mBuildableManufacturer.HasPower()
        ReturnValue_2: bool = Not_PreBool(ReturnValue_1)
        ReturnValue_3: bool = BooleanOR(ReturnValue_2, ReturnValue_0)
        
        Text = None
        Graphics = None
        Default__HUDHelpers.GetFactoryGameLightGray(self, Ref[Text], Ref[Graphics])
        
        Text = None
        Graphics = None
        Default__HUDHelpers.GetFactoryGameDarkGray(self, Ref[Text], Ref[Graphics])
        ReturnValue_4: LinearColor = SelectColor(Graphics, Graphics, ReturnValue_3)
        self.Widget_Output_Slot.mProgressBar.mProgressBar.SetFillColorAndOpacity(ReturnValue_4)
        ReturnValue_5: float = self.mFactory.GetProductionProgress()
        ReturnValue_6: float = ReturnValue_5 * 10
        ReturnValue_7: int32 = FTrunc(ReturnValue_6)
        ReturnValue_8: int32 = ReturnValue_7 * 10
        ReturnValue_9: FText = Default__KismetTextLibrary.Conv_IntToText(ReturnValue_8, False, False, 1, 324)
        FormatArgumentData.ArgumentName = "A"
        FormatArgumentData.ArgumentValueType = 4
        FormatArgumentData.ArgumentValue = ReturnValue_9
        FormatArgumentData.ArgumentValueInt = 0
        # Label 982
        FormatArgumentData.ArgumentValueFloat = 0
        FormatArgumentData.ArgumentValueGender = 0
        Array: List[FormatArgumentData] = [FormatArgumentData]
        ReturnValue_10: FText = Default__KismetTextLibrary.Format("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 1114, 'Value': '{A}%'}", Array)
        self.Widget_Output_Slot.mPercentageText.SetText(ReturnValue_10)
    

    def GetPotentialButton(self):
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(self.mBuildableManufacturer)
        # Label 51
        if not ReturnValue:
            goto('L166')
        ReturnValue_0: bool = self.mBuildableManufacturer.GetCanChangePotential()
        if not ReturnValue_0:
            goto('L146')
        ReturnValue_1: uint8 = 0
        goto('L166')
        # Label 146
        ReturnValue_1 = 1
    

    def CreateInfoBox(self, Recipe: TSubclassOf[FGRecipe]):
        ExecutionFlow.Push("L4222")
        # Label 5
        ReturnValue: bool = Default__KismetSystemLibrary.IsValidClass(Recipe)
        Variable: uint8 = 2
        Variable1: uint8 = 0
        Variable_0: bool = ReturnValue
        
        switch = {
            False: Variable,
            True: Variable1
        }
        self.Widget_BuildMenu_InfoBox.SetVisibility(switch.get(Variable_0, None))
        self.Widget_BuildMenu_InfoBox.mStatContainer.ClearChildren()
        
        self.Widget_BuildMenu_InfoBox.mByProductText.SetText(Ref[localClearText])
        self.Widget_BuildMenu_InfoBox.mCostContainer.ClearChildren()
        Variable_1: int32 = 0
        Variable_2: int32 = 0
        # Label 429
        ReturnValue_0: List[ItemAmount] = Default__FGRecipe.GetIngredients(Recipe)
        
        # Label 488
        ReturnValue_1: int32 = len(ReturnValue_0)
        ReturnValue_2: bool = Variable_1 <= ReturnValue_1
        if not ReturnValue_2:
            goto('L1027')
        Variable_2 = Variable_1
        ExecutionFlow.Push("L4024")
        ReturnValue1: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue1_0: Ptr[Widget_CostSlotWrapper] = Default__WidgetBlueprintLibrary.Create(self, Widget_CostSlotWrapper, ReturnValue1)
        ReturnValue_0 = Default__FGRecipe.GetIngredients(Recipe)
        
        Item = None
        Item = ReturnValue_0[Variable_2]
        ReturnValue1_0.Setup CostIcon(None, Item, None, 0, 0, False, False, False)
        ReturnValue1_1: Ptr[WrapBoxSlot] = self.Widget_BuildMenu_InfoBox.mCostContainer.AddChildToWrapBox(ReturnValue1_0)
        ReturnValue1_0.mCostSlotContainer.SetRenderOpacity(0)
        goto(ExecutionFlow.Pop())
        # Label 1027
        ExecutionFlow.Push("L3428")
        
        itemAmount = None
        self.GetItemAmount(self.mHoveredRecipe, Ref[itemAmount])
        
        itemAmount = None
        itemClass = None
        amountConverted = None
        Default__FGInventoryLibrary.GetAmountConvertedFromItemAmount(Ref[itemAmount], Ref[itemClass], Ref[amountConverted])
        ReturnValue1_2: Ptr[Texture2D] = Default__FGItemDescriptor.GetBigIcon(itemClass)
        SlateBrush1.ImageSize = self.Widget_BuildMenu_InfoBox.mPreviewIcon.Brush.ImageSize
        SlateBrush1.Margin = self.Widget_BuildMenu_InfoBox.mPreviewIcon.Brush.Margin
        SlateBrush1.TintColor = self.Widget_BuildMenu_InfoBox.mPreviewIcon.Brush.TintColor
        SlateBrush1.ResourceObject = ReturnValue1_2
        SlateBrush1.DrawAs = self.Widget_BuildMenu_InfoBox.mPreviewIcon.Brush.DrawAs
        SlateBrush1.Tiling = self.Widget_BuildMenu_InfoBox.mPreviewIcon.Brush.Tiling
        SlateBrush1.Mirroring = self.Widget_BuildMenu_InfoBox.mPreviewIcon.Brush.Mirroring
        
        SlateBrush1 = None
        self.Widget_BuildMenu_InfoBox.mPreviewIcon.SetBrush(Ref[SlateBrush1])
        ReturnValue_3: FText = self.GetCylceProducedAndNameText(self.mHoveredRecipe)
        self.Widget_BuildMenu_InfoBox.mItemName.SetText(ReturnValue_3)
        
        itemAmount = None
        self.GetItemAmount(self.mHoveredRecipe, Ref[itemAmount])
        
        itemAmount = None
        itemClass = None
        amountConverted = None
        Default__FGInventoryLibrary.GetAmountConvertedFromItemAmount(Ref[itemAmount], Ref[itemClass], Ref[amountConverted])
        ReturnValue1_3: FText = Default__FGItemDescriptor.GetItemDescription(itemClass)
        
        self.Widget_BuildMenu_InfoBox.mRichTextBlock.SetText(Ref[ReturnValue1_3])
        ReturnValue1_4: List[ItemAmount] = Default__FGRecipe.GetProducts(self.mHoveredRecipe, False)
        
        ReturnValue_4: bool = Default__KismetArrayLibrary.Array_IsValidIndex(1, Ref[ReturnValue1_4])
        self.Widget_BuildMenu_InfoBox.GetByProductIconVisibility(ReturnValue_4)
        ReturnValue1_4 = Default__FGRecipe.GetProducts(self.mHoveredRecipe, False)
        
        ReturnValue_4 = Default__KismetArrayLibrary.Array_IsValidIndex(1, Ref[ReturnValue1_4])
        if not ReturnValue_4:
            goto('L4098')
        ReturnValue1_4 = Default__FGRecipe.GetProducts(self.mHoveredRecipe, False)
        ReturnValue_5: FText = Default__FGItemDescriptor.GetItemDescription(ReturnValue1_4[1].ItemClass)
        
        self.Widget_BuildMenu_InfoBox.mByProductText.SetText(Ref[ReturnValue_5])
        self.Widget_BuildMenu_InfoBox.mByProductBox.SetVisibility(0)
        ReturnValue_6: List[ItemAmount] = Default__FGRecipe.GetProducts(self.mHoveredRecipe, False)
        ReturnValue_7: Ptr[Texture2D] = Default__FGItemDescriptor.GetBigIcon(ReturnValue_6[1].ItemClass)
        SlateBrush.ImageSize = self.Widget_BuildMenu_InfoBox.mByProductIcon.Brush.ImageSize
        SlateBrush.Margin = self.Widget_BuildMenu_InfoBox.mByProductIcon.Brush.Margin
        SlateBrush.TintColor = self.Widget_BuildMenu_InfoBox.mByProductIcon.Brush.TintColor
        SlateBrush.ResourceObject = ReturnValue_7
        SlateBrush.DrawAs = self.Widget_BuildMenu_InfoBox.mByProductIcon.Brush.DrawAs
        SlateBrush.Tiling = self.Widget_BuildMenu_InfoBox.mByProductIcon.Brush.Tiling
        SlateBrush.Mirroring = self.Widget_BuildMenu_InfoBox.mByProductIcon.Brush.Mirroring
        
        SlateBrush = None
        self.Widget_BuildMenu_InfoBox.mByProductIcon.SetBrush(Ref[SlateBrush])
        goto(ExecutionFlow.Pop())
        # Label 3428
        ReturnValue_8: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_9: Ptr[Widget_ManufacturingStat] = Default__WidgetBlueprintLibrary.Create(self, Widget_ManufacturingStat, ReturnValue_8)
        Default__KismetSystemLibrary.SetBoolPropertyByName(ReturnValue_9, "isCycleTime", True)
        ReturnValue_10: float = self.mBuildableManufacturer.GetProductionCycleTimeForRecipe(self.mHoveredRecipe)
        ReturnValue_11: FText = Default__KismetTextLibrary.Conv_FloatToText(ReturnValue_10, 0, False, True, 1, 324, 1, 1)
        
        ReturnValue_12: FString = Default__KismetTextLibrary.Conv_TextToString(Ref[ReturnValue_11])
        ReturnValue_13: float = Default__KismetStringLibrary.Conv_StringToFloat(ReturnValue_12)
        Default__KismetSystemLibrary.SetFloatPropertyByName(ReturnValue_9, "mManufacturingStat", ReturnValue_13)
        Default__KismetSystemLibrary.SetBoolPropertyByName(ReturnValue_9, "mWhiteIcon", True)
        ReturnValue_14: Ptr[WrapBoxSlot] = self.Widget_BuildMenu_InfoBox.mStatContainer.AddChildToWrapBox(ReturnValue_9)
        goto(ExecutionFlow.Pop())
        # Label 4024
        ReturnValue_15: int32 = Variable_1 + 1
        Variable_1 = ReturnValue_15
        goto('L429')
        
        # Label 4098
        self.Widget_BuildMenu_InfoBox.mByProductText.SetText(Ref[localClearText])
        self.Widget_BuildMenu_InfoBox.mByProductBox.SetVisibility(1)
        goto(ExecutionFlow.Pop())
    

    def OnManufacturingRecipeClicked(self, Recipe: TSubclassOf[FGRecipe]):
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        Controller: Ptr[FGPlayerController] = Cast[FGPlayerController](ReturnValue)
        bSuccess: bool = Controller
        if not bSuccess:
            goto('L348')
        ReturnValue_0: Ptr[BP_RemoteCallObject] = Controller.GetRemoteCallObjectOfClass(BP_RemoteCallObject)
        ReturnValue_0.Server_SetRecipeOnManufacturingProxy(self.mBuildableManufacturer, Recipe)
        self.SetActivatedRecipe(self.mHoveredRecipe)
        self.Widget_SlidingTabs.SetActiveIndex(1, True)
        self.UpdateIOSlots()
        # Label 287
        self.Widget_Window_DarkMode.SetInventoryVisibility(True, True)
        self.UpdateOutputSlotInfo(self.mActivatedRecipe)
    

    def OnStopHoveringManufacturingRecipe(self, Recipe: TSubclassOf[FGRecipe]):
        ReturnValue: bool = EqualEqual_ClassClass(Recipe, self.mHoveredRecipe)
        if not ReturnValue:
            goto('L63')
        self.mHoveredRecipe = None
    

    def OnManufacturingRecipeHovered(self, Recipe: TSubclassOf[FGRecipe]):
        self.mHoveredRecipe = Recipe
        self.CreateInfoBox(self.mHoveredRecipe)
        ReturnValue: Ptr[UMGSequencePlayer] = self.Widget_BuildMenu_InfoBox.PlayAnimation(self.Widget_BuildMenu_InfoBox.IconAnim, 0, 1, 0, 1)
        self.Widget_BuildMenu_InfoBox.AnimateCostSlots()
    

    def GetIsInfoButtonTabEnabled(self):
        ReturnValue: bool = Default__KismetSystemLibrary.IsValidClass(self.mActivatedRecipe)
        # Label 51
        ReturnValue_0: bool = ReturnValue
    

    def RemoveInputSlot(self):
        ExecutionFlow.Push("L465")
        # Label 5
        ExecutionFlow.Push("L279")
        # Label 10
        ReturnValue: Ptr[Widget] = self.mInputVBox.GetChildAt(0)
        IOSlot: Ptr[Widget_ManufacturingIOSlot] = Cast[Widget_ManufacturingIOSlot](ReturnValue)
        bSuccess: bool = IOSlot
        if not bSuccess:
           goto(ExecutionFlow.Pop())
        
        ReturnValue_0: bool = Default__KismetArrayLibrary.Array_RemoveItem(Ref[self.mIOSlots], Ref[IOSlot])
        OutputDelegate.BindUFunction(self, OnInventorySlotStackMove)
        IOSlot.Widget_InventorySlot.OnMoveStack.Remove(OutputDelegate)
        goto(ExecutionFlow.Pop())
        # Label 279
        ReturnValue_1: int32 = self.mInputVBox.GetChildrenCount()
        ReturnValue_2: int32 = ReturnValue_1 - 1
        ReturnValue_3: int32 = Min(ReturnValue_2, 0)
        ReturnValue_4: bool = self.mInputVBox.RemoveChildAt(ReturnValue_3)
        goto(ExecutionFlow.Pop())
    

    def AddInputSlot(self):
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_0: Ptr[Widget_ManufacturingIOSlot] = Default__WidgetBlueprintLibrary.Create(self, Widget_ManufacturingIOSlot, ReturnValue)
        Default__KismetSystemLibrary.SetObjectPropertyByName(ReturnValue_0, "mManufacturingWidget", self)
        ReturnValue_1: Ptr[VerticalBoxSlot] = self.mInputVBox.AddChildToVerticalBox(ReturnValue_0)
        
        ReturnValue_2: int32 = self.mIOSlots.append(ReturnValue_0)
        OutputDelegate.BindUFunction(self, OnInventorySlotStackMove)
        ReturnValue_0.Widget_CostSlotWrapper.Widget_InventorySlot.OnMoveStack.AddUnique(OutputDelegate)
    

    def UpdateIOSlots(self):
        ExecutionFlow.Push("L1643")
        # Label 5
        ReturnValue1: int32 = self.mInputVBox.GetChildrenCount()
        ReturnValue: List[ItemAmount] = Default__FGRecipe.GetIngredients(self.mActivatedRecipe)
        
        ReturnValue1_0: int32 = len(ReturnValue)
        ReturnValue_0: bool = ReturnValue1_0 != ReturnValue1
        if not ReturnValue_0:
            goto('L465')
        ExecutionFlow.Push("L5")
        ReturnValue1 = self.mInputVBox.GetChildrenCount()
        ReturnValue = Default__FGRecipe.GetIngredients(self.mActivatedRecipe)
        
        ReturnValue1_0 = len(ReturnValue)
        # Label 398
        ReturnValue_1: bool = ReturnValue1_0 > ReturnValue1
        # Label 436
        if not ReturnValue_1:
            goto('L1480')
        self.AddInputSlot()
        goto(ExecutionFlow.Pop())
        # Label 465
        Variable: int32 = 0
        # Label 488
        ReturnValue1 = self.mInputVBox.GetChildrenCount()
        ReturnValue_2: bool = Variable <= ReturnValue1
        if not ReturnValue_2:
            goto('L767')
        ExecutionFlow.Push("L1495")
        ReturnValue1_1: Ptr[Widget] = self.mInputVBox.GetChildAt(Variable)
        IOSlot1: Ptr[Widget_ManufacturingIOSlot] = Cast[Widget_ManufacturingIOSlot](ReturnValue1_1)
        bSuccess1: bool = IOSlot1
        if not bSuccess1:
           goto(ExecutionFlow.Pop())
        IOSlot1.Set CostSlot(Variable)
        goto(ExecutionFlow.Pop())
        
        self.Input_DropArea.mInventorySlots = None
        # Label 767
        Default__KismetArrayLibrary.Array_Clear(Ref[self.Input_DropArea.mInventorySlots])
        Variable_0: int32 = 0
        Variable_1: int32 = 0
        
        # Label 876
        ReturnValue_3: int32 = len(self.mIOSlots)
        ReturnValue_4: bool = Variable_0 <= ReturnValue_3
        if not ReturnValue_4:
            goto('L1213')
        Variable_1 = Variable_0
        ExecutionFlow.Push("L1569")
        
        Item = None
        Item = self.mIOSlots[Variable_1]
        
        self.Input_DropArea.mInventorySlots = None
        Item.Widget_CostSlotWrapper.Widget_InventorySlot = None
        # Label 1078
        ReturnValue_5: int32 = self.Input_DropArea.mInventorySlots.append(Item.Widget_CostSlotWrapper.Widget_InventorySlot)
        goto(ExecutionFlow.Pop())
        # Label 1213
        ReturnValue_6: int32 = self.mInputVBox.GetChildrenCount()
        ReturnValue_7: bool = EqualEqual_IntInt(ReturnValue_6, 4)
        if not ReturnValue_7:
           goto(ExecutionFlow.Pop())
        ReturnValue_8: Ptr[Widget] = self.mInputVBox.GetChildAt(3)
        IOSlot: Ptr[Widget_ManufacturingIOSlot] = Cast[Widget_ManufacturingIOSlot](ReturnValue_8)
        bSuccess: bool = IOSlot
        IOSlot.mDividerBottom.SetVisibility(1)
        goto(ExecutionFlow.Pop())
        # Label 1480
        self.RemoveInputSlot()
        goto(ExecutionFlow.Pop())
        # Label 1495
        ReturnValue_9: int32 = Variable + 1
        Variable = ReturnValue_9
        goto('L488')
        # Label 1569
        ReturnValue1_2: int32 = Variable_0 + 1
        Variable_0 = ReturnValue1_2
        goto('L876')
    

    def SetSelectedRecipe(self, Recipe: TSubclassOf[FGRecipe]):
        ReturnValue: bool = NotEqual_ClassClass(self.mHoveredRecipe, Recipe)
        if not ReturnValue:
            goto('L71')
        self.mHoveredRecipe = Recipe
    

    def InitRecipeList(self):
        ExecutionFlow.Push("L2156")
        # Label 5
        Variable: int32 = 0
        Variable2: int32 = 0
        # Label 51
        recipes: List[TSubclassOf[FGRecipe]] = []
        
        self.mBuildableManufacturer.GetAvailableRecipes(Ref[recipes])
        
        ReturnValue2: int32 = len(recipes)
        ReturnValue2_0: bool = Variable <= ReturnValue2
        if not ReturnValue2_0:
            goto('L390')
        Variable2 = Variable
        ExecutionFlow.Push("L2008")
        recipes = []
        
        self.mBuildableManufacturer.GetAvailableRecipes(Ref[recipes])
        
        Item2 = None
        Item2 = recipes[Variable2]
        
        self.AddUniqueRecipe(Item2, Ref[self.mCategorizedRecipes])
        goto(ExecutionFlow.Pop())
        # Label 390
        Variable1: int32 = 0
        Variable_0: int32 = 0
        
        # Label 436
        ReturnValue: int32 = len(self.mCategorizedRecipes)
        ReturnValue_0: bool = Variable1 <= ReturnValue
        if not ReturnValue_0:
           goto(ExecutionFlow.Pop())
        Variable_0 = Variable1
        ExecutionFlow.Push("L1934")
        Variable2_0: int32 = 0
        Variable1_0: int32 = 0
        
        Item = None
        # Label 621
        Item = self.mCategorizedRecipes[Variable_0]
        
        Item.Recipes_6_5C2C7BF54D78A483A81B2785C2CF7736 = None
        ReturnValue1: int32 = len(Item.Recipes_6_5C2C7BF54D78A483A81B2785C2CF7736)
        ReturnValue1_0: bool = Variable2_0 <= ReturnValue1
        if not ReturnValue1_0:
           goto(ExecutionFlow.Pop())
        Variable1_0 = Variable2_0
        ExecutionFlow.Push("L2082")
        ReturnValue_1: bool = EqualEqual_IntInt(Variable1_0, 0)
        if not ReturnValue_1:
            goto('L1366')
        # Label 876
        ReturnValue1_1: Ptr[PlayerController] = self.GetOwningPlayer()
        State: Ptr[FGPlayerState] = Cast[FGPlayerState](ReturnValue1_1.PlayerState)
        bSuccess: bool = State
        ReturnValue_2: List[TSubclassOf[FGItemCategory]] = State.GetCollapsedItemCategories()
        
        Item = None
        Item = self.mCategorizedRecipes[Variable_0]
        ReturnValue_3: FText = Default__FGItemCategory.GetCategoryName(Item.Category_5_48CE2A3C41089DC1E5DE39909CF17792)
        
        Item.Category_5_48CE2A3C41089DC1E5DE39909CF17792 = None
        ReturnValue_4: bool = Default__KismetArrayLibrary.Array_Contains(Ref[ReturnValue_2], Ref[Item.Category_5_48CE2A3C41089DC1E5DE39909CF17792])
        
        Widget = None
        # Label 1233
        self.CreateCategoryHeader(self.mVertBox, ReturnValue_3, ReturnValue_4, Ref[Widget])
        localCurrentCategory = Widget
        OutputDelegate.BindUFunction(self, OnCategoryClicked)
        localCurrentCategory.OnClicked.AddUnique(OutputDelegate)
        # Label 1366
        ReturnValue_5: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_6: Ptr[Widget_ManufacturingButton] = Default__WidgetBlueprintLibrary.Create(self, Widget_ManufacturingButton, ReturnValue_5)
        
        Item = None
        Item = self.mCategorizedRecipes[Variable_0]
        
        Item.Recipes_6_5C2C7BF54D78A483A81B2785C2CF7736 = None
        Item1 = None
        Item1 = Item.Recipes_6_5C2C7BF54D78A483A81B2785C2CF7736[Variable1_0]
        Default__KismetSystemLibrary.SetClassPropertyByName(ReturnValue_6, "mRecipeClass", Item1)
        Default__KismetSystemLibrary.SetObjectPropertyByName(ReturnValue_6, "mManufacturingWidget", self)
        localCurrentCategory.AddChildToContentWrapped(ReturnValue_6)
        OutputDelegate3.BindUFunction(self, OnManufacturingRecipeHovered)
        ReturnValue_6.OnManufacturingRecipeHovered.AddUnique(OutputDelegate3)
        OutputDelegate2.BindUFunction(self, OnManufacturingRecipeClicked)
        ReturnValue_6.OnManufacturingRecipeClicked.AddUnique(OutputDelegate2)
        OutputDelegate1.BindUFunction(self, OnStopHoveringManufacturingRecipe)
        ReturnValue_6.OnStopHoveringManufacturingRecipe.AddUnique(OutputDelegate1)
        goto(ExecutionFlow.Pop())
        # Label 1934
        ReturnValue1_2: int32 = Variable1 + 1
        Variable1 = ReturnValue1_2
        goto('L436')
        # Label 2008
        ReturnValue_7: int32 = Variable + 1
        Variable = ReturnValue_7
        goto('L51')
        # Label 2082
        ReturnValue2_1: int32 = Variable2_0 + 1
        Variable2_0 = ReturnValue2_1
        goto('L621')
    

    def BndEvt__Widget_StandbyButton_K2Node_ComponentBoundEvent_12_OnStandbyClicked__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_Manufacturing(437)
    

    def Tick(self):
        ExecuteUbergraph_Widget_Manufacturing.K2Node_Event_MyGeometry = MyGeometry #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_Manufacturing.K2Node_Event_InDeltaTime = InDeltaTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_Manufacturing(461)
    

    def OnNewRecipeSet(self, newRecipe: TSubclassOf[FGRecipe]):
        ExecuteUbergraph_Widget_Manufacturing.K2Node_CustomEvent_NewRecipe = newRecipe #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_Manufacturing(1621)
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_Manufacturing(1886)
    

    def Destruct(self):
        self.ExecuteUbergraph_Widget_Manufacturing(2005)
    

    def BndEvt__Widget_Window_DarkMode_K2Node_ComponentBoundEvent_0_OnClose__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_Manufacturing(2034)
    

    def BndEvt__Widget_Window_DarkMode_K2Node_ComponentBoundEvent_1_OnTabButtonClicked__DelegateSignature(self, ButtonIndex: int32):
        ExecuteUbergraph_Widget_Manufacturing.K2Node_ComponentBoundEvent_ButtonIndex = ButtonIndex #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_Manufacturing(2039)
    

    def OnReplicationDetailActorReplicated(self, replicationDetailActorOwner: Ptr[Actor]):
        ExecuteUbergraph_Widget_Manufacturing.K2Node_CustomEvent_replicationDetailActorOwner = replicationDetailActorOwner #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_Manufacturing(2191)
    

    def OnCategoryClicked(self, Instigator: Ptr[Widget_CraftBench_Category]):
        ExecuteUbergraph_Widget_Manufacturing.K2Node_CustomEvent_Instigator = Instigator #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_Manufacturing(2247)
    

    def OnModifierPressed(self, owningWidget: Ptr[FGInteractWidget]):
        ExecuteUbergraph_Widget_Manufacturing.K2Node_CustomEvent_owningWidget1 = owningWidget #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_Manufacturing(2576)
    

    def Init(self):
        self.ExecuteUbergraph_Widget_Manufacturing(2694)
    

    def OnModifierReleased(self, owningWidget: Ptr[FGInteractWidget]):
        ExecuteUbergraph_Widget_Manufacturing.K2Node_CustomEvent_owningWidget = owningWidget #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_Manufacturing(2699)
    

    def ExecuteUbergraph_Widget_Manufacturing(self):
        # Label 10
        self.OnEscapePressed()
        # End
        # Label 43
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        # Label 67
        Controller: Ptr[FGPlayerController] = Cast[FGPlayerController](ReturnValue)
        bSuccess: bool = Controller
        if not bSuccess:
            goto('L2699')
        # Label 146
        ReturnValue_0: bool = self.mBuildableManufacturer.IsProductionPaused()
        ReturnValue_1: bool = Not_PreBool(ReturnValue_0)
        ReturnValue_2: Ptr[BP_RemoteCallObject] = Controller.GetRemoteCallObjectOfClass(BP_RemoteCallObject)
        ReturnValue_2.Server_SetIsProductionPausedOnFactory(self.mBuildableManufacturer, ReturnValue_1)
        ReturnValue_0 = self.mBuildableManufacturer.IsProductionPaused()
        self.Widget_StandbyButton.SetStandbyButtonBrush(ReturnValue_0)
        self.GetManufacturingWarningVisibility(self.mBuildableManufacturer)
        # End
        goto('L43')
        # Label 442
        self.UpdateIOSlots()
        # End
        self.Tick(MyGeometry, InDeltaTime)
        self.UpdateProductivityPercentage()
        self.UpdateProductionStats()
        # End
        # Label 522
        self.mFactory = self.mBuildableManufacturer
        self.InitRecipeList()
        # Label 555
        OutputDelegate.BindUFunction(self, OnNewRecipeSet)
        self.mBuildableManufacturer.mCurrentRecipeChanged.AddUnique(OutputDelegate)
        ReturnValue_3: bool = self.mBuildableManufacturer.HasAuthority()
        if not ReturnValue_3:
            goto('L1467')
        # Label 675
        ReturnValue_4: TSubclassOf[FGRecipe] = self.mBuildableManufacturer.GetCurrentRecipe()
        ReturnValue_5: bool = Default__KismetSystemLibrary.IsValidClass(ReturnValue_4)
        if not ReturnValue_5:
            goto('L1536')
        ReturnValue_4 = self.mBuildableManufacturer.GetCurrentRecipe()
        self.SetActivatedRecipe(ReturnValue_4)
        self.Widget_SlidingTabs.SetActiveIndex(1, False)
        self.Widget_Window_DarkMode.SetInventoryVisibility(True, False)
        self.UpdateIOSlots()
        self.UpdateOutputSlotInfo(self.mActivatedRecipe)
        ReturnValue1: bool = self.mBuildableManufacturer.IsProductionPaused()
        self.Widget_StandbyButton.SetStandbyButtonBrush(ReturnValue1)
        self.GetManufacturingWarningVisibility(self.mBuildableManufacturer)
        OutputDelegate2.BindUFunction(self, OnInventorySlotStackMove)
        self.mOutput.OnMoveStack.AddUnique(OutputDelegate2)
        OutputDelegate2.BindUFunction(self, OnInventorySlotStackMove)
        self.Widget_Overclock.CostSlot_0.Widget_InventorySlot.OnMoveStack.AddUnique(OutputDelegate2)
        OutputDelegate2.BindUFunction(self, OnInventorySlotStackMove)
        self.Widget_Overclock.CostSlot_1.Widget_InventorySlot.OnMoveStack.AddUnique(OutputDelegate2)
        OutputDelegate2.BindUFunction(self, OnInventorySlotStackMove)
        self.Widget_Overclock.CostSlot_2.Widget_InventorySlot.OnMoveStack.AddUnique(OutputDelegate2)
        # End
        # Label 1467
        OutputDelegate1.BindUFunction(self, OnReplicationDetailActorReplicated)
        self.mBuildableManufacturer.OnReplicationDetailActorCreatedEvent.AddUnique(OutputDelegate1)
        goto('L675')
        # Label 1536
        self.Widget_SlidingTabs.SetActiveIndex(0, False)
        self.Widget_Window_DarkMode.SetInventoryVisibility(False, False)
        # End
        ReturnValue_6: bool = NotEqual_ClassClass(NewRecipe, self.mActivatedRecipe)
        if not ReturnValue_6:
            goto('L2699')
        self.SetActivatedRecipe(NewRecipe)
        goto('L442')
        # Label 1701
        self.Widget_Manufacturing_Warning.mManufacturer = self.mBuildableManufacturer
        self.Widget_Overclock.mBuildableFactory = self.mBuildableManufacturer
        OutputDelegate3.BindUFunction(self, OnModifierPressed)
        self.ModifierPressed.AddUnique(OutputDelegate3)
        OutputDelegate4.BindUFunction(self, OnModifierReleased)
        self.ModifierReleased.AddUnique(OutputDelegate4)
        self.GenerateOutputSlots()
        goto('L522')
        self.Construct()
        self.UpdateWindowText()
        
        self.Output_DropArea.mInventorySlots = None
        self.mOutput = None
        ReturnValue_7: int32 = self.Output_DropArea.mInventorySlots.append(self.mOutput)
        # End
        self.Destruct()
        self.RemoveInputSlot()
        # End
        goto('L10')
        Variable: bool = False
        Variable1: bool = True
        Variable_0: int32 = ButtonIndex
        
        switch = {
            0: Variable,
            1: Variable1
        }
        self.Widget_Window_DarkMode.SetInventoryVisibility(switch.get(Variable_0, None), True)
        # End
        self.ReconstructIOSlots()
        self.UpdateIOSlots()
        self.UpdateOutputSlotInfo(self.mActivatedRecipe)
        # End
        ReturnValue1_0: Ptr[PlayerController] = self.GetOwningPlayer()
        State: Ptr[FGPlayerState] = Cast[FGPlayerState](ReturnValue1_0.PlayerState)
        bSuccess1: bool = State
        if not bSuccess1:
            goto('L2699')
        ReturnValue_8: int32 = self.mVertBox.GetChildIndex(Instigator)
        
        Item = None
        Item = self.mCategorizedRecipes[ReturnValue_8]
        State.SetItemCategoryCollapsed(Item.Category_5_48CE2A3C41089DC1E5DE39909CF17792, Instigator.mIsCollapsed)
        # End
        # End
        # Label 2581
        self.Init()
        Manufacturer: Ptr[FGBuildableManufacturer] = Cast[FGBuildableManufacturer](self.mInteractObject)
        bSuccess2: bool = Manufacturer
        if not bSuccess2:
            goto('L2699')
        self.mBuildableManufacturer = Manufacturer
        goto('L1701')
        goto('L2581')
    
