
from codegen.ue4_stub import *

from Game.FactoryGame.Interface.UI.InGame.Hotbar.Widget_HotbarEntry import Widget_HotbarEntry
from Script.Engine import SetScalarParameterValue
from Script.Engine import Delay
from Script.FactoryGame import FGPlayerController
from Script.Engine import SetObjectPropertyByName
from Script.Engine import MaterialInstanceDynamic
from Script.Engine import Conv_IntToFloat
from Script.UMG import PanelSlot
from Game.FactoryGame.Interface.UI.InGame.Hotbar.Widget_HotbarContainer import ExecuteUbergraph_Widget_HotbarContainer.K2Node_CustomEvent_purchasedSchematic
from Script.UMG import AddChild
from Script.Engine import LatentActionInfo
from Script.Engine import FTrunc
from Script.Engine import Default__KismetSystemLibrary
from Script.FactoryGame import Get
from Script.Engine import PlayerController
from Script.Engine import Default__KismetArrayLibrary
from Script.UMG import SetRenderTranslation
from Script.UMG import PlayAnimation
from Script.Engine import IsValid
from Script.Engine import Conv_IntToText
from Script.UMG import Default__WidgetBlueprintLibrary
from Script.UMG import Destruct
from Script.FactoryGame import GetCurrentShortcuts
from Script.Engine import Default__KismetTextLibrary
from Script.FactoryGame import GetNumHotbars
from Script.Engine import Divide_IntInt
from Script.Engine import BreakVector2D
from Script.UMG import Construct
from Script.FactoryGame import FGHotbarShortcut
from Script.Engine import SetIntPropertyByName
from Script.UMG import WidgetAnimation
from Game.FactoryGame.Interface.UI.InGame.Hotbar.Widget_HotbarContainer import ExecuteUbergraph_Widget_HotbarContainer.K2Node_CustomEvent_NewIndex
from Script.UMG import UserWidget
from Script.FactoryGame import FGSchematicManager
from Script.UMG import UMGSequencePlayer
from Script.UMG import Create
from Game.FactoryGame.Interface.UI.InGame.Hotbar.Widget_HotbarContainer import ExecuteUbergraph_Widget_HotbarContainer.K2Node_CustomEvent_Index
from Script.CoreUObject import Vector2D
from Game.FactoryGame.Interface.UI.InGame.Hotbar.Widget_HotbarContainer import ExecuteUbergraph_Widget_HotbarContainer
from Script.Engine import Array_Clear
from Script.FactoryGame import Default__FGSchematicManager
from Script.UMG import GetDynamicMaterial
from Script.FactoryGame import GetCurrentHotbarIndex

class Widget_HotbarContainer(UserWidget):
    SwitchHotbarAnim: Ptr[WidgetAnimation]
    mEntryWidgets: List[Ptr[Widget_HotbarEntry]]
    mSlotWidth: int32
    mNumOfSlots: int32
    StopNotificationOnConstruct: bool = True
    mCurrentBarIndex: int32
    mShowNotification: bool
    
    def UpdateBarIndexIndicator(self):
        ReturnValue: int32 = self.mCurrentBarIndex + 1
        ReturnValue_0: FText = Default__KismetTextLibrary.Conv_IntToText(ReturnValue, False, True, 1, 324)
        self.mBarIndicatorText.SetText(ReturnValue_0)
        ReturnValue_1: Ptr[MaterialInstanceDynamic] = self.mBarIndicator.GetDynamicMaterial()
        ReturnValue_2: Ptr[PlayerController] = self.GetOwningPlayer()
        Controller: Ptr[FGPlayerController] = Cast[FGPlayerController](ReturnValue_2)
        bSuccess: bool = Controller
        ReturnValue_3: float = Conv_IntToFloat(self.mCurrentBarIndex)
        ReturnValue_4: int32 = Controller.GetNumHotbars()
        ReturnValue1: float = Conv_IntToFloat(ReturnValue_4)
        ReturnValue_5: float = ReturnValue_3 / ReturnValue1
        ReturnValue_6: float = ReturnValue_5 + 0.009999999776482582
        ReturnValue_1.SetScalarParameterValue("StartingPos", ReturnValue_6)
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_HotbarContainer(2918)
    

    def Destruct(self):
        self.ExecuteUbergraph_Widget_HotbarContainer(3123)
    

    def OnHotbarUpdated(self):
        self.ExecuteUbergraph_Widget_HotbarContainer(3439)
    

    def OnHotbarLayoutUpdated(self):
        self.ExecuteUbergraph_Widget_HotbarContainer(3444)
    

    def ShowNotification(self, index: int32):
        ExecuteUbergraph_Widget_HotbarContainer.K2Node_CustomEvent_Index = index #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_HotbarContainer(3763)
    

    def ListenForPurchasedSchematics(self):
        self.ExecuteUbergraph_Widget_HotbarContainer(4371)
    

    def OnPurchasedSchematic(self, purchasedSchematic: TSubclassOf[FGSchematic]):
        ExecuteUbergraph_Widget_HotbarContainer.K2Node_CustomEvent_purchasedSchematic = purchasedSchematic #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_HotbarContainer(4376)
    

    def StopListenForPurchasedSchematics(self):
        self.ExecuteUbergraph_Widget_HotbarContainer(4391)
    

    def OnHotbarIndexChanged(self, newIndex: int32):
        ExecuteUbergraph_Widget_HotbarContainer.K2Node_CustomEvent_NewIndex = newIndex #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_HotbarContainer(4667)
    

    def ExecuteUbergraph_Widget_HotbarContainer(self):
        goto(ComputedJump("EntryPoint"))
        # Label 15
        self.UpdateBarIndexIndicator()
        ReturnValue2: Ptr[PlayerController] = self.GetOwningPlayer()
        Controller1: Ptr[FGPlayerController] = Cast[FGPlayerController](ReturnValue2)
        bSuccess1: bool = Controller1
        if not bSuccess1:
           goto(ExecutionFlow.Pop())
        OutputDelegate.BindUFunction(self, OnHotbarUpdated)
        Controller1.OnShortcutChanged.AddUnique(OutputDelegate)
        OutputDelegate1.BindUFunction(self, OnHotbarLayoutUpdated)
        Controller1.OnShortcutsLayoutChanged.AddUnique(OutputDelegate1)
        OutputDelegate3.BindUFunction(self, OnHotbarIndexChanged)
        Controller1.OnHotbarIndexChanged.AddUnique(OutputDelegate3)
        self.ListenForPurchasedSchematics()
        Default__KismetSystemLibrary.Delay(self, 0.10000000149011612, LatentActionInfo(Linkage = 411, UUID = 1744909523, ExecutionFunction = "ExecuteUbergraph_Widget_HotbarContainer", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        self.StopNotificationOnConstruct = False
        ReturnValue: Ptr[MaterialInstanceDynamic] = self.mBarIndicator.GetDynamicMaterial()
        ReturnValue6: Ptr[PlayerController] = self.GetOwningPlayer()
        Controller3: Ptr[FGPlayerController] = Cast[FGPlayerController](ReturnValue6)
        bSuccess3: bool = Controller3
        ReturnValue_0: int32 = Controller3.GetNumHotbars()
        ReturnValue1: float = Conv_IntToFloat(ReturnValue_0)
        ReturnValue_1: float = 1 / ReturnValue1
        ReturnValue_2: float = ReturnValue_1 - 0.019999999552965164
        ReturnValue.SetScalarParameterValue("Value", ReturnValue_2)
        ReturnValue1_0: Ptr[MaterialInstanceDynamic] = self.mBarBackground.GetDynamicMaterial()
        ReturnValue7: Ptr[PlayerController] = self.GetOwningPlayer()
        Controller4: Ptr[FGPlayerController] = Cast[FGPlayerController](ReturnValue7)
        bSuccess4: bool = Controller4
        ReturnValue1_1: int32 = Controller4.GetNumHotbars()
        ReturnValue2_0: float = Conv_IntToFloat(ReturnValue1_1)
        ReturnValue1_0.SetScalarParameterValue("Segments", ReturnValue2_0)
        goto(ExecutionFlow.Pop())
        # Label 1051
        ReturnValue4: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_3: Ptr[FGSchematicManager] = Default__FGSchematicManager.Get(ReturnValue4)
        ReturnValue_4: bool = Default__KismetSystemLibrary.IsValid(ReturnValue_3)
        if not ReturnValue_4:
            goto('L1331')
        OutputDelegate2.BindUFunction(self, OnPurchasedSchematic)
        ReturnValue4 = self.GetOwningPlayer()
        ReturnValue_3 = Default__FGSchematicManager.Get(ReturnValue4)
        ReturnValue_3.PurchasedSchematicDelegate.AddUnique(OutputDelegate2)
        goto(ExecutionFlow.Pop())
        # Label 1331
        Default__KismetSystemLibrary.Delay(self, 0.20000000298023224, LatentActionInfo(Linkage = 1051, UUID = 830053156, ExecutionFunction = "ExecuteUbergraph_Widget_HotbarContainer", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        # Label 1408
        ReturnValue_5: int32 = Variable + 1
        Variable: int32 = ReturnValue_5
        
        # Label 1477
        ReturnValue2_1: int32 = len(self.mEntryWidgets)
        ReturnValue1_2: bool = Variable <= ReturnValue2_1
        if not ReturnValue1_2:
            goto('L1725')
        Variable_0: int32 = Variable
        ExecutionFlow.Push("L1408")
        
        Item = None
        Item = self.mEntryWidgets[Variable_0]
        Item.OnHotbarUpdated(self.mShowNotification)
        goto(ExecutionFlow.Pop())
        # Label 1725
        self.mShowNotification = True
        goto(ExecutionFlow.Pop())
        # Label 1737
        ReturnValue1_3: int32 = Variable1 + 1
        Variable1: int32 = ReturnValue1_3
        
        shortcuts = None
        # Label 1806
        ReturnValue_6: int32 = len(shortcuts)
        ReturnValue_7: bool = Variable1 <= ReturnValue_6
        if not ReturnValue_7:
            goto('L2394')
        Variable1_0: int32 = Variable1
        ExecutionFlow.Push("L1737")
        ReturnValue1_4: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_8: Ptr[Widget_HotbarEntry] = Default__WidgetBlueprintLibrary.Create(self, Widget_HotbarEntry, ReturnValue1_4)
        
        shortcuts = None
        Item2 = None
        Item2 = shortcuts[Variable1_0]
        Default__KismetSystemLibrary.SetObjectPropertyByName(ReturnValue_8, "mShortcut", Item2)
        Default__KismetSystemLibrary.SetIntPropertyByName(ReturnValue_8, "mShortcutIndex", Variable1_0)
        Default__KismetSystemLibrary.SetObjectPropertyByName(ReturnValue_8, "mHotbarContainer", self)
        ReturnValue_9: Ptr[PanelSlot] = self.mBox.AddChild(ReturnValue_8)
        
        ReturnValue_10: int32 = self.mEntryWidgets.append(ReturnValue_8)
        goto(ExecutionFlow.Pop())
        # Label 2394
        ReturnValue_11: bool = self.mNumOfSlots > 0
        if not ReturnValue_11:
           goto(ExecutionFlow.Pop())
        self.OnHotbarUpdated()
        
        Item1 = None
        Item1 = self.mEntryWidgets[0]
        
        X1 = None
        Y1 = None
        BreakVector2D(Item1.mHotbarSlot.Brush.ImageSize, Ref[X1], Ref[Y1])
        ReturnValue_12: float = X1 + Item1.padding.Left
        ReturnValue1_5: float = ReturnValue_12 + Item1.padding.Right
        ReturnValue_13: int32 = FTrunc(ReturnValue1_5)
        self.mSlotWidth = ReturnValue_13
        goto(ExecutionFlow.Pop())
        # Label 2816
        Variable1 = 0
        Variable1_0 = 0
        goto('L1806')
        # Label 2867
        Variable = 0
        Variable_0 = 0
        goto('L1477')
        self.Construct()
        ReturnValue8: Ptr[PlayerController] = self.GetOwningPlayer()
        Controller5: Ptr[FGPlayerController] = Cast[FGPlayerController](ReturnValue8)
        bSuccess5: bool = Controller5
        if not bSuccess5:
           goto(ExecutionFlow.Pop())
        ReturnValue_14: int32 = Controller5.GetCurrentHotbarIndex()
        self.mCurrentBarIndex = ReturnValue_14
        self.OnHotbarLayoutUpdated()
        goto('L15')
        self.Destruct()
        ReturnValue3: Ptr[PlayerController] = self.GetOwningPlayer()
        Controller2: Ptr[FGPlayerController] = Cast[FGPlayerController](ReturnValue3)
        bSuccess2: bool = Controller2
        if not bSuccess2:
           goto(ExecutionFlow.Pop())
        OutputDelegate.BindUFunction(self, OnHotbarUpdated)
        Controller2.OnShortcutChanged.Remove(OutputDelegate)
        OutputDelegate1.BindUFunction(self, OnHotbarLayoutUpdated)
        Controller2.OnShortcutsLayoutChanged.Remove(OutputDelegate1)
        OutputDelegate3.BindUFunction(self, OnHotbarIndexChanged)
        Controller2.OnHotbarIndexChanged.Remove(OutputDelegate3)
        self.StopListenForPurchasedSchematics()
        goto(ExecutionFlow.Pop())
        goto('L2867')
        # Label 3444
        self.mBox.ClearChildren()
        
        Default__KismetArrayLibrary.Array_Clear(Ref[self.mEntryWidgets])
        ReturnValue_15: Ptr[PlayerController] = self.GetOwningPlayer()
        Controller: Ptr[FGPlayerController] = Cast[FGPlayerController](ReturnValue_15)
        bSuccess: bool = Controller
        if not bSuccess:
           goto(ExecutionFlow.Pop())
        shortcuts: List[Ptr[FGHotbarShortcut]] = []
        
        Controller.GetCurrentShortcuts(Ref[shortcuts])
        
        ReturnValue1_6: int32 = len(shortcuts)
        self.mNumOfSlots = ReturnValue1_6
        goto('L2816')
        if not self.StopNotificationOnConstruct:
            goto('L3778')
        goto(ExecutionFlow.Pop())
        
        X = None
        Y = None
        # Label 3778
        BreakVector2D(self.Widget_HotbarNotification.RenderTransform.Translation, Ref[X], Ref[Y])
        ReturnValue_16: int32 = Divide_IntInt(self.mSlotWidth, 2)
        ReturnValue_17: int32 = self.mSlotWidth * Index
        ReturnValue2_2: int32 = ReturnValue_16 + ReturnValue_17
        ReturnValue1_7: int32 = Divide_IntInt(self.mNumOfSlots, 2)
        ReturnValue1_8: int32 = self.mSlotWidth * ReturnValue1_7
        ReturnValue_18: int32 = ReturnValue1_8 - ReturnValue2_2
        ReturnValue2_3: int32 = ReturnValue_18 * -1
        ReturnValue_19: float = Conv_IntToFloat(ReturnValue2_3)
        ReturnValue_20: Vector2D = Vector2D(ReturnValue_19, Y)
        self.Widget_HotbarNotification.SetRenderTranslation(ReturnValue_20)
        ReturnValue_21: Ptr[UMGSequencePlayer] = self.Widget_HotbarNotification.PlayAnimation(self.Widget_HotbarNotification.HotbarPopUp, 0, 1, 0, 1)
        goto(ExecutionFlow.Pop())
        goto('L1051')
        self.OnHotbarUpdated()
        goto(ExecutionFlow.Pop())
        ReturnValue5: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue1_9: Ptr[FGSchematicManager] = Default__FGSchematicManager.Get(ReturnValue5)
        ReturnValue1_10: bool = Default__KismetSystemLibrary.IsValid(ReturnValue1_9)
        if not ReturnValue1_10:
           goto(ExecutionFlow.Pop())
        OutputDelegate2.BindUFunction(self, OnPurchasedSchematic)
        ReturnValue5 = self.GetOwningPlayer()
        ReturnValue1_9 = Default__FGSchematicManager.Get(ReturnValue5)
        ReturnValue1_9.PurchasedSchematicDelegate.Remove(OutputDelegate2)
        goto(ExecutionFlow.Pop())
        self.mCurrentBarIndex = NewIndex
        ReturnValue1_11: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.SwitchHotbarAnim, 0, 1, 0, 1)
        self.mShowNotification = False
        goto('L3444')
    
