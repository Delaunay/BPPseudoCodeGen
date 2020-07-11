
from codegen.ue4_stub import *

from Script.FactoryGame import FGBuildableResourceExtractor
from Script.Engine import Texture2D
from Script.FactoryGame import FGResourceDescriptor
from Script.FactoryGame import GetExtractableResource
from Script.Engine import FClamp
from Script.Engine import Conv_IntToFloat
from Script.Engine import Not_PreBool
from Script.Engine import Default__KismetSystemLibrary
from Script.FactoryGame import GetFlowRateSmoothed
from Script.Engine import Default__KismetArrayLibrary
from Script.FactoryGame import GetItemName
from Script.UMG import ESlateVisibility
from Script.FactoryGame import GetNumExtractedItemsPerCycle
from Game.FactoryGame.Interface.UI.InGame.Widget_UseableBase import Construct
from Script.Engine import Conv_FloatToText
from Script.Engine import IsValid
from Script.FactoryGame import FGInventoryComponent
from Game.FactoryGame.Buildable.Factory.WaterPump.UI.BPW_ExtractorPump import ExecuteUbergraph_BPW_ExtractorPump.K2Node_Event_InDeltaTime
from Script.FactoryGame import GetCurrentPotential
from Script.FactoryGame import IsProductionPaused
from Script.Engine import Default__KismetTextLibrary
from Script.FactoryGame import GetSmallIcon
from Script.FactoryGame import FGExtractableResourceInterface
from Script.Engine import BooleanOR
from Script.FactoryGame import GetNumItems
from Game.FactoryGame.Buildable.Factory.WaterPump.UI.BPW_ExtractorPump import ExecuteUbergraph_BPW_ExtractorPump
from Game.FactoryGame.Interface.UI.InGame.Widget_UseableBase import Widget_UseableBase
from Game.FactoryGame.Buildable.Factory.WaterPump.UI.BPW_ExtractorPump import ExecuteUbergraph_BPW_ExtractorPump.K2Node_ComponentBoundEvent_state
from Script.FactoryGame import GetScaledFluidStackSize
from Script.FactoryGame import GetFluidColorLinear
from Script.FactoryGame import GetProducingPowerConsumption
from Script.FactoryGame import GetProductivity
from Game.FactoryGame.Interface.UI.InGame.Widget_UseableBase import Destruct
from Script.FactoryGame import Default__FGItemDescriptor
from Script.FactoryGame import GetMaxFlowRate
from Script.FactoryGame import GetOutputInventory
from Script.Engine import IsValidClass
from Game.FactoryGame.Buildable.Factory.WaterPump.UI.BPW_ExtractorPump import ExecuteUbergraph_BPW_ExtractorPump.K2Node_Event_MyGeometry
from Script.CoreUObject import LinearColor

class BPW_ExtractorPump(Widget_UseableBase):
    mBuildableExtractor: Ptr[FGBuildableResourceExtractor]
    mExtractableResource: TSubclassOf[FGResourceDescriptor]
    mShouldOpenInventory = True
    mUseKeyboard = True
    mUseMouse = True
    mCaptureInput = True
    mRestoreFocusWhenLost = True
    mDesiredHorizontalAlignment = 2
    mDesiredVerticalAlignment = 2
    mUseGamepadCursor = True
    mCallCustomTickOnConstruct = True
    bHasScriptImplementedTick = True
    
    def DropInventorySlotStack(self):
        ExecutionFlow.Push("L770")
        
        Slots = None
        self.Widget_Overclock.GetUnlockedOverclockSlots(Ref[Slots])
        Variable: bool = False
        Variable_0: int32 = 0
        Variable_1: int32 = 0
        # Label 107
        ReturnValue: bool = Not_PreBool(Variable)
        
        Slots = None
        ReturnValue_0: int32 = len(Slots)
        ReturnValue_1: bool = Variable_0 <= ReturnValue_0
        ReturnValue_2: bool = ReturnValue and ReturnValue_1
        if not ReturnValue_2:
            goto('L672')
        Variable_1 = Variable_0
        ExecutionFlow.Push("L696")
        Variable1: bool = True
        Variable2: bool = True
        
        Slots = None
        Item = None
        Item = Slots[Variable_1]
        
        slotHasItems = None
        Item.CheckSlotHasItems(Ref[slotHasItems])
        ReturnValue1: bool = Not_PreBool(slotHasItems)
        
        switch = {
            False: Variable1,
            True: ReturnValue1
        }
        if not switch.get(Variable2, None):
           goto(ExecutionFlow.Pop())
        
        Slots = None
        Item = None
        Item = Slots[Variable_1]
        
        Result = None
        Item.DropOntoInventorySlot(InventorySlot, Ref[Result])
        if not Result:
           goto(ExecutionFlow.Pop())
        Variable_2: bool = True
        Variable = True
        goto(ExecutionFlow.Pop())
        # Label 672
        WasStackMoved = Variable_2
        # End
        # Label 696
        ReturnValue_3: int32 = Variable_0 + 1
        Variable_0 = ReturnValue_3
        goto('L107')
    

    def UpdateWarning(self):
        Variable: FText = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 20, 'Value': 'PRODUCTION PAUSED'}"
        Variable1: FText = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 95, 'Value': 'NO POWER'}"
        ReturnValue: bool = self.mBuildableExtractor.IsProductionPaused()
        Variable_0: bool = ReturnValue
        
        switch = {
            False: Variable1,
            True: Variable
        }
        self.mWarningWidget.SetText(switch.get(Variable_0, None))
        Variable_1: uint8 = 3
        Variable1_0: uint8 = 1
        ReturnValue_0: bool = self.mBuildableExtractor.HasPower()
        ReturnValue_1: bool = Not_PreBool(ReturnValue_0)
        ReturnValue1: bool = self.mBuildableExtractor.IsProductionPaused()
        ReturnValue_2: bool = BooleanOR(ReturnValue1, ReturnValue_1)
        Variable1_1: bool = ReturnValue_2
        
        switch_0 = {
            False: Variable1_0,
            True: Variable_1
        }
        self.mWarningWidget.SetVisibility(switch_0.get(Variable1_1, None))
    

    def SetupStaticInfo(self):
        ReturnValue: bool = Default__KismetSystemLibrary.IsValidClass(self.mExtractableResource)
        if not ReturnValue:
            goto('L1969')
        ReturnValue_0: FText = Default__FGItemDescriptor.GetItemName(self.mExtractableResource)
        self.mFluidName.SetText(ReturnValue_0)
        ReturnValue_1: Ptr[Texture2D] = Default__FGItemDescriptor.GetSmallIcon(self.mExtractableResource)
        SlateBrush1.ImageSize = self.mFluidIcon.Brush.ImageSize
        SlateBrush1.Margin = self.mFluidIcon.Brush.Margin
        SlateBrush1.TintColor = self.mFluidIcon.Brush.TintColor
        SlateBrush1.ResourceObject = ReturnValue_1
        SlateBrush1.DrawAs = self.mFluidIcon.Brush.DrawAs
        SlateBrush1.Tiling = self.mFluidIcon.Brush.Tiling
        SlateBrush1.Mirroring = self.mFluidIcon.Brush.Mirroring
        
        SlateBrush1 = None
        self.mFluidIcon.SetBrush(Ref[SlateBrush1])
        ReturnValue_1 = Default__FGItemDescriptor.GetSmallIcon(self.mExtractableResource)
        SlateBrush.ImageSize = self.mFluidIconProduction.Brush.ImageSize
        SlateBrush.Margin = self.mFluidIconProduction.Brush.Margin
        SlateBrush.TintColor = self.mFluidIconProduction.Brush.TintColor
        SlateBrush.ResourceObject = ReturnValue_1
        # Label 975
        SlateBrush.DrawAs = self.mFluidIconProduction.Brush.DrawAs
        SlateBrush.Tiling = self.mFluidIconProduction.Brush.Tiling
        SlateBrush.Mirroring = self.mFluidIconProduction.Brush.Mirroring
        
        SlateBrush = None
        self.mFluidIconProduction.SetBrush(Ref[SlateBrush])
        ReturnValue_2: LinearColor = Default__FGItemDescriptor.GetFluidColorLinear(self.mExtractableResource)
        self.mFluidTank.SetTint(ReturnValue_2)
        ReturnValue_3: float = self.mBuildableExtractor.GetMaxFlowRate()
        ReturnValue_4: float = ReturnValue_3 * 60
        ReturnValue1: FText = Default__KismetTextLibrary.Conv_FloatToText(ReturnValue_4, 0, False, True, 1, 324, 0, 0)
        self.mMaxFlowRateText.SetText(ReturnValue1)
        ReturnValue_5: int32 = self.mBuildableExtractor.GetScaledFluidStackSize()
        ReturnValue_6: float = Conv_IntToFloat(ReturnValue_5)
        ReturnValue_7: float = ReturnValue_6 / 1000
        ReturnValue_8: FText = Default__KismetTextLibrary.Conv_FloatToText(ReturnValue_7, 0, False, True, 1, 324, 0, 1)
        self.mMaxAmountInPipe.SetText(ReturnValue_8)
        ReturnValue1_0: FText = Default__FGItemDescriptor.GetItemName(self.mExtractableResource)
        self.mOutputSlot.mRecipeName.SetText(ReturnValue1_0)
        self.mOutputSlot.mItemDescriptor = self.mExtractableResource
    

    def UpdateFluidTank(self):
        FluidAmount = 0
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(self.mBuildableExtractor)
        if not ReturnValue:
            goto('L638')
        ReturnValue_0: Ptr[FGInventoryComponent] = self.mBuildableExtractor.GetOutputInventory()
        ReturnValue_1: int32 = ReturnValue_0.GetNumItems(self.mExtractableResource)
        FluidAmount = ReturnValue_1
        ReturnValue_2: int32 = self.mBuildableExtractor.GetScaledFluidStackSize()
        ReturnValue1: float = Conv_IntToFloat(ReturnValue_2)
        ReturnValue2: float = Conv_IntToFloat(FluidAmount)
        ReturnValue1_0: float = ReturnValue2 / ReturnValue1
        self.mFluidTank.UpdateTankValue(ReturnValue1_0)
        ReturnValue_3: float = Conv_IntToFloat(FluidAmount)
        ReturnValue_4: float = ReturnValue_3 / 1000
        ReturnValue_5: FText = Default__KismetTextLibrary.Conv_FloatToText(ReturnValue_4, 0, False, True, 1, 324, 0, 1)
        self.mCurrentAmountInPipeText.SetText(ReturnValue_5)
    

    def UpdateFlowRate(self):
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(self.mBuildableExtractor)
        if not ReturnValue:
            goto('L835')
        ReturnValue_0: float = self.mBuildableExtractor.GetFlowRateSmoothed()
        ReturnValue_1: float = ReturnValue_0 * 60
        ReturnValue_2: FText = Default__KismetTextLibrary.Conv_FloatToText(ReturnValue_1, 0, False, True, 1, 324, 0, 0)
        self.mFlowRateText.SetText(ReturnValue_2)
        ReturnValue_0 = self.mBuildableExtractor.GetFlowRateSmoothed()
        ReturnValue_3: float = ReturnValue_0 / 10
        ReturnValue_4: float = FClamp(ReturnValue_3, 0, 1)
        self.mFlowRateGauge.UpdateGaugeValue(ReturnValue_4)
        ReturnValue_5: float = self.mBuildableExtractor.GetCurrentPotential()
        ReturnValue_6: float = self.mBuildableExtractor.GetMaxFlowRate()
        ReturnValue_7: int32 = self.mBuildableExtractor.GetNumExtractedItemsPerCycle()
        ReturnValue_8: float = Conv_IntToFloat(ReturnValue_7)
        ReturnValue1: float = ReturnValue_8 / 1000
        ReturnValue1_0: float = ReturnValue1 * ReturnValue_5
        ReturnValue2: float = ReturnValue1_0 / ReturnValue_6
        self.mFlowRateGauge.SetDividerPosition(ReturnValue2)
    

    def Construct(self):
        self.ExecuteUbergraph_BPW_ExtractorPump(1234)
    

    def Tick(self):
        ExecuteUbergraph_BPW_ExtractorPump.K2Node_Event_MyGeometry = MyGeometry #  PERSISTENT_FRAME(
        ExecuteUbergraph_BPW_ExtractorPump.K2Node_Event_InDeltaTime = InDeltaTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BPW_ExtractorPump(1239)
    

    def BndEvt__Widget_StandbyButton_K2Node_ComponentBoundEvent_1_OnStandbyClicked__DelegateSignature(self):
        self.ExecuteUbergraph_BPW_ExtractorPump(1648)
    

    def BndEvt__mBuildableExtractor_K2Node_ComponentBoundEvent_2_BuildingStateChanged__DelegateSignature(self, State: bool):
        ExecuteUbergraph_BPW_ExtractorPump.K2Node_ComponentBoundEvent_state = State #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BPW_ExtractorPump(1663)
    

    def BndEvt__Widget_Window_DarkMode_K2Node_ComponentBoundEvent_0_OnClose__DelegateSignature(self):
        self.ExecuteUbergraph_BPW_ExtractorPump(1678)
    

    def Destruct(self):
        self.ExecuteUbergraph_BPW_ExtractorPump(1693)
    

    def ExecuteUbergraph_BPW_ExtractorPump(self):
        goto(ComputedJump("EntryPoint"))
        # Label 15
        self.Construct()
        Extractor: Ptr[FGBuildableResourceExtractor] = Cast[FGBuildableResourceExtractor](self.mInteractObject)
        bSuccess: bool = Extractor
        if not bSuccess:
           goto(ExecutionFlow.Pop())
        self.mBuildableExtractor = Extractor
        ReturnValue: TScriptInterface[FGExtractableResourceInterface] = self.mBuildableExtractor.GetExtractableResource()
        ReturnValue_0: TSubclassOf[FGResourceDescriptor] = GetInterfaceUObject(ReturnValue).GetResourceClass()
        self.mExtractableResource = ReturnValue_0
        self.Widget_StandbyButton.mBuildableFactory = self.mBuildableExtractor
        self.SetupStaticInfo()
        self.Widget_Overclock.mBuildableFactory = self.mBuildableExtractor
        self.UpdateWarning()
        self.Widget_Window_DarkMode.SetTitle(self.mBuildableExtractor.mDisplayName)
        self.Widget_Window_DarkMode.SetInventoryVisibility(True, False)
        
        Slots = None
        self.Widget_Overclock.GetUnlockedOverclockSlots(Ref[Slots])
        Variable1: int32 = 0
        Variable: int32 = 0
        
        Slots = None
        # Label 541
        ReturnValue_1: int32 = len(Slots)
        ReturnValue1: bool = Variable1 <= ReturnValue_1
        # Label 638
        if not ReturnValue1:
           goto(ExecutionFlow.Pop())
        Variable = Variable1
        ExecutionFlow.Push("L804")
        OutputDelegate.BindUFunction(self, OnInventorySlotStackMove)
        
        Slots = None
        Item = None
        Item = Slots[Variable]
        Item.OnMoveStack.AddUnique(OutputDelegate)
        goto(ExecutionFlow.Pop())
        # Label 804
        ReturnValue1_0: int32 = Variable1 + 1
        Variable1 = ReturnValue1_0
        goto('L541')
        # Label 878
        ExecutionFlow.Push("L975")
        
        Slots1 = None
        Item1 = None
        Item1 = Slots1[Variable1_0]
        Item1.OnMoveStack.Clear()
        goto(ExecutionFlow.Pop())
        # Label 975
        ReturnValue_2: int32 = Variable_0 + 1
        Variable_0: int32 = ReturnValue_2
        
        Slots1 = None
        # Label 1044
        ReturnValue1_1: int32 = len(Slots1)
        ReturnValue_3: bool = Variable_0 <= ReturnValue1_1
        if not ReturnValue_3:
           goto(ExecutionFlow.Pop())
        Variable1_0: int32 = Variable_0
        goto('L878')
        # Label 1183
        Variable_0 = 0
        Variable1_0 = 0
        goto('L1044')
        goto('L15')
        self.UpdateFlowRate()
        self.UpdateFluidTank()
        ReturnValue_4: float = self.mBuildableExtractor.GetProductivity()
        ReturnValue_5: float = self.mBuildableExtractor.GetProducingPowerConsumption()
        ReturnValue_6: float = self.mBuildableExtractor.GetProductionCycleTime()
        ReturnValue_7: int32 = self.mBuildableExtractor.GetNumExtractedItemsPerCycle()
        self.mOutputSlot.UpdateProductionStats(ReturnValue_7, ReturnValue_6, ReturnValue_5, ReturnValue_4, 0)
        ReturnValue_8: float = self.mBuildableExtractor.GetProductionProgress()
        self.mOutputSlot.UpdateCycleProgress(ReturnValue_8)
        goto(ExecutionFlow.Pop())
        self.UpdateWarning()
        goto(ExecutionFlow.Pop())
        self.UpdateWarning()
        goto(ExecutionFlow.Pop())
        self.OnEscapePressed()
        goto(ExecutionFlow.Pop())
        self.Destruct()
        
        Slots1 = None
        self.Widget_Overclock.GetUnlockedOverclockSlots(Ref[Slots1])
        goto('L1183')
    
