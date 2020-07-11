
from codegen.ue4_stub import *

from Script.Engine import Default__KismetSystemLibrary
from Game.FactoryGame.Interface.UI.InGame.-Shared.Widget_AnalougeMeter import ExecuteUbergraph_Widget_AnalougeMeter.K2Node_Event_IsDesignTime
from Script.Engine import Texture
from Script.FactoryGame import GetFloatCurveValue
from Script.Engine import FClamp
from Script.Engine import K2_SetTimerDelegate
from Script.UMG import SetRenderAngle
from Script.Engine import Ease
from Script.Engine import TimerHandle
from Script.Engine import GreaterEqual_FloatFloat
from Script.Engine import RuntimeFloatCurve
from Script.FactoryGame import Default__FGSkySphere
from Script.Engine import K2_ClearAndInvalidateTimerHandle
from Script.UMG import SetColorAndOpacity
from Script.UMG import UserWidget
from Script.CoreUObject import LinearColor
from Game.FactoryGame.Interface.UI.InGame.-Shared.Widget_AnalougeMeter import ExecuteUbergraph_Widget_AnalougeMeter

class Widget_AnalougeMeter(UserWidget):
    mValuesImage: Ptr[Texture] = Namespace(AssetPath='/Game/FactoryGame/Interface/UI/Assets/AnalougeMeter/AnalougeMeter_Temperature.AnalougeMeter_Temperature')
    mIndicatorColor: LinearColor = Namespace(A=1, B=0.16601599752902985, G=0.17041200399398804, R=0.796875)
    mValue: float
    mStartValue: float
    mLerpT: float
    mUpdateTime: float = 0.029999999329447746
    mLerpDuration: float = 0.5
    LerpTimer: TimerHandle
    mWobbleT: float
    mWobbleDuration: float = 2
    mWobbleCurve: RuntimeFloatCurve = Namespace(EditorCurveData={'Keys': [], 'PreInfinityExtrap': 4, 'PostInfinityExtrap': 4, 'DefaultValue': 3.4028234663852886e+38}, ExternalCurve={'$AssetPath': '/Game/FactoryGame/Buildable/-Shared/Curves/AnalougeMeterWobble_Curve.AnalougeMeterWobble_Curve'})
    WobbleTimer: TimerHandle
    
    def SetValue(self, Value: float):
        self.mValue = Value
        ReturnValue: float = self.mIndicator.RenderTransform.Angle / 268
        ReturnValue_0: float = ReturnValue + 0.5
        self.mStartValue = ReturnValue_0
        self.mLerpT = 0
        
        Default__KismetSystemLibrary.K2_ClearAndInvalidateTimerHandle(self, Ref[self.WobbleTimer])
        
        Default__KismetSystemLibrary.K2_ClearAndInvalidateTimerHandle(self, Ref[self.LerpTimer])
        OutputDelegate.BindUFunction(self, LerpMeter)
        ReturnValue_1: TimerHandle = Default__KismetSystemLibrary.K2_SetTimerDelegate(OutputDelegate, self.mUpdateTime, True)
        self.LerpTimer = ReturnValue_1
    

    def PreConstruct(self):
        ExecuteUbergraph_Widget_AnalougeMeter.K2Node_Event_IsDesignTime = IsDesignTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_AnalougeMeter(57)
    

    def LerpMeter(self):
        self.ExecuteUbergraph_Widget_AnalougeMeter(638)
    

    def Wobble(self):
        self.ExecuteUbergraph_Widget_AnalougeMeter(1204)
    

    def Destruct(self):
        self.ExecuteUbergraph_Widget_AnalougeMeter(1898)
    

    def ExecuteUbergraph_Widget_AnalougeMeter(self):
        
        # Label 10
        Default__KismetSystemLibrary.K2_ClearAndInvalidateTimerHandle(self, Ref[self.LerpTimer])
        # End
        SlateBrush.ImageSize = self.mValuesImageObject.Brush.ImageSize
        SlateBrush.Margin = self.mValuesImageObject.Brush.Margin
        SlateBrush.TintColor = self.mValuesImageObject.Brush.TintColor
        SlateBrush.ResourceObject = self.mValuesImage
        SlateBrush.DrawAs = self.mValuesImageObject.Brush.DrawAs
        SlateBrush.Tiling = self.mValuesImageObject.Brush.Tiling
        SlateBrush.Mirroring = self.mValuesImageObject.Brush.Mirroring
        
        SlateBrush = None
        self.mValuesImageObject.SetBrush(Ref[SlateBrush])
        self.mIndicator.SetColorAndOpacity(self.mIndicatorColor)
        self.mIndicatorShadow.SetColorAndOpacity(self.mIndicatorColor)
        self.SetValue(0)
        # End
        ReturnValue: float = self.mUpdateTime / self.mLerpDuration
        ReturnValue_0: float = ReturnValue + self.mLerpT
        self.mLerpT = ReturnValue_0
        ReturnValue_1: float = Ease(self.mStartValue, self.mValue, self.mLerpT, 7, 2, 2)
        ReturnValue_2: float = ReturnValue_1 - 0.5
        ReturnValue_3: float = ReturnValue_2 * 268
        self.mIndicator.SetRenderAngle(ReturnValue_3)
        self.mIndicatorShadow.SetRenderAngle(ReturnValue_3)
        ReturnValue_4: bool = GreaterEqual_FloatFloat(self.mLerpT, 1)
        if not ReturnValue_4:
            goto('L1945')
        
        Default__KismetSystemLibrary.K2_ClearAndInvalidateTimerHandle(self, Ref[self.LerpTimer])
        OutputDelegate.BindUFunction(self, Wobble)
        ReturnValue_5: TimerHandle = Default__KismetSystemLibrary.K2_SetTimerDelegate(OutputDelegate, self.mUpdateTime, True)
        self.WobbleTimer = ReturnValue_5
        # End
        ReturnValue1: float = self.mUpdateTime / self.mWobbleDuration
        ReturnValue1_0: float = ReturnValue1 + self.mWobbleT
        self.mWobbleT = ReturnValue1_0
        
        ReturnValue_6: float = Default__FGSkySphere.GetFloatCurveValue(self.mWobbleT, Ref[self.mWobbleCurve])
        ReturnValue1_1: float = ReturnValue_6 * 20
        ReturnValue1_2: float = self.mValue - 0.5
        ReturnValue_7: float = FClamp(ReturnValue1_2, 0, 1)
        ReturnValue2: float = ReturnValue_7 * 2
        ReturnValue3: float = ReturnValue1_1 * ReturnValue2
        ReturnValue2_0: float = self.mValue - 0.5
        ReturnValue4: float = ReturnValue2_0 * 268
        ReturnValue2_1: float = ReturnValue3 + ReturnValue4
        self.mIndicator.SetRenderAngle(ReturnValue2_1)
        self.mIndicatorShadow.SetRenderAngle(ReturnValue2_1)
        ReturnValue1_3: bool = GreaterEqual_FloatFloat(self.mWobbleT, 1)
        if not ReturnValue1_3:
            goto('L1945')
        self.mWobbleT = 0
        # End
        
        Default__KismetSystemLibrary.K2_ClearAndInvalidateTimerHandle(self, Ref[self.WobbleTimer])
        goto('L10')
    
