
from codegen.ue4_stub import *

from Script.Engine import SetScalarParameterValue
from Script.UMG import UserWidget
from Script.Engine import MaterialInstanceDynamic
from Script.UMG import GetDynamicMaterial
from Game.FactoryGame.Buildable.Factory.RadarTower.UI.Widget_RadarTower_ScanLine import ExecuteUbergraph_Widget_RadarTower_ScanLine.K2Node_Event_IsDesignTime
from Game.FactoryGame.Buildable.Factory.RadarTower.UI.Widget_RadarTower_ScanLine import ExecuteUbergraph_Widget_RadarTower_ScanLine

class Widget_RadarTower_ScanLine(UserWidget):
    mMaxSize: float
    mNormalizedRadius: float
    
    def SetupScanline(self, MaxSize: float, NormalizedRadius: float):
        self.mMaxSize = MaxSize
        self.mNormalizedRadius = NormalizedRadius
        ReturnValue: Ptr[MaterialInstanceDynamic] = self.mCircle.GetDynamicMaterial()
        ReturnValue.SetScalarParameterValue("MaxSize", self.mMaxSize)
        ReturnValue.SetScalarParameterValue("NormalizedRadius", self.mNormalizedRadius)
    

    def PreConstruct(self):
        ExecuteUbergraph_Widget_RadarTower_ScanLine.K2Node_Event_IsDesignTime = IsDesignTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_RadarTower_ScanLine(10)
    

    def ExecuteUbergraph_Widget_RadarTower_ScanLine(self):
        self.SetupScanline(self.mMaxSize, self.mNormalizedRadius)
    
