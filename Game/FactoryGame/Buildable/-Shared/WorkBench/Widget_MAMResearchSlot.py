
from codegen.ue4_stub import *

from Script.Engine import Texture2D
from Script.Engine import EqualEqual_ClassClass
from Script.Engine import FClamp
from Script.Engine import GreaterEqual_IntInt
from Script.Engine import Conv_IntToFloat
from Script.SlateCore import Margin
from Script.Engine import Default__KismetSystemLibrary
from Game.FactoryGame.Buildable.-Shared.WorkBench.Widget_MAMResearchSlot import ExecuteUbergraph_Widget_MAMResearchSlot.K2Node_Event_MyGeometry
from Game.FactoryGame.Buildable.-Shared.WorkBench.Widget_MAMResearchSlot import ExecuteUbergraph_Widget_MAMResearchSlot.K2Node_Event_InDeltaTime
from Script.Engine import PlayerController
from Script.FactoryGame import FGResearchRecipe
from Script.Engine import SetStructurePropertyByName
from Script.Engine import Default__KismetArrayLibrary
from Script.Engine import FormatArgumentData
from Script.FactoryGame import GetItemName
from Script.UMG import ESlateVisibility
from Game.FactoryGame.Buildable.-Shared.WorkBench.Widget_MAMResearchSlot import ExecuteUbergraph_Widget_MAMResearchSlot
from Script.UMG import PlayAnimation
from Script.UMG import StopAnimation
from Game.FactoryGame.Interface.UI.InGame.InventorySlots.Widget_InventorySlot import Widget_InventorySlot
from Game.FactoryGame.Interface.UI.InGame.Widget_Tooltip import Widget_Tooltip
from Script.UMG import Default__WidgetBlueprintLibrary
from Script.Engine import EqualEqual_IntInt
from Script.Engine import Default__KismetTextLibrary
from Script.FactoryGame import GetSmallIcon
from Script.UMG import SetOpacity
from Script.Engine import BooleanOR
from Script.UMG import Tick
from Script.UMG import Widget
from Script.CoreUObject import Box2D
from Game.FactoryGame.Buildable.Factory.BP_DragNDropInventory import BP_DragNDropInventory
from Script.Engine import Format
from Script.Engine import LinearColorLerp
from Script.UMG import WidgetAnimation
from Script.UMG import UserWidget
from Script.UMG import UMGSequencePlayer
from Script.UMG import Create
from Script.FactoryGame import Default__FGItemDescriptor
from Script.Engine import Array_IsValidIndex
from Script.CoreUObject import Vector2D
from Script.SlateCore import SlateBrush
from Script.SlateCore import SlateColor
from Script.FactoryGame import ItemAmount
from Script.Engine import IsValidClass
from Script.CoreUObject import LinearColor

class Widget_MAMResearchSlot(UserWidget):
    AniDragDropSlot: Ptr[WidgetAnimation]
    mItemAmount: ItemAmount
    mCurrentPaidOff: int32
    mItemIndex: int32
    mResearchRecipe: TSubclassOf[FGResearchRecipe]
    mResearchCost: List[ItemAmount]
    
    def DropOntoInventorySlot(self, InventorySlot: Ptr[Widget_InventorySlot]):
        
        ItemClass = None
        InventorySlot.GetItemClass(Ref[ItemClass])
        ReturnValue: bool = EqualEqual_ClassClass(ItemClass, self.mItemAmount.ItemClass)
        ReturnValue_0: bool = self.mCurrentPaidOff <= self.mItemAmount.amount
        ReturnValue_1: bool = ReturnValue and ReturnValue_0
        if not ReturnValue_1:
            goto('L196')
        # End
        # Label 196
        Result = False
    

    def GetCustomTooltip(self):
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_0: Ptr[Widget_Tooltip] = Default__WidgetBlueprintLibrary.Create(self, Widget_Tooltip, ReturnValue)
        
        Default__KismetSystemLibrary.SetStructurePropertyByName(ReturnValue_0, "mItemDescriptor", Ref[self.mItemAmount])
        ReturnValue_1: Ptr[Widget] = ReturnValue_0
    

    def GetPaidOffSlotVisibility(self):
        ReturnValue: bool = EqualEqual_IntInt(self.mItemAmount.amount, self.mCurrentPaidOff)
        if not ReturnValue:
            goto('L86')
        ReturnValue_0: uint8 = 2
        goto('L106')
        # Label 86
        ReturnValue_0 = 3
    

    def GetProgressBarVisibility(self):
        ReturnValue: bool = EqualEqual_IntInt(self.mItemAmount.amount, self.mCurrentPaidOff)
        ReturnValue_0: bool = self.mCurrentPaidOff <= 1
        ReturnValue_1: bool = BooleanOR(ReturnValue_0, ReturnValue)
        if not ReturnValue_1:
            goto('L158')
        ReturnValue_2: uint8 = 2
        goto('L178')
        # Label 158
        ReturnValue_2 = 3
    

    def GetPaidOffColorFeedback(self):
        ReturnValue: float = Conv_IntToFloat(self.mCurrentPaidOff)
        ReturnValue_0: float = FClamp(ReturnValue, 0, 1)
        ReturnValue_1: LinearColor = LinearColorLerp(LinearColor(R = 0, G = 0.10640200227499008, B = 0.25, A = 1), LinearColor(R = 0.06055000051856041, G = 0.5643249750137329, B = 0.8650000095367432, A = 1), ReturnValue_0)
        SlateColor.SpecifiedColor = ReturnValue_1
        SlateColor.ColorUseRule = 0
        ReturnValue_2: SlateColor = SlateColor
    

    def GetPaidOffFeedbackImage(self):
        ReturnValue: bool = EqualEqual_IntInt(self.mCurrentPaidOff, self.mItemAmount.amount)
        if not ReturnValue:
            goto('L86')
        ReturnValue_0: uint8 = 3
        goto('L106')
        # Label 86
        ReturnValue_0 = 2
    

    def GetProgressbarPercent(self):
        ReturnValue: float = Conv_IntToFloat(self.mCurrentPaidOff)
        ReturnValue1: float = Conv_IntToFloat(self.mItemAmount.amount)
        ReturnValue_0: float = ReturnValue / ReturnValue1
        ReturnValue_1: float = FClamp(ReturnValue_0, 0, 1)
        ReturnValue_2: float = ReturnValue_1
    

    def OnDrop(self):
        numToPayOff = 0
        Inventory: Ptr[BP_DragNDropInventory] = Cast[BP_DragNDropInventory](Operation)
        bSuccess: bool = Inventory
        if not bSuccess:
            goto('L259')
        Slot: Ptr[Widget_InventorySlot] = Cast[Widget_InventorySlot](Inventory.payload)
        bSuccess1: bool = Slot
        if not bSuccess1:
            goto('L275')
        
        Result = None
        self.DropOntoInventorySlot(Slot, Ref[Result])
        ReturnValue = Result
        goto('L286')
        # Label 259
        ReturnValue = False
        goto('L286')
        # Label 275
        ReturnValue = False
    

    def GetItemQuotaText(self):
        FormatArgumentData.ArgumentName = "0"
        FormatArgumentData.ArgumentValueType = 0
        FormatArgumentData.ArgumentValue = 
        FormatArgumentData.ArgumentValueInt = self.mCurrentPaidOff
        FormatArgumentData.ArgumentValueFloat = 0
        FormatArgumentData.ArgumentValueGender = 0
        FormatArgumentData1.ArgumentName = "1"
        FormatArgumentData1.ArgumentValueType = 0
        FormatArgumentData1.ArgumentValue = 
        FormatArgumentData1.ArgumentValueInt = self.mItemAmount.amount
        FormatArgumentData1.ArgumentValueFloat = 0
        FormatArgumentData1.ArgumentValueGender = 0
        Array: List[FormatArgumentData] = [FormatArgumentData, FormatArgumentData1]
        ReturnValue: FText = Default__KismetTextLibrary.Format("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 459, 'Value': '{0} / {1}'}", Array)
        ReturnValue_0: FText = ReturnValue
    

    def GetItemText(self):
        ReturnValue: bool = Default__KismetSystemLibrary.IsValidClass(self.mItemAmount.ItemClass)
        if not ReturnValue:
            goto('L174')
        ReturnValue_0: FText = Default__FGItemDescriptor.GetItemName(self.mItemAmount.ItemClass)
        ReturnValue_1: FText = ReturnValue_0
        goto('L194')
        # Label 174
        ReturnValue_1 = 
    

    def GetItemImage(self):
        ReturnValue: bool = Default__KismetSystemLibrary.IsValidClass(self.mItemAmount.ItemClass)
        if not ReturnValue:
            goto('L706')
        SlateColor.SpecifiedColor = LinearColor(R = 0, G = 0, B = 0, A = 0.4000000059604645)
        SlateColor.ColorUseRule = 0
        SlateColor1.SpecifiedColor = LinearColor(R = 1, G = 1, B = 1, A = 1)
        SlateColor1.ColorUseRule = 0
        ReturnValue_0: bool = self.mCurrentPaidOff > 0
        Variable: bool = ReturnValue_0
        ReturnValue_1: Ptr[Texture2D] = Default__FGItemDescriptor.GetSmallIcon(self.mItemAmount.ItemClass)
        SlateBrush.ImageSize = Vector2D(X = 64, Y = 64)
        SlateBrush.Margin = Margin(Left = 0, Top = 0, Right = 0, Bottom = 0)
        
        switch = {
            False: SlateColor,
            True: SlateColor1
        }
        SlateBrush.TintColor = switch.get(Variable, None)
        SlateBrush.ResourceObject = ReturnValue_1
        SlateBrush.DrawAs = 3
        SlateBrush.Tiling = 0
        SlateBrush.Mirroring = 0
        ReturnValue_2: SlateBrush = SlateBrush
        goto('L934')
        # Label 706
        ReturnValue_2 = SlateBrush(ImageSize = Vector2D(X = 32, Y = 32), Margin = Margin(Left = 0, Top = 0, Right = 0, Bottom = 0), TintColor = SlateColor(SpecifiedColor = LinearColor(R = 1, G = 1, B = 1, A = 1), ColorUseRule = 0), ResourceObject = None, ResourceName = "None", UVRegion = Box2D(Min = Vector2D(X = 0, Y = 0), Max = Vector2D(X = 0, Y = 0), bIsValid = 0), DrawAs = 3, Tiling = 0, Mirroring = 0, ImageType = 0, bIsDynamicallyLoaded = False, bHasUObject = False)
    

    def Tick(self):
        ExecuteUbergraph_Widget_MAMResearchSlot.K2Node_Event_MyGeometry = MyGeometry #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_MAMResearchSlot.K2Node_Event_InDeltaTime = InDeltaTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_MAMResearchSlot(394)
    

    def ExecuteUbergraph_Widget_MAMResearchSlot(self):
        goto(ComputedJump("EntryPoint"))
        # Label 15
        Array: List[ItemAmount] = []
        self.mResearchCost = Array
        
        ReturnValue: bool = Default__KismetArrayLibrary.Array_IsValidIndex(self.mItemIndex, Ref[self.mResearchCost])
        if not ReturnValue:
            goto('L229')
        ReturnValue_0: int32 = self.mItemAmount.amount - self.mResearchCost[self.mItemIndex].amount
        self.mCurrentPaidOff = ReturnValue_0
        goto(ExecutionFlow.Pop())
        # Label 229
        self.mCurrentPaidOff = 0
        goto(ExecutionFlow.Pop())
        # Label 253
        Variable: bool = False
        self.StopAnimation(self.AniDragDropSlot)
        self.mSlotBg.SetOpacity(1)
        goto(ExecutionFlow.Pop())
        # Label 321
        if not Variable:
            goto('L336')
        goto(ExecutionFlow.Pop())
        # Label 336
        Variable = True
        ReturnValue_1: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.AniDragDropSlot, 0, 0, 0, 1)
        goto(ExecutionFlow.Pop())
        self.Tick(MyGeometry, InDeltaTime)
        ExecutionFlow.Push("L15")
        ReturnValue_2: bool = GreaterEqual_IntInt(self.mCurrentPaidOff, self.mItemAmount.amount)
        if not ReturnValue_2:
            goto('L503')
        if not Variable1:
            goto('L519')
        goto(ExecutionFlow.Pop())
        # Label 503
        Variable1: bool = False
        goto('L321')
        # Label 519
        Variable1 = True
        goto('L253')
    
