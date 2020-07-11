
from codegen.ue4_stub import *

from Script.Engine import Default__KismetSystemLibrary
from Script.FactoryGame import GetFloatCurveValue
from Script.Engine import Lerp
from Script.Engine import K2_SetTimerDelegate
from Game.FactoryGame.Interface.UI.InGame.-Shared.BPW_LerpingProgressBar import ExecuteUbergraph_BPW_LerpingProgressBar
from Script.Engine import TimerHandle
from Game.FactoryGame.Interface.UI.InGame.-Shared.BPW_LerpingProgressBar import ExecuteUbergraph_BPW_LerpingProgressBar.K2Node_Event_IsDesignTime
from Script.Engine import GreaterEqual_FloatFloat
from Script.UMG import SetPercent
from Script.Engine import RuntimeFloatCurve
from Script.FactoryGame import Default__FGSkySphere
from Script.Engine import K2_ClearAndInvalidateTimerHandle
from Script.UMG import UserWidget
from Script.SlateCore import ProgressBarStyle

class BPW_LerpingProgressBar(UserWidget):
    mStyle: ProgressBarStyle = Namespace(BackgroundImage={'ImageSize': {'X': 32, 'Y': 32}, 'Margin': {'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, 'TintColor': {'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, 'ResourceObject': {'$Empty': True}, 'ResourceName': 'None', 'UVRegion': {'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, 'DrawAs': 3, 'Tiling': 0, 'Mirroring': 0, 'ImageType': 0, 'bIsDynamicallyLoaded': False, 'bHasUObject': False}, FillImage={'ImageSize': {'X': 32, 'Y': 32}, 'Margin': {'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, 'TintColor': {'SpecifiedColor': {'R': 0.13286800682544708, 'G': 0.13286800682544708, 'B': 0.13563300669193268, 'A': 1}, 'ColorUseRule': 0}, 'ResourceObject': {'$Empty': True}, 'ResourceName': 'None', 'UVRegion': {'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, 'DrawAs': 3, 'Tiling': 0, 'Mirroring': 0, 'ImageType': 0, 'bIsDynamicallyLoaded': False, 'bHasUObject': False}, MarqueeImage={'ImageSize': {'X': 32, 'Y': 32}, 'Margin': {'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, 'TintColor': {'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, 'ResourceObject': {'$Empty': True}, 'ResourceName': 'None', 'UVRegion': {'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, 'DrawAs': 3, 'Tiling': 0, 'Mirroring': 0, 'ImageType': 0, 'bIsDynamicallyLoaded': False, 'bHasUObject': False})
    mLerpDuration: float = 0.30000001192092896
    mLerpUpdateTime: float = 0.009999999776482582
    mStartPercentage: float
    mLerpT: float
    mCurve: RuntimeFloatCurve = Namespace(EditorCurveData={'Keys': [{'InterpMode': 2, 'TangentMode': 2, 'TangentWeightMode': 0, 'Time': 0, 'Value': 0, 'ArriveTangent': 0, 'ArriveTangentWeight': 0, 'LeaveTangent': 0, 'LeaveTangentWeight': 0}, {'InterpMode': 2, 'TangentMode': 2, 'TangentWeightMode': 0, 'Time': 1, 'Value': 1, 'ArriveTangent': 0, 'ArriveTangentWeight': 0, 'LeaveTangent': 0, 'LeaveTangentWeight': 0}], 'PreInfinityExtrap': 4, 'PostInfinityExtrap': 4, 'DefaultValue': 3.4028234663852886e+38}, ExternalCurve={'$Empty': True})
    mLastPercent: float
    mNewPercent: float
    mLerpTimerHandle: TimerHandle
    mForceProgressBarWrap: bool
    
    def mSetPercent(self, Percent: float, ForceProgressBarWrap: bool):
        self.mNewPercent = Percent
        self.mForceProgressBarWrap = ForceProgressBarWrap
        self.mLastPercent = self.mProgressBar.Percent
        self.mLerpT = 0
        
        Default__KismetSystemLibrary.K2_ClearAndInvalidateTimerHandle(self, Ref[self.mLerpTimerHandle])
        self.LerpBar()
        OutputDelegate.BindUFunction(self, LerpBar)
        ReturnValue: TimerHandle = Default__KismetSystemLibrary.K2_SetTimerDelegate(OutputDelegate, self.mLerpUpdateTime, True)
        self.mLerpTimerHandle = ReturnValue
    

    def PreConstruct(self):
        ExecuteUbergraph_BPW_LerpingProgressBar.K2Node_Event_IsDesignTime = IsDesignTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BPW_LerpingProgressBar(10)
    

    def LerpBar(self):
        self.ExecuteUbergraph_BPW_LerpingProgressBar(105)
    

    def Destruct(self):
        self.ExecuteUbergraph_BPW_LerpingProgressBar(727)
    

    def ExecuteUbergraph_BPW_LerpingProgressBar(self):
        self.mProgressBar.WidgetStyle = self.mStyle
        self.mProgressBar.SetPercent(self.mStartPercentage)
        # End
        ReturnValue: float = self.mLerpUpdateTime / self.mLerpDuration
        ReturnValue_0: float = self.mLerpT + ReturnValue
        self.mLerpT = ReturnValue_0
        Variable: bool = self.mForceProgressBarWrap
        
        ReturnValue_1: float = Default__FGSkySphere.GetFloatCurveValue(self.mLerpT, Ref[self.mCurve])
        ReturnValue1: float = self.mNewPercent + 1
        
        switch = {
            False: self.mNewPercent,
            True: ReturnValue1
        }
        ReturnValue_2: float = Lerp(self.mLastPercent, switch.get(Variable, None), ReturnValue_1)
        ReturnValue_3: bool = ReturnValue_2 > 1
        ReturnValue_4: float = ReturnValue_2 - 1
        Variable1: bool = ReturnValue_3
        
        switch_0 = {
            False: ReturnValue_2,
            True: ReturnValue_4
        }
        self.mProgressBar.SetPercent(switch_0.get(Variable1, None))
        ReturnValue_5: bool = GreaterEqual_FloatFloat(self.mLerpT, 1)
        if not ReturnValue_5:
            goto('L769')
        
        Default__KismetSystemLibrary.K2_ClearAndInvalidateTimerHandle(self, Ref[self.mLerpTimerHandle])
        # End
        
        Default__KismetSystemLibrary.K2_ClearAndInvalidateTimerHandle(self, Ref[self.mLerpTimerHandle])
    
