
from codegen.ue4_stub import *

from Script.Engine import Texture
from Script.Engine import Delay
from Script.Engine import FClamp
from Game.FactoryGame.Interface.UI.InGame.-Shared.Widget_ProgressBar import ExecuteUbergraph_Widget_ProgressBar.K2Node_Event_IsDesignTime
from Script.Engine import LatentActionInfo
from Script.Engine import Ease
from Script.Engine import Default__KismetSystemLibrary
from Game.FactoryGame.Interface.UI.InGame.-Shared.Widget_ProgressBar import ExecuteUbergraph_Widget_ProgressBar.K2Node_CustomEvent_EndValue
from Script.UMG import ESlateVisibility
from Script.UMG import SetPercent
from Script.UMG import SetFillColorAndOpacity
from Game.FactoryGame.Interface.UI.InGame.-Shared.Widget_ProgressBar import ExecuteUbergraph_Widget_ProgressBar.K2Node_CustomEvent_LerpTime
from Script.Engine import LinearColorLerp
from Script.UMG import UserWidget
from Script.UMG import SetBrushColor
from Game.FactoryGame.Interface.UI.HUDHelpers.HUDHelpers import Default__HUDHelpers
from Script.UMG import SetRenderOpacity
from Game.FactoryGame.Interface.UI.InGame.-Shared.Widget_ProgressBar import ExecuteUbergraph_Widget_ProgressBar.K2Node_CustomEvent_StartValue
from Game.FactoryGame.Interface.UI.InGame.-Shared.Widget_ProgressBar import ExecuteUbergraph_Widget_ProgressBar
from Script.Engine import PrintString
from Script.CoreUObject import LinearColor

class Widget_ProgressBar(UserWidget):
    mBorderTint: LinearColor = Namespace(A=1, B=0.09530699998140335, G=0.09530699998140335, R=0.09530699998140335)
    LerpStartValue: float
    LerpEndValue: float
    T: float
    SecondsPerLerpUpdate: float = 0.0010000000474974513
    LerpActive: bool
    mBarTint: LinearColor = Namespace(A=1, B=0.09530699998140335, G=0.09530699998140335, R=0.09530699998140335)
    mIcon: Ptr[Texture]
    mShowIcon: bool
    mUseIconContainer: bool
    
    def SetUseIconContainer(self, mUseIconContainer: bool):
        self.mUseIconContainer = mUseIconContainer
        Variable: uint8 = 3
        Variable1: uint8 = 1
        Variable_0: bool = self.mUseIconContainer
        
        switch = {
            False: Variable1,
            True: Variable
        }
        self.mIconContainer.SetVisibility(switch.get(Variable_0, None))
    

    def SetShowIcon(self, mShowIcon: bool):
        self.mShowIcon = mShowIcon
        Variable: uint8 = 3
        Variable1: uint8 = 2
        Variable1_0: bool = self.mShowIcon
        
        switch = {
            False: Variable1,
            True: Variable
        }
        self.mIconObject.SetVisibility(switch.get(Variable1_0, None))
        Variable_0: float = 1
        Variable1_1: float = 0.5
        Variable_1: bool = self.mShowIcon
        
        switch_0 = {
            False: Variable1_1,
            True: Variable_0
        }
        self.mIconContainer.SetRenderOpacity(switch_0.get(Variable_1, None))
    

    def SetIcon(self, mIcon: Ptr[Texture]):
        self.mIcon = mIcon
        SlateBrush.ImageSize = self.mIconObject.Brush.ImageSize
        SlateBrush.Margin = self.mIconObject.Brush.Margin
        SlateBrush.TintColor = self.mIconObject.Brush.TintColor
        SlateBrush.ResourceObject = self.mIcon
        # Label 248
        SlateBrush.DrawAs = self.mIconObject.Brush.DrawAs
        SlateBrush.Tiling = self.mIconObject.Brush.Tiling
        SlateBrush.Mirroring = self.mIconObject.Brush.Mirroring
        
        SlateBrush = None
        self.mIconObject.SetBrush(Ref[SlateBrush])
    

    def GetCurveType(self):
        Curve = None
    

    def SetProgressBarFillColor(self, InputValue: float):
        ReturnValue: float = FClamp(InputValue, 0, 1)
        
        Text = None
        Graphics = None
        Default__HUDHelpers.GetFactoryGameDarkGray(self, Ref[Text], Ref[Graphics])
        
        Text = None
        Graphics = None
        Default__HUDHelpers.GetFactoryGameLightGray(self, Ref[Text], Ref[Graphics])
        ReturnValue_0: LinearColor = LinearColorLerp(Graphics, Graphics, ReturnValue)
        self.mProgressBar.SetFillColorAndOpacity(ReturnValue_0)
    

    def LerpBar(self, StartValue: float, EndValue: float, LerpTime: float):
        ExecuteUbergraph_Widget_ProgressBar.K2Node_CustomEvent_StartValue = StartValue #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_ProgressBar.K2Node_CustomEvent_EndValue = EndValue #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_ProgressBar.K2Node_CustomEvent_LerpTime = LerpTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_ProgressBar(758)
    

    def PreConstruct(self):
        ExecuteUbergraph_Widget_ProgressBar.K2Node_Event_IsDesignTime = IsDesignTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_ProgressBar(933)
    

    def ExecuteUbergraph_Widget_ProgressBar(self):
        goto(ComputedJump("EntryPoint"))
        ExecutionFlow.Push("L248")
        ReturnValue: float = self.SecondsPerLerpUpdate / LerpTime
        ReturnValue_0: float = self.T + ReturnValue
        self.T = ReturnValue_0
        ReturnValue_1: float = Ease(self.LerpStartValue, self.LerpEndValue, self.T, 6, 2, 2)
        self.mProgressBar.SetPercent(ReturnValue_1)
        goto(ExecutionFlow.Pop())
        # Label 248
        ReturnValue_2: bool = self.T <= 1
        ReturnValue_3: bool = self.LerpActive and ReturnValue_2
        if not ReturnValue_3:
            goto('L415')
        Default__KismetSystemLibrary.Delay(self, self.SecondsPerLerpUpdate, LatentActionInfo(Linkage = 15, UUID = 79583239, ExecutionFunction = "ExecuteUbergraph_Widget_ProgressBar", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        # Label 415
        self.LerpActive = False
        Default__KismetSystemLibrary.PrintString(self, "Completed", True, True, LinearColor(R = 0, G = 0.6600000262260437, B = 1, A = 1), 2)
        goto(ExecutionFlow.Pop())
        # Label 512
        self.SetUseIconContainer(self.mUseIconContainer)
        self.SetShowIcon(self.mShowIcon)
        self.SetIcon(self.mIcon)
        goto(ExecutionFlow.Pop())
        self.LerpActive = True
        Default__KismetSystemLibrary.PrintString(self, "Started", True, True, LinearColor(R = 0, G = 0.6600000262260437, B = 1, A = 1), 2)
        self.LerpStartValue = StartValue
        self.LerpEndValue = EndValue
        self.T = 0
        goto('L248')
        self.LerpActive = False
        Default__KismetSystemLibrary.Delay(self, 0.10000000149011612, LatentActionInfo(Linkage = 582, UUID = 999773456, ExecutionFunction = "ExecuteUbergraph_Widget_ProgressBar", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        # Label 846
        self.Border_0.SetBrushColor(self.mBorderTint)
        self.mProgressBar.SetFillColorAndOpacity(self.mBarTint)
        goto('L512')
        goto('L846')
    
