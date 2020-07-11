
from codegen.ue4_stub import *

from Game.FactoryGame.Character.Player.BP_RemoteCallObject import BP_RemoteCallObject
from Script.AkAudio import PostAkEvent
from Game.FactoryGame.Buildable.Factory.ResourceSink.UI.BPW_ResourceSink import ExecuteUbergraph_BPW_ResourceSink.K2Node_ComponentBoundEvent_state
from Script.Engine import Delay
from Script.FactoryGame import FGPlayerController
from Script.AkAudio import SetActorRTPCValue
from Script.FactoryGame import GetNumCoupons
from Script.FactoryGame import GetNumPointsToNextCoupon
from Script.Engine import FFloor
from Game.FactoryGame.Buildable.Factory.ResourceSink.UI.BPW_ResourceSink import ExecuteUbergraph_BPW_ResourceSink
from Script.Engine import Conv_IntToFloat
from Script.Engine import Not_PreBool
from Script.Engine import LatentActionInfo
from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import EqualEqual_FloatFloat
from Script.FactoryGame import Get
from Script.Engine import PlayerController
from Script.Engine import Default__KismetArrayLibrary
from Script.UMG import PlayAnimation
from Script.UMG import ESlateVisibility
from Script.FactoryGame import FGBuildableResourceSink
from Script.Engine import TimerHandle
from Game.FactoryGame.Buildable.Factory.ResourceSink.UI.BPW_ResourceSink import ExecuteUbergraph_BPW_ResourceSink.K2Node_CustomEvent_numAdded
from Script.FactoryGame import FGInventoryComponent
from Script.FactoryGame import GetCouponInventory
from Script.FactoryGame import IsProductionPaused
from Script.Engine import CurveFloat
from Script.FactoryGame import GetGlobalPointHistory
from Script.Engine import BooleanOR
from Game.FactoryGame.Interface.UI.InGame.Widget_UseableBase import Widget_UseableBase
from Game.FactoryGame.Interface.UI.Audio.Play_UI_ResourceSink_Ticket import Play_UI_ResourceSink_Ticket
from Script.FactoryGame import Default__FGResourceSinkSubsystem
from Script.UMG import WidgetAnimation
from Script.AkAudio import Default__AkGameplayStatics
from Game.FactoryGame.Interface.UI.Audio.Play_UI_ResourceSink_Pling import Play_UI_ResourceSink_Pling
from Game.FactoryGame.Buildable.Factory.ResourceSink.UI.BPW_ResourceSink import ExecuteUbergraph_BPW_ResourceSink.K2Node_CustomEvent_itemClass
from Game.FactoryGame.Buildable.Factory.ResourceSink.UI.BPW_ResourceSink import ExecuteUbergraph_BPW_ResourceSink.K2Node_Event_UpdateTime
from Game.FactoryGame.Interface.UI.HUDHelpers.BPHUDHelpers import Default__BPHUDHelpers
from Script.FactoryGame import GetRemoteCallObjectOfClass
from Script.FactoryGame import FGResourceSinkSubsystem
from Script.Engine import RandomIntegerInRange
from Script.FactoryGame import GetProgressionTowardsNextCoupon
from Script.UMG import UMGSequencePlayer
from Game.FactoryGame.Buildable.Factory.ResourceSink.Build_ResourceSink import Build_ResourceSink
from Script.AkAudio import AkComponent
from Script.Engine import GetFloatValue
from Script.CoreUObject import LinearColor

class BPW_ResourceSink(Widget_UseableBase):
    ProgressBarIdle: Ptr[WidgetAnimation]
    ProgressBarIdle2: Ptr[WidgetAnimation]
    ProgressBarPulse: Ptr[WidgetAnimation]
    mResourceSink: Ptr[FGBuildableResourceSink]
    mResourceSinkSubsystem: Ptr[FGResourceSinkSubsystem]
    mLastAmountOfCoupons: int32
    mTicketTimerValue: float
    mTicketCurveTimer: TimerHandle
    mCouponTicketCurve: Ptr[CurveFloat] = Namespace(AssetPath='/Game/FactoryGame/Buildable/Factory/ResourceSink/UI/Curve_CouponPrint.Curve_CouponPrint')
    mSetCurveValue: float
    mShouldOpenInventory = True
    mUseKeyboard = True
    mUseMouse = True
    mCaptureInput = True
    mRestoreFocusWhenLost = True
    mInputToPassThrough = ['Use']
    mDesiredHorizontalAlignment = 2
    mDesiredVerticalAlignment = 2
    mCustomTickRate = 1
    mCallCustomTickOnConstruct = True
    
    def UpdatePowerWarning(self):
        Variable2: uint8 = 1
        Variable3: uint8 = 3
        ReturnValue1: bool = self.mResourceSink.HasPower()
        Variable1: bool = ReturnValue1
        
        switch = {
            False: Variable3,
            True: Variable2
        }
        self.Widget_Manufacturing_Warning.SetVisibility(switch.get(Variable1, None))
        Variable: uint8 = 1
        Variable1_0: uint8 = 3
        ReturnValue: bool = self.mResourceSink.IsProductionPaused()
        ReturnValue_0: bool = self.mResourceSink.HasPower()
        ReturnValue_1: bool = Not_PreBool(ReturnValue_0)
        ReturnValue_2: bool = BooleanOR(ReturnValue_1, ReturnValue)
        Variable_0: bool = ReturnValue_2
        
        switch_0 = {
            False: Variable1_0,
            True: Variable
        }
        self.mScreenContent.SetVisibility(switch_0.get(Variable_0, None))
    

    def DropInventorySlotStack(self):
        WasStackMoved = False
    

    def UpdateTicketSoundCurve(self):
        ReturnValue: float = self.mTicketTimerValue + 0.05000000074505806
        self.mTicketTimerValue = ReturnValue
        Variable: float = 100
        Variable1: float = 0
        ReturnValue_0: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_1: float = self.mCouponTicketCurve.GetFloatValue(self.mTicketTimerValue)
        ReturnValue_2: bool = EqualEqual_FloatFloat(self.mSetCurveValue, ReturnValue_1)
        Variable_0: bool = ReturnValue_2
        
        switch = {
            False: Variable,
            True: Variable1
        }
        Default__AkGameplayStatics.SetActorRTPCValue("RTPC_ResourceSink_Ticket", switch.get(Variable_0, None), 0, ReturnValue_0)
        ReturnValue_1 = self.mCouponTicketCurve.GetFloatValue(self.mTicketTimerValue)
        self.mSetCurveValue = ReturnValue_1
    

    def IntArrayToFloatArray(self, IntArray: Ref[List[int32]]):
        ExecutionFlow.Push("L465")
        Variable: int32 = 0
        Variable_0: int32 = 0
        
        # Label 51
        ReturnValue: int32 = len(IntArray)
        ReturnValue_0: bool = Variable <= ReturnValue
        if not ReturnValue_0:
            goto('L359')
        Variable_0 = Variable
        ExecutionFlow.Push("L391")
        
        Item = None
        Item = IntArray[Variable_0]
        ReturnValue_1: float = Conv_IntToFloat(Item)
        
        ReturnValue_2: int32 = LocalFloatArray.append(ReturnValue_1)
        goto(ExecutionFlow.Pop())
        # Label 359
        FloatArray = LocalFloatArray
        # End
        # Label 391
        ReturnValue_3: int32 = Variable + 1
        Variable = ReturnValue_3
        goto('L51')
    

    def UpdateStats(self):
        ReturnValue2: int32 = self.mResourceSinkSubsystem.GetNumCoupons()
        self.mAmountOfCoupons.UpdateCounter(ReturnValue2)
        ReturnValue: int32 = self.mResourceSinkSubsystem.GetNumPointsToNextCoupon()
        self.mRemainingPoints.UpdateCounter(ReturnValue)
        ReturnValue1: float = self.mResourceSinkSubsystem.GetProgressionTowardsNextCoupon()
        ReturnValue_0: float = ReturnValue1 * 100
        ReturnValue_1: int32 = FFloor(ReturnValue_0)
        self.mPercentToNextText.UpdateCounter(ReturnValue_1)
        ReturnValue_2: float = self.mResourceSinkSubsystem.GetProgressionTowardsNextCoupon()
        ReturnValue4: int32 = self.mResourceSinkSubsystem.GetNumCoupons()
        ReturnValue2_0: bool = ReturnValue4 > self.mLastAmountOfCoupons
        self.mPercentToNextBar.mSetPercent(ReturnValue_2, ReturnValue2_0)
        ReturnValue_3: int32 = self.mResourceSinkSubsystem.GetNumCoupons()
        ReturnValue_4: bool = ReturnValue_3 > 0
        self.mPrintButton.SetEnabled(ReturnValue_4)
        ReturnValue_5: List[int32] = self.mResourceSinkSubsystem.GetGlobalPointHistory()
        
        FloatArray = None
        self.IntArrayToFloatArray(Ref[ReturnValue_5], Ref[FloatArray])
        
        FloatArray = None
        self.BPW_ResourceSink_Graph.UpdateOrAddGraphLine("Global", "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 812, 'Value': 'p/min'}", LinearColor(R = 0.7835379838943481, G = 0.2917709946632385, B = 0.057805001735687256, A = 1), Ref[FloatArray])
        ReturnValue1_0: int32 = self.mResourceSinkSubsystem.GetNumCoupons()
        ReturnValue1_1: bool = ReturnValue1_0 > self.mLastAmountOfCoupons
        if not ReturnValue1_1:
            goto('L1248')
        ReturnValue3: int32 = self.mResourceSinkSubsystem.GetNumCoupons()
        self.mLastAmountOfCoupons = ReturnValue3
        self.mProgressBarShine.PlayShineAnim()
        ReturnValue_6: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.ProgressBarPulse, 0, 1, 0, 1)
        ReturnValue_7: int32 = RandomIntegerInRange(25, 30)
        self.Widget_GenericParticleSpawner.CreateParticles(ReturnValue_7)
        # End
        # Label 1248
        ReturnValue3 = self.mResourceSinkSubsystem.GetNumCoupons()
        self.mLastAmountOfCoupons = ReturnValue3
    

    def Cleanup(self):
        self.Widget_Window_DarkMode.OnClose.Clear()
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        
        RCO = None
        Default__BPHUDHelpers.GetDefaultRCO(ReturnValue, self, Ref[RCO])
        RCO.Server_ReturnUnclaimedCoupons(self.mResourceSink)
    

    def Destruct(self):
        self.ExecuteUbergraph_BPW_ResourceSink(2130)
    

    def BndEvt__Widget_GlowingFactoryButton_K2Node_ComponentBoundEvent_0_OnClicked__DelegateSignature(self):
        self.ExecuteUbergraph_BPW_ResourceSink(69)
    

    def BndEvt__BPW_ResourceSinkCoupon_K2Node_ComponentBoundEvent_1_OnPrintCompleted__DelegateSignature(self):
        self.ExecuteUbergraph_BPW_ResourceSink(527)
    

    def OnCustomTick(self):
        ExecuteUbergraph_BPW_ResourceSink.K2Node_Event_UpdateTime = UpdateTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BPW_ResourceSink(695)
    

    def BndEvt__BPW_ResourceSinkCoupon_K2Node_ComponentBoundEvent_2_OnPrintPaused__DelegateSignature(self):
        self.ExecuteUbergraph_BPW_ResourceSink(700)
    

    def OnItemAddedToInventory(self, ItemClass: TSubclassOf[FGItemDescriptor], numAdded: int32):
        ExecuteUbergraph_BPW_ResourceSink.K2Node_CustomEvent_itemClass = ItemClass #  PERSISTENT_FRAME(
        ExecuteUbergraph_BPW_ResourceSink.K2Node_CustomEvent_numAdded = numAdded #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BPW_ResourceSink(1449)
    

    def Construct(self):
        self.ExecuteUbergraph_BPW_ResourceSink(1718)
    

    def BndEvt__mResourceSink_K2Node_ComponentBoundEvent_3_BuildingStateChanged__DelegateSignature(self, State: bool):
        ExecuteUbergraph_BPW_ResourceSink.K2Node_ComponentBoundEvent_state = State #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BPW_ResourceSink(1723)
    

    def BndEvt__Widget_StandbyButton_K2Node_ComponentBoundEvent_4_OnStandbyClicked__DelegateSignature(self):
        self.ExecuteUbergraph_BPW_ResourceSink(1738)
    

    def ExecuteUbergraph_BPW_ResourceSink(self):
        goto(ComputedJump("EntryPoint"))
        self.mLed.SetVisibility(2)
        goto(ExecutionFlow.Pop())
        # Label 54
        self.UpdateStats()
        goto(ExecutionFlow.Pop())
        ReturnValue1: Ptr[PlayerController] = self.GetOwningPlayer()
        
        RCO = None
        Default__BPHUDHelpers.GetDefaultRCO(ReturnValue1, self, Ref[RCO])
        ReturnValue4: int32 = self.mResourceSinkSubsystem.GetNumCoupons()
        RCO.Server_ClaimCoupons(self.mResourceSink, ReturnValue4)
        ReturnValue2: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_UI_ResourceSink_Ticket, ReturnValue2, True)
        goto(ExecutionFlow.Pop())
        # Label 338
        self.mPrintedCoupon.PrintCoupon()
        self.mPrintButton.SetEnabled(False)
        self.mLed.SetVisibility(3)
        ReturnValue3: int32 = self.mResourceSinkSubsystem.GetNumCoupons()
        self.mLastAmountOfCoupons = ReturnValue3
        goto(ExecutionFlow.Pop())
        self.mLed.SetVisibility(2)
        ReturnValue2_0: int32 = self.mResourceSinkSubsystem.GetNumCoupons()
        ReturnValue_0: bool = ReturnValue2_0 > 0
        self.mPrintButton.SetEnabled(ReturnValue_0)
        goto(ExecutionFlow.Pop())
        goto('L54')
        ReturnValue3_0: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue1_0: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_UI_ResourceSink_Pling, ReturnValue3_0, True)
        Default__KismetSystemLibrary.Delay(self, 0.20000000298023224, LatentActionInfo(Linkage = 15, UUID = 2001196783, ExecutionFunction = "ExecuteUbergraph_BPW_ResourceSink", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        # Label 862
        ReturnValue_1: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_2: Ptr[FGResourceSinkSubsystem] = Default__FGResourceSinkSubsystem.Get(ReturnValue_1)
        self.mResourceSinkSubsystem = ReturnValue_2
        ReturnValue_3: int32 = self.mResourceSinkSubsystem.GetNumCoupons()
        self.mLastAmountOfCoupons = ReturnValue_3
        ReturnValue_4: Ptr[FGInventoryComponent] = self.mResourceSink.GetCouponInventory()
        self.mPrintedCoupon.InitInventorySlot(ReturnValue_4)
        OutputDelegate1.BindUFunction(self, OnInventorySlotStackMove)
        self.mPrintedCoupon.mCouponSlot.OnMoveStack.AddUnique(OutputDelegate1)
        ReturnValue_5: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.ProgressBarIdle, 0, 0, 0, 1)
        ReturnValue1_1: int32 = self.mResourceSinkSubsystem.GetNumCoupons()
        self.mAmountOfCoupons.UpdateCounter(ReturnValue1_1)
        self.UpdatePowerWarning()
        ReturnValue1_2: bool = self.mResourceSink.IsProductionPaused()
        self.Widget_StandbyButton.SetStandbyButtonBrush(ReturnValue1_2)
        goto(ExecutionFlow.Pop())
        goto('L338')
        # Label 1454
        OutputDelegate.BindUFunction(self, OnItemAddedToInventory)
        ReturnValue1_3: Ptr[FGInventoryComponent] = self.mResourceSink.GetCouponInventory()
        ReturnValue1_3.OnItemAddedDelegate.AddUnique(OutputDelegate)
        OutputDelegate2.BindUFunction(self, OnEscapePressed)
        self.Widget_Window_DarkMode.OnClose.AddUnique(OutputDelegate2)
        goto('L862')
        # Label 1629
        Sink: Ptr[Build_ResourceSink] = Cast[Build_ResourceSink](self.mInteractObject)
        bSuccess: bool = Sink
        self.mResourceSink = Sink
        goto('L1454')
        goto('L1629')
        self.UpdatePowerWarning()
        goto(ExecutionFlow.Pop())
        ReturnValue4_0: Ptr[PlayerController] = self.GetOwningPlayer()
        Controller: Ptr[FGPlayerController] = Cast[FGPlayerController](ReturnValue4_0)
        bSuccess1: bool = Controller
        if not bSuccess1:
           goto(ExecutionFlow.Pop())
        ReturnValue_6: Ptr[BP_RemoteCallObject] = Controller.GetRemoteCallObjectOfClass(BP_RemoteCallObject)
        ReturnValue_7: bool = self.mResourceSink.IsProductionPaused()
        ReturnValue_8: bool = Not_PreBool(ReturnValue_7)
        ReturnValue_6.Server_SetIsProductionPausedOnFactory(self.mResourceSink, ReturnValue_8)
        ReturnValue_7 = self.mResourceSink.IsProductionPaused()
        self.Widget_StandbyButton.SetStandbyButtonBrush(ReturnValue_7)
        self.UpdatePowerWarning()
        goto(ExecutionFlow.Pop())
        # Label 2115
        self.Cleanup()
        goto(ExecutionFlow.Pop())
        goto('L2115')
    
