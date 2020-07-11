
from codegen.ue4_stub import *

from Script.Engine import Default__KismetSystemLibrary
from Game.FactoryGame.Buildable.Factory.TradingPost.Widget_TradingPost_PayOffGrid import Widget_TradingPost_PayOffGrid
from Game.FactoryGame.Buildable.Factory.SpaceElevator.Widget_SpaceElevator import Widget_SpaceElevator
from Game.FactoryGame.Buildable.-Shared.WorkBench.Widget_MAMResearchSlot import Widget_MAMResearchSlot
from Script.Engine import Not_PreBool
from Script.Engine import Default__KismetArrayLibrary
from Game.FactoryGame.Interface.UI.InGame.Inventory_DropArea_States import Inventory_DropArea_States
from Script.FactoryGame import IsItemAllowed
from Game.FactoryGame.Buildable.Factory.BP_DragNDropInventory import BP_DragNDropInventory
from Script.Engine import IsValid
from Game.FactoryGame.Interface.UI.InGame.InventorySlots.Widget_InventorySlot import Widget_InventorySlot
from Script.Engine import Default__KismetStringLibrary
from Script.Engine import Conv_BoolToString
from Script.Engine import NotEqual_ByteByte
from Script.Engine import PrintString
from Script.UMG import UserWidget
from Script.CoreUObject import LinearColor

class Widget_InventorySlot_DropArea(UserWidget):
    mDropAreaState: uint8
    mInventorySlots: List[Ptr[Widget_InventorySlot]]
    mHudPayOffGrid: Ptr[Widget_TradingPost_PayOffGrid]
    mSpaceElevator: Ptr[Widget_SpaceElevator]
    mMAMResearchSlot: Ptr[Widget_MAMResearchSlot]
    
    def OnDropInventorySlot(self, InventorySlot: Ptr[Widget_InventorySlot]):
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(InventorySlot)
        ReturnValue_0: FString = Default__KismetStringLibrary.Conv_BoolToString(ReturnValue)
        Default__KismetSystemLibrary.PrintString(self, ReturnValue_0, True, True, LinearColor(R = 0, G = 0.6600000262260437, B = 1, A = 1), 2)
        
        InventorySlot_0 = None
        Success = None
        self.FindCorrectSlot(InventorySlot, Ref[InventorySlot_0], Ref[Success])
        if not Success:
            goto('L367')
        
        InventorySlot_0 = None
        Success = None
        self.FindCorrectSlot(InventorySlot, Ref[InventorySlot_0], Ref[Success])
        
        Result = None
        InventorySlot_0.DropOntoInventorySlot(InventorySlot, Ref[Result])
        Result = Result
        # End
        # Label 367
        Result = False
    

    def FindCorrectSlot(self, payload: Ptr[Widget_InventorySlot]):
        ExecutionFlow.Push("L708")
        Variable: bool = False
        Variable_0: int32 = 0
        Variable_1: int32 = 0
        # Label 62
        ReturnValue: bool = Not_PreBool(Variable)
        
        ReturnValue_0: int32 = len(self.mInventorySlots)
        ReturnValue_1: bool = Variable_0 <= ReturnValue_0
        ReturnValue_2: bool = ReturnValue and ReturnValue_1
        if not ReturnValue_2:
            goto('L591')
        Variable_1 = Variable_0
        ExecutionFlow.Push("L634")
        
        ItemClass = None
        payload.GetItemClass(Ref[ItemClass])
        
        Item = None
        Item = self.mInventorySlots[Variable_1]
        ReturnValue_3: bool = Item.mCachedInventoryComponent.IsItemAllowed(ItemClass, Item.mSlotIdx)
        if not ReturnValue_3:
           goto(ExecutionFlow.Pop())
        
        Item = None
        Item = self.mInventorySlots[Variable_1]
        LocalInventorySlot = Item
        LocalFoundSlot = True
        Variable = True
        goto(ExecutionFlow.Pop())
        # Label 591
        InventorySlot = LocalInventorySlot
        success = LocalFoundSlot
        # End
        # Label 634
        ReturnValue_4: int32 = Variable_0 + 1
        Variable_0 = ReturnValue_4
        goto('L62')
    

    def OnDrop(self):
        Inventory: Ptr[BP_DragNDropInventory] = Cast[BP_DragNDropInventory](Operation)
        bSuccess: bool = Inventory
        if not bSuccess:
            goto('L384')
        Slot: Ptr[Widget_InventorySlot] = Cast[Widget_InventorySlot](Inventory.payload)
        bSuccess1: bool = Slot
        if not bSuccess1:
            goto('L400')
        LocalInventorySlot = Slot
        CmpSuccess: bool = NotEqual_ByteByte(self.mDropAreaState, 0)
        if not CmpSuccess:
            goto('L416')
        CmpSuccess = NotEqual_ByteByte(self.mDropAreaState, 1)
        if not CmpSuccess:
            goto('L472')
        CmpSuccess = NotEqual_ByteByte(self.mDropAreaState, 2)
        if not CmpSuccess:
            goto('L631')
        CmpSuccess = NotEqual_ByteByte(self.mDropAreaState, 3)
        if not CmpSuccess:
            goto('L790')
        goto('L944')
        # Label 384
        ReturnValue = False
        goto('L944')
        # Label 400
        ReturnValue = False
        goto('L944')
        
        Result = None
        # Label 416
        self.OnDropInventorySlot(LocalInventorySlot, Ref[Result])
        ReturnValue = Result
        goto('L944')
        # Label 472
        ReturnValue1: bool = Default__KismetSystemLibrary.IsValid(self.mHudPayOffGrid)
        if not ReturnValue1:
            goto('L615')
        
        Result = None
        self.mHudPayOffGrid.DropInventorySlotStack(LocalInventorySlot, Ref[Result])
        # Label 591
        ReturnValue = Result
        goto('L944')
        # Label 615
        ReturnValue = False
        goto('L944')
        # Label 631
        ReturnValue_0: bool = Default__KismetSystemLibrary.IsValid(self.mSpaceElevator)
        if not ReturnValue_0:
            goto('L774')
        
        WasStackMoved = None
        self.mSpaceElevator.DropInventorySlotStack(LocalInventorySlot, Ref[WasStackMoved])
        ReturnValue = WasStackMoved
        goto('L944')
        # Label 774
        ReturnValue = False
        goto('L944')
        # Label 790
        ReturnValue2: bool = Default__KismetSystemLibrary.IsValid(self.mMAMResearchSlot)
        if not ReturnValue2:
            goto('L933')
        
        Result = None
        self.mMAMResearchSlot.DropOntoInventorySlot(LocalInventorySlot, Ref[Result])
        ReturnValue = Result
        goto('L944')
        # Label 933
        ReturnValue = False
    
