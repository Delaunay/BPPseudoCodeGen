
from codegen.ue4_stub import *

from Script.Engine import K2_IsTimerActiveHandle
from Script.FactoryGame import GetFloatCurveValue
from Script.Engine import Delay
from Script.Engine import K2_SetTimerDelegate
from Script.Engine import EqualEqual_ByteByte
from Game.FactoryGame.Interface.UI.InGame.-Shared.Widget_AutoScrollingContainer import ExecuteUbergraph_Widget_AutoScrollingContainer
from Script.Engine import Conv_IntToFloat
from Script.Engine import Not_PreBool
from Script.SlateCore import EOrientation
from Script.UMG import SetOrientation
from Script.Engine import LatentActionInfo
from Script.Engine import Default__KismetSystemLibrary
from Script.UMG import GetChildAt
from Script.UMG import SetRenderTranslation
from Script.UMG import GetLocalSize
from Script.Engine import TimerHandle
from Script.Engine import GreaterEqual_FloatFloat
from Script.Engine import IsValid
from Script.UMG import SetScrollOffset
from Script.UMG import Default__SlateBlueprintLibrary
from Script.Engine import BreakVector2D
from Script.UMG import Widget
from Game.FactoryGame.Interface.UI.InGame.-Shared.Widget_AutoScrollingContainer import ExecuteUbergraph_Widget_AutoScrollingContainer.K2Node_Event_IsDesignTime
from Script.Engine import RuntimeFloatCurve
from Script.FactoryGame import Default__FGSkySphere
from Script.Engine import K2_ClearAndInvalidateTimerHandle
from Script.SlateCore import Geometry
from Script.UMG import UserWidget
from Script.CoreUObject import Vector2D
from Script.Engine import Round
from Script.UMG import ForceLayoutPrepass
from Script.UMG import GetCachedGeometry
from Game.FactoryGame.Interface.UI.InGame.-Shared.Widget_AutoScrollingContainer import ExecuteUbergraph_Widget_AutoScrollingContainer.K2Node_CustomEvent_Seconds_Delayed

class Widget_AutoScrollingContainer(UserWidget):
    mScrollT: float
    mUpdateTime: float = 0.029999999329447746
    mScrollTimer: TimerHandle
    mScrollTime: float = 2
    mOrientation: uint8
    mAutoScrollCurve: RuntimeFloatCurve = Namespace(EditorCurveData={'Keys': [], 'PreInfinityExtrap': 4, 'PostInfinityExtrap': 4, 'DefaultValue': 3.4028234663852886e+38}, ExternalCurve={'$AssetPath': '/Game/FactoryGame/Buildable/-Shared/Curves/AutoScroll_Curve.AutoScroll_Curve'})
    mYOffset: float = 7
    
    def StopAutoScroll(self):
        
        Default__KismetSystemLibrary.K2_ClearAndInvalidateTimerHandle(self, Ref[self.mScrollTimer])
        self.mScrollBox.SetScrollOffset(0)
    

    def StartAutoScroll(self):
        ReturnValue: bool = Default__KismetSystemLibrary.K2_IsTimerActiveHandle(self, self.mScrollTimer)
        ReturnValue_0: bool = Not_PreBool(ReturnValue)
        if not ReturnValue_0:
            goto('L920')
        ReturnValue_1: Ptr[Widget] = self.Content.GetChildAt(0)
        ReturnValue_2: bool = Default__KismetSystemLibrary.IsValid(ReturnValue_1)
        if not ReturnValue_2:
            goto('L920')
        self.ForceLayoutPrepass()
        ReturnValue_3: Const[Geometry] = self.GetCachedGeometry()
        
        ReturnValue_4: Vector2D = Default__SlateBlueprintLibrary.GetLocalSize(Ref[ReturnValue_3])
        
        X = None
        Y = None
        BreakVector2D(ReturnValue_4, Ref[X], Ref[Y])
        Variable: uint8 = self.mOrientation
        ReturnValue1: Const[Geometry] = self.Content.GetCachedGeometry()
        
        ReturnValue1_0: Vector2D = Default__SlateBlueprintLibrary.GetLocalSize(Ref[ReturnValue1])
        
        X1 = None
        Y1 = None
        BreakVector2D(ReturnValue1_0, Ref[X1], Ref[Y1])
        ReturnValue_5: bool = Y1 > Y
        ReturnValue1_1: bool = X1 > X
        
        switch = {
            0: ReturnValue1_1,
            1: ReturnValue_5
        }
        if not switch.get(Variable, None):
            goto('L920')
        self.mScrollT = 0
        OutputDelegate.BindUFunction(self, AutoScroll)
        ReturnValue_6: TimerHandle = Default__KismetSystemLibrary.K2_SetTimerDelegate(OutputDelegate, self.mUpdateTime, True)
        self.mScrollTimer = ReturnValue_6
        ReturnValue_7: bool = EqualEqual_ByteByte(self.mOrientation, 0)
        if not ReturnValue_7:
            goto('L920')
        ReturnValue_8: Vector2D = Vector2D(0, self.mYOffset)
        self.mScrollBox.SetRenderTranslation(ReturnValue_8)
    

    def AutoScroll(self):
        self.ExecuteUbergraph_Widget_AutoScrollingContainer(35)
    

    def BndEvt__mButton_K2Node_ComponentBoundEvent_0_OnButtonHoverEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_AutoScrollingContainer(1067)
    

    def BndEvt__mButton_K2Node_ComponentBoundEvent_1_OnButtonHoverEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_AutoScrollingContainer(1082)
    

    def PreConstruct(self):
        ExecuteUbergraph_Widget_AutoScrollingContainer.K2Node_Event_IsDesignTime = IsDesignTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_AutoScrollingContainer(1097)
    

    def DelayedStartAutoScroll(self, Seconds Delayed: float):
        ExecuteUbergraph_Widget_AutoScrollingContainer.K2Node_CustomEvent_Seconds_Delayed = Seconds Delayed #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_AutoScrollingContainer(1139)
    

    def ExecuteUbergraph_Widget_AutoScrollingContainer(self):
        goto(ComputedJump("EntryPoint"))
        # Label 15
        self.StartAutoScroll()
        goto(ExecutionFlow.Pop())
        goto('L15')
        ReturnValue: float = self.mUpdateTime / self.mScrollTime
        ReturnValue_0: float = ReturnValue + self.mScrollT
        self.mScrollT = ReturnValue_0
        ReturnValue_1: Const[Geometry] = self.Content.GetCachedGeometry()
        
        ReturnValue_2: Vector2D = Default__SlateBlueprintLibrary.GetLocalSize(Ref[ReturnValue_1])
        
        X = None
        Y = None
        BreakVector2D(ReturnValue_2, Ref[X], Ref[Y])
        Variable: uint8 = self.mOrientation
        ReturnValue1: Const[Geometry] = self.GetCachedGeometry()
        
        ReturnValue1_0: Vector2D = Default__SlateBlueprintLibrary.GetLocalSize(Ref[ReturnValue1])
        ReturnValue_3: float = self.mScrollT - 1
        
        X1 = None
        Y1 = None
        BreakVector2D(ReturnValue1_0, Ref[X1], Ref[Y1])
        ReturnValue1_1: float = 1 - ReturnValue_3
        ReturnValue2: float = Y - Y1
        ReturnValue3: float = X - X1
        ReturnValue_4: bool = self.mScrollT > 1
        Variable_0: bool = ReturnValue_4
        
        switch = {
            False: self.mScrollT,
            True: ReturnValue1_1
        }
        
        ReturnValue_5: float = Default__FGSkySphere.GetFloatCurveValue(switch.get(Variable_0, None), Ref[self.mAutoScrollCurve])
        
        switch_0 = {
            0: ReturnValue3,
            1: ReturnValue2
        }
        ReturnValue_6: float = ReturnValue_5 * switch_0.get(Variable, None)
        ReturnValue_7: int32 = Round(ReturnValue_6)
        ReturnValue_8: float = Conv_IntToFloat(ReturnValue_7)
        self.mScrollBox.SetScrollOffset(ReturnValue_8)
        ReturnValue_9: bool = GreaterEqual_FloatFloat(self.mScrollT, 2)
        if not ReturnValue_9:
           goto(ExecutionFlow.Pop())
        self.mScrollT = 0
        goto(ExecutionFlow.Pop())
        self.StartAutoScroll()
        goto(ExecutionFlow.Pop())
        self.StopAutoScroll()
        goto(ExecutionFlow.Pop())
        self.mScrollBox.SetOrientation(self.mOrientation)
        goto(ExecutionFlow.Pop())
        Default__KismetSystemLibrary.Delay(self, Delayed, LatentActionInfo(Linkage = 30, UUID = -8542553, ExecutionFunction = "ExecuteUbergraph_Widget_AutoScrollingContainer", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
    
