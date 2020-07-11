
from codegen.ue4_stub import *

from Game.FactoryGame.Character.Player.BP_RemoteCallObject import BP_RemoteCallObject
from Game.FactoryGame.Buildable.Factory.TradingPost.Widget_TradingPostPayOffSlot import ExecuteUbergraph_Widget_TradingPostPayOffSlot.K2Node_Event_MyGeometry
from Script.AkAudio import PostAkEvent
from Script.Engine import Texture2D
from Script.Engine import EqualEqual_ClassClass
from Script.Engine import FClamp
from Script.Engine import Pawn
from Script.UMG import OverlaySlot
from Game.FactoryGame.Interface.UI.Audio.WorkBench.Play_UI_WorkBench_MouseOver import Play_UI_WorkBench_MouseOver
from Script.UMG import Default__WidgetLayoutLibrary
from Script.UMG import SetJustification
from Script.Engine import Conv_IntToFloat
from Script.UMG import SlotAsOverlaySlot
from Script.SlateCore import Margin
from Script.Engine import Not_PreBool
from Script.Engine import Ease
from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import EqualEqual_FloatFloat
from Script.FactoryGame import Get
from Script.Engine import PlayerController
from Script.Engine import SetStructurePropertyByName
from Script.UMG import SetHorizontalAlignment
from Script.Engine import Default__KismetArrayLibrary
from Script.UMG import SetRenderTranslation
from Script.Engine import FormatArgumentData
from Script.UMG import ESlateVisibility
from Script.FactoryGame import GetItemName
from Script.UMG import PlayAnimation
from Script.Engine import GameStateBase
from Script.UMG import StopAnimation
from Script.FactoryGame import FGInventoryComponent
from Script.Engine import GetWorldDeltaSeconds
from Game.FactoryGame.Interface.UI.InGame.InventorySlots.Widget_InventorySlot import Widget_InventorySlot
from Game.FactoryGame.Interface.UI.InGame.Widget_Tooltip import Widget_Tooltip
from Game.FactoryGame.Buildable.Factory.TradingPost.Widget_TradingPostPayOffSlot import ExecuteUbergraph_Widget_TradingPostPayOffSlot.K2Node_Event_InDeltaTime
from Script.UMG import Default__WidgetBlueprintLibrary
from Script.UMG import SetColorAndOpacity
from Script.Engine import Conv_IntToText
from Game.FactoryGame.Buildable.Factory.TradingPost.Widget_TradingPostPayOffSlot import ExecuteUbergraph_Widget_TradingPostPayOffSlot
from Game.FactoryGame.Buildable.Factory.TradingPost.Widget_TradingPostPayOffSlot import ExecuteUbergraph_Widget_TradingPostPayOffSlot.K2Node_CustomEvent_SchematicManager
from Script.Engine import EqualEqual_IntInt
from Script.Engine import Default__KismetTextLibrary
from Script.FactoryGame import GetSmallIcon
from Game.FactoryGame.Buildable.Factory.TradingPost.Widget_TradingPostPayOffSlot import ExecuteUbergraph_Widget_TradingPostPayOffSlot.K2Node_Event_MouseEvent
from Script.Engine import Default__GameplayStatics
from Script.Engine import BooleanOR
from Script.UMG import Tick
from Script.UMG import Widget
from Script.CoreUObject import Box2D
from Script.FactoryGame import GetPaidOffCostFor
from Game.FactoryGame.Buildable.Factory.BP_DragNDropInventory import BP_DragNDropInventory
from Script.Engine import Format
from Script.Engine import LinearColorLerp
from Script.FactoryGame import FGSchematic
from Script.UMG import WidgetAnimation
from Script.AkAudio import Default__AkGameplayStatics
from Script.UMG import UserWidget
from Script.FactoryGame import IsShipAtTradingPost
from Script.FactoryGame import GetRemoteCallObjectOfClass
from Game.FactoryGame.Buildable.Factory.TradingPost.Widget_TradingPostPayOffSlot import ExecuteUbergraph_Widget_TradingPostPayOffSlot.K2Node_Event_MyGeometry1
from Game.FactoryGame.Interface.UI.HUDHelpers.HUDHelpers import Default__HUDHelpers
from Script.UMG import GetOwningPlayerPawn
from Script.FactoryGame import FGSchematicManager
from Script.UMG import UMGSequencePlayer
from Script.UMG import Create
from Script.FactoryGame import Default__FGItemDescriptor
from Script.Engine import GetGameState
from Script.CoreUObject import Vector2D
from Script.SlateCore import SlateBrush
from Script.SlateCore import SlateColor
from Game.FactoryGame.Character.Player.BP_PlayerController import BP_PlayerController
from Script.FactoryGame import ItemAmount
from Script.AkAudio import AkComponent
from Script.FactoryGame import Default__FGSchematicManager
from Script.Engine import IsValidClass
from Script.CoreUObject import LinearColor

class Widget_TradingPostPayOffSlot(UserWidget):
    EmptyAnim: Ptr[WidgetAnimation]
    AniDragDropSlot: Ptr[WidgetAnimation]
    mItemAmount: ItemAmount
    mSchematic: TSubclassOf[FGSchematic]
    mCurrentPaidOff: int32
    IsHovered_0: bool
    CachedInventory: Ptr[FGInventoryComponent]
    T: float
    LastValue: float
    
    def StopEmptyAnim(self):
        self.StopAnimation(self.EmptyAnim)
        LinearColor.R = 1
        LinearColor.G = 1
        LinearColor.B = 1
        LinearColor.A = 1
        self.mItemImage.SetColorAndOpacity(LinearColor)
    

    def DropOntoInventorySlot(self, InventorySlot: Ptr[Widget_InventorySlot]):
        ReturnValue: Ptr[FGSchematicManager] = Default__FGSchematicManager.Get(self)
        ReturnValue_0: bool = ReturnValue.IsShipAtTradingPost()
        
        ItemClass = None
        InventorySlot.GetItemClass(Ref[ItemClass])
        ReturnValue_1: bool = self.mCurrentPaidOff <= self.mItemAmount.amount
        ReturnValue_2: bool = EqualEqual_ClassClass(ItemClass, self.mItemAmount.ItemClass)
        ReturnValue_3: bool = ReturnValue_2 and ReturnValue_1
        ReturnValue1: bool = ReturnValue_3 and ReturnValue_0
        if not ReturnValue1:
            goto('L577')
        ReturnValue_4: Ptr[PlayerController] = self.GetOwningPlayer()
        Controller: Ptr[BP_PlayerController] = Cast[BP_PlayerController](ReturnValue_4)
        bSuccess: bool = Controller
        ReturnValue_5: Ptr[BP_RemoteCallObject] = Controller.GetRemoteCallObjectOfClass(BP_RemoteCallObject)
        ReturnValue_5.Server_PayOffOnSchematic(self.mSchematic, InventorySlot.mCachedInventoryComponent, InventorySlot.mSlotIdx)
        Result = True
        # End
        # Label 577
        Result = False
    

    def GetSlotBackgroundBrush(self):
        ReturnValue: bool = EqualEqual_IntInt(self.mCurrentPaidOff, self.mItemAmount.amount)
        if not ReturnValue:
            goto('L597')
        self.StopAnimation(self.AniDragDropSlot)
        
        Text = None
        Graphics = None
        Default__HUDHelpers.GetFactoryGameDarkGray(self, Ref[Text], Ref[Graphics])
        SlateBrush1.ImageSize = self.PayOffSlotBG.Brush.ImageSize
        SlateBrush1.Margin = self.PayOffSlotBG.Brush.Margin
        SlateBrush1.TintColor = Text
        SlateBrush1.ResourceObject = self.PayOffSlotBG.Brush.ResourceObject
        SlateBrush1.DrawAs = self.PayOffSlotBG.Brush.DrawAs
        SlateBrush1.Tiling = self.PayOffSlotBG.Brush.Tiling
        SlateBrush1.Mirroring = self.PayOffSlotBG.Brush.Mirroring
        ReturnValue_0: SlateBrush = SlateBrush1
        goto('L1109')
        
        Text = None
        Graphics = None
        # Label 597
        Default__HUDHelpers.GetFactoryGameLightGray(self, Ref[Text], Ref[Graphics])
        SlateBrush.ImageSize = self.PayOffSlotBG.Brush.ImageSize
        SlateBrush.Margin = self.PayOffSlotBG.Brush.Margin
        SlateBrush.TintColor = Text
        SlateBrush.ResourceObject = self.PayOffSlotBG.Brush.ResourceObject
        SlateBrush.DrawAs = self.PayOffSlotBG.Brush.DrawAs
        SlateBrush.Tiling = self.PayOffSlotBG.Brush.Tiling
        SlateBrush.Mirroring = self.PayOffSlotBG.Brush.Mirroring
        ReturnValue_0 = SlateBrush
    

    def GetDarkGrayColor(self):
        
        Text = None
        Graphics = None
        Default__HUDHelpers.GetFactoryGameDarkGray(self, Ref[Text], Ref[Graphics])
        ReturnValue = Graphics
    

    def GetProgressbarPercent(self):
        LerpTime = 0.5
        if not False:
            goto('L57')
        ReturnValue = 1
        goto('L1226')
        # Label 57
        ReturnValue_0: float = Default__GameplayStatics.GetWorldDeltaSeconds(self)
        ReturnValue1: float = ReturnValue_0 / LerpTime
        ReturnValue_1: float = ReturnValue1 + self.T
        self.T = ReturnValue_1
        ReturnValue_2: float = FClamp(self.T, 0, 1)
        ReturnValue_3: float = Conv_IntToFloat(self.mItemAmount.amount)
        ReturnValue1_0: float = Conv_IntToFloat(self.mCurrentPaidOff)
        ReturnValue_4: float = ReturnValue1_0 / ReturnValue_3
        ReturnValue1_1: float = FClamp(ReturnValue_4, 0, 1)
        ReturnValue_5: float = Ease(self.LastValue, ReturnValue1_1, ReturnValue_2, 7, 2, 2)
        ReturnValue_6: bool = EqualEqual_FloatFloat(ReturnValue_5, ReturnValue1_1)
        if not ReturnValue_6:
            goto('L909')
        ReturnValue_2 = FClamp(self.T, 0, 1)
        ReturnValue_3 = Conv_IntToFloat(self.mItemAmount.amount)
        ReturnValue1_0 = Conv_IntToFloat(self.mCurrentPaidOff)
        ReturnValue_4 = ReturnValue1_0 / ReturnValue_3
        ReturnValue1_1 = FClamp(ReturnValue_4, 0, 1)
        ReturnValue_5 = Ease(self.LastValue, ReturnValue1_1, ReturnValue_2, 7, 2, 2)
        self.LastValue = ReturnValue_5
        self.T = 0
        # Label 909
        ReturnValue_2 = FClamp(self.T, 0, 1)
        ReturnValue_3 = Conv_IntToFloat(self.mItemAmount.amount)
        ReturnValue1_0 = Conv_IntToFloat(self.mCurrentPaidOff)
        ReturnValue_4 = ReturnValue1_0 / ReturnValue_3
        ReturnValue1_1 = FClamp(ReturnValue_4, 0, 1)
        ReturnValue_5 = Ease(self.LastValue, ReturnValue1_1, ReturnValue_2, 7, 2, 2)
        ReturnValue = ReturnValue_5
    

    def SetTextboxFormating(self):
        ReturnValue: bool = self.mCurrentPaidOff > 0
        if not ReturnValue:
            goto('L313')
        ReturnValue1: Ptr[OverlaySlot] = Default__WidgetLayoutLibrary.SlotAsOverlaySlot(self.TextboxContainer)
        ReturnValue1.SetHorizontalAlignment(0)
        self.TextboxContainer.SetRenderTranslation(Vector2D(X = 0, Y = 1))
        self.mStackSizeLbl.SetJustification(1)
        ReturnValue_0: Ptr[OverlaySlot] = Default__WidgetLayoutLibrary.SlotAsOverlaySlot(self.mStackSizeLbl)
        ReturnValue_0.SetHorizontalAlignment(0)
        # End
        # Label 313
        ReturnValue1 = Default__WidgetLayoutLibrary.SlotAsOverlaySlot(self.TextboxContainer)
        ReturnValue1.SetHorizontalAlignment(3)
        self.TextboxContainer.SetRenderTranslation(Vector2D(X = 1, Y = 1))
        self.mStackSizeLbl.SetJustification(2)
        ReturnValue_0 = Default__WidgetLayoutLibrary.SlotAsOverlaySlot(self.mStackSizeLbl)
        ReturnValue_0.SetHorizontalAlignment(3)
    

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
        ReturnValue_1: LinearColor = LinearColorLerp(LinearColor(R = 0.6038280129432678, G = 0.5972020030021667, B = 0.5972020030021667, A = 1), LinearColor(R = 1, G = 0.9943370223045349, B = 0.9166669845581055, A = 1), ReturnValue_0)
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
        ReturnValue: bool = self.mCurrentPaidOff > 0
        if not ReturnValue:
            goto('L608')
        self.SetTextboxFormating()
        FormatArgumentData.ArgumentName = "1"
        FormatArgumentData.ArgumentValueType = 0
        FormatArgumentData.ArgumentValue = 
        FormatArgumentData.ArgumentValueInt = self.mItemAmount.amount
        FormatArgumentData.ArgumentValueFloat = 0
        FormatArgumentData.ArgumentValueGender = 0
        FormatArgumentData1.ArgumentName = "0"
        # Label 286
        FormatArgumentData1.ArgumentValueType = 0
        FormatArgumentData1.ArgumentValue = 
        FormatArgumentData1.ArgumentValueInt = self.mCurrentPaidOff
        FormatArgumentData1.ArgumentValueFloat = 0
        FormatArgumentData1.ArgumentValueGender = 0
        Array: List[FormatArgumentData] = [FormatArgumentData1, FormatArgumentData]
        ReturnValue_0: FText = Default__KismetTextLibrary.Format("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 521, 'Value': '{0}/{1}'}", Array)
        ReturnValue_1: FText = ReturnValue_0
        goto('L729')
        # Label 608
        self.SetTextboxFormating()
        ReturnValue_2: FText = Default__KismetTextLibrary.Conv_IntToText(self.mItemAmount.amount, False, True, 1, 324)
        ReturnValue_1 = ReturnValue_2
    

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
        self.ExecuteUbergraph_Widget_TradingPostPayOffSlot(875)
    

    def OnSchematicPaidOff(self, schematicManager: Ptr[FGSchematicManager]):
        ExecuteUbergraph_Widget_TradingPostPayOffSlot.K2Node_CustomEvent_SchematicManager = schematicManager #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_TradingPostPayOffSlot(1197)
    

    def Destruct(self):
        self.ExecuteUbergraph_Widget_TradingPostPayOffSlot(1202)
    

    def Tick(self):
        ExecuteUbergraph_Widget_TradingPostPayOffSlot.K2Node_Event_MyGeometry1 = MyGeometry #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_TradingPostPayOffSlot.K2Node_Event_InDeltaTime = InDeltaTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_TradingPostPayOffSlot(1361)
    

    def OnMouseEnter(self):
        ExecuteUbergraph_Widget_TradingPostPayOffSlot.K2Node_Event_MyGeometry = MyGeometry #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_TradingPostPayOffSlot.K2Node_Event_MouseEvent = MouseEvent #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_TradingPostPayOffSlot(1390)
    

    def ExecuteUbergraph_Widget_TradingPostPayOffSlot(self):
        goto(ComputedJump("EntryPoint"))
        # Label 15
        self.StopEmptyAnim()
        goto(ExecutionFlow.Pop())
        # Label 30
        Variable: bool = False
        Variable_0: int32 = 0
        Variable_1: int32 = 0
        # Label 87
        ReturnValue: bool = Not_PreBool(Variable)
        ReturnValue_0: List[ItemAmount] = SchematicManager.GetPaidOffCostFor(self.mSchematic)
        
        ReturnValue_1: int32 = len(ReturnValue_0)
        ReturnValue_2: bool = Variable_0 <= ReturnValue_1
        ReturnValue_3: bool = ReturnValue and ReturnValue_2
        if not ReturnValue_3:
            goto('L706')
        Variable_1 = Variable_0
        ExecutionFlow.Push("L801")
        ReturnValue_0 = SchematicManager.GetPaidOffCostFor(self.mSchematic)
        
        Item = None
        Item = ReturnValue_0[Variable_1]
        ReturnValue_4: bool = EqualEqual_ClassClass(Item.ItemClass, self.mItemAmount.ItemClass)
        if not ReturnValue_4:
           goto(ExecutionFlow.Pop())
        ReturnValue_0 = SchematicManager.GetPaidOffCostFor(self.mSchematic)
        
        Item = None
        Item = ReturnValue_0[Variable_1]
        self.mCurrentPaidOff = Item.amount
        Variable = True
        goto(ExecutionFlow.Pop())
        # Label 706
        ReturnValue_5: bool = EqualEqual_IntInt(self.mCurrentPaidOff, 0)
        if not ReturnValue_5:
            goto('L15')
        ReturnValue1: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.EmptyAnim, 0, 0, 0, 1)
        goto(ExecutionFlow.Pop())
        # Label 801
        ReturnValue_6: int32 = Variable_0 + 1
        Variable_0 = ReturnValue_6
        goto('L87')
        ReturnValue_7: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.AniDragDropSlot, 0, 0, 0, 1)
        ReturnValue_8: Ptr[GameStateBase] = Default__GameplayStatics.GetGameState(self)
        OutputDelegate.BindUFunction(self, OnSchematicPaidOff)
        ReturnValue_9: Ptr[FGSchematicManager] = Default__FGSchematicManager.Get(ReturnValue_8)
        ReturnValue_9.PaidOffOnSchematicDelegate.AddUnique(OutputDelegate)
        ReturnValue_8 = Default__GameplayStatics.GetGameState(self)
        ReturnValue_9 = Default__FGSchematicManager.Get(ReturnValue_8)
        self.OnSchematicPaidOff(ReturnValue_9)
        goto(ExecutionFlow.Pop())
        goto('L30')
        ReturnValue1_0: Ptr[GameStateBase] = Default__GameplayStatics.GetGameState(self)
        OutputDelegate1.BindUFunction(self, OnSchematicPaidOff)
        ReturnValue1_1: Ptr[FGSchematicManager] = Default__FGSchematicManager.Get(ReturnValue1_0)
        ReturnValue1_1.PaidOffOnSchematicDelegate.Remove(OutputDelegate1)
        goto(ExecutionFlow.Pop())
        self.Tick(MyGeometry1, InDeltaTime)
        goto(ExecutionFlow.Pop())
        ReturnValue_10: Ptr[Pawn] = self.GetOwningPlayerPawn()
        ReturnValue_11: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_UI_WorkBench_MouseOver, ReturnValue_10, True)
        goto(ExecutionFlow.Pop())
    
