
from codegen.ue4_stub import *

from Script.Engine import EqualEqual_FloatFloat
from Game.FactoryGame.Interface.UI.InGame.Widget_BuildGunDelay import ExecuteUbergraph_Widget_BuildGunDelay
from Game.FactoryGame.Equipment.BuildGun.BP_BuildGun import BP_BuildGun
from Script.UMG import ESlateVisibility
from Game.FactoryGame.Interface.UI.InGame.Widget_BuildGunDelay import ExecuteUbergraph_Widget_BuildGunDelay.K2Node_Event_MyGeometry
from Script.FactoryGame import GetCurrentBuildGunDelayPercentage
from Script.UMG import SetPercent
from Game.FactoryGame.Interface.UI.InGame.Widget_BuildGunDelay import ExecuteUbergraph_Widget_BuildGunDelay.K2Node_Event_InDeltaTime
from Script.UMG import UserWidget

class Widget_BuildGunDelay(UserWidget):
    mBuildGun: Ptr[BP_BuildGun]
    mInvertDelay: float = 1
    Visibility = ESlateVisibility::HitTestInvisible
    
    def GetWidgetVisibility(self):
        Variable: uint8 = 2
        Variable1: uint8 = 3
        ReturnValue: float = self.mBuildGun.GetCurrentBuildGunDelayPercentage()
        ReturnValue_0: bool = EqualEqual_FloatFloat(ReturnValue, 0)
        Variable_0: bool = ReturnValue_0
        
        switch = {
            False: Variable1,
            True: Variable
        }
        ReturnValue_1: uint8 = switch.get(Variable_0, None)
    

    def Tick(self):
        ExecuteUbergraph_Widget_BuildGunDelay.K2Node_Event_MyGeometry = MyGeometry #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_BuildGunDelay.K2Node_Event_InDeltaTime = InDeltaTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_BuildGunDelay(10)
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_BuildGunDelay(406)
    

    def ExecuteUbergraph_Widget_BuildGunDelay(self):
        Variable: uint8 = 2
        Variable1: uint8 = 3
        ReturnValue: float = self.mBuildGun.GetCurrentBuildGunDelayPercentage()
        ReturnValue_0: bool = EqualEqual_FloatFloat(ReturnValue, 0)
        Variable_0: bool = ReturnValue_0
        
        switch = {
            False: Variable1,
            True: Variable
        }
        self.mDismantleContainer.SetVisibility(switch.get(Variable_0, None))
        ReturnValue1: float = self.mBuildGun.GetCurrentBuildGunDelayPercentage()
        ReturnValue_1: float = self.mInvertDelay - ReturnValue1
        self.Widget_ProgressBar.mProgressBar.SetPercent(ReturnValue_1)
        # End
    
