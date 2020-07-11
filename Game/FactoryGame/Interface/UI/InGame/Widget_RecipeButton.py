
from codegen.ue4_stub import *

from Script.Engine import Texture2D
from Game.FactoryGame.Interface.UI.InGame.Widget_RecipeButton import ExecuteUbergraph_Widget_RecipeButton.K2Node_Event_MouseEvent
from Script.InputCore import Key
from Game.FactoryGame.Interface.UI.InGame.Widget_RecipeButton import Widget_RecipeButton
from Script.FactoryGame import GetProducts
from Script.Engine import Default__KismetSystemLibrary
from Script.UMG import GetChildAt
from Script.UMG import Handled
from Script.Engine import FormatArgumentData
from Script.UMG import ESlateVisibility
from Script.UMG import IsOpen
from Script.Engine import IsValid
from Script.FactoryGame import GetIngredients
from Script.UMG import SetColorAndOpacity
from Script.Engine import EqualEqual_IntInt
from Script.Engine import Default__KismetTextLibrary
from Script.FactoryGame import GetSmallIcon
from Script.UMG import Construct
from Script.FactoryGame import GetNumItemsFromCentralStorage
from Script.UMG import PanelWidget
from Script.FactoryGame import FGButtonWidget
from Game.FactoryGame.Interface.UI.HUDHelpers.HUDHelpers import Default__HUDHelpers
from Script.UMG import Create
from Script.Engine import GetGameState
from Script.SlateCore import SlateBrush
from Script.SlateCore import SlateColor
from Script.CoreUObject import LinearColor
from Game.FactoryGame.Interface.UI.InGame.BuildMenu.Prototype.Widget_BuildMenu_RightClickMenu import Widget_BuildMenu_RightClickMenu
from Script.Engine import EqualEqual_ClassClass
from Script.Engine import SetClassPropertyByName
from Script.Engine import Pawn
from Script.Engine import GreaterEqual_IntInt
from Script.UMG import GetChildrenCount
from Game.FactoryGame.Interface.UI.Audio.WorkBench.Play_UI_WorkBench_MouseOver import Play_UI_WorkBench_MouseOver
from Game.FactoryGame.Interface.UI.InGame.Widget_RecipeButton import ExecuteUbergraph_Widget_RecipeButton.K2Node_Event_MyGeometry
from Script.Engine import SetStructurePropertyByName
from Script.Engine import Default__KismetArrayLibrary
from Script.Engine import GameStateBase
from Script.FactoryGame import FGInventoryComponent
from Script.FactoryGame import IsValidResearchRecipeReward
from Script.FactoryGame import Default__FGRecipeManager
from Script.FactoryGame import Default__FGRecipe
from Script.AkAudio import Default__AkGameplayStatics
from Script.FactoryGame import IsRecipeAvailable
from Script.UMG import Close
from Script.FactoryGame import Default__FGItemDescriptor
from Script.FactoryGame import FGRecipe
from Script.FactoryGame import ItemAmount
from Script.FactoryGame import ResearchRecipeReward
from Script.AkAudio import AkComponent
from Script.FactoryGame import Default__FGCentralStorageSubsystem
from Script.UMG import EventReply
from Script.UMG import GetParent
from Script.AkAudio import PostAkEvent
from Script.FactoryGame import SetButton
from Game.FactoryGame.Interface.UI.Audio.WorkBench.Play_UI_WorkBench_Select import Play_UI_WorkBench_Select
from Script.UMG import ToggleOpen
from Script.FactoryGame import Get
from Script.Engine import PlayerController
from Script.FactoryGame import FGResearchRecipe
from Script.UMG import Unhandled
from Script.Engine import PointerEvent_IsMouseButtonDown
from Game.FactoryGame.Interface.UI.InGame.Widget_RecipeButton import ExecuteUbergraph_Widget_RecipeButton.K2Node_ComponentBoundEvent_Index
from Script.UMG import Default__WidgetBlueprintLibrary
from Game.FactoryGame.Interface.UI.InGame.Widget_RecipeButton import ExecuteUbergraph_Widget_RecipeButton.K2Node_ComponentBoundEvent_ListButton
from Script.Engine import Default__GameplayStatics
from Script.Engine import Format
from Game.FactoryGame.Interface.UI.InGame.Widget_RecipeButton import ExecuteUbergraph_Widget_RecipeButton
from Script.FactoryGame import GetRecipeName
from Script.FactoryGame import FGCentralStorageSubsystem
from Script.Engine import Default__KismetInputLibrary
from Game.FactoryGame.Buildable.-Shared.WorkBench.Widget_ManualManufacturing import Widget_ManualManufacturing
from Script.Engine import Not_PreBool
from Game.FactoryGame.Interface.UI.InGame.Widget_Tooltip import Widget_Tooltip
from Script.Engine import Divide_IntInt
from Script.Engine import BooleanOR
from Script.UMG import Tick
from Script.UMG import Widget
from Script.FactoryGame import Default__FGResearchRecipe
from Script.UMG import GetOwningPlayerPawn
from Game.FactoryGame.Interface.UI.InGame.Widget_RecipeButton import ExecuteUbergraph_Widget_RecipeButton.K2Node_Event_InDeltaTime
from Script.Engine import Min
from Script.FactoryGame import FGRecipeManager
from Script.FactoryGame import GetResearcResults

class Widget_RecipeButton(FGButtonWidget):
    mRecipeClass: TSubclassOf[FGRecipe]
    Workbench: Ptr[Widget_ManualManufacturing]
    mCachedInventory: Ptr[FGInventoryComponent]
    NewVar_0: Ptr[FGInventoryComponent]
    isAffordable: bool
    mItemAmount: ItemAmount
    UpdateWindowWidgetOffset: FMulticastScriptDelegate
    OnRecipeButtonClicked: FMulticastScriptDelegate
    mHideIfUnaffordable: bool
    bIsFocusable = True
    
    def ClearButtonSelection(self):
        ExecutionFlow.Push("L436")
        Variable: int32 = 0
        # Label 28
        ReturnValue1: Ptr[PanelWidget] = self.GetParent()
        ReturnValue: int32 = ReturnValue1.GetChildrenCount()
        ReturnValue_0: bool = Variable <= ReturnValue
        if not ReturnValue_0:
            goto('L357')
        ExecutionFlow.Push("L362")
        ReturnValue_1: Ptr[PanelWidget] = self.GetParent()
        ReturnValue_2: Ptr[Widget] = ReturnValue_1.GetChildAt(Variable)
        Button: Ptr[Widget_RecipeButton] = Cast[Widget_RecipeButton](ReturnValue_2)
        bSuccess: bool = Button
        if not bSuccess:
           goto(ExecutionFlow.Pop())
        Button.Widget_ListButton.mIsSelected = False
        goto(ExecutionFlow.Pop())
        # Label 357
        # End
        # Label 362
        ReturnValue_3: int32 = Variable + 1
        Variable = ReturnValue_3
        goto('L28')
    

    def GetCustomTooltip(self):
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_0: Ptr[Widget_Tooltip] = Default__WidgetBlueprintLibrary.Create(self, Widget_Tooltip, ReturnValue)
        ReturnValue_1: List[ItemAmount] = Default__FGRecipe.GetProducts(self.mRecipeClass, False)
        
        Item = None
        Item = ReturnValue_1[0]
        
        Item = None
        Default__KismetSystemLibrary.SetStructurePropertyByName(ReturnValue_0, "mItemDescriptor", Ref[Item])
        ReturnValue_2: Ptr[Widget] = ReturnValue_0
    

    def GetRightClickMenuVisibility(self):
        ReturnValue: bool = self.mRightClickMenu.IsOpen()
        if not ReturnValue:
            goto('L81')
        ReturnValue_0: uint8 = 0
        goto('L101')
        # Label 81
        ReturnValue_0 = 3
    

    def CreateRightClickMenu(self):
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_0: Ptr[Widget_BuildMenu_RightClickMenu] = Default__WidgetBlueprintLibrary.Create(self, Widget_BuildMenu_RightClickMenu, ReturnValue)
        Default__KismetSystemLibrary.SetClassPropertyByName(ReturnValue_0, "mRecipe", self.mRecipeClass)
        OutputDelegate.BindUFunction(self, UpdateWindowWidgetOffset_Event)
        ReturnValue_0.UpdateWindowWidgetOffset.AddUnique(OutputDelegate)
        ReturnValue_1: Ptr[Widget] = ReturnValue_0
    

    def GetButtonHoverColor(self):
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(self.Workbench)
        if not ReturnValue:
            goto('L433')
        ReturnValue_0: bool = self.IsHovered()
        if not ReturnValue_0:
            goto('L190')
        
        Text = None
        Graphics = None
        Default__HUDHelpers.GetFactoryGameDarkGray(self, Ref[Text], Ref[Graphics])
        ReturnValue_1: LinearColor = Graphics
        goto('L433')
        # Label 190
        ReturnValue_2: bool = EqualEqual_ClassClass(self.Workbench.mCurrentRecipe, self.mRecipeClass)
        if not ReturnValue_2:
            goto('L351')
        
        Orange = None
        OrangeText = None
        Default__HUDHelpers.GetFactoryGameOrange(self, Ref[Orange], Ref[OrangeText])
        ReturnValue_1 = Orange
        goto('L433')
        
        TextWhite = None
        GraphicsWhite = None
        # Label 351
        Default__HUDHelpers.GetFactoryGameWhite(self, Ref[TextWhite], Ref[GraphicsWhite])
        ReturnValue_1 = GraphicsWhite
    

    def GetTextHoverColor(self):
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(self.Workbench)
        if not ReturnValue:
            goto('L370')
        ReturnValue_0: bool = EqualEqual_ClassClass(self.Workbench.mCurrentRecipe, self.mRecipeClass)
        ReturnValue_1: bool = self.IsHovered()
        ReturnValue_2: bool = BooleanOR(ReturnValue_1, ReturnValue_0)
        if not ReturnValue_2:
            goto('L288')
        
        TextWhite = None
        GraphicsWhite = None
        Default__HUDHelpers.GetFactoryGameWhite(self, Ref[TextWhite], Ref[GraphicsWhite])
        ReturnValue_3: SlateColor = TextWhite
        goto('L370')
        
        Text = None
        Graphics = None
        # Label 288
        Default__HUDHelpers.GetFactoryGameDarkGray(self, Ref[Text], Ref[Graphics])
        ReturnValue_3 = Text
    

    def IsButtonEnabled(self):
        Recipe: TSubclassOf[FGResearchRecipe] = ClassCast[FGResearchRecipe](self.mRecipeClass)
        bSuccess: bool = Recipe
        if not bSuccess:
            goto('L476')
        ReturnValue: ResearchRecipeReward = Default__FGResearchRecipe.GetResearcResults(Recipe)
        ReturnValue_0: bool = Default__FGResearchRecipe.IsValidResearchRecipeReward(ReturnValue)
        if not ReturnValue_0:
            goto('L465')
        ReturnValue_1: Ptr[GameStateBase] = Default__GameplayStatics.GetGameState(self)
        ReturnValue_2: Ptr[FGRecipeManager] = Default__FGRecipeManager.Get(ReturnValue_1)
        
        ReturnValue.ResearchRecipes = None
        Item = None
        Item = ReturnValue.ResearchRecipes[0]
        ReturnValue_3: bool = ReturnValue_2.IsRecipeAvailable(Item)
        ReturnValue_4: bool = Not_PreBool(ReturnValue_3)
        ReturnValue_5: bool = ReturnValue_4
        goto('L476')
        # Label 465
        ReturnValue_5 = True
    

    def GetNumCanProduce(self):
        ExecutionFlow.Push("L1706")
        minRecipesThatCanBeProduced = 999999
        # Label 28
        Variable: int32 = 0
        Variable_0: int32 = 0
        # Label 74
        ReturnValue: List[ItemAmount] = Default__FGRecipe.GetIngredients(self.mRecipeClass)
        
        ReturnValue1: int32 = len(ReturnValue)
        ReturnValue_0: bool = Variable <= ReturnValue1
        if not ReturnValue_0:
            goto('L1235')
        Variable_0 = Variable
        ExecutionFlow.Push("L1632")
        ReturnValue_1: Ptr[Pawn] = self.GetOwningPlayerPawn()
        ReturnValue = Default__FGRecipe.GetIngredients(self.mRecipeClass)
        
        Item1 = None
        Item1 = ReturnValue[Variable_0]
        
        numItems = None
        Default__HUDHelpers.GetNumItemsFromPlayerInventory(ReturnValue_1, Item1.ItemClass, self, Ref[numItems])
        NumItems = numItems
        ReturnValue_2: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_3: Ptr[FGCentralStorageSubsystem] = Default__FGCentralStorageSubsystem.Get(ReturnValue_2)
        ReturnValue_4: bool = Default__KismetSystemLibrary.IsValid(ReturnValue_3)
        if not ReturnValue_4:
            goto('L988')
        ReturnValue_2 = self.GetOwningPlayer()
        ReturnValue_3 = Default__FGCentralStorageSubsystem.Get(ReturnValue_2)
        ReturnValue = Default__FGRecipe.GetIngredients(self.mRecipeClass)
        
        Item1 = None
        Item1 = ReturnValue[Variable_0]
        ReturnValue_5: int32 = ReturnValue_3.GetNumItemsFromCentralStorage(Item1.ItemClass)
        ReturnValue1_0: int32 = ReturnValue_5 + NumItems
        NumItems = ReturnValue1_0
        # Label 988
        ReturnValue = Default__FGRecipe.GetIngredients(self.mRecipeClass)
        
        Item1 = None
        Item1 = ReturnValue[Variable_0]
        ReturnValue_6: int32 = Divide_IntInt(NumItems, Item1.amount)
        ReturnValue_7: int32 = Min(ReturnValue_6, minRecipesThatCanBeProduced)
        minRecipesThatCanBeProduced = ReturnValue_7
        goto(ExecutionFlow.Pop())
        # Label 1235
        ReturnValue_8: List[ItemAmount] = Default__FGRecipe.GetProducts(self.mRecipeClass, False)
        
        ReturnValue_9: int32 = len(ReturnValue_8)
        ReturnValue_10: bool = ReturnValue_9 > 0
        if not ReturnValue_10:
            goto('L1604')
        ReturnValue1_1: List[ItemAmount] = Default__FGRecipe.GetProducts(self.mRecipeClass, False)
        
        Item = None
        Item = ReturnValue1_1[0]
        ReturnValue_11: int32 = Item.amount * minRecipesThatCanBeProduced
        Result = ReturnValue_11
        # End
        # Label 1604
        Result = 0
        # End
        # Label 1632
        ReturnValue_12: int32 = Variable + 1
        Variable = ReturnValue_12
        goto('L74')
    

    def GetNumCanProduceVisibility(self):
        Variable: uint8 = 2
        Variable1: uint8 = 0
        
        Result = None
        self.GetNumCanProduce(Ref[Result])
        ReturnValue: bool = EqualEqual_IntInt(Result, 0)
        Variable_0: bool = ReturnValue
        
        switch = {
            False: Variable1,
            True: Variable
        }
        ReturnValue_0: uint8 = switch.get(Variable_0, None)
    

    def GetNumCanProduceText(self):
        minRecipesThatCanBeProduced = 0
        
        Result = None
        self.GetNumCanProduce(Ref[Result])
        FormatArgumentData.ArgumentName = "0"
        FormatArgumentData.ArgumentValueType = 0
        FormatArgumentData.ArgumentValue = 
        FormatArgumentData.ArgumentValueInt = Result
        FormatArgumentData.ArgumentValueFloat = 0
        FormatArgumentData.ArgumentValueGender = 0
        Array: List[FormatArgumentData] = [FormatArgumentData]
        ReturnValue: FText = Default__KismetTextLibrary.Format("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 302, 'Value': '[ {0} ] '}", Array)
        ReturnValue_0: FText = ReturnValue
    

    def CheckIngredients(self):
        ExecutionFlow.Push("L732")
        Variable: bool = False
        Variable_0: int32 = 0
        Variable_1: int32 = 0
        # Label 62
        ReturnValue: bool = Not_PreBool(Variable)
        ReturnValue_0: List[ItemAmount] = Default__FGRecipe.GetIngredients(self.mRecipeClass)
        
        ReturnValue_1: int32 = len(ReturnValue_0)
        ReturnValue_2: bool = Variable_0 <= ReturnValue_1
        ReturnValue_3: bool = ReturnValue and ReturnValue_2
        if not ReturnValue_3:
           goto(ExecutionFlow.Pop())
        Variable_1 = Variable_0
        ExecutionFlow.Push("L646")
        ReturnValue_0 = Default__FGRecipe.GetIngredients(self.mRecipeClass)
        
        Item = None
        Item = ReturnValue_0[Variable_1]
        self.mItemAmount = Item
        ReturnValue_4: Ptr[Pawn] = self.GetOwningPlayerPawn()
        
        numItems = None
        Default__HUDHelpers.GetNumItemsFromPlayerInventory(ReturnValue_4, self.mItemAmount.ItemClass, self, Ref[numItems])
        ReturnValue_5: bool = GreaterEqual_IntInt(numItems, self.mItemAmount.amount)
        self.isAffordable = ReturnValue_5
        if not self.isAffordable:
            goto('L720')
        goto(ExecutionFlow.Pop())
        # Label 646
        ReturnValue_6: int32 = Variable_0 + 1
        Variable_0 = ReturnValue_6
        goto('L62')
        # Label 720
        Variable = True
        goto(ExecutionFlow.Pop())
    

    def GetRecipeIcon(self):
        ReturnValue: List[ItemAmount] = Default__FGRecipe.GetProducts(self.mRecipeClass, True)
        
        Item = None
        Item = ReturnValue[0]
        ReturnValue_0: Ptr[Texture2D] = Default__FGItemDescriptor.GetSmallIcon(Item.ItemClass)
        SlateBrush.ImageSize = self.Widget_ListButton.mItemImageBrush.Brush.ImageSize
        SlateBrush.Margin = self.Widget_ListButton.mItemImageBrush.Brush.Margin
        SlateBrush.TintColor = self.Widget_ListButton.mItemImageBrush.Brush.TintColor
        SlateBrush.ResourceObject = ReturnValue_0
        SlateBrush.DrawAs = self.Widget_ListButton.mItemImageBrush.Brush.DrawAs
        SlateBrush.Tiling = self.Widget_ListButton.mItemImageBrush.Brush.Tiling
        SlateBrush.Mirroring = self.Widget_ListButton.mItemImageBrush.Brush.Mirroring
        ReturnValue_1: SlateBrush = SlateBrush
    

    def GetIconColor(self):
        if not self.isAffordable:
            goto('L71')
        ReturnValue = LinearColor(R = 1, G = 1, B = 1, A = 1)
        goto('L123')
        # Label 71
        ReturnValue = LinearColor(R = 0.09530699998140335, G = 0.09530699998140335, B = 0.09530699998140335, A = 0.5)
    

    def OnMouseButtonDown(self):
        localMouseEvent = MouseEvent
        
        ReturnValue: bool = Default__KismetInputLibrary.PointerEvent_IsMouseButtonDown(Key(KeyName = "RightMouseButton"), Ref[localMouseEvent])
        if not ReturnValue:
            goto('L234')
        # Label 119
        self.mRightClickMenu.ToggleOpen(False)
        ReturnValue_0: EventReply = Default__WidgetBlueprintLibrary.Handled()
        ReturnValue_1: EventReply = ReturnValue_0
        goto('L422')
        # Label 234
        ReturnValue_2: bool = EqualEqual_ClassClass(self.Workbench.mCurrentRecipe, self.mRecipeClass)
        if not ReturnValue_2:
            goto('L313')
        goto('L119')
        # Label 313
        self.mRightClickMenu.Close()
        ReturnValue_3: EventReply = Default__WidgetBlueprintLibrary.Unhandled()
        ReturnValue_1 = ReturnValue_3
    

    def GetRecipeDisplayName(self):
        ReturnValue: FText = Default__FGRecipe.GetRecipeName(self.mRecipeClass)
        ReturnValue_0: FText = ReturnValue
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_RecipeButton(53)
    

    def Tick(self):
        ExecuteUbergraph_Widget_RecipeButton.K2Node_Event_MyGeometry = MyGeometry #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_RecipeButton.K2Node_Event_InDeltaTime = InDeltaTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_RecipeButton(367)
    

    def OnClicked(self):
        self.ExecuteUbergraph_Widget_RecipeButton(1423)
    

    def OnHovered(self):
        self.ExecuteUbergraph_Widget_RecipeButton(1475)
    

    def OnPressed(self):
        self.ExecuteUbergraph_Widget_RecipeButton(1480)
    

    def OnMouseLeave(self):
        ExecuteUbergraph_Widget_RecipeButton.K2Node_Event_MouseEvent = MouseEvent #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_RecipeButton(1485)
    

    def UpdateWindowWidgetOffset_Event(self):
        self.ExecuteUbergraph_Widget_RecipeButton(1522)
    

    def BndEvt__Widget_ListButton_K2Node_ComponentBoundEvent_0_OnClicked__DelegateSignature(self, index: int32, ListButton: Ptr[Widget_ListButton]):
        ExecuteUbergraph_Widget_RecipeButton.K2Node_ComponentBoundEvent_Index = index #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_RecipeButton.K2Node_ComponentBoundEvent_ListButton = ListButton #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_RecipeButton(1672)
    

    def ExecuteUbergraph_Widget_RecipeButton(self):
        # Label 10
        self.mContent.SetVisibility(0)
        # End
        self.Construct()
        self.SetButton(self.Widget_ListButton.mRecipeButton)
        OutputDelegate.BindUFunction(self, OnClicked)
        self.Widget_ListButton.mRecipeButton.OnClicked.AddUnique(OutputDelegate)
        # Label 190
        OutputDelegate1.BindUFunction(self, OnHovered)
        self.Widget_ListButton.mRecipeButton.OnHovered.AddUnique(OutputDelegate1)
        OutputDelegate2.BindUFunction(self, OnPressed)
        self.Widget_ListButton.mRecipeButton.OnPressed.AddUnique(OutputDelegate2)
        # Label 362
        # End
        self.Tick(MyGeometry, InDeltaTime)
        self.CheckIngredients()
        ReturnValue: FText = self.GetNumCanProduceText()
        ReturnValue_0: FText = Default__FGRecipe.GetRecipeName(self.mRecipeClass)
        ReturnValue_1: List[ItemAmount] = Default__FGRecipe.GetProducts(self.mRecipeClass, True)
        ReturnValue_2: uint8 = self.GetNumCanProduceVisibility()
        
        Item = None
        Item = ReturnValue_1[0]
        ReturnValue_3: Ptr[Texture2D] = Default__FGItemDescriptor.GetSmallIcon(Item.ItemClass)
        self.Widget_ListButton.UpdateButton(ReturnValue_3, ReturnValue_0, ReturnValue, ReturnValue_2, 0, )
        if not self.isAffordable:
            goto('L890')
        self.Widget_ListButton.mItemImageBrush.SetColorAndOpacity(LinearColor(R = 1, G = 1, B = 1, A = 1))
        goto('L10')
        # Label 890
        self.Widget_ListButton.mItemImageBrush.SetColorAndOpacity(LinearColor(R = 1, G = 1, B = 1, A = 0.3499999940395355))
        Variable: uint8 = 1
        Variable1: uint8 = 0
        Variable_0: bool = self.mHideIfUnaffordable
        
        switch = {
            False: Variable1,
            True: Variable
        }
        self.mContent.SetVisibility(switch.get(Variable_0, None))
        # End
        # Label 1131
        self.Workbench.SetSelectedRecipe(self.mRecipeClass)
        # End
        # Label 1181
        ReturnValue_4: bool = Default__KismetSystemLibrary.IsValid(self.Workbench)
        if not ReturnValue_4:
            goto('L1692')
        goto('L1131')
        # Label 1251
        ReturnValue_5: Ptr[Pawn] = self.GetOwningPlayerPawn()
        ReturnValue_6: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_UI_WorkBench_MouseOver, ReturnValue_5, True)
        # End
        # Label 1337
        ReturnValue1: Ptr[Pawn] = self.GetOwningPlayerPawn()
        ReturnValue1_0: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_UI_WorkBench_Select, ReturnValue1, True)
        # End
        self.ClearButtonSelection()
        self.Widget_ListButton.mIsSelected = True
        goto('L1181')
        goto('L1251')
        goto('L1337')
        self.mRightClickMenu.Close()
        # End
        ReturnValue1_1: bool = Default__KismetSystemLibrary.IsValid(self.Workbench.Manufacturing_Container)
        if not ReturnValue1_1:
            goto('L1692')
        self.Workbench.Manufacturing_Container.SetWindowAlignment()
        # End
        self.OnRecipeButtonClicked.ProcessMulticastDelegate(self)
    

    def OnRecipeButtonClicked__DelegateSignature(self, ClickedButton: Ptr[Widget_RecipeButton]):
        pass
    

    def UpdateWindowWidgetOffset__DelegateSignature(self):
        pass
    
