
from codegen.ue4_stub import *

from Game.FactoryGame.Buildable.Factory.BP_DragNDropInventory import ExecuteUbergraph_BP_DragNDropInventory.K2Node_Event_PointerEvent2
from Game.FactoryGame.Buildable.Factory.BP_DragNDropInventory import ExecuteUbergraph_BP_DragNDropInventory
from Game.FactoryGame.Buildable.Factory.BP_DragNDropInventory import ExecuteUbergraph_BP_DragNDropInventory.K2Node_Event_PointerEvent1
from Script.UMG import Dragged
from Game.FactoryGame.Buildable.Factory.BP_DragNDropInventory import ExecuteUbergraph_BP_DragNDropInventory.K2Node_Event_PointerEvent
from Game.FactoryGame.Interface.UI.InGame.Widget_InventoryDragNDropRep import Widget_InventoryDragNDropRep
from Script.UMG import DragDropOperation
from Game.FactoryGame.Interface.UI.InGame.InventorySlots.Widget_InventorySlot import Widget_InventorySlot

class BP_DragNDropInventory(DragDropOperation):
    
    
    def Dragged(self):
        ExecuteUbergraph_BP_DragNDropInventory.K2Node_Event_PointerEvent2 = PointerEvent #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_DragNDropInventory(442)
    

    def DragCancelled(self):
        ExecuteUbergraph_BP_DragNDropInventory.K2Node_Event_PointerEvent1 = PointerEvent #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_DragNDropInventory(466)
    

    def Drop(self):
        ExecuteUbergraph_BP_DragNDropInventory.K2Node_Event_PointerEvent = PointerEvent #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_DragNDropInventory(550)
    

    def ExecuteUbergraph_BP_DragNDropInventory(self):
        # Label 10
        Slot: Ptr[Widget_InventorySlot] = Cast[Widget_InventorySlot](self.payload)
        bSuccess: bool = Slot
        if not bSuccess:
            goto('L555')
        # End
        # Label 94
        Slot1: Ptr[Widget_InventorySlot] = Cast[Widget_InventorySlot](self.payload)
        bSuccess1: bool = Slot1
        if not bSuccess1:
            goto('L555')
        
        Num = None
        Slot1.GetNumItems(Ref[Num])
        Rep.mNumItems = Num
        
        ItemClass = None
        Slot1.GetItemClass(Ref[ItemClass])
        Rep.mInventoryItem = ItemClass
        # End
        # Label 358
        Rep: Ptr[Widget_InventoryDragNDropRep] = Cast[Widget_InventoryDragNDropRep](self.DefaultDragVisual)
        bSuccess2: bool = Rep
        if not bSuccess2:
            goto('L555')
        goto('L94')
        
        PointerEvent2 = None
        self.Dragged(Ref[PointerEvent2])
        goto('L358')
        Slot2: Ptr[Widget_InventorySlot] = Cast[Widget_InventorySlot](self.payload)
        bSuccess3: bool = Slot2
        if not bSuccess3:
            goto('L555')
        # End
        goto('L10')
    
