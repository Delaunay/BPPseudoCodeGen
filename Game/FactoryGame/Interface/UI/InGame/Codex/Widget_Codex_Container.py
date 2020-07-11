
from codegen.ue4_stub import *

from Script.FactoryGame import FGEquipmentDescriptor
from Script.Engine import Texture2D
from Script.UMG import AddChild
from Script.UMG import VerticalBox
from Game.FactoryGame.Interface.UI.InGame.Codex.Widget_Codex_Container import ExecuteUbergraph_Widget_Codex_Container.K2Node_ComponentBoundEvent_ListButton
from Script.Engine import Default__KismetSystemLibrary
from Script.FactoryGame import GetProducts
from Script.UMG import GetChildAt
from Script.Engine import FormatArgumentData
from Game.FactoryGame.Interface.UI.InGame.Codex.Widget_Codex_Container import ExecuteUbergraph_Widget_Codex_Container.K2Node_CustomEvent_ListButton
from Script.UMG import ESlateVisibility
from Script.Engine import Array_Append
from Script.Engine import IsValid
from Script.Engine import Conv_IntToText
from Game.FactoryGame.Interface.UI.InGame.Codex.Widget_Codex_Container import ExecuteUbergraph_Widget_Codex_Container.K2Node_ComponentBoundEvent_Index2
from Script.FactoryGame import FGMessageBase
from Script.Engine import Default__KismetTextLibrary
from Script.FactoryGame import GetSmallIcon
from Script.Engine import Conv_StringToText
from Script.UMG import Construct
from Script.FactoryGame import GetAllAvailableRecipes
from Script.Engine import Default__KismetStringLibrary
from Game.FactoryGame.Interface.UI.HUDHelpers.HUDHelpers import Default__HUDHelpers
from Script.UMG import Create
from Script.Engine import GetGameState
from Game.FactoryGame.Interface.UI.InGame.Codex.Widget_Codex_Container import ExecuteUbergraph_Widget_Codex_Container.K2Node_ComponentBoundEvent_Index1
from Game.FactoryGame.Interface.UI.InGame.Codex.Widget_Codex_Container import ExecuteUbergraph_Widget_Codex_Container
from Game.FactoryGame.Interface.UI.InGame.Codex.Widget_Codex_Container import ExecuteUbergraph_Widget_Codex_Container.K2Node_CustomEvent_ListButton1
from Game.FactoryGame.Interface.UI.BPI_GameUI import BPI_GameUI
from Script.Engine import Array_Clear
from Game.FactoryGame.Interface.UI.InGame.Codex.Widget_Codex_Container import ExecuteUbergraph_Widget_Codex_Container.K2Node_ComponentBoundEvent_Text
from Script.FactoryGame import FGResourceDescriptor
from Script.Engine import EqualEqual_ClassClass
from Script.Engine import SetClassPropertyByName
from Script.Engine import EqualEqual_ByteByte
from Script.Engine import SetObjectPropertyByName
from Game.FactoryGame.Interface.UI.InGame.Codex.Widget_Codex_Container import ExecuteUbergraph_Widget_Codex_Container.K2Node_ComponentBoundEvent_ListButton3
from Script.Engine import GreaterEqual_IntInt
from Script.Engine import Max
from Script.Engine import Default__KismetArrayLibrary
from Script.Engine import GameStateBase
from Script.FactoryGame import FindRecipesByIngredient
from Game.FactoryGame.Interface.UI.InGame.Codex.Widget_Codex_Container import ExecuteUbergraph_Widget_Codex_Container.K2Node_ComponentBoundEvent_Index3
from Script.FactoryGame import SetDefaultFocusWidget
from Script.FactoryGame import FGVehicleDescriptor
from Script.FactoryGame import FGInteractWidget
from Script.FactoryGame import Default__FGRecipeManager
from Script.FactoryGame import Default__FGRecipe
from Script.Engine import Conv_IntToString
from Script.FactoryGame import FindRecipesByProduct
from Game.FactoryGame.Interface.UI.InGame.Codex.Widget_Codex_Container import ExecuteUbergraph_Widget_Codex_Container.K2Node_ComponentBoundEvent_ListButton2
from Game.FactoryGame.Interface.UI.HUDHelpers.BPHUDHelpers import Default__BPHUDHelpers
from Script.FactoryGame import Default__FGItemDescriptor
from Script.FactoryGame import FGRecipe
from Script.FactoryGame import ItemAmount
from Game.FactoryGame.Interface.UI.InGame.Codex.Widget_Codex_Container import ExecuteUbergraph_Widget_Codex_Container.K2Node_CustomEvent_Index
from Script.FactoryGame import MessageData
from Script.FactoryGame import FGBuildingDescriptor
from Script.UMG import SetUserFocus
from Script.Engine import SetTextPropertyByName
from Script.FactoryGame import EMessageType
from Script.Engine import GetEmptyText
from Game.FactoryGame.Interface.UI.InGame.Widget_MessageNotifier import Widget_MessageNotifier
from Script.Engine import Delay
from Game.FactoryGame.Interface.UI.InGame.Codex.Widget_Codex_Container import ExecuteUbergraph_Widget_Codex_Container.K2Node_ComponentBoundEvent_ButtonIndex
from Script.FactoryGame import FGPlayerState
from Script.UMG import PanelSlot
from Script.Engine import LatentActionInfo
from Script.FactoryGame import Get
from Script.Engine import PlayerController
from Script.UMG import Default__WidgetBlueprintLibrary
from Game.FactoryGame.Interface.UI.InGame.Codex.Widget_Codex_MessageButton import Widget_Codex_MessageButton
from Script.Engine import SetBoolPropertyByName
from Script.Engine import Default__GameplayStatics
from Game.FactoryGame.Interface.UI.InGame.-Shared.Widget_ListButton import Widget_ListButton
from Script.Engine import Format
from Game.FactoryGame.Interface.UI.InGame.Codex.BPW_Interactable_Recipe import BPW_Interactable_Recipe
from Game.FactoryGame.Interface.UI.InGame.Codex.Widget_CodexButton import Widget_CodexButton
from Script.UMG import HasAnyChildren
from Script.FactoryGame import GetAllMessages
from Script.FactoryGame import FGItemDescriptor
from Game.FactoryGame.Interface.UI.InGame.-Shared.Widget_SlidingTabs_Button import Widget_SlidingTabs_Button
from Script.Engine import Conv_TextToString
from Script.Engine import Not_PreBool
from Script.FactoryGame import GetItemName
from Script.FactoryGame import GetBigIcon
from Script.FactoryGame import GetAllMessageData
from Game.FactoryGame.Interface.UI.InGame.Codex.Widget_Codex_Container import ExecuteUbergraph_Widget_Codex_Container.K2Node_CustomEvent_Index1
from Script.Engine import BooleanOR
from Script.UMG import Widget
from Script.Engine import Array_AddUnique
from Game.FactoryGame.Interface.UI.InGame.Codex.Widget_Codex_Container import ExecuteUbergraph_Widget_Codex_Container.K2Node_ComponentBoundEvent_Index
from Game.FactoryGame.Interface.UI.InGame.Codex.Widget_Codex_Container import ExecuteUbergraph_Widget_Codex_Container.K2Node_ComponentBoundEvent_ListButton1
from Script.FactoryGame import GetItemDescription
from Script.FactoryGame import ReadMessage
from Script.Engine import EqualEqual_TextText
from Script.FactoryGame import FGRecipeManager
from Script.Engine import IsValidClass
from Script.Engine import Concat_StrStr

class Widget_Codex_Container(FGInteractWidget):
    mMessageIsClicked: bool
    mButtons: List[Ptr[Widget_Codex_MessageButton]]
    mSelectedMessage: TSubclassOf[FGMessageBase]
    mActiveButton: Ptr[Widget_CodexButton]
    mCurrentTab: uint8
    mParts: List[TSubclassOf[FGItemDescriptor]]
    mSearchResults: List[TSubclassOf[FGItemDescriptor]]
    mShowRecipeIngredientList: bool
    mEquipment: List[TSubclassOf[FGItemDescriptor]]
    mBuildings: List[TSubclassOf[FGItemDescriptor]]
    mCurrentList: List[TSubclassOf[FGItemDescriptor]]
    mVehicles: List[TSubclassOf[FGItemDescriptor]]
    mOpenOnRecipe: TSubclassOf[FGItemDescriptor]
    mUseMouse = True
    mCaptureInput = True
    mRestoreFocusWhenLost = True
    mInputToPassThrough = ['OpenCodex']
    mDesiredHorizontalAlignment = 2
    mDesiredVerticalAlignment = 2
    mUseGamepadCursor = True
    mCallCustomTickOnConstruct = True
    
    def PopulateSearchResults(self, InText: FText):
        ExecutionFlow.Push("L1897")
        LocalSearchText = InText
        
        Default__KismetArrayLibrary.Array_Clear(Ref[self.mSearchResults])
        self.mItemSearchList.ClearChildren()
        Variable2: uint8 = 1
        Variable3: uint8 = 0
        ReturnValue1: FText = Default__KismetTextLibrary.GetEmptyText()
        
        ReturnValue1_0: bool = Default__KismetTextLibrary.EqualEqual_TextText(Ref[LocalSearchText], Ref[ReturnValue1])
        Variable1: bool = ReturnValue1_0
        
        switch = {
            False: Variable3,
            True: Variable2
        }
        self.mSearchContainer.SetVisibility(switch.get(Variable1, None))
        Variable: uint8 = 0
        Variable1_0: uint8 = 2
        ReturnValue: FText = Default__KismetTextLibrary.GetEmptyText()
        
        ReturnValue_0: bool = Default__KismetTextLibrary.EqualEqual_TextText(Ref[LocalSearchText], Ref[ReturnValue])
        Variable_0: bool = ReturnValue_0
        
        switch_0 = {
            False: Variable1_0,
            True: Variable
        }
        self.mRecipeDirectory.SetVisibility(switch_0.get(Variable_0, None))
        LocalAllRecipes = self.mParts
        
        Default__KismetArrayLibrary.Array_Append(Ref[LocalAllRecipes], Ref[self.mEquipment])
        
        Default__KismetArrayLibrary.Array_Append(Ref[LocalAllRecipes], Ref[self.mBuildings])
        
        Default__KismetArrayLibrary.Array_Append(Ref[LocalAllRecipes], Ref[self.mVehicles])
        Variable_1: int32 = 0
        Variable_2: int32 = 0
        
        # Label 848
        ReturnValue_1: int32 = len(LocalAllRecipes)
        ReturnValue_2: bool = Variable_1 <= ReturnValue_1
        if not ReturnValue_2:
           goto(ExecutionFlow.Pop())
        Variable_2 = Variable_1
        ExecutionFlow.Push("L1823")
        
        Item = None
        Item = LocalAllRecipes[Variable_2]
        LoacalProduct = Item
        ReturnValue1_1: FText = Default__FGItemDescriptor.GetItemName(LoacalProduct)
        
        ReturnValue_3: FString = Default__KismetTextLibrary.Conv_TextToString(Ref[ReturnValue1_1])
        
        ReturnValue1_2: FString = Default__KismetTextLibrary.Conv_TextToString(Ref[LocalSearchText])
        ReturnValue_4: bool = Default__BPHUDHelpers.DoesTextContainSearchWords(ReturnValue_3, ReturnValue1_2, True, self)
        if not ReturnValue_4:
           goto(ExecutionFlow.Pop())
        
        ReturnValue_5: int32 = self.mSearchResults.append(LoacalProduct)
        ReturnValue_6: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_7: Ptr[Widget_ListButton] = Default__WidgetBlueprintLibrary.Create(self, Widget_ListButton, ReturnValue_6)
        ReturnValue_8: Ptr[Texture2D] = Default__FGItemDescriptor.GetSmallIcon(LoacalProduct)
        Default__KismetSystemLibrary.SetObjectPropertyByName(ReturnValue_7, "mIcon", ReturnValue_8)
        ReturnValue_9: FText = Default__FGItemDescriptor.GetItemName(LoacalProduct)
        
        Default__KismetSystemLibrary.SetTextPropertyByName(ReturnValue_7, "mTitle", Ref[ReturnValue_9])
        OutputDelegate.BindUFunction(self, OnSearchResultClicked)
        ReturnValue_7.OnClicked.AddUnique(OutputDelegate)
        ReturnValue_10: Ptr[PanelSlot] = self.mItemSearchList.AddChild(ReturnValue_7)
        goto(ExecutionFlow.Pop())
        # Label 1823
        ReturnValue_11: int32 = Variable_1 + 1
        Variable_1 = ReturnValue_11
        goto('L848')
    

    def UpdateItemInfo(self, product: TSubclassOf[FGItemDescriptor]):
        ExecutionFlow.Push("L3442")
        localProduct = product
        ReturnValue: Ptr[Texture2D] = Default__FGItemDescriptor.GetBigIcon(localProduct)
        SlateBrush.ImageSize = self.mItemIcon.Brush.ImageSize
        SlateBrush.Margin = self.mItemIcon.Brush.Margin
        SlateBrush.TintColor = self.mItemIcon.Brush.TintColor
        SlateBrush.ResourceObject = ReturnValue
        SlateBrush.DrawAs = self.mItemIcon.Brush.DrawAs
        SlateBrush.Tiling = self.mItemIcon.Brush.Tiling
        # Label 438
        SlateBrush.Mirroring = self.mItemIcon.Brush.Mirroring
        
        SlateBrush = None
        self.mItemIcon.SetBrush(Ref[SlateBrush])
        ReturnValue1: FText = Default__FGItemDescriptor.GetItemName(localProduct)
        self.mIconTitle.SetText(ReturnValue1)
        ReturnValue_0: FText = Default__FGItemDescriptor.GetItemDescription(localProduct)
        self.mIconDescription.SetText(ReturnValue_0)
        self.mItemInfo.SetVisibility(4)
        self.mRecipeProductList.ClearChildren()
        # Label 832
        self.mRecipeIngredientList.ClearChildren()
        ReturnValue3: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue1_0: Ptr[FGRecipeManager] = Default__FGRecipeManager.Get(ReturnValue3)
        ReturnValue_1: List[TSubclassOf[FGRecipe]] = ReturnValue1_0.FindRecipesByProduct(localProduct)
        Variable: int32 = 0
        Variable1: int32 = 0
        
        # Label 1048
        ReturnValue2: int32 = len(ReturnValue_1)
        ReturnValue1_1: bool = Variable <= ReturnValue2
        if not ReturnValue1_1:
            goto('L2174')
        Variable1 = Variable
        ExecutionFlow.Push("L3255")
        # Label 1191
        ReturnValue2_0: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue1_2: Ptr[BPW_Interactable_Recipe] = Default__WidgetBlueprintLibrary.Create(self, BPW_Interactable_Recipe, ReturnValue2_0)
        Variable_0: FText = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 1296, 'Value': 'Standard Recipe: '}"
        ReturnValue_2: bool = Variable1 > 0
        Variable_1: bool = ReturnValue_2
        ReturnValue_3: FString = Default__KismetStringLibrary.Conv_IntToString(Variable1)
        ReturnValue_4: FString = Default__KismetStringLibrary.Concat_StrStr("Alternate Recipe ", ReturnValue_3)
        ReturnValue1_3: FString = Default__KismetStringLibrary.Concat_StrStr(ReturnValue_4, ":")
        ReturnValue_5: FText = Default__KismetTextLibrary.Conv_StringToText(ReturnValue1_3)
        
        switch = {
            False: Variable_0,
            True: ReturnValue_5
        }
        
        switch.get(Variable_1, None) = None
        Default__KismetSystemLibrary.SetTextPropertyByName(ReturnValue1_2, "mRecipeNameText", Ref[switch.get(Variable_1, None)])
        Descriptor: TSubclassOf[FGVehicleDescriptor] = ClassCast[FGVehicleDescriptor](localProduct)
        bSuccess: bool = Descriptor
        Descriptor_0: TSubclassOf[FGBuildingDescriptor] = ClassCast[FGBuildingDescriptor](localProduct)
        bSuccess1: bool = Descriptor_0
        ReturnValue_6: bool = BooleanOR(bSuccess1, bSuccess)
        Default__KismetSystemLibrary.SetBoolPropertyByName(ReturnValue1_2, "mHideProductionInfo", ReturnValue_6)
        
        Item2 = None
        Item2 = ReturnValue_1[Variable1]
        Default__KismetSystemLibrary.SetClassPropertyByName(ReturnValue1_2, "mRecipe", Item2)
        ReturnValue1_4: Ptr[PanelSlot] = self.mRecipeProductList.AddChild(ReturnValue1_2)
        goto(ExecutionFlow.Pop())
        # Label 2174
        if not self.mShowRecipeIngredientList:
            goto('L3216')
        ReturnValue_7: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_8: Ptr[FGRecipeManager] = Default__FGRecipeManager.Get(ReturnValue_7)
        ReturnValue_9: List[TSubclassOf[FGRecipe]] = ReturnValue_8.FindRecipesByIngredient(localProduct)
        
        ReturnValue1_5: int32 = len(ReturnValue_9)
        ReturnValue1_6: bool = ReturnValue1_5 > 0
        if not ReturnValue1_6:
            goto('L3329')
        self.mRecipeIngredientTitle.SetVisibility(0)
        Variable1_0: int32 = 0
        Variable_2: int32 = 0
        
        # Label 2513
        ReturnValue_10: int32 = len(ReturnValue_9)
        ReturnValue_11: bool = Variable1_0 <= ReturnValue_10
        if not ReturnValue_11:
           goto(ExecutionFlow.Pop())
        Variable_2 = Variable1_0
        ExecutionFlow.Push("L3368")
        ReturnValue1_7: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_12: Ptr[BPW_Interactable_Recipe] = Default__WidgetBlueprintLibrary.Create(self, BPW_Interactable_Recipe, ReturnValue1_7)
        
        Item = None
        Item = ReturnValue_9[Variable_2]
        ReturnValue_13: List[ItemAmount] = Default__FGRecipe.GetProducts(Item, False)
        
        Item1 = None
        Item1 = ReturnValue_13[0]
        ReturnValue_14: FText = Default__FGItemDescriptor.GetItemName(Item1.ItemClass)
        
        Default__KismetSystemLibrary.SetTextPropertyByName(ReturnValue_12, "mRecipeNameText", Ref[ReturnValue_14])
        
        Item = None
        Item = ReturnValue_9[Variable_2]
        Default__KismetSystemLibrary.SetClassPropertyByName(ReturnValue_12, "mRecipe", Item)
        ReturnValue_15: Ptr[PanelSlot] = self.mRecipeIngredientList.AddChild(ReturnValue_12)
        goto(ExecutionFlow.Pop())
        # Label 3216
        self.mRecipeIngredientTitle.SetVisibility(1)
        goto(ExecutionFlow.Pop())
        # Label 3255
        ReturnValue_16: int32 = Variable + 1
        Variable = ReturnValue_16
        goto('L1048')
        # Label 3329
        self.mRecipeIngredientTitle.SetVisibility(1)
        goto(ExecutionFlow.Pop())
        # Label 3368
        ReturnValue1_8: int32 = Variable1_0 + 1
        Variable1_0 = ReturnValue1_8
        goto('L2513')
    

    def SetAllItemsAndBuildings(self):
        ExecutionFlow.Push("L1704")
        ReturnValue: Ptr[GameStateBase] = Default__GameplayStatics.GetGameState(self)
        ReturnValue_0: Ptr[FGRecipeManager] = Default__FGRecipeManager.Get(ReturnValue)
        recipes: List[TSubclassOf[FGRecipe]] = []
        
        ReturnValue_0.GetAllAvailableRecipes(Ref[recipes])
        Variable: int32 = 0
        Variable1: int32 = 0
        
        # Label 197
        ReturnValue_1: int32 = len(recipes)
        # Label 256
        ReturnValue_2: bool = Variable <= ReturnValue_1
        if not ReturnValue_2:
            goto('L930')
        Variable1 = Variable
        ExecutionFlow.Push("L1043")
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
        ExecutionFlow.Push("L1117")
        
        Item = None
        Item = recipes[Variable1]
        ReturnValue_3 = Default__FGRecipe.GetProducts(Item, False)
        
        Item1 = None
        Item1 = ReturnValue_3[Variable_0]
        LocalClass = Item1.ItemClass
        Descriptor: TSubclassOf[FGResourceDescriptor] = ClassCast[FGResourceDescriptor](LocalClass)
        bSuccess: bool = Descriptor
        if not bSuccess:
            goto('L1191')
        goto(ExecutionFlow.Pop())
        # Label 930
        self.mBuildings = LocalBuildings
        self.mEquipment = LocalEquipment
        self.mVehicles = LocalVehicles
        self.mParts = LocalItems
        # End
        # Label 1043
        ReturnValue_4: int32 = Variable + 1
        Variable = ReturnValue_4
        goto('L197')
        # Label 1117
        ReturnValue1_1: int32 = Variable1_0 + 1
        Variable1_0 = ReturnValue1_1
        goto('L386')
        # Label 1191
        Descriptor_0: TSubclassOf[FGBuildingDescriptor] = ClassCast[FGBuildingDescriptor](LocalClass)
        bSuccess3: bool = Descriptor_0
        if not bSuccess3:
            goto('L1339')
        
        ReturnValue2: int32 = Default__KismetArrayLibrary.Array_AddUnique(Ref[LocalBuildings], Ref[LocalClass])
        goto(ExecutionFlow.Pop())
        # Label 1339
        Descriptor_1: TSubclassOf[FGVehicleDescriptor] = ClassCast[FGVehicleDescriptor](LocalClass)
        bSuccess2: bool = Descriptor_1
        if not bSuccess2:
            goto('L1487')
        
        ReturnValue_5: int32 = Default__KismetArrayLibrary.Array_AddUnique(Ref[LocalVehicles], Ref[LocalClass])
        goto(ExecutionFlow.Pop())
        # Label 1487
        Descriptor_2: TSubclassOf[FGEquipmentDescriptor] = ClassCast[FGEquipmentDescriptor](LocalClass)
        bSuccess1: bool = Descriptor_2
        if not bSuccess1:
            goto('L1635')
        
        ReturnValue1_2: int32 = Default__KismetArrayLibrary.Array_AddUnique(Ref[LocalEquipment], Ref[LocalClass])
        goto(ExecutionFlow.Pop())
        
        # Label 1635
        ReturnValue3: int32 = Default__KismetArrayLibrary.Array_AddUnique(Ref[LocalItems], Ref[LocalClass])
        goto(ExecutionFlow.Pop())
    

    def GenerateReceipes(self, InRecipes: Ref[List[TSubclassOf[FGItemDescriptor]]]):
        ExecutionFlow.Push("L855")
        self.mItemList.ClearChildren()
        Variable: int32 = 0
        Variable_0: int32 = 0
        
        # Label 87
        ReturnValue: int32 = len(InRecipes)
        ReturnValue_0: bool = Variable <= ReturnValue
        if not ReturnValue_0:
           goto(ExecutionFlow.Pop())
        Variable_0 = Variable
        ExecutionFlow.Push("L781")
        ReturnValue_1: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_2: Ptr[Widget_ListButton] = Default__WidgetBlueprintLibrary.Create(self, Widget_ListButton, ReturnValue_1)
        
        Item = None
        Item = InRecipes[Variable_0]
        ReturnValue_3: Ptr[Texture2D] = Default__FGItemDescriptor.GetSmallIcon(Item)
        Default__KismetSystemLibrary.SetObjectPropertyByName(ReturnValue_2, "mIcon", ReturnValue_3)
        
        Item = None
        Item = InRecipes[Variable_0]
        ReturnValue_4: FText = Default__FGItemDescriptor.GetItemName(Item)
        
        Default__KismetSystemLibrary.SetTextPropertyByName(ReturnValue_2, "mTitle", Ref[ReturnValue_4])
        OutputDelegate.BindUFunction(self, OnRecipeButtonClicked)
        ReturnValue_2.OnClicked.AddUnique(OutputDelegate)
        ReturnValue_5: Ptr[PanelSlot] = self.mItemList.AddChild(ReturnValue_2)
        goto(ExecutionFlow.Pop())
        # Label 781
        ReturnValue_6: int32 = Variable + 1
        Variable = ReturnValue_6
        goto('L87')
    

    def UpdateNotifications(self, forButton: Ptr[Widget_CodexButton]):
        ExecutionFlow.Push("L1190")
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(forButton)
        if not ReturnValue:
            goto('L832')
        localButton = forButton
        # Label 89
        ReturnValue_0: Ptr[PlayerController] = self.GetOwningPlayer()
        State: Ptr[FGPlayerState] = Cast[FGPlayerState](ReturnValue_0.PlayerState)
        bSuccess: bool = State
        if not bSuccess:
           goto(ExecutionFlow.Pop())
        Variable: int32 = 0
        Variable_0: int32 = 0
        # Label 256
        ReturnValue_1: List[MessageData] = State.GetAllMessageData()
        
        ReturnValue_2: int32 = len(ReturnValue_1)
        ReturnValue_3: bool = Variable <= ReturnValue_2
        if not ReturnValue_3:
            goto('L856')
        Variable_0 = Variable
        ExecutionFlow.Push("L1116")
        ReturnValue_1 = State.GetAllMessageData()
        
        Item = None
        Item = ReturnValue_1[Variable_0]
        ReturnValue_4: bool = Not_PreBool(Item.WasRead)
        ReturnValue_5: bool = EqualEqual_ByteByte(Item.MessageClass.ClassDefaultObject.mType, localButton.mType)
        ReturnValue_6: bool = ReturnValue_4 and ReturnValue_5
        if not ReturnValue_6:
           goto(ExecutionFlow.Pop())
        ReturnValue1: int32 = LocalCounter + 1
        Variable_1: int32 = ReturnValue1
        LocalCounter = Variable_1
        goto(ExecutionFlow.Pop())
        # Label 832
        localButton = self.mActiveButton
        goto('L89')
        # Label 856
        ReturnValue_7: FText = Default__KismetTextLibrary.Conv_IntToText(LocalCounter, False, True, 1, 324)
        ReturnValue_8: bool = LocalCounter > 0
        Variable_2: bool = ReturnValue_8
        Variable_3: FText = 
        
        switch = {
            False: Variable_3,
            True: ReturnValue_7
        }
        localButton.mMessageNotification.mText = switch.get(Variable_2, None)
        goto(ExecutionFlow.Pop())
        # Label 1116
        ReturnValue_9: int32 = Variable + 1
        Variable = ReturnValue_9
        goto('L256')
    

    def OnFilterButtonPressed(self, ButtonPressed: Ptr[Widget_CodexButton]):
        self.mActiveButton = ButtonPressed
        self.PopulateList()
    

    def SelectButtonWithMessage(self, inMessage: TSubclassOf[FGMessageBase]):
        ExecutionFlow.Push("L597")
        LocalMessage = inMessage
        Variable: bool = False
        Variable_0: int32 = 0
        Variable_1: int32 = 0
        # Label 81
        ReturnValue: bool = Not_PreBool(Variable)
        
        ReturnValue_0: int32 = len(self.mButtons)
        ReturnValue_1: bool = Variable_0 <= ReturnValue_0
        ReturnValue_2: bool = ReturnValue and ReturnValue_1
        if not ReturnValue_2:
           goto(ExecutionFlow.Pop())
        Variable_1 = Variable_0
        ExecutionFlow.Push("L523")
        
        Item = None
        Item = self.mButtons[Variable_1]
        ReturnValue_3: bool = EqualEqual_ClassClass(Item.mMessage, LocalMessage)
        if not ReturnValue_3:
           goto(ExecutionFlow.Pop())
        
        Item = None
        Item = self.mButtons[Variable_1]
        Item.MessageWasClicked()
        Variable = True
        goto(ExecutionFlow.Pop())
        # Label 523
        ReturnValue_4: int32 = Variable_0 + 1
        Variable_0 = ReturnValue_4
        goto('L81')
    

    def CheckShouldOpenMessage(self):
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        
        gameUI = None
        Default__HUDHelpers.GetFGGameUI(ReturnValue, self, Ref[gameUI])
        UI: TScriptInterface[BPI_GameUI] = QueryInterface[BPI_GameUI](gameUI)
        bSuccess: bool = UI
        if not bSuccess:
            goto('L422')
        
        messageBox = None
        GetInterfaceUObject(UI).GetMessageBox(Ref[messageBox])
        # Label 204
        ReturnValue_0: bool = messageBox.HasAnyChildren()
        if not ReturnValue_0:
            goto('L438')
        ReturnValue_1: Ptr[Widget] = messageBox.GetChildAt(0)
        Notifier: Ptr[Widget_MessageNotifier] = Cast[Widget_MessageNotifier](ReturnValue_1)
        bSuccess1: bool = Notifier
        self.SelectButtonWithMessage(Notifier.mMessage)
        # End
        # Label 422
        messageBox: Ptr[VerticalBox] = None
        goto('L204')
    

    def UpdateMessageText(self, senderMail: FText, Sender: FText, Title: FText):
        FormatArgumentData1.ArgumentName = "A"
        FormatArgumentData1.ArgumentValueType = 4
        # Label 59
        FormatArgumentData1.ArgumentValue = senderMail
        FormatArgumentData1.ArgumentValueInt = 0
        FormatArgumentData1.ArgumentValueFloat = 0
        FormatArgumentData1.ArgumentValueGender = 0
        Array1: List[FormatArgumentData] = [FormatArgumentData1]
        ReturnValue1: FText = Default__KismetTextLibrary.Format("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 259, 'Value': 'From: {A}'}", Array1)
        self.mSenderEmailAdress.SetText(ReturnValue1)
        FormatArgumentData.ArgumentName = "A"
        FormatArgumentData.ArgumentValueType = 4
        FormatArgumentData.ArgumentValue = Title
        FormatArgumentData.ArgumentValueInt = 0
        FormatArgumentData.ArgumentValueFloat = 0
        FormatArgumentData.ArgumentValueGender = 0
        Array: List[FormatArgumentData] = [FormatArgumentData]
        ReturnValue: FText = Default__KismetTextLibrary.Format("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 620, 'Value': 'Subject: {A}'}", Array)
        self.mMessageNameText.SetText(ReturnValue)
        self.mSenderNameText.SetText(Sender)
        self.mMessageIsClicked = True
    

    def PopulateList(self):
        ExecutionFlow.Push("L1561")
        
        Default__KismetArrayLibrary.Array_Clear(Ref[self.mButtons])
        self.Testetete.ClearChildren()
        ReturnValue1: Ptr[PlayerController] = self.GetOwningPlayer()
        State: Ptr[FGPlayerState] = Cast[FGPlayerState](ReturnValue1.PlayerState)
        bSuccess: bool = State
        if not bSuccess:
           goto(ExecutionFlow.Pop())
        ReturnValue: List[MessageData] = State.GetAllMessageData()
        
        ReturnValue_0: int32 = len(ReturnValue)
        ReturnValue1_0: int32 = ReturnValue_0 - 1
        Variable: int32 = ReturnValue1_0
        ReturnValue = State.GetAllMessageData()
        
        ReturnValue_0 = len(ReturnValue)
        ReturnValue1_0 = ReturnValue_0 - 1
        ReturnValue_1: int32 = Max(0, ReturnValue1_0)
        Variable_0: int32 = ReturnValue_1
        # Label 601
        ReturnValue_2: bool = GreaterEqual_IntInt(Variable, 0)
        if not ReturnValue_2:
           goto(ExecutionFlow.Pop())
        Variable_0 = Variable
        ExecutionFlow.Push("L1487")
        ReturnValue = State.GetAllMessageData()
        
        Item = None
        Item = ReturnValue[Variable_0]
        ReturnValue_3: bool = EqualEqual_ByteByte(Item.MessageClass.ClassDefaultObject.mType, self.mCurrentTab)
        # Label 855
        if not ReturnValue_3:
           goto(ExecutionFlow.Pop())
        ReturnValue_4: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_5: Ptr[Widget_Codex_MessageButton] = Default__WidgetBlueprintLibrary.Create(self, Widget_Codex_MessageButton, ReturnValue_4)
        Default__KismetSystemLibrary.SetObjectPropertyByName(ReturnValue_5, "mOwningCodex", self)
        ReturnValue = State.GetAllMessageData()
        
        Item = None
        Item = ReturnValue[Variable_0]
        Default__KismetSystemLibrary.SetClassPropertyByName(ReturnValue_5, "mMessage", Item.MessageClass)
        ReturnValue = State.GetAllMessageData()
        
        Item = None
        Item = ReturnValue[Variable_0]
        Default__KismetSystemLibrary.SetBoolPropertyByName(ReturnValue_5, "mMessageHasBeenRead", Item.WasRead)
        
        ReturnValue_6: int32 = self.mButtons.append(ReturnValue_5)
        ReturnValue_7: Ptr[PanelSlot] = self.Testetete.AddChild(ReturnValue_5)
        goto(ExecutionFlow.Pop())
        # Label 1487
        ReturnValue_8: int32 = Variable - 1
        Variable = ReturnValue_8
        goto('L601')
    

    def GetActiveTabFeedback(self):
        pass
    

    def GetMessageVisiblity(self):
        if not self.mMessageIsClicked:
            goto('L39')
        ReturnValue = 0
        goto('L59')
        # Label 39
        ReturnValue = 2
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_Codex_Container(674)
    

    def CloseCodex(self):
        self.ExecuteUbergraph_Widget_Codex_Container(1284)
    

    def MarkAllAsRead(self):
        self.ExecuteUbergraph_Widget_Codex_Container(1448)
    

    def BndEvt__Widget_Window_DarkMode_K2Node_ComponentBoundEvent_0_OnTabButtonClicked__DelegateSignature(self, ButtonIndex: int32):
        ExecuteUbergraph_Widget_Codex_Container.K2Node_ComponentBoundEvent_ButtonIndex = ButtonIndex #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_Codex_Container(1453)
    

    def OnRecipeButtonClicked(self, index: int32, ListButton: Ptr[Widget_ListButton]):
        ExecuteUbergraph_Widget_Codex_Container.K2Node_CustomEvent_Index1 = index #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_Codex_Container.K2Node_CustomEvent_ListButton1 = ListButton #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_Codex_Container(2094)
    

    def BndEvt__mSearchBar_K2Node_ComponentBoundEvent_1_OnTextChanged__DelegateSignature(self, text: FText):
        ExecuteUbergraph_Widget_Codex_Container.K2Node_ComponentBoundEvent_Text = text #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_Codex_Container(2177)
    

    def OnSearchResultClicked(self, index: int32, ListButton: Ptr[Widget_ListButton]):
        ExecuteUbergraph_Widget_Codex_Container.K2Node_CustomEvent_Index = index #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_Codex_Container.K2Node_CustomEvent_ListButton = ListButton #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_Codex_Container(2201)
    

    def BndEvt__Widget_ListButton_K2Node_ComponentBoundEvent_2_OnClicked__DelegateSignature(self, index: int32, ListButton: Ptr[Widget_ListButton]):
        ExecuteUbergraph_Widget_Codex_Container.K2Node_ComponentBoundEvent_Index3 = index #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_Codex_Container.K2Node_ComponentBoundEvent_ListButton3 = ListButton #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_Codex_Container(2284)
    

    def BndEvt__Widget_ListButton_C_0_K2Node_ComponentBoundEvent_3_OnClicked__DelegateSignature(self, index: int32, ListButton: Ptr[Widget_ListButton]):
        ExecuteUbergraph_Widget_Codex_Container.K2Node_ComponentBoundEvent_Index2 = index #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_Codex_Container.K2Node_ComponentBoundEvent_ListButton2 = ListButton #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_Codex_Container(2335)
    

    def BndEvt__Widget_ListButton_C_1_K2Node_ComponentBoundEvent_4_OnClicked__DelegateSignature(self, index: int32, ListButton: Ptr[Widget_ListButton]):
        ExecuteUbergraph_Widget_Codex_Container.K2Node_ComponentBoundEvent_Index1 = index #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_Codex_Container.K2Node_ComponentBoundEvent_ListButton1 = ListButton #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_Codex_Container(2367)
    

    def BndEvt__mCategoryVehicles_K2Node_ComponentBoundEvent_5_OnClicked__DelegateSignature(self, index: int32, ListButton: Ptr[Widget_ListButton]):
        ExecuteUbergraph_Widget_Codex_Container.K2Node_ComponentBoundEvent_Index = index #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_Codex_Container.K2Node_ComponentBoundEvent_ListButton = ListButton #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_Codex_Container(2399)
    

    def ExecuteUbergraph_Widget_Codex_Container(self):
        goto(ComputedJump("EntryPoint"))
        # Label 15
        Default__KismetSystemLibrary.Delay(self, 0.10000000149011612, LatentActionInfo(Linkage = 92, UUID = -843323016, ExecutionFunction = "ExecuteUbergraph_Widget_Codex_Container", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        ReturnValue1: Ptr[PlayerController] = self.GetOwningPlayer()
        self.mSearchbar.mInputBox.SetUserFocus(ReturnValue1)
        goto(ExecutionFlow.Pop())
        # Label 180
        ExecutionFlow.Push("L345")
        ReturnValue: List[TSubclassOf[FGMessageBase]] = State.GetAllMessages(self.mCurrentTab)
        
        Item2 = None
        Item2 = ReturnValue[Variable]
        State.ReadMessage(Item2)
        goto(ExecutionFlow.Pop())
        # Label 345
        ReturnValue_0: int32 = Variable + 1
        Variable: int32 = ReturnValue_0
        # Label 414
        ReturnValue = State.GetAllMessages(self.mCurrentTab)
        
        ReturnValue_1: int32 = len(ReturnValue)
        ReturnValue_2: bool = Variable <= ReturnValue_1
        if not ReturnValue_2:
            goto('L616')
        Variable = Variable
        goto('L180')
        # Label 616
        self.PopulateList()
        self.UpdateNotifications(None)
        goto(ExecutionFlow.Pop())
        # Label 646
        Variable = 0
        goto('L414')
        self.Construct()
        self.SetDefaultFocusWidget(self.mInboxButton)
        OutputDelegate.BindUFunction(self, CloseCodex)
        self.Widget_Window_DarkMode.OnClose.AddUnique(OutputDelegate)
        self.mActiveButton = self.mInboxButton
        OutputDelegate1.BindUFunction(self, OnFilterButtonPressed)
        self.mInboxButton.OnClicked.AddUnique(OutputDelegate1)
        OutputDelegate2.BindUFunction(self, OnFilterButtonPressed)
        self.mSpamButton.OnClicked.AddUnique(OutputDelegate2)
        OutputDelegate3.BindUFunction(self, OnFilterButtonPressed)
        self.mNotificationsButton.OnClicked.AddUnique(OutputDelegate3)
        OutputDelegate4.BindUFunction(self, MarkAllAsRead)
        self.mMarkAllAsReadButton.OnClicked.AddUnique(OutputDelegate4)
        self.PopulateList()
        self.UpdateNotifications(self.mInboxButton)
        self.UpdateNotifications(self.mNotificationsButton)
        self.UpdateNotifications(self.mSpamButton)
        self.CheckShouldOpenMessage()
        self.SetAllItemsAndBuildings()
        self.Widget_SlidingTabs.SetActiveIndex(2, False)
        ReturnValue_3: bool = Default__KismetSystemLibrary.IsValidClass(self.mOpenOnRecipe)
        if not ReturnValue_3:
            goto('L15')
        self.UpdateItemInfo(self.mOpenOnRecipe)
        goto(ExecutionFlow.Pop())
        self.OnEscapePressed()
        goto(ExecutionFlow.Pop())
        # Label 1299
        ReturnValue_4: Ptr[PlayerController] = self.GetOwningPlayer()
        State: Ptr[FGPlayerState] = Cast[FGPlayerState](ReturnValue_4.PlayerState)
        bSuccess: bool = State
        if not bSuccess:
           goto(ExecutionFlow.Pop())
        Variable = 0
        goto('L646')
        goto('L1299')
        CmpSuccess: bool = ButtonIndex != 0
        # Label 1487
        if not CmpSuccess:
            goto('L1598')
        CmpSuccess = ButtonIndex != 1
        if not CmpSuccess:
            goto('L1675')
        CmpSuccess = ButtonIndex != 2
        if not CmpSuccess:
            goto('L2051')
        goto(ExecutionFlow.Pop())
        # Label 1598
        self.mCurrentTab = 0
        self.PopulateList()
        self.Widget_SlidingTabs.SetActiveIndex(0, True)
        goto(ExecutionFlow.Pop())
        # Label 1675
        self.mCurrentTab = 1
        self.PopulateList()
        ReturnValue_5: bool = self.Widget_SlidingTabs.mActiveIndex != 0
        if not ReturnValue_5:
           goto(ExecutionFlow.Pop())
        self.Widget_SlidingTabs.SetActiveIndex(0, True)
        ReturnValue_6: Ptr[Widget] = self.Widget_Window_DarkMode.Widget_TabsContainer.mContainer.GetChildAt(1)
        Button: Ptr[Widget_SlidingTabs_Button] = Cast[Widget_SlidingTabs_Button](ReturnValue_6)
        bSuccess1: bool = Button
        if not bSuccess1:
           goto(ExecutionFlow.Pop())
        self.Widget_Window_DarkMode.Widget_TabsContainer.SetActiveButton(Button)
        goto(ExecutionFlow.Pop())
        # Label 2051
        self.Widget_SlidingTabs.SetActiveIndex(2, True)
        goto(ExecutionFlow.Pop())
        
        Item1 = None
        Item1 = self.mCurrentList[Index1]
        self.UpdateItemInfo(Item1)
        goto(ExecutionFlow.Pop())
        self.PopulateSearchResults(Text)
        goto(ExecutionFlow.Pop())
        
        Item = None
        Item = self.mSearchResults[Index]
        self.UpdateItemInfo(Item)
        goto(ExecutionFlow.Pop())
        self.mCurrentList = self.mParts
        
        # Label 2311
        self.GenerateReceipes(Ref[self.mCurrentList])
        goto(ExecutionFlow.Pop())
        self.mCurrentList = self.mEquipment
        goto('L2311')
        self.mCurrentList = self.mBuildings
        goto('L2311')
        self.mCurrentList = self.mVehicles
        goto('L2311')
    
