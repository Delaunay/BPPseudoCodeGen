
from codegen.ue4_stub import *

from Game.FactoryGame.Character.Player.Widget_PlayerEquipmentInventory import ExecuteUbergraph_Widget_PlayerEquipmentInventory.K2Node_Event_InDeltaTime
from Game.FactoryGame.Character.Player.Widget_PlayerEquipmentInventory import ExecuteUbergraph_Widget_PlayerEquipmentInventory.K2Node_Event_MyGeometry
from Script.Engine import Delay
from Script.FactoryGame import FGCharacterPlayer
from Script.Engine import Pawn
from Script.Engine import GreaterEqual_IntInt
from Script.UMG import GetChildrenCount
from Script.Engine import LatentActionInfo
from Script.Engine import Default__KismetSystemLibrary
from Script.UMG import GetChildAt
from Script.Engine import Default__KismetArrayLibrary
from Script.UMG import ESlateVisibility
from Script.Engine import Array_Append
from Script.Engine import IsValid
from Game.FactoryGame.Interface.UI.InGame.InventorySlots.Widget_InventorySlot import Widget_InventorySlot
from Script.FactoryGame import FGInventoryComponentEquipment
from Script.Engine import EqualEqual_IntInt
from Script.UMG import Construct
from Script.UMG import Tick
from Script.UMG import Widget
from Script.FactoryGame import GetActiveIndex
from Game.FactoryGame.Character.Player.Widget_PlayerEquipmentInventory import ExecuteUbergraph_Widget_PlayerEquipmentInventory
from Script.UMG import UserWidget
from Script.UMG import GetOwningPlayerPawn
from Script.FactoryGame import GetSizeLinear
from Script.FactoryGame import GetEquipmentSlot

class Widget_PlayerEquipmentInventory(UserWidget):
    mActiveSlotIndex: int32 = -10
    mCharacterPlayer: Ptr[FGCharacterPlayer]
    
    def SetActiveSlot(self, mActiveSlotIndex: int32):
        ExecutionFlow.Push("L777")
        self.mActiveSlotIndex = mActiveSlotIndex
        Variable: int32 = 0
        # Label 55
        ReturnValue: int32 = self.mHandsSlot.mSlots.GetChildrenCount()
        ReturnValue_0: bool = Variable <= ReturnValue
        if not ReturnValue_0:
           goto(ExecutionFlow.Pop())
        ExecutionFlow.Push("L703")
        ReturnValue_1: Ptr[Widget] = self.mHandsSlot.mSlots.GetChildAt(Variable)
        Slot: Ptr[Widget_InventorySlot] = Cast[Widget_InventorySlot](ReturnValue_1)
        bSuccess: bool = Slot
        if not bSuccess:
           goto(ExecutionFlow.Pop())
        Variable_0: uint8 = 3
        Variable1: uint8 = 1
        ReturnValue_2: bool = EqualEqual_IntInt(Variable, self.mActiveSlotIndex)
        ReturnValue_3: Ptr[FGInventoryComponentEquipment] = self.mCharacterPlayer.GetEquipmentSlot(1)
        ReturnValue_4: int32 = ReturnValue_3.GetSizeLinear()
        ReturnValue_5: bool = ReturnValue_4 > 1
        ReturnValue_6: bool = ReturnValue_2 and ReturnValue_5
        Variable_1: bool = ReturnValue_6
        
        switch = {
            False: Variable1,
            True: Variable_0
        }
        Slot.mEquipmentFeedback.SetVisibility(switch.get(Variable_1, None))
        goto(ExecutionFlow.Pop())
        # Label 703
        ReturnValue_7: int32 = Variable + 1
        Variable = ReturnValue_7
        goto('L55')
    

    def ArmSelectionVisibility(self):
        ReturnValue: Ptr[Pawn] = self.GetOwningPlayerPawn()
        Player: Ptr[FGCharacterPlayer] = Cast[FGCharacterPlayer](ReturnValue)
        bSuccess: bool = Player
        if not bSuccess:
            goto('L362')
        Variable: uint8 = 3
        Variable1: uint8 = 1
        ReturnValue_0: Ptr[FGInventoryComponentEquipment] = Player.GetEquipmentSlot(1)
        ReturnValue_1: int32 = ReturnValue_0.GetActiveIndex()
        ReturnValue_2: bool = GreaterEqual_IntInt(ReturnValue_1, 0)
        Variable_0: bool = ReturnValue_2
        
        switch = {
            False: Variable1,
            True: Variable
        }
        ReturnValue_3: uint8 = switch.get(Variable_0, None)
        goto('L382')
        # Label 362
        ReturnValue_3 = 1
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_PlayerEquipmentInventory(1061)
    

    def Tick(self):
        ExecuteUbergraph_Widget_PlayerEquipmentInventory.K2Node_Event_MyGeometry = MyGeometry #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_PlayerEquipmentInventory.K2Node_Event_InDeltaTime = InDeltaTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_PlayerEquipmentInventory(1262)
    

    def Destruct(self):
        self.ExecuteUbergraph_Widget_PlayerEquipmentInventory(1295)
    

    def ExecuteUbergraph_Widget_PlayerEquipmentInventory(self):
        goto(ComputedJump("EntryPoint"))
        # Label 15
        self.SetActiveSlot(-1)
        goto(ExecutionFlow.Pop())
        
        InventorySlots = None
        self.mHandsSlot.GetAllInventorySlots(Ref[InventorySlots])
        
        self.Widget_InventorySlot_DropArea.mInventorySlots = None
        InventorySlots = None
        Default__KismetArrayLibrary.Array_Append(Ref[self.Widget_InventorySlot_DropArea.mInventorySlots], Ref[InventorySlots])
        
        InventorySlots1 = None
        self.mBackSlot.GetAllInventorySlots(Ref[InventorySlots1])
        
        self.Widget_InventorySlot_DropArea.mInventorySlots = None
        InventorySlots1 = None
        Default__KismetArrayLibrary.Array_Append(Ref[self.Widget_InventorySlot_DropArea.mInventorySlots], Ref[InventorySlots1])
        goto(ExecutionFlow.Pop())
        # Label 270
        ReturnValue: int32 = self.mHandsSlot.mSlots.GetChildrenCount()
        ReturnValue_0: bool = ReturnValue > 0
        if not ReturnValue_0:
            goto('L508')
        ReturnValue_1: Ptr[FGInventoryComponentEquipment] = self.mCharacterPlayer.GetEquipmentSlot(1)
        ReturnValue_2: int32 = ReturnValue_1.GetActiveIndex()
        self.SetActiveSlot(ReturnValue_2)
        goto(ExecutionFlow.Pop())
        # Label 508
        Default__KismetSystemLibrary.Delay(self, 0.10000000149011612, LatentActionInfo(Linkage = 270, UUID = -1695573871, ExecutionFunction = "ExecuteUbergraph_Widget_PlayerEquipmentInventory", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        # Label 585
        Variable: bool = False
        ReturnValue_1 = self.mCharacterPlayer.GetEquipmentSlot(1)
        ReturnValue_2 = ReturnValue_1.GetActiveIndex()
        ReturnValue_3: bool = ReturnValue_2 != self.mActiveSlotIndex
        if not ReturnValue_3:
            goto('L757')
        if not Variable1:
            goto('L795')
        goto(ExecutionFlow.Pop())
        # Label 757
        Variable1: bool = False
        if not Variable2:
            goto('L783')
        goto(ExecutionFlow.Pop())
        # Label 783
        Variable2: bool = True
        goto(ExecutionFlow.Pop())
        # Label 795
        Variable1 = True
        Variable2 = False
        goto('L270')
        # Label 822
        ReturnValue_4: bool = Default__KismetSystemLibrary.IsValid(self.mCharacterPlayer)
        if not ReturnValue_4:
           goto(ExecutionFlow.Pop())
        ReturnValue_1 = self.mCharacterPlayer.GetEquipmentSlot(1)
        ReturnValue_2 = ReturnValue_1.GetActiveIndex()
        ReturnValue_5: bool = GreaterEqual_IntInt(ReturnValue_2, 0)
        if not ReturnValue_5:
            goto('L1030')
        goto('L585')
        # Label 1030
        if not Variable:
            goto('L1045')
        goto(ExecutionFlow.Pop())
        # Label 1045
        Variable = True
        goto('L15')
        self.Construct()
        ReturnValue_6: Ptr[Pawn] = self.GetOwningPlayerPawn()
        Player: Ptr[FGCharacterPlayer] = Cast[FGCharacterPlayer](ReturnValue_6)
        bSuccess: bool = Player
        if not bSuccess:
           goto(ExecutionFlow.Pop())
        self.mCharacterPlayer = Player
        Default__KismetSystemLibrary.Delay(self, 1, LatentActionInfo(Linkage = 35, UUID = -795895032, ExecutionFunction = "ExecuteUbergraph_Widget_PlayerEquipmentInventory", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        self.Tick(MyGeometry, InDeltaTime)
        goto('L822')
        self.mActiveSlotIndex = -10
        goto(ExecutionFlow.Pop())
    
