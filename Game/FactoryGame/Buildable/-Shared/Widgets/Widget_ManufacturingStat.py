
from codegen.ue4_stub import *

from Script.Engine import GetEmptyText
from Game.FactoryGame.Buildable.-Shared.Widgets.Widget_ManufacturingStat import ExecuteUbergraph_Widget_ManufacturingStat.K2Node_Event_Operation1
from Script.Engine import K2_SetTimerDelegate
from Game.FactoryGame.Interface.UI.Assets.Shared.cycletime import cycletime
from Game.FactoryGame.Buildable.-Shared.Widgets.Widget_ManufacturingStat import ExecuteUbergraph_Widget_ManufacturingStat.K2Node_Event_MyGeometry
from Script.SlateCore import Margin
from Game.FactoryGame.Buildable.-Shared.Widgets.Widget_ManufacturingStat import ExecuteUbergraph_Widget_ManufacturingStat.K2Node_Event_IsDesignTime
from Script.Engine import Default__KismetSystemLibrary
from Game.FactoryGame.Buildable.-Shared.Widgets.Widget_ManufacturingStat import ExecuteUbergraph_Widget_ManufacturingStat.K2Node_Event_Operation
from Script.Engine import FormatArgumentData
from Script.Engine import Conv_FloatToText
from Script.Engine import TimerHandle
from Script.UMG import SetColorAndOpacity
from Script.Engine import Default__KismetTextLibrary
from Script.CoreUObject import Box2D
from Game.FactoryGame.Buildable.-Shared.Widgets.Widget_ManufacturingStat import ExecuteUbergraph_Widget_ManufacturingStat.K2Node_Event_PointerEvent1
from Script.Engine import Format
from Game.FactoryGame.Buildable.-Shared.Widgets.Widget_ManufacturingStat import ExecuteUbergraph_Widget_ManufacturingStat
from Script.UMG import UserWidget
from Game.FactoryGame.Interface.UI.Assets.BuildMenu.ResIcon_Power import ResIcon_Power
from Game.FactoryGame.Interface.UI.HUDHelpers.HUDHelpers import Default__HUDHelpers
from Script.Engine import EqualEqual_TextText
from Script.Engine import AsPercent_Float
from Script.CoreUObject import Vector2D
from Script.UMG import SetContentColorAndOpacity
from Script.SlateCore import SlateBrush
from Script.SlateCore import SlateColor
from Game.FactoryGame.Buildable.-Shared.Widgets.Widget_ManufacturingStat import ExecuteUbergraph_Widget_ManufacturingStat.K2Node_Event_PointerEvent
from Game.FactoryGame.Interface.UI.Assets.Shared.efficiency import efficiency
from Script.Engine import K2_ClearAndInvalidateTimerHandle
from Script.CoreUObject import LinearColor

class Widget_ManufacturingStat(UserWidget):
    isCycleTime: bool
    isPowerConsumption: bool
    mManufacturingStat: float
    isEfficiency: bool
    mWhiteIcon: bool
    mIconColor: LinearColor = Namespace(A=1, B=0.09530699998140335, G=0.09530699998140335, R=0.09530699998140335)
    mUpdateTimer: TimerHandle
    mCustomSuffix: FText
    
    def SetBrush(self):
        Variable: Const[SlateBrush] = SlateBrush(ImageSize = Vector2D(X = 32, Y = 32), Margin = Margin(Left = 0, Top = 0, Right = 0, Bottom = 0), TintColor = SlateColor(SpecifiedColor = LinearColor(R = 1, G = 1, B = 1, A = 1), ColorUseRule = 0), ResourceObject = None, ResourceName = "None", UVRegion = Box2D(Min = Vector2D(X = 0, Y = 0), Max = Vector2D(X = 0, Y = 0), bIsValid = 0), DrawAs = 3, Tiling = 0, Mirroring = 0, ImageType = 0, bIsDynamicallyLoaded = False, bHasUObject = False)
        SlateBrush.ImageSize = Vector2D(X = 25, Y = 25)
        SlateBrush.Margin = Margin(Left = 0, Top = 0, Right = 0, Bottom = 0)
        SlateBrush.TintColor = SlateColor(SpecifiedColor = LinearColor(R = 1, G = 1, B = 1, A = 1), ColorUseRule = 0)
        SlateBrush.ResourceObject = cycletime
        SlateBrush.DrawAs = 3
        SlateBrush.Tiling = 0
        SlateBrush.Mirroring = 0
        Variable_0: bool = self.isCycleTime
        SlateBrush1.ImageSize = Vector2D(X = 25, Y = 25)
        SlateBrush1.Margin = Margin(Left = 0, Top = 0, Right = 0, Bottom = 0)
        SlateBrush1.TintColor = SlateColor(SpecifiedColor = LinearColor(R = 1, G = 1, B = 1, A = 1), ColorUseRule = 0)
        SlateBrush1.ResourceObject = efficiency
        SlateBrush1.DrawAs = 3
        SlateBrush1.Tiling = 0
        SlateBrush1.Mirroring = 0
        SlateBrush2.ImageSize = Vector2D(X = 25, Y = 25)
        SlateBrush2.Margin = Margin(Left = 0, Top = 0, Right = 0, Bottom = 0)
        SlateBrush2.TintColor = SlateColor(SpecifiedColor = LinearColor(R = 1, G = 1, B = 1, A = 1), ColorUseRule = 0)
        SlateBrush2.ResourceObject = ResIcon_Power
        SlateBrush2.DrawAs = 3
        SlateBrush2.Tiling = 0
        SlateBrush2.Mirroring = 0
        Variable2: bool = self.isPowerConsumption
        Variable1: bool = self.isEfficiency
        
        switch = {
            False: Variable,
            True: SlateBrush1
        }
        
        switch_0 = {
            False: switch.get(Variable1, None),
            True: SlateBrush2
        }
        
        switch_1 = {
            False: switch_0.get(Variable2, None),
            True: SlateBrush
        }
        
        switch_1.get(Variable_0, None) = None
        self.mIcon.SetBrush(Ref[switch_1.get(Variable_0, None)])
    

    def SetIconColor(self):
        if not self.mWhiteIcon:
            goto('L211')
        
        TextWhite1 = None
        GraphicsWhite1 = None
        Default__HUDHelpers.GetFactoryGameWhite(self, Ref[TextWhite1], Ref[GraphicsWhite1])
        self.mIconContainer.SetContentColorAndOpacity(GraphicsWhite1)
        
        TextWhite = None
        GraphicsWhite = None
        Default__HUDHelpers.GetFactoryGameWhite(self, Ref[TextWhite], Ref[GraphicsWhite])
        self.mStatText.SetColorAndOpacity(TextWhite)
        # End
        # Label 211
        self.mIconContainer.SetContentColorAndOpacity(self.mIconColor)
        
        Orange = None
        OrangeText = None
        Default__HUDHelpers.GetFactoryGameOrange(self, Ref[Orange], Ref[OrangeText])
        self.mStatText.SetColorAndOpacity(OrangeText)
    

    def GetStatText(self):
        Variable: FText = 
        ReturnValue: FText = Default__KismetTextLibrary.GetEmptyText()
        ReturnValue_0: FText = Default__KismetTextLibrary.Conv_FloatToText(self.mManufacturingStat, 0, False, True, 1, 4, 0, 1)
        FormatArgumentData.ArgumentName = "value"
        FormatArgumentData.ArgumentValueType = 4
        FormatArgumentData.ArgumentValue = ReturnValue_0
        FormatArgumentData.ArgumentValueInt = 0
        FormatArgumentData.ArgumentValueFloat = 0
        FormatArgumentData.ArgumentValueGender = 0
        FormatArgumentData1.ArgumentName = "suffix"
        FormatArgumentData1.ArgumentValueType = 4
        FormatArgumentData1.ArgumentValue = self.mCustomSuffix
        FormatArgumentData1.ArgumentValueInt = 0
        FormatArgumentData1.ArgumentValueFloat = 0
        FormatArgumentData1.ArgumentValueGender = 0
        
        ReturnValue_1: bool = Default__KismetTextLibrary.EqualEqual_TextText(Ref[ReturnValue], Ref[self.mCustomSuffix])
        Array: List[FormatArgumentData] = [FormatArgumentData, FormatArgumentData1]
        Variable_0: bool = ReturnValue_1
        ReturnValue_2: FText = Default__KismetTextLibrary.Format("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 697, 'Value': '{value} {suffix}'}", Array)
        Variable2: bool = self.isPowerConsumption
        ReturnValue_3: FText = Default__KismetTextLibrary.AsPercent_Float(self.mManufacturingStat, 0, False, True, 1, 4, 0, 0)
        Variable1: bool = self.isEfficiency
        ReturnValue1: FText = Default__KismetTextLibrary.Conv_FloatToText(self.mManufacturingStat, 0, False, True, 1, 4, 0, 1)
        FormatArgumentData2.ArgumentName = "A"
        FormatArgumentData2.ArgumentValueType = 4
        FormatArgumentData2.ArgumentValue = ReturnValue1
        FormatArgumentData2.ArgumentValueInt = 0
        FormatArgumentData2.ArgumentValueFloat = 0
        FormatArgumentData2.ArgumentValueGender = 0
        Array1: List[FormatArgumentData] = [FormatArgumentData2]
        Variable3: bool = self.isCycleTime
        ReturnValue1_0: FText = Default__KismetTextLibrary.Format("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 1207, 'Value': '{A} MW'}", Array1)
        ReturnValue2: FText = Default__KismetTextLibrary.Conv_FloatToText(self.mManufacturingStat, 0, False, True, 1, 4, 0, 1)
        FormatArgumentData3.ArgumentName = "A"
        FormatArgumentData3.ArgumentValueType = 4
        FormatArgumentData3.ArgumentValue = ReturnValue2
        FormatArgumentData3.ArgumentValueInt = 0
        FormatArgumentData3.ArgumentValueFloat = 0
        FormatArgumentData3.ArgumentValueGender = 0
        Array2: List[FormatArgumentData] = [FormatArgumentData3]
        ReturnValue2_0: FText = Default__KismetTextLibrary.Format("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 1603, 'Value': '{A} sec'}", Array2)
        
        switch = {
            False: Variable,
            True: ReturnValue_3
        }
        
        switch_0 = {
            False: switch.get(Variable1, None),
            True: ReturnValue1_0
        }
        
        switch_1 = {
            False: switch_0.get(Variable2, None),
            True: ReturnValue2_0
        }
        
        switch_2 = {
            False: ReturnValue_2,
            True: switch_1.get(Variable3, None)
        }
        ReturnValue_4: FText = switch_2.get(Variable_0, None)
    

    def PreConstruct(self):
        ExecuteUbergraph_Widget_ManufacturingStat.K2Node_Event_IsDesignTime = IsDesignTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_ManufacturingStat(144)
    

    def OnDragEnter(self):
        ExecuteUbergraph_Widget_ManufacturingStat.K2Node_Event_MyGeometry = MyGeometry #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_ManufacturingStat.K2Node_Event_PointerEvent1 = PointerEvent #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_ManufacturingStat.K2Node_Event_Operation1 = Operation #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_ManufacturingStat(177)
    

    def OnDragLeave(self):
        ExecuteUbergraph_Widget_ManufacturingStat.K2Node_Event_PointerEvent = PointerEvent #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_ManufacturingStat.K2Node_Event_Operation = Operation #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_ManufacturingStat(198)
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_ManufacturingStat(219)
    

    def UpdateStat(self):
        self.ExecuteUbergraph_Widget_ManufacturingStat(224)
    

    def Destruct(self):
        self.ExecuteUbergraph_Widget_ManufacturingStat(306)
    

    def ExecuteUbergraph_Widget_ManufacturingStat(self):
        # Label 10
        self.UpdateStat()
        OutputDelegate.BindUFunction(self, UpdateStat)
        ReturnValue: TimerHandle = Default__KismetSystemLibrary.K2_SetTimerDelegate(OutputDelegate, 0.5, True)
        self.mUpdateTimer = ReturnValue
        # End
        self.SetIconColor()
        self.SetBrush()
        # End
        self.SetVisibility(3)
        # End
        self.SetVisibility(4)
        # End
        goto('L10')
        ReturnValue_0: FText = self.GetStatText()
        self.mStatText.SetText(ReturnValue_0)
        # End
        
        Default__KismetSystemLibrary.K2_ClearAndInvalidateTimerHandle(self, Ref[self.mUpdateTimer])
    
