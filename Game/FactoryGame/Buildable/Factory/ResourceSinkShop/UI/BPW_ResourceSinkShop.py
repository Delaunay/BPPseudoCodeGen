
from codegen.ue4_stub import *

from Script.FactoryGame import FGCharacterPlayer
from Script.FactoryGame import GetCost
from Game.FactoryGame.Buildable.Factory.ResourceSinkShop.UI.ResourceSinkShop_Banner_Struct import ResourceSinkShop_Banner_Struct
from Script.Engine import FTrunc
from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import Array_Find
from Script.UMG import GetChildAt
from Script.Engine import NotEqual_ClassClass
from Script.Engine import FormatArgumentData
from Script.FactoryGame import GetSchematicCategory
from Script.UMG import ESlateVisibility
from Script.FactoryGame import GetAllSchematicsOfTypeFilteredOnDependency
from Script.Engine import TimerHandle
from Script.Engine import IsValid
from Script.Engine import Conv_IntToText
from Script.Engine import EqualEqual_IntInt
from Script.Engine import Default__KismetTextLibrary
from Script.Engine import Map_Values
from Script.FactoryGame import FGBuildableResourceSinkShop
from Script.Engine import SetIntPropertyByName
from Script.Engine import Map_Find
from Script.UMG import ScrollToStart
from Script.Engine import Map_Add
from Script.FactoryGame import FGUnlockGiveItem
from Game.FactoryGame.Buildable.Factory.ResourceSinkShop.UI.BPW_ResourceSinkShop_Item import BPW_ResourceSinkShop_Item
from Script.UMG import Create
from Script.SlateCore import SlateBrush
from Game.FactoryGame.Resource.Parts.ResourceSinkCoupon.Desc_ResourceSinkCoupon import Desc_ResourceSinkCoupon
from Script.FactoryGame import FGSchematicCategory
from Script.Engine import Array_Clear
from Game.FactoryGame.Interface.UI.Audio.Play_Shop_SpaceCashier import Play_Shop_SpaceCashier
from Script.Engine import EqualEqual_ClassClass
from Script.Engine import SetClassPropertyByName
from Game.FactoryGame.Buildable.Factory.ResourceSinkShop.UI.BPW_ResourceSinkShop import ExecuteUbergraph_BPW_ResourceSinkShop
from Game.FactoryGame.Buildable.Factory.ResourceSinkShop.UI.BPW_ResourceSinkShop_CartItem import BPW_ResourceSinkShop_CartItem
from Script.Engine import EqualEqual_ByteByte
from Script.UMG import GetVisibility
from Script.Engine import Pawn
from Script.Engine import GreaterEqual_IntInt
from Script.UMG import AddChildToVerticalBox
from Script.Engine import Default__KismetArrayLibrary
from Script.UMG import SetHorizontalAlignment
from Script.FactoryGame import GetInventory
from Script.FactoryGame import FGUnlock
from Script.FactoryGame import SortInventory
from Script.FactoryGame import FGInventoryComponent
from Game.FactoryGame.Buildable.Factory.ResourceSinkShop.UI.BPW_ResourceSinkShop import ExecuteUbergraph_BPW_ResourceSinkShop.K2Node_ComponentBoundEvent_mSchematic
from Script.FactoryGame import GetSubCategories
from Script.Engine import SetMouseLocation
from Script.AkAudio import Default__AkGameplayStatics
from Script.UMG import WrapBoxSlot
from Game.FactoryGame.Schematics.ResourceSinkShopCategories.SC_RSS_Attachments import SC_RSS_Attachments
from Script.FactoryGame import Default__FGSchematicCategory
from Game.FactoryGame.Interface.UI.HUDHelpers.BPHUDHelpers import Default__BPHUDHelpers
from Script.FactoryGame import FGResourceSinkSubsystem
from Script.UMG import AddChildToHorizontalBox
from Script.UMG import VerticalBoxSlot
from Script.FactoryGame import ItemAmount
from Script.AkAudio import AkComponent
from Game.FactoryGame.Buildable.Factory.ResourceSinkShop.UI.BPW_ResourceSinkShop import ExecuteUbergraph_BPW_ResourceSinkShop.K2Node_ComponentBoundEvent_ButtonIndex
from Script.UMG import EventReply
from Script.Engine import SetTextPropertyByName
from Game.FactoryGame.Buildable.Factory.ResourceSinkShop.UI.BPW_ResourceSinkShop import ExecuteUbergraph_BPW_ResourceSinkShop.K2Node_ComponentBoundEvent_Schematic
from Script.AkAudio import PostAkEvent
from Script.Engine import Array_Contains
from Script.FactoryGame import FGPlayerState
from Game.FactoryGame.Buildable.Factory.ResourceSinkShop.UI.BPW_ResourceSinkShop import ExecuteUbergraph_BPW_ResourceSinkShop.K2Node_CustomEvent_CurrentOffset
from Script.UMG import Default__WidgetLayoutLibrary
from Script.FactoryGame import GetCategoryName
from Script.FactoryGame import Get
from Script.Engine import PlayerController
from Script.Engine import Map_Remove
from Script.UMG import PlayAnimation
from Script.UMG import Unhandled
from Script.FactoryGame import GetCategoryIcon
from Script.FactoryGame import GetShopInventory
from Script.FactoryGame import GetUnlocks
from Script.FactoryGame import IsRepeatPurchasesAllowed
from Script.FactoryGame import GetLastSelectedResourceSinkShopCategory
from Script.UMG import Default__WidgetBlueprintLibrary
from Script.FactoryGame import SetLastSelectedResourceSinkShopCategory
from Script.UMG import AddChildToWrapBox
from Script.Engine import BreakVector2D
from Script.Engine import SetBoolPropertyByName
from Script.Engine import Format
from Game.FactoryGame.Interface.UI.InGame.Widget_UseableBase import Widget_UseableBase
from Script.FactoryGame import Default__FGResourceSinkSubsystem
from Script.FactoryGame import Default__FGBlueprintFunctionLibrary
from Script.FactoryGame import FGSchematicManager
from Script.CoreUObject import Vector2D
from Script.Engine import Map_Keys
from Script.UMG import SetVerticalAlignment
from Game.FactoryGame.Buildable.Factory.ResourceSinkShop.UI.ResourceSinkShop_CartItem_Struct import ResourceSinkShop_CartItem_Struct
from Script.UMG import SetSize
from Script.UMG import GetScrollOffset
from Script.UMG import GetViewportSize
from Game.FactoryGame.Buildable.Factory.ResourceSinkShop.UI.BPW_ResourceSinkShop import ExecuteUbergraph_BPW_ResourceSinkShop.K2Node_ComponentBoundEvent_Amount
from Script.Engine import Map_Contains
from Script.UMG import HorizontalBoxSlot
from Script.Engine import Not_PreBool
from Script.Engine import Map_Clear
from Game.FactoryGame.Buildable.Factory.ResourceSinkShop.UI.BPW_ResourceSinkShop_CategoryButtons import BPW_ResourceSinkShop_CategoryButtons
from Script.FactoryGame import GetNumItems
from Script.UMG import Widget
from Script.Engine import Array_AddUnique
from Script.FactoryGame import FGSchematic
from Script.UMG import WidgetAnimation
from Script.UMG import GetOwningPlayerPawn
from Script.UMG import UMGSequencePlayer
from Script.FactoryGame import Default__FGSchematic
from Script.FactoryGame import GetSubCategoriesForSchematicCategory
from Game.FactoryGame.BPW_ResourceSinkShop_Subcategory_Header import BPW_ResourceSinkShop_Subcategory_Header
from Script.Engine import Default__BlueprintMapLibrary
from Script.Engine import IsValidClass
from Script.FactoryGame import Default__FGSchematicManager

class BPW_ResourceSinkShop(Widget_UseableBase):
    AddedToCart: Ptr[WidgetAnimation]
    MinimizeHeader: Ptr[WidgetAnimation]
    FadeInCategory: Ptr[WidgetAnimation]
    mHoveredButton: Ptr[BPW_ResourceSinkShop_Item]
    mHoveredSchematic: TSubclassOf[FGSchematic]
    mSelectedSchematicCategory: TSubclassOf[FGSchematicCategory]
    mAllSchematicCategories: List[TSubclassOf[FGSchematicCategory]]
    mIsSearchFocused: bool
    mSearchWaitForKeyUp: bool
    mSearchResultHoveredTimerHandle: TimerHandle
    mCartItemStruct: Dict[TSubclassOf[FGSchematic], ResourceSinkShop_CartItem_Struct]
    mResourceSinkShop: Ptr[FGBuildableResourceSinkShop]
    mShopItemButtons: List[Ptr[BPW_ResourceSinkShop_Item]]
    mBannerStruct: List[ResourceSinkShop_Banner_Struct]
    mShouldOpenInventory = True
    mUseKeyboard = True
    mUseMouse = True
    mCaptureInput = True
    mRestoreFocusWhenLost = True
    mInputToPassThrough = ['Use']
    mDesiredHorizontalAlignment = 2
    mDesiredVerticalAlignment = 2
    mCallCustomTickOnConstruct = True
    
    def OnStorageOpened(self):
        ExecutionFlow.Push("L631")
        self.mWindow.SetInventoryVisibility(True, True)
        ReturnValue: Ptr[FGInventoryComponent] = self.mResourceSinkShop.GetShopInventory()
        ReturnValue.SortInventory()
        ReturnValue = self.mResourceSinkShop.GetShopInventory()
        self.mShopInventory.Init(ReturnValue)
        Variable: int32 = 0
        Variable_0: int32 = 0
        
        self.mShopInventory.mInventorySlots = None
        # Label 250
        ReturnValue_0: int32 = len(self.mShopInventory.mInventorySlots)
        ReturnValue_1: bool = Variable <= ReturnValue_0
        if not ReturnValue_1:
           goto(ExecutionFlow.Pop())
        Variable_0 = Variable
        ExecutionFlow.Push("L557")
        OutputDelegate.BindUFunction(self, OnInventorySlotStackMove)
        
        self.mShopInventory.mInventorySlots = None
        Item = None
        Item = self.mShopInventory.mInventorySlots[Variable_0]
        Item.OnMoveStack.AddUnique(OutputDelegate)
        goto(ExecutionFlow.Pop())
        # Label 557
        ReturnValue_2: int32 = Variable + 1
        Variable = ReturnValue_2
        goto('L250')
    

    def UpdateBanner(self):
        Variable: Vector2D = Vector2D(X = 300, Y = 300)
        Variable1: Vector2D = Vector2D(X = 230, Y = 230)
        ReturnValue: bool = EqualEqual_ClassClass(self.mSelectedSchematicCategory, SC_RSS_Attachments)
        ReturnValue_0: SlateBrush = Default__FGSchematicCategory.GetCategoryIcon(self.mSelectedSchematicCategory)
        Variable_0: bool = ReturnValue
        ReturnValue_1: FText = Default__FGSchematicCategory.GetCategoryName(self.mSelectedSchematicCategory)
        
        switch = {
            False: Variable1,
            True: Variable
        }
        SlateBrush.ImageSize = switch.get(Variable_0, None)
        SlateBrush.Margin = self.BPW_ResourceSinkShop_Banner.mBannerStruct.ImageBrush_5_012E7B504A7AB4B9D1F758A855CF7C5F.Margin
        SlateBrush.TintColor = self.BPW_ResourceSinkShop_Banner.mBannerStruct.ImageBrush_5_012E7B504A7AB4B9D1F758A855CF7C5F.TintColor
        SlateBrush.ResourceObject = ReturnValue_0.ResourceObject
        SlateBrush.DrawAs = self.BPW_ResourceSinkShop_Banner.mBannerStruct.ImageBrush_5_012E7B504A7AB4B9D1F758A855CF7C5F.DrawAs
        SlateBrush.Tiling = self.BPW_ResourceSinkShop_Banner.mBannerStruct.ImageBrush_5_012E7B504A7AB4B9D1F758A855CF7C5F.Tiling
        SlateBrush.Mirroring = self.BPW_ResourceSinkShop_Banner.mBannerStruct.ImageBrush_5_012E7B504A7AB4B9D1F758A855CF7C5F.Mirroring
        Struct.Text_7_9ECC94234929451FA80AFDAC404AD507 = ReturnValue_1
        Struct.ImageBrush_5_012E7B504A7AB4B9D1F758A855CF7C5F = SlateBrush
        Struct.TextEndPosition_12_284EB20F4CB57ECB983D038E3F457990 = self.BPW_ResourceSinkShop_Banner.mBannerStruct.TextEndPosition_12_284EB20F4CB57ECB983D038E3F457990
        Struct.ImageEndPosition_10_3EA4EF5B4A94A13E17A775B8C65CE230 = self.BPW_ResourceSinkShop_Banner.mBannerStruct.ImageEndPosition_10_3EA4EF5B4A94A13E17A775B8C65CE230
        self.BPW_ResourceSinkShop_Banner.SetBanner(Struct)
    

    def GetBannerStruct(self):
        pass
    

    def GetAmountOfCouponsInPlayerInventory(self):
        ReturnValue: Ptr[Pawn] = self.GetOwningPlayerPawn()
        Player: Ptr[FGCharacterPlayer] = Cast[FGCharacterPlayer](ReturnValue)
        bSuccess: bool = Player
        if not bSuccess:
            goto('L601')
        ReturnValue_0: Ptr[FGInventoryComponent] = Player.GetInventory()
        ReturnValue_1: int32 = ReturnValue_0.GetNumItems(Desc_ResourceSinkCoupon)
        ReturnValue_2: FText = Default__KismetTextLibrary.Conv_IntToText(ReturnValue_1, False, True, 1, 324)
        FormatArgumentData.ArgumentName = "amount"
        FormatArgumentData.ArgumentValueType = 4
        FormatArgumentData.ArgumentValue = ReturnValue_2
        FormatArgumentData.ArgumentValueInt = 0
        FormatArgumentData.ArgumentValueFloat = 0
        FormatArgumentData.ArgumentValueGender = 0
        Array: List[FormatArgumentData] = [FormatArgumentData]
        ReturnValue_3: FText = Default__KismetTextLibrary.Format("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 535, 'Value': 'x{amount}'}", Array)
        self.mAmountOfCouponsText.SetText(ReturnValue_3)
    

    def ResetHeader(self):
        ReturnValue: float = self.mContentScrollBox.GetScrollOffset()
        ReturnValue_0: bool = ReturnValue > 0.10000000149011612
        if not ReturnValue_0:
            goto('L149')
        self.mContentScrollBox.ScrollToStart()
        self.OnScroll(0)
    

    def ListButtonOnClicked(self, index: int32, Button: Ptr[Widget_ListButton]):
        self.OnSchematicCategoryClicked(index)
    

    def DropInventorySlotStack(self):
        WasStackMoved = False
    

    def CheckItemsInCart(self):
        ExecutionFlow.Push("L662")
        Variable: int32 = 0
        Variable_0: int32 = 0
        
        # Label 51
        ReturnValue: int32 = len(self.mShopItemButtons)
        ReturnValue_0: bool = Variable <= ReturnValue
        if not ReturnValue_0:
           goto(ExecutionFlow.Pop())
        Variable_0 = Variable
        ExecutionFlow.Push("L588")
        
        Item = None
        Item = self.mShopItemButtons[Variable_0]
        ReturnValue_1: bool = Not_PreBool(Item.mIsAddedToCart)
        if not ReturnValue_1:
           goto(ExecutionFlow.Pop())
        
        Item = None
        Item = self.mShopItemButtons[Variable_0]
        
        Item.FGSchematic = None
        ReturnValue_2: bool = Default__BlueprintMapLibrary.Map_Contains(Ref[self.mCartItemStruct], Ref[Item.FGSchematic])
        Item.mIsAddedToCart = ReturnValue_2
        
        Item = None
        Item = self.mShopItemButtons[Variable_0]
        Item.UpdateButtonState()
        goto(ExecutionFlow.Pop())
        # Label 588
        ReturnValue_3: int32 = Variable + 1
        Variable = ReturnValue_3
        goto('L51')
    

    def UpdateShopButtonStates(self):
        ExecutionFlow.Push("L603")
        Variable: int32 = 0
        Variable_0: int32 = 0
        
        # Label 51
        ReturnValue: int32 = len(self.mShopItemButtons)
        ReturnValue_0: bool = Variable <= ReturnValue
        if not ReturnValue_0:
           goto(ExecutionFlow.Pop())
        Variable_0 = Variable
        ExecutionFlow.Push("L529")
        Keys: List[TSubclassOf[FGSchematic]] = []
        
        Default__BlueprintMapLibrary.Map_Keys(Ref[self.mCartItemStruct], Ref[Keys])
        
        Item = None
        Item = self.mShopItemButtons[Variable_0]
        
        Item.FGSchematic = None
        ReturnValue_1: bool = Default__KismetArrayLibrary.Array_Contains(Ref[Keys], Ref[Item.FGSchematic])
        Item.mIsAddedToCart = ReturnValue_1
        
        Item = None
        Item = self.mShopItemButtons[Variable_0]
        Item.UpdateButtonState()
        goto(ExecutionFlow.Pop())
        # Label 529
        ReturnValue_2: int32 = Variable + 1
        Variable = ReturnValue_2
        goto('L51')
    

    def SetInitialSelectedCategory(self):
        ExecutionFlow.Push("L695")
        ExecutionFlow.Push("L272")
        # Label 10
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        State: Ptr[FGPlayerState] = Cast[FGPlayerState](ReturnValue.PlayerState)
        bSuccess1: bool = State
        # Label 121
        if not bSuccess1:
           goto(ExecutionFlow.Pop())
        ReturnValue_0: TSubclassOf[FGSchematicCategory] = State.GetLastSelectedResourceSinkShopCategory()
        self.mSelectedSchematicCategory = ReturnValue_0
        ReturnValue_1: bool = Default__KismetSystemLibrary.IsValidClass(self.mSelectedSchematicCategory)
        if not ReturnValue_1:
            goto('L616')
        # Label 257
        self.PopulateShop()
        goto(ExecutionFlow.Pop())
        
        # Label 272
        ReturnValue_2: int32 = Default__KismetArrayLibrary.Array_Find(Ref[self.mAllSchematicCategories], Ref[self.mSelectedSchematicCategory])
        ReturnValue_3: bool = GreaterEqual_IntInt(ReturnValue_2, 0)
        # Label 374
        if not ReturnValue_3:
           goto(ExecutionFlow.Pop())
        
        ReturnValue_2 = Default__KismetArrayLibrary.Array_Find(Ref[self.mAllSchematicCategories], Ref[self.mSelectedSchematicCategory])
        ReturnValue_4: Ptr[Widget] = self.mCategoryContainer.GetChildAt(ReturnValue_2)
        Buttons: Ptr[BPW_ResourceSinkShop_CategoryButtons] = Cast[BPW_ResourceSinkShop_CategoryButtons](ReturnValue_4)
        bSuccess: bool = Buttons
        if not bSuccess:
           goto(ExecutionFlow.Pop())
        Buttons.SetIsSelected(True)
        goto(ExecutionFlow.Pop())
        
        Item = None
        # Label 616
        Item = self.mAllSchematicCategories[0]
        self.mSelectedSchematicCategory = Item
        goto('L257')
    

    def ChangeItemAmountInCart(self, schematic: TSubclassOf[FGSchematic], ItemAmount: int32):
        
        Value1 = None
        ReturnValue1: bool = Default__BlueprintMapLibrary.Map_Find(Ref[self.mCartItemStruct], Ref[schematic], Ref[Value1])
        Struct.mSchematic_2_F254EA0E48CE5A1D4DAD3296BA94D668 = Value1.mSchematic_2_F254EA0E48CE5A1D4DAD3296BA94D668
        Struct.mCartItemAmount_6_93629BD24F75478DFED5F086C5732798 = ItemAmount
        Struct.mIsAddedToWishlist_9_29588D2B45D70D08A8074F8ACB4F5B3A = Value1.mIsAddedToWishlist_9_29588D2B45D70D08A8074F8ACB4F5B3A
        
        Struct = None
        Default__BlueprintMapLibrary.Map_Add(Ref[self.mCartItemStruct], Ref[schematic], Ref[Struct])
        Keys: List[TSubclassOf[FGSchematic]] = []
        
        Default__BlueprintMapLibrary.Map_Keys(Ref[self.mCartItemStruct], Ref[Keys])
        
        ReturnValue: int32 = Default__KismetArrayLibrary.Array_Find(Ref[Keys], Ref[schematic])
        ReturnValue_0: Ptr[Widget] = self.mShoppingCartList.mCartList.mCartItemVerticalBox.GetChildAt(ReturnValue)
        Item: Ptr[BPW_ResourceSinkShop_CartItem] = Cast[BPW_ResourceSinkShop_CartItem](ReturnValue_0)
        bSuccess: bool = Item
        if not bSuccess:
            goto('L655')
        
        Value = None
        ReturnValue_1: bool = Default__BlueprintMapLibrary.Map_Find(Ref[self.mCartItemStruct], Ref[schematic], Ref[Value])
        Item.UpdateCartItem(Value)
    

    def UpdateCartAmount(self):
        self.AmountOverlay.SetVisibility(3)
        Values: List[ResourceSinkShop_CartItem_Struct] = []
        
        Default__BlueprintMapLibrary.Map_Values(Ref[self.mCartItemStruct], Ref[Values])
        
        ReturnValue: int32 = len(Values)
        localItemAmount = ReturnValue
        ReturnValue1: FText = Default__KismetTextLibrary.Conv_IntToText(localItemAmount, False, True, 1, 324)
        self.mAmountInShoppingCart.SetText(ReturnValue1)
        
        TotalCost = None
        self.GetTotalCost(Ref[TotalCost])
        ReturnValue_0: FText = Default__KismetTextLibrary.Conv_IntToText(TotalCost, False, True, 1, 324)
        self.mShoppingCartList.SetTotalCostText(ReturnValue_0)
        ReturnValue_1: bool = localItemAmount > 0
        if not ReturnValue_1:
            goto('L493')
        # End
        # Label 493
        self.AmountOverlay.SetVisibility(1)
    

    def GetTotalCost(self):
        ExecutionFlow.Push("L632")
        Values: List[ResourceSinkShop_CartItem_Struct] = []
        
        Default__BlueprintMapLibrary.Map_Values(Ref[self.mCartItemStruct], Ref[Values])
        Variable: int32 = 0
        Variable_0: int32 = 0
        
        # Label 112
        ReturnValue: int32 = len(Values)
        # Label 171
        ReturnValue_0: bool = Variable <= ReturnValue
        # Label 209
        if not ReturnValue_0:
            goto('L526')
        Variable_0 = Variable
        # Label 250
        ExecutionFlow.Push("L558")
        
        Item = None
        Item = Values[Variable_0]
        ReturnValue_1: List[ItemAmount] = Default__FGSchematic.GetCost(Item.mSchematic_2_F254EA0E48CE5A1D4DAD3296BA94D668)
        ReturnValue_2: int32 = ReturnValue_1[0].amount * Item.mCartItemAmount_6_93629BD24F75478DFED5F086C5732798
        ReturnValue1: int32 = localTotalCost + ReturnValue_2
        localTotalCost = ReturnValue1
        goto(ExecutionFlow.Pop())
        # Label 526
        totalCost = localTotalCost
        # End
        # Label 558
        ReturnValue_3: int32 = Variable + 1
        Variable = ReturnValue_3
        goto('L112')
    

    def OnBuyAll(self):
        ExecutionFlow.Push("L2241")
        ReturnValue: Ptr[Pawn] = self.GetOwningPlayerPawn()
        Player: Ptr[FGCharacterPlayer] = Cast[FGCharacterPlayer](ReturnValue)
        bSuccess1: bool = Player
        if not bSuccess1:
           goto(ExecutionFlow.Pop())
        ReturnValue_0: Ptr[FGInventoryComponent] = Player.GetInventory()
        localPlayerInventory = ReturnValue_0
        
        TotalCost = None
        self.GetTotalCost(Ref[TotalCost])
        ReturnValue_1: int32 = localPlayerInventory.GetNumItems(Desc_ResourceSinkCoupon)
        ReturnValue_2: bool = GreaterEqual_IntInt(ReturnValue_1, TotalCost)
        if not ReturnValue_2:
            goto('L1205')
        Keys: List[TSubclassOf[FGSchematic]] = []
        
        Default__BlueprintMapLibrary.Map_Keys(Ref[self.mCartItemStruct], Ref[Keys])
        Variable1: int32 = 0
        Variable: int32 = 0
        
        # Label 402
        ReturnValue_3: int32 = len(Keys)
        ReturnValue1: bool = Variable1 <= ReturnValue_3
        if not ReturnValue1:
            goto('L1242')
        Variable = Variable1
        ExecutionFlow.Push("L1558")
        Variable_0: bool = False
        Variable_1: int32 = 0
        Variable1_0: int32 = 0
        # Label 602
        ReturnValue_4: bool = Not_PreBool(Variable_0)
        
        Item = None
        # Label 631
        Item = Keys[Variable]
        ReturnValue_5: List[Ptr[FGUnlock]] = Default__FGSchematic.GetUnlocks(Item)
        
        ReturnValue1_0: int32 = len(ReturnValue_5)
        ReturnValue_6: bool = Variable_1 <= ReturnValue1_0
        ReturnValue_7: bool = ReturnValue_4 and ReturnValue_6
        if not ReturnValue_7:
            goto('L1632')
        Variable1_0 = Variable_1
        ExecutionFlow.Push("L2167")
        
        Item = None
        Item = Keys[Variable]
        ReturnValue_5 = Default__FGSchematic.GetUnlocks(Item)
        
        Item1 = None
        Item1 = ReturnValue_5[Variable1_0]
        Item: Ptr[FGUnlockGiveItem] = Cast[FGUnlockGiveItem](Item1)
        bSuccess: bool = Item
        if not bSuccess:
           goto(ExecutionFlow.Pop())
        localContaisGiveItemUnlock = True
        Variable_0 = True
        goto(ExecutionFlow.Pop())
        # Label 1205
        self.mShoppingCartList.PlayCantAffordAnim()
        goto(ExecutionFlow.Pop())
        # Label 1242
        ReturnValue_8: Ptr[PlayerController] = self.GetOwningPlayer()
        
        RCO = None
        Default__BPHUDHelpers.GetDefaultRCO(ReturnValue_8, self, Ref[RCO])
        
        RCO.Server_PurchaseResourceSinkSchematics(self.mResourceSinkShop, localPlayerInventory, Ref[SchematicsToPurchase])
        
        Default__BlueprintMapLibrary.Map_Clear(Ref[self.mCartItemStruct])
        self.UpdateShoppingCartList()
        self.UpdateCartAmount()
        self.mShoppingCartList.SetVisibility(1)
        if not localContaisGiveItemUnlock:
           goto(ExecutionFlow.Pop())
        self.Widget_SlidingTabs.SetActiveIndex(1, True)
        self.OnStorageOpened()
        goto(ExecutionFlow.Pop())
        # Label 1558
        ReturnValue2: int32 = Variable1 + 1
        Variable1 = ReturnValue2
        goto('L402')
        # Label 1632
        Variable_2: int32 = 0
        
        # Label 1655
        Item = Keys[Variable]
        
        Value = None
        ReturnValue_9: bool = Default__BlueprintMapLibrary.Map_Find(Ref[self.mCartItemStruct], Ref[Item], Ref[Value])
        ReturnValue_10: int32 = Value.mCartItemAmount_6_93629BD24F75478DFED5F086C5732798 - 1
        ReturnValue_11: bool = Variable_2 <= ReturnValue_10
        if not ReturnValue_11:
           goto(ExecutionFlow.Pop())
        ExecutionFlow.Push("L2093")
        
        Item = Keys[Variable]
        
        Value = None
        ReturnValue_9 = Default__BlueprintMapLibrary.Map_Find(Ref[self.mCartItemStruct], Ref[Item], Ref[Value])
        
        Value.mSchematic_2_F254EA0E48CE5A1D4DAD3296BA94D668 = None
        ReturnValue_12: int32 = SchematicsToPurchase.append(Value.mSchematic_2_F254EA0E48CE5A1D4DAD3296BA94D668)
        goto(ExecutionFlow.Pop())
        # Label 2093
        ReturnValue1_1: int32 = Variable_2 + 1
        Variable_2 = ReturnValue1_1
        goto('L1655')
        # Label 2167
        ReturnValue_13: int32 = Variable_1 + 1
        # Label 2209
        Variable_1 = ReturnValue_13
        goto('L602')
    

    def UpdateShoppingCartList(self):
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(self.mShoppingCartList)
        # Label 51
        if not ReturnValue:
            goto('L171')
        Values: List[ResourceSinkShop_CartItem_Struct] = []
        
        Default__BlueprintMapLibrary.Map_Values(Ref[self.mCartItemStruct], Ref[Values])
        
        self.mShoppingCartList.UpdateCartList(Ref[Values])
    

    def OnItemRemovedFromCart(self, mSchematic: TSubclassOf[FGSchematic]):
        
        ReturnValue: bool = Default__BlueprintMapLibrary.Map_Remove(Ref[self.mCartItemStruct], Ref[mSchematic])
        if not ReturnValue:
            goto('L174')
        self.UpdateShoppingCartList()
        self.UpdateCartAmount()
        self.mShoppingCartList.mCartList.UpdateEmptyCartFeedback()
        self.CheckItemsInCart()
    

    def OnMouseButtonDown(self):
        ReturnValue: bool = self.mShoppingCartList.IsHovered()
        ReturnValue_0: bool = Not_PreBool(ReturnValue)
        if not ReturnValue_0:
            goto('L209')
        self.mShoppingCartList.SetVisibility(1)
        ReturnValue1: EventReply = Default__WidgetBlueprintLibrary.Unhandled()
        ReturnValue_1: EventReply = ReturnValue1
        goto('L286')
        # Label 209
        ReturnValue_2: EventReply = Default__WidgetBlueprintLibrary.Unhandled()
        ReturnValue_1 = ReturnValue_2
    

    def FilterSchematicByCategory(self, mSchematic: TSubclassOf[FGSchematic], mSchematicCategory: TSubclassOf[FGSchematicCategory], mSchematicSubcategory: TSubclassOf[FGSchematicCategory]):
        
        Default__FGSchematic.GetSubCategories(mSchematic, Ref[localSubCategories])
        ReturnValue: TSubclassOf[FGSchematicCategory] = Default__FGSchematic.GetSchematicCategory(mSchematic)
        
        ReturnValue_0: bool = Default__KismetArrayLibrary.Array_Contains(Ref[localSubCategories], Ref[mSchematicSubcategory])
        ReturnValue_1: bool = EqualEqual_ClassClass(ReturnValue, mSchematicCategory)
        ReturnValue_2: bool = ReturnValue_1 and ReturnValue_0
        IsVisible = ReturnValue_2
    

    def OpenCartMenu(self):
        Values: List[ResourceSinkShop_CartItem_Struct] = []
        
        Default__BlueprintMapLibrary.Map_Values(Ref[self.mCartItemStruct], Ref[Values])
        
        self.mShoppingCartList.UpdateCartList(Ref[Values])
        self.mShoppingCartList.SetVisibility(0)
        
        TotalCost = None
        self.GetTotalCost(Ref[TotalCost])
        ReturnValue: FText = Default__KismetTextLibrary.Conv_IntToText(TotalCost, False, True, 1, 324)
        self.mShoppingCartList.SetTotalCostText(ReturnValue)
    

    def PopulateShop(self):
        ExecutionFlow.Push("L2418")
        
        Default__KismetArrayLibrary.Array_Clear(Ref[self.mShopItemButtons])
        self.mSubcategoryContainer.ClearChildren()
        ReturnValue1: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue1_0: Ptr[FGResourceSinkSubsystem] = Default__FGResourceSinkSubsystem.Get(ReturnValue1)
        
        Default__FGBlueprintFunctionLibrary.GetSubCategoriesForSchematicCategory(ReturnValue1_0, self.mSelectedSchematicCategory, Ref[localAllSubCategories])
        
        ReturnValue2: int32 = len(localAllSubCategories)
        ReturnValue: bool = ReturnValue2 <= 1
        localSingleSubcategory = ReturnValue
        Variable: int32 = 0
        Variable1: int32 = 0
        
        # Label 374
        ReturnValue1_1: int32 = len(localAllSubCategories)
        ReturnValue1_2: bool = Variable <= ReturnValue1_1
        if not ReturnValue1_2:
           goto(ExecutionFlow.Pop())
        Variable1 = Variable
        ExecutionFlow.Push("L2209")
        
        Item1 = None
        Item1 = localAllSubCategories[Variable1]
        # Label 572
        localSchematicSubcategory = Item1
        ReturnValue3: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue1_3: Ptr[BPW_ResourceSinkShop_Subcategory_Header] = Default__WidgetBlueprintLibrary.Create(self, BPW_ResourceSinkShop_Subcategory_Header, ReturnValue3)
        Default__KismetSystemLibrary.SetClassPropertyByName(ReturnValue1_3, "mSchematicSubcategory", localSchematicSubcategory)
        Default__KismetSystemLibrary.SetBoolPropertyByName(ReturnValue1_3, "mHideTitle", localSingleSubcategory)
        localSubCategoryHeader = ReturnValue1_3
        localShopItemContainer = ReturnValue1_3.mShopItemsContainer
        localShopItemContainer.ClearChildren()
        ReturnValue_0: Ptr[VerticalBoxSlot] = self.mSubcategoryContainer.AddChildToVerticalBox(localSubCategoryHeader)
        ReturnValue_0.SetVerticalAlignment(1)
        ReturnValue_1: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_2: Ptr[FGSchematicManager] = Default__FGSchematicManager.Get(ReturnValue_1)
        schematics: List[TSubclassOf[FGSchematic]] = []
        
        ReturnValue_2.GetAllSchematicsOfTypeFilteredOnDependency(7, Ref[schematics])
        Variable1_0: int32 = 0
        Variable_0: int32 = 0
        
        # Label 1158
        ReturnValue_3: int32 = len(schematics)
        ReturnValue_4: bool = Variable1_0 <= ReturnValue_3
        if not ReturnValue_4:
            goto('L2283')
        Variable_0 = Variable1_0
        ExecutionFlow.Push("L2344")
        
        Item = None
        Item = schematics[Variable_0]
        localSchematic = Item
        
        isVisible = None
        self.FilterSchematicByCategory(localSchematic, self.mSelectedSchematicCategory, localSchematicSubcategory, Ref[isVisible])
        if not isVisible:
           goto(ExecutionFlow.Pop())
        Keys: List[TSubclassOf[FGSchematic]] = []
        
        Default__BlueprintMapLibrary.Map_Keys(Ref[self.mCartItemStruct], Ref[Keys])
        ReturnValue2_0: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_5: Ptr[BPW_ResourceSinkShop_Item] = Default__WidgetBlueprintLibrary.Create(self, BPW_ResourceSinkShop_Item, ReturnValue2_0)
        Default__KismetSystemLibrary.SetClassPropertyByName(ReturnValue_5, "FGSchematic", localSchematic)
        ReturnValue_6: List[ItemAmount] = Default__FGSchematic.GetCost(localSchematic)
        Default__KismetSystemLibrary.SetIntPropertyByName(ReturnValue_5, "mSchematicCost", ReturnValue_6[0].amount)
        
        ReturnValue_7: bool = Default__KismetArrayLibrary.Array_Contains(Ref[Keys], Ref[localSchematic])
        Default__KismetSystemLibrary.SetBoolPropertyByName(ReturnValue_5, "mIsAddedToCart", ReturnValue_7)
        localResourceSinkItemWidget = ReturnValue_5
        
        ReturnValue_8: int32 = self.mShopItemButtons.append(localResourceSinkItemWidget)
        ReturnValue_9: Ptr[WrapBoxSlot] = localShopItemContainer.AddChildToWrapBox(localResourceSinkItemWidget)
        ReturnValue_9.SetHorizontalAlignment(2)
        OutputDelegate1.BindUFunction(self, OnShopSchematicClicked)
        localResourceSinkItemWidget.OnShopItemClicked.AddUnique(OutputDelegate1)
        OutputDelegate.BindUFunction(self, OnShopSchematicClicked)
        # Label 2167
        localResourceSinkItemWidget.OnBuyButtonClicked.AddUnique(OutputDelegate)
        goto(ExecutionFlow.Pop())
        # Label 2209
        ReturnValue_10: int32 = Variable + 1
        Variable = ReturnValue_10
        goto('L374')
        # Label 2283
        ReturnValue_11: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.FadeInCategory, 0, 1, 0, 1)
        self.ResetHeader()
        goto(ExecutionFlow.Pop())
        # Label 2344
        ReturnValue1_4: int32 = Variable1_0 + 1
        Variable1_0 = ReturnValue1_4
        goto('L1158')
    

    def OnSchematicCategoryClicked(self, index: int32):
        
        Item = None
        Item = self.mAllSchematicCategories[index]
        ReturnValue: bool = NotEqual_ClassClass(self.mSelectedSchematicCategory, Item)
        if not ReturnValue:
            goto('L618')
        
        ReturnValue_0: int32 = Default__KismetArrayLibrary.Array_Find(Ref[self.mAllSchematicCategories], Ref[self.mSelectedSchematicCategory])
        ReturnValue_1: Ptr[Widget] = self.mCategoryContainer.GetChildAt(ReturnValue_0)
        Buttons: Ptr[BPW_ResourceSinkShop_CategoryButtons] = Cast[BPW_ResourceSinkShop_CategoryButtons](ReturnValue_1)
        bSuccess: bool = Buttons
        if not bSuccess:
            goto('L618')
        Buttons.SetIsSelected(False)
        
        Item = None
        Item = self.mAllSchematicCategories[index]
        self.mSelectedSchematicCategory = Item
        ReturnValue_2: Ptr[PlayerController] = self.GetOwningPlayer()
        State: Ptr[FGPlayerState] = Cast[FGPlayerState](ReturnValue_2.PlayerState)
        bSuccess1: bool = State
        if not bSuccess1:
            goto('L618')
        State.SetLastSelectedResourceSinkShopCategory(self.mSelectedSchematicCategory)
        self.PopulateShop()
        self.UpdateBanner()
    

    def CreateCategoryButtons(self):
        ExecutionFlow.Push("L1357")
        ReturnValue1: Ptr[PlayerController] = self.GetOwningPlayer()
        # Label 29
        ReturnValue: Ptr[FGSchematicManager] = Default__FGSchematicManager.Get(ReturnValue1)
        schematics: List[TSubclassOf[FGSchematic]] = []
        
        # Label 91
        ReturnValue.GetAllSchematicsOfTypeFilteredOnDependency(7, Ref[schematics])
        Variable: int32 = 0
        Variable1: int32 = 0
        
        # Label 180
        ReturnValue1_0: int32 = len(schematics)
        ReturnValue1_1: bool = Variable <= ReturnValue1_0
        if not ReturnValue1_1:
            goto('L502')
        Variable1 = Variable
        ExecutionFlow.Push("L1283")
        
        Item1 = None
        Item1 = schematics[Variable1]
        ReturnValue_0: TSubclassOf[FGSchematicCategory] = Default__FGSchematic.GetSchematicCategory(Item1)
        
        ReturnValue_1: int32 = Default__KismetArrayLibrary.Array_AddUnique(Ref[self.mAllSchematicCategories], Ref[ReturnValue_0])
        goto(ExecutionFlow.Pop())
        # Label 502
        Variable1_0: int32 = 0
        Variable_0: int32 = 0
        
        # Label 548
        ReturnValue_2: int32 = len(self.mAllSchematicCategories)
        ReturnValue_3: bool = Variable1_0 <= ReturnValue_2
        if not ReturnValue_3:
           goto(ExecutionFlow.Pop())
        # Label 655
        Variable_0 = Variable1_0
        ExecutionFlow.Push("L1209")
        
        Item = None
        Item = self.mAllSchematicCategories[Variable_0]
        localSchematicCategory = Item
        ReturnValue_4: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_5: Ptr[BPW_ResourceSinkShop_CategoryButtons] = Default__WidgetBlueprintLibrary.Create(self, BPW_ResourceSinkShop_CategoryButtons, ReturnValue_4)
        ReturnValue_6: FText = Default__FGSchematicCategory.GetCategoryName(localSchematicCategory)
        
        Default__KismetSystemLibrary.SetTextPropertyByName(ReturnValue_5, "mName", Ref[ReturnValue_6])
        CategoryButton = ReturnValue_5
        ReturnValue_7: Ptr[HorizontalBoxSlot] = self.mCategoryContainer.AddChildToHorizontalBox(CategoryButton)
        SlateChildSize.Value = 1
        SlateChildSize.SizeRule = 1
        ReturnValue_7.SetSize(SlateChildSize)
        OutputDelegate.BindUFunction(self, OnSchematicCategoryClicked)
        CategoryButton.OnClicked.AddUnique(OutputDelegate)
        goto(ExecutionFlow.Pop())
        # Label 1209
        ReturnValue1_2: int32 = Variable1_0 + 1
        Variable1_0 = ReturnValue1_2
        goto('L548')
        # Label 1283
        ReturnValue_8: int32 = Variable + 1
        Variable = ReturnValue_8
        goto('L180')
    

    def OnShopSchematicHovered(self, mSchematic: TSubclassOf[FGSchematic], mButton: Ptr[BPW_ResourceSinkShop_Item]):
        self.mHoveredButton = mButton
        self.mHoveredSchematic = mSchematic
    

    def OnShopSchematicClicked(self, schematic: TSubclassOf[FGSchematic]):
        ReturnValue: bool = Default__FGSchematic.IsRepeatPurchasesAllowed(schematic)
        # Label 51
        ReturnValue_0: bool = Not_PreBool(ReturnValue)
        
        ReturnValue_1: bool = Default__BlueprintMapLibrary.Map_Contains(Ref[self.mCartItemStruct], Ref[schematic])
        ReturnValue_2: bool = ReturnValue_1 and ReturnValue_0
        ReturnValue1: bool = Not_PreBool(ReturnValue_2)
        if not ReturnValue1:
            goto('L572')
        
        Value = None
        ReturnValue_3: bool = Default__BlueprintMapLibrary.Map_Find(Ref[self.mCartItemStruct], Ref[schematic], Ref[Value])
        ReturnValue_4: int32 = Value.mCartItemAmount_6_93629BD24F75478DFED5F086C5732798 + 1
        Struct.mSchematic_2_F254EA0E48CE5A1D4DAD3296BA94D668 = schematic
        Struct.mCartItemAmount_6_93629BD24F75478DFED5F086C5732798 = ReturnValue_4
        Struct.mIsAddedToWishlist_9_29588D2B45D70D08A8074F8ACB4F5B3A = False
        
        Struct = None
        Default__BlueprintMapLibrary.Map_Add(Ref[self.mCartItemStruct], Ref[schematic], Ref[Struct])
        self.UpdateShoppingCartList()
        self.UpdateCartAmount()
        self.CheckItemsInCart()
        # Label 526
        ReturnValue_5: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.AddedToCart, 0, 1, 0, 1)
    

    def BndEvt__mWindow_K2Node_ComponentBoundEvent_0_OnClose__DelegateSignature(self):
        self.ExecuteUbergraph_BPW_ResourceSinkShop(218)
    

    def Construct(self):
        self.ExecuteUbergraph_BPW_ResourceSinkShop(237)
    

    def BndEvt__mShoppingCartList_K2Node_ComponentBoundEvent_9_OnBuyAllButtonClicked__DelegateSignature(self):
        self.ExecuteUbergraph_BPW_ResourceSinkShop(1123)
    

    def BndEvt__mShoppingCartList_K2Node_ComponentBoundEvent_10_OnItemAmountChangedInCart__DelegateSignature(self, schematic: TSubclassOf[FGSchematic], amount: int32):
        ExecuteUbergraph_BPW_ResourceSinkShop.K2Node_ComponentBoundEvent_Schematic = schematic #  PERSISTENT_FRAME(
        ExecuteUbergraph_BPW_ResourceSinkShop.K2Node_ComponentBoundEvent_Amount = amount #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BPW_ResourceSinkShop(1519)
    

    def BndEvt__mShoppingCartList_K2Node_ComponentBoundEvent_11_OnItemRemovedFromCart__DelegateSignature(self, mSchematic: TSubclassOf[FGSchematic]):
        ExecuteUbergraph_BPW_ResourceSinkShop.K2Node_ComponentBoundEvent_mSchematic = mSchematic #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BPW_ResourceSinkShop(1720)
    

    def BndEvt__mWindow_K2Node_ComponentBoundEvent_5_OnTabButtonClicked__DelegateSignature(self, ButtonIndex: int32):
        ExecuteUbergraph_BPW_ResourceSinkShop.K2Node_ComponentBoundEvent_ButtonIndex = ButtonIndex #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BPW_ResourceSinkShop(1854)
    

    def BndEvt__mCart_Button_K2Node_ComponentBoundEvent_6_OnButtonClickedEvent__DelegateSignature(self):
        self.ExecuteUbergraph_BPW_ResourceSinkShop(1964)
    

    def OnScroll(self, CurrentOffset: float):
        ExecuteUbergraph_BPW_ResourceSinkShop.K2Node_CustomEvent_CurrentOffset = CurrentOffset #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BPW_ResourceSinkShop(1969)
    

    def ExecuteUbergraph_BPW_ResourceSinkShop(self):
        # Label 10
        self.UpdateShopButtonStates()
        # End
        # Label 29
        Variable: bool = False
        ReturnValue: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.MinimizeHeader, 0, 1, 0, 1)
        # End
        # Label 91
        Variable1: bool = False
        if not Variable:
            goto('L121')
        # End
        # Label 121
        Variable = True
        ReturnValue1: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.MinimizeHeader, 0, 1, 1, 1)
        # End
        # Label 183
        if not Variable1:
            goto('L202')
        # End
        # Label 202
        Variable1 = True
        goto('L29')
        self.OnEscapePressed()
        # End
        Shop: Ptr[FGBuildableResourceSinkShop] = Cast[FGBuildableResourceSinkShop](self.mInteractObject)
        bSuccess: bool = Shop
        self.mResourceSinkShop = Shop
        self.CreateCategoryButtons()
        ReturnValue_0: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_1: Vector2D = Default__WidgetLayoutLibrary.GetViewportSize(self)
        
        X = None
        Y = None
        BreakVector2D(ReturnValue_1, Ref[X], Ref[Y])
        ReturnValue_2: float = Y / 2
        ReturnValue1_0: float = X / 2
        ReturnValue_3: int32 = FTrunc(ReturnValue_2)
        ReturnValue1_1: int32 = FTrunc(ReturnValue1_0)
        ReturnValue_0.SetMouseLocation(ReturnValue1_1, ReturnValue_3)
        # Label 655
        self.bIsFocusable = True
        self.SetInitialSelectedCategory()
        self.mWindow.SetInventoryVisibility(False, False)
        self.GetAmountOfCouponsInPlayerInventory()
        OutputDelegate.BindUFunction(self, OnScroll)
        self.mContentScrollBox.OnUserScrolled.AddUnique(OutputDelegate)
        self.UpdateBanner()
        # End
        # Label 815
        ReturnValue_4: bool = CurrentOffset > 0.20000000298023224
        if not ReturnValue_4:
            goto('L91')
        goto('L183')
        # Label 868
        Values: List[ResourceSinkShop_CartItem_Struct] = []
        
        Default__BlueprintMapLibrary.Map_Values(Ref[self.mCartItemStruct], Ref[Values])
        
        self.mShoppingCartList.SetBuyButtonVisibility(Ref[Values])
        self.mShoppingCartList.mCartList.UpdateEmptyCartFeedback()
        # End
        # Label 1037
        self.mShoppingCartList.SetVisibility(1)
        # End
        # Label 1080
        self.mShoppingCartList.SetVisibility(0)
        goto('L868')
        self.OnBuyAll()
        self.UpdateShopButtonStates()
        self.mShoppingCartList.mCartList.UpdateEmptyCartFeedback()
        # Label 1209
        Values2: List[ResourceSinkShop_CartItem_Struct] = []
        
        Default__BlueprintMapLibrary.Map_Values(Ref[self.mCartItemStruct], Ref[Values2])
        
        self.mShoppingCartList.SetBuyButtonVisibility(Ref[Values2])
        self.GetAmountOfCouponsInPlayerInventory()
        ReturnValue1_2: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_5: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_Shop_SpaceCashier, ReturnValue1_2, True)
        # End
        # Label 1419
        ReturnValue_6: uint8 = self.mShoppingCartList.GetVisibility()
        ReturnValue_7: bool = EqualEqual_ByteByte(ReturnValue_6, 0)
        if not ReturnValue_7:
            goto('L1080')
        goto('L1037')
        self.ChangeItemAmountInCart(Schematic, Amount)
        self.mShoppingCartList.mCartList.UpdateEmptyCartFeedback()
        Values3: List[ResourceSinkShop_CartItem_Struct] = []
        
        Default__BlueprintMapLibrary.Map_Values(Ref[self.mCartItemStruct], Ref[Values3])
        
        self.mShoppingCartList.SetBuyButtonVisibility(Ref[Values3])
        # End
        self.OnItemRemovedFromCart(mSchematic)
        Values1: List[ResourceSinkShop_CartItem_Struct] = []
        
        Default__BlueprintMapLibrary.Map_Values(Ref[self.mCartItemStruct], Ref[Values1])
        
        self.mShoppingCartList.SetBuyButtonVisibility(Ref[Values1])
        goto('L10')
        ReturnValue_8: bool = EqualEqual_IntInt(ButtonIndex, 1)
        if not ReturnValue_8:
            goto('L1921')
        self.OnStorageOpened()
        # End
        # Label 1921
        self.mWindow.SetInventoryVisibility(False, True)
        # End
        goto('L1419')
        goto('L815')
    
