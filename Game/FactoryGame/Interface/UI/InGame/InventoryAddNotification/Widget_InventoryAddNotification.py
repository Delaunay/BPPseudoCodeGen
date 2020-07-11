
from codegen.ue4_stub import *

from Script.Engine import Texture2D
from Script.Engine import EqualEqual_ClassClass
from Script.FactoryGame import FindWidgetByClass
from Script.Engine import SetClassPropertyByName
from Script.Engine import Delay
from Script.FactoryGame import FGCharacterPlayer
from Game.FactoryGame.-Shared.Crate.Widget_Crate import Widget_Crate
from Game.FactoryGame.Interface.UI.InGame.InventoryAddNotification.InventoryAddTimes import InventoryAddTimes
from Script.Engine import SetObjectPropertyByName
from Script.Engine import Pawn
from Script.Engine import GreaterEqual_IntInt
from Script.UMG import PanelSlot
from Script.SlateCore import Margin
from Script.Engine import Array_Set
from Script.UMG import AddChild
from Script.Engine import Max
from Script.Engine import Not_PreBool
from Script.Engine import LatentActionInfo
from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import PlayerController
from Script.Engine import Default__KismetArrayLibrary
from Script.FactoryGame import GetInventory
from Script.FactoryGame import GetBigIcon
from Script.Engine import GetObjectClass
from Script.FactoryGame import FGInventoryComponent
from Script.Engine import IsValid
from Script.UMG import Default__WidgetBlueprintLibrary
from Script.Engine import GetTimeSeconds
from Script.FactoryGame import FGInteractWidget
from Script.Engine import Default__GameplayStatics
from Script.Engine import BooleanOR
from Script.UMG import Tick
from Game.FactoryGame.Character.Player.Widget_InventoryAddNotificationIcon import Widget_InventoryAddNotificationIcon
from Script.Engine import SetIntPropertyByName
from Game.FactoryGame.Interface.UI.InGame.InventoryAddNotification.Widget_InventoryAddNotification import ExecuteUbergraph_Widget_InventoryAddNotification.K2Node_Event_InDeltaTime
from Game.FactoryGame.Interface.UI.InGame.InventoryAddNotification.Widget_ItemNotification import Widget_ItemNotification
from Script.UMG import UserWidget
from Script.Engine import NotEqual_ObjectObject
from Script.UMG import GetOwningPlayerPawn
from Game.FactoryGame.Interface.UI.HUDHelpers.HUDHelpers import Default__HUDHelpers
from Script.FactoryGame import Default__FGItemDescriptor
from Script.UMG import Create
from Game.FactoryGame.Interface.UI.InGame.InventoryAddNotification.Widget_InventoryAddNotification import ExecuteUbergraph_Widget_InventoryAddNotification.K2Node_Event_MyGeometry
from Game.FactoryGame.Interface.UI.InGame.InventoryAddNotification.Widget_InventoryAddNotification import ExecuteUbergraph_Widget_InventoryAddNotification
from Script.UMG import RemoveChild

class Widget_InventoryAddNotification(UserWidget):
    mItemsAddTimes: List[InventoryAddTimes]
    mTimeWindow: float = 5
    mCachedOwningChar: Ptr[FGCharacterPlayer]
    mDelegateIsBound: bool
    Current_ItemNotfication: Ptr[Widget_ItemNotification]
    CurrentItemIcon: Ptr[Widget_InventoryAddNotificationIcon]
    Visibility = ESlateVisibility::Hidden
    
    def BindOnInventoryAddAndCacheChar(self):
        ReturnValue: Ptr[Pawn] = self.GetOwningPlayerPawn()
        Player: Ptr[FGCharacterPlayer] = Cast[FGCharacterPlayer](ReturnValue)
        bSuccess: bool = Player
        if not bSuccess:
            goto('L358')
        self.mCachedOwningChar = Player
        ReturnValue_0: Ptr[FGInventoryComponent] = self.mCachedOwningChar.GetInventory()
        ReturnValue_1: bool = Default__KismetSystemLibrary.IsValid(ReturnValue_0)
        if not ReturnValue_1:
            goto('L347')
        ReturnValue_0 = self.mCachedOwningChar.GetInventory()
        OutputDelegate.BindUFunction(self, OnItemAdded)
        ReturnValue_0.OnItemAddedDelegate.AddUnique(OutputDelegate)
        self.mDelegateIsBound = True
        # End
        # Label 347
        self.mDelegateIsBound = False
    

    def UnbindOnInventoryAdd(self, FromCharacter: Ptr[FGCharacterPlayer]):
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(FromCharacter)
        if not ReturnValue:
            goto('L182')
        ReturnValue_0: Ptr[FGInventoryComponent] = FromCharacter.GetInventory()
        OutputDelegate.BindUFunction(self, OnItemAdded)
        ReturnValue_0.OnItemAddedDelegate.Remove(OutputDelegate)
        self.mDelegateIsBound = False
    

    def IsInteractWidgetOpen(self):
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        
        gameUI = None
        Default__HUDHelpers.GetFGGameUI(ReturnValue, self, Ref[gameUI])
        ReturnValue_0: Ptr[FGInteractWidget] = gameUI.FindWidgetByClass(FGInteractWidget)
        ReturnValue_1: bool = Default__KismetSystemLibrary.IsValid(ReturnValue_0)
        ReturnValue_2: TSubclassOf[FGInteractWidget] = Default__GameplayStatics.GetObjectClass(ReturnValue_0)
        Crate: TSubclassOf[Widget_Crate] = ClassCast[Widget_Crate](ReturnValue_2)
        bSuccess: bool = Crate
        ReturnValue_3: bool = Not_PreBool(bSuccess)
        ReturnValue_4: bool = ReturnValue_1 and ReturnValue_3
        IsOpen = ReturnValue_4
    

    def OnItemAdded(self, ItemClass: TSubclassOf[FGItemDescriptor], numAdded: int32):
        ExecutionFlow.Push("L2186")
        
        IsOpen = None
        self.IsInteractWidgetOpen(Ref[IsOpen])
        if not IsOpen:
            goto('L73')
        self.SetVisibility(1)
        goto(ExecutionFlow.Pop())
        # Label 73
        self.SetVisibility(3)
        Variable: int32 = 0
        Variable_0: int32 = 0
        
        # Label 149
        ReturnValue: int32 = len(self.mItemsAddTimes)
        ReturnValue_0: bool = Variable <= ReturnValue
        if not ReturnValue_0:
            goto('L1454')
        Variable_0 = Variable
        ExecutionFlow.Push("L2112")
        
        Item1 = None
        Item1 = self.mItemsAddTimes[Variable_0]
        ReturnValue_1: bool = EqualEqual_ClassClass(ItemClass, Item1.ItemClass_2_7DB810DB420443F0B7D053A862489422)
        if not ReturnValue_1:
           goto(ExecutionFlow.Pop())
        ReturnValue1: float = Default__GameplayStatics.GetTimeSeconds(self)
        
        Item = None
        Item = self.mItemsAddTimes[Variable_0]
        InventoryAddTimes1.ItemClass_2_7DB810DB420443F0B7D053A862489422 = Item.ItemClass_2_7DB810DB420443F0B7D053A862489422
        InventoryAddTimes1.TimeStamp_5_CC0FCA014A6FADACF5A9FCB6FAACC871 = ReturnValue1
        InventoryAddTimes1.Widget_8_5F8B5CA8468B3EE4884636828A86531D = Item.Widget_8_5F8B5CA8468B3EE4884636828A86531D
        InventoryAddTimes1.IsAnimatingOut_10_DBA94AC14B27887644CA6081B090B4F3 = False
        
        InventoryAddTimes1 = None
        Default__KismetArrayLibrary.Array_Set(Variable_0, False, Ref[self.mItemsAddTimes], Ref[InventoryAddTimes1])
        
        Item = None
        Item = self.mItemsAddTimes[Variable_0]
        Item.Widget_8_5F8B5CA8468B3EE4884636828A86531D.AddToNumItems(numAdded)
        self.Widget_InventoryAddNotificationIcon.Animate Icon()
        # Label 857
        ReturnValue_2: Ptr[Texture2D] = Default__FGItemDescriptor.GetBigIcon(ItemClass)
        SlateBrush.ImageSize = self.Widget_InventoryAddNotificationIcon.ResourceIcon.Brush.ImageSize
        SlateBrush.Margin = Margin(Left = 0, Top = 0, Right = 0, Bottom = 0)
        SlateBrush.TintColor = self.Widget_InventoryAddNotificationIcon.ResourceIcon.Brush.TintColor
        SlateBrush.ResourceObject = ReturnValue_2
        SlateBrush.DrawAs = self.Widget_InventoryAddNotificationIcon.ResourceIcon.Brush.DrawAs
        SlateBrush.Tiling = self.Widget_InventoryAddNotificationIcon.ResourceIcon.Brush.Tiling
        SlateBrush.Mirroring = 0
        
        SlateBrush = None
        self.Widget_InventoryAddNotificationIcon.ResourceIcon.SetBrush(Ref[SlateBrush])
        # End
        # Label 1454
        ReturnValue_3: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_4: Ptr[Widget_ItemNotification] = Default__WidgetBlueprintLibrary.Create(self, Widget_ItemNotification, ReturnValue_3)
        Default__KismetSystemLibrary.SetClassPropertyByName(ReturnValue_4, "mItemClass", ItemClass)
        Default__KismetSystemLibrary.SetIntPropertyByName(ReturnValue_4, "mNumItems", numAdded)
        ReturnValue_5: Ptr[FGInventoryComponent] = self.mCachedOwningChar.GetInventory()
        Default__KismetSystemLibrary.SetObjectPropertyByName(ReturnValue_4, "mInventory", ReturnValue_5)
        ReturnValue_6: Ptr[PanelSlot] = self.mVerticalBox.AddChild(ReturnValue_4)
        self.Current_ItemNotfication = ReturnValue_4
        ReturnValue_7: float = Default__GameplayStatics.GetTimeSeconds(self)
        InventoryAddTimes.ItemClass_2_7DB810DB420443F0B7D053A862489422 = ItemClass
        InventoryAddTimes.TimeStamp_5_CC0FCA014A6FADACF5A9FCB6FAACC871 = ReturnValue_7
        InventoryAddTimes.Widget_8_5F8B5CA8468B3EE4884636828A86531D = ReturnValue_4
        InventoryAddTimes.IsAnimatingOut_10_DBA94AC14B27887644CA6081B090B4F3 = False
        
        InventoryAddTimes = None
        ReturnValue_8: int32 = self.mItemsAddTimes.append(InventoryAddTimes)
        self.Widget_InventoryAddNotificationIcon.Animate Icon()
        goto('L857')
        # Label 2112
        ReturnValue_9: int32 = Variable + 1
        Variable = ReturnValue_9
        goto('L149')
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_InventoryAddNotification(145)
    

    def Destruct(self):
        self.ExecuteUbergraph_Widget_InventoryAddNotification(150)
    

    def Tick(self):
        ExecuteUbergraph_Widget_InventoryAddNotification.K2Node_Event_MyGeometry = MyGeometry #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_InventoryAddNotification.K2Node_Event_InDeltaTime = InDeltaTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_InventoryAddNotification(174)
    

    def ExecuteUbergraph_Widget_InventoryAddNotification(self):
        goto(ComputedJump("EntryPoint"))
        # Label 15
        self.BindOnInventoryAddAndCacheChar()
        ReturnValue1: bool = Not_PreBool(self.mDelegateIsBound)
        if not ReturnValue1:
           goto(ExecutionFlow.Pop())
        Default__KismetSystemLibrary.Delay(self, 0.5, LatentActionInfo(Linkage = 15, UUID = -2037842536, ExecutionFunction = "ExecuteUbergraph_Widget_InventoryAddNotification", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        goto('L15')
        self.UnbindOnInventoryAdd(self.mCachedOwningChar)
        goto(ExecutionFlow.Pop())
        self.Tick(MyGeometry, InDeltaTime)
        ReturnValue: bool = Not_PreBool(self.mDelegateIsBound)
        ReturnValue_0: Ptr[Pawn] = self.GetOwningPlayerPawn()
        ReturnValue_1: bool = NotEqual_ObjectObject(self.mCachedOwningChar, ReturnValue_0)
        ReturnValue_2: bool = BooleanOR(ReturnValue_1, ReturnValue)
        if not ReturnValue_2:
            goto('L378')
        self.UnbindOnInventoryAdd(self.mCachedOwningChar)
        self.BindOnInventoryAddAndCacheChar()
        
        # Label 378
        ReturnValue_3: int32 = len(self.mItemsAddTimes)
        ReturnValue_4: int32 = ReturnValue_3 - 1
        Variable: int32 = ReturnValue_4
        
        ReturnValue_3 = len(self.mItemsAddTimes)
        ReturnValue_4 = ReturnValue_3 - 1
        ReturnValue_5: int32 = Max(0, ReturnValue_4)
        Variable_0: int32 = ReturnValue_5
        # Label 676
        ReturnValue_6: bool = GreaterEqual_IntInt(Variable, 0)
        if not ReturnValue_6:
           goto(ExecutionFlow.Pop())
        Variable_0 = Variable
        ExecutionFlow.Push("L1135")
        ReturnValue_7: float = Default__GameplayStatics.GetTimeSeconds(self)
        
        Item = None
        Item = self.mItemsAddTimes[Variable_0]
        ReturnValue_8: float = ReturnValue_7 - Item.TimeStamp_5_CC0FCA014A6FADACF5A9FCB6FAACC871
        ReturnValue_9: bool = ReturnValue_8 > self.mTimeWindow
        if not ReturnValue_9:
           goto(ExecutionFlow.Pop())
        
        Item = None
        Item = self.mItemsAddTimes[Variable_0]
        ReturnValue_10: bool = self.mVerticalBox.RemoveChild(Item.Widget_8_5F8B5CA8468B3EE4884636828A86531D)
        
        self.mItemsAddTimes.remove(Variable_0)
        goto(ExecutionFlow.Pop())
        # Label 1135
        ReturnValue1_0: int32 = Variable - 1
        Variable = ReturnValue1_0
        goto('L676')
    
