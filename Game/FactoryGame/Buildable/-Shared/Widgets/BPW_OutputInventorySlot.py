
from codegen.ue4_stub import *

from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import PlayerController
from Script.UMG import AddChild
from Game.FactoryGame.Buildable.-Shared.Widgets.BPW_OutputInventorySlot import ExecuteUbergraph_BPW_OutputInventorySlot
from Script.UMG import Create
from Script.Engine import SetObjectPropertyByName
from Game.FactoryGame.Interface.UI.InGame.Widget_CostSlotWrapper import Widget_CostSlotWrapper
from Game.FactoryGame.Interface.UI.InGame.ESlotType import ESlotType
from Script.FactoryGame import FGInventoryComponent
from Game.FactoryGame.Interface.UI.InGame.InventorySlots.Widget_InventorySlot import Widget_InventorySlot
from Script.Engine import SetIntPropertyByName
from Script.UMG import PanelSlot
from Script.UMG import Default__WidgetBlueprintLibrary
from Script.Engine import NotEqual_ByteByte
from Script.UMG import UserWidget

class BPW_OutputInventorySlot(UserWidget):
    mTitle: FText
    mCachedInventoryCompontent: Ptr[FGInventoryComponent]
    mSlotIdx: int32
    mSlotType: uint8
    mRequiredAmount: int32
    mInventorySlot: Ptr[Widget_InventorySlot]
    
    def SetupCostSlot(self, mCachedInventoryComponent: Ptr[FGInventoryComponent], mSlotIdx: int32, RequiredAmount: int32):
        self.mCachedInventoryCompontent = mCachedInventoryComponent
        self.mRequiredAmount = self.mRequiredAmount
        self.mSlotIdx = mSlotIdx
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_0: Ptr[Widget_CostSlotWrapper] = Default__WidgetBlueprintLibrary.Create(self, Widget_CostSlotWrapper, ReturnValue)
        ReturnValue_1: Ptr[PanelSlot] = self.mContainer.AddChild(ReturnValue_0)
        ItemAmount.ItemClass = None
        ItemAmount.amount = self.mRequiredAmount
        ReturnValue_0.Setup CostIcon(None, ItemAmount, self.mCachedInventoryCompontent, self.mSlotIdx, 0, False, False, False)
        self.mInventorySlot = ReturnValue_0.Widget_InventorySlot
    

    def UpdateSlot(self, Title: FText, mCachedInventoryComponent: Ptr[FGInventoryComponent], mSlotIdx: int32, slotType: uint8, mRequiredAmount: int32):
        self.mContainer.ClearChildren()
        self.SetTitle(Title)
        self.mSlotType = slotType
        CmpSuccess: bool = NotEqual_ByteByte(self.mSlotType, 0)
        if not CmpSuccess:
            goto('L181')
        CmpSuccess = NotEqual_ByteByte(self.mSlotType, 1)
        if not CmpSuccess:
            goto('L218')
        # End
        # Label 181
        self.SetupInventorySlot(mCachedInventoryComponent, mSlotIdx)
        # End
        # Label 218
        self.SetupCostSlot(mCachedInventoryComponent, mSlotIdx, mRequiredAmount)
    

    def SetupInventorySlot(self, mCachedInventoryComponent: Ptr[FGInventoryComponent], mSlotIdx: int32):
        self.mCachedInventoryCompontent = mCachedInventoryComponent
        self.mSlotIdx = mSlotIdx
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_0: Ptr[Widget_InventorySlot] = Default__WidgetBlueprintLibrary.Create(self, Widget_InventorySlot, ReturnValue)
        Default__KismetSystemLibrary.SetIntPropertyByName(ReturnValue_0, "mSlotIdx", self.mSlotIdx)
        Default__KismetSystemLibrary.SetObjectPropertyByName(ReturnValue_0, "mCachedInventoryComponent", self.mCachedInventoryCompontent)
        self.mInventorySlot = ReturnValue_0
        ReturnValue_1: Ptr[PanelSlot] = self.mContainer.AddChild(self.mInventorySlot)
    

    def SetTitle(self, Title: FText):
        self.mTitle = Title
        self.mTitleObject.SetText(self.mTitle)
    

    def Construct(self):
        self.ExecuteUbergraph_BPW_OutputInventorySlot(10)
    

    def ExecuteUbergraph_BPW_OutputInventorySlot(self):
        self.UpdateSlot(self.mTitle, self.mCachedInventoryCompontent, self.mSlotIdx, self.mSlotType, self.mRequiredAmount)
    
