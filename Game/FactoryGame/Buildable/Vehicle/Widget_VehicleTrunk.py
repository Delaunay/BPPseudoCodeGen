
from codegen.ue4_stub import *

from Game.FactoryGame.Character.Player.BP_RemoteCallObject import BP_RemoteCallObject
from Script.Engine import Default__KismetInputLibrary
from Script.FactoryGame import FGPlayerController
from Script.FactoryGame import FGCharacterPlayer
from Script.UMG import SetPadding
from Script.Engine import Pawn
from Script.InputCore import Key
from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import PlayerController
from Script.Engine import Default__KismetArrayLibrary
from Script.Engine import K2_GetPawn
from Script.UMG import Unhandled
from Script.FactoryGame import GetInventory
from Game.FactoryGame.Interface.UI.InGame.Widget_UseableBase import Construct
from Game.FactoryGame.Resource.Parts.Fuel.Desc_Fuel import Desc_Fuel
from Script.FactoryGame import FGInventoryComponent
from Script.Engine import IsValid
from Script.UMG import Default__WidgetBlueprintLibrary
from Script.FactoryGame import FGVehicle
from Game.FactoryGame.Buildable.-Shared.Widgets.Widget_ImageTabButton import Widget_ImageTabButton
from Game.FactoryGame.Interface.UI.InGame.Widget_UseableBase import Widget_UseableBase
from Script.FactoryGame import Init
from Game.FactoryGame.Buildable.Vehicle.BP_WheeledVehicle import BP_WheeledVehicle
from Game.FactoryGame.Buildable.Vehicle.Widget_VehicleTrunk import ExecuteUbergraph_Widget_VehicleTrunk.K2Node_ComponentBoundEvent_RelevantClasses
from Script.Engine import GetKey
from Game.FactoryGame.Buildable.Vehicle.Widget_VehicleTrunk import ExecuteUbergraph_Widget_VehicleTrunk.K2Node_ComponentBoundEvent_ButtonIndex
from Script.Engine import EqualEqual_KeyKey
from Script.FactoryGame import SetDesiredHorizontalAlignment
from Script.UMG import ScrollToStart
from Script.FactoryGame import GetRemoteCallObjectOfClass
from Script.UMG import GetOwningPlayerPawn
from Game.FactoryGame.Interface.UI.HUDHelpers.HUDHelpers import Default__HUDHelpers
from Script.UMG import HasAnyChildren
from Game.FactoryGame.Interface.UI.InGame.Widget_UseableBase import Destruct
from Script.FactoryGame import FGItemDescriptor
from Script.FactoryGame import GetFuelInventory
from Game.FactoryGame.Buildable.Vehicle.Widget_VehicleTrunk import ExecuteUbergraph_Widget_VehicleTrunk
from Script.FactoryGame import GetStorageInventory
from Game.FactoryGame.Interface.UI.BPI_GameUI import BPI_GameUI
from Game.FactoryGame.Interface.UI.InGame.ShoppingList.Widget_ShoppingList import Widget_ShoppingList
from Script.UMG import EventReply

class Widget_VehicleTrunk(Widget_UseableBase):
    mOwningVehicle: Ptr[BP_WheeledVehicle]
    mActiveTab: Ptr[Widget_ImageTabButton]
    mFuelComponent: Ptr[FGInventoryComponent]
    mCraftBenchRelevantClasses: List[TSubclassOf[FGItemDescriptor]]
    mShouldOpenInventory = True
    mUseKeyboard = True
    mUseMouse = True
    mCaptureInput = True
    mRestoreFocusWhenLost = True
    mInputToPassThrough = ['Use']
    mDesiredHorizontalAlignment = 2
    mDesiredVerticalAlignment = 2
    mUseGamepadCursor = True
    mCallCustomTickOnConstruct = True
    
    def UpdateRelevantClasses(self):
        Array: Const[List[TSubclassOf[FGItemDescriptor]]] = [Desc_Fuel]
        Variable: int32 = self.Widget_Window_DarkMode.Widget_TabsContainer.mSlidingTabsWidget.mActiveIndex
        
        switch = {
            0: self.mCraftBenchRelevantClasses,
            1: Array
        }
        
        switch.get(Variable, None) = None
        self.Widget_Window_DarkMode.SetupRelevantInventory(Ref[switch.get(Variable, None)])
    

    def OnPreviewKeyDown(self):
        
        ReturnValue: Key = Default__KismetInputLibrary.GetKey(Ref[InKeyEvent])
        ReturnValue_0: bool = Default__KismetInputLibrary.EqualEqual_KeyKey(ReturnValue, Key(KeyName = "SpaceBar"))
        if not ReturnValue_0:
            goto('L187')
        self.mManualManufacturerWidget.SpaceBarOverride()
        # Label 187
        ReturnValue_1: EventReply = Default__WidgetBlueprintLibrary.Unhandled()
        ReturnValue_2: EventReply = ReturnValue_1
    

    def SetTitle(self):
        AsFGVehicle: Ptr[FGVehicle] = Cast[FGVehicle](self.mInteractObject)
        bSuccess: bool = AsFGVehicle
        if not bSuccess:
            goto('L146')
        self.Widget_Window_DarkMode.SetTitle(AsFGVehicle.mDisplayName)
    

    def InitCallbacks(self):
        ExecutionFlow.Push("L668")
        OutputDelegate3.BindUFunction(self, OnInventorySlotStackMove)
        self.mFuelSlot.OnMoveStack.AddUnique(OutputDelegate3)
        Variable: int32 = 0
        Variable_0: int32 = 0
        
        self.mVehicleStorageWidget.mInventorySlots = None
        # Label 115
        ReturnValue: int32 = len(self.mVehicleStorageWidget.mInventorySlots)
        ReturnValue_0: bool = Variable <= ReturnValue
        # Label 234
        if not ReturnValue_0:
           goto(ExecutionFlow.Pop())
        Variable_0 = Variable
        ExecutionFlow.Push("L594")
        OutputDelegate2.BindUFunction(self, OnInventorySlotStackMove)
        
        self.mVehicleStorageWidget.mInventorySlots = None
        Item = None
        Item = self.mVehicleStorageWidget.mInventorySlots[Variable_0]
        Item.OnMoveStack.AddUnique(OutputDelegate2)
        OutputDelegate.BindUFunction(self, StoreAllInVehicleStorage)
        self.mDumpAllButton.mButton.OnClicked.AddUnique(OutputDelegate)
        OutputDelegate1.BindUFunction(self, GrabAllFromVehicleStorage)
        self.mGrabAllButton.mButton.OnClicked.AddUnique(OutputDelegate1)
        goto(ExecutionFlow.Pop())
        # Label 594
        ReturnValue_1: int32 = Variable + 1
        Variable = ReturnValue_1
        goto('L115')
    

    def DropInventorySlotStack(self):
        ExecutionFlow.Push("L423")
        CmpSuccess: bool = self.Widget_Window_DarkMode.Widget_TabsContainer.mSlidingTabsWidget.mActiveIndex != 0
        if not CmpSuccess:
            goto('L234')
        CmpSuccess = self.Widget_Window_DarkMode.Widget_TabsContainer.mSlidingTabsWidget.mActiveIndex != 1
        if not CmpSuccess:
            goto('L250')
        goto(ExecutionFlow.Pop())
        # Label 234
        WasStackMoved = False
        # End
        # Label 250
        ExecutionFlow.Push("L404")
        
        Result = None
        self.mFuelSlot.DropOntoInventorySlot(InventorySlot, Ref[Result])
        LocalResult = Result
        if not LocalResult:
            goto('L343')
        goto(ExecutionFlow.Pop())
        
        Result = None
        # Label 343
        self.DropInventoryStackOnInventoryWidget(InventorySlot, self.mVehicleStorageWidget, Ref[Result])
        LocalResult = Result
        goto(ExecutionFlow.Pop())
        # Label 404
        WasStackMoved = LocalResult
    

    def SetWindowAlignment(self):
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        
        gameUI = None
        Default__HUDHelpers.GetFGGameUI(ReturnValue, self, Ref[gameUI])
        UI: TScriptInterface[BPI_GameUI] = QueryInterface[BPI_GameUI](gameUI)
        # Label 115
        bSuccess: bool = UI
        if not bSuccess:
            goto('L468')
        
        shoppingList = None
        GetInterfaceUObject(UI).GetShoppingList(Ref[shoppingList])
        # Label 204
        ReturnValue_0: bool = shoppingList.mShoppingListIngredientContainer.HasAnyChildren()
        # Label 268
        if not ReturnValue_0:
            goto('L484')
        self.SetDesiredHorizontalAlignment(1)
        Margin1.Left = 128
        Margin1.Top = 0
        Margin1.Right = 0
        Margin1.Bottom = 0
        self.Widget_Window_DarkMode.SetPadding(Margin1)
        # End
        # Label 468
        shoppingList: Ptr[Widget_ShoppingList] = None
        goto('L204')
        # Label 484
        self.SetDesiredHorizontalAlignment(2)
        Margin.Left = 0
        Margin.Top = 0
        Margin.Right = 0
        Margin.Bottom = 0
        self.Widget_Window_DarkMode.SetPadding(Margin)
    

    def CloseVehicle(self):
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(self.mOwningVehicle)
        if not ReturnValue:
            goto('L372')
        ReturnValue_0: Ptr[Pawn] = self.GetOwningPlayerPawn()
        Player: Ptr[FGCharacterPlayer] = Cast[FGCharacterPlayer](ReturnValue_0)
        bSuccess1: bool = Player
        if not bSuccess1:
            goto('L372')
        ReturnValue_1: Ptr[PlayerController] = self.GetOwningPlayer()
        Controller: Ptr[FGPlayerController] = Cast[FGPlayerController](ReturnValue_1)
        bSuccess: bool = Controller
        if not bSuccess:
            goto('L372')
        ReturnValue_2: Ptr[BP_RemoteCallObject] = Controller.GetRemoteCallObjectOfClass(BP_RemoteCallObject)
        ReturnValue_2.ServerCloseVehicleTrunk(self.mOwningVehicle, Player)
    

    def Cleanup(self):
        self.CloseVehicle()
        self.mManualManufacturerWidget.Cleanup()
        self.Widget_Window_DarkMode.OnClose.Clear()
    

    def Destruct(self):
        self.ExecuteUbergraph_Widget_VehicleTrunk(1304)
    

    def Init(self):
        self.ExecuteUbergraph_Widget_VehicleTrunk(1299)
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_VehicleTrunk(860)
    

    def GrabAllFromVehicleStorage(self):
        self.ExecuteUbergraph_Widget_VehicleTrunk(1728)
    

    def StoreAllInVehicleStorage(self):
        self.ExecuteUbergraph_Widget_VehicleTrunk(1733)
    

    def BndEvt__mSortButton_K2Node_ComponentBoundEvent_0_OnClicked__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_VehicleTrunk(1738)
    

    def BndEvt__Widget_Window_DarkMode_K2Node_ComponentBoundEvent_1_OnTabButtonClicked__DelegateSignature(self, ButtonIndex: int32):
        ExecuteUbergraph_Widget_VehicleTrunk.K2Node_ComponentBoundEvent_ButtonIndex = ButtonIndex #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_VehicleTrunk(2018)
    

    def BndEvt__mManualManufacturerWidget_K2Node_ComponentBoundEvent_2_OnRelevantClassesUpdated__DelegateSignature(self, relevantClasses: Ref[List[TSubclassOf[FGItemDescriptor]]]):
        ExecuteUbergraph_Widget_VehicleTrunk.K2Node_ComponentBoundEvent_RelevantClasses = relevantClasses #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_VehicleTrunk(2037)
    

    def ExecuteUbergraph_Widget_VehicleTrunk(self):
        # Label 10
        self.UpdateRelevantClasses()
        # End
        # Label 29
        self.Construct()
        self.Widget_SlidingTabs.SetActiveIndex(1, False)
        self.SetTitle()
        OutputDelegate.BindUFunction(self, OnEscapePressed)
        self.Widget_Window_DarkMode.OnClose.AddUnique(OutputDelegate)
        self.SetWindowAlignment()
        
        self.Widget_InventorySlot_DropArea.mInventorySlots = None
        self.mFuelSlot = None
        ReturnValue: int32 = self.Widget_InventorySlot_DropArea.mInventorySlots.append(self.mFuelSlot)
        # End
        # Label 268
        self.Cleanup()
        # End
        # Label 287
        self.Destruct()
        goto('L268')
        # Label 302
        ReturnValue_0: bool = Default__KismetSystemLibrary.IsValid(self.mOwningVehicle)
        if not ReturnValue_0:
            goto('L2069')
        ReturnValue_1: Ptr[FGInventoryComponent] = self.mOwningVehicle.GetStorageInventory()
        self.mVehicleStorageWidget.Init(ReturnValue_1)
        ReturnValue_2: Ptr[FGInventoryComponent] = self.mOwningVehicle.GetFuelInventory()
        self.mFuelSlot.mCachedInventoryComponent = ReturnValue_2
        self.InitCallbacks()
        self.Widget_Window_DarkMode.SetTitle(self.mOwningVehicle.mDisplayName)
        self.Widget_Window_DarkMode.SetInventoryVisibility(True, False)
        self.UpdateRelevantClasses()
        # End
        # Label 675
        Vehicle: Ptr[BP_WheeledVehicle] = Cast[BP_WheeledVehicle](self.mInteractObject)
        bSuccess: bool = Vehicle
        if not bSuccess:
            goto('L2069')
        self.mOwningVehicle = Vehicle
        goto('L302')
        # Label 778
        self.mManualManufacturerWidget.mInteractObject = self.mInteractObject
        self.mManualManufacturerWidget.Init()
        goto('L675')
        goto('L29')
        # Label 865
        ReturnValue_3: Ptr[PlayerController] = self.GetOwningPlayer()
        Controller: Ptr[FGPlayerController] = Cast[FGPlayerController](ReturnValue_3)
        bSuccess1: bool = Controller
        if not bSuccess1:
            goto('L2069')
        ReturnValue_4: Ptr[Pawn] = Controller.K2_GetPawn()
        Player: Ptr[FGCharacterPlayer] = Cast[FGCharacterPlayer](ReturnValue_4)
        bSuccess2: bool = Player
        if not bSuccess2:
            goto('L2069')
        ReturnValue_5: Ptr[BP_RemoteCallObject] = Controller.GetRemoteCallObjectOfClass(BP_RemoteCallObject)
        ReturnValue1: Ptr[FGInventoryComponent] = self.mOwningVehicle.GetStorageInventory()
        ReturnValue_6: Ptr[FGInventoryComponent] = Player.GetInventory()
        ReturnValue_5.Server_GrabAllItemsFromInventory(ReturnValue1, ReturnValue_6, None)
        # End
        # Label 1284
        self.Init()
        goto('L778')
        goto('L1284')
        goto('L287')
        # Label 1309
        ReturnValue1_0: Ptr[PlayerController] = self.GetOwningPlayer()
        Controller1: Ptr[FGPlayerController] = Cast[FGPlayerController](ReturnValue1_0)
        bSuccess3: bool = Controller1
        if not bSuccess3:
            goto('L2069')
        ReturnValue1_1: Ptr[Pawn] = Controller1.K2_GetPawn()
        Player1: Ptr[FGCharacterPlayer] = Cast[FGCharacterPlayer](ReturnValue1_1)
        bSuccess4: bool = Player1
        if not bSuccess4:
            goto('L2069')
        ReturnValue2: Ptr[FGInventoryComponent] = self.mOwningVehicle.GetStorageInventory()
        ReturnValue1_2: Ptr[BP_RemoteCallObject] = Controller1.GetRemoteCallObjectOfClass(BP_RemoteCallObject)
        ReturnValue1_3: Ptr[FGInventoryComponent] = Player1.GetInventory()
        ReturnValue1_2.Server_GrabAllItemsFromInventory(ReturnValue1_3, ReturnValue2, None)
        # End
        goto('L865')
        goto('L1309')
        ReturnValue2_0: Ptr[PlayerController] = self.GetOwningPlayer()
        Controller2: Ptr[FGPlayerController] = Cast[FGPlayerController](ReturnValue2_0)
        bSuccess5: bool = Controller2
        if not bSuccess5:
            goto('L2069')
        ReturnValue2_1: Ptr[BP_RemoteCallObject] = Controller2.GetRemoteCallObjectOfClass(BP_RemoteCallObject)
        ReturnValue2_1.Server_SortInventory(self.mVehicleStorageWidget.mInventoryComponent)
        self.Widget_Scrollbox.mScrollBox.ScrollToStart()
        # End
        self.UpdateRelevantClasses()
        # End
        self.mCraftBenchRelevantClasses = RelevantClasses
        goto('L10')
    
