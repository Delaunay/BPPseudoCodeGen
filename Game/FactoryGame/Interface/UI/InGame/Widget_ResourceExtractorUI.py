
from codegen.ue4_stub import *

from Game.FactoryGame.Character.Player.BP_RemoteCallObject import BP_RemoteCallObject
from Script.FactoryGame import FGBuildableResourceExtractor
from Script.Engine import Conv_TextToString
from Script.FactoryGame import FGResourceDescriptor
from Script.FactoryGame import GetExtractableResource
from Game.FactoryGame.Buildable.Factory.WaterPump.Build_WaterPump import Build_WaterPump
from Script.Engine import Conv_IntToFloat
from Script.Engine import Not_PreBool
from Script.Engine import FTrunc
from Script.Engine import Default__KismetSystemLibrary
from Script.FactoryGame import Get
from Script.Engine import PlayerController
from Script.Engine import Default__KismetArrayLibrary
from Script.Engine import FormatArgumentData
from Script.FactoryGame import GetItemName
from Script.UMG import ESlateVisibility
from Game.FactoryGame.Interface.UI.InGame.Widget_ResourceExtractorUI import ExecuteUbergraph_Widget_ResourceExtractorUI.K2Node_Event_MyGeometry
from Script.FactoryGame import GetNumExtractedItemsPerCycle
from Game.FactoryGame.Interface.UI.InGame.Widget_UseableBase import Construct
from Script.Engine import Conv_FloatToText
from Script.Engine import TimerHandle
from Script.CoreUObject import Object
from Script.Engine import IsValid
from Game.FactoryGame.Interface.UI.InGame.InventorySlots.Widget_InventorySlot import Widget_InventorySlot
from Script.UMG import SetPercent
from Script.FactoryGame import FGInventoryComponent
from Script.Engine import Conv_IntToText
from Game.FactoryGame.Resource.Environment.Crystal.Desc_CrystalShard import Desc_CrystalShard
from Script.FactoryGame import IsProductionPaused
from Script.Engine import Default__KismetTextLibrary
from Script.FactoryGame import FGExtractableResourceInterface
from Script.UMG import SetFillColorAndOpacity
from Script.Engine import BooleanOR
from Game.FactoryGame.Interface.UI.InGame.Widget_ResourceExtractorUI import ExecuteUbergraph_Widget_ResourceExtractorUI
from Game.FactoryGame.Interface.UI.InGame.Widget_ResourceExtractorUI import ExecuteUbergraph_Widget_ResourceExtractorUI.K2Node_Event_InDeltaTime
from Script.FactoryGame import GetIsBuildingOverclockUnlocked
from Script.UMG import Tick
from Script.Engine import Format
from Game.FactoryGame.Interface.UI.InGame.Widget_UseableBase import Widget_UseableBase
from Script.FactoryGame import Init
from Script.Engine import Default__KismetStringLibrary
from Script.FactoryGame import FGUnlockSubsystem
from Script.FactoryGame import GetProducingPowerConsumption
from Script.FactoryGame import GetRemoteCallObjectOfClass
from Game.FactoryGame.Interface.UI.HUDHelpers.HUDHelpers import Default__HUDHelpers
from Script.Engine import SelectColor
from Script.FactoryGame import GetProductivity
from Script.Engine import Conv_StringToFloat
from Game.FactoryGame.Interface.UI.InGame.OutputSlotData_Struct import OutputSlotData_Struct
from Script.FactoryGame import Default__FGItemDescriptor
from Game.FactoryGame.Interface.UI.InGame.Widget_UseableBase import Destruct
from Script.FactoryGame import FGItemDescriptor
from Game.FactoryGame.Character.Player.BP_PlayerController import BP_PlayerController
from Script.FactoryGame import GetOutputInventory
from Script.FactoryGame import Default__FGUnlockSubsystem
from Script.Engine import K2_ClearAndInvalidateTimerHandle
from Script.CoreUObject import LinearColor

class Widget_ResourceExtractorUI(Widget_UseableBase):
    mDesiredMiningIndex: int32
    mResourceExtractor: Ptr[FGBuildableResourceExtractor]
    mSelectedMiningIndex: int32 = -1
    mExtractorNode: Ptr[Object]
    mTitleText: FText = NSLOCTEXT("", "DCB14CD94CCC3E575495FE9C82179079", "EXTRACTOR")
    mCurrentOreClass: TSubclassOf[FGItemDescriptor]
    mCheckOreTimer: TimerHandle
    NewOutputSlot: Ptr[Widget_InventorySlot]
    mShouldOpenInventory = True
    mUseKeyboard = True
    mUseMouse = True
    mCaptureInput = True
    mRestoreFocusWhenLost = True
    mInputToPassThrough = ['Use']
    mDesiredHorizontalAlignment = 2
    mDesiredVerticalAlignment = 2
    mUseGamepadCursor = True
    mCallCustomTickOnConstruct = True
    bHasScriptImplementedTick = True
    
    def CleanUpBindings(self):
        ExecutionFlow.Push("L442")
        self.NewOutputSlot.OnMoveStack.Clear()
        
        Slots = None
        self.Widget_Overclock.GetUnlockedOverclockSlots(Ref[Slots])
        Variable: int32 = 0
        Variable_0: int32 = 0
        
        Slots = None
        # Label 128
        ReturnValue: int32 = len(Slots)
        ReturnValue_0: bool = Variable <= ReturnValue
        if not ReturnValue_0:
            goto('L363')
        Variable_0 = Variable
        ExecutionFlow.Push("L368")
        
        Slots = None
        Item = None
        Item = Slots[Variable_0]
        Item.OnMoveStack.Clear()
        goto(ExecutionFlow.Pop())
        # Label 363
        # End
        # Label 368
        ReturnValue_1: int32 = Variable + 1
        Variable = ReturnValue_1
        goto('L128')
    

    def DropInventorySlotStack(self):
        ExecutionFlow.Push("L854")
        
        Result = None
        self.NewOutputSlot.DropOntoInventorySlot(InventorySlot, Ref[Result])
        if not Result:
            goto('L89')
        WasStackMoved = True
        # End
        
        Slots = None
        # Label 89
        self.Widget_Overclock.GetUnlockedOverclockSlots(Ref[Slots])
        Variable: bool = False
        Variable_0: int32 = 0
        Variable_1: int32 = 0
        # Label 191
        ReturnValue: bool = Not_PreBool(Variable)
        
        Slots = None
        ReturnValue_0: int32 = len(Slots)
        ReturnValue_1: bool = Variable_0 <= ReturnValue_0
        ReturnValue_2: bool = ReturnValue and ReturnValue_1
        if not ReturnValue_2:
            goto('L756')
        Variable_1 = Variable_0
        ExecutionFlow.Push("L780")
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
        
        Result1 = None
        Item.DropOntoInventorySlot(InventorySlot, Ref[Result1])
        if not Result1:
           goto(ExecutionFlow.Pop())
        Variable_2: bool = True
        Variable = True
        goto(ExecutionFlow.Pop())
        # Label 756
        WasStackMoved = Variable_2
        # End
        # Label 780
        ReturnValue_3: int32 = Variable_0 + 1
        Variable_0 = ReturnValue_3
        goto('L191')
    

    def GetWarningVisibility(self, buildableResourceExtractor: Ptr[FGBuildableResourceExtractor]):
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(buildableResourceExtractor)
        if not ReturnValue:
            goto('L368')
        ReturnValue_0: bool = buildableResourceExtractor.HasPower()
        ReturnValue_1: bool = Not_PreBool(ReturnValue_0)
        ReturnValue_2: bool = buildableResourceExtractor.IsProductionPaused()
        ReturnValue_3: bool = BooleanOR(ReturnValue_2, ReturnValue_1)
        Variable: uint8 = 0
        Variable_0: bool = ReturnValue_3
        Variable1: uint8 = 1
        
        switch = {
            False: Variable1,
            True: Variable
        }
        self.mWarningWidget.SetVisibility(switch.get(Variable_0, None))
    

    def UpdateOutputInfo(self):
        ReturnValue: TScriptInterface[FGExtractableResourceInterface] = self.mResourceExtractor.GetExtractableResource()
        ReturnValue_0: TSubclassOf[FGResourceDescriptor] = GetInterfaceUObject(ReturnValue).GetResourceClass()
        ReturnValue_1: FText = Default__FGItemDescriptor.GetItemName(ReturnValue_0)
        self.Widget_ManufacturingOutput_Slot.mRecipeName.SetText(ReturnValue_1)
    

    def UpdateExtractorStats(self):
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(self.mResourceExtractor)
        if not ReturnValue:
            goto('L2129')
        ReturnValue_0: int32 = self.mResourceExtractor.GetNumExtractedItemsPerCycle()
        ReturnValue_1: float = Conv_IntToFloat(ReturnValue_0)
        Pump: Ptr[Build_WaterPump] = Cast[Build_WaterPump](self.mResourceExtractor)
        bSuccess: bool = Pump
        ReturnValue1: float = ReturnValue_1 / 1000
        Variable: bool = bSuccess
        ReturnValue_2: float = ReturnValue1 * 60
        ReturnValue_3: float = self.mResourceExtractor.GetProductionCycleTime()
        ReturnValue_4: FText = Default__KismetTextLibrary.Conv_FloatToText(ReturnValue_2, 0, False, True, 1, 324, 0, 1)
        ReturnValue2: float = 60 / ReturnValue_3
        FormatArgumentData.ArgumentName = "value"
        FormatArgumentData.ArgumentValueType = 4
        FormatArgumentData.ArgumentValue = ReturnValue_4
        FormatArgumentData.ArgumentValueInt = 0
        FormatArgumentData.ArgumentValueFloat = 0
        FormatArgumentData.ArgumentValueGender = 0
        ReturnValue_5: float = ReturnValue_0 * ReturnValue2
        Array: List[FormatArgumentData] = [FormatArgumentData]
        ReturnValue1_0: FText = Default__KismetTextLibrary.Conv_FloatToText(ReturnValue_5, 0, False, True, 1, 324, 1, 1)
        ReturnValue_6: FText = Default__KismetTextLibrary.Format("{'Instruction': 'EX_UnicodeStringConst', 'InstOffsetFromTop': 891, 'Value': '{value} m³'}", Array)
        
        switch = {
            False: ReturnValue1_0,
            True: ReturnValue_6
        }
        self.Widget_ManufacturingOutput_Slot.mNumPerSecond.SetText(switch.get(Variable, None))
        ReturnValue1_1: float = self.mResourceExtractor.GetProductivity()
        self.Widget_ManufacturingOutput_Slot.mEfficiency.mManufacturingStat = ReturnValue1_1
        ReturnValue1_2: float = self.mResourceExtractor.GetProductionCycleTime()
        ReturnValue2_0: FText = Default__KismetTextLibrary.Conv_FloatToText(ReturnValue1_2, 0, False, True, 1, 324, 1, 1)
        
        ReturnValue_7: FString = Default__KismetTextLibrary.Conv_TextToString(Ref[ReturnValue2_0])
        ReturnValue_8: float = Default__KismetStringLibrary.Conv_StringToFloat(ReturnValue_7)
        self.Widget_ManufacturingOutput_Slot.mCycleTime.mManufacturingStat = ReturnValue_8
        ReturnValue_9: float = self.mResourceExtractor.GetProducingPowerConsumption()
        ReturnValue3: FText = Default__KismetTextLibrary.Conv_FloatToText(ReturnValue_9, 0, False, True, 1, 324, 1, 1)
        
        ReturnValue1_3: FString = Default__KismetTextLibrary.Conv_TextToString(Ref[ReturnValue3])
        ReturnValue1_4: float = Default__KismetStringLibrary.Conv_StringToFloat(ReturnValue1_3)
        self.Widget_ManufacturingOutput_Slot.mPowerConsumption.mManufacturingStat = ReturnValue1_4
        ReturnValue_10: float = self.mResourceExtractor.GetProductivity()
        ReturnValue_11: bool = ReturnValue_10 > 0
        if not ReturnValue_11:
            goto('L2084')
        ReturnValue_10 = self.mResourceExtractor.GetProductivity()
        ReturnValue_12: float = 0.20000000298023224 / ReturnValue_10
        self.Widget_Turbine.mSpeed = ReturnValue_12
        # End
        # Label 2084
        self.Widget_Turbine.mSpeed = 0
    

    def UpdateExtractorProgress(self):
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(self.mResourceExtractor)
        if not ReturnValue:
            goto('L1233')
        ReturnValue_0: float = self.mResourceExtractor.GetProductionProgress()
        self.Widget_ManufacturingOutput_Slot.mProgressBar.mProgressBar.SetPercent(ReturnValue_0)
        ReturnValue1: float = self.mResourceExtractor.GetProductionProgress()
        ReturnValue_1: float = ReturnValue1 * 10
        ReturnValue_2: int32 = FTrunc(ReturnValue_1)
        ReturnValue_3: int32 = ReturnValue_2 * 10
        ReturnValue_4: FText = Default__KismetTextLibrary.Conv_IntToText(ReturnValue_3, False, False, 1, 324)
        FormatArgumentData.ArgumentName = "A"
        FormatArgumentData.ArgumentValueType = 4
        FormatArgumentData.ArgumentValue = ReturnValue_4
        FormatArgumentData.ArgumentValueInt = 0
        FormatArgumentData.ArgumentValueFloat = 0
        FormatArgumentData.ArgumentValueGender = 0
        Array: List[FormatArgumentData] = [FormatArgumentData]
        ReturnValue_5: FText = Default__KismetTextLibrary.Format("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 709, 'Value': '{A}%'}", Array)
        self.Widget_ManufacturingOutput_Slot.mPercentageText.SetText(ReturnValue_5)
        ReturnValue_6: bool = self.mResourceExtractor.IsProductionPaused()
        ReturnValue_7: bool = self.mResourceExtractor.HasPower()
        
        Text = None
        Graphics = None
        Default__HUDHelpers.GetFactoryGameLightGray(self, Ref[Text], Ref[Graphics])
        ReturnValue_8: bool = Not_PreBool(ReturnValue_7)
        
        Text = None
        Graphics = None
        Default__HUDHelpers.GetFactoryGameDarkGray(self, Ref[Text], Ref[Graphics])
        ReturnValue_9: bool = BooleanOR(ReturnValue_8, ReturnValue_6)
        ReturnValue_10: LinearColor = SelectColor(Graphics, Graphics, ReturnValue_9)
        self.Widget_ManufacturingOutput_Slot.mProgressBar.mProgressBar.SetFillColorAndOpacity(ReturnValue_10)
    

    def GetOverclockWidgetVisibility(self):
        Variable: uint8 = 4
        Variable1: uint8 = 1
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_0: Ptr[FGUnlockSubsystem] = Default__FGUnlockSubsystem.Get(ReturnValue)
        ReturnValue_1: bool = ReturnValue_0.GetIsBuildingOverclockUnlocked()
        Variable_0: bool = ReturnValue_1
        
        switch = {
            False: Variable1,
            True: Variable
        }
        ReturnValue_2: uint8 = switch.get(Variable_0, None)
    

    def Init(self):
        self.ExecuteUbergraph_Widget_ResourceExtractorUI(30)
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_ResourceExtractorUI(1042)
    

    def Tick(self):
        ExecuteUbergraph_Widget_ResourceExtractorUI.K2Node_Event_MyGeometry = MyGeometry #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_ResourceExtractorUI.K2Node_Event_InDeltaTime = InDeltaTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_ResourceExtractorUI(1918)
    

    def BndEvt__Widget_StandbyButton_K2Node_ComponentBoundEvent_0_OnStandbyClicked__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_ResourceExtractorUI(1975)
    

    def BndEvt__Widget_Window_DarkMode_K2Node_ComponentBoundEvent_2_OnClose__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_ResourceExtractorUI(1980)
    

    def Destruct(self):
        self.ExecuteUbergraph_Widget_ResourceExtractorUI(1985)
    

    def ExecuteUbergraph_Widget_ResourceExtractorUI(self):
        goto(ComputedJump("EntryPoint"))
        # Label 15
        self.CleanUpBindings()
        goto(ExecutionFlow.Pop())
        self.Init()
        self.mWarningWidget.mResourceExtractor = self.mResourceExtractor
        ReturnValue: Ptr[FGInventoryComponent] = self.mResourceExtractor.GetOutputInventory()
        Struct.Title_3_16865392480E04744923368E818FDF9E = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 152, 'Value': 'Output'}"
        Struct.InventoryComponent_6_670B318B4DE9249E98B040BFD46013A9 = ReturnValue
        Struct.InventorySlotIndex_10_ECF91A0C4E759F6F2FC3768CE0512AB9 = 0
        Array: List[OutputSlotData_Struct] = [Struct]
        
        self.Widget_ManufacturingOutput_Slot.GenerateOutputSlots(Ref[Array])
        
        InventorySlot = None
        Success = None
        self.Widget_ManufacturingOutput_Slot.GetSlot(0, Ref[InventorySlot], Ref[Success])
        self.NewOutputSlot = InventorySlot
        self.Widget_Overclock.mBuildableFactory = self.mResourceExtractor
        ReturnValue1: bool = self.mResourceExtractor.IsProductionPaused()
        self.Widget_StandbyButton.SetStandbyButtonBrush(ReturnValue1)
        self.GetWarningVisibility(self.mResourceExtractor)
        OutputDelegate.BindUFunction(self, OnInventorySlotStackMove)
        self.NewOutputSlot.OnMoveStack.AddUnique(OutputDelegate)
        
        Slots = None
        self.Widget_Overclock.GetUnlockedOverclockSlots(Ref[Slots])
        Variable: int32 = 0
        Variable_0: int32 = 0
        
        Slots = None
        # Label 705
        ReturnValue_0: int32 = len(Slots)
        ReturnValue_1: bool = Variable <= ReturnValue_0
        if not ReturnValue_1:
           goto(ExecutionFlow.Pop())
        Variable_0 = Variable
        ExecutionFlow.Push("L968")
        
        Slots = None
        Item = None
        Item = Slots[Variable_0]
        OutputDelegate1.BindUFunction(self, OnInventorySlotStackMove)
        Item.OnMoveStack.AddUnique(OutputDelegate1)
        goto(ExecutionFlow.Pop())
        # Label 968
        ReturnValue_2: int32 = Variable + 1
        Variable = ReturnValue_2
        goto('L705')
        self.Construct()
        self.Widget_Window_DarkMode.SetTitle("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 1089, 'Value': 'Miner'}")
        Extractor: Ptr[FGBuildableResourceExtractor] = Cast[FGBuildableResourceExtractor](self.mInteractObject)
        bSuccess: bool = Extractor
        if not bSuccess:
           goto(ExecutionFlow.Pop())
        self.mResourceExtractor = Extractor
        self.UpdateOutputInfo()
        
        self.Widget_InventorySlot_DropArea.mInventorySlots = None
        ReturnValue_3: int32 = self.Widget_InventorySlot_DropArea.mInventorySlots.append(self.NewOutputSlot)
        ReturnValue_4: TScriptInterface[FGExtractableResourceInterface] = self.mResourceExtractor.GetExtractableResource()
        ReturnValue_5: TSubclassOf[FGResourceDescriptor] = GetInterfaceUObject(ReturnValue_4).GetResourceClass()
        Array1: Const[List[TSubclassOf[FGItemDescriptor]]] = [ReturnValue_5, Desc_CrystalShard]
        
        self.Widget_Window_DarkMode.SetupRelevantInventory(Ref[Array1])
        goto(ExecutionFlow.Pop())
        # Label 1503
        self.OnEscapePressed()
        goto(ExecutionFlow.Pop())
        # Label 1532
        ReturnValue_6: Ptr[PlayerController] = self.GetOwningPlayer()
        Controller: Ptr[BP_PlayerController] = Cast[BP_PlayerController](ReturnValue_6)
        bSuccess1: bool = Controller
        if not bSuccess1:
           goto(ExecutionFlow.Pop())
        ReturnValue_7: Ptr[BP_RemoteCallObject] = Controller.GetRemoteCallObjectOfClass(BP_RemoteCallObject)
        ReturnValue_8: bool = self.mResourceExtractor.IsProductionPaused()
        ReturnValue_9: bool = Not_PreBool(ReturnValue_8)
        ReturnValue_7.Server_SetIsProductionPausedOnFactory(self.mResourceExtractor, ReturnValue_9)
        ReturnValue_8 = self.mResourceExtractor.IsProductionPaused()
        self.Widget_StandbyButton.SetStandbyButtonBrush(ReturnValue_8)
        self.GetWarningVisibility(self.mResourceExtractor)
        goto(ExecutionFlow.Pop())
        self.Tick(MyGeometry, InDeltaTime)
        self.UpdateExtractorProgress()
        self.UpdateExtractorStats()
        goto(ExecutionFlow.Pop())
        goto('L1532')
        goto('L1503')
        self.Destruct()
        
        Default__KismetSystemLibrary.K2_ClearAndInvalidateTimerHandle(self, Ref[self.mCheckOreTimer])
        goto('L15')
    
