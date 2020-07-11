
from codegen.ue4_stub import *

from Script.FactoryGame import GetPowerCircuit
from Script.Engine import Texture2D
from Script.UMG import AddChild
from Script.Engine import Default__KismetSystemLibrary
from Script.UMG import ESlateVisibility
from Game.FactoryGame.Interface.UI.InGame.Widget_UseableBase import Construct
from Script.FactoryGame import GetCurrentFuelClass
from Script.Engine import TimerHandle
from Script.Engine import IsValid
from Script.UMG import SetPercent
from Script.FactoryGame import GetSmallIcon
from Script.UMG import SetFillColorAndOpacity
from Script.Engine import NotEqual_FloatFloat
from Script.FactoryGame import Init
from Game.FactoryGame.Buildable.Factory.GeneratorFuel.Build_GeneratorFuel import Build_GeneratorFuel
from Game.FactoryGame.Interface.UI.HUDHelpers.HUDHelpers import Default__HUDHelpers
from Game.FactoryGame.Interface.UI.InGame.Widget_UseableBase import Destruct
from Script.UMG import Create
from Script.FactoryGame import InventoryItem
from Script.FactoryGame import GetFuelInventory
from Game.FactoryGame.Character.Player.BP_PlayerController import BP_PlayerController
from Game.FactoryGame.Resource.Parts.NuclearWaste.Desc_NuclearWaste import Desc_NuclearWaste
from Script.FactoryGame import Default__FGUnlockSubsystem
from Script.Engine import K2_ClearAndInvalidateTimerHandle
from Script.FactoryGame import GetFuelAmount
from Script.FactoryGame import FGPlayerController
from Script.FactoryGame import GetSupplementalResourceClass
from Script.FactoryGame import FGBuildable
from Script.FactoryGame import FGPowerInfoComponent
from Script.FactoryGame import GetSupplementalConsumptionRateMaximum
from Script.FactoryGame import GetAmountConvertedByForm
from Script.Engine import Default__KismetArrayLibrary
from Script.FactoryGame import FGBuildableGeneratorFuel
from Script.FactoryGame import FGBuildableGeneratorNuclear
from Script.FactoryGame import FGInventoryComponent
from Game.FactoryGame.Interface.UI.InGame.InventorySlots.Widget_InventorySlot import Widget_InventorySlot
from Script.FactoryGame import GetRequiresSupplementalResource
from Script.FactoryGame import GetIsBuildingOverclockUnlocked
from Game.FactoryGame.Buildable.-Shared.Widgets.Widget_Generator import ExecuteUbergraph_Widget_Generator.K2Node_CustomEvent_state
from Script.FactoryGame import FGBuildableGenerator
from Script.FactoryGame import GetWasteInventory
from Script.AkAudio import Default__AkGameplayStatics
from Game.FactoryGame.Buildable.-Shared.Widgets.Widget_Generator import ExecuteUbergraph_Widget_Generator.K2Node_Event_UpdateTime
from Script.FactoryGame import Default__FGItemDescriptor
from Script.FactoryGame import GetCircuitID
from Script.AkAudio import AkComponent
from Script.FactoryGame import GetPowerInfo
from Script.AkAudio import PostAkEvent
from Script.FactoryGame import GetEnergyValue
from Script.Engine import K2_SetTimerDelegate
from Game.FactoryGame.Buildable.-Shared.Widgets.Widget_Generator import ExecuteUbergraph_Widget_Generator
from Script.FactoryGame import Default__FGInventoryLibrary
from Script.FactoryGame import FGPowerCircuit
from Script.UMG import PanelSlot
from Script.Engine import HasAuthority
from Script.FactoryGame import Get
from Script.Engine import PlayerController
from Script.UMG import PlayAnimation
from Game.FactoryGame.Resource.Environment.Crystal.Desc_CrystalShard import Desc_CrystalShard
from Script.UMG import Default__WidgetBlueprintLibrary
from Script.FactoryGame import IsProductionPaused
from Script.FactoryGame import GetPowerProductionCapacity
from Script.FactoryGame import IsFuseTriggered
from Script.FactoryGame import GetLoadPercentage
from Script.FactoryGame import IsConnected
from Game.FactoryGame.Interface.UI.InGame.-Shared.Widget_Smoke import Widget_Smoke
from Game.FactoryGame.Interface.UI.InGame.Widget_UseableBase import Widget_UseableBase
from Script.FactoryGame import GetScaledFluidStackSize
from Script.FactoryGame import GetRemoteCallObjectOfClass
from Script.FactoryGame import FGItemDescriptor
from Game.FactoryGame.Character.Player.BP_RemoteCallObject import BP_RemoteCallObject
from Script.FactoryGame import GetAvailableFuelClasses
from Script.FactoryGame import HasEnoughSpaceForItem
from Script.Engine import Not_PreBool
from Script.FactoryGame import GetItemName
from Script.UMG import PauseAnimation
from Script.FactoryGame import GetCurrentPotential
from Game.FactoryGame.Interface.UI.Audio.PowerStatus.Play_UI_PowerLossWarning_ResetFuse import Play_UI_PowerLossWarning_ResetFuse
from Script.Engine import BooleanOR
from Script.FactoryGame import MakeInventoryItem
from Script.UMG import WidgetAnimation
from Script.FactoryGame import FGUnlockSubsystem
from Script.UMG import UMGSequencePlayer
from Script.UMG import IsAnimationPlaying
from Script.Engine import IsValidClass

class Widget_Generator(Widget_UseableBase):
    NuclearGlowStop: Ptr[WidgetAnimation]
    NuclearGlow: Ptr[WidgetAnimation]
    mFuelGenerator: Ptr[FGBuildableGeneratorFuel]
    mWarningMessageTimerHandle: TimerHandle
    mGenerator: Ptr[FGBuildableGenerator]
    mNuclearGenerator: Ptr[FGBuildableGeneratorNuclear]
    SmokeTimer: TimerHandle
    PreviousEffiency: float
    UpdateSlotStatsTimer: TimerHandle
    mRelevantItems: List[TSubclassOf[FGItemDescriptor]]
    InputSlot: Ptr[Widget_InventorySlot]
    mWasteSlot: Ptr[Widget_InventorySlot]
    mFluidClass: TSubclassOf[FGItemDescriptor] = NewObject[Desc_Water]()
    mIsFluidGenerator: bool
    mShouldOpenInventory = True
    mUseKeyboard = True
    mUseMouse = True
    mCaptureInput = True
    mRestoreFocusWhenLost = True
    mInputToPassThrough = ['Use']
    mUseGamepadCursor = True
    mCustomTickRate = 0.10000000149011612
    mCallCustomTickOnConstruct = True
    
    def UpdateFluidStats(self):
        ReturnValue: bool = self.mFuelGenerator.GetRequiresSupplementalResource()
        if not ReturnValue:
            goto('L447')
        ReturnValue_0: int32 = self.mFuelGenerator.GetScaledFluidStackSize()
        ReturnValue_1: Ptr[FGInventoryComponent] = self.mFuelGenerator.GetFuelInventory()
        ReturnValue_2: float = Default__FGInventoryLibrary.GetAmountConvertedByForm(ReturnValue_0, 2)
        
        numItems = None
        Default__HUDHelpers.GetNumItemsFromInventory(ReturnValue_1, self.mFluidClass, self, Ref[numItems])
        ReturnValue_3: float = self.mFuelGenerator.GetSupplementalConsumptionRateMaximum()
        ReturnValue1: float = Default__FGInventoryLibrary.GetAmountConvertedByForm(numItems, 2)
        self.BPW_FluidModule.UpdateValues(ReturnValue_2, ReturnValue1, ReturnValue_3)
    

    def SetupInputs(self):
        ReturnValue: Ptr[FGInventoryComponent] = self.mFuelGenerator.GetFuelInventory()
        Struct1.Title_3_16865392480E04744923368E818FDF9E = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 71, 'Value': 'Fuel'}"
        Struct1.InventoryComponent_6_670B318B4DE9249E98B040BFD46013A9 = ReturnValue
        Struct1.InventorySlotIndex_10_ECF91A0C4E759F6F2FC3768CE0512AB9 = 0
        
        Struct1 = None
        # Label 173
        ReturnValue1: int32 = LocalInputs.append(Struct1)
        ReturnValue1_0: bool = Default__KismetSystemLibrary.IsValid(self.mNuclearGenerator)
        if not ReturnValue1_0:
            goto('L548')
        ReturnValue_0: Ptr[FGInventoryComponent] = self.mNuclearGenerator.GetWasteInventory()
        Struct.Title_3_16865392480E04744923368E818FDF9E = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 377, 'Value': 'Waste'}"
        Struct.InventoryComponent_6_670B318B4DE9249E98B040BFD46013A9 = ReturnValue_0
        Struct.InventorySlotIndex_10_ECF91A0C4E759F6F2FC3768CE0512AB9 = 0
        
        Struct = None
        ReturnValue_1: int32 = LocalInputs.append(Struct)
        
        # Label 548
        self.Widget_Output_Slot.GenerateOutputSlots(Ref[LocalInputs])
        
        InventorySlot1 = None
        Success1 = None
        # Label 593
        self.Widget_Output_Slot.GetSlot(0, Ref[InventorySlot1], Ref[Success1])
        self.InputSlot = InventorySlot1
        ReturnValue_2: bool = Default__KismetSystemLibrary.IsValid(self.mNuclearGenerator)
        if not ReturnValue_2:
            goto('L814')
        
        InventorySlot = None
        Success = None
        self.Widget_Output_Slot.GetSlot(1, Ref[InventorySlot], Ref[Success])
        self.mWasteSlot = InventorySlot
    

    def OnReplicationDetailActorCreated(self, ReplicationDetailActor: Ptr[Actor]):
        self.SetupInputs()
    

    def InitModule(self):
        Variable2: uint8 = 1
        Variable3: uint8 = 3
        ReturnValue2: bool = Default__KismetSystemLibrary.IsValid(self.mNuclearGenerator)
        Variable1: bool = ReturnValue2
        
        switch = {
            False: Variable3,
            True: Variable2
        }
        self.mModuleFuel.SetVisibility(switch.get(Variable1, None))
        Variable: uint8 = 3
        Variable1_0: uint8 = 1
        ReturnValue1: bool = Default__KismetSystemLibrary.IsValid(self.mNuclearGenerator)
        Variable_0: bool = ReturnValue1
        
        switch_0 = {
            False: Variable1_0,
            True: Variable
        }
        self.mModuleNuclear.SetVisibility(switch_0.get(Variable_0, None))
        ReturnValue: bool = self.mGenerator.IsProducing()
        ReturnValue_0: bool = Default__KismetSystemLibrary.IsValid(self.mNuclearGenerator)
        ReturnValue_1: bool = ReturnValue_0 and ReturnValue
        if not ReturnValue_1:
            goto('L593')
        ReturnValue_2: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.NuclearGlow, 0, 0, 0, 1)
    

    def UpdateHeaderText(self):
        AsFGBuildable: Ptr[FGBuildable] = Cast[FGBuildable](self.mInteractObject)
        bSuccess: bool = AsFGBuildable
        if not bSuccess:
            goto('L146')
        self.Widget_Window_DarkMode.SetTitle(AsFGBuildable.mDisplayName)
    

    def UpdateWarningWidget(self):
        ReturnValue1: bool = Default__KismetSystemLibrary.IsValid(self.mFuelGenerator)
        if not ReturnValue1:
            goto('L1705')
        mLocalGenerator = self.mFuelGenerator
        
        IsConnected = None
        self.IsConnected(Ref[IsConnected])
        if not IsConnected:
            goto('L1281')
        self.mConnectionWarning.HideWarning()
        ReturnValue: bool = mLocalGenerator.HasPower()
        ReturnValue_0: bool = mLocalGenerator.IsProductionPaused()
        ReturnValue_1: bool = Not_PreBool(ReturnValue)
        ReturnValue_2: bool = BooleanOR(ReturnValue_0, ReturnValue_1)
        if not ReturnValue_2:
            goto('L1375')
        self.mConnectionWarning.UpdateWarning("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 363, 'Value': 'NO POWER'}")
        # Label 410
        ReturnValue_3: bool = Default__KismetSystemLibrary.IsValid(self.mWasteSlot)
        if not ReturnValue_3:
            goto('L657')
        ReturnValue_4: InventoryItem = Default__FGInventoryLibrary.MakeInventoryItem(Desc_NuclearWaste)
        
        ReturnValue_5: bool = self.mWasteSlot.mCachedInventoryComponent.HasEnoughSpaceForItem(Ref[ReturnValue_4])
        if not ReturnValue_5:
            goto('L1416')
        self.mFuelWarning.HideWarning()
        
        slotHasItems = None
        # Label 657
        self.InputSlot.CheckSlotHasItems(Ref[slotHasItems])
        if not slotHasItems:
            goto('L1515')
        self.mFuelWarning.HideWarning()
        
        ItemClass = None
        self.InputSlot.GetItemClass(Ref[ItemClass])
        ReturnValue_6: FText = Default__FGItemDescriptor.GetItemName(ItemClass)
        self.Widget_Output_Slot.mRecipeName.SetText(ReturnValue_6)
        # Label 923
        ReturnValue_7: bool = Default__KismetSystemLibrary.IsValidClass(self.mFluidClass)
        if not ReturnValue_7:
            goto('L1667')
        Variable: uint8 = 3
        ReturnValue_8: Ptr[FGInventoryComponent] = self.mFuelGenerator.GetFuelInventory()
        
        numItems = None
        Default__HUDHelpers.GetNumItemsFromInventory(ReturnValue_8, self.mFluidClass, self, Ref[numItems])
        ReturnValue_9: bool = numItems > 0
        Variable1: uint8 = 2
        Variable_0: bool = ReturnValue_9
        
        switch = {
            False: Variable,
            True: Variable1
        }
        self.mWaterWarning.SetVisibility(switch.get(Variable_0, None))
        # End
        # Label 1281
        self.mConnectionWarning.UpdateWarning("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 1318, 'Value': 'NO CONNECTION'}")
        # End
        # Label 1375
        self.mConnectionWarning.HideWarning()
        goto('L410')
        # Label 1416
        self.mFuelWarning.UpdateWarning("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 1453, 'Value': 'WASTE SLOT IS FULL'}")
        # End
        # Label 1515
        self.mFuelWarning.UpdateWarning("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 1552, 'Value': 'INSERT FUEL'}")
        self.Widget_Output_Slot.mRecipeName.SetText()
        goto('L923')
        # Label 1667
        self.mWaterWarning.SetVisibility(0)
    

    def DropInventorySlotStack(self):
        ExecutionFlow.Push("L854")
        
        Result = None
        self.InputSlot.DropOntoInventorySlot(InventorySlot, Ref[Result])
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
        # Label 527
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
    

    def UpdateSlotStats(self):
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(self.mFuelGenerator)
        if not ReturnValue:
            goto('L2709')
        self.UpdateFluidStats()
        ReturnValue_0: float = self.GetBurnProgressPercent()
        ReturnValue_1: bool = ReturnValue_0 > 0
        ReturnValue1: TSubclassOf[FGItemDescriptor] = self.mFuelGenerator.GetCurrentFuelClass()
        ReturnValue_2: bool = Default__KismetSystemLibrary.IsValidClass(ReturnValue1)
        ReturnValue_3: bool = ReturnValue_2 and ReturnValue_1
        if not ReturnValue_3:
            goto('L2008')
        self.Widget_Output_Slot.mProgressBar.SetShowIcon(True)
        ReturnValue_4: TSubclassOf[FGItemDescriptor] = self.mFuelGenerator.GetCurrentFuelClass()
        ReturnValue_5: Ptr[Texture2D] = Default__FGItemDescriptor.GetSmallIcon(ReturnValue_4)
        self.Widget_Output_Slot.mProgressBar.SetIcon(ReturnValue_5)
        
        slotHasItems = None
        # Label 509
        self.InputSlot.CheckSlotHasItems(Ref[slotHasItems])
        if not slotHasItems:
            goto('L2709')
        ReturnValue_6: float = self.mFuelGenerator.GetPowerProductionCapacity()
        # Label 618
        self.Widget_Output_Slot.mPowerConsumption.mManufacturingStat = ReturnValue_6
        if not self.mIsFluidGenerator:
            goto('L2072')
        ReturnValue_6 = self.mFuelGenerator.GetPowerProductionCapacity()
        
        ItemClass = None
        self.InputSlot.GetItemClass(Ref[ItemClass])
        ReturnValue_7: float = Default__FGItemDescriptor.GetEnergyValue(ItemClass)
        ReturnValue_8: float = ReturnValue_7 / ReturnValue_6
        ReturnValue1_0: float = 60 / ReturnValue_8
        ReturnValue2: float = ReturnValue1_0 / 1000
        self.Widget_Output_Slot.mCycleTime.mManufacturingStat = ReturnValue2
        self.Widget_Output_Slot.mCycleTime.mCustomSuffix = STRING_TABLE_ENTRY("StringTable /Game/FactoryGame/Interface/UI/ST_Units.ST_Units", "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 1180, 'Value': 'm3PerMin'}"
        # Label 1190
        ReturnValue_9: float = self.mFuelGenerator.GetLoadPercentage()
        self.Widget_Output_Slot.mEfficiency.mManufacturingStat = ReturnValue_9
        ReturnValue_10: bool = self.mFuelGenerator.IsProductionPaused()
        ReturnValue_11: float = self.mFuelGenerator.GetCurrentPotential()
        ReturnValue_9 = self.mFuelGenerator.GetLoadPercentage()
        ReturnValue_12: float = ReturnValue_9 * ReturnValue_11
        Variable: bool = ReturnValue_10
        Variable_0: float = 0
        
        switch = {
            False: ReturnValue_12,
            True: Variable_0
        }
        ReturnValue_13: bool = NotEqual_FloatFloat(self.PreviousEffiency, switch.get(Variable, None))
        if not ReturnValue_13:
            goto('L2709')
        ReturnValue_10 = self.mFuelGenerator.IsProductionPaused()
        ReturnValue_11 = self.mFuelGenerator.GetCurrentPotential()
        ReturnValue_9 = self.mFuelGenerator.GetLoadPercentage()
        ReturnValue_12 = ReturnValue_9 * ReturnValue_11
        Variable = ReturnValue_10
        Variable_0 = 0
        
        switch_0 = {
            False: ReturnValue_12,
            True: Variable_0
        }
        self.PreviousEffiency = switch_0.get(Variable, None)
        ReturnValue1_1: bool = Default__KismetSystemLibrary.IsValid(self.mNuclearGenerator)
        if not ReturnValue1_1:
            goto('L2348')
        # End
        # Label 2008
        self.Widget_Output_Slot.mProgressBar.SetShowIcon(False)
        goto('L509')
        # Label 2072
        ReturnValue_6 = self.mFuelGenerator.GetPowerProductionCapacity()
        
        ItemClass = None
        self.InputSlot.GetItemClass(Ref[ItemClass])
        ReturnValue_7 = Default__FGItemDescriptor.GetEnergyValue(ItemClass)
        ReturnValue_8 = ReturnValue_7 / ReturnValue_6
        self.Widget_Output_Slot.mCycleTime.mManufacturingStat = ReturnValue_8
        goto('L1190')
        # Label 2348
        ReturnValue_10 = self.mFuelGenerator.IsProductionPaused()
        ReturnValue_11 = self.mFuelGenerator.GetCurrentPotential()
        ReturnValue_9 = self.mFuelGenerator.GetLoadPercentage()
        ReturnValue_12 = ReturnValue_9 * ReturnValue_11
        Variable = ReturnValue_10
        Variable_0 = 0
        
        switch_1 = {
            False: ReturnValue_12,
            True: Variable_0
        }
        ReturnValue3: float = switch_1.get(Variable, None) / 2.5
        self.mModuleFuel_Meter.SetValue(ReturnValue3)
    

    def GetFuseVisibility(self):
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(self.mPowerCircuitGraph)
        if not ReturnValue:
            goto('L295')
        ReturnValue_0: Ptr[FGPowerCircuit] = self.mPowerCircuitGraph.GetPowerCircuit()
        ReturnValue1: bool = Default__KismetSystemLibrary.IsValid(ReturnValue_0)
        if not ReturnValue1:
            goto('L295')
        ReturnValue_0 = self.mPowerCircuitGraph.GetPowerCircuit()
        ReturnValue_1: bool = ReturnValue_0.IsFuseTriggered()
        if not ReturnValue_1:
            goto('L295')
        ReturnValue_2: uint8 = 4
        goto('L315')
        # Label 295
        ReturnValue_2 = 1
    

    def UpdateSlotInfo(self):
        ReturnValue: float = self.GetBurnProgressPercent()
        self.Widget_Output_Slot.mProgressBar.mProgressBar.SetPercent(ReturnValue)
        
        Text = None
        Graphics = None
        Default__HUDHelpers.GetFactoryGameDarkGray(self, Ref[Text], Ref[Graphics])
        self.Widget_Output_Slot.mProgressBar.mProgressBar.SetFillColorAndOpacity(Graphics)
    

    def OnGetPowerCircuit(self):
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(self.mFuelGenerator)
        if not ReturnValue:
            goto('L280')
        ReturnValue_0: Ptr[FGPowerInfoComponent] = self.mFuelGenerator.GetPowerInfo()
        ReturnValue1: bool = Default__KismetSystemLibrary.IsValid(ReturnValue_0)
        if not ReturnValue1:
            goto('L280')
        ReturnValue_0 = self.mFuelGenerator.GetPowerInfo()
        ReturnValue_1: Ptr[FGPowerCircuit] = ReturnValue_0.GetPowerCircuit()
        ReturnValue_2: Ptr[FGPowerCircuit] = ReturnValue_1
        goto('L291')
        # Label 280
        ReturnValue_2 = None
    

    def IsConnected(self):
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(self.mFuelGenerator)
        if not ReturnValue:
            goto('L173')
        ReturnValue_0: Ptr[FGPowerInfoComponent] = self.mFuelGenerator.GetPowerInfo()
        ReturnValue_1: bool = ReturnValue_0.IsConnected()
        IsConnected = ReturnValue_1
        # End
        # Label 173
        IsConnected = False
    

    def Cleanup(self):
        ExecutionFlow.Push("L665")
        self.Widget_Window_DarkMode.OnClose.Clear()
        
        Default__KismetSystemLibrary.K2_ClearAndInvalidateTimerHandle(self, Ref[self.UpdateSlotStatsTimer])
        
        Default__KismetSystemLibrary.K2_ClearAndInvalidateTimerHandle(self, Ref[self.SmokeTimer])
        
        Default__KismetSystemLibrary.K2_ClearAndInvalidateTimerHandle(self, Ref[self.mWarningMessageTimerHandle])
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(self.InputSlot)
        if not ReturnValue:
            goto('L260')
        self.InputSlot.OnMoveStack.Clear()
        
        Slots = None
        # Label 260
        self.Widget_Overclock.GetUnlockedOverclockSlots(Ref[Slots])
        Variable: int32 = 0
        Variable_0: int32 = 0
        
        Slots = None
        # Label 351
        ReturnValue_0: int32 = len(Slots)
        # Label 410
        ReturnValue_1: bool = Variable <= ReturnValue_0
        if not ReturnValue_1:
            goto('L586')
        Variable_0 = Variable
        ExecutionFlow.Push("L591")
        
        Slots = None
        Item = None
        Item = Slots[Variable_0]
        Item.OnMoveStack.Clear()
        goto(ExecutionFlow.Pop())
        # Label 586
        # End
        # Label 591
        ReturnValue_2: int32 = Variable + 1
        Variable = ReturnValue_2
        goto('L351')
    

    def GetBurnProgressPercent(self):
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(self.mFuelGenerator)
        if not ReturnValue:
            goto('L142')
        ReturnValue_0: float = self.mFuelGenerator.GetFuelAmount()
        ReturnValue_1: float = ReturnValue_0
    

    def Init(self):
        self.ExecuteUbergraph_Widget_Generator(955)
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_Generator(2280)
    

    def Destruct(self):
        self.ExecuteUbergraph_Widget_Generator(2389)
    

    def BndEvt__Widget_StandbyButton_K2Node_ComponentBoundEvent_1_OnStandbyClicked__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_Generator(2777)
    

    def ResetFuse(self):
        self.ExecuteUbergraph_Widget_Generator(3393)
    

    def WarningMessageCheck(self):
        self.ExecuteUbergraph_Widget_Generator(3398)
    

    def SpawnSmoke(self):
        self.ExecuteUbergraph_Widget_Generator(3477)
    

    def OnProductionChanged(self, State: bool):
        ExecuteUbergraph_Widget_Generator.K2Node_CustomEvent_state = State #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_Generator(3614)
    

    def OnCustomTick(self):
        ExecuteUbergraph_Widget_Generator.K2Node_Event_UpdateTime = UpdateTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_Generator(4029)
    

    def ExecuteUbergraph_Widget_Generator(self):
        goto(ComputedJump("EntryPoint"))
        # Label 15
        Fuel: Ptr[FGBuildableGeneratorFuel] = Cast[FGBuildableGeneratorFuel](self.mGenerator)
        bSuccess: bool = Fuel
        if not bSuccess:
            goto('L192')
        Nuclear: Ptr[FGBuildableGeneratorNuclear] = Cast[FGBuildableGeneratorNuclear](Fuel)
        bSuccess1: bool = Nuclear
        if not bSuccess1:
            goto('L192')
        # Label 173
        self.mNuclearGenerator = Nuclear
        # Label 192
        self.UpdateHeaderText()
        OutputDelegate4.BindUFunction(self, OnProductionChanged)
        self.mGenerator.mOnHasProductionChanged.AddUnique(OutputDelegate4)
        OutputDelegate.BindUFunction(self, OnEscapePressed)
        self.Widget_Window_DarkMode.OnClose.AddUnique(OutputDelegate)
        OutputDelegate1.BindUFunction(self, ResetFuse)
        self.Widget_Fusebox.ResetFuse.AddUnique(OutputDelegate1)
        ReturnValue1: bool = Default__KismetSystemLibrary.IsValid(self.InputSlot)
        if not ReturnValue1:
            goto('L527')
        OutputDelegate8.BindUFunction(self, OnInventorySlotStackMove)
        self.InputSlot.OnMoveStack.AddUnique(OutputDelegate8)
        
        Slots = None
        # Label 527
        self.Widget_Overclock.GetUnlockedOverclockSlots(Ref[Slots])
        Variable: int32 = 0
        Variable_0: int32 = 0
        
        Slots = None
        # Label 618
        ReturnValue: int32 = len(Slots)
        ReturnValue_0: bool = Variable <= ReturnValue
        if not ReturnValue_0:
           goto(ExecutionFlow.Pop())
        Variable_0 = Variable
        ExecutionFlow.Push("L881")
        
        Slots = None
        Item = None
        Item = Slots[Variable_0]
        OutputDelegate7.BindUFunction(self, OnInventorySlotStackMove)
        Item.OnMoveStack.AddUnique(OutputDelegate7)
        goto(ExecutionFlow.Pop())
        # Label 881
        ReturnValue_1: int32 = Variable + 1
        # Label 923
        Variable = ReturnValue_1
        goto('L618')
        self.Init()
        Fuel1: Ptr[FGBuildableGeneratorFuel] = Cast[FGBuildableGeneratorFuel](self.mInteractObject)
        bSuccess2: bool = Fuel1
        if not bSuccess2:
           goto(ExecutionFlow.Pop())
        self.mFuelGenerator = Fuel1
        ReturnValue_2: bool = self.mFuelGenerator.HasAuthority()
        if not ReturnValue_2:
            goto('L2211')
        # Label 1115
        Fuel_0: Ptr[Build_GeneratorFuel] = Cast[Build_GeneratorFuel](self.mFuelGenerator)
        bSuccess6: bool = Fuel_0
        self.mIsFluidGenerator = bSuccess6
        self.Widget_Overclock.mBuildableFactory = self.mFuelGenerator
        ReturnValue1_0: bool = self.mFuelGenerator.IsProductionPaused()
        self.Widget_StandbyButton.SetStandbyButtonBrush(ReturnValue1_0)
        self.SetupInputs()
        OutputDelegate2.BindUFunction(self, WarningMessageCheck)
        ReturnValue_3: TimerHandle = Default__KismetSystemLibrary.K2_SetTimerDelegate(OutputDelegate2, 0.30000001192092896, True)
        self.mWarningMessageTimerHandle = ReturnValue_3
        self.InitModule()
        
        self.Widget_InventorySlot_DropArea.mInventorySlots = None
        ReturnValue_4: int32 = self.Widget_InventorySlot_DropArea.mInventorySlots.append(self.InputSlot)
        self.UpdateSlotStats()
        OutputDelegate6.BindUFunction(self, UpdateSlotStats)
        ReturnValue2: TimerHandle = Default__KismetSystemLibrary.K2_SetTimerDelegate(OutputDelegate6, 0.05000000074505806, True)
        self.UpdateSlotStatsTimer = ReturnValue2
        ReturnValue_5: bool = self.mFuelGenerator.GetRequiresSupplementalResource()
        if not ReturnValue_5:
            goto('L1870')
        self.mFluidModuleContainer.SetVisibility(4)
        ReturnValue_6: TSubclassOf[FGItemDescriptor] = self.mFuelGenerator.GetSupplementalResourceClass()
        self.BPW_FluidModule.SetFluidType(ReturnValue_6)
        # Label 1870
        ReturnValue_7: List[TSubclassOf[FGItemDescriptor]] = self.mFuelGenerator.GetAvailableFuelClasses()
        self.mRelevantItems = ReturnValue_7
        ReturnValue3: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_8: Ptr[FGUnlockSubsystem] = Default__FGUnlockSubsystem.Get(ReturnValue3)
        ReturnValue_9: bool = ReturnValue_8.GetIsBuildingOverclockUnlocked()
        if not ReturnValue_9:
            goto('L2165')
        Variable_1: Const[TSubclassOf[FGItemDescriptor]] = Desc_CrystalShard
        
        ReturnValue1_1: int32 = self.mRelevantItems.append(Variable_1)
        
        # Label 2165
        self.Widget_Window_DarkMode.SetupRelevantInventory(Ref[self.mRelevantItems])
        goto(ExecutionFlow.Pop())
        # Label 2211
        OutputDelegate5.BindUFunction(self, OnReplicationDetailActorCreated)
        self.mFuelGenerator.OnReplicationDetailActorCreatedEvent.AddUnique(OutputDelegate5)
        goto('L1115')
        self.Construct()
        Generator: Ptr[FGBuildableGenerator] = Cast[FGBuildableGenerator](self.mInteractObject)
        bSuccess5: bool = Generator
        if not bSuccess5:
           goto(ExecutionFlow.Pop())
        self.mGenerator = Generator
        goto('L15')
        self.Destruct()
        self.Cleanup()
        goto(ExecutionFlow.Pop())
        # Label 2414
        ReturnValue_10: Ptr[PlayerController] = self.GetOwningPlayer()
        Controller: Ptr[BP_PlayerController] = Cast[BP_PlayerController](ReturnValue_10)
        bSuccess3: bool = Controller
        if not bSuccess3:
           goto(ExecutionFlow.Pop())
        ReturnValue_11: Ptr[BP_RemoteCallObject] = Controller.GetRemoteCallObjectOfClass(BP_RemoteCallObject)
        ReturnValue_12: bool = self.mFuelGenerator.IsProductionPaused()
        ReturnValue_13: bool = Not_PreBool(ReturnValue_12)
        ReturnValue_11.Server_SetIsProductionPausedOnFactory(self.mFuelGenerator, ReturnValue_13)
        ReturnValue_12 = self.mFuelGenerator.IsProductionPaused()
        self.Widget_StandbyButton.SetStandbyButtonBrush(ReturnValue_12)
        goto(ExecutionFlow.Pop())
        goto('L2414')
        # Label 2782
        ReturnValue1_2: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_14: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_UI_PowerLossWarning_ResetFuse, ReturnValue1_2, True)
        goto(ExecutionFlow.Pop())
        # Label 2868
        ReturnValue1_2 = self.GetOwningPlayer()
        Controller_0: Ptr[FGPlayerController] = Cast[FGPlayerController](ReturnValue1_2)
        bSuccess4: bool = Controller_0
        if not bSuccess4:
           goto(ExecutionFlow.Pop())
        ReturnValue1_3: Ptr[BP_RemoteCallObject] = Controller_0.GetRemoteCallObjectOfClass(BP_RemoteCallObject)
        ReturnValue_15: Ptr[FGPowerCircuit] = self.mPowerCircuitGraph.GetPowerCircuit()
        ReturnValue_16: int32 = ReturnValue_15.GetCircuitID()
        ReturnValue1_3.Server_ResetFuse(ReturnValue_16)
        goto('L2782')
        # Label 3160
        Variable_2: bool = False
        if not Variable1:
            goto('L3186')
        goto(ExecutionFlow.Pop())
        # Label 3186
        Variable1: bool = True
        
        Default__KismetSystemLibrary.K2_ClearAndInvalidateTimerHandle(self, Ref[self.SmokeTimer])
        goto(ExecutionFlow.Pop())
        # Label 3240
        if not Variable_2:
            goto('L3255')
        goto(ExecutionFlow.Pop())
        # Label 3255
        Variable_2 = True
        Variable1 = False
        OutputDelegate3.BindUFunction(self, SpawnSmoke)
        ReturnValue1_4: TimerHandle = Default__KismetSystemLibrary.K2_SetTimerDelegate(OutputDelegate3, 1, True)
        self.SmokeTimer = ReturnValue1_4
        goto(ExecutionFlow.Pop())
        goto('L2868')
        self.UpdateWarningWidget()
        ReturnValue_17: bool = self.mGenerator.IsProducing()
        if not ReturnValue_17:
            goto('L3160')
        goto('L3240')
        ReturnValue2_0: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_18: Ptr[Widget_Smoke] = Default__WidgetBlueprintLibrary.Create(self, Widget_Smoke, ReturnValue2_0)
        ReturnValue_19: Ptr[PanelSlot] = self.mSmokeContainers.AddChild(ReturnValue_18)
        goto(ExecutionFlow.Pop())
        ReturnValue_20: bool = Default__KismetSystemLibrary.IsValid(self.mNuclearGenerator)
        ReturnValue1_5: bool = self.mGenerator.IsProducing()
        ReturnValue_21: bool = self.IsAnimationPlaying(self.NuclearGlow)
        ReturnValue_22: bool = ReturnValue_20 and ReturnValue1_5
        ReturnValue1_6: bool = Not_PreBool(ReturnValue_21)
        ReturnValue1_7: bool = ReturnValue_22 and ReturnValue1_6
        if not ReturnValue1_7:
            goto('L3906')
        ReturnValue_23: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.NuclearGlow, 0, 0, 0, 1)
        goto(ExecutionFlow.Pop())
        # Label 3906
        ReturnValue1_8: bool = self.IsAnimationPlaying(self.NuclearGlow)
        if not ReturnValue1_8:
           goto(ExecutionFlow.Pop())
        ReturnValue_24: float = self.PauseAnimation(self.NuclearGlow)
        ReturnValue1_9: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.NuclearGlowStop, 0, 1, 0, 1)
        goto(ExecutionFlow.Pop())
        self.UpdateSlotInfo()
        goto(ExecutionFlow.Pop())
    
