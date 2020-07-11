
from codegen.ue4_stub import *

from Script.UMG import GetParent
from Game.FactoryGame.Buildable.-Shared.Widgets.Widget_Manufacturing import Widget_Manufacturing
from Script.Engine import Delay
from Script.UMG import GetChildIndex
from Script.FactoryGame import EResourceForm
from Script.UMG import GetChildrenCount
from Script.FactoryGame import GetInputInventory
from Script.FactoryGame import Default__FGInventoryLibrary
from Script.Engine import LatentActionInfo
from Script.Engine import Default__KismetSystemLibrary
from Script.FactoryGame import GetProducts
from Script.FactoryGame import GetProductionSuffixFromFormType
from Script.Engine import Default__KismetArrayLibrary
from Script.Engine import FormatArgumentData
from Script.FactoryGame import GetItemName
from Script.UMG import ESlateVisibility
from Script.Engine import Conv_FloatToText
from Script.FactoryGame import GetForm
from Script.FactoryGame import FGInventoryComponent
from Script.Engine import IsValid
from Script.FactoryGame import GetIngredients
from Script.Engine import EqualEqual_IntInt
from Script.Engine import Default__KismetTextLibrary
from Game.FactoryGame.Buildable.-Shared.Widgets.Widget_ManufacturingIOSlot import ExecuteUbergraph_Widget_ManufacturingIOSlot
from Script.FactoryGame import GetAmountConvertedFromItemAmount
from Script.FactoryGame import Default__FGRecipe
from Script.UMG import PanelWidget
from Script.Engine import Format
from Script.Engine import NotEqual_ByteByte
from Script.UMG import UserWidget
from Script.FactoryGame import Default__FGItemDescriptor
from Script.Engine import Min
from Script.FactoryGame import ItemAmount
from Script.FactoryGame import GetOutputInventory
from Game.FactoryGame.Buildable.-Shared.Widgets.Widget_ManufacturingIOSlot import ExecuteUbergraph_Widget_ManufacturingIOSlot.K2Node_CustomEvent_SlotIdx

class Widget_ManufacturingIOSlot(UserWidget):
    mManufacturingWidget: Ptr[Widget_Manufacturing]
    mIsOutput: bool
    mCachedInventorySlot: Ptr[FGInventoryComponent]
    InputObject: Ptr[UserWidget]
    
    def ConstructFromManufacturingWidget(self, WidgetManufacturing: Ptr[Widget_Manufacturing]):
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(WidgetManufacturing)
        if not ReturnValue:
            goto('L420')
        Variable: bool = self.mIsOutput
        ReturnValue_0: Ptr[FGInventoryComponent] = self.mManufacturingWidget.mBuildableManufacturer.GetOutputInventory()
        ReturnValue_1: Ptr[FGInventoryComponent] = self.mManufacturingWidget.mBuildableManufacturer.GetInputInventory()
        
        switch = {
            False: ReturnValue_1,
            True: ReturnValue_0
        }
        self.mCachedInventorySlot = switch.get(Variable, None)
        if not self.mIsOutput:
            goto('L420')
        self.Widget_CostSlotWrapper.SetVisibility(1)
        self.Widget_InventorySlot.SetVisibility(0)
        self.Widget_InventorySlot.mCachedInventoryComponent = self.mCachedInventorySlot
        self.UpdateOutputTooltip()
    

    def UpdateOutputTooltip(self):
        
        itemAmount = None
        self.GetItemAmount(Ref[itemAmount])
        self.Widget_InventorySlot.mFilterItemDescriptor = itemAmount.ItemClass
    

    def GetDividerTopVisibility(self):
        if not self.mIsOutput:
            goto('L39')
        ReturnValue = 1
        goto('L325')
        # Label 39
        ReturnValue_0: Ptr[PanelWidget] = self.GetParent()
        ReturnValue_1: int32 = ReturnValue_0.GetChildIndex(self)
        ReturnValue_2: int32 = ReturnValue_0.GetChildrenCount()
        ReturnValue_3: bool = EqualEqual_IntInt(ReturnValue_1, 0)
        ReturnValue_4: bool = ReturnValue_2 <= 4
        ReturnValue_5: bool = ReturnValue_4 and ReturnValue_3
        if not ReturnValue_5:
            goto('L305')
        ReturnValue = 0
        goto('L325')
        # Label 305
        ReturnValue = 1
    

    def GetDividerVisibility(self):
        Variable: uint8 = 1
        Variable1: uint8 = 0
        Variable_0: bool = self.mIsOutput
        
        switch = {
            False: Variable1,
            True: Variable
        }
        ReturnValue = switch.get(Variable_0, None)
    

    def GetInputInfoVisibility(self):
        Variable: uint8 = 1
        Variable1: uint8 = 0
        Variable_0: bool = self.mIsOutput
        
        switch = {
            False: Variable1,
            True: Variable
        }
        ReturnValue = switch.get(Variable_0, None)
    

    def GetNumPerSecond(self):
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(self.mManufacturingWidget)
        if not ReturnValue:
            goto('L421')
        
        itemAmount = None
        self.GetItemAmount(Ref[itemAmount])
        
        itemAmount = None
        itemClass = None
        amountConverted = None
        Default__FGInventoryLibrary.GetAmountConvertedFromItemAmount(Ref[itemAmount], Ref[itemClass], Ref[amountConverted])
        ReturnValue_0: float = self.mManufacturingWidget.mBuildableManufacturer.GetProductionCycleTime()
        ReturnValue_1: float = amountConverted / ReturnValue_0
        ReturnValue_2: float = ReturnValue_1 * 60
        ReturnValue_3: FText = Default__KismetTextLibrary.Conv_FloatToText(ReturnValue_2, 1, False, True, 1, 324, 0, 3)
        ReturnValue_4: FText = ReturnValue_3
    

    def GetOutputSlotVisibility(self):
        Variable: uint8 = 0
        Variable1: uint8 = 1
        Variable_0: bool = self.mIsOutput
        
        switch = {
            False: Variable1,
            True: Variable
        }
        ReturnValue = switch.get(Variable_0, None)
    

    def GetItemNum(self):
        
        itemAmount = None
        self.GetItemAmount(Ref[itemAmount])
        
        itemAmount = None
        itemClass = None
        amountConverted = None
        Default__FGInventoryLibrary.GetAmountConvertedFromItemAmount(Ref[itemAmount], Ref[itemClass], Ref[amountConverted])
        ReturnValue: FText = Default__KismetTextLibrary.Conv_FloatToText(amountConverted, 0, False, True, 1, 324, 0, 3)
        ReturnValue_0: FText = ReturnValue
    

    def GetItemAmount(self):
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(self.mManufacturingWidget)
        if not ReturnValue:
            goto('L650')
        ReturnValue_0: List[ItemAmount] = Default__FGRecipe.GetIngredients(self.mManufacturingWidget.mActivatedRecipe)
        
        ReturnValue_1: int32 = len(ReturnValue_0)
        ReturnValue_2: int32 = ReturnValue_1 - 1
        ReturnValue_3: List[ItemAmount] = Default__FGRecipe.GetProducts(self.mManufacturingWidget.mActivatedRecipe, False)
        
        Item = None
        Item = ReturnValue_3[0]
        Variable: bool = self.mIsOutput
        ReturnValue_4: Ptr[PanelWidget] = self.GetParent()
        ReturnValue_5: int32 = ReturnValue_4.GetChildIndex(self)
        ReturnValue_6: int32 = Min(ReturnValue_2, ReturnValue_5)
        
        Item1 = None
        Item1 = ReturnValue_0[ReturnValue_6]
        
        switch = {
            False: Item1,
            True: Item
        }
        ItemAmount = switch.get(Variable, None)
    

    def GetItemName(self):
        
        itemAmount = None
        self.GetItemAmount(Ref[itemAmount])
        Variable: FText = 
        ReturnValue: FText = Default__FGItemDescriptor.GetItemName(itemAmount.ItemClass)
        ReturnValue_0: uint8 = Default__FGItemDescriptor.GetForm(itemAmount.ItemClass)
        FormatArgumentData.ArgumentName = "name"
        FormatArgumentData.ArgumentValueType = 4
        FormatArgumentData.ArgumentValue = ReturnValue
        FormatArgumentData.ArgumentValueInt = 0
        FormatArgumentData.ArgumentValueFloat = 0
        FormatArgumentData.ArgumentValueGender = 0
        ReturnValue_1: bool = NotEqual_ByteByte(ReturnValue_0, 1)
        ReturnValue_2: FText = Default__FGInventoryLibrary.GetProductionSuffixFromFormType(ReturnValue_0)
        Variable_0: bool = ReturnValue_1
        FormatArgumentData1.ArgumentName = "suffix"
        FormatArgumentData1.ArgumentValueType = 4
        
        switch = {
            False: Variable,
            True: ReturnValue_2
        }
        FormatArgumentData1.ArgumentValue = switch.get(Variable_0, None)
        FormatArgumentData1.ArgumentValueInt = 0
        FormatArgumentData1.ArgumentValueFloat = 0
        FormatArgumentData1.ArgumentValueGender = 0
        Array: List[FormatArgumentData] = [FormatArgumentData1]
        ReturnValue_3: FText = Default__KismetTextLibrary.Format("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 787, 'Value': '{suffix} '}", Array)
        FormatArgumentData2.ArgumentName = "suffix"
        FormatArgumentData2.ArgumentValueType = 4
        FormatArgumentData2.ArgumentValue = ReturnValue_3
        FormatArgumentData2.ArgumentValueInt = 0
        FormatArgumentData2.ArgumentValueFloat = 0
        FormatArgumentData2.ArgumentValueGender = 0
        Array1: List[FormatArgumentData] = [FormatArgumentData2, FormatArgumentData]
        ReturnValue1: FText = Default__KismetTextLibrary.Format("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 1117, 'Value': '{suffix}{name}'}", Array1)
        ReturnValue_4: FText = ReturnValue1
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_ManufacturingIOSlot(181)
    

    def Set CostSlot(self, slotIdx: int32):
        ExecuteUbergraph_Widget_ManufacturingIOSlot.K2Node_CustomEvent_SlotIdx = slotIdx #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_ManufacturingIOSlot(186)
    

    def ExecuteUbergraph_Widget_ManufacturingIOSlot(self):
        goto(ComputedJump("EntryPoint"))
        # Label 15
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(self.mManufacturingWidget)
        if not ReturnValue:
            goto('L104')
        self.ConstructFromManufacturingWidget(self.mManufacturingWidget)
        goto(ExecutionFlow.Pop())
        # Label 104
        Default__KismetSystemLibrary.Delay(self, 0.10000000149011612, LatentActionInfo(Linkage = 15, UUID = -1694640019, ExecutionFunction = "ExecuteUbergraph_Widget_ManufacturingIOSlot", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        goto('L15')
        
        itemAmount = None
        self.GetItemAmount(Ref[itemAmount])
        self.Widget_CostSlotWrapper.Setup CostIcon(None, itemAmount, self.mCachedInventorySlot, SlotIdx, 0, False, False, False)
        goto(ExecutionFlow.Pop())
    
