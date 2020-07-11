
from codegen.ue4_stub import *

from Script.UMG import AddChildToUniformGrid
from Script.Engine import SetClassPropertyByName
from Script.FactoryGame import GetCost
from Script.Engine import Not_PreBool
from Script.Engine import Default__KismetSystemLibrary
from Script.UMG import SetColumn
from Script.Engine import PlayerController
from Script.Engine import SetStructurePropertyByName
from Script.Engine import Default__KismetArrayLibrary
from Script.UMG import Default__WidgetBlueprintLibrary
from Script.UMG import UniformGridSlot
from Script.UMG import SetRow
from Script.UMG import Construct
from Script.FactoryGame import FGSchematic
from Script.UMG import UserWidget
from Game.FactoryGame.Buildable.Factory.TradingPost.Widget_TradingPost_PayOffGrid import ExecuteUbergraph_Widget_TradingPost_PayOffGrid
from Game.FactoryGame.Buildable.Factory.TradingPost.Widget_TradingPostPayOffSlot import Widget_TradingPostPayOffSlot
from Script.UMG import Create
from Script.FactoryGame import Default__FGSchematic
from Game.FactoryGame.Buildable.Factory.TradingPost.Widget_TradingPost import Widget_TradingPost
from Script.FactoryGame import ItemAmount
from Script.Engine import Array_Clear
from Script.Engine import IsValidClass

class Widget_TradingPost_PayOffGrid(UserWidget):
    mSchematic: TSubclassOf[FGSchematic]
    mTradingPostWidget: Ptr[Widget_TradingPost]
    mPayOffSlots: List[Ptr[Widget_TradingPostPayOffSlot]]
    
    def DropInventorySlotStack(self, InventorySlot: Ptr[Widget_InventorySlot]):
        ExecutionFlow.Push("L524")
        Variable: bool = False
        Variable_0: int32 = 0
        Variable_1: int32 = 0
        # Label 62
        ReturnValue: bool = Not_PreBool(Variable)
        
        ReturnValue_0: int32 = len(self.mPayOffSlots)
        ReturnValue_1: bool = Variable_0 <= ReturnValue_0
        ReturnValue_2: bool = ReturnValue and ReturnValue_1
        if not ReturnValue_2:
            goto('L426')
        Variable_1 = Variable_0
        ExecutionFlow.Push("L450")
        
        Item = None
        Item = self.mPayOffSlots[Variable_1]
        
        Result = None
        Item.DropOntoInventorySlot(InventorySlot, Ref[Result])
        LocalResult = Result
        if not LocalResult:
           goto(ExecutionFlow.Pop())
        Variable = True
        goto(ExecutionFlow.Pop())
        # Label 426
        Result = LocalResult
        # End
        # Label 450
        ReturnValue_3: int32 = Variable_0 + 1
        Variable_0 = ReturnValue_3
        goto('L62')
    

    def SetUpPayOffSlots(self, mSchematic: TSubclassOf[FGSchematic]):
        ExecutionFlow.Push("L988")
        self.mPayOffGrid.ClearChildren()
        
        Default__KismetArrayLibrary.Array_Clear(Ref[self.mPayOffSlots])
        ReturnValue: bool = Default__KismetSystemLibrary.IsValidClass(mSchematic)
        if not ReturnValue:
           goto(ExecutionFlow.Pop())
        Variable: int32 = 0
        Variable_0: int32 = 0
        # Label 189
        ReturnValue_0: List[ItemAmount] = Default__FGSchematic.GetCost(mSchematic)
        
        ReturnValue_1: int32 = len(ReturnValue_0)
        ReturnValue_2: bool = Variable <= ReturnValue_1
        if not ReturnValue_2:
           goto(ExecutionFlow.Pop())
        Variable_0 = Variable
        ExecutionFlow.Push("L914")
        ReturnValue_3: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_4: Ptr[Widget_TradingPostPayOffSlot] = Default__WidgetBlueprintLibrary.Create(self, Widget_TradingPostPayOffSlot, ReturnValue_3)
        ReturnValue_0 = Default__FGSchematic.GetCost(mSchematic)
        
        Item = None
        Item = ReturnValue_0[Variable_0]
        
        Item = None
        Default__KismetSystemLibrary.SetStructurePropertyByName(ReturnValue_4, "mItemAmount", Ref[Item])
        Default__KismetSystemLibrary.SetClassPropertyByName(ReturnValue_4, "mSchematic", mSchematic)
        ReturnValue_5: Ptr[UniformGridSlot] = self.mPayOffGrid.AddChildToUniformGrid(ReturnValue_4)
        ReturnValue_5.SetRow(0)
        ReturnValue_5.SetColumn(Variable_0)
        
        ReturnValue_6: int32 = self.mPayOffSlots.append(ReturnValue_4)
        goto(ExecutionFlow.Pop())
        # Label 914
        ReturnValue_7: int32 = Variable + 1
        Variable = ReturnValue_7
        goto('L189')
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_TradingPost_PayOffGrid(48)
    

    def ExecuteUbergraph_Widget_TradingPost_PayOffGrid(self):
        # Label 10
        self.Construct()
        self.SetUpPayOffSlots(self.mSchematic)
        # End
        goto('L10')
    
