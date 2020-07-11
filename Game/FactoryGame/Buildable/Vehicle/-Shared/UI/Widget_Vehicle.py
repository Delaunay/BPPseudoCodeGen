
from codegen.ue4_stub import *

from Script.FactoryGame import FGHealthComponent
from Script.FactoryGame import GetHealthComponent
from Script.Engine import NotEqual_BoolBool
from Script.Engine import Delay
from Script.FactoryGame import FGPlayerController
from Script.Engine import K2_SetTimerDelegate
from Script.Engine import FClamp
from Script.Engine import Pawn
from Script.Engine import Conv_IntToFloat
from Script.Engine import LatentActionInfo
from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import PlayerController
from Game.FactoryGame.Buildable.Vehicle.-Shared.UI.Widget_Vehicle import ExecuteUbergraph_Widget_Vehicle
from Script.Engine import Default__KismetArrayLibrary
from Script.UMG import PlayAnimation
from Script.UMG import ESlateVisibility
from Script.Engine import Conv_FloatToText
from Script.Engine import TimerHandle
from Script.UMG import StopAnimation
from Script.FactoryGame import FGInventoryComponent
from Script.UMG import SetPercent
from Script.Engine import IsValid
from Game.FactoryGame.Buildable.Vehicle.-Shared.UI.Widget_Vehicle import ExecuteUbergraph_Widget_Vehicle.K2Node_Event_InDeltaTime
from Script.Engine import Conv_IntToText
from Script.PhysXVehicles import GetCurrentGear
from Script.Engine import EqualEqual_IntInt
from Script.Engine import Default__KismetTextLibrary
from Script.Engine import Conv_StringToText
from Script.FactoryGame import GetIsUsingGamepad
from Script.Engine import BooleanOR
from Script.UMG import IsVisible
from Script.PhysXVehicles import GetEngineRotationSpeed
from Script.UMG import Construct
from Script.UMG import SetRenderAngle
from Script.Engine import SelectString
from Game.FactoryGame.Buildable.Vehicle.BP_WheeledVehicle import BP_WheeledVehicle
from Script.UMG import WidgetAnimation
from Script.Engine import Default__KismetStringLibrary
from Script.PhysXVehicles import WheeledVehicleMovementComponent
from Script.Engine import Abs_Int
from Script.FactoryGame import GetCurrentHealth
from Script.UMG import UserWidget
from Script.FactoryGame import GetInventoryStacks
from Script.UMG import GetOwningPlayerPawn
from Script.UMG import UMGSequencePlayer
from Game.FactoryGame.Buildable.Vehicle.-Shared.UI.Widget_Vehicle import ExecuteUbergraph_Widget_Vehicle.K2Node_Event_MyGeometry
from Script.Engine import Abs
from Script.FactoryGame import GetSizeLinear
from Script.FactoryGame import GetFuelInventory
from Script.FactoryGame import GetMaxHealth
from Script.FactoryGame import GetStorageInventory
from Script.FactoryGame import GetForwardSpeed
from Script.Engine import Concat_StrStr
from Script.FactoryGame import GetVehicleMovementComponent
from Script.FactoryGame import InventoryStack

class Widget_Vehicle(UserWidget):
    StopAnim: Ptr[WidgetAnimation]
    StartRecordHUDBox: Ptr[WidgetAnimation]
    HealthLow: Ptr[WidgetAnimation]
    FuelWarning: Ptr[WidgetAnimation]
    StopRecordingAnim: Ptr[WidgetAnimation]
    StartRecordingAnim: Ptr[WidgetAnimation]
    AutoPilotTimer: TimerHandle
    BPVehicle: Ptr[BP_WheeledVehicle]
    VehicleInventory: Ptr[FGInventoryComponent]
    
    def OnItemAddedOrRemoved(self, ItemClass: TSubclassOf[FGItemDescriptor], NumAddedRemoved: int32):
        self.UpdateTransferStatus()
    

    def UpdateTransferStatus(self):
        ExecutionFlow.Push("L1026")
        ExecutionFlow.Push("L355")
        stacks: List[InventoryStack] = []
        
        self.VehicleInventory.GetInventoryStacks(Ref[stacks])
        
        ReturnValue: int32 = len(stacks)
        ReturnValue_0: float = Conv_IntToFloat(ReturnValue)
        ReturnValue_1: int32 = self.VehicleInventory.GetSizeLinear()
        ReturnValue1: float = Conv_IntToFloat(ReturnValue_1)
        ReturnValue_2: float = ReturnValue_0 / ReturnValue1
        self.mProgressBarLoadingUnloading.mProgressBar.SetPercent(ReturnValue_2)
        goto(ExecutionFlow.Pop())
        # Label 355
        ReturnValue_3: bool = self.mTruckStationLoadingStatus.IsVisible()
        ReturnValue_4: bool = BooleanOR(self.BPVehicle.mIsUnloadingVehicle, self.BPVehicle.mIsLoadingVehicle)
        ReturnValue_5: bool = NotEqual_BoolBool(ReturnValue_3, ReturnValue_4)
        if not ReturnValue_5:
           goto(ExecutionFlow.Pop())
        Variable: uint8 = 0
        Variable1: uint8 = 2
        ReturnValue_4 = BooleanOR(self.BPVehicle.mIsUnloadingVehicle, self.BPVehicle.mIsLoadingVehicle)
        Variable_0: bool = ReturnValue_4
        
        switch = {
            False: Variable1,
            True: Variable
        }
        self.mTruckStationLoadingStatus.SetVisibility(switch.get(Variable_0, None))
        Variable_1: FText = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 777, 'Value': 'Loading...'}"
        Variable1_0: FText = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 845, 'Value': 'Unloading...'}"
        Variable1_1: bool = self.BPVehicle.mIsLoadingVehicle
        
        switch_0 = {
            False: Variable1_0,
            True: Variable_1
        }
        self.mTransferStatusText.SetText(switch_0.get(Variable1_1, None))
        goto(ExecutionFlow.Pop())
    

    def GetSelfDrivingText(self):
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        Controller: Ptr[FGPlayerController] = Cast[FGPlayerController](ReturnValue)
        bSuccess: bool = Controller
        ReturnValue_0: bool = Controller.GetIsUsingGamepad()
        ReturnValue_1: FString = SelectString("LB", "C", ReturnValue_0)
        ReturnValue_2: FString = Default__KismetStringLibrary.Concat_StrStr("Press [", ReturnValue_1)
        ReturnValue1: FString = Default__KismetStringLibrary.Concat_StrStr(ReturnValue_2, "] to open Self Driving Menu")
        ReturnValue_3: FText = Default__KismetTextLibrary.Conv_StringToText(ReturnValue1)
        ReturnValue_4: FText = ReturnValue_3
    

    def GetVehicleHealthPercent(self):
        ReturnValue: Ptr[Pawn] = self.GetOwningPlayerPawn()
        Vehicle: Ptr[BP_WheeledVehicle] = Cast[BP_WheeledVehicle](ReturnValue)
        bSuccess: bool = Vehicle
        if not bSuccess:
            goto('L314')
        ReturnValue_0: Ptr[FGHealthComponent] = Vehicle.GetHealthComponent()
        ReturnValue_1: float = ReturnValue_0.GetCurrentHealth()
        ReturnValue_2: float = ReturnValue_0.GetMaxHealth()
        ReturnValue_3: float = ReturnValue_1 / ReturnValue_2
        ReturnValue_4: float = ReturnValue_3
    

    def GetCurrentSpeedVisibility(self):
        ReturnValue: Ptr[Pawn] = self.GetOwningPlayerPawn()
        Vehicle: Ptr[BP_WheeledVehicle] = Cast[BP_WheeledVehicle](ReturnValue)
        bSuccess: bool = Vehicle
        if not bSuccess:
            goto('L285')
        Variable: uint8 = 0
        Variable1: uint8 = 2
        ReturnValue_0: bool = Vehicle.mSpeedInKMH > 0
        Variable_0: bool = ReturnValue_0
        
        switch = {
            False: Variable1,
            True: Variable
        }
        ReturnValue_1: uint8 = switch.get(Variable_0, None)
    

    def GetCurrentGearText(self):
        ReturnValue: Ptr[Pawn] = self.GetOwningPlayerPawn()
        Vehicle: Ptr[BP_WheeledVehicle] = Cast[BP_WheeledVehicle](ReturnValue)
        bSuccess: bool = Vehicle
        if not bSuccess:
            goto('L798')
        ReturnValue_0: Ptr[WheeledVehicleMovementComponent] = Vehicle.GetVehicleMovementComponent()
        ReturnValue_1: int32 = ReturnValue_0.GetCurrentGear()
        ReturnValue_2: bool = ReturnValue_1 > 0
        if not ReturnValue_2:
            goto('L434')
        ReturnValue_0 = Vehicle.GetVehicleMovementComponent()
        # Label 281
        ReturnValue_1 = ReturnValue_0.GetCurrentGear()
        ReturnValue_3: FText = Default__KismetTextLibrary.Conv_IntToText(ReturnValue_1, False, True, 1, 324)
        ReturnValue_4: FText = ReturnValue_3
        goto('L798')
        # Label 434
        ReturnValue_0 = Vehicle.GetVehicleMovementComponent()
        ReturnValue_1 = ReturnValue_0.GetCurrentGear()
        ReturnValue_5: bool = ReturnValue_1 <= -1
        if not ReturnValue_5:
            goto('L638')
        ReturnValue_4 = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 594, 'Value': 'R'}"
        goto('L798')
        # Label 638
        ReturnValue_0 = Vehicle.GetVehicleMovementComponent()
        ReturnValue_1 = ReturnValue_0.GetCurrentGear()
        ReturnValue_6: bool = EqualEqual_IntInt(ReturnValue_1, 0)
        if not ReturnValue_6:
            goto('L798')
        ReturnValue_4 = 
    

    def GetCurrentSpeedinKMHText(self):
        ReturnValue: Ptr[Pawn] = self.GetOwningPlayerPawn()
        Vehicle: Ptr[BP_WheeledVehicle] = Cast[BP_WheeledVehicle](ReturnValue)
        bSuccess: bool = Vehicle
        if not bSuccess:
            goto('L261')
        ReturnValue_0: int32 = Abs_Int(Vehicle.mSpeedInKMH)
        ReturnValue_1: FText = Default__KismetTextLibrary.Conv_IntToText(ReturnValue_0, False, True, 1, 324)
        ReturnValue_2: FText = ReturnValue_1
        goto('L281')
        # Label 261
        ReturnValue_2 = 
    

    def GetRPMText(self):
        ReturnValue: Ptr[Pawn] = self.GetOwningPlayerPawn()
        Vehicle: Ptr[BP_WheeledVehicle] = Cast[BP_WheeledVehicle](ReturnValue)
        bSuccess: bool = Vehicle
        if not bSuccess:
            goto('L306')
        ReturnValue_0: Ptr[WheeledVehicleMovementComponent] = Vehicle.GetVehicleMovementComponent()
        ReturnValue_1: float = ReturnValue_0.GetEngineRotationSpeed()
        ReturnValue_2: FText = Default__KismetTextLibrary.Conv_FloatToText(ReturnValue_1, 0, False, True, 1, 324, 0, 3)
        ReturnValue_3: FText = ReturnValue_2
        goto('L326')
        # Label 306
        ReturnValue_3 = 
    

    def Init(self, Vehicle: Ptr[BP_WheeledVehicle]):
        ReturnValue: Ptr[FGInventoryComponent] = Vehicle.GetFuelInventory()
        self.mFuelInventorySlot.mCachedInventoryComponent = ReturnValue
        if not Vehicle.mIsRecording:
            goto('L133')
        self.StartRecording()
    

    def StopRecording(self):
        self.StopAnimation(self.StartRecordHUDBox)
        ReturnValue1: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.StopRecordingAnim, 0, 1, 0, 1)
        self.Recording.SetVisibility(2)
        self.mRecordText.SetText("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 140, 'Value': 'Not Recording'}")
        self.RecordIcon.SetVisibility(2)
        self.StopIcon.SetVisibility(0)
        ReturnValue: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.StopAnim, 0, 0, 0, 1)
    

    def StartRecording(self):
        self.Recording.SetVisibility(0)
        ReturnValue: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.StartRecordHUDBox, 0, 0, 0, 1)
        self.RecordIcon.SetVisibility(0)
        self.StopIcon.SetVisibility(2)
        self.mRecordText.SetText("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 197, 'Value': 'Recording...'}")
        self.StopAnimation(self.StopAnim)
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_Vehicle(1382)
    

    def Tick(self):
        ExecuteUbergraph_Widget_Vehicle.K2Node_Event_MyGeometry = MyGeometry #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_Vehicle.K2Node_Event_InDeltaTime = InDeltaTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_Vehicle(809)
    

    def AutoPilotCheck(self):
        self.ExecuteUbergraph_Widget_Vehicle(1172)
    

    def ExecuteUbergraph_Widget_Vehicle(self):
        goto(ComputedJump("EntryPoint"))
        # Label 15
        self.UpdateTransferStatus()
        self.Init(self.BPVehicle)
        ReturnValue: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.StopAnim, 0, 0, 0, 1)
        self.AutoPilotCheck()
        OutputDelegate2.BindUFunction(self, AutoPilotCheck)
        ReturnValue_0: TimerHandle = Default__KismetSystemLibrary.K2_SetTimerDelegate(OutputDelegate2, 0.5, True)
        self.AutoPilotTimer = ReturnValue_0
        goto(ExecutionFlow.Pop())
        # Label 228
        ReturnValue_1: Ptr[Pawn] = self.GetOwningPlayerPawn()
        Vehicle: Ptr[BP_WheeledVehicle] = Cast[BP_WheeledVehicle](ReturnValue_1)
        bSuccess: bool = Vehicle
        if not bSuccess:
            goto('L732')
        self.BPVehicle = Vehicle
        OutputDelegate.BindUFunction(self, StartRecording)
        self.BPVehicle.OnStartRecording.AddUnique(OutputDelegate)
        OutputDelegate1.BindUFunction(self, StopRecording)
        self.BPVehicle.OnStopRecording.AddUnique(OutputDelegate1)
        OutputDelegate3.BindUFunction(self, UpdateTransferStatus)
        self.BPVehicle.TranferStatusChangedDelegate.AddUnique(OutputDelegate3)
        ReturnValue_2: Ptr[FGInventoryComponent] = self.BPVehicle.GetStorageInventory()
        self.VehicleInventory = ReturnValue_2
        OutputDelegate4.BindUFunction(self, OnItemAddedOrRemoved)
        self.VehicleInventory.OnItemAddedDelegate.AddUnique(OutputDelegate4)
        OutputDelegate4.BindUFunction(self, OnItemAddedOrRemoved)
        self.VehicleInventory.OnItemRemovedDelegate.AddUnique(OutputDelegate4)
        goto('L15')
        # Label 732
        Default__KismetSystemLibrary.Delay(self, 0.20000000298023224, LatentActionInfo(Linkage = 228, UUID = 1878698236, ExecutionFunction = "ExecuteUbergraph_Widget_Vehicle", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        ReturnValue_3: bool = Default__KismetSystemLibrary.IsValid(self.BPVehicle)
        if not ReturnValue_3:
           goto(ExecutionFlow.Pop())
        ReturnValue_4: float = self.BPVehicle.GetForwardSpeed()
        ReturnValue_5: float = Abs(ReturnValue_4)
        ReturnValue_6: float = ReturnValue_5 / 28
        ReturnValue_7: float = ReturnValue_6 * 0.6000000238418579
        ReturnValue_8: float = ReturnValue_7 - 45
        ReturnValue_9: float = FClamp(ReturnValue_8, -45, 45)
        self.PointerContainer.SetRenderAngle(ReturnValue_9)
        goto(ExecutionFlow.Pop())
        if not self.BPVehicle.mIsAutoPilotEnabled:
            goto('L1288')
        self.AutoPilotText.SetText("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 1245, 'Value': 'Yes'}")
        goto(ExecutionFlow.Pop())
        # Label 1288
        self.AutoPilotText.SetText("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 1325, 'Value': 'No'}")
        goto(ExecutionFlow.Pop())
        # Label 1367
        self.Construct()
        goto('L228')
        goto('L1367')
    
