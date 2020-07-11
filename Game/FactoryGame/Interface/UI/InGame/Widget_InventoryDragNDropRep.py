
from codegen.ue4_stub import *

from Script.UMG import GetOwningPlayerPawn
from Script.UMG import Construct
from Script.AkAudio import PostAkEvent
from Script.FactoryGame import FGItemDescriptor
from Script.Engine import Pawn
from Game.FactoryGame.Interface.UI.Audio.Play_UI_Inventory_Drag import Play_UI_Inventory_Drag
from Game.FactoryGame.Interface.UI.InGame.InventorySlots.Widget_InventorySlot import Widget_InventorySlot
from Script.AkAudio import AkComponent
from Game.FactoryGame.Interface.UI.Audio.Play_UI_Inventory_Drop import Play_UI_Inventory_Drop
from Script.AkAudio import Default__AkGameplayStatics
from Game.FactoryGame.Interface.UI.InGame.Widget_InventoryDragNDropRep import ExecuteUbergraph_Widget_InventoryDragNDropRep
from Script.UMG import UserWidget
from Script.UMG import Destruct

class Widget_InventoryDragNDropRep(UserWidget):
    mNumItems: int32
    mInventoryItem: TSubclassOf[FGItemDescriptor]
    mIsEquipment: bool
    mInventorySlotWidget: Ptr[Widget_InventorySlot]
    
    def Construct(self):
        self.ExecuteUbergraph_Widget_InventoryDragNDropRep(10)
    

    def Destruct(self):
        self.ExecuteUbergraph_Widget_InventoryDragNDropRep(240)
    

    def ExecuteUbergraph_Widget_InventoryDragNDropRep(self):
        self.Construct()
        ReturnValue: Ptr[Pawn] = self.GetOwningPlayerPawn()
        ReturnValue_0: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_UI_Inventory_Drag, ReturnValue, True)
        self.Widget_InventorySlot.mCachedInventoryComponent = self.mInventorySlotWidget.mCachedInventoryComponent
        self.Widget_InventorySlot.mSlotIdx = self.mInventorySlotWidget.mSlotIdx
        # End
        self.Destruct()
        ReturnValue1: Ptr[Pawn] = self.GetOwningPlayerPawn()
        ReturnValue1_0: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_UI_Inventory_Drop, ReturnValue1, True)
    
