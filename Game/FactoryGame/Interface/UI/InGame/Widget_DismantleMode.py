
from codegen.ue4_stub import *

from Script.FactoryGame import BreakInventoryStack
from Script.FactoryGame import GetNumPendingDismantleActors
from Script.FactoryGame import GetCurrentBuildGunDelayPercentage
from Script.Engine import Pawn
from Script.FactoryGame import FGBuildable
from Script.FactoryGame import Default__FGInventoryLibrary
from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import PlayerController
from Script.Engine import Default__KismetArrayLibrary
from Script.Engine import FormatArgumentData
from Script.UMG import PlayAnimation
from Script.UMG import ESlateVisibility
from Game.FactoryGame.Interface.UI.InGame.Widget_CostSlotWrapper import Widget_CostSlotWrapper
from Script.Engine import IsValid
from Script.UMG import Default__WidgetBlueprintLibrary
from Script.Engine import Default__KismetTextLibrary
from Script.FactoryGame import GetMaxNumPendingDismantleActors
from Script.UMG import AddChildToWrapBox
from Script.FactoryGame import FGInteractWidget
from Game.FactoryGame.Interface.UI.InGame.Widget_DismantleMode import ExecuteUbergraph_Widget_DismantleMode
from Script.UMG import Construct
from Script.FactoryGame import ToggleBuildGun
from Script.FactoryGame import HasReachedMaxNumPendingDismantleActors
from Game.FactoryGame.Character.Player.Char_Player import Char_Player
from Script.Engine import Format
from Script.FactoryGame import GetBuildGun
from Script.FactoryGame import Init
from Script.FactoryGame import FGBuildGunStateDismantle
from Script.UMG import WidgetAnimation
from Script.UMG import WrapBoxSlot
from Script.FactoryGame import GetSelectedActor
from Script.UMG import GetOwningPlayerPawn
from Script.Engine import Actor
from Script.UMG import UMGSequencePlayer
from Game.FactoryGame.Interface.UI.InGame.Widget_DismantleMode import ExecuteUbergraph_Widget_DismantleMode.K2Node_CustomEvent_newState
from Script.FactoryGame import FGBuildGun
from Script.UMG import Create
from Script.FactoryGame import InventoryItem
from Game.FactoryGame.Interface.UI.InGame.Widget_DismantleMode import ExecuteUbergraph_Widget_DismantleMode.K2Node_CustomEvent_dismantleGun
from Script.FactoryGame import BreakInventoryItem
from Script.FactoryGame import GetPeekDismantleRefund
from Script.FactoryGame import InventoryStack

class Widget_DismantleMode(FGInteractWidget):
    MaxNumDismantleReached: Ptr[WidgetAnimation]
    NumDismantleChanged: Ptr[WidgetAnimation]
    circle: Ptr[WidgetAnimation]
    DismantleModeStaticBorder: Ptr[WidgetAnimation]
    DismantleMode: Ptr[WidgetAnimation]
    mOwningState: Ptr[FGBuildGunStateDismantle]
    mDisplayingCostsForActor: Ptr[Actor]
    mCachedDismantleRefunds: InventoryItem
    mRestoreFocusWhenLost = True
    mInputToPassThrough = ['ToggleBuildGun', 'SecondaryFire', 'PrimaryFire', 'JetPackThrust', 'PauseGame', 'Jump', 'ToggleSprint', 'NextShortcut', 'PreviousShortcut', 'Shortcut1', 'Shortcut2', 'Shortcut3', 'Shortcut4', 'Shortcut5', 'inventory']
    mCallCustomTickOnConstruct = True
    Priority = 3
    
    def UpdateMassDismantleFeedback(self):
        ReturnValue: int32 = self.mOwningState.GetNumPendingDismantleActors(False)
        ReturnValue_0: int32 = self.mOwningState.GetMaxNumPendingDismantleActors()
        FormatArgumentData.ArgumentName = "CurrentNumDismantle"
        FormatArgumentData.ArgumentValueType = 0
        FormatArgumentData.ArgumentValue = 
        FormatArgumentData.ArgumentValueInt = ReturnValue
        FormatArgumentData.ArgumentValueFloat = 0
        FormatArgumentData.ArgumentValueGender = 0
        FormatArgumentData1.ArgumentName = "MaxNumDismantle"
        FormatArgumentData1.ArgumentValueType = 0
        FormatArgumentData1.ArgumentValue = 
        FormatArgumentData1.ArgumentValueInt = ReturnValue_0
        FormatArgumentData1.ArgumentValueFloat = 0
        FormatArgumentData1.ArgumentValueGender = 0
        Array: List[FormatArgumentData] = [FormatArgumentData, FormatArgumentData1]
        ReturnValue_1: FText = Default__KismetTextLibrary.Format("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 583, 'Value': '{CurrentNumDismantle} / {MaxNumDismantle}'}", Array)
        self.mDismantleNumberText.SetText(ReturnValue_1)
        ReturnValue_2: bool = self.mOwningState.HasReachedMaxNumPendingDismantleActors()
        if not ReturnValue_2:
            goto('L824')
        ReturnValue_3: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.MaxNumDismantleReached, 0, 0, 0, 1)
        # End
        # Label 824
        ReturnValue1: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.NumDismantleChanged, 0, 1, 0, 1)
    

    def SetDismantleFeedbackVisibility(self, Condition: bool):
        if not Condition:
            goto('L57')
        self.mMassDismantleFeedback.SetVisibility(3)
        # End
        # Label 57
        self.mMassDismantleFeedback.SetVisibility(2)
    

    def GetReticleVisibility(self):
        Variable: uint8 = 2
        Variable1: uint8 = 3
        ReturnValue: Ptr[FGBuildGun] = self.mOwningState.GetBuildGun()
        ReturnValue_0: float = ReturnValue.GetCurrentBuildGunDelayPercentage()
        ReturnValue_1: bool = ReturnValue_0 > 0
        Variable_0: bool = ReturnValue_1
        
        switch = {
            False: Variable1,
            True: Variable
        }
        ReturnValue_2: uint8 = switch.get(Variable_0, None)
    

    def SetDismantleRefunds(self):
        ExecutionFlow.Push("L1547")
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(self.mOwningState)
        if not ReturnValue:
           goto(ExecutionFlow.Pop())
        self.Widget_DismantleRefunds.mCostSlotsGrid.ClearChildren()
        Variable: int32 = 0
        Variable_0: int32 = 0
        # Label 170
        ReturnValue_0: List[InventoryStack] = self.mOwningState.GetPeekDismantleRefund()
        
        ReturnValue_1: int32 = len(ReturnValue_0)
        ReturnValue_2: bool = Variable <= ReturnValue_1
        if not ReturnValue_2:
            goto('L1068')
        Variable_0 = Variable
        ExecutionFlow.Push("L1473")
        ReturnValue_0 = self.mOwningState.GetPeekDismantleRefund()
        
        Item = None
        Item = ReturnValue_0[Variable_0]
        
        Item = None
        numItems = None
        item = None
        Default__FGInventoryLibrary.BreakInventoryStack(Ref[Item], Ref[numItems], Ref[item])
        self.mCachedDismantleRefunds = item
        ReturnValue_3: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_4: Ptr[Widget_CostSlotWrapper] = Default__WidgetBlueprintLibrary.Create(self, Widget_CostSlotWrapper, ReturnValue_3)
        ReturnValue_5: Ptr[WrapBoxSlot] = self.Widget_DismantleRefunds.mCostSlotsGrid.AddChildToWrapBox(ReturnValue_4)
        ReturnValue_0 = self.mOwningState.GetPeekDismantleRefund()
        
        itemClass = None
        itemState = None
        Default__FGInventoryLibrary.BreakInventoryItem(Ref[self.mCachedDismantleRefunds], Ref[itemClass], Ref[itemState])
        
        Item = None
        Item = ReturnValue_0[Variable_0]
        
        Item = None
        numItems = None
        item = None
        Default__FGInventoryLibrary.BreakInventoryStack(Ref[Item], Ref[numItems], Ref[item])
        ItemAmount.ItemClass = itemClass
        ItemAmount.amount = numItems
        ReturnValue_4.Setup CostIcon(None, ItemAmount, None, 0, 0, False, False, True)
        goto(ExecutionFlow.Pop())
        # Label 1068
        ReturnValue1: Ptr[Actor] = self.mOwningState.GetSelectedActor()
        self.mDisplayingCostsForActor = ReturnValue1
        ReturnValue_6: Ptr[Actor] = self.mOwningState.GetSelectedActor()
        AsFGBuildable: Ptr[FGBuildable] = Cast[FGBuildable](ReturnValue_6)
        bSuccess: bool = AsFGBuildable
        if not bSuccess:
            goto('L1376')
        self.Widget_DismantleRefunds.mBuildingName.SetText(AsFGBuildable.mDisplayName)
        self.Widget_DismantleRefunds.PlayDismantleAnimation()
        goto(ExecutionFlow.Pop())
        # Label 1376
        self.Widget_DismantleRefunds.mBuildingName.SetText()
        self.Widget_DismantleRefunds.StopDismantleAnimation()
        goto(ExecutionFlow.Pop())
        # Label 1473
        ReturnValue_7: int32 = Variable + 1
        Variable = ReturnValue_7
        goto('L170')
    

    def OnEscapePressed(self):
        self.ExecuteUbergraph_Widget_DismantleMode(951)
    

    def Init(self):
        self.ExecuteUbergraph_Widget_DismantleMode(29)
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_DismantleMode(334)
    

    def OnDismantleRefundChanged(self, dismantleGun: Ptr[FGBuildGunStateDismantle]):
        ExecuteUbergraph_Widget_DismantleMode.K2Node_CustomEvent_dismantleGun = dismantleGun #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_DismantleMode(487)
    

    def Event OnMultiDismantleStateChanged(self, newState: bool):
        ExecuteUbergraph_Widget_DismantleMode.K2Node_CustomEvent_newState = newState #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_DismantleMode(642)
    

    def Event OnPendingDismantleActorsChanged(self):
        self.ExecuteUbergraph_Widget_DismantleMode(670)
    

    def Destruct(self):
        self.ExecuteUbergraph_Widget_DismantleMode(689)
    

    def ExecuteUbergraph_Widget_DismantleMode(self):
        # Label 10
        self.SetDismantleRefunds()
        # End
        self.Init()
        Dismantle: Ptr[FGBuildGunStateDismantle] = Cast[FGBuildGunStateDismantle](self.mInteractObject)
        bSuccess: bool = Dismantle
        if not bSuccess:
            goto('L137')
        self.mOwningState = Dismantle
        # Label 137
        OutputDelegate.BindUFunction(self, OnDismantleRefundChanged)
        self.mOwningState.OnPeekRefundsChanged.AddUnique(OutputDelegate)
        OutputDelegate1.BindUFunction(self, Event OnMultiDismantleStateChanged)
        self.mOwningState.OnMultiDismantleStateChanged.AddUnique(OutputDelegate1)
        OutputDelegate2.BindUFunction(self, Event OnPendingDismantleActorsChanged)
        self.mOwningState.OnPendingDismantleActorsChanged.AddUnique(OutputDelegate2)
        goto('L10')
        self.Construct()
        ReturnValue: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.DismantleMode, 0, 0, 0, 1)
        ReturnValue1: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.DismantleModeStaticBorder, 0, 0, 0, 1)
        ReturnValue2: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.circle, 0, 0, 0, 1)
        # End
        self.SetDismantleRefunds()
        # End
        # Label 506
        ReturnValue_0: Ptr[Pawn] = self.GetOwningPlayerPawn()
        Player: Ptr[Char_Player] = Cast[Char_Player](ReturnValue_0)
        bSuccess1: bool = Player
        if not bSuccess1:
            goto('L956')
        Player.ToggleBuildGun()
        # End
        self.SetDismantleFeedbackVisibility(newState)
        # End
        self.UpdateMassDismantleFeedback()
        # End
        ReturnValue_1: bool = Default__KismetSystemLibrary.IsValid(self.mOwningState)
        if not ReturnValue_1:
            goto('L956')
        OutputDelegate3.BindUFunction(self, OnDismantleRefundChanged)
        self.mOwningState.OnPeekRefundsChanged.Remove(OutputDelegate3)
        OutputDelegate4.BindUFunction(self, Event OnMultiDismantleStateChanged)
        self.mOwningState.OnMultiDismantleStateChanged.Remove(OutputDelegate4)
        OutputDelegate5.BindUFunction(self, Event OnPendingDismantleActorsChanged)
        self.mOwningState.OnPendingDismantleActorsChanged.Remove(OutputDelegate5)
        # End
        goto('L506')
    
