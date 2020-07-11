
from codegen.ue4_stub import *

from Game.FactoryGame.Character.Player.BP_RemoteCallObject import BP_RemoteCallObject
from Script.Engine import Texture2D
from Script.Engine import EqualEqual_ClassClass
from Game.FactoryGame.Buildable.Factory.SpaceElevator.Widget_SpaceElevatorPayOffSlot import ExecuteUbergraph_Widget_SpaceElevatorPayOffSlot.K2Node_Event_MyGeometry
from Script.FactoryGame import FGGamePhaseManager
from Script.Engine import FClamp
from Game.FactoryGame.Buildable.Factory.SpaceElevator.Widget_SpaceElevatorPayOffSlot import ExecuteUbergraph_Widget_SpaceElevatorPayOffSlot.K2Node_Event_InDeltaTime
from Script.Engine import K2_SetTimerDelegate
from Script.FactoryGame import EGamePhase
from Script.Engine import Default__KismetNodeHelperLibrary
from Script.Engine import Conv_IntToFloat
from Script.SlateCore import Margin
from Script.FactoryGame import Default__FGGamePhaseManager
from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import Add_ByteByte
from Script.FactoryGame import Get
from Script.Engine import PlayerController
from Script.Engine import SetStructurePropertyByName
from Script.Engine import NotEqual_ClassClass
from Script.Engine import Default__KismetArrayLibrary
from Script.Engine import GameStateBase
from Script.Engine import FormatArgumentData
from Script.FactoryGame import GetItemName
from Script.UMG import ESlateVisibility
from Script.UMG import PlayAnimation
from Script.Engine import TimerHandle
from Script.UMG import StopAnimation
from Game.FactoryGame.Interface.UI.InGame.InventorySlots.Widget_InventorySlot import Widget_InventorySlot
from Script.Engine import GetValidValue
from Game.FactoryGame.Interface.UI.InGame.Widget_Tooltip import Widget_Tooltip
from Script.UMG import Default__WidgetBlueprintLibrary
from Script.Engine import EqualEqual_IntInt
from Script.Engine import Default__KismetTextLibrary
from Script.FactoryGame import GetSmallIcon
from Script.Engine import BooleanOR
from Script.Engine import Default__GameplayStatics
from Script.FactoryGame import GetCostForGamePhase
from Script.UMG import Tick
from Script.UMG import Widget
from Script.CoreUObject import Box2D
from Game.FactoryGame.Buildable.Factory.BP_DragNDropInventory import BP_DragNDropInventory
from Script.Engine import Format
from Script.Engine import LinearColorLerp
from Script.FactoryGame import GetGamePhase
from Script.UMG import WidgetAnimation
from Script.UMG import UserWidget
from Script.FactoryGame import GetRemoteCallObjectOfClass
from Script.UMG import UMGSequencePlayer
from Script.UMG import Create
from Script.FactoryGame import Default__FGItemDescriptor
from Script.Engine import GetGameState
from Script.CoreUObject import Vector2D
from Script.SlateCore import SlateBrush
from Script.SlateCore import SlateColor
from Game.FactoryGame.Character.Player.BP_PlayerController import BP_PlayerController
from Script.FactoryGame import ItemAmount
from Script.FactoryGame import FGBuildableSpaceElevator
from Script.Engine import IsValidClass
from Game.FactoryGame.Buildable.Factory.SpaceElevator.Widget_SpaceElevatorPayOffSlot import ExecuteUbergraph_Widget_SpaceElevatorPayOffSlot
from Script.Engine import Array_Clear
from Game.FactoryGame.Resource.Parts.SpaceElevatorBlocker.Desc_SpaceElevatorBlocker import Desc_SpaceElevatorBlocker
from Script.CoreUObject import LinearColor

class Widget_SpaceElevatorPayOffSlot(UserWidget):
    GlowAnim: Ptr[WidgetAnimation]
    AniDragDropSlot: Ptr[WidgetAnimation]
    mItemAmount: ItemAmount
    mCurrentPaidOff: int32
    mItemIndex: int32
    mSpaceElevator: Ptr[FGBuildableSpaceElevator]
    mGamePhaseCost: List[ItemAmount]
    padding = Namespace(Bottom=8, Left=8, Right=8, Top=8)
    
    def DropOntoInventorySlot(self, InventorySlot: Ptr[Widget_InventorySlot]):
        
        ItemClass = None
        InventorySlot.GetItemClass(Ref[ItemClass])
        ReturnValue: bool = self.mCurrentPaidOff <= self.mItemAmount.amount
        ReturnValue_0: bool = EqualEqual_ClassClass(ItemClass, self.mItemAmount.ItemClass)
        ReturnValue_1: bool = ReturnValue_0 and ReturnValue
        if not ReturnValue_1:
            goto('L454')
        ReturnValue_2: Ptr[PlayerController] = self.GetOwningPlayer()
        Controller: Ptr[BP_PlayerController] = Cast[BP_PlayerController](ReturnValue_2)
        bSuccess: bool = Controller
        ReturnValue_3: Ptr[BP_RemoteCallObject] = Controller.GetRemoteCallObjectOfClass(BP_RemoteCallObject)
        ReturnValue_3.Server_PayOffTowTruckUpgrade(self.mSpaceElevator, InventorySlot.mCachedInventoryComponent, InventorySlot.mSlotIdx)
        Result = True
        # End
        # Label 454
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
        # Label 61
        ReturnValue_0: uint8 = 2
        goto('L106')
        # Label 86
        ReturnValue_0 = 3
    

    def GetProgressBarVisibility(self):
        ReturnValue: bool = EqualEqual_IntInt(self.mItemAmount.amount, self.mCurrentPaidOff)
        ReturnValue_0: bool = self.mCurrentPaidOff <= 1
        ReturnValue_1: bool = BooleanOR(ReturnValue_0, ReturnValue)
        # Label 119
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
        # Label 61
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
        ReturnValue: bool = NotEqual_ClassClass(self.mItemAmount.ItemClass, Desc_SpaceElevatorBlocker)
        if not ReturnValue:
            goto('L609')
        # Label 61
        FormatArgumentData.ArgumentName = "1"
        FormatArgumentData.ArgumentValueType = 0
        FormatArgumentData.ArgumentValue = 
        FormatArgumentData.ArgumentValueInt = self.mItemAmount.amount
        # Label 194
        FormatArgumentData.ArgumentValueFloat = 0
        FormatArgumentData.ArgumentValueGender = 0
        FormatArgumentData1.ArgumentName = "0"
        FormatArgumentData1.ArgumentValueType = 0
        FormatArgumentData1.ArgumentValue = 
        FormatArgumentData1.ArgumentValueInt = self.mCurrentPaidOff
        FormatArgumentData1.ArgumentValueFloat = 0
        FormatArgumentData1.ArgumentValueGender = 0
        Array: List[FormatArgumentData] = [FormatArgumentData1, FormatArgumentData]
        ReturnValue_0: FText = Default__KismetTextLibrary.Format("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 520, 'Value': '{0} / {1}'}", Array)
        ReturnValue_1: FText = ReturnValue_0
        goto('L629')
        # Label 609
        ReturnValue_1 = 
    

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
            goto('L596')
        ReturnValue_0: Ptr[Texture2D] = Default__FGItemDescriptor.GetSmallIcon(self.mItemAmount.ItemClass)
        SlateBrush.ImageSize = self.mItemImage.Brush.ImageSize
        SlateBrush.Margin = self.mItemImage.Brush.Margin
        SlateBrush.TintColor = self.mItemImage.Brush.TintColor
        SlateBrush.ResourceObject = ReturnValue_0
        SlateBrush.DrawAs = self.mItemImage.Brush.DrawAs
        SlateBrush.Tiling = self.mItemImage.Brush.Tiling
        SlateBrush.Mirroring = self.mItemImage.Brush.Mirroring
        ReturnValue_1: SlateBrush = SlateBrush
        goto('L824')
        # Label 596
        ReturnValue_1 = SlateBrush(ImageSize = Vector2D(X = 32, Y = 32), Margin = Margin(Left = 0, Top = 0, Right = 0, Bottom = 0), TintColor = SlateColor(SpecifiedColor = LinearColor(R = 1, G = 1, B = 1, A = 1), ColorUseRule = 0), ResourceObject = None, ResourceName = "None", UVRegion = Box2D(Min = Vector2D(X = 0, Y = 0), Max = Vector2D(X = 0, Y = 0), bIsValid = 0), DrawAs = 3, Tiling = 0, Mirroring = 0, ImageType = 0, bIsDynamicallyLoaded = False, bHasUObject = False)
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_SpaceElevatorPayOffSlot(747)
    

    def Tick(self):
        ExecuteUbergraph_Widget_SpaceElevatorPayOffSlot.K2Node_Event_MyGeometry = MyGeometry #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_SpaceElevatorPayOffSlot.K2Node_Event_InDeltaTime = InDeltaTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_SpaceElevatorPayOffSlot(882)
    

    def GlowTimer(self):
        self.ExecuteUbergraph_Widget_SpaceElevatorPayOffSlot(1216)
    

    def ExecuteUbergraph_Widget_SpaceElevatorPayOffSlot(self):
        goto(ComputedJump("EntryPoint"))
        # Label 15
        Variable: bool = False
        self.StopAnimation(self.GlowAnim)
        goto(ExecutionFlow.Pop())
        # Label 46
        if not Variable:
            goto('L61')
        goto(ExecutionFlow.Pop())
        # Label 61
        Variable = True
        ReturnValue1: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.GlowAnim, 0, 0, 0, 1)
        goto(ExecutionFlow.Pop())
        # Label 119
        ExecutionFlow.Push("L441")
        
        Item = None
        Item = self.mGamePhaseCost[Variable_0]
        ReturnValue: bool = EqualEqual_ClassClass(Item.ItemClass, self.mItemAmount.ItemClass)
        if not ReturnValue:
           goto(ExecutionFlow.Pop())
        
        Item = None
        Item = self.mGamePhaseCost[Variable_0]
        ReturnValue_0: int32 = self.mItemAmount.amount - Item.amount
        self.mCurrentPaidOff = ReturnValue_0
        
        Default__KismetArrayLibrary.Array_Clear(Ref[self.mGamePhaseCost])
        goto(ExecutionFlow.Pop())
        # Label 441
        ReturnValue_1: int32 = Variable_0 + 1
        Variable_0: int32 = ReturnValue_1
        
        # Label 510
        ReturnValue_2: int32 = len(self.mGamePhaseCost)
        ReturnValue_3: bool = Variable_0 <= ReturnValue_2
        if not ReturnValue_3:
           goto(ExecutionFlow.Pop())
        Variable_0 = Variable_0
        goto('L119')
        # Label 649
        Variable_0 = 0
        Variable_0 = 0
        goto('L510')
        # Label 700
        Variable1: bool = False
        goto('L46')
        # Label 716
        if not Variable1:
            goto('L731')
        goto(ExecutionFlow.Pop())
        # Label 731
        Variable1 = True
        goto('L15')
        ReturnValue_4: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.AniDragDropSlot, 0, 0, 0, 1)
        OutputDelegate.BindUFunction(self, GlowTimer)
        ReturnValue_5: TimerHandle = Default__KismetSystemLibrary.K2_SetTimerDelegate(OutputDelegate, 0.20000000298023224, True)
        goto(ExecutionFlow.Pop())
        self.Tick(MyGeometry, InDeltaTime)
        ReturnValue_6: Ptr[GameStateBase] = Default__GameplayStatics.GetGameState(self)
        ReturnValue_7: Ptr[FGGamePhaseManager] = Default__FGGamePhaseManager.Get(ReturnValue_6)
        ReturnValue_8: uint8 = ReturnValue_7.GetGamePhase()
        ReturnValue_9: uint8 = Add_ByteByte(ReturnValue_8, 1)
        ReturnValue_10: uint8 = Default__KismetNodeHelperLibrary.GetValidValue(EGamePhase, ReturnValue_9)
        
        ReturnValue_7.GetCostForGamePhase(ReturnValue_10, Ref[self.mGamePhaseCost])
        goto('L649')
        ReturnValue_11: bool = EqualEqual_IntInt(self.mCurrentPaidOff, self.mItemAmount.amount)
        if not ReturnValue_11:
            goto('L700')
        goto('L716')
    
