
from codegen.ue4_stub import *

from Script.UMG import RemoveChildAt
from Script.FactoryGame import FGCharacterPlayer
from Script.Engine import SetObjectPropertyByName
from Script.Engine import Pawn
from Game.FactoryGame.Character.Player.Widget_PlayerInventoryAddon import ExecuteUbergraph_Widget_PlayerInventoryAddon.K2Node_Event_IsDesignTime
from Script.UMG import GetChildrenCount
from Script.UMG import PanelSlot
from Script.UMG import AddChild
from Script.Engine import Default__KismetSystemLibrary
from Script.UMG import GetChildAt
from Script.Engine import PlayerController
from Script.Engine import Default__KismetArrayLibrary
from Script.UMG import ESlateVisibility
from Script.FactoryGame import GetInventory
from Script.FactoryGame import SortInventory
from Script.FactoryGame import FGInventoryComponent
from Script.Engine import IsValid
from Game.FactoryGame.Interface.UI.InGame.InventorySlots.Widget_InventorySlot import Widget_InventorySlot
from Script.UMG import Default__WidgetBlueprintLibrary
from Script.UMG import SetColorAndOpacity
from Script.Engine import ClassIsChildOf
from Script.Engine import EqualEqual_IntInt
from Script.FactoryGame import FGInteractWidget
from Script.UMG import Construct
from Script.UMG import Widget
from Script.CoreUObject import LinearColor
from Game.FactoryGame.Character.Player.Widget_PlayerInventoryAddon import ExecuteUbergraph_Widget_PlayerInventoryAddon.K2Node_CustomEvent_itemClass
from Script.Engine import SetIntPropertyByName
from Script.FactoryGame import GetRelevantStackIndexes
from Game.FactoryGame.Character.Player.Widget_PlayerInventoryAddon import ExecuteUbergraph_Widget_PlayerInventoryAddon
from Script.UMG import GetOwningPlayerPawn
from Script.UMG import HasAnyChildren
from Script.UMG import Create
from Script.FactoryGame import FGItemDescriptor
from Script.FactoryGame import GetTrashSlot
from Script.Engine import PrintString
from Game.FactoryGame.Character.Player.Widget_PlayerInventoryAddon import ExecuteUbergraph_Widget_PlayerInventoryAddon.K2Node_CustomEvent_numAdded

class Widget_PlayerInventoryAddon(FGInteractWidget):
    mInventoryComponent: Ptr[FGInventoryComponent]
    mTrashInventoryComponent: Ptr[FGInventoryComponent]
    SlotStackMoveEvent: FMulticastScriptDelegate
    mRelevantClasses: List[TSubclassOf[FGItemDescriptor]]
    mRelevantItemsText: FText = NSLOCTEXT("", "764BB7194B92BE7BCC551195F2CB6804", "Relevant Items:")
    mRelevantInventoryStackLimit: int32 = 12
    mRestoreFocusWhenLost = True
    mCallCustomTickOnConstruct = True
    Priority = 10
    bIsFocusable = True
    
    def FindInventorySlotWithIdx(self, slotIdx: int32):
        ExecutionFlow.Push("L541")
        
        InventorySlots = None
        self.mInventoryWidget.GetAllInventorySlots(Ref[InventorySlots])
        Variable: int32 = 0
        Variable_0: int32 = 0
        
        InventorySlots = None
        # Label 96
        ReturnValue: int32 = len(InventorySlots)
        ReturnValue_0: bool = Variable <= ReturnValue
        if not ReturnValue_0:
            goto('L451')
        Variable_0 = Variable
        ExecutionFlow.Push("L467")
        
        InventorySlots = None
        Item = None
        Item = InventorySlots[Variable_0]
        ReturnValue_1: bool = EqualEqual_IntInt(Item.mSlotIdx, slotIdx)
        if not ReturnValue_1:
           goto(ExecutionFlow.Pop())
        
        InventorySlots = None
        Item = None
        Item = InventorySlots[Variable_0]
        Array Element = Item
        # End
        # Label 451
        Array Element = None
        # End
        # Label 467
        ReturnValue_2: int32 = Variable + 1
        Variable = ReturnValue_2
        goto('L96')
    

    def SetDividerVisibility(self, IsVisible: bool):
        Variable: bool = IsVisible
        Variable_0: uint8 = 3
        Variable1: uint8 = 1
        
        switch = {
            False: Variable1,
            True: Variable_0
        }
        self.mDivider.SetVisibility(switch.get(Variable, None))
    

    def SetRelevantItemsText(self, mRelevantItemsText: FText):
        self.mRelevantItemsText = mRelevantItemsText
        self.mRelevantItemsTextObject.SetText(self.mRelevantItemsText)
    

    def ShouldItemClassUpdateRelevantInventory(self, UpdatedItemClass: TSubclassOf[Object]):
        ExecutionFlow.Push("L407")
        Variable: int32 = 0
        Variable_0: int32 = 0
        
        # Label 51
        ReturnValue: int32 = len(self.mRelevantClasses)
        ReturnValue_0: bool = Variable <= ReturnValue
        if not ReturnValue_0:
            goto('L317')
        Variable_0 = Variable
        ExecutionFlow.Push("L333")
        
        Item = None
        Item = self.mRelevantClasses[Variable_0]
        ReturnValue_1: bool = ClassIsChildOf(UpdatedItemClass, Item)
        if not ReturnValue_1:
           goto(ExecutionFlow.Pop())
        Return = True
        # End
        # Label 317
        Return = False
        # End
        # Label 333
        ReturnValue_2: int32 = Variable + 1
        Variable = ReturnValue_2
        goto('L51')
    

    def SetupRelevantInventory(self, mRelevantClasses: Ref[List[TSubclassOf[FGItemDescriptor]]]):
        self.mRelevantClasses = mRelevantClasses
        self.UpdateRelevantInventory()
    

    def UpdateRelevantInventory(self):
        ExecutionFlow.Push("L1971")
        ReturnValue: List[int32] = self.mInventoryComponent.GetRelevantStackIndexes(self.mRelevantClasses, self.mRelevantInventoryStackLimit)
        LocalRelevantInventoryIndexes = ReturnValue
        Variable: int32 = 0
        Variable_0: int32 = 0
        
        # Label 146
        ReturnValue1: int32 = len(LocalRelevantInventoryIndexes)
        ReturnValue_0: bool = Variable <= ReturnValue1
        if not ReturnValue_0:
            goto('L878')
        Variable_0 = Variable
        ExecutionFlow.Push("L1379")
        ReturnValue_1: Ptr[Widget] = self.mRelevantInventory.GetChildAt(Variable_0)
        ReturnValue_2: bool = Default__KismetSystemLibrary.IsValid(ReturnValue_1)
        if not ReturnValue_2:
            goto('L1453')
        ReturnValue_1 = self.mRelevantInventory.GetChildAt(Variable_0)
        Slot: Ptr[Widget_InventorySlot] = Cast[Widget_InventorySlot](ReturnValue_1)
        bSuccess: bool = Slot
        
        Item = None
        Item = LocalRelevantInventoryIndexes[Variable_0]
        Slot.mSlotIdx = Item
        ReturnValue_1 = self.mRelevantInventory.GetChildAt(Variable_0)
        Slot = Cast[Widget_InventorySlot](ReturnValue_1)
        bSuccess = Slot
        
        Item = None
        Item = LocalRelevantInventoryIndexes[Variable_0]
        
        Element = None
        self.FindInventorySlotWithIdx(Item, Ref[Element])
        Slot.mInventorySlotToRepresent = Element
        goto(ExecutionFlow.Pop())
        
        # Label 878
        ReturnValue_3: int32 = len(LocalRelevantInventoryIndexes)
        ReturnValue_4: int32 = self.mRelevantInventory.GetChildrenCount()
        ReturnValue_5: bool = ReturnValue_4 > ReturnValue_3
        if not ReturnValue_5:
            goto('L1188')
        ExecutionFlow.Push("L878")
        ReturnValue1_0: int32 = self.mRelevantInventory.GetChildrenCount()
        ReturnValue_6: int32 = ReturnValue1_0 - 1
        ReturnValue_7: bool = self.mRelevantInventory.RemoveChildAt(ReturnValue_6)
        goto(ExecutionFlow.Pop())
        # Label 1188
        Variable_1: uint8 = 1
        Variable1: uint8 = 4
        ReturnValue_8: bool = self.mRelevantInventory.HasAnyChildren()
        Variable_2: bool = ReturnValue_8
        
        switch = {
            False: Variable_1,
            True: Variable1
        }
        self.mRelevantInventoryContainer.SetVisibility(switch.get(Variable_2, None))
        goto(ExecutionFlow.Pop())
        # Label 1379
        ReturnValue_9: int32 = Variable + 1
        Variable = ReturnValue_9
        goto('L146')
        # Label 1453
        ReturnValue_10: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_11: Ptr[Widget_InventorySlot] = Default__WidgetBlueprintLibrary.Create(self, Widget_InventorySlot, ReturnValue_10)
        
        Item = None
        Item = LocalRelevantInventoryIndexes[Variable_0]
        Default__KismetSystemLibrary.SetIntPropertyByName(ReturnValue_11, "mSlotIdx", Item)
        Default__KismetSystemLibrary.SetObjectPropertyByName(ReturnValue_11, "mCachedInventoryComponent", self.mInventoryComponent)
        
        Item = None
        Item = LocalRelevantInventoryIndexes[Variable_0]
        
        Element = None
        self.FindInventorySlotWithIdx(Item, Ref[Element])
        ReturnValue_11.mInventorySlotToRepresent = Element
        ReturnValue_12: Ptr[PanelSlot] = self.mRelevantInventory.AddChild(ReturnValue_11)
        OutputDelegate.BindUFunction(self, OnInventorySlotMoveStack)
        ReturnValue_11.OnMoveStack.AddUnique(OutputDelegate)
        goto(ExecutionFlow.Pop())
    

    def OnInventorySlotMoveStack(self, InventorySlotSender: Ptr[Widget_InventorySlot]):
        self.SlotStackMoveEvent.ProcessMulticastDelegate(InventorySlotSender, 0)
        self.UpdateRelevantInventory()
    

    def SetInventoryComponents(self, inventoryComponent: Ptr[FGInventoryComponent], trash: Ptr[FGInventoryComponent]):
        self.mInventoryComponent = inventoryComponent
        self.mTrashInventoryComponent = trash
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_PlayerInventoryAddon(594)
    

    def BndEvt__mSortButton_K2Node_ComponentBoundEvent_0_OnClicked__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_PlayerInventoryAddon(1110)
    

    def OnUpdateRelevantInventory(self, ItemClass: TSubclassOf[FGItemDescriptor], numAdded: int32):
        ExecuteUbergraph_Widget_PlayerInventoryAddon.K2Node_CustomEvent_itemClass = ItemClass #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_PlayerInventoryAddon.K2Node_CustomEvent_numAdded = numAdded #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_PlayerInventoryAddon(1157)
    

    def PreConstruct(self):
        ExecuteUbergraph_Widget_PlayerInventoryAddon.K2Node_Event_IsDesignTime = IsDesignTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_PlayerInventoryAddon(1214)
    

    def BndEvt__mTrashInventoryWidget_K2Node_ComponentBoundEvent_1_OnInventoryDragEnter__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_PlayerInventoryAddon(1418)
    

    def BndEvt__mTrashInventoryWidget_K2Node_ComponentBoundEvent_2_OnInventoryDragLeave__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_PlayerInventoryAddon(1485)
    

    def BndEvt__mTrashInventoryWidget_K2Node_ComponentBoundEvent_3_OnInventoryMouseLeave__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_PlayerInventoryAddon(15)
    

    def ExecuteUbergraph_Widget_PlayerInventoryAddon(self):
        goto(ComputedJump("EntryPoint"))
        # Label 15
        self.mTrashBG.SetColorAndOpacity(LinearColor(R = 0.09530699998140335, G = 0.09530699998140335, B = 0.09530699998140335, A = 1))
        goto(ExecutionFlow.Pop())
        # Label 82
        ExecutionFlow.Push("L211")
        OutputDelegate1.BindUFunction(self, OnInventorySlotMoveStack)
        
        InventorySlots = None
        Item = None
        Item = InventorySlots[Variable]
        Item.OnMoveStack.AddUnique(OutputDelegate1)
        goto(ExecutionFlow.Pop())
        # Label 211
        ReturnValue: int32 = Variable + 1
        Variable: int32 = ReturnValue
        
        InventorySlots = None
        # Label 280
        ReturnValue_0: int32 = len(InventorySlots)
        ReturnValue_1: bool = Variable <= ReturnValue_0
        if not ReturnValue_1:
            goto('L423')
        Variable = Variable
        goto('L82')
        # Label 423
        OutputDelegate.BindUFunction(self, OnUpdateRelevantInventory)
        self.mInventoryComponent.OnItemAddedDelegate.AddUnique(OutputDelegate)
        OutputDelegate.BindUFunction(self, OnUpdateRelevantInventory)
        self.mInventoryComponent.OnItemRemovedDelegate.AddUnique(OutputDelegate)
        self.UpdateRelevantInventory()
        goto(ExecutionFlow.Pop())
        # Label 566
        Variable = 0
        goto('L280')
        self.Construct()
        ReturnValue_2: Ptr[Pawn] = self.GetOwningPlayerPawn()
        Player: Ptr[FGCharacterPlayer] = Cast[FGCharacterPlayer](ReturnValue_2)
        bSuccess: bool = Player
        if not bSuccess:
            goto('L982')
        ReturnValue_3: Ptr[FGInventoryComponent] = Player.GetTrashSlot()
        ReturnValue_4: Ptr[FGInventoryComponent] = Player.GetInventory()
        self.SetInventoryComponents(ReturnValue_4, ReturnValue_3)
        self.mInventoryWidget.Init(self.mInventoryComponent)
        self.mTrashInventoryWidget.Init(self.mTrashInventoryComponent)
        
        InventorySlots = None
        self.mInventoryWidget.GetAllInventorySlots(Ref[InventorySlots])
        Variable = 0
        goto('L566')
        # Label 982
        Default__KismetSystemLibrary.PrintString(self, "Cast to fgcharacterplayer failed in inventory addon", True, True, LinearColor(R = 0, G = 0.6600000262260437, B = 1, A = 1), 2)
        goto(ExecutionFlow.Pop())
        self.mInventoryComponent.SortInventory()
        self.UpdateRelevantInventory()
        goto(ExecutionFlow.Pop())
        
        Return = None
        self.ShouldItemClassUpdateRelevantInventory(itemClass, Ref[Return])
        if not Return:
           goto(ExecutionFlow.Pop())
        self.UpdateRelevantInventory()
        goto(ExecutionFlow.Pop())
        self.SetRelevantItemsText(self.mRelevantItemsText)
        Variable_0: int32 = 9
        Variable1: int32 = 6
        Variable_1: bool = self.mInventoryWidget.mUseSmallSlots
        
        switch = {
            False: Variable1,
            True: Variable_0
        }
        self.mInventoryWidget.mOverrideWidth = switch.get(Variable_1, None)
        goto(ExecutionFlow.Pop())
        self.mTrashBG.SetColorAndOpacity(LinearColor(R = 0.7835379838943481, G = 0.2917709946632385, B = 0.057805001735687256, A = 1))
        goto(ExecutionFlow.Pop())
        goto('L15')
    

    def SlotStackMoveEvent__DelegateSignature(self, InventorySlot: Ptr[Widget_InventorySlot], Direction: uint8):
        pass
    
