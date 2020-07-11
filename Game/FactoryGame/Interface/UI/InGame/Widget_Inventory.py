
from codegen.ue4_stub import *

from Script.UMG import AddChildToUniformGrid
from Game.FactoryGame.Interface.UI.InGame.Widget_Inventory import ExecuteUbergraph_Widget_Inventory
from Game.FactoryGame.Interface.UI.InGame.Widget_Inventory import ExecuteUbergraph_Widget_Inventory.K2Node_Event_PointerEvent
from Script.FactoryGame import GetFGGameUserSettings
from Script.Engine import SetObjectPropertyByName
from Script.Engine import FFloor
from Script.Engine import Conv_IntToFloat
from Script.Engine import Not_PreBool
from Script.Engine import Default__KismetSystemLibrary
from Script.UMG import SetColumn
from Game.FactoryGame.Interface.UI.InGame.Widget_Inventory import ExecuteUbergraph_Widget_Inventory.K2Node_CustomEvent_newSize
from Script.Engine import PlayerController
from Game.FactoryGame.Interface.UI.InGame.Widget_Inventory import ExecuteUbergraph_Widget_Inventory.K2Node_Event_Operation
from Script.Engine import Default__KismetArrayLibrary
from Script.Engine import Sqrt
from Game.FactoryGame.Interface.UI.InGame.Widget_Inventory import ExecuteUbergraph_Widget_Inventory.K2Node_Event_Operation1
from Game.FactoryGame.Interface.UI.InGame.Widget_Inventory import ExecuteUbergraph_Widget_Inventory.K2Node_Event_MouseEvent
from Script.FactoryGame import FGInventoryComponent
from Game.FactoryGame.Interface.UI.InGame.InventorySlots.Widget_InventorySlot import Widget_InventorySlot
from Script.Engine import IsValid
from Game.FactoryGame.Interface.UI.InGame.Widget_Inventory import ExecuteUbergraph_Widget_Inventory.K2Node_CustomEvent_oldSize
from Script.FactoryGame import GetBoolOptionValue
from Script.UMG import Default__WidgetBlueprintLibrary
from Script.FactoryGame import FGGameUserSettings
from Script.UMG import UniformGridSlot
from Game.FactoryGame.Interface.UI.InGame.Widget_Inventory import ExecuteUbergraph_Widget_Inventory.K2Node_Event_PointerEvent1
from Script.Engine import Divide_IntInt
from Script.UMG import SetRow
from Script.FactoryGame import Default__FGGameUserSettings
from Script.Engine import SetBoolPropertyByName
from Script.Engine import Percent_IntInt
from Script.Engine import SetIntPropertyByName
from Script.Engine import SelectInt
from Script.UMG import UserWidget
from Script.UMG import Create
from Script.FactoryGame import GetSizeLinear
from Script.Engine import Min
from Script.Engine import Array_Clear
from Game.FactoryGame.Interface.UI.InGame.Widget_Inventory import ExecuteUbergraph_Widget_Inventory.K2Node_Event_MyGeometry
from Script.Engine import PrintString
from Script.CoreUObject import LinearColor

class Widget_Inventory(UserWidget):
    mInventoryComponent: Ptr[FGInventoryComponent]
    mMaxInventoryColumns: int32 = 9999
    mIsLockedInventory: bool
    mUncalculatedWidth: int32
    mOverrideWidth: int32 = -1
    mUseLinearSize: bool
    mUseSmallSlots: bool
    mInventorySlots: List[Ptr[Widget_InventorySlot]]
    mAlwaysBigSlot: bool
    mKeepWidthRegardlessOfSlotSize: bool = True
    OnInventoryDragEnter: FMulticastScriptDelegate
    OnInventoryDragLeave: FMulticastScriptDelegate
    OnInventoryMouseLeave: FMulticastScriptDelegate
    padding = Namespace(Bottom=4, Left=4, Right=4, Top=4)
    
    def GetAllInventorySlots(self):
        InventorySlots = self.mInventorySlots
    

    def GetSqrtOfLinearSize(self):
        ReturnValue: int32 = self.mInventoryComponent.GetSizeLinear()
        ReturnValue_0: float = Conv_IntToFloat(ReturnValue)
        ReturnValue_1: float = Sqrt(ReturnValue_0)
        ReturnValue_2: int32 = FFloor(ReturnValue_1)
        ReturnValue_3: int32 = ReturnValue_2
    

    def GetWidth(self):
        ReturnValue: float = 42 / 64
        ReturnValue_0: bool = Not_PreBool(self.mUseSmallSlots)
        ReturnValue_1: float = self.mOverrideWidth * ReturnValue
        ReturnValue_2: bool = self.mKeepWidthRegardlessOfSlotSize and ReturnValue_0
        ReturnValue_3: int32 = FFloor(ReturnValue_1)
        ReturnValue_4: int32 = self.mInventoryComponent.GetSizeLinear()
        ReturnValue_5: int32 = SelectInt(ReturnValue_3, self.mOverrideWidth, ReturnValue_2)
        ReturnValue_6: bool = self.mOverrideWidth != -1
        ReturnValue_7: int32 = self.GetSqrtOfLinearSize()
        ReturnValue_8: int32 = Min(ReturnValue_7, self.mMaxInventoryColumns)
        ReturnValue1: int32 = SelectInt(ReturnValue_5, ReturnValue_8, ReturnValue_6)
        ReturnValue2: int32 = SelectInt(ReturnValue_4, ReturnValue1, self.mUseLinearSize)
        ReturnValue_9: int32 = ReturnValue2
    

    def CreateAllSlots(self):
        ExecutionFlow.Push("L1902")
        
        Default__KismetArrayLibrary.Array_Clear(Ref[self.mInventorySlots])
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(self.mInventoryComponent)
        if not ReturnValue:
            goto('L322')
        if not self.mUseLinearSize:
            goto('L446')
        Variable3: int32 = 0
        # Label 148
        ReturnValue_0: int32 = self.GetWidth()
        ReturnValue_1: int32 = ReturnValue_0 - 1
        ReturnValue3: bool = Variable3 <= ReturnValue_1
        if not ReturnValue3:
           goto(ExecutionFlow.Pop())
        ExecutionFlow.Push("L1754")
        
        Result2 = None
        self.CreateSlot(Variable3, 0, Variable3, Ref[Result2])
        goto(ExecutionFlow.Pop())
        # Label 322
        Default__KismetSystemLibrary.PrintString(self, "no inventory component? this should not happen!", True, True, LinearColor(R = 0, G = 0.6600000262260437, B = 1, A = 1), 2)
        goto(ExecutionFlow.Pop())
        # Label 446
        Variable: int32 = 0
        # Label 469
        ReturnValue8: int32 = self.GetWidth()
        ReturnValue3_0: int32 = ReturnValue8 - 1
        ReturnValue1: bool = Variable <= ReturnValue3_0
        if not ReturnValue1:
            goto('L957')
        ExecutionFlow.Push("L883")
        Variable1: int32 = 0
        # Label 623
        ReturnValue2: int32 = self.GetWidth()
        ReturnValue1_0: int32 = ReturnValue2 - 1
        ReturnValue_2: bool = Variable1 <= ReturnValue1_0
        if not ReturnValue_2:
           goto(ExecutionFlow.Pop())
        ExecutionFlow.Push("L1828")
        ReturnValue7: int32 = self.GetWidth()
        
        idx = None
        self.CalcIndex(Variable1, Variable, ReturnValue7, Ref[idx])
        
        Result = None
        self.CreateSlot(idx, Variable, Variable1, Ref[Result])
        goto(ExecutionFlow.Pop())
        # Label 883
        ReturnValue_3: int32 = Variable + 1
        Variable = ReturnValue_3
        goto('L469')
        # Label 957
        ReturnValue1_1: int32 = self.GetWidth()
        ReturnValue6: int32 = self.GetWidth()
        ReturnValue_4: int32 = ReturnValue6 * ReturnValue1_1
        Variable2: int32 = ReturnValue_4
        # Label 1094
        ReturnValue_5: int32 = self.mInventoryComponent.GetSizeLinear()
        ReturnValue4: int32 = ReturnValue_5 - 1
        ReturnValue2_0: bool = Variable2 <= ReturnValue4
        if not ReturnValue2_0:
           goto(ExecutionFlow.Pop())
        ExecutionFlow.Push("L1680")
        ReturnValue1_1 = self.GetWidth()
        ReturnValue3_1: int32 = self.GetWidth()
        ReturnValue4_0: int32 = self.GetWidth()
        ReturnValue5: int32 = self.GetWidth()
        ReturnValue_6: int32 = Percent_IntInt(Variable2, ReturnValue4_0)
        ReturnValue6 = self.GetWidth()
        ReturnValue_4 = ReturnValue6 * ReturnValue1_1
        ReturnValue2_1: int32 = Variable2 - ReturnValue_4
        ReturnValue_7: int32 = Divide_IntInt(ReturnValue2_1, ReturnValue5)
        ReturnValue3_2: int32 = ReturnValue3_1 + ReturnValue_7
        
        Result1 = None
        self.CreateSlot(Variable2, ReturnValue3_2, ReturnValue_6, Ref[Result1])
        goto(ExecutionFlow.Pop())
        # Label 1680
        ReturnValue1_2: int32 = Variable2 + 1
        Variable2 = ReturnValue1_2
        goto('L1094')
        # Label 1754
        ReturnValue4_1: int32 = Variable3 + 1
        Variable3 = ReturnValue4_1
        goto('L148')
        # Label 1828
        ReturnValue2_2: int32 = Variable1 + 1
        Variable1 = ReturnValue2_2
        goto('L623')
    

    def ClearAllSlots(self):
        self.mSlots.ClearChildren()
        
        Default__KismetArrayLibrary.Array_Clear(Ref[self.mInventorySlots])
    

    def CalcIndex(self, X: int32, Y: int32, Width: int32):
        ReturnValue: int32 = Y * Width
        ReturnValue_0: int32 = X + ReturnValue
        idx = ReturnValue_0
    

    def CreateSlot(self, index: int32, Row: int32, Column: int32):
        ReturnValue: int32 = self.mInventoryComponent.GetSizeLinear()
        ReturnValue_0: bool = index <= ReturnValue
        if not ReturnValue_0:
            goto('L637')
        ReturnValue_1: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_2: Ptr[Widget_InventorySlot] = Default__WidgetBlueprintLibrary.Create(self, Widget_InventorySlot, ReturnValue_1)
        Default__KismetSystemLibrary.SetIntPropertyByName(ReturnValue_2, "mSlotIdx", index)
        Default__KismetSystemLibrary.SetObjectPropertyByName(ReturnValue_2, "mCachedInventoryComponent", self.mInventoryComponent)
        Default__KismetSystemLibrary.SetBoolPropertyByName(ReturnValue_2, "mIsLocked", self.mIsLockedInventory)
        ReturnValue_2.mSmallSlot = self.mUseSmallSlots
        ReturnValue_3: Ptr[UniformGridSlot] = self.mSlots.AddChildToUniformGrid(ReturnValue_2)
        ReturnValue_3.SetRow(Row)
        ReturnValue_3.SetColumn(Column)
        
        ReturnValue_4: int32 = self.mInventorySlots.append(ReturnValue_2)
        Result = ReturnValue_2
    

    def Init(self, component: Ptr[FGInventoryComponent]):
        self.mInventoryComponent = component
        OutputDelegate.BindUFunction(self, OnInventoryResized)
        self.mInventoryComponent.ResizeInventoryDelegate.AddUnique(OutputDelegate)
        self.ClearAllSlots()
        self.CreateAllSlots()
    

    def OnInventoryResized(self, oldSize: int32, newSize: int32):
        ExecuteUbergraph_Widget_Inventory.K2Node_CustomEvent_oldSize = oldSize #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_Inventory.K2Node_CustomEvent_newSize = newSize #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_Inventory(34)
    

    def Destruct(self):
        self.ExecuteUbergraph_Widget_Inventory(67)
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_Inventory(201)
    

    def OnDragEnter(self):
        ExecuteUbergraph_Widget_Inventory.K2Node_Event_MyGeometry = MyGeometry #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_Inventory.K2Node_Event_PointerEvent1 = PointerEvent #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_Inventory.K2Node_Event_Operation1 = Operation #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_Inventory(425)
    

    def OnDragLeave(self):
        ExecuteUbergraph_Widget_Inventory.K2Node_Event_PointerEvent = PointerEvent #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_Inventory.K2Node_Event_Operation = Operation #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_Inventory(449)
    

    def OnMouseLeave(self):
        ExecuteUbergraph_Widget_Inventory.K2Node_Event_MouseEvent = MouseEvent #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_Inventory(473)
    

    def ExecuteUbergraph_Widget_Inventory(self):
        # Label 10
        self.OnInventoryMouseLeave.ProcessMulticastDelegate()
        # End
        self.ClearAllSlots()
        self.CreateAllSlots()
        # End
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(self.mInventoryComponent)
        if not ReturnValue:
            goto('L478')
        OutputDelegate.BindUFunction(self, OnInventoryResized)
        self.mInventoryComponent.ResizeInventoryDelegate.Remove(OutputDelegate)
        # End
        ReturnValue_0: Ptr[FGGameUserSettings] = Default__FGGameUserSettings.GetFGGameUserSettings()
        Variable1: bool = False
        ReturnValue_1: bool = ReturnValue_0.GetBoolOptionValue("FG.BigSlots")
        Variable: bool = self.mAlwaysBigSlot
        ReturnValue_2: bool = Not_PreBool(ReturnValue_1)
        
        switch = {
            False: ReturnValue_2,
            True: Variable1
        }
        self.mUseSmallSlots = switch.get(Variable, None)
        # End
        self.OnInventoryDragEnter.ProcessMulticastDelegate()
        # End
        self.OnInventoryDragLeave.ProcessMulticastDelegate()
        # End
        goto('L10')
    

    def OnInventoryMouseLeave__DelegateSignature(self):
        pass
    

    def OnInventoryDragLeave__DelegateSignature(self):
        pass
    

    def OnInventoryDragEnter__DelegateSignature(self):
        pass
    
