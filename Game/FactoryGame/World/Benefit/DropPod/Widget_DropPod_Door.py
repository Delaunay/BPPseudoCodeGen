
from codegen.ue4_stub import *

from Script.AkAudio import PostAkEvent
from Script.Engine import Delay
from Script.Engine import FClamp
from Script.Engine import Pawn
from Game.FactoryGame.World.Benefit.DropPod.Widget_DropPod_Door import ExecuteUbergraph_Widget_DropPod_Door.K2Node_Event_InDeltaTime
from Game.FactoryGame.World.Benefit.DropPod.Audio.UI.Stop_CrashPod_Door_OpenLoop import Stop_CrashPod_Door_OpenLoop
from Game.FactoryGame.World.Benefit.DropPod.Audio.UI.Play_CrashPod_Door_CloseLoopV2 import Play_CrashPod_Door_CloseLoopV2
from Script.Engine import LatentActionInfo
from Script.Engine import Ease
from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import EqualEqual_FloatFloat
from Game.FactoryGame.World.Benefit.DropPod.Audio.UI.Play_CrashPod_Door_Fail import Play_CrashPod_Door_Fail
from Game.FactoryGame.World.Benefit.DropPod.Audio.UI.Stop_CrashPod_Door_CloseLoopV2 import Stop_CrashPod_Door_CloseLoopV2
from Game.FactoryGame.World.Benefit.DropPod.Audio.UI.Play_CrashPod_Door_SlideOpen import Play_CrashPod_Door_SlideOpen
from Script.Engine import GreaterEqual_FloatFloat
from Game.FactoryGame.World.Benefit.DropPod.Widget_DropPod_Door import ExecuteUbergraph_Widget_DropPod_Door.K2Node_ComponentBoundEvent_Value
from Script.UMG import SetValue
from Script.UMG import Destruct
from Script.Engine import CurveFloat
from Script.UMG import SetRenderAngle
from Game.FactoryGame.World.Benefit.DropPod.Widget_DropPod_Door import ExecuteUbergraph_Widget_DropPod_Door
from Script.AkAudio import Default__AkGameplayStatics
from Script.UMG import UserWidget
from Script.UMG import GetOwningPlayerPawn
from Game.FactoryGame.World.Benefit.DropPod.Audio.UI.Play_CrashPod_Door_OpenLoop import Play_CrashPod_Door_OpenLoop
from Game.FactoryGame.World.Benefit.DropPod.Audio.UI.Stop_CrashPod_Door_SlideOpen import Stop_CrashPod_Door_SlideOpen
from Script.AkAudio import AkComponent
from Game.FactoryGame.World.Benefit.DropPod.Widget_DropPod_Door import ExecuteUbergraph_Widget_DropPod_Door.K2Node_Event_MyGeometry
from Script.Engine import GetFloatValue
from Script.UMG import GetValue
from Game.FactoryGame.World.Benefit.DropPod.Audio.UI.Play_CrashPod_Door_Clonk import Play_CrashPod_Door_Clonk

class Widget_DropPod_Door(UserWidget):
    ReturnHandle: bool
    T: float
    LastSliderValue: float
    OnDoorOpen: FMulticastScriptDelegate
    DoorCurve: Ptr[CurveFloat] = Namespace(AssetPath='/Game/FactoryGame/Buildable/-Shared/Curves/DropPodDoor_Curve.DropPodDoor_Curve')
    mDoorOpened: bool
    IsLocked: bool
    NewVar_0: bool
    mCurrentLeverValue: float
    mLastLeverValue: float
    
    def SetHasBeenOpened(self, HasBeenOpened: bool):
        self.mDoorOpened = HasBeenOpened
        if not self.mDoorOpened:
            goto('L52')
        self.SetHandleAngle(-90)
    

    def SetLEDVisibility(self):
        if not self.IsLocked:
            goto('L95')
        self.ledOff.SetVisibility(0)
        # Label 52
        self.ledOn.SetVisibility(2)
        # Label 90
        # End
        # Label 95
        self.ledOff.SetVisibility(2)
        self.ledOn.SetVisibility(0)
        goto('L90')
    

    def SetHandleAngle(self, Angle: float):
        self.DoorHandleBack.SetRenderAngle(Angle)
        self.DoorHandleHighlight.SetRenderAngle(Angle)
        self.DoorHandleTop.SetRenderAngle(Angle)
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_DropPod_Door(297)
    

    def Tick(self):
        ExecuteUbergraph_Widget_DropPod_Door.K2Node_Event_MyGeometry = MyGeometry #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_DropPod_Door.K2Node_Event_InDeltaTime = InDeltaTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_DropPod_Door(340)
    

    def BndEvt__Slider_0_K2Node_ComponentBoundEvent_0_OnFloatValueChangedEvent__DelegateSignature(self, Value: float):
        ExecuteUbergraph_Widget_DropPod_Door.K2Node_ComponentBoundEvent_Value = Value #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_DropPod_Door(764)
    

    def BndEvt__HandleSlider_K2Node_ComponentBoundEvent_1_OnMouseCaptureEndEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_DropPod_Door(2537)
    

    def BndEvt__HandleSlider_K2Node_ComponentBoundEvent_2_OnControllerCaptureEndEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_DropPod_Door(2823)
    

    def OnDoorOpen_Event(self):
        self.ExecuteUbergraph_Widget_DropPod_Door(2828)
    

    def Destruct(self):
        self.ExecuteUbergraph_Widget_DropPod_Door(3078)
    

    def ExecuteUbergraph_Widget_DropPod_Door(self):
        goto(ComputedJump("EntryPoint"))
        Variable1: bool = False
        Variable: bool = True
        goto(ExecutionFlow.Pop())
        # Label 38
        ReturnValue: Ptr[Pawn] = self.GetOwningPlayerPawn()
        ReturnValue_0: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Stop_CrashPod_Door_SlideOpen, ReturnValue, True)
        goto(ExecutionFlow.Pop())
        ReturnValue2: Ptr[Pawn] = self.GetOwningPlayerPawn()
        ReturnValue6: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Stop_CrashPod_Door_CloseLoopV2, ReturnValue2, True)
        ReturnValue2 = self.GetOwningPlayerPawn()
        ReturnValue5: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Stop_CrashPod_Door_OpenLoop, ReturnValue2, True)
        goto(ExecutionFlow.Pop())
        # Label 283
        if not False:
           goto(ExecutionFlow.Pop())
        Variable_0: bool = True
        goto(ExecutionFlow.Pop())
        OutputDelegate.BindUFunction(self, OnDoorOpen_Event)
        self.OnDoorOpen.AddUnique(OutputDelegate)
        goto(ExecutionFlow.Pop())
        if not self.ReturnHandle:
           goto(ExecutionFlow.Pop())
        ReturnValue_1: float = InDeltaTime + self.T
        self.T = ReturnValue_1
        ReturnValue_2: float = FClamp(self.T, 0, 1)
        ReturnValue_3: float = Ease(self.LastSliderValue, 0, ReturnValue_2, 6, 2, 2)
        ReturnValue1: float = ReturnValue_3 * -90
        self.SetHandleAngle(ReturnValue1)
        ReturnValue_2 = FClamp(self.T, 0, 1)
        ReturnValue_3 = Ease(self.LastSliderValue, 0, ReturnValue_2, 6, 2, 2)
        ReturnValue1_0: bool = ReturnValue_3 <= 0
        if not ReturnValue1_0:
           goto(ExecutionFlow.Pop())
        self.ReturnHandle = False
        goto(ExecutionFlow.Pop())
        if not self.mDoorOpened:
            goto('L816')
        self.HandleSlider.SetValue(1)
        goto(ExecutionFlow.Pop())
        # Label 816
        ReturnValue_4: float = self.DoorCurve.GetFloatValue(Value)
        self.HandleSlider.SetValue(ReturnValue_4)
        ReturnValue_4 = self.DoorCurve.GetFloatValue(Value)
        ReturnValue1_1: bool = ReturnValue_4 > 0.05000000074505806
        ReturnValue_5: bool = self.IsLocked and ReturnValue1_1
        if not ReturnValue_5:
            goto('L1327')
        self.HandleSlider.SetValue(0.05000000074505806)
        # Label 1098
        ReturnValue2_0: float = self.HandleSlider.GetValue()
        ReturnValue_6: float = ReturnValue2_0 * -90
        self.SetHandleAngle(ReturnValue_6)
        ReturnValue3: float = self.HandleSlider.GetValue()
        ReturnValue_7: bool = EqualEqual_FloatFloat(ReturnValue3, 1)
        if not ReturnValue_7:
           goto(ExecutionFlow.Pop())
        self.OnDoorOpen.ProcessMulticastDelegate()
        goto(ExecutionFlow.Pop())
        # Label 1327
        ExecutionFlow.Push("L1337")
        goto('L1098')
        # Label 1337
        if not self.IsLocked:
            goto('L1512')
        ReturnValue_4 = self.DoorCurve.GetFloatValue(Value)
        ReturnValue_8: bool = ReturnValue_4 > 0.009999999776482582
        ReturnValue1_2: bool = self.IsLocked and ReturnValue_8
        if not ReturnValue1_2:
           goto(ExecutionFlow.Pop())
        ExecutionFlow.Push("L2076")
        if not Variable:
            goto('L2260')
        goto(ExecutionFlow.Pop())
        # Label 1512
        self.mCurrentLeverValue = Value
        ReturnValue1_3: bool = GreaterEqual_FloatFloat(self.mCurrentLeverValue, self.mLastLeverValue)
        if not ReturnValue1_3:
            goto('L1728')
        ReturnValue1_4: float = self.mLastLeverValue + 0.05000000074505806
        ReturnValue_9: bool = GreaterEqual_FloatFloat(self.mCurrentLeverValue, ReturnValue1_4)
        if not ReturnValue_9:
           goto(ExecutionFlow.Pop())
        self.mLastLeverValue = self.mCurrentLeverValue
        ExecutionFlow.Push("L2285")
        if not Variable2:
            goto('L2496')
        goto(ExecutionFlow.Pop())
        # Label 1728
        ReturnValue_10: float = self.mLastLeverValue - 0.05000000074505806
        ReturnValue_11: bool = self.mCurrentLeverValue <= ReturnValue_10
        if not ReturnValue_11:
           goto(ExecutionFlow.Pop())
        self.mLastLeverValue = self.mCurrentLeverValue
        ExecutionFlow.Push("L1865")
        if not Variable1_0:
            goto('L2521')
        goto(ExecutionFlow.Pop())
        # Label 1865
        if not Variable_0:
            goto('L1880')
        goto(ExecutionFlow.Pop())
        # Label 1880
        Variable_0 = True
        ReturnValue1_5: Ptr[Pawn] = self.GetOwningPlayerPawn()
        ReturnValue4: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_CrashPod_Door_CloseLoopV2, ReturnValue1_5, True)
        ReturnValue1_5 = self.GetOwningPlayerPawn()
        ReturnValue1_6: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Stop_CrashPod_Door_OpenLoop, ReturnValue1_5, True)
        Variable2: bool = False
        Variable2 = True
        goto(ExecutionFlow.Pop())
        # Label 2076
        if not Variable1:
            goto('L2091')
        goto(ExecutionFlow.Pop())
        # Label 2091
        Variable1 = True
        ReturnValue3_0: Ptr[Pawn] = self.GetOwningPlayerPawn()
        ReturnValue9: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_CrashPod_Door_Fail, ReturnValue3_0, True)
        Default__KismetSystemLibrary.Delay(self, 0.5, LatentActionInfo(Linkage = 15, UUID = 1308786644, ExecutionFunction = "ExecuteUbergraph_Widget_DropPod_Door", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        # Label 2260
        Variable = True
        if not False:
           goto(ExecutionFlow.Pop())
        Variable1 = True
        goto(ExecutionFlow.Pop())
        # Label 2285
        if not Variable2:
            goto('L2300')
        goto(ExecutionFlow.Pop())
        # Label 2300
        Variable2 = True
        ReturnValue1_5 = self.GetOwningPlayerPawn()
        ReturnValue3_1: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_CrashPod_Door_OpenLoop, ReturnValue1_5, True)
        ReturnValue1_5 = self.GetOwningPlayerPawn()
        ReturnValue2_1: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Stop_CrashPod_Door_CloseLoopV2, ReturnValue1_5, True)
        Variable_0 = False
        Variable1_0: bool = True
        goto(ExecutionFlow.Pop())
        # Label 2496
        Variable2 = True
        if not False:
           goto(ExecutionFlow.Pop())
        Variable2 = True
        goto(ExecutionFlow.Pop())
        # Label 2521
        Variable1_0 = True
        goto('L283')
        # Label 2537
        ReturnValue_12: float = self.HandleSlider.GetValue()
        ReturnValue_13: bool = ReturnValue_12 <= 1
        if not ReturnValue_13:
            goto('L2784')
        self.T = 0
        ReturnValue1_7: float = self.HandleSlider.GetValue()
        self.LastSliderValue = ReturnValue1_7
        self.ReturnHandle = True
        self.HandleSlider.SetValue(0)
        goto(ExecutionFlow.Pop())
        # Label 2784
        self.HandleSlider.SetVisibility(2)
        goto(ExecutionFlow.Pop())
        goto('L2537')
        self.mDoorOpened = True
        ReturnValue2 = self.GetOwningPlayerPawn()
        ReturnValue8: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_CrashPod_Door_Clonk, ReturnValue2, True)
        ReturnValue2 = self.GetOwningPlayerPawn()
        ReturnValue7: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_CrashPod_Door_SlideOpen, ReturnValue2, True)
        Default__KismetSystemLibrary.Delay(self, 0.20000000298023224, LatentActionInfo(Linkage = 120, UUID = -223500841, ExecutionFunction = "ExecuteUbergraph_Widget_DropPod_Door", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        self.Destruct()
        goto('L38')
    

    def OnDoorOpen__DelegateSignature(self):
        pass
    
