
from codegen.ue4_stub import *

from Script.Engine import SetTextPropertyByName
from Script.Engine import NotEqual_BoolBool
from Script.FactoryGame import FGCharacterPlayer
from Script.Engine import Pawn
from Script.FactoryGame import FGHologram
from Script.UMG import PanelSlot
from Script.UMG import AddChild
from Script.FactoryGame import FGConstructDisqualifier
from Script.FactoryGame import GetConstructDisqualifiers
from Script.Engine import Default__KismetSystemLibrary
from Game.FactoryGame.Interface.UI.InGame.BuildMenu.Widget_BuildMode import ExecuteUbergraph_Widget_BuildMode.K2Node_CustomEvent_newSplineMode
from Script.Engine import PlayerController
from Script.Engine import NotEqual_ClassClass
from Game.FactoryGame.Interface.UI.InGame.BuildMenu.Widget_BuildMode import ExecuteUbergraph_Widget_BuildMode
from Script.Engine import Default__KismetArrayLibrary
from Script.Engine import FormatArgumentData
from Script.FactoryGame import GetItemName
from Script.UMG import ESlateVisibility
from Script.UMG import PlayAnimation
from Script.FactoryGame import GetHologram
from Game.FactoryGame.Interface.UI.InGame.Widget_CostSlotWrapper import Widget_CostSlotWrapper
from Script.FactoryGame import GetSupportedSplineModes
from Script.Engine import IsValid
from Script.UMG import StopAnimation
from Script.UMG import Default__WidgetBlueprintLibrary
from Script.Engine import EqualEqual_IntInt
from Script.Engine import Default__KismetTextLibrary
from Script.FactoryGame import GetDisqualifyingText
from Script.UMG import AddChildToWrapBox
from Script.FactoryGame import CanConstruct
from Script.Engine import BooleanOR
from Script.FactoryGame import ToggleBuildGun
from Script.UMG import Construct
from Script.FactoryGame import FGInteractWidget
from Script.Engine import Format
from Script.Engine import Array_RemoveItem
from Script.UMG import WidgetAnimation
from Game.FactoryGame.Interface.UI.InGame.BuildMenu.Widget_Build_IngredientInfo import Widget_Build_IngredientInfo
from Script.UMG import WrapBoxSlot
from Script.FactoryGame import Default__FGConstructDisqualifier
from Script.FactoryGame import FGBuildGunStateBuild
from Script.FactoryGame import GetHologramCost
from Script.Engine import NotEqual_ObjectObject
from Game.FactoryGame.Interface.UI.InGame.-Shared.Struct_KeybindingHint import Struct_KeybindingHint
from Script.UMG import GetOwningPlayerPawn
from Game.FactoryGame.Interface.UI.HUDHelpers.HUDHelpers import Default__HUDHelpers
from Script.UMG import UMGSequencePlayer
from Script.UMG import Create
from Script.FactoryGame import Default__FGItemDescriptor
from Script.Engine import Array_IsValidIndex
from Script.FactoryGame import FGItemDescriptor
from Script.FactoryGame import GetDescriptor
from Script.Engine import Array_Insert
from Script.FactoryGame import EHologramSplinePathMode
from Script.FactoryGame import GetSplineMode
from Script.FactoryGame import ItemAmount
from Game.FactoryGame.Interface.UI.InGame.BuildMenu.Widget_BuildMode import ExecuteUbergraph_Widget_BuildMode.K2Node_Event_UpdateTime
from Script.Engine import Array_Clear
from Script.Engine import PrintString
from Script.CoreUObject import LinearColor

class Widget_BuildMode(FGInteractWidget):
    FadeInSplineAnim: Ptr[WidgetAnimation]
    DisqualifierAnim: Ptr[WidgetAnimation]
    DismantleAnim: Ptr[WidgetAnimation]
    mOwningState: Ptr[FGBuildGunStateBuild]
    mSetupCostHologram: Ptr[FGHologram]
    mPrevHologramCostLength: int32
    mCostSlots: List[Ptr[Widget_CostSlotWrapper]]
    isDismantleMode: bool
    mPrevHologramCost: List[ItemAmount]
    mCurrentHologramCost: List[ItemAmount]
    mRebuildHologramCosts: bool
    mSupportedSplineModes: List[uint8]
    mShouldShowBuildModesHint: bool
    mRestoreFocusWhenLost = True
    mCustomTickRate = 0.10000000149011612
    mCallCustomTickOnConstruct = True
    Visibility = ESlateVisibility::HitTestInvisible
    
    def GetHasMultipleSplineModes(self):
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(self.mOwningState)
        if not ReturnValue:
            goto('L232')
        ReturnValue_0: List[uint8] = self.mOwningState.GetSupportedSplineModes()
        
        # Label 115
        ReturnValue_1: int32 = len(ReturnValue_0)
        ReturnValue_2: bool = ReturnValue_1 > 0
        ReturnValue_3: bool = ReturnValue_2
        goto('L243')
        # Label 232
        ReturnValue_3 = False
    

    def UpdateHintVisibility(self):
        LocalBuildModeHint = Struct_KeybindingHint(Action_3_8CED3F9B4A70C1822B95758560DE8695 = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 33, 'Value': 'Toggle Build Mode'}", KeyBinding_5_6C26EF9041BC54531A02F2B5B7DC3464 = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 90, 'Value': '{Reload}'}")
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(self.mOwningState)
        if not ReturnValue:
            goto('L600')
        ReturnValue_0: bool = self.GetHasMultipleSplineModes()
        ReturnValue_1: bool = NotEqual_BoolBool(self.mShouldShowBuildModesHint, ReturnValue_0)
        if not ReturnValue_1:
            goto('L804')
        ReturnValue_0 = self.GetHasMultipleSplineModes()
        self.mShouldShowBuildModesHint = ReturnValue_0
        if not self.mShouldShowBuildModesHint:
            goto('L600')
        self.CurrentBuildModeOverlay.SetVisibility(4)
        
        self.mBHints.mKeyBindingHints = None
        Default__KismetArrayLibrary.Array_Insert(4, Ref[self.mBHints.mKeyBindingHints], Ref[LocalBuildModeHint])
        Default__KismetSystemLibrary.PrintString(self, "on", True, True, LinearColor(R = 0, G = 0.6600000262260437, B = 1, A = 1), 2)
        
        self.mBHints.mKeyBindingHints = None
        # Label 528
        self.mBHints.SetKeybindingHints(Ref[self.mBHints.mKeyBindingHints])
        # End
        # Label 600
        self.CurrentBuildModeOverlay.SetVisibility(1)
        
        self.mBHints.mKeyBindingHints = None
        ReturnValue_2: bool = Default__KismetArrayLibrary.Array_RemoveItem(Ref[self.mBHints.mKeyBindingHints], Ref[LocalBuildModeHint])
        Default__KismetSystemLibrary.PrintString(self, "off", True, True, LinearColor(R = 0, G = 0.6600000262260437, B = 1, A = 1), 2)
        goto('L528')
    

    def CheckHologramState(self):
        ExecutionFlow.Push("L1846")
        ReturnValue: Ptr[FGHologram] = self.mOwningState.GetHologram()
        ReturnValue_0: bool = Default__KismetSystemLibrary.IsValid(ReturnValue)
        ReturnValue1: bool = Default__KismetSystemLibrary.IsValid(self.mOwningState)
        ReturnValue_1: bool = ReturnValue1 and ReturnValue_0
        if not ReturnValue_1:
            goto('L1080')
        ReturnValue_2: List[ItemAmount] = self.mOwningState.GetHologramCost()
        self.mCurrentHologramCost = ReturnValue_2
        
        ReturnValue2: int32 = len(self.mCurrentHologramCost)
        
        ReturnValue3: int32 = len(self.mPrevHologramCost)
        ReturnValue1_0: bool = ReturnValue2 != ReturnValue3
        ReturnValue1_1: Ptr[FGHologram] = self.mOwningState.GetHologram()
        ReturnValue_3: bool = NotEqual_ObjectObject(self.mSetupCostHologram, ReturnValue1_1)
        ReturnValue2_0: bool = Default__KismetSystemLibrary.IsValid(ReturnValue1_1)
        ReturnValue1_2: bool = ReturnValue_3 and ReturnValue2_0
        ReturnValue1_3: bool = BooleanOR(ReturnValue1_2, ReturnValue1_0)
        self.mRebuildHologramCosts = ReturnValue1_3
        
        ReturnValue2 = len(self.mCurrentHologramCost)
        
        ReturnValue3 = len(self.mPrevHologramCost)
        # Label 778
        ReturnValue1_0 = ReturnValue2 != ReturnValue3
        ReturnValue1_1 = self.mOwningState.GetHologram()
        ReturnValue_3 = NotEqual_ObjectObject(self.mSetupCostHologram, ReturnValue1_1)
        ReturnValue2_0 = Default__KismetSystemLibrary.IsValid(ReturnValue1_1)
        ReturnValue1_2 = ReturnValue_3 and ReturnValue2_0
        ReturnValue1_3 = BooleanOR(ReturnValue1_2, ReturnValue1_0)
        mShouldUpdate = ReturnValue1_3
        if not mShouldUpdate:
            goto('L1282')
        # Label 1056
        ReturnValue_4: bool = mShouldUpdate
        goto('L1846')
        
        # Label 1080
        ReturnValue_5: int32 = len(self.mCurrentHologramCost)
        ReturnValue_6: bool = ReturnValue_5 > 0
        if not ReturnValue_6:
            goto('L1255')
        
        Default__KismetArrayLibrary.Array_Clear(Ref[self.mCurrentHologramCost])
        self.mRebuildHologramCosts = True
        mShouldUpdate = True
        goto('L1056')
        # Label 1255
        self.mRebuildHologramCosts = False
        mShouldUpdate = False
        goto('L1056')
        # Label 1282
        Variable: int32 = 0
        
        # Label 1305
        ReturnValue1_4: int32 = len(self.mCurrentHologramCost)
        ReturnValue_7: int32 = ReturnValue1_4 - 1
        ReturnValue_8: bool = Variable <= ReturnValue_7
        if not ReturnValue_8:
            goto('L1056')
        ExecutionFlow.Push("L1772")
        
        ReturnValue_9: bool = Default__KismetArrayLibrary.Array_IsValidIndex(Variable, Ref[self.mPrevHologramCost])
        if not ReturnValue_9:
            goto('L1749')
        ReturnValue_10: bool = self.mCurrentHologramCost[Variable].amount != self.mPrevHologramCost[Variable].amount
        ReturnValue_11: bool = NotEqual_ClassClass(self.mCurrentHologramCost[Variable].ItemClass, self.mPrevHologramCost[Variable].ItemClass)
        ReturnValue_12: bool = BooleanOR(ReturnValue_11, ReturnValue_10)
        if not ReturnValue_12:
           goto(ExecutionFlow.Pop())
        mShouldUpdate = True
        goto(ExecutionFlow.Pop())
        # Label 1749
        mShouldUpdate = True
        self.mRebuildHologramCosts = True
        goto(ExecutionFlow.Pop())
        # Label 1772
        ReturnValue_13: int32 = Variable + 1
        Variable = ReturnValue_13
        goto('L1305')
    

    def GetBuildDisqualifiersVisibility(self):
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(self.mSetupCostHologram)
        if not ReturnValue:
            goto('L242')
        Variable: uint8 = 2
        Variable1: uint8 = 0
        ReturnValue_0: bool = self.mSetupCostHologram.CanConstruct()
        Variable_0: bool = ReturnValue_0
        
        switch = {
            False: Variable1,
            True: Variable
        }
        ReturnValue_1: uint8 = switch.get(Variable_0, None)
        goto('L262')
        # Label 242
        ReturnValue_1 = 2
    

    def GetBuildDisqualifiersText(self):
        ExecutionFlow.Push("L1534")
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(self.mSetupCostHologram)
        if not ReturnValue:
            goto('L1403')
        constructResults: List[TSubclassOf[FGConstructDisqualifier]] = []
        
        self.mSetupCostHologram.GetConstructDisqualifiers(Ref[constructResults])
        constructDisqualifiers = constructResults
        Variable: int32 = 0
        Variable_0: int32 = 0
        
        # Label 195
        ReturnValue_0: int32 = len(constructDisqualifiers)
        ReturnValue_1: bool = Variable <= ReturnValue_0
        if not ReturnValue_1:
            goto('L1428')
        Variable_0 = Variable
        ExecutionFlow.Push("L1460")
        
        Item = None
        Item = constructDisqualifiers[Variable_0]
        ReturnValue_2: FText = Default__FGConstructDisqualifier.GetDisqualifyingText(Item)
        FormatArgumentData.ArgumentName = "0"
        FormatArgumentData.ArgumentValueType = 4
        FormatArgumentData.ArgumentValue = ReturnValue_2
        FormatArgumentData.ArgumentValueInt = 0
        FormatArgumentData.ArgumentValueFloat = 0
        FormatArgumentData.ArgumentValueGender = 0
        Array: List[FormatArgumentData] = [FormatArgumentData]
        ReturnValue_3: FText = Default__KismetTextLibrary.Format("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 715, 'Value': '{0}'}", Array)
        FormatArgumentData1.ArgumentName = "1"
        FormatArgumentData1.ArgumentValueType = 4
        FormatArgumentData1.ArgumentValue = ReturnValue_3
        FormatArgumentData1.ArgumentValueInt = 0
        FormatArgumentData1.ArgumentValueFloat = 0
        FormatArgumentData1.ArgumentValueGender = 0
        ReturnValue_4: bool = Variable_0 > 0
        FormatArgumentData2.ArgumentName = "0"
        FormatArgumentData2.ArgumentValueType = 4
        FormatArgumentData2.ArgumentValue = finalText
        FormatArgumentData2.ArgumentValueInt = 0
        FormatArgumentData2.ArgumentValueFloat = 0
        FormatArgumentData2.ArgumentValueGender = 0
        Variable_1: bool = ReturnValue_4
        Array1: List[FormatArgumentData] = [FormatArgumentData2, FormatArgumentData1]
        ReturnValue1: FText = Default__KismetTextLibrary.Format("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 1275, 'Value': '{0}\r\n{1}'}", Array1)
        
        switch = {
            False: ReturnValue_3,
            True: ReturnValue1
        }
        finalText = switch.get(Variable_1, None)
        goto(ExecutionFlow.Pop())
        # Label 1403
        ReturnValue_5: FText = 
        goto('L1534')
        # Label 1428
        ReturnValue_5 = finalText
        goto('L1534')
        # Label 1460
        ReturnValue_6: int32 = Variable + 1
        Variable = ReturnValue_6
        goto('L195')
    

    def UpdateCost(self):
        ExecutionFlow.Push("L1759")
        if not self.mRebuildHologramCosts:
            goto('L69')
        self.VerticalBox_1.ClearChildren()
        self.CreateCostSlots()
        # Label 69
        Variable: int32 = 0
        Variable_0: int32 = 0
        
        # Label 115
        ReturnValue: int32 = len(self.mCurrentHologramCost)
        ReturnValue_0: bool = Variable <= ReturnValue
        if not ReturnValue_0:
           goto(ExecutionFlow.Pop())
        Variable_0 = Variable
        ExecutionFlow.Push("L1685")
        
        ReturnValue1: int32 = len(self.mCostSlots)
        ReturnValue1_0: bool = Variable_0 <= ReturnValue1
        if not ReturnValue1_0:
           goto(ExecutionFlow.Pop())
        
        Item = None
        Item = self.mCurrentHologramCost[Variable_0]
        localCost = Item
        ReturnValue_1: bool = localCost.amount > 0
        if not ReturnValue_1:
           goto(ExecutionFlow.Pop())
        ReturnValue_2: Ptr[Pawn] = self.GetOwningPlayerPawn()
        
        numItems = None
        Default__HUDHelpers.GetNumItemsFromPlayerInventory(ReturnValue_2, localCost.ItemClass, self, Ref[numItems])
        
        Item1 = None
        Item1 = self.mCostSlots[Variable_0]
        Item1.Setup CostIcon(None, localCost, None, 0, numItems, False, False, False)
        ReturnValue_2 = self.GetOwningPlayerPawn()
        
        numItems = None
        Default__HUDHelpers.GetNumItemsFromPlayerInventory(ReturnValue_2, localCost.ItemClass, self, Ref[numItems])
        ReturnValue_3: bool = EqualEqual_IntInt(numItems, 0)
        ReturnValue_4: bool = self.mRebuildHologramCosts and ReturnValue_3
        if not ReturnValue_4:
           goto(ExecutionFlow.Pop())
        ReturnValue_5: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_6: Ptr[Widget_Build_IngredientInfo] = Default__WidgetBlueprintLibrary.Create(self, Widget_Build_IngredientInfo, ReturnValue_5)
        FormatArgumentData.ArgumentName = "B"
        FormatArgumentData.ArgumentValueType = 0
        FormatArgumentData.ArgumentValue = 
        FormatArgumentData.ArgumentValueInt = localCost.amount
        FormatArgumentData.ArgumentValueFloat = 0
        FormatArgumentData.ArgumentValueGender = 0
        ReturnValue_7: FText = Default__FGItemDescriptor.GetItemName(localCost.ItemClass)
        FormatArgumentData1.ArgumentName = "A"
        FormatArgumentData1.ArgumentValueType = 4
        FormatArgumentData1.ArgumentValue = ReturnValue_7
        FormatArgumentData1.ArgumentValueInt = 0
        FormatArgumentData1.ArgumentValueFloat = 0
        FormatArgumentData1.ArgumentValueGender = 0
        Array: List[FormatArgumentData] = [FormatArgumentData1, FormatArgumentData]
        ReturnValue_8: FText = Default__KismetTextLibrary.Format("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 1506, 'Value': 'Missing {A} x{B}'}", Array)
        
        Default__KismetSystemLibrary.SetTextPropertyByName(ReturnValue_6, "mTitle", Ref[ReturnValue_8])
        ReturnValue_9: Ptr[PanelSlot] = self.VerticalBox_1.AddChild(ReturnValue_6)
        goto(ExecutionFlow.Pop())
        # Label 1685
        ReturnValue_10: int32 = Variable + 1
        Variable = ReturnValue_10
        goto('L115')
    

    def CreateCostSlots(self):
        ExecutionFlow.Push("L852")
        self.mCostSlotsGrid.ClearChildren()
        
        Default__KismetArrayLibrary.Array_Clear(Ref[self.mCostSlots])
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(self.mOwningState)
        if not ReturnValue:
           goto(ExecutionFlow.Pop())
        Variable: int32 = 0
        Variable_0: int32 = 0
        
        # Label 189
        ReturnValue_0: int32 = len(self.mCurrentHologramCost)
        ReturnValue_1: bool = Variable <= ReturnValue_0
        if not ReturnValue_1:
            goto('L570')
        Variable_0 = Variable
        ExecutionFlow.Push("L778")
        ReturnValue_2: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_3: Ptr[Widget_CostSlotWrapper] = Default__WidgetBlueprintLibrary.Create(self, Widget_CostSlotWrapper, ReturnValue_2)
        ReturnValue_3.mForceEmptyAnim = True
        
        ReturnValue_4: int32 = self.mCostSlots.append(ReturnValue_3)
        ReturnValue_5: Ptr[WrapBoxSlot] = self.mCostSlotsGrid.AddChildToWrapBox(ReturnValue_3)
        goto(ExecutionFlow.Pop())
        # Label 570
        ReturnValue_6: Ptr[FGHologram] = self.mOwningState.GetHologram()
        self.mSetupCostHologram = ReturnValue_6
        ReturnValue_7: TSubclassOf[FGItemDescriptor] = self.mOwningState.GetDescriptor()
        ReturnValue_8: FText = Default__FGItemDescriptor.GetItemName(ReturnValue_7)
        self.mBuildingName.SetText(ReturnValue_8)
        goto(ExecutionFlow.Pop())
        # Label 778
        ReturnValue_9: int32 = Variable + 1
        Variable = ReturnValue_9
        goto('L189')
    

    def GetTextColor(self):
        
        TextWhite = None
        GraphicsWhite = None
        Default__HUDHelpers.GetFactoryGameWhite(self, Ref[TextWhite], Ref[GraphicsWhite])
        ReturnValue = TextWhite
    

    def OnEscapePressed(self):
        self.ExecuteUbergraph_Widget_BuildMode(10)
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_BuildMode(146)
    

    def PlayDismantleAnimation(self):
        self.ExecuteUbergraph_Widget_BuildMode(1714)
    

    def StopDismantleAnimation(self):
        self.ExecuteUbergraph_Widget_BuildMode(1803)
    

    def OnCustomTick(self):
        ExecuteUbergraph_Widget_BuildMode.K2Node_Event_UpdateTime = UpdateTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_BuildMode(2316)
    

    def PlayOnSplineModeChangedAnimation(self, newSplineMode: uint8):
        ExecuteUbergraph_Widget_BuildMode.K2Node_CustomEvent_newSplineMode = newSplineMode #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_BuildMode(2321)
    

    def ExecuteUbergraph_Widget_BuildMode(self):
        ReturnValue: Ptr[Pawn] = self.GetOwningPlayerPawn()
        Player: Ptr[FGCharacterPlayer] = Cast[FGCharacterPlayer](ReturnValue)
        bSuccess: bool = Player
        if not bSuccess:
            goto('L3138')
        Player.ToggleBuildGun()
        # End
        self.Construct()
        Build: Ptr[FGBuildGunStateBuild] = Cast[FGBuildGunStateBuild](self.mInteractObject)
        bSuccess1: bool = Build
        self.mOwningState = Build
        self.CreateCostSlots()
        self.UpdateHintVisibility()
        Variable2: uint8 = 3
        Variable4: uint8 = 1
        Variable: bool = self.isDismantleMode
        
        switch = {
            False: Variable2,
            True: Variable4
        }
        self.mBHints.SetVisibility(switch.get(Variable, None))
        Variable3: uint8 = 1
        Variable5: uint8 = 3
        Variable1: bool = self.isDismantleMode
        
        switch_0 = {
            False: Variable3,
            True: Variable5
        }
        self.mDHints.SetVisibility(switch_0.get(Variable1, None))
        ReturnValue1: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.DisqualifierAnim, 0, 0, 0, 0.15000000596046448)
        ReturnValue4: bool = Default__KismetSystemLibrary.IsValid(self.mOwningState)
        if not ReturnValue4:
            goto('L3138')
        OutputDelegate.BindUFunction(self, PlayOnSplineModeChangedAnimation)
        self.mOwningState.OnSplineModeChangedDelegate.AddUnique(OutputDelegate)
        ReturnValue1_0: Ptr[FGHologram] = self.mOwningState.GetHologram()
        ReturnValue3: bool = Default__KismetSystemLibrary.IsValid(ReturnValue1_0)
        if not ReturnValue3:
            goto('L3138')
        ReturnValue1_0 = self.mOwningState.GetHologram()
        ReturnValue_0: uint8 = ReturnValue1_0.GetSplineMode()
        Variable8: FText = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 958, 'Value': 'Noodle'}"
        Variable9: FText = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 1022, 'Value': 'Conveyor 2D'}"
        Variable10: FText = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 1091, 'Value': 'Path Find'}"
        Variable11: FText = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 1158, 'Value': 'Vertical To Horizontal'}"
        Variable12: FText = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 1238, 'Value': 'Vertical'}"
        Variable13: FText = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 1304, 'Value': 'Straight Vertical'}"
        Variable14: FText = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 1379, 'Value': 'Straight Horizontal'}"
        Variable15: FText = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 1456, 'Value': 'Default'}"
        Variable1_0: uint8 = ReturnValue_0
        
        switch_1 = {
            0: Variable15,
            1: Variable14,
            2: Variable13,
            3: Variable12,
            4: Variable11,
            5: Variable10,
            6: Variable9,
            7: Variable8
        }
        self.mCurrentModeText.SetText(switch_1.get(Variable1_0, None))
        # End
        self.mDismantleText.SetVisibility(3)
        ReturnValue_1: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.DismantleAnim, 0, 0, 0, 1)
        # End
        self.mDismantleText.SetVisibility(1)
        self.StopAnimation(self.DismantleAnim)
        # End
        # Label 1865
        self.UpdateCost()
        # Label 1879
        ReturnValue_2: bool = Default__KismetSystemLibrary.IsValid(self.mOwningState)
        ReturnValue_3: Ptr[FGHologram] = self.mOwningState.GetHologram()
        ReturnValue1_1: bool = Default__KismetSystemLibrary.IsValid(ReturnValue_3)
        ReturnValue_4: bool = ReturnValue_2 and ReturnValue1_1
        if not ReturnValue_4:
            goto('L2157')
        ReturnValue_5: List[ItemAmount] = self.mOwningState.GetHologramCost()
        self.mPrevHologramCost = ReturnValue_5
        # End
        # Label 2157
        self.mPrevHologramCost = self.mCurrentHologramCost
        # End
        # Label 2189
        ReturnValue_6: bool = self.CheckHologramState()
        if not ReturnValue_6:
            goto('L1879')
        goto('L1865')
        # Label 2232
        ReturnValue2: bool = Default__KismetSystemLibrary.IsValid(self.mOwningState)
        if not ReturnValue2:
            goto('L3138')
        self.UpdateHintVisibility()
        goto('L2189')
        goto('L2232')
        ReturnValue2_0: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.FadeInSplineAnim, 0, 1, 0, 1)
        Variable_0: FText = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 2387, 'Value': 'Noodle'}"
        Variable1_1: FText = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 2451, 'Value': 'Conveyor 2D'}"
        Variable2_0: FText = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 2520, 'Value': 'Path Find'}"
        Variable3_0: FText = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 2587, 'Value': 'Vertical To Horizontal'}"
        Variable4_0: FText = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 2667, 'Value': 'Vertical'}"
        Variable5_0: FText = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 2733, 'Value': 'Straight Vertical'}"
        Variable6: FText = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 2808, 'Value': 'Straight Horizontal'}"
        Variable7: FText = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 2885, 'Value': 'Default'}"
        Variable_1: uint8 = newSplineMode
        
        switch_2 = {
            0: Variable7,
            1: Variable6,
            2: Variable5_0,
            3: Variable4_0,
            4: Variable3_0,
            5: Variable2_0,
            6: Variable1_1,
            7: Variable_0
        }
        self.mCurrentModeText.SetText(switch_2.get(Variable_1, None))
    
