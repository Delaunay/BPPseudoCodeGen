
from codegen.ue4_stub import *

from Script.Engine import Texture
from Script.Engine import Conv_IntToFloat
from Script.Engine import Ease
from Game.FactoryGame.Interface.UI.InGame.-Shared.Widget_GenericParticle import ExecuteUbergraph_Widget_GenericParticle.K2Node_Event_InDeltaTime
from Script.UMG import SetRenderScale
from Script.UMG import SetRenderTranslation
from Game.FactoryGame.Interface.UI.InGame.-Shared.Widget_GenericParticle import ExecuteUbergraph_Widget_GenericParticle.K2Node_Event_MyGeometry
from Script.UMG import SetBrushSize
from Script.Engine import BreakVector2D
from Game.FactoryGame.Interface.UI.InGame.-Shared.Widget_GenericParticle import ExecuteUbergraph_Widget_GenericParticle
from Script.UMG import SetRenderAngle
from Script.Engine import LinearColorLerp
from Script.UMG import UserWidget
from Script.Engine import RandomIntegerInRange
from Script.UMG import SetBrushTintColor
from Script.CoreUObject import Vector2D
from Script.UMG import SetRenderOpacity
from Script.CoreUObject import LinearColor
from Script.Engine import RandomFloatInRange

class Widget_GenericParticle(UserWidget):
    mParticleTexture: Ptr[Texture] = Namespace(AssetPath='/Game/FactoryGame/Interface/UI/Assets/Shared/0_White.0_White')
    mParticleSize: Vector2D
    mSpeed: float
    mMaxDistance: Vector2D
    mTargetPosition: Vector2D
    mParticleScale: Vector2D
    mStartTint: LinearColor = Namespace(A=0, B=0.8566930294036865, G=0, R=1)
    mEndTint: LinearColor
    T: float
    CurrentPosition: Vector2D
    mRotation: float
    mMinRot: float
    mMaxRot: float
    
    def Construct(self):
        self.ExecuteUbergraph_Widget_GenericParticle(10)
    

    def Tick(self):
        ExecuteUbergraph_Widget_GenericParticle.K2Node_Event_MyGeometry = MyGeometry #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_GenericParticle.K2Node_Event_InDeltaTime = InDeltaTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_GenericParticle(1817)
    

    def ExecuteUbergraph_Widget_GenericParticle(self):
        SlateBrush.ImageSize = self.mParticle.Brush.ImageSize
        SlateBrush.Margin = self.mParticle.Brush.Margin
        SlateBrush.TintColor = self.mParticle.Brush.TintColor
        SlateBrush.ResourceObject = self.mParticleTexture
        SlateBrush.DrawAs = self.mParticle.Brush.DrawAs
        SlateBrush.Tiling = self.mParticle.Brush.Tiling
        SlateBrush.Mirroring = self.mParticle.Brush.Mirroring
        
        SlateBrush = None
        self.mParticle.SetBrush(Ref[SlateBrush])
        self.mParticle.SetBrushSize(self.mParticleSize)
        ReturnValue: int32 = RandomIntegerInRange(0, 1)
        ReturnValue1: int32 = RandomIntegerInRange(0, 1)
        ReturnValue_0: float = Conv_IntToFloat(ReturnValue)
        ReturnValue1_0: float = Conv_IntToFloat(ReturnValue1)
        
        X1 = None
        Y1 = None
        BreakVector2D(self.mMaxDistance, Ref[X1], Ref[Y1])
        ReturnValue1_1: float = RandomFloatInRange(0, Y1)
        ReturnValue_1: float = ReturnValue1_0 * 2 - 1 * ReturnValue1_1
        ReturnValue2: float = RandomFloatInRange(0, X1)
        ReturnValue1_2: float = ReturnValue_0 * 2 - 1 * ReturnValue2
        ReturnValue2_0: Vector2D = Vector2D(ReturnValue1_2, ReturnValue_1)
        self.mTargetPosition = ReturnValue2_0
        ReturnValue_2: float = RandomFloatInRange(0.800000011920929, 1.2000000476837158)
        ReturnValue1_3: Vector2D = Vector2D(ReturnValue_2, ReturnValue_2)
        self.mParticleScale = ReturnValue1_3
        self.mParticle.SetRenderScale(self.mParticleScale)
        ReturnValue3: float = RandomFloatInRange(0.10000000149011612, self.mRotation)
        ReturnValue2_1: float = ReturnValue3 * -1
        ReturnValue2_2: int32 = RandomIntegerInRange(0, 1)
        Variable: int32 = ReturnValue2_2
        
        switch = {
            0: ReturnValue3,
            1: ReturnValue2_1
        }
        ReturnValue1_4: float = switch.get(Variable, None) / 2
        self.mMinRot = ReturnValue1_4
        ReturnValue3 = RandomFloatInRange(0.10000000149011612, self.mRotation)
        ReturnValue2_1 = ReturnValue3 * -1
        ReturnValue2_2 = RandomIntegerInRange(0, 1)
        Variable = ReturnValue2_2
        
        switch_0 = {
            0: ReturnValue3,
            1: ReturnValue2_1
        }
        ReturnValue1_4 = switch_0.get(Variable, None) / 2
        
        switch_1 = {
            0: ReturnValue3,
            1: ReturnValue2_1
        }
        ReturnValue1_5: float = switch_1.get(Variable, None) + ReturnValue1_4
        self.mMaxRot = ReturnValue1_5
        # End
        ReturnValue_3: float = InDeltaTime / self.mSpeed
        ReturnValue_4: float = ReturnValue_3 + self.T
        self.T = ReturnValue_4
        
        X = None
        Y = None
        BreakVector2D(self.mTargetPosition, Ref[X], Ref[Y])
        ReturnValue_5: float = Ease(0, X, self.T, 6, 5, 2)
        ReturnValue1_6: float = Ease(0, Y, self.T, 6, 5, 2)
        ReturnValue_6: Vector2D = Vector2D(ReturnValue_5, ReturnValue1_6)
        self.CurrentPosition = ReturnValue_6
        ReturnValue4: float = Ease(self.mMinRot, self.mMaxRot, self.T, 6, 3, 2)
        self.mParticle.SetRenderAngle(ReturnValue4)
        self.mParticle.SetRenderTranslation(self.CurrentPosition)
        ReturnValue2_3: float = Ease(0, 1, self.T, 6, 3, 2)
        ReturnValue_7: LinearColor = LinearColorLerp(self.mStartTint, self.mEndTint, ReturnValue2_3)
        SlateColor.SpecifiedColor = ReturnValue_7
        SlateColor.ColorUseRule = 0
        self.mParticle.SetBrushTintColor(SlateColor)
        ReturnValue3_0: float = Ease(1, 0, self.T, 6, 1, 2)
        self.SetRenderOpacity(ReturnValue3_0)
        ReturnValue_8: bool = self.T > 1
        if not ReturnValue_8:
            goto('L2681')
        self.RemoveFromParent()
    
