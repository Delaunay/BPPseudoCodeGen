
from codegen.ue4_stub import *

from Game.FactoryGame.Buildable.-Shared.Widgets.Widget_Output_Slot import ExecuteUbergraph_Widget_Output_Slot.K2Node_Event_IsDesignTime
from Script.Engine import SetTextPropertyByName
from Script.Engine import Conv_TextToString
from Script.FactoryGame import FGCharacterPlayer
from Script.Engine import SetObjectPropertyByName
from Script.UMG import SetPadding
from Script.Engine import Pawn
from Script.FactoryGame import EResourceForm
from Script.UMG import HorizontalBoxSlot
from Script.UMG import GetChildrenCount
from Script.FactoryGame import Default__FGInventoryLibrary
from Script.Engine import SetBytePropertyByName
from Script.Engine import Not_PreBool
from Script.Engine import FTrunc
from Script.Engine import Default__KismetSystemLibrary
from Script.FactoryGame import Get
from Script.FactoryGame import GetProductionSuffixFromFormType
from Script.Engine import PlayerController
from Script.UMG import GetChildAt
from Script.FactoryGame import GetAmountConvertedByForm
from Script.Engine import Default__KismetArrayLibrary
from Script.Engine import FormatArgumentData
from Game.FactoryGame.Buildable.-Shared.Widgets.Widget_Output_Slot import ExecuteUbergraph_Widget_Output_Slot
from Script.UMG import ESlateVisibility
from Script.FactoryGame import GetInventory
from Game.FactoryGame.Interface.UI.InGame.Widget_UseableBase import Construct
from Script.Engine import Conv_FloatToText
from Script.FactoryGame import GetForm
from Script.FactoryGame import FGInventoryComponent
from Script.UMG import SetPercent
from Game.FactoryGame.Interface.UI.InGame.Widget_Tooltip import Widget_Tooltip
from Script.Engine import Conv_IntToText
from Script.UMG import Default__WidgetBlueprintLibrary
from Script.Engine import Default__KismetTextLibrary
from Script.Engine import SetBoolPropertyByName
from Script.UMG import Widget
from Script.Engine import Format
from Game.FactoryGame.Interface.UI.InGame.Widget_UseableBase import Widget_UseableBase
from Script.Engine import Default__KismetStringLibrary
from Script.Engine import SetIntPropertyByName
from Script.Engine import NotEqual_ByteByte
from Script.FactoryGame import FGUnlockSubsystem
from Script.UMG import GetOwningPlayerPawn
from Script.UMG import AddChildToHorizontalBox
from Game.FactoryGame.Buildable.-Shared.Widgets.Widget_Output_Slot import ExecuteUbergraph_Widget_Output_Slot.K2Node_Event_InventorySlot
from Script.Engine import Conv_StringToFloat
from Game.FactoryGame.Buildable.-Shared.Widgets.BPW_OutputInventorySlot import BPW_OutputInventorySlot
from Script.FactoryGame import Default__FGItemDescriptor
from Script.UMG import Create
from Script.UMG import HasAnyChildren
from Script.FactoryGame import FGItemDescriptor
from Script.UMG import SetVerticalAlignment
from Script.FactoryGame import Default__FGUnlockSubsystem
from Script.Engine import IsValidClass
from Script.FactoryGame import GetIsBuildingEfficiencyUnlocked
from Script.Engine import PrintString
from Script.CoreUObject import LinearColor
from Script.Engine import MakeLiteralByte

class Widget_Output_Slot(Widget_UseableBase):
    isProductionSlot: bool
    OnDropInventorySlotStack: FMulticastScriptDelegate
    mUseCustomSlot: bool
    mUseCycleTime: bool = True
    mItemDescriptor: TSubclassOf[FGItemDescriptor]
    mShowSecondPartsPerMin: bool
    mSecondaryItemDesc: TSubclassOf[FGItemDescriptor]
    mRecipeText: FText
    mRestoreFocusWhenLost = True
    mCallCustomTickOnConstruct = True
    
    def SetShowSecondPartsPerMin(self, ShowSecondPartsPerMin: bool, SecondaryItemDesc: TSubclassOf[FGItemDescriptor]):
        self.mShowSecondPartsPerMin = ShowSecondPartsPerMin
        ReturnValue: bool = Default__KismetSystemLibrary.IsValidClass(SecondaryItemDesc)
        Variable: uint8 = 3
        Variable1: uint8 = 1
        ReturnValue_0: bool = self.mShowSecondPartsPerMin and ReturnValue
        Variable_0: bool = ReturnValue_0
        
        switch = {
            False: Variable1,
            True: Variable
        }
        self.mSecondPartsPerMin.SetVisibility(switch.get(Variable_0, None))
        self.mSecondaryItemDesc = SecondaryItemDesc
    

    def UpdateProductionStats(self, NumPerCycle: int32, cycletime: float, PowerConsumption: float, efficiency: float, SecondNumPerCycle: int32):
        ReturnValue: bool = Default__KismetSystemLibrary.IsValidClass(self.mItemDescriptor)
        if not ReturnValue:
            goto('L3746')
        ReturnValue_0: uint8 = Default__FGItemDescriptor.GetForm(self.mItemDescriptor)
        LocalForm = ReturnValue_0
        # Label 151
        ReturnValue1: float = 60 / cycletime
        ReturnValue1_0: float = Default__FGInventoryLibrary.GetAmountConvertedByForm(NumPerCycle, LocalForm)
        ReturnValue1_1: float = ReturnValue1_0 * ReturnValue1
        ReturnValue1_2: FText = Default__KismetTextLibrary.Conv_FloatToText(ReturnValue1_1, 0, False, True, 1, 324, 1, 1)
        self.mNumPerSecond.SetText(ReturnValue1_2)
        ReturnValue_1: bool = NotEqual_ByteByte(LocalForm, 1)
        ReturnValue_2: FText = Default__FGInventoryLibrary.GetProductionSuffixFromFormType(LocalForm)
        FormatArgumentData.ArgumentName = "suffix"
        FormatArgumentData.ArgumentValueType = 4
        FormatArgumentData.ArgumentValue = ReturnValue_2
        FormatArgumentData.ArgumentValueInt = 0
        FormatArgumentData.ArgumentValueFloat = 0
        FormatArgumentData.ArgumentValueGender = 0
        ReturnValue1_3: bool = Default__KismetSystemLibrary.IsValidClass(self.mSecondaryItemDesc)
        Array: List[FormatArgumentData] = [FormatArgumentData]
        ReturnValue_3: FText = Default__KismetTextLibrary.Format("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 840, 'Value': 'Fluid {suffix}'}", Array)
        ReturnValue_4: bool = self.mShowSecondPartsPerMin and ReturnValue1_3
        Variable: bool = ReturnValue_4
        Variable2: bool = ReturnValue_1
        FormatArgumentData1.ArgumentName = "suffix"
        FormatArgumentData1.ArgumentValueType = 4
        
        switch = {
            False: ReturnValue_2,
            True: ReturnValue_3
        }
        FormatArgumentData1.ArgumentValue = switch.get(Variable2, None)
        FormatArgumentData1.ArgumentValueInt = 0
        FormatArgumentData1.ArgumentValueFloat = 0
        FormatArgumentData1.ArgumentValueGender = 0
        Array1: List[FormatArgumentData] = [FormatArgumentData1]
        ReturnValue1_4: FText = Default__KismetTextLibrary.Format("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 1286, 'Value': '{suffix} per minute'}", Array1)
        ReturnValue2: FText = Default__FGInventoryLibrary.GetProductionSuffixFromFormType(LocalForm)
        FormatArgumentData4.ArgumentName = "suffix"
        FormatArgumentData4.ArgumentValueType = 4
        FormatArgumentData4.ArgumentValue = ReturnValue2
        FormatArgumentData4.ArgumentValueInt = 0
        FormatArgumentData4.ArgumentValueFloat = 0
        FormatArgumentData4.ArgumentValueGender = 0
        Array4: List[FormatArgumentData] = [FormatArgumentData4]
        ReturnValue4: FText = Default__KismetTextLibrary.Format("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 1676, 'Value': '{suffix} per minute'}", Array4)
        
        switch_0 = {
            False: ReturnValue4,
            True: ReturnValue1_4
        }
        self.mPerMinuteText.SetText(switch_0.get(Variable, None))
        self.mEfficiency.mManufacturingStat = efficiency
        ReturnValue3: FText = Default__KismetTextLibrary.Conv_FloatToText(cycletime, 0, False, True, 1, 324, 1, 1)
        
        ReturnValue1_5: FString = Default__KismetTextLibrary.Conv_TextToString(Ref[ReturnValue3])
        ReturnValue1_6: float = Default__KismetStringLibrary.Conv_StringToFloat(ReturnValue1_5)
        self.mCycleTime.mManufacturingStat = ReturnValue1_6
        ReturnValue2_0: FText = Default__KismetTextLibrary.Conv_FloatToText(PowerConsumption, 0, False, True, 1, 324, 1, 1)
        
        ReturnValue_5: FString = Default__KismetTextLibrary.Conv_TextToString(Ref[ReturnValue2_0])
        ReturnValue_6: float = Default__KismetStringLibrary.Conv_StringToFloat(ReturnValue_5)
        self.mPowerConsumption.mManufacturingStat = ReturnValue_6
        ReturnValue2_1: bool = Default__KismetSystemLibrary.IsValidClass(self.mSecondaryItemDesc)
        ReturnValue1_7: bool = self.mShowSecondPartsPerMin and ReturnValue2_1
        if not ReturnValue1_7:
            goto('L3771')
        ReturnValue2_2: uint8 = Default__FGItemDescriptor.GetForm(self.mSecondaryItemDesc)
        ReturnValue1_8: bool = NotEqual_ByteByte(ReturnValue2_2, 1)
        Variable1: bool = ReturnValue1_8
        ReturnValue1_9: FText = Default__FGInventoryLibrary.GetProductionSuffixFromFormType(ReturnValue2_2)
        FormatArgumentData2.ArgumentName = "suffix"
        FormatArgumentData2.ArgumentValueType = 4
        FormatArgumentData2.ArgumentValue = ReturnValue1_9
        FormatArgumentData2.ArgumentValueInt = 0
        FormatArgumentData2.ArgumentValueFloat = 0
        FormatArgumentData2.ArgumentValueGender = 0
        Array2: List[FormatArgumentData] = [FormatArgumentData2]
        ReturnValue2_3: FText = Default__KismetTextLibrary.Format("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 2916, 'Value': 'Fluid {suffix}'}", Array2)
        FormatArgumentData3.ArgumentName = "suffix"
        FormatArgumentData3.ArgumentValueType = 4
        
        switch_1 = {
            False: ReturnValue1_9,
            True: ReturnValue2_3
        }
        FormatArgumentData3.ArgumentValue = switch_1.get(Variable1, None)
        FormatArgumentData3.ArgumentValueInt = 0
        FormatArgumentData3.ArgumentValueFloat = 0
        FormatArgumentData3.ArgumentValueGender = 0
        Array3: List[FormatArgumentData] = [FormatArgumentData3]
        ReturnValue3_0: FText = Default__KismetTextLibrary.Format("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 3286, 'Value': '{suffix} per minute'}", Array3)
        self.mSecondPerMinText.SetText(ReturnValue3_0)
        ReturnValue1_10: uint8 = Default__FGItemDescriptor.GetForm(self.mSecondaryItemDesc)
        ReturnValue_7: float = Default__FGInventoryLibrary.GetAmountConvertedByForm(SecondNumPerCycle, ReturnValue1_10)
        ReturnValue_8: float = 60 / cycletime
        ReturnValue_9: float = ReturnValue_7 * ReturnValue_8
        ReturnValue_10: FText = Default__KismetTextLibrary.Conv_FloatToText(ReturnValue_9, 0, False, True, 1, 324, 1, 1)
        self.mSecondNumPerSec.SetText(ReturnValue_10)
        # End
        # Label 3746
        LocalForm = 1
        goto('L151')
    

    def UpdateCycleProgress(self, CycleProgress: float):
        ReturnValue: float = CycleProgress * 10
        ReturnValue_0: int32 = FTrunc(ReturnValue)
        ReturnValue_1: int32 = ReturnValue_0 * 10
        ReturnValue_2: FText = Default__KismetTextLibrary.Conv_IntToText(ReturnValue_1, False, False, 1, 324)
        FormatArgumentData.ArgumentName = "A"
        FormatArgumentData.ArgumentValueType = 4
        FormatArgumentData.ArgumentValue = ReturnValue_2
        FormatArgumentData.ArgumentValueInt = 0
        FormatArgumentData.ArgumentValueFloat = 0
        FormatArgumentData.ArgumentValueGender = 0
        Array: List[FormatArgumentData] = [FormatArgumentData]
        ReturnValue_3: FText = Default__KismetTextLibrary.Format("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 451, 'Value': '{A}%'}", Array)
        self.mPercentageText.SetText(ReturnValue_3)
        self.mProgressBar.mProgressBar.SetPercent(CycleProgress)
    

    def UpdateStaticInfo(self, RecipeName: FText):
        self.mRecipeText = RecipeName
        self.mRecipeName.SetText(self.mRecipeText)
    

    def GenerateCostSlots(self, OutputCostSlotData: Ref[List[OutputCostSlotData_Struct]]):
        ExecutionFlow.Push("L1110")
        self.mSlotContainer.ClearChildren()
        Variable: int32 = 0
        Variable_0: int32 = 0
        
        # Label 87
        ReturnValue: int32 = len(OutputCostSlotData)
        ReturnValue_0: bool = Variable <= ReturnValue
        if not ReturnValue_0:
           goto(ExecutionFlow.Pop())
        Variable_0 = Variable
        ExecutionFlow.Push("L1036")
        ReturnValue_1: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_2: Ptr[BPW_OutputInventorySlot] = Default__WidgetBlueprintLibrary.Create(self, BPW_OutputInventorySlot, ReturnValue_1)
        
        Item = None
        Item = OutputCostSlotData[Variable_0]
        
        Item.Title_3_16865392480E04744923368E818FDF9E = None
        Default__KismetSystemLibrary.SetTextPropertyByName(ReturnValue_2, "mTitle", Ref[Item.Title_3_16865392480E04744923368E818FDF9E])
        
        Item = None
        Item = OutputCostSlotData[Variable_0]
        Default__KismetSystemLibrary.SetObjectPropertyByName(ReturnValue_2, "mCachedInventoryCompontent", Item.InventoryComponent_6_670B318B4DE9249E98B040BFD46013A9)
        
        Item = None
        Item = OutputCostSlotData[Variable_0]
        Default__KismetSystemLibrary.SetIntPropertyByName(ReturnValue_2, "mSlotIdx", Item.InventorySlotIndex_10_ECF91A0C4E759F6F2FC3768CE0512AB9)
        ReturnValue_3: uint8 = Default__KismetSystemLibrary.MakeLiteralByte(1)
        Default__KismetSystemLibrary.SetBytePropertyByName(ReturnValue_2, "mSlotType", ReturnValue_3)
        
        Item = None
        Item = OutputCostSlotData[Variable_0]
        Default__KismetSystemLibrary.SetIntPropertyByName(ReturnValue_2, "mRequiredAmount", Item.RequiredAmount_14_830FF83949DA2C4550D4DFADE26300D5)
        # Label 950
        ReturnValue_4: Ptr[HorizontalBoxSlot] = self.mSlotContainer.AddChildToHorizontalBox(ReturnValue_2)
        ReturnValue_4.SetVerticalAlignment(0)
        goto(ExecutionFlow.Pop())
        # Label 1036
        ReturnValue_5: int32 = Variable + 1
        Variable = ReturnValue_5
        goto('L87')
    

    def GetSlot(self, index: int32):
        ReturnValue: int32 = self.mSlotContainer.GetChildrenCount()
        ReturnValue_0: bool = index <= ReturnValue
        if not ReturnValue_0:
            goto('L289')
        ReturnValue_1: Ptr[Widget] = self.mSlotContainer.GetChildAt(index)
        Slot: Ptr[BPW_OutputInventorySlot] = Cast[BPW_OutputInventorySlot](ReturnValue_1)
        bSuccess: bool = Slot
        if not bSuccess:
            goto('L289')
        InventorySlot = Slot.mInventorySlot
        success = True
        # End
        # Label 289
        InventorySlot = None
        success = False
    

    def GenerateOutputSlots(self, OutputSlotData: Ref[List[OutputSlotData_Struct]]):
        ExecutionFlow.Push("L950")
        self.mSlotContainer.ClearChildren()
        Variable: int32 = 0
        Variable_0: int32 = 0
        
        # Label 87
        ReturnValue: int32 = len(OutputSlotData)
        ReturnValue_0: bool = Variable <= ReturnValue
        if not ReturnValue_0:
           goto(ExecutionFlow.Pop())
        Variable_0 = Variable
        ExecutionFlow.Push("L876")
        ReturnValue_1: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_2: Ptr[BPW_OutputInventorySlot] = Default__WidgetBlueprintLibrary.Create(self, BPW_OutputInventorySlot, ReturnValue_1)
        
        Item = None
        Item = OutputSlotData[Variable_0]
        
        Item.Title_3_16865392480E04744923368E818FDF9E = None
        Default__KismetSystemLibrary.SetTextPropertyByName(ReturnValue_2, "mTitle", Ref[Item.Title_3_16865392480E04744923368E818FDF9E])
        
        Item = None
        Item = OutputSlotData[Variable_0]
        Default__KismetSystemLibrary.SetObjectPropertyByName(ReturnValue_2, "mCachedInventoryCompontent", Item.InventoryComponent_6_670B318B4DE9249E98B040BFD46013A9)
        
        Item = None
        Item = OutputSlotData[Variable_0]
        Default__KismetSystemLibrary.SetIntPropertyByName(ReturnValue_2, "mSlotIdx", Item.InventorySlotIndex_10_ECF91A0C4E759F6F2FC3768CE0512AB9)
        ReturnValue_3: Ptr[HorizontalBoxSlot] = self.mSlotContainer.AddChildToHorizontalBox(ReturnValue_2)
        ReturnValue_3.SetVerticalAlignment(0)
        OutputDelegate.BindUFunction(self, OnInventorySlotStackMove)
        ReturnValue_2.mInventorySlot.OnMoveStack.AddUnique(OutputDelegate)
        goto(ExecutionFlow.Pop())
        # Label 876
        ReturnValue_4: int32 = Variable + 1
        Variable = ReturnValue_4
        goto('L87')
    

    def UpdateWasteSlotVisibility(self):
        Variable2: uint8 = 4
        Variable3: uint8 = 1
        ReturnValue1: bool = self.InsertWasteSlotHere.HasAnyChildren()
        Variable1: bool = ReturnValue1
        
        switch = {
            False: Variable3,
            True: Variable2
        }
        self.mWasteSlotContainer.SetVisibility(switch.get(Variable1, None))
        Variable: uint8 = 4
        Variable1_0: uint8 = 2
        ReturnValue: bool = self.InsertWasteSlotHere.HasAnyChildren()
        Variable_0: bool = ReturnValue
        
        switch_0 = {
            False: Variable1_0,
            True: Variable
        }
        self.mInputLabel.SetVisibility(switch_0.get(Variable_0, None))
    

    def CreateEfficiencyToolTip(self):
        efficiencyDescriptionText = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 20, 'Value': 'How efficient the production is compared to the current max production speed.'}"
        efficiencyTitleText = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 155, 'Value': 'Efficiency'}"
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_0: Ptr[Widget_Tooltip] = Default__WidgetBlueprintLibrary.Create(self, Widget_Tooltip, ReturnValue)
        Default__KismetSystemLibrary.SetBoolPropertyByName(ReturnValue_0, "mIsManufacturingStat", True)
        
        Default__KismetSystemLibrary.SetTextPropertyByName(ReturnValue_0, "mDescriptionText", Ref[efficiencyDescriptionText])
        
        Default__KismetSystemLibrary.SetTextPropertyByName(ReturnValue_0, "mTitleText", Ref[efficiencyTitleText])
        ReturnValue_1: Ptr[Widget] = ReturnValue_0
    

    def CreatePowerConsumptionToolTip(self):
        productionDescriptionText = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 20, 'Value': 'How much power this machine consumes.'}"
        productionTitleText = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 115, 'Value': 'Power Consumption'}"
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_0: Ptr[Widget_Tooltip] = Default__WidgetBlueprintLibrary.Create(self, Widget_Tooltip, ReturnValue)
        Default__KismetSystemLibrary.SetBoolPropertyByName(ReturnValue_0, "mIsManufacturingStat", True)
        localTooltip = ReturnValue_0
        if not self.isProductionSlot:
            goto('L581')
        localTooltip.mDescriptionText = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 385, 'Value': 'How much power this machine consumes.'}"
        localTooltip.mTitleText = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 502, 'Value': 'Power Consumption'}"
        ReturnValue_1: Ptr[Widget] = localTooltip
        goto('L813')
        # Label 581
        localTooltip.mDescriptionText = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 623, 'Value': 'How much power this machine produces.'}"
        localTooltip.mTitleText = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 740, 'Value': 'Power Production'}"
        ReturnValue_1 = localTooltip
    

    def CreateCycleTimeTooltip(self):
        cycleTimeDescription = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 20, 'Value': 'How long this part takes to craft.'}"
        cycleTimeTitle = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 112, 'Value': 'Production Time'}"
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_0: Ptr[Widget_Tooltip] = Default__WidgetBlueprintLibrary.Create(self, Widget_Tooltip, ReturnValue)
        Default__KismetSystemLibrary.SetBoolPropertyByName(ReturnValue_0, "mIsManufacturingStat", True)
        localTooltip = ReturnValue_0
        if not self.isProductionSlot:
            goto('L571')
        localTooltip.mTitleText = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 380, 'Value': 'Production Time'}"
        localTooltip.mDescriptionText = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 475, 'Value': 'How long this part takes to craft.'}"
        ReturnValue_1: Ptr[Widget] = localTooltip
        goto('L820')
        # Label 571
        localTooltip.mTitleText = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 613, 'Value': 'Consumption Rate'}"
        localTooltip.mDescriptionText = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 709, 'Value': 'How long it takes to consume one fuel unit in seconds.'}"
        ReturnValue_1 = localTooltip
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_Output_Slot(10)
    

    def PreConstruct(self):
        ExecuteUbergraph_Widget_Output_Slot.K2Node_Event_IsDesignTime = IsDesignTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_Output_Slot(1040)
    

    def OnInventorySlotStackMove(self):
        ExecuteUbergraph_Widget_Output_Slot.K2Node_Event_InventorySlot = InventorySlot #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_Output_Slot(1281)
    

    def ExecuteUbergraph_Widget_Output_Slot(self):
        self.Construct()
        Variable: uint8 = 0
        Variable1: uint8 = 1
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_0: Ptr[FGUnlockSubsystem] = Default__FGUnlockSubsystem.Get(ReturnValue)
        ReturnValue_1: bool = ReturnValue_0.GetIsBuildingEfficiencyUnlocked()
        Variable_0: bool = ReturnValue_1
        
        switch = {
            False: Variable1,
            True: Variable
        }
        self.mEfficiency.SetVisibility(switch.get(Variable_0, None))
        # End
        # Label 290
        Variable2: uint8 = 0
        Variable3: uint8 = 1
        Variable1_0: bool = self.isProductionSlot
        
        switch_0 = {
            False: Variable3,
            True: Variable2
        }
        self.mPerSecondHBox.SetVisibility(switch_0.get(Variable1_0, None))
        
        switch_1 = {
            False: Variable3,
            True: Variable2
        }
        self.mProducingTextBox.SetVisibility(switch_1.get(Variable1_0, None))
        Variable2_0: bool = self.isProductionSlot
        Margin.Left = 0
        Margin.Top = 24
        Margin.Right = 0
        Margin.Bottom = 5
        Margin1.Left = 0
        Margin1.Top = 24
        Margin1.Right = 0
        Margin1.Bottom = 16
        
        switch_2 = {
            False: Margin1,
            True: Margin
        }
        self.mProgressBar.SetPadding(switch_2.get(Variable2_0, None))
        Variable4: bool = self.mUseCycleTime
        Variable6: uint8 = 0
        Variable7: uint8 = 1
        
        switch_3 = {
            False: Variable7,
            True: Variable6
        }
        self.mCycleTime.SetVisibility(switch_3.get(Variable4, None))
        # End
        Variable4_0: uint8 = 0
        Variable5: uint8 = 1
        Variable3_0: bool = self.mUseCustomSlot
        
        switch_4 = {
            False: Variable5,
            True: Variable4_0
        }
        self.mOldSlotContainer.SetVisibility(switch_4.get(Variable3_0, None))
        self.UpdateWasteSlotVisibility()
        ReturnValue_2: bool = Not_PreBool(self.isProductionSlot)
        self.mProgressBar.SetUseIconContainer(ReturnValue_2)
        goto('L290')
        ReturnValue_3: Ptr[Pawn] = self.GetOwningPlayerPawn()
        Player: Ptr[FGCharacterPlayer] = Cast[FGCharacterPlayer](ReturnValue_3)
        bSuccess: bool = Player
        ReturnValue_4: Ptr[FGInventoryComponent] = Player.GetInventory()
        
        Result = None
        self.DropInventoryStackOnInventoryComponent(InventorySlot, ReturnValue_4, Ref[Result])
        Default__KismetSystemLibrary.PrintString(self, "Move Atempted", True, True, LinearColor(R = 0, G = 0.6600000262260437, B = 1, A = 1), 2)
    

    def OnDropInventorySlotStack__DelegateSignature(self, InventorySlot: Ptr[Widget_InventorySlot]):
        pass
    
