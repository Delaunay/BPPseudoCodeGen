
from codegen.ue4_stub import *

from Script.Engine import Conv_IntToFloat
from Script.Engine import Not_PreBool
from Script.Engine import Ease
from Script.UMG import SetRenderScale
from Script.UMG import SetRenderTranslation
from Game.FactoryGame.Interface.UI.InGame.-Shared.Widget_Sparks import ExecuteUbergraph_Widget_Sparks.K2Node_Event_InDeltaTime
from Game.FactoryGame.Interface.UI.InGame.-Shared.Widget_Sparks import ExecuteUbergraph_Widget_Sparks.K2Node_Event_MyGeometry
from Script.Engine import BreakVector2D
from Script.Engine import LinearColorLerp
from Script.UMG import UserWidget
from Script.Engine import RandomIntegerInRange
from Script.UMG import SetBrushTintColor
from Script.CoreUObject import Vector2D
from Script.UMG import SetContentColorAndOpacity
from Game.FactoryGame.Interface.UI.InGame.-Shared.Widget_Sparks import ExecuteUbergraph_Widget_Sparks
from Script.Engine import EqualEqual_Vector2DVector2D
from Game.FactoryGame.Interface.UI.InGame.-Shared.Widget_Sparks import ExecuteUbergraph_Widget_Sparks.K2Node_Event_IsDesignTime
from Script.CoreUObject import LinearColor
from Script.Engine import RandomFloatInRange

class Widget_Sparks(UserWidget):
    T: float
    TargetPosition: Vector2D
    TintValue: float
    mTopBorderPos: float = -48
    CurrentPosition: Vector2D
    OnParticleBounce: FMulticastScriptDelegate
    SparkScale: Vector2D
    mBounceOn: bool = True
    mMaxDistance: Vector2D = Namespace(X=200, Y=150)
    mSpeed: float = 0.699999988079071
    
    def Tick(self):
        ExecuteUbergraph_Widget_Sparks.K2Node_Event_MyGeometry = MyGeometry #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_Sparks.K2Node_Event_InDeltaTime = InDeltaTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_Sparks(2507)
    

    def PreConstruct(self):
        ExecuteUbergraph_Widget_Sparks.K2Node_Event_IsDesignTime = IsDesignTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_Sparks(2994)
    

    def ExecuteUbergraph_Widget_Sparks(self):
        goto(ComputedJump("EntryPoint"))
        # Label 15
        self.mSpeed = 0.699999988079071
        # Label 38
        ReturnValue: bool = EqualEqual_Vector2DVector2D(self.mMaxDistance, Vector2D(X = 0, Y = 0), 9.999999747378752e-05)
        ReturnValue_0: bool = Not_PreBool(ReturnValue)
        if not ReturnValue_0:
            goto('L853')
        # Label 139
        ReturnValue_1: int32 = RandomIntegerInRange(0, 1)
        ReturnValue_2: float = Conv_IntToFloat(ReturnValue_1)
        ReturnValue1: int32 = RandomIntegerInRange(0, 1)
        ReturnValue1_0: float = Conv_IntToFloat(ReturnValue1)
        
        X4 = None
        Y4 = None
        BreakVector2D(self.mMaxDistance, Ref[X4], Ref[Y4])
        ReturnValue2: float = RandomFloatInRange(0, Y4)
        ReturnValue3: float = RandomFloatInRange(0, X4)
        ReturnValue1_1: float = ReturnValue1_0 * 2 - 1 * ReturnValue2
        ReturnValue2_0: float = ReturnValue_2 * 2 - 1 * ReturnValue3
        ReturnValue3_0: Vector2D = Vector2D(ReturnValue2_0, ReturnValue1_1)
        self.TargetPosition = ReturnValue3_0
        ReturnValue_3: float = RandomFloatInRange(0.10000000149011612, 0.30000001192092896)
        ReturnValue1_2: Vector2D = Vector2D(ReturnValue_3, ReturnValue_3)
        self.SparkScale = ReturnValue1_2
        self.SparkContainer.SetRenderScale(self.SparkScale)
        ReturnValue1_3: float = RandomFloatInRange(0.4000000059604645, 1)
        self.TintValue = ReturnValue1_3
        goto(ExecutionFlow.Pop())
        # Label 853
        self.mMaxDistance = Vector2D(X = 200, Y = 150)
        goto('L139')
        # Label 900
        ExecutionFlow.Push("L1047")
        
        X1 = None
        Y1 = None
        BreakVector2D(self.CurrentPosition, Ref[X1], Ref[Y1])
        ReturnValue_4: bool = Y1 <= self.mTopBorderPos
        ReturnValue_5: bool = ReturnValue_4 and self.mBounceOn
        if not ReturnValue_5:
            goto('L2409')
        if not Variable1:
            goto('L2447')
        goto(ExecutionFlow.Pop())
        
        X2 = None
        Y2 = None
        # Label 1047
        BreakVector2D(self.CurrentPosition, Ref[X2], Ref[Y2])
        
        X3 = None
        Y3 = None
        BreakVector2D(self.CurrentPosition, Ref[X3], Ref[Y3])
        ReturnValue_6: float = self.mTopBorderPos - Y3 + self.mTopBorderPos
        ReturnValue2_1: Vector2D = Vector2D(X2, ReturnValue_6)
        self.CurrentPosition = ReturnValue2_1
        # Label 1259
        self.SparkContainer.SetRenderTranslation(self.CurrentPosition)
        ReturnValue2_2: float = Ease(0, 1, self.T, 6, 3, 2)
        ReturnValue2_3: LinearColor = LinearColorLerp(LinearColor(R = 1, G = 0.8375049829483032, B = 0, A = 1), LinearColor(R = 0.6979169845581055, G = 0.25804299116134644, B = 0, A = 1), ReturnValue2_2)
        SlateColor2.SpecifiedColor = ReturnValue2_3
        SlateColor2.ColorUseRule = 0
        self.BackSpark.SetBrushTintColor(SlateColor2)
        ReturnValue2_2 = Ease(0, 1, self.T, 6, 3, 2)
        ReturnValue1_4: LinearColor = LinearColorLerp(LinearColor(R = 1, G = 1, B = 1, A = 1), LinearColor(R = 0.6979169845581055, G = 0.6965939998626709, B = 0, A = 1), ReturnValue2_2)
        SlateColor1.SpecifiedColor = ReturnValue1_4
        SlateColor1.ColorUseRule = 0
        self.FrontSpark.SetBrushTintColor(SlateColor1)
        ReturnValue2_2 = Ease(0, 1, self.T, 6, 3, 2)
        ReturnValue_7: LinearColor = LinearColorLerp(LinearColor(R = 0.7019609808921814, G = 0.645238995552063, B = 0.39485299587249756, A = 1), LinearColor(R = 0.7019609808921814, G = 0.35612499713897705, B = 0, A = 0), ReturnValue2_2)
        SlateColor.SpecifiedColor = ReturnValue_7
        SlateColor.ColorUseRule = 0
        self.Glow.SetBrushTintColor(SlateColor)
        ReturnValue3_1: float = Ease(1, 0, self.T, 6, 1, 2)
        LinearColor.R = 1
        LinearColor.G = self.TintValue
        LinearColor.B = self.TintValue
        LinearColor.A = ReturnValue3_1
        self.TintBorder.SetContentColorAndOpacity(LinearColor)
        ReturnValue_8: bool = self.T > 1
        if not ReturnValue_8:
           goto(ExecutionFlow.Pop())
        self.RemoveFromParent()
        goto(ExecutionFlow.Pop())
        # Label 2409
        Variable1: bool = False
        if not Variable:
            goto('L2435')
        goto(ExecutionFlow.Pop())
        # Label 2435
        Variable: bool = True
        goto(ExecutionFlow.Pop())
        # Label 2447
        Variable1 = True
        Variable = False
        self.OnParticleBounce.ProcessMulticastDelegate(self.CurrentPosition, self.SparkScale)
        goto(ExecutionFlow.Pop())
        ReturnValue_9: float = InDeltaTime / self.mSpeed
        ReturnValue_10: float = ReturnValue_9 + self.T
        self.T = ReturnValue_10
        
        X = None
        Y = None
        BreakVector2D(self.TargetPosition, Ref[X], Ref[Y])
        ReturnValue_11: float = Ease(0, X, self.T, 6, 5, 2)
        ReturnValue1_5: float = Ease(0, Y, self.T, 6, 5, 2)
        ReturnValue_12: Vector2D = Vector2D(ReturnValue_11, ReturnValue1_5)
        self.CurrentPosition = ReturnValue_12
        
        X1 = None
        Y1 = None
        BreakVector2D(self.CurrentPosition, Ref[X1], Ref[Y1])
        ReturnValue_4 = Y1 <= self.mTopBorderPos
        ReturnValue_5 = ReturnValue_4 and self.mBounceOn
        if not ReturnValue_5:
            goto('L1259')
        goto('L900')
        ReturnValue_13: bool = self.mSpeed <= 0
        ReturnValue1_6: bool = Not_PreBool(ReturnValue_13)
        if not ReturnValue1_6:
            goto('L15')
        goto('L38')
    

    def OnParticleBounce__DelegateSignature(self, Position: Vector2D, Scale: Vector2D):
        pass
    
