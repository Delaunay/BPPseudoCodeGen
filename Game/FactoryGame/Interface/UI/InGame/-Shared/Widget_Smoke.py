
from codegen.ue4_stub import *

from Script.UMG import UserWidget
from Script.UMG import UMGSequencePlayer
from Game.FactoryGame.Interface.UI.InGame.-Shared.Widget_Smoke import ExecuteUbergraph_Widget_Smoke
from Script.UMG import PlayAnimation
from Script.Engine import Lerp
from Script.UMG import SetRenderAngle
from Game.FactoryGame.Interface.UI.InGame.-Shared.Widget_Smoke import ExecuteUbergraph_Widget_Smoke.K2Node_Event_MyGeometry
from Script.UMG import BindToAnimationFinished
from Script.UMG import WidgetAnimation
from Game.FactoryGame.Interface.UI.InGame.-Shared.Widget_Smoke import ExecuteUbergraph_Widget_Smoke.K2Node_Event_InDeltaTime
from Game.FactoryGame.Interface.UI.InGame.-Shared.Widget_Smoke import ExecuteUbergraph_Widget_Smoke.K2Node_Event_IsDesignTime
from Script.Engine import RandomFloatInRange

class Widget_Smoke(UserWidget):
    SpawnAnim: Ptr[WidgetAnimation]
    T: float
    Smoke1RotateDeg: float
    Smoke2RotateDeg: float
    Smoke3RotateDeg: float
    TimeMultiplier: float
    Smoke1StartDeg: float
    Smoke2StartDeg: float
    Smoke3StartDeg: float
    
    def Construct(self):
        self.ExecuteUbergraph_Widget_Smoke(10)
    

    def OnAnimEnd(self):
        self.ExecuteUbergraph_Widget_Smoke(116)
    

    def Tick(self):
        ExecuteUbergraph_Widget_Smoke.K2Node_Event_MyGeometry = MyGeometry #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_Smoke.K2Node_Event_InDeltaTime = InDeltaTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_Smoke(135)
    

    def PreConstruct(self):
        ExecuteUbergraph_Widget_Smoke.K2Node_Event_IsDesignTime = IsDesignTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_Smoke(1134)
    

    def ExecuteUbergraph_Widget_Smoke(self):
        ReturnValue: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.SpawnAnim, 0, 1, 0, self.TimeMultiplier)
        OutputDelegate.BindUFunction(self, OnAnimEnd)
        self.BindToAnimationFinished(self.SpawnAnim, OutputDelegate)
        # End
        self.RemoveFromParent()
        # End
        ReturnValue_0: float = InDeltaTime / self.TimeMultiplier
        ReturnValue_1: float = ReturnValue_0 + self.T
        self.T = ReturnValue_1
        ReturnValue_2: float = Lerp(0, 1, self.T)
        ReturnValue1: float = self.Smoke1RotateDeg * ReturnValue_2
        ReturnValue1_0: float = self.Smoke1StartDeg + ReturnValue1
        self.Smoke_1.SetRenderAngle(ReturnValue1_0)
        ReturnValue_2 = Lerp(0, 1, self.T)
        ReturnValue2: float = self.Smoke2RotateDeg * ReturnValue_2
        ReturnValue2_0: float = self.Smoke2StartDeg + ReturnValue2
        self.Smoke_2.SetRenderAngle(ReturnValue2_0)
        ReturnValue_2 = Lerp(0, 1, self.T)
        ReturnValue_3: float = self.Smoke3RotateDeg * ReturnValue_2
        ReturnValue3: float = self.Smoke3StartDeg + ReturnValue_3
        self.Smoke_3.SetRenderAngle(ReturnValue3)
        # End
        # Label 799
        ReturnValue_4: float = RandomFloatInRange(-15, 15)
        self.Smoke3RotateDeg = ReturnValue_4
        ReturnValue4: float = RandomFloatInRange(0, 360)
        self.Smoke1StartDeg = ReturnValue4
        ReturnValue5: float = RandomFloatInRange(0, 360)
        self.Smoke2StartDeg = ReturnValue5
        ReturnValue6: float = RandomFloatInRange(0, 360)
        self.Smoke3StartDeg = ReturnValue6
        # End
        # Label 1064
        ReturnValue1_1: float = RandomFloatInRange(-20, 20)
        self.Smoke2RotateDeg = ReturnValue1_1
        goto('L799')
        ReturnValue3_0: float = RandomFloatInRange(0.800000011920929, 1.2000000476837158)
        self.TimeMultiplier = ReturnValue3_0
        ReturnValue2_1: float = RandomFloatInRange(-10, 10)
        self.Smoke1RotateDeg = ReturnValue2_1
        goto('L1064')
    
